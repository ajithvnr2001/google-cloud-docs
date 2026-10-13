---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.AutoscalingConfig.Types.AsymmetricAutoscalingOption.Types.AutoscalingConfigOverrides
title: Google Cloud Spanner Instance Administration v1 API - Class AutoscalingConfig.Types.AsymmetricAutoscalingOption.Types.AutoscalingConfigOverrides (5.13.0-beta11) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:11:54.996134+00:00
---

# Google Cloud Spanner Instance Administration v1 API - Class AutoscalingConfig.Types.AsymmetricAutoscalingOption.Types.AutoscalingConfigOverrides (5.13.0-beta11)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.AutoscalingConfig.Types.AsymmetricAutoscalingOption.Types.AutoscalingConfigOverrides

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Spanner Instance Administration v1 API - Class AutoscalingConfig.Types.AsymmetricAutoscalingOption.Types.AutoscalingConfigOverrides (5.13.0-beta11) Stay organized with collections  Save and categorize content based on your preferences. 

5.13.0-beta11  5.13.0-beta10  5.12.0 (latest)  5.11.0  5.10.0  5.9.0  5.8.0  5.7.0  5.6.0  5.5.0  5.4.0  5.3.0  5.2.0  5.1.0  5.0.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.15.1  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0 
    
    
    public sealed class AutoscalingConfig.Types.AsymmetricAutoscalingOption.Types.AutoscalingConfigOverrides : IMessage<AutoscalingConfig.Types.AsymmetricAutoscalingOption.Types.AutoscalingConfigOverrides>, IEquatable<AutoscalingConfig.Types.AsymmetricAutoscalingOption.Types.AutoscalingConfigOverrides>, IDeepCloneable<AutoscalingConfig.Types.AsymmetricAutoscalingOption.Types.AutoscalingConfigOverrides>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Spanner Instance Administration v1 API class AutoscalingConfig.Types.AsymmetricAutoscalingOption.Types.AutoscalingConfigOverrides.

Overrides the top-level autoscaling configuration for the replicas identified by `replica_selection`. All fields in this message are optional. Any unspecified fields will use the corresponding values from the top-level autoscaling configuration.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AutoscalingConfig.Types.AsymmetricAutoscalingOption.Types.AutoscalingConfigOverrides

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AutoscalingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.AutoscalingConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.AutoscalingConfig.Types)[AsymmetricAutoscalingOption](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.AutoscalingConfig.Types.AsymmetricAutoscalingOption)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.AutoscalingConfig.Types.AsymmetricAutoscalingOption.Types)[AutoscalingConfigOverrides](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.AutoscalingConfig.Types.AsymmetricAutoscalingOption.Types.AutoscalingConfigOverrides), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AutoscalingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.AutoscalingConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.AutoscalingConfig.Types)[AsymmetricAutoscalingOption](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.AutoscalingConfig.Types.AsymmetricAutoscalingOption)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.AutoscalingConfig.Types.AsymmetricAutoscalingOption.Types)[AutoscalingConfigOverrides](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.AutoscalingConfig.Types.AsymmetricAutoscalingOption.Types.AutoscalingConfigOverrides), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AutoscalingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.AutoscalingConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.AutoscalingConfig.Types)[AsymmetricAutoscalingOption](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.AutoscalingConfig.Types.AsymmetricAutoscalingOption)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.AutoscalingConfig.Types.AsymmetricAutoscalingOption.Types)[AutoscalingConfigOverrides](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.AutoscalingConfig.Types.AsymmetricAutoscalingOption.Types.AutoscalingConfigOverrides), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Spanner.Admin.Instance.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1)

## Assembly

Google.Cloud.Spanner.Admin.Instance.V1.dll

## Constructors 

### AutoscalingConfigOverrides()
    
    
    public AutoscalingConfigOverrides()

