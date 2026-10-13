---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AutoscalingPolicy/
title: Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::AutoscalingPolicy (v4.0.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:09:32.611628+00:00
---

# Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::AutoscalingPolicy (v4.0.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AutoscalingPolicy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::AutoscalingPolicy (v4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.12.0  3.10.0  3.9.1  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.22.0  2.21.1  2.20.0  2.19.1  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.2  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.10.0  1.9.0  1.8.0  1.7.1  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.5.0 

Reference documentation and code samples for the Google Cloud Compute V1 API class Google::Cloud::Compute::V1::AutoscalingPolicy.

Cloud Autoscaler policy.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #cool_down_period_sec
    
    
    def cool_down_period_sec() -> ::Integer

**Returns**

  * (::Integer) — The number of seconds that your application takes to initialize on a VM instance. This is referred to as the [initialization period](https://docs.cloud.google.com/compute/docs/autoscaler#cool_down_period). Specifying an accurate initialization period improves autoscaler decisions. For example, when scaling out, the autoscaler ignores data from VMs that are still initializing because those VMs might not yet represent normal usage of your application. The default initialization period is 60 seconds.

Initialization periods might vary because of numerous factors. We recommend that you test how long your application takes to initialize. To do this, create a VM and time your application's startup process. 




### #cool_down_period_sec=
    
    
    def cool_down_period_sec=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The number of seconds that your application takes to initialize on a VM instance. This is referred to as the [initialization period](https://docs.cloud.google.com/compute/docs/autoscaler#cool_down_period). Specifying an accurate initialization period improves autoscaler decisions. For example, when scaling out, the autoscaler ignores data from VMs that are still initializing because those VMs might not yet represent normal usage of your application. The default initialization period is 60 seconds.

Initialization periods might vary because of numerous factors. We recommend that you test how long your application takes to initialize. To do this, create a VM and time your application's startup process. 




**Returns**

  * (::Integer) — The number of seconds that your application takes to initialize on a VM instance. This is referred to as the [initialization period](https://docs.cloud.google.com/compute/docs/autoscaler#cool_down_period). Specifying an accurate initialization period improves autoscaler decisions. For example, when scaling out, the autoscaler ignores data from VMs that are still initializing because those VMs might not yet represent normal usage of your application. The default initialization period is 60 seconds.

Initialization periods might vary because of numerous factors. We recommend that you test how long your application takes to initialize. To do this, create a VM and time your application's startup process. 




### #cpu_utilization
    
    
    def cpu_utilization() -> ::Google::Cloud::Compute::V1::AutoscalingPolicyCpuUtilization

**Returns**

  * ([::Google::Cloud::Compute::V1::AutoscalingPolicyCpuUtilization](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AutoscalingPolicyCpuUtilization)) — Defines the CPU utilization policy that allows the autoscaler to scale based on the average CPU utilization of a managed instance group. 



### #cpu_utilization=
    
    
    def cpu_utilization=(value) -> ::Google::Cloud::Compute::V1::AutoscalingPolicyCpuUtilization

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::AutoscalingPolicyCpuUtilization](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AutoscalingPolicyCpuUtilization)) — Defines the CPU utilization policy that allows the autoscaler to scale based on the average CPU utilization of a managed instance group. 



**Returns**

  * ([::Google::Cloud::Compute::V1::AutoscalingPolicyCpuUtilization](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AutoscalingPolicyCpuUtilization)) — Defines the CPU utilization policy that allows the autoscaler to scale based on the average CPU utilization of a managed instance group. 



### #custom_metric_utilizations
    
    
    def custom_metric_utilizations() -> ::Array<::Google::Cloud::Compute::V1::AutoscalingPolicyCustomMetricUtilization>

**Returns**

  * (::Array<[::Google::Cloud::Compute::V1::AutoscalingPolicyCustomMetricUtilization](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AutoscalingPolicyCustomMetricUtilization)>) — Configuration parameters of autoscaling based on a custom metric. 



### #custom_metric_utilizations=
    
    
    def custom_metric_utilizations=(value) -> ::Array<::Google::Cloud::Compute::V1::AutoscalingPolicyCustomMetricUtilization>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Compute::V1::AutoscalingPolicyCustomMetricUtilization](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AutoscalingPolicyCustomMetricUtilization)>) — Configuration parameters of autoscaling based on a custom metric. 



