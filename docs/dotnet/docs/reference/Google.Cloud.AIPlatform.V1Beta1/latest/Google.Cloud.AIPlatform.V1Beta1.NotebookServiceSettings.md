---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NotebookServiceSettings
title: Vertex AI v1beta1 API - Class NotebookServiceSettings (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:43:01.660693+00:00
---

# Vertex AI v1beta1 API - Class NotebookServiceSettings (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NotebookServiceSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class NotebookServiceSettings (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    public sealed class NotebookServiceSettings : ServiceSettingsBase

Reference documentation and code samples for the Vertex AI v1beta1 API class NotebookServiceSettings.

Settings for [NotebookServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NotebookServiceClient) instances.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ServiceSettingsBase](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceSettingsBase.html) > NotebookServiceSettings

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

[Google.Cloud.AIPlatform.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1)

## Assembly

Google.Cloud.AIPlatform.V1Beta1.dll

## Constructors 

### NotebookServiceSettings()
    
    
    public NotebookServiceSettings()

Constructs a new [NotebookServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NotebookServiceSettings) object with default settings.

## Properties 

### AssignNotebookRuntimeOperationsSettings
    
    
    public OperationsSettings AssignNotebookRuntimeOperationsSettings { get; set; }

Long Running Operation settings for calls to `NotebookServiceClient.AssignNotebookRuntime` and `NotebookServiceClient.AssignNotebookRuntimeAsync`.

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



### AssignNotebookRuntimeSettings
    
    
    public CallSettings AssignNotebookRuntimeSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `NotebookServiceClient.AssignNotebookRuntime` and `NotebookServiceClient.AssignNotebookRuntimeAsync` .

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### CreateNotebookExecutionJobOperationsSettings
    
    
    public OperationsSettings CreateNotebookExecutionJobOperationsSettings { get; set; }

Long Running Operation settings for calls to `NotebookServiceClient.CreateNotebookExecutionJob` and `NotebookServiceClient.CreateNotebookExecutionJobAsync`.

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



### CreateNotebookExecutionJobSettings
    
    
    public CallSettings CreateNotebookExecutionJobSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `NotebookServiceClient.CreateNotebookExecutionJob` and `NotebookServiceClient.CreateNotebookExecutionJobAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### CreateNotebookRuntimeTemplateOperationsSettings
    
    
    public OperationsSettings CreateNotebookRuntimeTemplateOperationsSettings { get; set; }

Long Running Operation settings for calls to `NotebookServiceClient.CreateNotebookRuntimeTemplate` and `NotebookServiceClient.CreateNotebookRuntimeTemplateAsync`.

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



### CreateNotebookRuntimeTemplateSettings
    
    
    public CallSettings CreateNotebookRuntimeTemplateSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `NotebookServiceClient.CreateNotebookRuntimeTemplate` and `NotebookServiceClient.CreateNotebookRuntimeTemplateAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### DeleteNotebookExecutionJobOperationsSettings
    
    
    public OperationsSettings DeleteNotebookExecutionJobOperationsSettings { get; set; }

Long Running Operation settings for calls to `NotebookServiceClient.DeleteNotebookExecutionJob` and `NotebookServiceClient.DeleteNotebookExecutionJobAsync`.

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



