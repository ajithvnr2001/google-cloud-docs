---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.MaintenancePolicy
title: Google Cloud Memorystore for Redis v1beta1 API - Class MaintenancePolicy (3.0.0-beta06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:00:03.143450+00:00
---

# Google Cloud Memorystore for Redis v1beta1 API - Class MaintenancePolicy (3.0.0-beta06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.MaintenancePolicy

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Memorystore for Redis v1beta1 API - Class MaintenancePolicy (3.0.0-beta06) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.0.0-beta06 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.MaintenancePolicy)
  * [ 3.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/3.0.0-beta05/Google.Cloud.Redis.V1Beta1.MaintenancePolicy)
  * [ 2.0.0-beta09 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/2.0.0-beta09/Google.Cloud.Redis.V1Beta1.MaintenancePolicy)


    
    
    public sealed class MaintenancePolicy : IMessage<MaintenancePolicy>, IEquatable<MaintenancePolicy>, IDeepCloneable<MaintenancePolicy>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Memorystore for Redis v1beta1 API class MaintenancePolicy.

Maintenance policy for an instance.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > MaintenancePolicy

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[MaintenancePolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.MaintenancePolicy), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[MaintenancePolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.MaintenancePolicy), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[MaintenancePolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.MaintenancePolicy), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Redis.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1)

## Assembly

Google.Cloud.Redis.V1Beta1.dll

## Constructors 

### MaintenancePolicy()
    
    
    public MaintenancePolicy()

### MaintenancePolicy(MaintenancePolicy)
    
    
    public MaintenancePolicy(MaintenancePolicy other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[MaintenancePolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.MaintenancePolicy)`  
  
  
## Properties 

### CreateTime
    
    
    public Timestamp CreateTime { get; set; }

Output only. The time when the policy was created.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### Description
    
    
    public string Description { get; set; }

Optional. Description of what this policy is for. Create/Update methods return INVALID_ARGUMENT if the length is greater than 512.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### UpdateTime
    
    
    public Timestamp UpdateTime { get; set; }

Output only. The time when the policy was last updated.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### WeeklyMaintenanceWindow
    
    
    public RepeatedField<WeeklyMaintenanceWindow> WeeklyMaintenanceWindow { get; }

Optional. Maintenance window that is applied to resources covered by this policy. Minimum 1. For the current version, the maximum number of weekly_window is expected to be one.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[WeeklyMaintenanceWindow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.WeeklyMaintenanceWindow)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
