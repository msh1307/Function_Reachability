import idaapi
import idautils

def is_function_reachable(start_ea, target_ea):
    start_func = idaapi.get_func(start_ea)
    target_func = idaapi.get_func(target_ea)

    def get_function_xrefs(func):
        res = []
        for head in idautils.Heads(func.start_ea, func.end_ea):
            for xref in idautils.XrefsFrom(head, 0):
                if xref.type in [idaapi.fl_CN, idaapi.fl_CF, idaapi.fl_JN, idaapi.fl_JF]:
                    res.append(xref.to)
        return res

    visited = set()
    
    def dfs(current_func, path):
        path.append(idaapi.get_func_name(current_func.start_ea))
        if current_func.start_ea == target_func.start_ea:
            return 2
        
        if current_func.start_ea in visited:
            return 0
        
        visited.add(current_func.start_ea)
        f = 0
        for ea in get_function_xrefs(current_func):
            called_func = idaapi.get_func(ea)
            ret = dfs(called_func, path)
            if called_func and ret > 0:
                if ret == 2:
                    print("---TRACE---")
                    print(path[0])
                    for i in path[1:]:
                        print(' -> '+i)
                    print()
                f = 1
            path.pop()
        if f:
            return 1
        else:
            return 0
    
    return dfs(start_func, [])

start_function_name = "apic_mem_write"
target_function_name = "vapic_enable"  
target_ea = idaapi.get_name_ea(idaapi.BADADDR, target_function_name)
start_ea = idaapi.get_name_ea(idaapi.BADADDR, start_function_name)
if is_function_reachable(start_ea, target_ea) != 0:
    print(f'{start_function_name} => {target_function_name} Reachable')
else:
    print(f'{start_function_name} => {target_function_name} Not Reachable')