### DeleteNotebookExecutionJobSettings
    
    
    public CallSettings DeleteNotebookExecutionJobSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `NotebookServiceClient.DeleteNotebookExecutionJob` and `NotebookServiceClient.DeleteNotebookExecutionJobAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### DeleteNotebookRuntimeOperationsSettings
    
    
    public OperationsSettings DeleteNotebookRuntimeOperationsSettings { get; set; }

Long Running Operation settings for calls to `NotebookServiceClient.DeleteNotebookRuntime` and `NotebookServiceClient.DeleteNotebookRuntimeAsync`.

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



### DeleteNotebookRuntimeSettings
    
    
    public CallSettings DeleteNotebookRuntimeSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `NotebookServiceClient.DeleteNotebookRuntime` and `NotebookServiceClient.DeleteNotebookRuntimeAsync` .

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### DeleteNotebookRuntimeTemplateOperationsSettings
    
    
    public OperationsSettings DeleteNotebookRuntimeTemplateOperationsSettings { get; set; }

Long Running Operation settings for calls to `NotebookServiceClient.DeleteNotebookRuntimeTemplate` and `NotebookServiceClient.DeleteNotebookRuntimeTemplateAsync`.

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



### DeleteNotebookRuntimeTemplateSettings
    
    
    public CallSettings DeleteNotebookRuntimeTemplateSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `NotebookServiceClient.DeleteNotebookRuntimeTemplate` and `NotebookServiceClient.DeleteNotebookRuntimeTemplateAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### GetNotebookExecutionJobSettings
    
    
    public CallSettings GetNotebookExecutionJobSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `NotebookServiceClient.GetNotebookExecutionJob` and `NotebookServiceClient.GetNotebookExecutionJobAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### GetNotebookRuntimeSettings
    
    
    public CallSettings GetNotebookRuntimeSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `NotebookServiceClient.GetNotebookRuntime` and `NotebookServiceClient.GetNotebookRuntimeAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### GetNotebookRuntimeTemplateSettings
    
    
    public CallSettings GetNotebookRuntimeTemplateSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `NotebookServiceClient.GetNotebookRuntimeTemplate` and `NotebookServiceClient.GetNotebookRuntimeTemplateAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### IAMPolicySettings
    
    
    public IAMPolicySettings IAMPolicySettings { get; set; }

The settings to use for the [IAMPolicyClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.IAMPolicyClient.html) associated with the client.

**Property Value**  
---  
**Type** | **Description**  
`[IAMPolicySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.IAMPolicySettings.html)` |   
  
### ListNotebookExecutionJobsSettings
    
    
    public CallSettings ListNotebookExecutionJobsSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `NotebookServiceClient.ListNotebookExecutionJobs` and `NotebookServiceClient.ListNotebookExecutionJobsAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### ListNotebookRuntimeTemplatesSettings
    
    
    public CallSettings ListNotebookRuntimeTemplatesSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `NotebookServiceClient.ListNotebookRuntimeTemplates` and `NotebookServiceClient.ListNotebookRuntimeTemplatesAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### ListNotebookRuntimesSettings
    
    
    public CallSettings ListNotebookRuntimesSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `NotebookServiceClient.ListNotebookRuntimes` and `NotebookServiceClient.ListNotebookRuntimesAsync` .

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### LocationsSettings
    
    
    public LocationsSettings LocationsSettings { get; set; }

The settings to use for the [LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.LocationsClient.html) associated with the client.

**Property Value**  
---  
**Type** | **Description**  
`[LocationsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.LocationsSettings.html)` |   
  
### StartNotebookRuntimeOperationsSettings
    
    
    public OperationsSettings StartNotebookRuntimeOperationsSettings { get; set; }

Long Running Operation settings for calls to `NotebookServiceClient.StartNotebookRuntime` and `NotebookServiceClient.StartNotebookRuntimeAsync`.

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



### StartNotebookRuntimeSettings
    
    
    public CallSettings StartNotebookRuntimeSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `NotebookServiceClient.StartNotebookRuntime` and `NotebookServiceClient.StartNotebookRuntimeAsync` .

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### StopNotebookRuntimeOperationsSettings
    
    
    public OperationsSettings StopNotebookRuntimeOperationsSettings { get; set; }

Long Running Operation settings for calls to `NotebookServiceClient.StopNotebookRuntime` and `NotebookServiceClient.StopNotebookRuntimeAsync`.

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



### StopNotebookRuntimeSettings
    
    
    public CallSettings StopNotebookRuntimeSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `NotebookServiceClient.StopNotebookRuntime` and `NotebookServiceClient.StopNotebookRuntimeAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### UpdateNotebookRuntimeTemplateSettings
    
    
    public CallSettings UpdateNotebookRuntimeTemplateSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `NotebookServiceClient.UpdateNotebookRuntimeTemplate` and `NotebookServiceClient.UpdateNotebookRuntimeTemplateAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### UpgradeNotebookRuntimeOperationsSettings
    
    
    public OperationsSettings UpgradeNotebookRuntimeOperationsSettings { get; set; }

Long Running Operation settings for calls to `NotebookServiceClient.UpgradeNotebookRuntime` and `NotebookServiceClient.UpgradeNotebookRuntimeAsync`.

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



### UpgradeNotebookRuntimeSettings
    
    
    public CallSettings UpgradeNotebookRuntimeSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `NotebookServiceClient.UpgradeNotebookRuntime` and `NotebookServiceClient.UpgradeNotebookRuntimeAsync` .

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



## Methods 

### Clone()
    
    
    public NotebookServiceSettings Clone()

Creates a deep clone of this object, with all the same property values.

**Returns**  
---  
**Type** | **Description**  
`[NotebookServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NotebookServiceSettings)` | A deep clone of this [NotebookServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NotebookServiceSettings) object.  
  
### GetDefault()
    
    
    public static NotebookServiceSettings GetDefault()

Get a new instance of the default [NotebookServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NotebookServiceSettings).

**Returns**  
---  
**Type** | **Description**  
`[NotebookServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NotebookServiceSettings)` | A new instance of the default [NotebookServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NotebookServiceSettings).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
