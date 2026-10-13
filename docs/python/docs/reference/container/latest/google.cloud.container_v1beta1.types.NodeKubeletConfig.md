---
url: https://docs.cloud.google.com/python/docs/reference/container/latest/google.cloud.container_v1beta1.types.NodeKubeletConfig
title: Class NodeKubeletConfig (2.67.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:32:07.652715+00:00
---

# Class NodeKubeletConfig (2.67.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/container/latest/google.cloud.container_v1beta1.types.NodeKubeletConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class NodeKubeletConfig (2.67.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.67.0 (latest)  2.66.0  2.65.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.1  2.55.1  2.54.0  2.53.0  2.52.0  2.50.0  2.49.0  2.48.0  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.4  2.16.0  2.15.0  2.14.0  2.13.0  2.12.2  2.11.2  2.10.8  2.9.0  2.8.1  2.7.1  2.6.1  2.5.0  2.4.1  2.3.1  2.2.0  2.1.0  2.0.1  1.0.3  0.5.0  0.4.0  0.3.0 
    
    
    NodeKubeletConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Node kubelet configs.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`cpu_manager_policy` |  `str`   
Control the CPU management policy on the node. See https://kubernetes.io/docs/tasks/administer-cluster/cpu-management-policies/ The following values are allowed. \- "none": the default, which represents the existing scheduling behavior. \- "static": allows pods with certain resource characteristics to be granted increased CPU affinity and exclusivity on the node. The default value is 'none' if unspecified.   
`topology_manager` |  `[google.cloud.container_v1beta1.types.TopologyManager](https://docs.cloud.google.com/python/docs/reference/container/latest/google.cloud.container_v1beta1.types.TopologyManager)`   
Optional. Controls Topology Manager configuration on the node. For more information, see: https://kubernetes.io/docs/tasks/administer-cluster/topology-manager/   
`memory_manager` |  `[google.cloud.container_v1beta1.types.MemoryManager](https://docs.cloud.google.com/python/docs/reference/container/latest/google.cloud.container_v1beta1.types.MemoryManager)`   
Optional. Controls NUMA-aware Memory Manager configuration on the node. For more information, see: https://kubernetes.io/docs/tasks/administer-cluster/memory-manager/   
`cpu_cfs_quota` |  `google.protobuf.wrappers_pb2.BoolValue`   
Enable CPU CFS quota enforcement for containers that specify CPU limits. This option is enabled by default which makes kubelet use CFS quota (https://www.kernel.org/doc/Documentation/scheduler/sched-bwc.txt) to enforce container CPU limits. Otherwise, CPU limits will not be enforced at all. Disable this option to mitigate CPU throttling problems while still having your pods to be in Guaranteed QoS class by specifying the CPU limits. The default value is 'true' if unspecified.   
`cpu_cfs_quota_period` |  `str`   
Set the CPU CFS quota period value 'cpu.cfs_period_us'. The string must be a sequence of decimal numbers, each with optional fraction and a unit suffix, such as "300ms". Valid time units are "ns", "us" (or "µs"), "ms", "s", "m", "h". The value must be a positive duration between 1ms and 1 second, inclusive.   
`pod_pids_limit` |  `int`   
Set the Pod PID limits. See https://kubernetes.io/docs/concepts/policy/pid-limiting/#pod-pid-limits Controls the maximum number of processes allowed to run in a pod. The value must be greater than or equal to 1024 and less than 4194304.   
`insecure_kubelet_readonly_port_enabled` |  `bool`   
Enable or disable Kubelet read only port. This field is a member of `oneof`_ `_insecure_kubelet_readonly_port_enabled`.   
`image_gc_low_threshold_percent` |  `int`   
Optional. Defines the percent of disk usage before which image garbage collection is never run. Lowest disk usage to garbage collect to. The percent is calculated as this field value out of 100. The value must be between 10 and 85, inclusive and smaller than image_gc_high_threshold_percent. The default value is 80 if unspecified.   
`image_gc_high_threshold_percent` |  `int`   
Optional. Defines the percent of disk usage after which image garbage collection is always run. The percent is calculated as this field value out of 100. The value must be between 10 and 85, inclusive and greater than image_gc_low_threshold_percent. The default value is 85 if unspecified.   
`image_minimum_gc_age` |  `str`   
Optional. Defines the minimum age for an unused image before it is garbage collected. The string must be a sequence of decimal numbers, each with optional fraction and a unit suffix, such as "300s", "1.5h", and "2h45m". Valid time units are "ns", "us" (or "µs"), "ms", "s", "m", "h". The value must be a positive duration less than or equal to 2 minutes. The default value is "2m0s" if unspecified.   
`image_maximum_gc_age` |  `str`   
Optional. Defines the maximum age an image can be unused before it is garbage collected. The string must be a sequence of decimal numbers, each with optional fraction and a unit suffix, such as "300s", "1.5h", and "2h45m". Valid time units are "ns", "us" (or "µs"), "ms", "s", "m", "h". The value must be a positive duration greater than image_minimum_gc_age or "0s". The default value is "0s" if unspecified, which disables this field, meaning images won't be garbage collected based on being unused for too long.   
`container_log_max_size` |  `str`   
Optional. Defines the maximum size of the container log file before it is rotated. See https://kubernetes.io/docs/concepts/cluster-administration/logging/#log-rotation Valid format is positive number + unit, e.g. 100Ki, 10Mi. Valid units are Ki, Mi, Gi. The value must be between 10Mi and 500Mi, inclusive. Note that the total container log size (container_log_max_size \\* container_log_max_files) cannot exceed 1% of the total storage of the node, to avoid disk pressure caused by log files. The default value is 10Mi if unspecified.   
`container_log_max_files` |  `int`   
Optional. Defines the maximum number of container log files that can be present for a container. See https://kubernetes.io/docs/concepts/cluster-administration/logging/#log-rotation The value must be an integer between 2 and 10, inclusive. The default value is 5 if unspecified.   
`allowed_unsafe_sysctls` |  `MutableSequence[str]`   
Optional. Defines a comma-separated allowlist of unsafe sysctls or sysctl patterns (ending in `*`). The unsafe namespaced sysctl groups are `kernel.shm*`, `kernel.msg*`, `kernel.sem`, `fs.mqueue.*`, and `net.*`. Leaving this allowlist empty means they cannot be set on Pods. To allow certain sysctls or sysctl patterns to be set on Pods, list them separated by commas. For example: `kernel.msg*,net.ipv4.route.min_pmtu`. See https://kubernetes.io/docs/tasks/administer-cluster/sysctl-cluster/ for more details.   
`eviction_soft` |  `[google.cloud.container_v1beta1.types.EvictionSignals](https://docs.cloud.google.com/python/docs/reference/container/latest/google.cloud.container_v1beta1.types.EvictionSignals)`   
Optional. eviction_soft is a map of signal names to quantities that defines soft eviction thresholds. Each signal is compared to its corresponding threshold to determine if a pod eviction should occur.   
`eviction_soft_grace_period` |  `[google.cloud.container_v1beta1.types.EvictionGracePeriod](https://docs.cloud.google.com/python/docs/reference/container/latest/google.cloud.container_v1beta1.types.EvictionGracePeriod)`   
Optional. eviction_soft_grace_period is a map of signal names to quantities that defines grace periods for each soft eviction signal. The grace period is the amount of time that a pod must be under pressure before an eviction occurs.   
`eviction_minimum_reclaim` |  `[google.cloud.container_v1beta1.types.EvictionMinimumReclaim](https://docs.cloud.google.com/python/docs/reference/container/latest/google.cloud.container_v1beta1.types.EvictionMinimumReclaim)`   
Optional. eviction_minimum_reclaim is a map of signal names to quantities that defines minimum reclaims, which describe the minimum amount of a given resource the kubelet will reclaim when performing a pod eviction while that resource is under pressure.   
`eviction_max_pod_grace_period_seconds` |  `int`   
Optional. eviction_max_pod_grace_period_seconds is the maximum allowed grace period (in seconds) to use when terminating pods in response to a soft eviction threshold being met. This value effectively caps the Pod's terminationGracePeriodSeconds value during soft evictions. Default: 0. Range: [0, 300].   
`max_parallel_image_pulls` |  `int`   
Optional. Defines the maximum number of image pulls in parallel. The range is 2 to 5, inclusive. The default value is 2 or 3 depending on the disk type. See https://kubernetes.io/docs/concepts/containers/images/#maximum-parallel-image-pulls for more details.   
`single_process_oom_kill` |  `bool`   
Optional. Defines whether to enable single process OOM killer. If true, will prevent the memory.oom.group flag from being set for container cgroups in cgroups v2. This causes processes in the container to be OOM killed individually instead of as a group. This field is a member of `oneof`_ `_single_process_oom_kill`.   
`crash_loop_back_off` |  `[google.cloud.container_v1beta1.types.NodeKubeletConfig.CrashLoopBackOffConfig](https://docs.cloud.google.com/python/docs/reference/container/latest/google.cloud.container_v1beta1.types.NodeKubeletConfig.CrashLoopBackOffConfig)`   
Optional. Contains configuration options to modify node-level parameters for container restart behavior.   
`shutdown_grace_period_seconds` |  `int`   
Optional. shutdown_grace_period_seconds is the maximum allowed grace period (in seconds) the total duration that the node should delay the shutdown during a graceful shutdown. This is the total grace period for pod termination for both regular and critical pods. https://kubernetes.io/docs/concepts/cluster-administration/node-shutdown/ If set to 0, node will not enable the graceful node shutdown functionality. This field is only valid for Spot VMs. Allowed values: 0, 30, 120. This field is a member of `oneof`_ `_shutdown_grace_period_seconds`.   
`shutdown_grace_period_critical_pods_seconds` |  `int`   
Optional. shutdown_grace_period_critical_pods_seconds is the maximum allowed grace period (in seconds) used to terminate critical pods during a node shutdown. This value should be <= shutdown_grace_period_seconds,="" and="" is="" only="" valid="" if="" shutdown_grace_period_seconds="" is="" set.="" https://kubernetes.io/docs/concepts/cluster-administration/node-shutdown/="" range:="" [0,="" 120].="" this="" field="" is="" a="" member="" of="">`oneof`_ `_shutdown_grace_period_critical_pods_seconds`.   
  
## Classes 

### CrashLoopBackOffConfig
    
    
    CrashLoopBackOffConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Contains config to modify node-level parameters for container restart behavior.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
