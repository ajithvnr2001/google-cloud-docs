---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RapidMigrationAssessment.V1/latest/Google.Cloud.RapidMigrationAssessment.V1.RapidMigrationAssessmentSettings
title: Rapid Migration Assessment v1 API - Class RapidMigrationAssessmentSettings (1.3.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:56:58.812907+00:00
---

# Rapid Migration Assessment v1 API - Class RapidMigrationAssessmentSettings (1.3.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RapidMigrationAssessment.V1/latest/Google.Cloud.RapidMigrationAssessment.V1.RapidMigrationAssessmentSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Rapid Migration Assessment v1 API - Class RapidMigrationAssessmentSettings (1.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.3.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RapidMigrationAssessment.V1/latest/Google.Cloud.RapidMigrationAssessment.V1.RapidMigrationAssessmentSettings)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RapidMigrationAssessment.V1/1.2.0/Google.Cloud.RapidMigrationAssessment.V1.RapidMigrationAssessmentSettings)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RapidMigrationAssessment.V1/1.1.0/Google.Cloud.RapidMigrationAssessment.V1.RapidMigrationAssessmentSettings)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RapidMigrationAssessment.V1/1.0.0/Google.Cloud.RapidMigrationAssessment.V1.RapidMigrationAssessmentSettings)


    
    
    public sealed class RapidMigrationAssessmentSettings : ServiceSettingsBase

Reference documentation and code samples for the Rapid Migration Assessment v1 API class RapidMigrationAssessmentSettings.

Settings for [RapidMigrationAssessmentClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RapidMigrationAssessment.V1/latest/Google.Cloud.RapidMigrationAssessment.V1.RapidMigrationAssessmentClient) instances.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ServiceSettingsBase](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceSettingsBase.html) > RapidMigrationAssessmentSettings

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

[Google.Cloud.RapidMigrationAssessment.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RapidMigrationAssessment.V1/latest/Google.Cloud.RapidMigrationAssessment.V1)

## Assembly

Google.Cloud.RapidMigrationAssessment.V1.dll

## Constructors 

### RapidMigrationAssessmentSettings()
    
    
    public RapidMigrationAssessmentSettings()

Constructs a new [RapidMigrationAssessmentSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RapidMigrationAssessment.V1/latest/Google.Cloud.RapidMigrationAssessment.V1.RapidMigrationAssessmentSettings) object with default settings.

## Properties 

### CreateAnnotationOperationsSettings
    
    
    public OperationsSettings CreateAnnotationOperationsSettings { get; set; }

Long Running Operation settings for calls to `RapidMigrationAssessmentClient.CreateAnnotation` and `RapidMigrationAssessmentClient.CreateAnnotationAsync`.

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



### CreateAnnotationSettings
    
    
    public CallSettings CreateAnnotationSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `RapidMigrationAssessmentClient.CreateAnnotation` and `RapidMigrationAssessmentClient.CreateAnnotationAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 60 seconds.



### CreateCollectorOperationsSettings
    
    
    public OperationsSettings CreateCollectorOperationsSettings { get; set; }

Long Running Operation settings for calls to `RapidMigrationAssessmentClient.CreateCollector` and `RapidMigrationAssessmentClient.CreateCollectorAsync`.

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



### CreateCollectorSettings
    
    
    public CallSettings CreateCollectorSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `RapidMigrationAssessmentClient.CreateCollector` and `RapidMigrationAssessmentClient.CreateCollectorAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 60 seconds.



### DeleteCollectorOperationsSettings
    
    
    public OperationsSettings DeleteCollectorOperationsSettings { get; set; }

Long Running Operation settings for calls to `RapidMigrationAssessmentClient.DeleteCollector` and `RapidMigrationAssessmentClient.DeleteCollectorAsync`.

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