**Returns**

  * (::Array<[::Google::Cloud::Compute::V1::AutoscalingPolicyCustomMetricUtilization](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AutoscalingPolicyCustomMetricUtilization)>) — Configuration parameters of autoscaling based on a custom metric. 



### #load_balancing_utilization
    
    
    def load_balancing_utilization() -> ::Google::Cloud::Compute::V1::AutoscalingPolicyLoadBalancingUtilization

**Returns**

  * ([::Google::Cloud::Compute::V1::AutoscalingPolicyLoadBalancingUtilization](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AutoscalingPolicyLoadBalancingUtilization)) — Configuration parameters of autoscaling based on load balancer. 



### #load_balancing_utilization=
    
    
    def load_balancing_utilization=(value) -> ::Google::Cloud::Compute::V1::AutoscalingPolicyLoadBalancingUtilization

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::AutoscalingPolicyLoadBalancingUtilization](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AutoscalingPolicyLoadBalancingUtilization)) — Configuration parameters of autoscaling based on load balancer. 



**Returns**

  * ([::Google::Cloud::Compute::V1::AutoscalingPolicyLoadBalancingUtilization](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AutoscalingPolicyLoadBalancingUtilization)) — Configuration parameters of autoscaling based on load balancer. 



### #max_num_replicas
    
    
    def max_num_replicas() -> ::Integer

**Returns**

  * (::Integer) — The maximum number of instances that the autoscaler can scale out to. This is required when creating or updating an autoscaler. The maximum number of replicas must not be lower than minimal number of replicas. 



### #max_num_replicas=
    
    
    def max_num_replicas=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The maximum number of instances that the autoscaler can scale out to. This is required when creating or updating an autoscaler. The maximum number of replicas must not be lower than minimal number of replicas. 



**Returns**

  * (::Integer) — The maximum number of instances that the autoscaler can scale out to. This is required when creating or updating an autoscaler. The maximum number of replicas must not be lower than minimal number of replicas. 



### #min_num_replicas
    
    
    def min_num_replicas() -> ::Integer

**Returns**

  * (::Integer) — The minimum number of replicas that the autoscaler can scale in to. This cannot be less than 0. If not provided, autoscaler chooses a default value depending on maximum number of instances allowed. 



### #min_num_replicas=
    
    
    def min_num_replicas=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The minimum number of replicas that the autoscaler can scale in to. This cannot be less than 0. If not provided, autoscaler chooses a default value depending on maximum number of instances allowed. 



**Returns**

  * (::Integer) — The minimum number of replicas that the autoscaler can scale in to. This cannot be less than 0. If not provided, autoscaler chooses a default value depending on maximum number of instances allowed. 



### #mode
    
    
    def mode() -> ::String

**Returns**

  * (::String) — Defines the operating mode for this policy. The following modes are available:

    * OFF: Disables the autoscaler but maintains its configuration.
    * ONLY_SCALE_OUT: Restricts the autoscaler to add VM instances only.
    * ON: Enables all autoscaler activities according to its policy.

For more information, see "Turning off or restricting an autoscaler" Check the Mode enum for the list of possible values. 




### #mode=
    
    
    def mode=(value) -> ::String

**Parameter**

  * **value** (::String) — Defines the operating mode for this policy. The following modes are available:

    * OFF: Disables the autoscaler but maintains its configuration.
    * ONLY_SCALE_OUT: Restricts the autoscaler to add VM instances only.
    * ON: Enables all autoscaler activities according to its policy.

