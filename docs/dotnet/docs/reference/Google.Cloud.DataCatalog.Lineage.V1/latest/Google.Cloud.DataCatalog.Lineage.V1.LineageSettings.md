---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageSettings
title: Data Lineage v1 API - Class LineageSettings (1.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:36.482428+00:00
---

# Data Lineage v1 API - Class LineageSettings (1.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Data Lineage v1 API - Class LineageSettings (1.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.6.0 (latest)  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class LineageSettings : ServiceSettingsBase

Reference documentation and code samples for the Data Lineage v1 API class LineageSettings.

Settings for [LineageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageClient) instances.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ServiceSettingsBase](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceSettingsBase.html) > LineageSettings

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

[Google.Cloud.DataCatalog.Lineage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1)

## Assembly

Google.Cloud.DataCatalog.Lineage.V1.dll

## Constructors 

### LineageSettings()
    
    
    public LineageSettings()

Constructs a new [LineageSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageSettings) object with default settings.

## Properties 

### BatchSearchLinkProcessesSettings
    
    
    public CallSettings BatchSearchLinkProcessesSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `LineageClient.BatchSearchLinkProcesses` and `LineageClient.BatchSearchLinkProcessesAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable).
  * Timeout: 60 seconds.



### CreateLineageEventSettings
    
    
    public CallSettings CreateLineageEventSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `LineageClient.CreateLineageEvent` and `LineageClient.CreateLineageEventAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable).
  * Timeout: 60 seconds.



### CreateProcessSettings
    
    
    public CallSettings CreateProcessSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `LineageClient.CreateProcess` and `LineageClient.CreateProcessAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable).
  * Timeout: 60 seconds.



### CreateRunSettings
    
    
    public CallSettings CreateRunSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `LineageClient.CreateRun` and `LineageClient.CreateRunAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable).
  * Timeout: 60 seconds.



### DeleteLineageEventSettings
    
    
    public CallSettings DeleteLineageEventSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `LineageClient.DeleteLineageEvent` and `LineageClient.DeleteLineageEventAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable).
  * Timeout: 60 seconds.



### DeleteProcessOperationsSettings
    
    
    public OperationsSettings DeleteProcessOperationsSettings { get; set; }

Long Running Operation settings for calls to `LineageClient.DeleteProcess` and `LineageClient.DeleteProcessAsync`.

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



### DeleteProcessSettings
    
    
    public CallSettings DeleteProcessSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `LineageClient.DeleteProcess` and `LineageClient.DeleteProcessAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable).
  * Timeout: 60 seconds.



### DeleteRunOperationsSettings
    
    
    public OperationsSettings DeleteRunOperationsSettings { get; set; }

Long Running Operation settings for calls to `LineageClient.DeleteRun` and `LineageClient.DeleteRunAsync`.

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



### DeleteRunSettings
    
    
    public CallSettings DeleteRunSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `LineageClient.DeleteRun` and `LineageClient.DeleteRunAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable).
  * Timeout: 60 seconds.



### GetLineageEventSettings
    
    
    public CallSettings GetLineageEventSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `LineageClient.GetLineageEvent` and `LineageClient.GetLineageEventAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable).
  * Timeout: 60 seconds.



### GetProcessSettings
    
    
    public CallSettings GetProcessSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `LineageClient.GetProcess` and `LineageClient.GetProcessAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable).
  * Timeout: 60 seconds.



### GetRunSettings
    
    
    public CallSettings GetRunSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `LineageClient.GetRun` and `LineageClient.GetRunAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable).
  * Timeout: 60 seconds.



### ListLineageEventsSettings
    
    
    public CallSettings ListLineageEventsSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `LineageClient.ListLineageEvents` and `LineageClient.ListLineageEventsAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable).
  * Timeout: 60 seconds.



### ListProcessesSettings
    
    
    public CallSettings ListProcessesSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `LineageClient.ListProcesses` and `LineageClient.ListProcessesAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable).
  * Timeout: 60 seconds.



### ListRunsSettings
    
    
    public CallSettings ListRunsSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `LineageClient.ListRuns` and `LineageClient.ListRunsAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable).
  * Timeout: 60 seconds.



### ProcessOpenLineageRunEventSettings
    
    
    public CallSettings ProcessOpenLineageRunEventSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `LineageClient.ProcessOpenLineageRunEvent` and `LineageClient.ProcessOpenLineageRunEventAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable).
  * Timeout: 60 seconds.



### SearchLineageStreamingSettings
    
    
    public CallSettings SearchLineageStreamingSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `LineageClient.SearchLineageStreaming` and `LineageClient.SearchLineageStreamingAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

Timeout: 60 seconds.

### SearchLinksSettings
    
    
    public CallSettings SearchLinksSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `LineageClient.SearchLinks` and `LineageClient.SearchLinksAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable).
  * Timeout: 60 seconds.



### UpdateProcessSettings
    
    
    public CallSettings UpdateProcessSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `LineageClient.UpdateProcess` and `LineageClient.UpdateProcessAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable).
  * Timeout: 60 seconds.



### UpdateRunSettings
    
    
    public CallSettings UpdateRunSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `LineageClient.UpdateRun` and `LineageClient.UpdateRunAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 100 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 60000 milliseconds.
  * Maximum attempts: Unlimited
  * Retriable status codes: [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable).
  * Timeout: 60 seconds.



## Methods 

### Clone()
    
    
    public LineageSettings Clone()

Creates a deep clone of this object, with all the same property values.

**Returns**  
---  
**Type** | **Description**  
`[LineageSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageSettings)` | A deep clone of this [LineageSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageSettings) object.  
  
### GetDefault()
    
    
    public static LineageSettings GetDefault()

Get a new instance of the default [LineageSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageSettings).

**Returns**  
---  
**Type** | **Description**  
`[LineageSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageSettings)` | A new instance of the default [LineageSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageSettings).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-11 UTC."],[],[]] 
