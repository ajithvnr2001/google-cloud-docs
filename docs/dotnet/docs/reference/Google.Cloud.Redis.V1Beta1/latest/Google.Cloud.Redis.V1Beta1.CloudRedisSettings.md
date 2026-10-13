---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.CloudRedisSettings
title: Google Cloud Memorystore for Redis v1beta1 API - Class CloudRedisSettings (3.0.0-beta06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:59:59.366168+00:00
---

# Google Cloud Memorystore for Redis v1beta1 API - Class CloudRedisSettings (3.0.0-beta06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.CloudRedisSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Memorystore for Redis v1beta1 API - Class CloudRedisSettings (3.0.0-beta06) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.0.0-beta06 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.CloudRedisSettings)
  * [ 3.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/3.0.0-beta05/Google.Cloud.Redis.V1Beta1.CloudRedisSettings)
  * [ 2.0.0-beta09 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/2.0.0-beta09/Google.Cloud.Redis.V1Beta1.CloudRedisSettings)


    
    
    public sealed class CloudRedisSettings : ServiceSettingsBase

Reference documentation and code samples for the Google Cloud Memorystore for Redis v1beta1 API class CloudRedisSettings.

Settings for [CloudRedisClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.CloudRedisClient) instances.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ServiceSettingsBase](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceSettingsBase.html) > CloudRedisSettings

## Inherited Members