For more information, see "Turning off or restricting an autoscaler" Check the Mode enum for the list of possible values. 




**Returns**

  * (::String) — Defines the operating mode for this policy. The following modes are available:

    * OFF: Disables the autoscaler but maintains its configuration.
    * ONLY_SCALE_OUT: Restricts the autoscaler to add VM instances only.
    * ON: Enables all autoscaler activities according to its policy.

For more information, see "Turning off or restricting an autoscaler" Check the Mode enum for the list of possible values. 




### #scale_in_control
    
    
    def scale_in_control() -> ::Google::Cloud::Compute::V1::AutoscalingPolicyScaleInControl

**Returns**

  * ([::Google::Cloud::Compute::V1::AutoscalingPolicyScaleInControl](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AutoscalingPolicyScaleInControl)) 



### #scale_in_control=
    
    
    def scale_in_control=(value) -> ::Google::Cloud::Compute::V1::AutoscalingPolicyScaleInControl

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::AutoscalingPolicyScaleInControl](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AutoscalingPolicyScaleInControl)) 



**Returns**

  * ([::Google::Cloud::Compute::V1::AutoscalingPolicyScaleInControl](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AutoscalingPolicyScaleInControl)) 



### #scaling_schedules
    
    
    def scaling_schedules() -> ::Google::Protobuf::Map{::String => ::Google::Cloud::Compute::V1::AutoscalingPolicyScalingSchedule}

**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Cloud::Compute::V1::AutoscalingPolicyScalingSchedule}) — Scaling schedules defined for an autoscaler. Multiple schedules can be set on an autoscaler, and they can overlap. During overlapping periods the greatest min_required_replicas of all scaling schedules is applied. Up to 128 scaling schedules are allowed. 



### #scaling_schedules=
    
    
    def scaling_schedules=(value) -> ::Google::Protobuf::Map{::String => ::Google::Cloud::Compute::V1::AutoscalingPolicyScalingSchedule}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::Google::Cloud::Compute::V1::AutoscalingPolicyScalingSchedule}) — Scaling schedules defined for an autoscaler. Multiple schedules can be set on an autoscaler, and they can overlap. During overlapping periods the greatest min_required_replicas of all scaling schedules is applied. Up to 128 scaling schedules are allowed. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Cloud::Compute::V1::AutoscalingPolicyScalingSchedule}) — Scaling schedules defined for an autoscaler. Multiple schedules can be set on an autoscaler, and they can overlap. During overlapping periods the greatest min_required_replicas of all scaling schedules is applied. Up to 128 scaling schedules are allowed. 



### #stabilization_period_sec
    
    
    def stabilization_period_sec() -> ::Integer

**Returns**

  * (::Integer) — The number of seconds that autoscaler waits for load stabilization before making scale-in decisions. This is referred to as the [stabilization period](https://docs.cloud.google.com/compute/docs/autoscaler#stabilization_period). This might appear as a delay in scaling in but it is an important mechanism for your application to not have fluctuating size due to short term load fluctuations.

The default stabilization period is 600 seconds. 




### #stabilization_period_sec=
    
    
    def stabilization_period_sec=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The number of seconds that autoscaler waits for load stabilization before making scale-in decisions. This is referred to as the [stabilization period](https://docs.cloud.google.com/compute/docs/autoscaler#stabilization_period). This might appear as a delay in scaling in but it is an important mechanism for your application to not have fluctuating size due to short term load fluctuations.

The default stabilization period is 600 seconds. 




**Returns**

  * (::Integer) — The number of seconds that autoscaler waits for load stabilization before making scale-in decisions. This is referred to as the [stabilization period](https://docs.cloud.google.com/compute/docs/autoscaler#stabilization_period). This might appear as a delay in scaling in but it is an important mechanism for your application to not have fluctuating size due to short term load fluctuations.

The default stabilization period is 600 seconds. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