### AutoscalingConfigOverrides(AutoscalingConfigOverrides)
    
    
    public AutoscalingConfigOverrides(AutoscalingConfig.Types.AsymmetricAutoscalingOption.Types.AutoscalingConfigOverrides other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AutoscalingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.AutoscalingConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.AutoscalingConfig.Types)[AsymmetricAutoscalingOption](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.AutoscalingConfig.Types.AsymmetricAutoscalingOption)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.AutoscalingConfig.Types.AsymmetricAutoscalingOption.Types)[AutoscalingConfigOverrides](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.AutoscalingConfig.Types.AsymmetricAutoscalingOption.Types.AutoscalingConfigOverrides)`  
  
  
## Properties 

### AutoscalingLimits
    
    
    public AutoscalingConfig.Types.AutoscalingLimits AutoscalingLimits { get; set; }

Optional. If specified, overrides the min/max limit in the top-level autoscaling configuration for the selected replicas.

**Property Value**  
---  
**Type** | **Description**  
`[AutoscalingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.AutoscalingConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.AutoscalingConfig.Types)[AutoscalingLimits](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.AutoscalingConfig.Types.AutoscalingLimits)` |   
  
### AutoscalingTargetHighPriorityCpuUtilizationPercent
    
    
    public int AutoscalingTargetHighPriorityCpuUtilizationPercent { get; set; }

Optional. If specified, overrides the autoscaling target high_priority_cpu_utilization_percent in the top-level autoscaling configuration for the selected replicas.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### AutoscalingTargetTotalCpuUtilizationPercent
    
    
    public int AutoscalingTargetTotalCpuUtilizationPercent { get; set; }

Optional. If specified, overrides the autoscaling target `total_cpu_utilization_percent` in the top-level autoscaling configuration for the selected replicas.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### DisableHighPriorityCpuAutoscaling
    
    
    public bool DisableHighPriorityCpuAutoscaling { get; set; }

Optional. If true, disables high priority CPU autoscaling for the selected replicas and ignores [high_priority_cpu_utilization_percent][google.spanner.admin.instance.v1.AutoscalingConfig.AutoscalingTargets.high_priority_cpu_utilization_percent] in the top-level autoscaling configuration.

When setting this field to true, setting [autoscaling_target_high_priority_cpu_utilization_percent][google.spanner.admin.instance.v1.AutoscalingConfig.AsymmetricAutoscalingOption.AutoscalingConfigOverrides.autoscaling_target_high_priority_cpu_utilization_percent] field to a non-zero value for the same replica is not supported.

If false, the [autoscaling_target_high_priority_cpu_utilization_percent][google.spanner.admin.instance.v1.AutoscalingConfig.AsymmetricAutoscalingOption.AutoscalingConfigOverrides.autoscaling_target_high_priority_cpu_utilization_percent] field in the replica will be used if set to a non-zero value. Otherwise, the [high_priority_cpu_utilization_percent][google.spanner.admin.instance.v1.AutoscalingConfig.AutoscalingTargets.high_priority_cpu_utilization_percent] field in the top-level autoscaling configuration will be used.

Setting both [disable_high_priority_cpu_autoscaling][google.spanner.admin.instance.v1.AutoscalingConfig.AsymmetricAutoscalingOption.AutoscalingConfigOverrides.disable_high_priority_cpu_autoscaling] and [disable_total_cpu_autoscaling][google.spanner.admin.instance.v1.AutoscalingConfig.AsymmetricAutoscalingOption.AutoscalingConfigOverrides.disable_total_cpu_autoscaling] to true for the same replica is not supported.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### DisableTotalCpuAutoscaling
    
    
    public bool DisableTotalCpuAutoscaling { get; set; }

Optional. If true, disables total CPU autoscaling for the selected replicas and ignores [total_cpu_utilization_percent][google.spanner.admin.instance.v1.AutoscalingConfig.AutoscalingTargets.total_cpu_utilization_percent] in the top-level autoscaling configuration.

When setting this field to true, setting [autoscaling_target_total_cpu_utilization_percent][google.spanner.admin.instance.v1.AutoscalingConfig.AsymmetricAutoscalingOption.AutoscalingConfigOverrides.autoscaling_target_total_cpu_utilization_percent] field to a non-zero value for the same replica is not supported.

If false, the [autoscaling_target_total_cpu_utilization_percent][google.spanner.admin.instance.v1.AutoscalingConfig.AsymmetricAutoscalingOption.AutoscalingConfigOverrides.autoscaling_target_total_cpu_utilization_percent] field in the replica will be used if set to a non-zero value. Otherwise, the [total_cpu_utilization_percent][google.spanner.admin.instance.v1.AutoscalingConfig.AutoscalingTargets.total_cpu_utilization_percent] field in the top-level autoscaling configuration will be used.

Setting both [disable_high_priority_cpu_autoscaling][google.spanner.admin.instance.v1.AutoscalingConfig.AsymmetricAutoscalingOption.AutoscalingConfigOverrides.disable_high_priority_cpu_autoscaling] and [disable_total_cpu_autoscaling][google.spanner.admin.instance.v1.AutoscalingConfig.AsymmetricAutoscalingOption.AutoscalingConfigOverrides.disable_total_cpu_autoscaling] to true for the same replica is not supported.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-17 UTC."],[],[]] 
