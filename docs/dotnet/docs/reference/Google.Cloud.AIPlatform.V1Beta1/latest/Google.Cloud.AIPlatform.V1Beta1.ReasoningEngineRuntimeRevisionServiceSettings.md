---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngineRuntimeRevisionServiceSettings
title: Vertex AI v1beta1 API - Class ReasoningEngineRuntimeRevisionServiceSettings (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:27:48.971463+00:00
---

# Vertex AI v1beta1 API - Class ReasoningEngineRuntimeRevisionServiceSettings (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngineRuntimeRevisionServiceSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class ReasoningEngineRuntimeRevisionServiceSettings (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    public sealed class ReasoningEngineRuntimeRevisionServiceSettings : ServiceSettingsBase

Reference documentation and code samples for the Vertex AI v1beta1 API class ReasoningEngineRuntimeRevisionServiceSettings.

Settings for [ReasoningEngineRuntimeRevisionServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngineRuntimeRevisionServiceClient) instances.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ServiceSettingsBase](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceSettingsBase.html) > ReasoningEngineRuntimeRevisionServiceSettings

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

### ReasoningEngineRuntimeRevisionServiceSettings()
    
    
    public ReasoningEngineRuntimeRevisionServiceSettings()

Constructs a new [ReasoningEngineRuntimeRevisionServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngineRuntimeRevisionServiceSettings) object with default settings.

## Properties 

### DeleteReasoningEngineRuntimeRevisionOperationsSettings
    
    
    public OperationsSettings DeleteReasoningEngineRuntimeRevisionOperationsSettings { get; set; }

Long Running Operation settings for calls to `ReasoningEngineRuntimeRevisionServiceClient.DeleteReasoningEngineRuntimeRevision` and `ReasoningEngineRuntimeRevisionServiceClient.DeleteReasoningEngineRuntimeRevisionAsync`.

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



### DeleteReasoningEngineRuntimeRevisionSettings
    
    
    public CallSettings DeleteReasoningEngineRuntimeRevisionSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `ReasoningEngineRuntimeRevisionServiceClient.DeleteReasoningEngineRuntimeRevision` and `ReasoningEngineRuntimeRevisionServiceClient.DeleteReasoningEngineRuntimeRevisionAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### GetReasoningEngineRuntimeRevisionSettings
    
    
    public CallSettings GetReasoningEngineRuntimeRevisionSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `ReasoningEngineRuntimeRevisionServiceClient.GetReasoningEngineRuntimeRevision` and `ReasoningEngineRuntimeRevisionServiceClient.GetReasoningEngineRuntimeRevisionAsync`.

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
  
### ListReasoningEngineRuntimeRevisionsSettings
    
    
    public CallSettings ListReasoningEngineRuntimeRevisionsSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `ReasoningEngineRuntimeRevisionServiceClient.ListReasoningEngineRuntimeRevisions` and `ReasoningEngineRuntimeRevisionServiceClient.ListReasoningEngineRuntimeRevisionsAsync`.

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
  
## Methods 

### Clone()
    
    
    public ReasoningEngineRuntimeRevisionServiceSettings Clone()

Creates a deep clone of this object, with all the same property values.

**Returns**  
---  
**Type** | **Description**  
`[ReasoningEngineRuntimeRevisionServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngineRuntimeRevisionServiceSettings)` | A deep clone of this [ReasoningEngineRuntimeRevisionServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngineRuntimeRevisionServiceSettings) object.  
  
### GetDefault()
    
    
    public static ReasoningEngineRuntimeRevisionServiceSettings GetDefault()

Get a new instance of the default [ReasoningEngineRuntimeRevisionServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngineRuntimeRevisionServiceSettings).

**Returns**  
---  
**Type** | **Description**  
`[ReasoningEngineRuntimeRevisionServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngineRuntimeRevisionServiceSettings)` | A new instance of the default [ReasoningEngineRuntimeRevisionServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngineRuntimeRevisionServiceSettings).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
