```
---TRACE---
apic_mem_write
 -> apic_deliver_irq
 -> apic_bus_deliver
 -> apic_set_irq
 -> apic_sync_vapic
 -> address_space_write_rom
 -> invalidate_and_set_dirty
 -> tb_invalidate_phys_range
 -> page_collection_lock
 -> .g_malloc

---TRACE---
apic_mem_write
 -> apic_deliver_irq
 -> apic_bus_deliver
 -> apic_set_irq
 -> apic_sync_vapic
 -> address_space_write_rom
 -> invalidate_and_set_dirty
 -> tb_invalidate_phys_range
 -> page_collection_lock
 -> page_trylock_add
 -> .g_malloc

---TRACE---
apic_mem_write
 -> apic_deliver_irq
 -> apic_bus_deliver
 -> apic_set_irq
 -> apic_sync_vapic
 -> address_space_write_rom
 -> invalidate_and_set_dirty
 -> tb_invalidate_phys_range
 -> page_collection_lock
 -> page_trylock_add
 ... 
 -> .g_malloc

---TRACE---
apic_mem_write
 -> apic_deliver_irq
 -> apic_bus_deliver
 -> apic_set_irq
 -> apic_sync_vapic
 -> address_space_write_rom
 -> invalidate_and_set_dirty
 -> tb_invalidate_phys_range
 -> page_collection_lock
 -> page_trylock_add
 ... 
 -> .g_malloc

---TRACE---
apic_mem_write
 -> apic_deliver_irq
 -> apic_bus_deliver
 -> apic_set_irq
 -> apic_sync_vapic
 -> cpu_physical_memory_rw
 -> flatview_read
 -> flatview_read_continue
 -> kvm_flush_coalesced_mmio_buffer
 -> address_space_write
 -> flatview_write
 -> flatview_write_continue
 -> invalidate_and_set_dirty
 ... 
 -> .g_malloc

---TRACE---
apic_mem_write
 -> apic_deliver_irq
 -> apic_bus_deliver
 -> apic_set_irq
 ... 
 -> .g_malloc

---TRACE---
apic_mem_write
 -> apic_local_deliver
 -> apic_set_irq
 ... 
 -> .g_malloc

---TRACE---
apic_mem_write
 -> apic_sync_vapic
 ... 
 -> .g_malloc

---TRACE---
apic_mem_write
 -> apic_sync_vapic
 ... 
 -> .g_malloc

---TRACE---
apic_mem_write
 -> apic_bus_deliver
 ... 
 -> .g_malloc

---TRACE---
apic_mem_write
 -> cpu_report_tpr_access
 -> apic_handle_tpr_access_report
 -> vapic_report_tpr_access
 -> cpu_memory_rw_debug
 -> invalidate_and_set_dirty
 ... 
 -> .g_malloc

---TRACE---
apic_mem_write
 -> cpu_report_tpr_access
 -> apic_handle_tpr_access_report
 -> vapic_report_tpr_access
 -> qdev_get_machine
 -> object_get_root
 -> object_new_with_type
 -> .g_malloc

---TRACE---
apic_mem_write
 -> cpu_report_tpr_access
 -> apic_handle_tpr_access_report
 -> vapic_report_tpr_access
 -> qdev_get_machine
 -> container_get
 -> object_new
 -> object_new_with_type
 ... 
 -> .g_malloc

---TRACE---
apic_mem_write
 -> cpu_report_tpr_access
 -> apic_handle_tpr_access_report
 -> vapic_report_tpr_access
 -> .g_malloc

---TRACE---
apic_mem_write
 -> ioapic_eoi_broadcast
 -> ioapic_service
 -> qdev_get_machine
 ... 
 -> .g_malloc

---TRACE---
apic_mem_write
 -> ioapic_eoi_broadcast
 -> ioapic_service
 -> address_space_stl_le
 -> invalidate_and_set_dirty
 ... 
 -> .g_malloc

apic_mem_write => .g_malloc Reachable
```
