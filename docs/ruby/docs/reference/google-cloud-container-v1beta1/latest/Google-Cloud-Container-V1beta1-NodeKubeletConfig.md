---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Cloud-Container-V1beta1-NodeKubeletConfig/
title: Kubernetes Engine V1beta1 API - Class Google::Cloud::Container::V1beta1::NodeKubeletConfig (v0.57.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:20:19.216014+00:00
---

# Kubernetes Engine V1beta1 API - Class Google::Cloud::Container::V1beta1::NodeKubeletConfig (v0.57.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Cloud-Container-V1beta1-NodeKubeletConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Kubernetes Engine V1beta1 API - Class Google::Cloud::Container::V1beta1::NodeKubeletConfig (v0.57.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.57.1 (latest)  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.1  0.50.0  0.49.1  0.48.0  0.47.0  0.46.0  0.45.1  0.44.0  0.43.0  0.42.1  0.41.0  0.40.1  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.3  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.1  0.20.0  0.19.0  0.18.0  0.17.0  0.16.3  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.1  0.9.0  0.8.3 

Reference documentation and code samples for the Kubernetes Engine V1beta1 API class Google::Cloud::Container::V1beta1::NodeKubeletConfig.

Node kubelet configs.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #allowed_unsafe_sysctls
    
    
    def allowed_unsafe_sysctls() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Optional. Defines a comma-separated allowlist of unsafe sysctls or sysctl patterns (ending in `*`).

The unsafe namespaced sysctl groups are `kernel.shm*`, `kernel.msg*`, `kernel.sem`, `fs.mqueue.*`, and `net.*`. Leaving this allowlist empty means they cannot be set on Pods.

To allow certain sysctls or sysctl patterns to be set on Pods, list them separated by commas. For example: `kernel.msg*,net.ipv4.route.min_pmtu`.

See https://kubernetes.io/docs/tasks/administer-cluster/sysctl-cluster/ for more details. 




### #allowed_unsafe_sysctls=
    
    
    def allowed_unsafe_sysctls=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Optional. Defines a comma-separated allowlist of unsafe sysctls or sysctl patterns (ending in `*`).

The unsafe namespaced sysctl groups are `kernel.shm*`, `kernel.msg*`, `kernel.sem`, `fs.mqueue.*`, and `net.*`. Leaving this allowlist empty means they cannot be set on Pods.

To allow certain sysctls or sysctl patterns to be set on Pods, list them separated by commas. For example: `kernel.msg*,net.ipv4.route.min_pmtu`.

See https://kubernetes.io/docs/tasks/administer-cluster/sysctl-cluster/ for more details. 




**Returns**

  * (::Array<::String>) — Optional. Defines a comma-separated allowlist of unsafe sysctls or sysctl patterns (ending in `*`).

The unsafe namespaced sysctl groups are `kernel.shm*`, `kernel.msg*`, `kernel.sem`, `fs.mqueue.*`, and `net.*`. Leaving this allowlist empty means they cannot be set on Pods.

To allow certain sysctls or sysctl patterns to be set on Pods, list them separated by commas. For example: `kernel.msg*,net.ipv4.route.min_pmtu`.

See https://kubernetes.io/docs/tasks/administer-cluster/sysctl-cluster/ for more details. 




### #container_log_max_files
    
    
    def container_log_max_files() -> ::Integer

**Returns**

  * (::Integer) — Optional. Defines the maximum number of container log files that can be present for a container. See https://kubernetes.io/docs/concepts/cluster-administration/logging/#log-rotation

The value must be an integer between 2 and 10, inclusive. The default value is 5 if unspecified. 




### #container_log_max_files=
    
    
    def container_log_max_files=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Defines the maximum number of container log files that can be present for a container. See https://kubernetes.io/docs/concepts/cluster-administration/logging/#log-rotation

The value must be an integer between 2 and 10, inclusive. The default value is 5 if unspecified. 




**Returns**

  * (::Integer) — Optional. Defines the maximum number of container log files that can be present for a container. See https://kubernetes.io/docs/concepts/cluster-administration/logging/#log-rotation

The value must be an integer between 2 and 10, inclusive. The default value is 5 if unspecified. 




### #container_log_max_size
    
    
    def container_log_max_size() -> ::String

**Returns**

  * (::String) — Optional. Defines the maximum size of the container log file before it is rotated. See https://kubernetes.io/docs/concepts/cluster-administration/logging/#log-rotation

Valid format is positive number + unit, e.g. 100Ki, 10Mi. Valid units are Ki, Mi, Gi. The value must be between 10Mi and 500Mi, inclusive.

Note that the total container log size (container_log_max_size * container_log_max_files) cannot exceed 1% of the total storage of the node, to avoid disk pressure caused by log files.

The default value is 10Mi if unspecified. 




### #container_log_max_size=
    
    
    def container_log_max_size=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Defines the maximum size of the container log file before it is rotated. See https://kubernetes.io/docs/concepts/cluster-administration/logging/#log-rotation

Valid format is positive number + unit, e.g. 100Ki, 10Mi. Valid units are Ki, Mi, Gi. The value must be between 10Mi and 500Mi, inclusive.

Note that the total container log size (container_log_max_size * container_log_max_files) cannot exceed 1% of the total storage of the node, to avoid disk pressure caused by log files.

The default value is 10Mi if unspecified. 




**Returns**

  * (::String) — Optional. Defines the maximum size of the container log file before it is rotated. See https://kubernetes.io/docs/concepts/cluster-administration/logging/#log-rotation

Valid format is positive number + unit, e.g. 100Ki, 10Mi. Valid units are Ki, Mi, Gi. The value must be between 10Mi and 500Mi, inclusive.

Note that the total container log size (container_log_max_size * container_log_max_files) cannot exceed 1% of the total storage of the node, to avoid disk pressure caused by log files.

The default value is 10Mi if unspecified. 




### #cpu_cfs_quota
    
    
    def cpu_cfs_quota() -> ::Google::Protobuf::BoolValue

**Returns**

  * ([::Google::Protobuf::BoolValue](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Protobuf-BoolValue)) — Enable CPU CFS quota enforcement for containers that specify CPU limits.

This option is enabled by default which makes kubelet use CFS quota (https://www.kernel.org/doc/Documentation/scheduler/sched-bwc.txt) to enforce container CPU limits. Otherwise, CPU limits will not be enforced at all.

Disable this option to mitigate CPU throttling problems while still having your pods to be in Guaranteed QoS class by specifying the CPU limits.

The default value is 'true' if unspecified. 




### #cpu_cfs_quota=
    
    
    def cpu_cfs_quota=(value) -> ::Google::Protobuf::BoolValue

**Parameter**

  * **value** ([::Google::Protobuf::BoolValue](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Protobuf-BoolValue)) — Enable CPU CFS quota enforcement for containers that specify CPU limits.

This option is enabled by default which makes kubelet use CFS quota (https://www.kernel.org/doc/Documentation/scheduler/sched-bwc.txt) to enforce container CPU limits. Otherwise, CPU limits will not be enforced at all.

Disable this option to mitigate CPU throttling problems while still having your pods to be in Guaranteed QoS class by specifying the CPU limits.

The default value is 'true' if unspecified. 




**Returns**

  * ([::Google::Protobuf::BoolValue](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Protobuf-BoolValue)) — Enable CPU CFS quota enforcement for containers that specify CPU limits.

This option is enabled by default which makes kubelet use CFS quota (https://www.kernel.org/doc/Documentation/scheduler/sched-bwc.txt) to enforce container CPU limits. Otherwise, CPU limits will not be enforced at all.

Disable this option to mitigate CPU throttling problems while still having your pods to be in Guaranteed QoS class by specifying the CPU limits.

The default value is 'true' if unspecified. 




### #cpu_cfs_quota_period
    
    
    def cpu_cfs_quota_period() -> ::String

**Returns**

  * (::String) — Set the CPU CFS quota period value 'cpu.cfs_period_us'.

The string must be a sequence of decimal numbers, each with optional fraction and a unit suffix, such as "300ms". Valid time units are "ns", "us" (or "µs"), "ms", "s", "m", "h". The value must be a positive duration between 1ms and 1 second, inclusive. 




### #cpu_cfs_quota_period=
    
    
    def cpu_cfs_quota_period=(value) -> ::String

**Parameter**

  * **value** (::String) — Set the CPU CFS quota period value 'cpu.cfs_period_us'.

The string must be a sequence of decimal numbers, each with optional fraction and a unit suffix, such as "300ms". Valid time units are "ns", "us" (or "µs"), "ms", "s", "m", "h". The value must be a positive duration between 1ms and 1 second, inclusive. 




**Returns**

  * (::String) — Set the CPU CFS quota period value 'cpu.cfs_period_us'.

The string must be a sequence of decimal numbers, each with optional fraction and a unit suffix, such as "300ms". Valid time units are "ns", "us" (or "µs"), "ms", "s", "m", "h". The value must be a positive duration between 1ms and 1 second, inclusive. 




### #cpu_manager_policy
    
    
    def cpu_manager_policy() -> ::String

**Returns**

  * (::String) — 

Control the CPU management policy on the node. See https://kubernetes.io/docs/tasks/administer-cluster/cpu-management-policies/

The following values are allowed.

    * "none": the default, which represents the existing scheduling behavior.
    * "static": allows pods with certain resource characteristics to be granted increased CPU affinity and exclusivity on the node. The default value is 'none' if unspecified.



### #cpu_manager_policy=
    
    
    def cpu_manager_policy=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Control the CPU management policy on the node. See https://kubernetes.io/docs/tasks/administer-cluster/cpu-management-policies/

The following values are allowed.

    * "none": the default, which represents the existing scheduling behavior.
    * "static": allows pods with certain resource characteristics to be granted increased CPU affinity and exclusivity on the node. The default value is 'none' if unspecified.



**Returns**

  * (::String) — 

Control the CPU management policy on the node. See https://kubernetes.io/docs/tasks/administer-cluster/cpu-management-policies/

The following values are allowed.

    * "none": the default, which represents the existing scheduling behavior.
    * "static": allows pods with certain resource characteristics to be granted increased CPU affinity and exclusivity on the node. The default value is 'none' if unspecified.



### #crash_loop_back_off
    
    
    def crash_loop_back_off() -> ::Google::Cloud::Container::V1beta1::NodeKubeletConfig::CrashLoopBackOffConfig

**Returns**

  * ([::Google::Cloud::Container::V1beta1::NodeKubeletConfig::CrashLoopBackOffConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Cloud-Container-V1beta1-NodeKubeletConfig-CrashLoopBackOffConfig)) — Optional. Contains configuration options to modify node-level parameters for container restart behavior. 



### #crash_loop_back_off=
    
    
    def crash_loop_back_off=(value) -> ::Google::Cloud::Container::V1beta1::NodeKubeletConfig::CrashLoopBackOffConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1beta1::NodeKubeletConfig::CrashLoopBackOffConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Cloud-Container-V1beta1-NodeKubeletConfig-CrashLoopBackOffConfig)) — Optional. Contains configuration options to modify node-level parameters for container restart behavior. 



**Returns**

  * ([::Google::Cloud::Container::V1beta1::NodeKubeletConfig::CrashLoopBackOffConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Cloud-Container-V1beta1-NodeKubeletConfig-CrashLoopBackOffConfig)) — Optional. Contains configuration options to modify node-level parameters for container restart behavior. 



### #eviction_max_pod_grace_period_seconds
    
    
    def eviction_max_pod_grace_period_seconds() -> ::Integer

**Returns**

  * (::Integer) — Optional. eviction_max_pod_grace_period_seconds is the maximum allowed grace period (in seconds) to use when terminating pods in response to a soft eviction threshold being met. This value effectively caps the Pod's terminationGracePeriodSeconds value during soft evictions. Default: 0. Range: [0, 300]. 



### #eviction_max_pod_grace_period_seconds=
    
    
    def eviction_max_pod_grace_period_seconds=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. eviction_max_pod_grace_period_seconds is the maximum allowed grace period (in seconds) to use when terminating pods in response to a soft eviction threshold being met. This value effectively caps the Pod's terminationGracePeriodSeconds value during soft evictions. Default: 0. Range: [0, 300]. 



**Returns**

  * (::Integer) — Optional. eviction_max_pod_grace_period_seconds is the maximum allowed grace period (in seconds) to use when terminating pods in response to a soft eviction threshold being met. This value effectively caps the Pod's terminationGracePeriodSeconds value during soft evictions. Default: 0. Range: [0, 300]. 



### #eviction_minimum_reclaim
    
    
    def eviction_minimum_reclaim() -> ::Google::Cloud::Container::V1beta1::EvictionMinimumReclaim

**Returns**

  * ([::Google::Cloud::Container::V1beta1::EvictionMinimumReclaim](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Cloud-Container-V1beta1-EvictionMinimumReclaim)) — Optional. eviction_minimum_reclaim is a map of signal names to quantities that defines minimum reclaims, which describe the minimum amount of a given resource the kubelet will reclaim when performing a pod eviction while that resource is under pressure. 



### #eviction_minimum_reclaim=
    
    
    def eviction_minimum_reclaim=(value) -> ::Google::Cloud::Container::V1beta1::EvictionMinimumReclaim

**Parameter**

  * **value** ([::Google::Cloud::Container::V1beta1::EvictionMinimumReclaim](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Cloud-Container-V1beta1-EvictionMinimumReclaim)) — Optional. eviction_minimum_reclaim is a map of signal names to quantities that defines minimum reclaims, which describe the minimum amount of a given resource the kubelet will reclaim when performing a pod eviction while that resource is under pressure. 



**Returns**

  * ([::Google::Cloud::Container::V1beta1::EvictionMinimumReclaim](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Cloud-Container-V1beta1-EvictionMinimumReclaim)) — Optional. eviction_minimum_reclaim is a map of signal names to quantities that defines minimum reclaims, which describe the minimum amount of a given resource the kubelet will reclaim when performing a pod eviction while that resource is under pressure. 



### #eviction_soft
    
    
    def eviction_soft() -> ::Google::Cloud::Container::V1beta1::EvictionSignals

**Returns**

  * ([::Google::Cloud::Container::V1beta1::EvictionSignals](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Cloud-Container-V1beta1-EvictionSignals)) — Optional. eviction_soft is a map of signal names to quantities that defines soft eviction thresholds. Each signal is compared to its corresponding threshold to determine if a pod eviction should occur. 



### #eviction_soft=
    
    
    def eviction_soft=(value) -> ::Google::Cloud::Container::V1beta1::EvictionSignals

**Parameter**

  * **value** ([::Google::Cloud::Container::V1beta1::EvictionSignals](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Cloud-Container-V1beta1-EvictionSignals)) — Optional. eviction_soft is a map of signal names to quantities that defines soft eviction thresholds. Each signal is compared to its corresponding threshold to determine if a pod eviction should occur. 



**Returns**

  * ([::Google::Cloud::Container::V1beta1::EvictionSignals](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Cloud-Container-V1beta1-EvictionSignals)) — Optional. eviction_soft is a map of signal names to quantities that defines soft eviction thresholds. Each signal is compared to its corresponding threshold to determine if a pod eviction should occur. 



### #eviction_soft_grace_period
    
    
    def eviction_soft_grace_period() -> ::Google::Cloud::Container::V1beta1::EvictionGracePeriod

**Returns**

  * ([::Google::Cloud::Container::V1beta1::EvictionGracePeriod](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Cloud-Container-V1beta1-EvictionGracePeriod)) — Optional. eviction_soft_grace_period is a map of signal names to quantities that defines grace periods for each soft eviction signal. The grace period is the amount of time that a pod must be under pressure before an eviction occurs. 



### #eviction_soft_grace_period=
    
    
    def eviction_soft_grace_period=(value) -> ::Google::Cloud::Container::V1beta1::EvictionGracePeriod

**Parameter**

  * **value** ([::Google::Cloud::Container::V1beta1::EvictionGracePeriod](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Cloud-Container-V1beta1-EvictionGracePeriod)) — Optional. eviction_soft_grace_period is a map of signal names to quantities that defines grace periods for each soft eviction signal. The grace period is the amount of time that a pod must be under pressure before an eviction occurs. 



**Returns**

  * ([::Google::Cloud::Container::V1beta1::EvictionGracePeriod](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Cloud-Container-V1beta1-EvictionGracePeriod)) — Optional. eviction_soft_grace_period is a map of signal names to quantities that defines grace periods for each soft eviction signal. The grace period is the amount of time that a pod must be under pressure before an eviction occurs. 



### #image_gc_high_threshold_percent
    
    
    def image_gc_high_threshold_percent() -> ::Integer

**Returns**

  * (::Integer) — Optional. Defines the percent of disk usage after which image garbage collection is always run. The percent is calculated as this field value out of 100.

The value must be between 10 and 85, inclusive and greater than image_gc_low_threshold_percent.

The default value is 85 if unspecified. 




### #image_gc_high_threshold_percent=
    
    
    def image_gc_high_threshold_percent=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Defines the percent of disk usage after which image garbage collection is always run. The percent is calculated as this field value out of 100.

The value must be between 10 and 85, inclusive and greater than image_gc_low_threshold_percent.

The default value is 85 if unspecified. 




**Returns**

  * (::Integer) — Optional. Defines the percent of disk usage after which image garbage collection is always run. The percent is calculated as this field value out of 100.

The value must be between 10 and 85, inclusive and greater than image_gc_low_threshold_percent.

The default value is 85 if unspecified. 




### #image_gc_low_threshold_percent
    
    
    def image_gc_low_threshold_percent() -> ::Integer

**Returns**

  * (::Integer) — Optional. Defines the percent of disk usage before which image garbage collection is never run. Lowest disk usage to garbage collect to. The percent is calculated as this field value out of 100.

The value must be between 10 and 85, inclusive and smaller than image_gc_high_threshold_percent.

The default value is 80 if unspecified. 




### #image_gc_low_threshold_percent=
    
    
    def image_gc_low_threshold_percent=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Defines the percent of disk usage before which image garbage collection is never run. Lowest disk usage to garbage collect to. The percent is calculated as this field value out of 100.

The value must be between 10 and 85, inclusive and smaller than image_gc_high_threshold_percent.

The default value is 80 if unspecified. 




**Returns**

  * (::Integer) — Optional. Defines the percent of disk usage before which image garbage collection is never run. Lowest disk usage to garbage collect to. The percent is calculated as this field value out of 100.

The value must be between 10 and 85, inclusive and smaller than image_gc_high_threshold_percent.

The default value is 80 if unspecified. 




### #image_maximum_gc_age
    
    
    def image_maximum_gc_age() -> ::String

**Returns**

  * (::String) — Optional. Defines the maximum age an image can be unused before it is garbage collected. The string must be a sequence of decimal numbers, each with optional fraction and a unit suffix, such as "300s", "1.5h", and "2h45m". Valid time units are "ns", "us" (or "µs"), "ms", "s", "m", "h".

The value must be a positive duration greater than image_minimum_gc_age or "0s".

The default value is "0s" if unspecified, which disables this field, meaning images won't be garbage collected based on being unused for too long. 




### #image_maximum_gc_age=
    
    
    def image_maximum_gc_age=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Defines the maximum age an image can be unused before it is garbage collected. The string must be a sequence of decimal numbers, each with optional fraction and a unit suffix, such as "300s", "1.5h", and "2h45m". Valid time units are "ns", "us" (or "µs"), "ms", "s", "m", "h".

The value must be a positive duration greater than image_minimum_gc_age or "0s".

The default value is "0s" if unspecified, which disables this field, meaning images won't be garbage collected based on being unused for too long. 




**Returns**

  * (::String) — Optional. Defines the maximum age an image can be unused before it is garbage collected. The string must be a sequence of decimal numbers, each with optional fraction and a unit suffix, such as "300s", "1.5h", and "2h45m". Valid time units are "ns", "us" (or "µs"), "ms", "s", "m", "h".

The value must be a positive duration greater than image_minimum_gc_age or "0s".

The default value is "0s" if unspecified, which disables this field, meaning images won't be garbage collected based on being unused for too long. 




### #image_minimum_gc_age
    
    
    def image_minimum_gc_age() -> ::String

**Returns**

  * (::String) — Optional. Defines the minimum age for an unused image before it is garbage collected.

The string must be a sequence of decimal numbers, each with optional fraction and a unit suffix, such as "300s", "1.5h", and "2h45m". Valid time units are "ns", "us" (or "µs"), "ms", "s", "m", "h".

The value must be a positive duration less than or equal to 2 minutes.

The default value is "2m0s" if unspecified. 




### #image_minimum_gc_age=
    
    
    def image_minimum_gc_age=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Defines the minimum age for an unused image before it is garbage collected.

The string must be a sequence of decimal numbers, each with optional fraction and a unit suffix, such as "300s", "1.5h", and "2h45m". Valid time units are "ns", "us" (or "µs"), "ms", "s", "m", "h".

The value must be a positive duration less than or equal to 2 minutes.

The default value is "2m0s" if unspecified. 




**Returns**

  * (::String) — Optional. Defines the minimum age for an unused image before it is garbage collected.

The string must be a sequence of decimal numbers, each with optional fraction and a unit suffix, such as "300s", "1.5h", and "2h45m". Valid time units are "ns", "us" (or "µs"), "ms", "s", "m", "h".

The value must be a positive duration less than or equal to 2 minutes.

The default value is "2m0s" if unspecified. 




### #insecure_kubelet_readonly_port_enabled
    
    
    def insecure_kubelet_readonly_port_enabled() -> ::Boolean

**Returns**

  * (::Boolean) — Enable or disable Kubelet read only port. 



### #insecure_kubelet_readonly_port_enabled=
    
    
    def insecure_kubelet_readonly_port_enabled=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Enable or disable Kubelet read only port. 



**Returns**

  * (::Boolean) — Enable or disable Kubelet read only port. 



### #max_parallel_image_pulls
    
    
    def max_parallel_image_pulls() -> ::Integer

**Returns**

  * (::Integer) — Optional. Defines the maximum number of image pulls in parallel. The range is 2 to 5, inclusive. The default value is 2 or 3 depending on the disk type.

See https://kubernetes.io/docs/concepts/containers/images/#maximum-parallel-image-pulls for more details. 




### #max_parallel_image_pulls=
    
    
    def max_parallel_image_pulls=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Defines the maximum number of image pulls in parallel. The range is 2 to 5, inclusive. The default value is 2 or 3 depending on the disk type.

See https://kubernetes.io/docs/concepts/containers/images/#maximum-parallel-image-pulls for more details. 




**Returns**

  * (::Integer) — Optional. Defines the maximum number of image pulls in parallel. The range is 2 to 5, inclusive. The default value is 2 or 3 depending on the disk type.

See https://kubernetes.io/docs/concepts/containers/images/#maximum-parallel-image-pulls for more details. 




### #memory_manager
    
    
    def memory_manager() -> ::Google::Cloud::Container::V1beta1::MemoryManager

**Returns**

  * ([::Google::Cloud::Container::V1beta1::MemoryManager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Cloud-Container-V1beta1-MemoryManager)) — Optional. Controls NUMA-aware Memory Manager configuration on the node. For more information, see: https://kubernetes.io/docs/tasks/administer-cluster/memory-manager/ 



### #memory_manager=
    
    
    def memory_manager=(value) -> ::Google::Cloud::Container::V1beta1::MemoryManager

**Parameter**

  * **value** ([::Google::Cloud::Container::V1beta1::MemoryManager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Cloud-Container-V1beta1-MemoryManager)) — Optional. Controls NUMA-aware Memory Manager configuration on the node. For more information, see: https://kubernetes.io/docs/tasks/administer-cluster/memory-manager/ 



**Returns**

  * ([::Google::Cloud::Container::V1beta1::MemoryManager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Cloud-Container-V1beta1-MemoryManager)) — Optional. Controls NUMA-aware Memory Manager configuration on the node. For more information, see: https://kubernetes.io/docs/tasks/administer-cluster/memory-manager/ 



### #pod_pids_limit
    
    
    def pod_pids_limit() -> ::Integer

**Returns**

  * (::Integer) — Set the Pod PID limits. See https://kubernetes.io/docs/concepts/policy/pid-limiting/#pod-pid-limits

Controls the maximum number of processes allowed to run in a pod. The value must be greater than or equal to 1024 and less than 4194304. 




### #pod_pids_limit=
    
    
    def pod_pids_limit=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Set the Pod PID limits. See https://kubernetes.io/docs/concepts/policy/pid-limiting/#pod-pid-limits

Controls the maximum number of processes allowed to run in a pod. The value must be greater than or equal to 1024 and less than 4194304. 




**Returns**

  * (::Integer) — Set the Pod PID limits. See https://kubernetes.io/docs/concepts/policy/pid-limiting/#pod-pid-limits

Controls the maximum number of processes allowed to run in a pod. The value must be greater than or equal to 1024 and less than 4194304. 




### #shutdown_grace_period_critical_pods_seconds
    
    
    def shutdown_grace_period_critical_pods_seconds() -> ::Integer

**Returns**

  * (::Integer) — Optional. shutdown_grace_period_critical_pods_seconds is the maximum allowed grace period (in seconds) used to terminate critical pods during a node shutdown. This value should be <= shutdown_grace_period_seconds, and is only valid if shutdown_grace_period_seconds is set. https://kubernetes.io/docs/concepts/cluster-administration/node-shutdown/ Range: [0, 120]. 



### #shutdown_grace_period_critical_pods_seconds=
    
    
    def shutdown_grace_period_critical_pods_seconds=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. shutdown_grace_period_critical_pods_seconds is the maximum allowed grace period (in seconds) used to terminate critical pods during a node shutdown. This value should be <= shutdown_grace_period_seconds, and is only valid if shutdown_grace_period_seconds is set. https://kubernetes.io/docs/concepts/cluster-administration/node-shutdown/ Range: [0, 120]. 



**Returns**

  * (::Integer) — Optional. shutdown_grace_period_critical_pods_seconds is the maximum allowed grace period (in seconds) used to terminate critical pods during a node shutdown. This value should be <= shutdown_grace_period_seconds, and is only valid if shutdown_grace_period_seconds is set. https://kubernetes.io/docs/concepts/cluster-administration/node-shutdown/ Range: [0, 120]. 



### #shutdown_grace_period_seconds
    
    
    def shutdown_grace_period_seconds() -> ::Integer

**Returns**

  * (::Integer) — Optional. shutdown_grace_period_seconds is the maximum allowed grace period (in seconds) the total duration that the node should delay the shutdown during a graceful shutdown. This is the total grace period for pod termination for both regular and critical pods. https://kubernetes.io/docs/concepts/cluster-administration/node-shutdown/ If set to 0, node will not enable the graceful node shutdown functionality. This field is only valid for Spot VMs. Allowed values: 0, 30, 120. 



### #shutdown_grace_period_seconds=
    
    
    def shutdown_grace_period_seconds=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. shutdown_grace_period_seconds is the maximum allowed grace period (in seconds) the total duration that the node should delay the shutdown during a graceful shutdown. This is the total grace period for pod termination for both regular and critical pods. https://kubernetes.io/docs/concepts/cluster-administration/node-shutdown/ If set to 0, node will not enable the graceful node shutdown functionality. This field is only valid for Spot VMs. Allowed values: 0, 30, 120. 



**Returns**

  * (::Integer) — Optional. shutdown_grace_period_seconds is the maximum allowed grace period (in seconds) the total duration that the node should delay the shutdown during a graceful shutdown. This is the total grace period for pod termination for both regular and critical pods. https://kubernetes.io/docs/concepts/cluster-administration/node-shutdown/ If set to 0, node will not enable the graceful node shutdown functionality. This field is only valid for Spot VMs. Allowed values: 0, 30, 120. 



### #single_process_oom_kill
    
    
    def single_process_oom_kill() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. Defines whether to enable single process OOM killer. If true, will prevent the memory.oom.group flag from being set for container cgroups in cgroups v2. This causes processes in the container to be OOM killed individually instead of as a group. 



### #single_process_oom_kill=
    
    
    def single_process_oom_kill=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. Defines whether to enable single process OOM killer. If true, will prevent the memory.oom.group flag from being set for container cgroups in cgroups v2. This causes processes in the container to be OOM killed individually instead of as a group. 



**Returns**

  * (::Boolean) — Optional. Defines whether to enable single process OOM killer. If true, will prevent the memory.oom.group flag from being set for container cgroups in cgroups v2. This causes processes in the container to be OOM killed individually instead of as a group. 



### #topology_manager
    
    
    def topology_manager() -> ::Google::Cloud::Container::V1beta1::TopologyManager

**Returns**

  * ([::Google::Cloud::Container::V1beta1::TopologyManager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Cloud-Container-V1beta1-TopologyManager)) — Optional. Controls Topology Manager configuration on the node. For more information, see: https://kubernetes.io/docs/tasks/administer-cluster/topology-manager/ 



### #topology_manager=
    
    
    def topology_manager=(value) -> ::Google::Cloud::Container::V1beta1::TopologyManager

**Parameter**

  * **value** ([::Google::Cloud::Container::V1beta1::TopologyManager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Cloud-Container-V1beta1-TopologyManager)) — Optional. Controls Topology Manager configuration on the node. For more information, see: https://kubernetes.io/docs/tasks/administer-cluster/topology-manager/ 



**Returns**

  * ([::Google::Cloud::Container::V1beta1::TopologyManager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Cloud-Container-V1beta1-TopologyManager)) — Optional. Controls Topology Manager configuration on the node. For more information, see: https://kubernetes.io/docs/tasks/administer-cluster/topology-manager/ 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