[ServiceSettingsBase.VersionHeaderBuilder](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceSettingsBase.html#Google_Api_Gax_Grpc_ServiceSettingsBase_VersionHeaderBuilder)

[ServiceSettingsBase.CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceSettingsBase.html#Google_Api_Gax_Grpc_ServiceSettingsBase_CallSettings)

[ServiceSettingsBase.Clock](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceSettingsBase.html#Google_Api_Gax_Grpc_ServiceSettingsBase_Clock)

[ServiceSettingsBase.Scheduler](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceSettingsBase.html#Google_Api_Gax_Grpc_ServiceSettingsBase_Scheduler)

[ServiceSettingsBase.Interceptor](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceSettingsBase.html#Google_Api_Gax_Grpc_ServiceSettingsBase_Interceptor)

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Redis.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1)

## Assembly

Google.Cloud.Redis.V1Beta1.dll

## Constructors 

### CloudRedisSettings()
    
    
    public CloudRedisSettings()

Constructs a new [CloudRedisSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.CloudRedisSettings) object with default settings.

## Properties 

### CreateInstanceOperationsSettings
    
    
    public OperationsSettings CreateInstanceOperationsSettings { get; set; }

Long Running Operation settings for calls to `CloudRedisClient.CreateInstance` and `CloudRedisClient.CreateInstanceAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsSettings.html)` |   
**Remarks**

Uses default [PollSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PollSettings.html) of: 

  * Initial delay: 20 seconds.
  * Delay multiplier: 1.5
  * Maximum delay: 45 seconds.
  * Total timeout: 24 hours.



### CreateInstanceSettings
    
    
    public CallSettings CreateInstanceSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `CloudRedisClient.CreateInstance` and `CloudRedisClient.CreateInstanceAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 600 seconds.



### DeleteInstanceOperationsSettings
    
    
    public OperationsSettings DeleteInstanceOperationsSettings { get; set; }

Long Running Operation settings for calls to `CloudRedisClient.DeleteInstance` and `CloudRedisClient.DeleteInstanceAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsSettings.html)` |   
**Remarks**

Uses default [PollSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PollSettings.html) of: 

  * Initial delay: 20 seconds.
  * Delay multiplier: 1.5
  * Maximum delay: 45 seconds.
  * Total timeout: 24 hours.



### DeleteInstanceSettings
    
    
    public CallSettings DeleteInstanceSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `CloudRedisClient.DeleteInstance` and `CloudRedisClient.DeleteInstanceAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 600 seconds.



### ExportInstanceOperationsSettings
    
    
    public OperationsSettings ExportInstanceOperationsSettings { get; set; }

Long Running Operation settings for calls to `CloudRedisClient.ExportInstance` and `CloudRedisClient.ExportInstanceAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsSettings.html)` |   
**Remarks**

Uses default [PollSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PollSettings.html) of: 

  * Initial delay: 20 seconds.
  * Delay multiplier: 1.5
  * Maximum delay: 45 seconds.
  * Total timeout: 24 hours.



### ExportInstanceSettings
    
    
    public CallSettings ExportInstanceSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `CloudRedisClient.ExportInstance` and `CloudRedisClient.ExportInstanceAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 600 seconds.



### FailoverInstanceOperationsSettings
    
    
    public OperationsSettings FailoverInstanceOperationsSettings { get; set; }

Long Running Operation settings for calls to `CloudRedisClient.FailoverInstance` and `CloudRedisClient.FailoverInstanceAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsSettings.html)` |   
**Remarks**

Uses default [PollSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PollSettings.html) of: 

  * Initial delay: 20 seconds.
  * Delay multiplier: 1.5
  * Maximum delay: 45 seconds.
  * Total timeout: 24 hours.



### FailoverInstanceSettings
    
    
    public CallSettings FailoverInstanceSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `CloudRedisClient.FailoverInstance` and `CloudRedisClient.FailoverInstanceAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 600 seconds.



### GetInstanceAuthStringSettings
    
    
    public CallSettings GetInstanceAuthStringSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `CloudRedisClient.GetInstanceAuthString` and `CloudRedisClient.GetInstanceAuthStringAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 600 seconds.



### GetInstanceSettings
    
    
    public CallSettings GetInstanceSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `CloudRedisClient.GetInstance` and `CloudRedisClient.GetInstanceAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 600 seconds.



### ImportInstanceOperationsSettings
    
    
    public OperationsSettings ImportInstanceOperationsSettings { get; set; }

Long Running Operation settings for calls to `CloudRedisClient.ImportInstance` and `CloudRedisClient.ImportInstanceAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsSettings.html)` |   
**Remarks**

Uses default [PollSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PollSettings.html) of: 

  * Initial delay: 20 seconds.
  * Delay multiplier: 1.5
  * Maximum delay: 45 seconds.
  * Total timeout: 24 hours.



### ImportInstanceSettings
    
    
    public CallSettings ImportInstanceSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `CloudRedisClient.ImportInstance` and `CloudRedisClient.ImportInstanceAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 600 seconds.



### ListInstancesSettings
    
    
    public CallSettings ListInstancesSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `CloudRedisClient.ListInstances` and `CloudRedisClient.ListInstancesAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 600 seconds.



### RescheduleMaintenanceOperationsSettings
    
    
    public OperationsSettings RescheduleMaintenanceOperationsSettings { get; set; }

Long Running Operation settings for calls to `CloudRedisClient.RescheduleMaintenance` and `CloudRedisClient.RescheduleMaintenanceAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsSettings.html)` |   
**Remarks**

Uses default [PollSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PollSettings.html) of: 

  * Initial delay: 20 seconds.
  * Delay multiplier: 1.5
  * Maximum delay: 45 seconds.
  * Total timeout: 24 hours.



### RescheduleMaintenanceSettings
    
    
    public CallSettings RescheduleMaintenanceSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `CloudRedisClient.RescheduleMaintenance` and `CloudRedisClient.RescheduleMaintenanceAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### UpdateInstanceOperationsSettings
    
    
    public OperationsSettings UpdateInstanceOperationsSettings { get; set; }

Long Running Operation settings for calls to `CloudRedisClient.UpdateInstance` and `CloudRedisClient.UpdateInstanceAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsSettings.html)` |   
**Remarks**

Uses default [PollSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PollSettings.html) of: 

  * Initial delay: 20 seconds.
  * Delay multiplier: 1.5
  * Maximum delay: 45 seconds.
  * Total timeout: 24 hours.



### UpdateInstanceSettings
    
    
    public CallSettings UpdateInstanceSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `CloudRedisClient.UpdateInstance` and `CloudRedisClient.UpdateInstanceAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 600 seconds.



### UpgradeInstanceOperationsSettings
    
    
    public OperationsSettings UpgradeInstanceOperationsSettings { get; set; }

Long Running Operation settings for calls to `CloudRedisClient.UpgradeInstance` and `CloudRedisClient.UpgradeInstanceAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsSettings.html)` |   
**Remarks**

Uses default [PollSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PollSettings.html) of: 

  * Initial delay: 20 seconds.
  * Delay multiplier: 1.5
  * Maximum delay: 45 seconds.
  * Total timeout: 24 hours.



### UpgradeInstanceSettings
    
    
    public CallSettings UpgradeInstanceSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `CloudRedisClient.UpgradeInstance` and `CloudRedisClient.UpgradeInstanceAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 600 seconds.



## Methods 

### Clone()
    
    
    public CloudRedisSettings Clone()

Creates a deep clone of this object, with all the same property values.

**Returns**  
---  
**Type** | **Description**  
`[CloudRedisSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.CloudRedisSettings)` | A deep clone of this [CloudRedisSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.CloudRedisSettings) object.  
  
### GetDefault()
    
    
    public static CloudRedisSettings GetDefault()

Get a new instance of the default [CloudRedisSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.CloudRedisSettings).

**Returns**  
---  
**Type** | **Description**  
`[CloudRedisSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.CloudRedisSettings)` | A new instance of the default [CloudRedisSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.CloudRedisSettings).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
