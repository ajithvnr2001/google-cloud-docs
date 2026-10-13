---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.HubServiceSettings
title: Network Connectivity v1alpha1 API - Class HubServiceSettings (2.0.0-alpha05) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:43:51.836908+00:00
---

# Network Connectivity v1alpha1 API - Class HubServiceSettings (2.0.0-alpha05)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.HubServiceSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Network Connectivity v1alpha1 API - Class HubServiceSettings (2.0.0-alpha05) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-alpha05 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.HubServiceSettings)
  * [ 2.0.0-alpha04 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/2.0.0-alpha04/Google.Cloud.NetworkConnectivity.V1Alpha1.HubServiceSettings)
  * [ 1.0.0-alpha03 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/1.0.0-alpha03/Google.Cloud.NetworkConnectivity.V1Alpha1.HubServiceSettings)


    
    
    public sealed class HubServiceSettings : ServiceSettingsBase

Reference documentation and code samples for the Network Connectivity v1alpha1 API class HubServiceSettings.

Settings for [HubServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.HubServiceClient) instances.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ServiceSettingsBase](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceSettingsBase.html) > HubServiceSettings

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

[Google.Cloud.NetworkConnectivity.V1Alpha1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1)

## Assembly

Google.Cloud.NetworkConnectivity.V1Alpha1.dll

## Constructors 

### HubServiceSettings()
    
    
    public HubServiceSettings()

Constructs a new [HubServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.HubServiceSettings) object with default settings.

## Properties 

### CreateHubOperationsSettings
    
    
    public OperationsSettings CreateHubOperationsSettings { get; set; }

Long Running Operation settings for calls to `HubServiceClient.CreateHub` and `HubServiceClient.CreateHubAsync`.

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



### CreateHubSettings
    
    
    public CallSettings CreateHubSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `HubServiceClient.CreateHub` and `HubServiceClient.CreateHubAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 60 seconds.



### CreateSpokeOperationsSettings
    
    
    public OperationsSettings CreateSpokeOperationsSettings { get; set; }

Long Running Operation settings for calls to `HubServiceClient.CreateSpoke` and `HubServiceClient.CreateSpokeAsync`.

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



### CreateSpokeSettings
    
    
    public CallSettings CreateSpokeSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `HubServiceClient.CreateSpoke` and `HubServiceClient.CreateSpokeAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 60 seconds.



### DeleteHubOperationsSettings
    
    
    public OperationsSettings DeleteHubOperationsSettings { get; set; }

Long Running Operation settings for calls to `HubServiceClient.DeleteHub` and `HubServiceClient.DeleteHubAsync`.

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



### DeleteHubSettings
    
    
    public CallSettings DeleteHubSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `HubServiceClient.DeleteHub` and `HubServiceClient.DeleteHubAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 60 seconds.



### DeleteSpokeOperationsSettings
    
    
    public OperationsSettings DeleteSpokeOperationsSettings { get; set; }

Long Running Operation settings for calls to `HubServiceClient.DeleteSpoke` and `HubServiceClient.DeleteSpokeAsync`.

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



### DeleteSpokeSettings
    
    
    public CallSettings DeleteSpokeSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `HubServiceClient.DeleteSpoke` and `HubServiceClient.DeleteSpokeAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 60 seconds.



### GetHubSettings
    
    
    public CallSettings GetHubSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `HubServiceClient.GetHub` and `HubServiceClient.GetHubAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 1000 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 10000 milliseconds.
  * Maximum attempts: 5
  * Retriable status codes: [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable).
  * Timeout: 60 seconds.



### GetSpokeSettings
    
    
    public CallSettings GetSpokeSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `HubServiceClient.GetSpoke` and `HubServiceClient.GetSpokeAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 1000 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 10000 milliseconds.
  * Maximum attempts: 5
  * Retriable status codes: [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable).
  * Timeout: 60 seconds.



### ListHubsSettings
    
    
    public CallSettings ListHubsSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `HubServiceClient.ListHubs` and `HubServiceClient.ListHubsAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 1000 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 10000 milliseconds.
  * Maximum attempts: 5
  * Retriable status codes: [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable).
  * Timeout: 60 seconds.



### ListSpokesSettings
    
    
    public CallSettings ListSpokesSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `HubServiceClient.ListSpokes` and `HubServiceClient.ListSpokesAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * Initial retry delay: 1000 milliseconds.
  * Retry delay multiplier: 1.3
  * Retry maximum delay: 10000 milliseconds.
  * Maximum attempts: 5
  * Retriable status codes: [Unavailable](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable).
  * Timeout: 60 seconds.



### UpdateHubOperationsSettings
    
    
    public OperationsSettings UpdateHubOperationsSettings { get; set; }

Long Running Operation settings for calls to `HubServiceClient.UpdateHub` and `HubServiceClient.UpdateHubAsync`.

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



### UpdateHubSettings
    
    
    public CallSettings UpdateHubSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `HubServiceClient.UpdateHub` and `HubServiceClient.UpdateHubAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 60 seconds.



### UpdateSpokeOperationsSettings
    
    
    public OperationsSettings UpdateSpokeOperationsSettings { get; set; }

Long Running Operation settings for calls to `HubServiceClient.UpdateSpoke` and `HubServiceClient.UpdateSpokeAsync`.

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



### UpdateSpokeSettings
    
    
    public CallSettings UpdateSpokeSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `HubServiceClient.UpdateSpoke` and `HubServiceClient.UpdateSpokeAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * Timeout: 60 seconds.



## Methods 

### Clone()
    
    
    public HubServiceSettings Clone()

Creates a deep clone of this object, with all the same property values.

**Returns**  
---  
**Type** | **Description**  
`[HubServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.HubServiceSettings)` | A deep clone of this [HubServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.HubServiceSettings) object.  
  
### GetDefault()
    
    
    public static HubServiceSettings GetDefault()

Get a new instance of the default [HubServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.HubServiceSettings).

**Returns**  
---  
**Type** | **Description**  
`[HubServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.HubServiceSettings)` | A new instance of the default [HubServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.HubServiceSettings).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
