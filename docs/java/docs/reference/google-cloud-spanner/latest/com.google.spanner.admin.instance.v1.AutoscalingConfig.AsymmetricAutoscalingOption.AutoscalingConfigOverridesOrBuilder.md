---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.AutoscalingConfig.AsymmetricAutoscalingOption.AutoscalingConfigOverridesOrBuilder
title: Interface AutoscalingConfig.AsymmetricAutoscalingOption.AutoscalingConfigOverridesOrBuilder (6.124.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:12:46.535221+00:00
---

# Interface AutoscalingConfig.AsymmetricAutoscalingOption.AutoscalingConfigOverridesOrBuilder (6.124.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.AutoscalingConfig.AsymmetricAutoscalingOption.AutoscalingConfigOverridesOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface AutoscalingConfig.AsymmetricAutoscalingOption.AutoscalingConfigOverridesOrBuilder (6.124.0) Stay organized with collections  Save and categorize content based on your preferences. 

6.124.0 (latest)  6.120.0  6.119.0  6.118.0  6.116.0  6.111.1  6.108.0  6.107.0  6.103.0  6.102.1  6.101.1  6.100.0  6.99.0  6.98.1  6.97.1  6.96.1  6.95.1  6.94.0  6.93.0  6.89.0  6.88.0  6.87.0  6.86.0  6.85.0  6.83.0  6.82.0  6.80.1  6.79.0  6.77.0  6.74.1  6.72.0  6.71.0  6.69.0  6.68.0  6.66.0  6.65.1  6.62.0  6.60.0  6.58.0  6.57.0  6.56.0  6.55.0  6.54.0  6.53.0  6.52.1  6.51.0  6.50.1  6.49.0  6.25.1  6.24.0  6.23.4  6.22.0  6.21.2  6.20.0  6.19.1  6.18.0  6.17.4  6.14.1 
    
    
    public static interface AutoscalingConfig.AsymmetricAutoscalingOption.AutoscalingConfigOverridesOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAutoscalingLimits()
    
    
    public abstract AutoscalingConfig.AutoscalingLimits getAutoscalingLimits()

Optional. If specified, overrides the min/max limit in the top-level autoscaling configuration for the selected replicas.

` .google.spanner.admin.instance.v1.AutoscalingConfig.AutoscalingLimits autoscaling_limits = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[AutoscalingConfig.AutoscalingLimits](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.AutoscalingConfig.AutoscalingLimits)` | The autoscalingLimits.  
  
### getAutoscalingLimitsOrBuilder()
    
    
    public abstract AutoscalingConfig.AutoscalingLimitsOrBuilder getAutoscalingLimitsOrBuilder()

Optional. If specified, overrides the min/max limit in the top-level autoscaling configuration for the selected replicas.

` .google.spanner.admin.instance.v1.AutoscalingConfig.AutoscalingLimits autoscaling_limits = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[AutoscalingConfig.AutoscalingLimitsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.AutoscalingConfig.AutoscalingLimitsOrBuilder)` |   
  
### getAutoscalingTargetHighPriorityCpuUtilizationPercent()
    
    
    public abstract int getAutoscalingTargetHighPriorityCpuUtilizationPercent()

Optional. If specified, overrides the autoscaling target high_priority_cpu_utilization_percent in the top-level autoscaling configuration for the selected replicas.

` int32 autoscaling_target_high_priority_cpu_utilization_percent = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The autoscalingTargetHighPriorityCpuUtilizationPercent.  
  
### getAutoscalingTargetTotalCpuUtilizationPercent()
    
    
    public abstract int getAutoscalingTargetTotalCpuUtilizationPercent()

Optional. If specified, overrides the autoscaling target `total_cpu_utilization_percent` in the top-level autoscaling configuration for the selected replicas.

` int32 autoscaling_target_total_cpu_utilization_percent = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The autoscalingTargetTotalCpuUtilizationPercent.  
  
### getDisableHighPriorityCpuAutoscaling()
    
    
    public abstract boolean getDisableHighPriorityCpuAutoscaling()

Optional. If true, disables high priority CPU autoscaling for the selected replicas and ignores high_priority_cpu_utilization_percent in the top-level autoscaling configuration.

When setting this field to true, setting autoscaling_target_high_priority_cpu_utilization_percent field to a non-zero value for the same replica is not supported.

If false, the autoscaling_target_high_priority_cpu_utilization_percent field in the replica will be used if set to a non-zero value. Otherwise, the high_priority_cpu_utilization_percent field in the top-level autoscaling configuration will be used.

Setting both disable_high_priority_cpu_autoscaling and disable_total_cpu_autoscaling to true for the same replica is not supported.

` bool disable_high_priority_cpu_autoscaling = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The disableHighPriorityCpuAutoscaling.  
  
### getDisableTotalCpuAutoscaling()
    
    
    public abstract boolean getDisableTotalCpuAutoscaling()

Optional. If true, disables total CPU autoscaling for the selected replicas and ignores total_cpu_utilization_percent in the top-level autoscaling configuration.

When setting this field to true, setting autoscaling_target_total_cpu_utilization_percent field to a non-zero value for the same replica is not supported.

If false, the autoscaling_target_total_cpu_utilization_percent field in the replica will be used if set to a non-zero value. Otherwise, the total_cpu_utilization_percent field in the top-level autoscaling configuration will be used.

Setting both disable_high_priority_cpu_autoscaling and disable_total_cpu_autoscaling to true for the same replica is not supported.

`bool disable_total_cpu_autoscaling = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The disableTotalCpuAutoscaling.  
  
### hasAutoscalingLimits()
    
    
    public abstract boolean hasAutoscalingLimits()

Optional. If specified, overrides the min/max limit in the top-level autoscaling configuration for the selected replicas.

` .google.spanner.admin.instance.v1.AutoscalingConfig.AutoscalingLimits autoscaling_limits = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the autoscalingLimits field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
