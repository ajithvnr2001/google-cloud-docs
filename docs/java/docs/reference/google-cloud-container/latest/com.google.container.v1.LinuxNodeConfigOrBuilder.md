---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.LinuxNodeConfigOrBuilder
title: Interface LinuxNodeConfigOrBuilder (2.102.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:42:34.441567+00:00
---

# Interface LinuxNodeConfigOrBuilder (2.102.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.LinuxNodeConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface LinuxNodeConfigOrBuilder (2.102.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.102.0 (latest)  2.98.0  2.97.0  2.96.0  2.94.0  2.91.0  2.90.0  2.88.0  2.86.0  2.85.0  2.84.0  2.83.0  2.81.0  2.79.0  2.78.0  2.77.0  2.76.0  2.75.0  2.73.0  2.71.0  2.70.0  2.67.0  2.66.0  2.65.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.2  2.4.1  2.3.8 
    
    
    public interface LinuxNodeConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsSysctls(String key)
    
    
    public abstract boolean containsSysctls(String key)

The Linux kernel parameters to be applied to the nodes and all pods running on the nodes.

The following parameters are supported.

net.core.busy_poll net.core.busy_read net.core.netdev_max_backlog net.core.rmem_max net.core.rmem_default net.core.wmem_default net.core.wmem_max net.core.optmem_max net.core.somaxconn net.ipv4.neigh.default.gc_thresh1 net.ipv4.neigh.default.gc_thresh2 net.ipv4.neigh.default.gc_thresh3 net.ipv4.tcp_rmem net.ipv4.tcp_wmem net.ipv4.tcp_tw_reuse net.ipv4.tcp_mtu_probing net.ipv4.tcp_max_orphans net.ipv4.tcp_max_tw_buckets net.ipv4.tcp_syn_retries net.ipv4.tcp_ecn net.ipv4.tcp_congestion_control net.netfilter.nf_conntrack_max net.netfilter.nf_conntrack_buckets net.netfilter.nf_conntrack_tcp_timeout_close_wait net.netfilter.nf_conntrack_tcp_timeout_time_wait net.netfilter.nf_conntrack_tcp_timeout_established net.netfilter.nf_conntrack_acct kernel.keys.maxkeys kernel.keys.maxbytes kernel.shmmni kernel.shmmax kernel.shmall kernel.core_pattern kernel.perf_event_paranoid kernel.sched_rt_runtime_us kernel.softlockup_panic kernel.yama.ptrace_scope kernel.kptr_restrict kernel.dmesg_restrict kernel.sysrq fs.aio-max-nr fs.file-max fs.inotify.max_user_instances fs.inotify.max_user_watches fs.nr_open vm.dirty_background_ratio vm.dirty_background_bytes vm.dirty_expire_centisecs vm.dirty_ratio vm.dirty_bytes vm.dirty_writeback_centisecs vm.max_map_count vm.overcommit_memory vm.overcommit_ratio vm.vfs_cache_pressure vm.swappiness vm.watermark_scale_factor vm.min_free_kbytes

`map<string, string> sysctls = 1;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAccurateTimeConfig()
    
    
    public abstract LinuxNodeConfig.AccurateTimeConfig getAccurateTimeConfig()

Optional. The accurate time configuration for the node pool.

` optional .google.container.v1.LinuxNodeConfig.AccurateTimeConfig accurate_time_config = 14 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[LinuxNodeConfig.AccurateTimeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.LinuxNodeConfig.AccurateTimeConfig)` | The accurateTimeConfig.  
  
### getAccurateTimeConfigOrBuilder()
    
    
    public abstract LinuxNodeConfig.AccurateTimeConfigOrBuilder getAccurateTimeConfigOrBuilder()

Optional. The accurate time configuration for the node pool.

` optional .google.container.v1.LinuxNodeConfig.AccurateTimeConfig accurate_time_config = 14 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[LinuxNodeConfig.AccurateTimeConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.LinuxNodeConfig.AccurateTimeConfigOrBuilder)` |   
  
### getCgroupMode()
    
    
    public abstract LinuxNodeConfig.CgroupMode getCgroupMode()

cgroup_mode specifies the cgroup mode to be used on the node.

`.google.container.v1.LinuxNodeConfig.CgroupMode cgroup_mode = 2;`

**Returns**  
---  
**Type** | **Description**  
`[LinuxNodeConfig.CgroupMode](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.LinuxNodeConfig.CgroupMode)` | The cgroupMode.  
  
### getCgroupModeValue()
    
    
    public abstract int getCgroupModeValue()

cgroup_mode specifies the cgroup mode to be used on the node.

`.google.container.v1.LinuxNodeConfig.CgroupMode cgroup_mode = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for cgroupMode.  
  
### getCustomNodeInit()
    
    
    public abstract LinuxNodeConfig.CustomNodeInit getCustomNodeInit()

Optional. Allow users to run arbitrary bash script or container on the node.

` .google.container.v1.LinuxNodeConfig.CustomNodeInit custom_node_init = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[LinuxNodeConfig.CustomNodeInit](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.LinuxNodeConfig.CustomNodeInit)` | The customNodeInit.  
  
### getCustomNodeInitOrBuilder()
    
    
    public abstract LinuxNodeConfig.CustomNodeInitOrBuilder getCustomNodeInitOrBuilder()

Optional. Allow users to run arbitrary bash script or container on the node.

` .google.container.v1.LinuxNodeConfig.CustomNodeInit custom_node_init = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[LinuxNodeConfig.CustomNodeInitOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.LinuxNodeConfig.CustomNodeInitOrBuilder)` |   
  
### getDiskIoScheduler()
    
    
    public abstract DiskIoScheduler getDiskIoScheduler()

Optional. Controls the configuration for the disk IO scheduler.

` .google.container.v1.DiskIoScheduler disk_io_scheduler = 16 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[DiskIoScheduler](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.DiskIoScheduler)` | The diskIoScheduler.  
  
### getDiskIoSchedulerOrBuilder()
    
    
    public abstract DiskIoSchedulerOrBuilder getDiskIoSchedulerOrBuilder()

Optional. Controls the configuration for the disk IO scheduler.

` .google.container.v1.DiskIoScheduler disk_io_scheduler = 16 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[DiskIoSchedulerOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.DiskIoSchedulerOrBuilder)` |   
  
### getHugepages()
    
    
    public abstract LinuxNodeConfig.HugepagesConfig getHugepages()

Optional. Amounts for 2M and 1G hugepages

` optional .google.container.v1.LinuxNodeConfig.HugepagesConfig hugepages = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[LinuxNodeConfig.HugepagesConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.LinuxNodeConfig.HugepagesConfig)` | The hugepages.  
  
### getHugepagesOrBuilder()
    
    
    public abstract LinuxNodeConfig.HugepagesConfigOrBuilder getHugepagesOrBuilder()

Optional. Amounts for 2M and 1G hugepages

` optional .google.container.v1.LinuxNodeConfig.HugepagesConfig hugepages = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[LinuxNodeConfig.HugepagesConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.LinuxNodeConfig.HugepagesConfigOrBuilder)` |   
  
### getNodeKernelModuleLoading()
    
    
    public abstract LinuxNodeConfig.NodeKernelModuleLoading getNodeKernelModuleLoading()

Optional. Configuration for kernel module loading on nodes. When enabled, the node pool will be provisioned with a Container-Optimized OS image that enforces kernel module signature verification.

` .google.container.v1.LinuxNodeConfig.NodeKernelModuleLoading node_kernel_module_loading = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[LinuxNodeConfig.NodeKernelModuleLoading](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.LinuxNodeConfig.NodeKernelModuleLoading)` | The nodeKernelModuleLoading.  
  
### getNodeKernelModuleLoadingOrBuilder()
    
    
    public abstract LinuxNodeConfig.NodeKernelModuleLoadingOrBuilder getNodeKernelModuleLoadingOrBuilder()

Optional. Configuration for kernel module loading on nodes. When enabled, the node pool will be provisioned with a Container-Optimized OS image that enforces kernel module signature verification.

` .google.container.v1.LinuxNodeConfig.NodeKernelModuleLoading node_kernel_module_loading = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[LinuxNodeConfig.NodeKernelModuleLoadingOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.LinuxNodeConfig.NodeKernelModuleLoadingOrBuilder)` |   
  
### getNodeVfioConfig()
    
    
    public abstract LinuxNodeConfig.NodeVfioConfig getNodeVfioConfig()

Optional. Contains VFIO-related configurations for this node.

` .google.container.v1.LinuxNodeConfig.NodeVfioConfig node_vfio_config = 15 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[LinuxNodeConfig.NodeVfioConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.LinuxNodeConfig.NodeVfioConfig)` | The nodeVfioConfig.  
  
### getNodeVfioConfigOrBuilder()
    
    
    public abstract LinuxNodeConfig.NodeVfioConfigOrBuilder getNodeVfioConfigOrBuilder()

Optional. Contains VFIO-related configurations for this node.

` .google.container.v1.LinuxNodeConfig.NodeVfioConfig node_vfio_config = 15 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[LinuxNodeConfig.NodeVfioConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.LinuxNodeConfig.NodeVfioConfigOrBuilder)` |   
  
### getSwapConfig()
    
    
    public abstract LinuxNodeConfig.SwapConfig getSwapConfig()

Optional. Enables and configures swap space on nodes. If omitted, swap is disabled.

` optional .google.container.v1.LinuxNodeConfig.SwapConfig swap_config = 12 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[LinuxNodeConfig.SwapConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.LinuxNodeConfig.SwapConfig)` | The swapConfig.  
  
### getSwapConfigOrBuilder()
    
    
    public abstract LinuxNodeConfig.SwapConfigOrBuilder getSwapConfigOrBuilder()

Optional. Enables and configures swap space on nodes. If omitted, swap is disabled.

` optional .google.container.v1.LinuxNodeConfig.SwapConfig swap_config = 12 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[LinuxNodeConfig.SwapConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.LinuxNodeConfig.SwapConfigOrBuilder)` |   
  
### getSysctls() (deprecated)
    
    
    public abstract Map<String,String> getSysctls()

Use [#getSysctlsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.LinuxNodeConfigOrBuilder#com_google_container_v1_LinuxNodeConfigOrBuilder_getSysctlsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getSysctlsCount()
    
    
    public abstract int getSysctlsCount()

The Linux kernel parameters to be applied to the nodes and all pods running on the nodes.

The following parameters are supported.

net.core.busy_poll net.core.busy_read net.core.netdev_max_backlog net.core.rmem_max net.core.rmem_default net.core.wmem_default net.core.wmem_max net.core.optmem_max net.core.somaxconn net.ipv4.neigh.default.gc_thresh1 net.ipv4.neigh.default.gc_thresh2 net.ipv4.neigh.default.gc_thresh3 net.ipv4.tcp_rmem net.ipv4.tcp_wmem net.ipv4.tcp_tw_reuse net.ipv4.tcp_mtu_probing net.ipv4.tcp_max_orphans net.ipv4.tcp_max_tw_buckets net.ipv4.tcp_syn_retries net.ipv4.tcp_ecn net.ipv4.tcp_congestion_control net.netfilter.nf_conntrack_max net.netfilter.nf_conntrack_buckets net.netfilter.nf_conntrack_tcp_timeout_close_wait net.netfilter.nf_conntrack_tcp_timeout_time_wait net.netfilter.nf_conntrack_tcp_timeout_established net.netfilter.nf_conntrack_acct kernel.keys.maxkeys kernel.keys.maxbytes kernel.shmmni kernel.shmmax kernel.shmall kernel.core_pattern kernel.perf_event_paranoid kernel.sched_rt_runtime_us kernel.softlockup_panic kernel.yama.ptrace_scope kernel.kptr_restrict kernel.dmesg_restrict kernel.sysrq fs.aio-max-nr fs.file-max fs.inotify.max_user_instances fs.inotify.max_user_watches fs.nr_open vm.dirty_background_ratio vm.dirty_background_bytes vm.dirty_expire_centisecs vm.dirty_ratio vm.dirty_bytes vm.dirty_writeback_centisecs vm.max_map_count vm.overcommit_memory vm.overcommit_ratio vm.vfs_cache_pressure vm.swappiness vm.watermark_scale_factor vm.min_free_kbytes

`map<string, string> sysctls = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getSysctlsMap()
    
    
    public abstract Map<String,String> getSysctlsMap()

The Linux kernel parameters to be applied to the nodes and all pods running on the nodes.

The following parameters are supported.

net.core.busy_poll net.core.busy_read net.core.netdev_max_backlog net.core.rmem_max net.core.rmem_default net.core.wmem_default net.core.wmem_max net.core.optmem_max net.core.somaxconn net.ipv4.neigh.default.gc_thresh1 net.ipv4.neigh.default.gc_thresh2 net.ipv4.neigh.default.gc_thresh3 net.ipv4.tcp_rmem net.ipv4.tcp_wmem net.ipv4.tcp_tw_reuse net.ipv4.tcp_mtu_probing net.ipv4.tcp_max_orphans net.ipv4.tcp_max_tw_buckets net.ipv4.tcp_syn_retries net.ipv4.tcp_ecn net.ipv4.tcp_congestion_control net.netfilter.nf_conntrack_max net.netfilter.nf_conntrack_buckets net.netfilter.nf_conntrack_tcp_timeout_close_wait net.netfilter.nf_conntrack_tcp_timeout_time_wait net.netfilter.nf_conntrack_tcp_timeout_established net.netfilter.nf_conntrack_acct kernel.keys.maxkeys kernel.keys.maxbytes kernel.shmmni kernel.shmmax kernel.shmall kernel.core_pattern kernel.perf_event_paranoid kernel.sched_rt_runtime_us kernel.softlockup_panic kernel.yama.ptrace_scope kernel.kptr_restrict kernel.dmesg_restrict kernel.sysrq fs.aio-max-nr fs.file-max fs.inotify.max_user_instances fs.inotify.max_user_watches fs.nr_open vm.dirty_background_ratio vm.dirty_background_bytes vm.dirty_expire_centisecs vm.dirty_ratio vm.dirty_bytes vm.dirty_writeback_centisecs vm.max_map_count vm.overcommit_memory vm.overcommit_ratio vm.vfs_cache_pressure vm.swappiness vm.watermark_scale_factor vm.min_free_kbytes

`map<string, string> sysctls = 1;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getSysctlsOrDefault(String key, String defaultValue)
    
    
    public abstract String getSysctlsOrDefault(String key, String defaultValue)

The Linux kernel parameters to be applied to the nodes and all pods running on the nodes.

The following parameters are supported.

net.core.busy_poll net.core.busy_read net.core.netdev_max_backlog net.core.rmem_max net.core.rmem_default net.core.wmem_default net.core.wmem_max net.core.optmem_max net.core.somaxconn net.ipv4.neigh.default.gc_thresh1 net.ipv4.neigh.default.gc_thresh2 net.ipv4.neigh.default.gc_thresh3 net.ipv4.tcp_rmem net.ipv4.tcp_wmem net.ipv4.tcp_tw_reuse net.ipv4.tcp_mtu_probing net.ipv4.tcp_max_orphans net.ipv4.tcp_max_tw_buckets net.ipv4.tcp_syn_retries net.ipv4.tcp_ecn net.ipv4.tcp_congestion_control net.netfilter.nf_conntrack_max net.netfilter.nf_conntrack_buckets net.netfilter.nf_conntrack_tcp_timeout_close_wait net.netfilter.nf_conntrack_tcp_timeout_time_wait net.netfilter.nf_conntrack_tcp_timeout_established net.netfilter.nf_conntrack_acct kernel.keys.maxkeys kernel.keys.maxbytes kernel.shmmni kernel.shmmax kernel.shmall kernel.core_pattern kernel.perf_event_paranoid kernel.sched_rt_runtime_us kernel.softlockup_panic kernel.yama.ptrace_scope kernel.kptr_restrict kernel.dmesg_restrict kernel.sysrq fs.aio-max-nr fs.file-max fs.inotify.max_user_instances fs.inotify.max_user_watches fs.nr_open vm.dirty_background_ratio vm.dirty_background_bytes vm.dirty_expire_centisecs vm.dirty_ratio vm.dirty_bytes vm.dirty_writeback_centisecs vm.max_map_count vm.overcommit_memory vm.overcommit_ratio vm.vfs_cache_pressure vm.swappiness vm.watermark_scale_factor vm.min_free_kbytes

`map<string, string> sysctls = 1;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getSysctlsOrThrow(String key)
    
    
    public abstract String getSysctlsOrThrow(String key)

The Linux kernel parameters to be applied to the nodes and all pods running on the nodes.

The following parameters are supported.

net.core.busy_poll net.core.busy_read net.core.netdev_max_backlog net.core.rmem_max net.core.rmem_default net.core.wmem_default net.core.wmem_max net.core.optmem_max net.core.somaxconn net.ipv4.neigh.default.gc_thresh1 net.ipv4.neigh.default.gc_thresh2 net.ipv4.neigh.default.gc_thresh3 net.ipv4.tcp_rmem net.ipv4.tcp_wmem net.ipv4.tcp_tw_reuse net.ipv4.tcp_mtu_probing net.ipv4.tcp_max_orphans net.ipv4.tcp_max_tw_buckets net.ipv4.tcp_syn_retries net.ipv4.tcp_ecn net.ipv4.tcp_congestion_control net.netfilter.nf_conntrack_max net.netfilter.nf_conntrack_buckets net.netfilter.nf_conntrack_tcp_timeout_close_wait net.netfilter.nf_conntrack_tcp_timeout_time_wait net.netfilter.nf_conntrack_tcp_timeout_established net.netfilter.nf_conntrack_acct kernel.keys.maxkeys kernel.keys.maxbytes kernel.shmmni kernel.shmmax kernel.shmall kernel.core_pattern kernel.perf_event_paranoid kernel.sched_rt_runtime_us kernel.softlockup_panic kernel.yama.ptrace_scope kernel.kptr_restrict kernel.dmesg_restrict kernel.sysrq fs.aio-max-nr fs.file-max fs.inotify.max_user_instances fs.inotify.max_user_watches fs.nr_open vm.dirty_background_ratio vm.dirty_background_bytes vm.dirty_expire_centisecs vm.dirty_ratio vm.dirty_bytes vm.dirty_writeback_centisecs vm.max_map_count vm.overcommit_memory vm.overcommit_ratio vm.vfs_cache_pressure vm.swappiness vm.watermark_scale_factor vm.min_free_kbytes

`map<string, string> sysctls = 1;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getTransparentHugepageDefrag()
    
    
    public abstract LinuxNodeConfig.TransparentHugepageDefrag getTransparentHugepageDefrag()

Optional. Defines the transparent hugepage defrag configuration on the node. VM hugepage allocation can be managed by either limiting defragmentation for delayed allocation or skipping it entirely for immediate allocation only.

See <https://docs.kernel.org/admin-guide/mm/transhuge.html> for more details.

` .google.container.v1.LinuxNodeConfig.TransparentHugepageDefrag transparent_hugepage_defrag = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[LinuxNodeConfig.TransparentHugepageDefrag](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.LinuxNodeConfig.TransparentHugepageDefrag)` | The transparentHugepageDefrag.  
  
### getTransparentHugepageDefragValue()
    
    
    public abstract int getTransparentHugepageDefragValue()

Optional. Defines the transparent hugepage defrag configuration on the node. VM hugepage allocation can be managed by either limiting defragmentation for delayed allocation or skipping it entirely for immediate allocation only.

See <https://docs.kernel.org/admin-guide/mm/transhuge.html> for more details.

` .google.container.v1.LinuxNodeConfig.TransparentHugepageDefrag transparent_hugepage_defrag = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for transparentHugepageDefrag.  
  
### getTransparentHugepageEnabled()
    
    
    public abstract LinuxNodeConfig.TransparentHugepageEnabled getTransparentHugepageEnabled()

Optional. Transparent hugepage support for anonymous memory can be entirely disabled (mostly for debugging purposes) or only enabled inside MADV_HUGEPAGE regions (to avoid the risk of consuming more memory resources) or enabled system wide.

See <https://docs.kernel.org/admin-guide/mm/transhuge.html> for more details.

` .google.container.v1.LinuxNodeConfig.TransparentHugepageEnabled transparent_hugepage_enabled = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[LinuxNodeConfig.TransparentHugepageEnabled](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.LinuxNodeConfig.TransparentHugepageEnabled)` | The transparentHugepageEnabled.  
  
### getTransparentHugepageEnabledValue()
    
    
    public abstract int getTransparentHugepageEnabledValue()

Optional. Transparent hugepage support for anonymous memory can be entirely disabled (mostly for debugging purposes) or only enabled inside MADV_HUGEPAGE regions (to avoid the risk of consuming more memory resources) or enabled system wide.

See <https://docs.kernel.org/admin-guide/mm/transhuge.html> for more details.

` .google.container.v1.LinuxNodeConfig.TransparentHugepageEnabled transparent_hugepage_enabled = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for transparentHugepageEnabled.  
  
### hasAccurateTimeConfig()
    
    
    public abstract boolean hasAccurateTimeConfig()

Optional. The accurate time configuration for the node pool.

` optional .google.container.v1.LinuxNodeConfig.AccurateTimeConfig accurate_time_config = 14 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the accurateTimeConfig field is set.  
  
### hasCustomNodeInit()
    
    
    public abstract boolean hasCustomNodeInit()

Optional. Allow users to run arbitrary bash script or container on the node.

` .google.container.v1.LinuxNodeConfig.CustomNodeInit custom_node_init = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the customNodeInit field is set.  
  
### hasDiskIoScheduler()
    
    
    public abstract boolean hasDiskIoScheduler()

Optional. Controls the configuration for the disk IO scheduler.

` .google.container.v1.DiskIoScheduler disk_io_scheduler = 16 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the diskIoScheduler field is set.  
  
### hasHugepages()
    
    
    public abstract boolean hasHugepages()

Optional. Amounts for 2M and 1G hugepages

` optional .google.container.v1.LinuxNodeConfig.HugepagesConfig hugepages = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the hugepages field is set.  
  
### hasNodeKernelModuleLoading()
    
    
    public abstract boolean hasNodeKernelModuleLoading()

Optional. Configuration for kernel module loading on nodes. When enabled, the node pool will be provisioned with a Container-Optimized OS image that enforces kernel module signature verification.

` .google.container.v1.LinuxNodeConfig.NodeKernelModuleLoading node_kernel_module_loading = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the nodeKernelModuleLoading field is set.  
  
### hasNodeVfioConfig()
    
    
    public abstract boolean hasNodeVfioConfig()

Optional. Contains VFIO-related configurations for this node.

` .google.container.v1.LinuxNodeConfig.NodeVfioConfig node_vfio_config = 15 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the nodeVfioConfig field is set.  
  
### hasSwapConfig()
    
    
    public abstract boolean hasSwapConfig()

Optional. Enables and configures swap space on nodes. If omitted, swap is disabled.

` optional .google.container.v1.LinuxNodeConfig.SwapConfig swap_config = 12 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the swapConfig field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