### DeleteCollectorSettings
    
    
    public CallSettings DeleteCollectorSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `RapidMigrationAssessmentClient.DeleteCollector` and `RapidMigrationAssessmentClient.DeleteCollectorAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 60 seconds.



### GetAnnotationSettings
    
    
    public CallSettings GetAnnotationSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `RapidMigrationAssessmentClient.GetAnnotation` and `RapidMigrationAssessmentClient.GetAnnotationAsync` .

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 1000 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 10000 milliseconds.
  * Maximum attempts: 5
  * Retriable status codes: [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable), [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded). 
  * Timeout: 60 seconds.



### GetCollectorSettings
    
    
    public CallSettings GetCollectorSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `RapidMigrationAssessmentClient.GetCollector` and `RapidMigrationAssessmentClient.GetCollectorAsync` .

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 1000 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 10000 milliseconds.
  * Maximum attempts: 5
  * Retriable status codes: [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable), [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded). 
  * Timeout: 60 seconds.



### ListCollectorsSettings
    
    
    public CallSettings ListCollectorsSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `RapidMigrationAssessmentClient.ListCollectors` and `RapidMigrationAssessmentClient.ListCollectorsAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 1000 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 10000 milliseconds.
  * Maximum attempts: 5
  * Retriable status codes: [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable), [DeadlineExceeded](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_DeadlineExceeded). 
  * Timeout: 60 seconds.



### LocationsSettings
    
    
    public LocationsSettings LocationsSettings { get; set; }

The settings to use for the [LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.LocationsClient.html) associated with the client.

**Property Value**  
---  
**Type** | **Description**  
`[LocationsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.LocationsSettings.html)` |   
  
### PauseCollectorOperationsSettings
    
    
    public OperationsSettings PauseCollectorOperationsSettings { get; set; }

Long Running Operation settings for calls to `RapidMigrationAssessmentClient.PauseCollector` and `RapidMigrationAssessmentClient.PauseCollectorAsync`.

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



### PauseCollectorSettings
    
    
    public CallSettings PauseCollectorSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `RapidMigrationAssessmentClient.PauseCollector` and `RapidMigrationAssessmentClient.PauseCollectorAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 60 seconds.



### RegisterCollectorOperationsSettings
    
    
    public OperationsSettings RegisterCollectorOperationsSettings { get; set; }

Long Running Operation settings for calls to `RapidMigrationAssessmentClient.RegisterCollector` and `RapidMigrationAssessmentClient.RegisterCollectorAsync`.

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



### RegisterCollectorSettings
    
    
    public CallSettings RegisterCollectorSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `RapidMigrationAssessmentClient.RegisterCollector` and `RapidMigrationAssessmentClient.RegisterCollectorAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 60 seconds.



### ResumeCollectorOperationsSettings
    
    
    public OperationsSettings ResumeCollectorOperationsSettings { get; set; }

Long Running Operation settings for calls to `RapidMigrationAssessmentClient.ResumeCollector` and `RapidMigrationAssessmentClient.ResumeCollectorAsync`.

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



### ResumeCollectorSettings
    
    
    public CallSettings ResumeCollectorSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `RapidMigrationAssessmentClient.ResumeCollector` and `RapidMigrationAssessmentClient.ResumeCollectorAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 60 seconds.



### UpdateCollectorOperationsSettings
    
    
    public OperationsSettings UpdateCollectorOperationsSettings { get; set; }

Long Running Operation settings for calls to `RapidMigrationAssessmentClient.UpdateCollector` and `RapidMigrationAssessmentClient.UpdateCollectorAsync`.

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



### UpdateCollectorSettings
    
    
    public CallSettings UpdateCollectorSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `RapidMigrationAssessmentClient.UpdateCollector` and `RapidMigrationAssessmentClient.UpdateCollectorAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 60 seconds.



## Methods 

### Clone()
    
    
    public RapidMigrationAssessmentSettings Clone()

Creates a deep clone of this object, with all the same property values.

**Returns**  
---  
**Type** | **Description**  
`[RapidMigrationAssessmentSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RapidMigrationAssessment.V1/latest/Google.Cloud.RapidMigrationAssessment.V1.RapidMigrationAssessmentSettings)` | A deep clone of this [RapidMigrationAssessmentSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RapidMigrationAssessment.V1/latest/Google.Cloud.RapidMigrationAssessment.V1.RapidMigrationAssessmentSettings) object.  
  
### GetDefault()
    
    
    public static RapidMigrationAssessmentSettings GetDefault()

Get a new instance of the default [RapidMigrationAssessmentSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RapidMigrationAssessment.V1/latest/Google.Cloud.RapidMigrationAssessment.V1.RapidMigrationAssessmentSettings).

**Returns**  
---  
**Type** | **Description**  
`[RapidMigrationAssessmentSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RapidMigrationAssessment.V1/latest/Google.Cloud.RapidMigrationAssessment.V1.RapidMigrationAssessmentSettings)` | A new instance of the default [RapidMigrationAssessmentSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RapidMigrationAssessment.V1/latest/Google.Cloud.RapidMigrationAssessment.V1.RapidMigrationAssessmentSettings).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
