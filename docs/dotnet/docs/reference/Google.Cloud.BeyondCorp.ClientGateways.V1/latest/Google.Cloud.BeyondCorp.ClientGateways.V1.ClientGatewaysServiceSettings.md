---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BeyondCorp.ClientGateways.V1/latest/Google.Cloud.BeyondCorp.ClientGateways.V1.ClientGatewaysServiceSettings
title: BeyondCorp Client Gateways v1 API - Class ClientGatewaysServiceSettings (1.4.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:52:27.288809+00:00
---

# BeyondCorp Client Gateways v1 API - Class ClientGatewaysServiceSettings (1.4.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BeyondCorp.ClientGateways.V1/latest/Google.Cloud.BeyondCorp.ClientGateways.V1.ClientGatewaysServiceSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  BeyondCorp Client Gateways v1 API - Class ClientGatewaysServiceSettings (1.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.4.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BeyondCorp.ClientGateways.V1/latest/Google.Cloud.BeyondCorp.ClientGateways.V1.ClientGatewaysServiceSettings)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BeyondCorp.ClientGateways.V1/1.3.0/Google.Cloud.BeyondCorp.ClientGateways.V1.ClientGatewaysServiceSettings)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BeyondCorp.ClientGateways.V1/1.2.0/Google.Cloud.BeyondCorp.ClientGateways.V1.ClientGatewaysServiceSettings)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BeyondCorp.ClientGateways.V1/1.1.0/Google.Cloud.BeyondCorp.ClientGateways.V1.ClientGatewaysServiceSettings)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BeyondCorp.ClientGateways.V1/1.0.0/Google.Cloud.BeyondCorp.ClientGateways.V1.ClientGatewaysServiceSettings)


    
    
    public sealed class ClientGatewaysServiceSettings : ServiceSettingsBase

Reference documentation and code samples for the BeyondCorp Client Gateways v1 API class ClientGatewaysServiceSettings.

Settings for [ClientGatewaysServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BeyondCorp.ClientGateways.V1/latest/Google.Cloud.BeyondCorp.ClientGateways.V1.ClientGatewaysServiceClient) instances.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ServiceSettingsBase](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceSettingsBase.html) > ClientGatewaysServiceSettings

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

[Google.Cloud.BeyondCorp.ClientGateways.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BeyondCorp.ClientGateways.V1/latest/Google.Cloud.BeyondCorp.ClientGateways.V1)

## Assembly

Google.Cloud.BeyondCorp.ClientGateways.V1.dll

## Constructors 

### ClientGatewaysServiceSettings()
    
    
    public ClientGatewaysServiceSettings()

Constructs a new [ClientGatewaysServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BeyondCorp.ClientGateways.V1/latest/Google.Cloud.BeyondCorp.ClientGateways.V1.ClientGatewaysServiceSettings) object with default settings.

## Properties 

### CreateClientGatewayOperationsSettings
    
    
    public OperationsSettings CreateClientGatewayOperationsSettings { get; set; }

Long Running Operation settings for calls to `ClientGatewaysServiceClient.CreateClientGateway` and `ClientGatewaysServiceClient.CreateClientGatewayAsync`.

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



### CreateClientGatewaySettings
    
    
    public CallSettings CreateClientGatewaySettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `ClientGatewaysServiceClient.CreateClientGateway` and `ClientGatewaysServiceClient.CreateClientGatewayAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### DeleteClientGatewayOperationsSettings
    
    
    public OperationsSettings DeleteClientGatewayOperationsSettings { get; set; }

Long Running Operation settings for calls to `ClientGatewaysServiceClient.DeleteClientGateway` and `ClientGatewaysServiceClient.DeleteClientGatewayAsync`.

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



### DeleteClientGatewaySettings
    
    
    public CallSettings DeleteClientGatewaySettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `ClientGatewaysServiceClient.DeleteClientGateway` and `ClientGatewaysServiceClient.DeleteClientGatewayAsync`.

**Property Value**  
---  
**Type** | **Description**  
`[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)` |   
**Remarks**

  * This call will not be retried.
  * No timeout is applied.



### GetClientGatewaySettings
    
    
    public CallSettings GetClientGatewaySettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `ClientGatewaysServiceClient.GetClientGateway` and `ClientGatewaysServiceClient.GetClientGatewayAsync` .

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
  
### ListClientGatewaysSettings
    
    
    public CallSettings ListClientGatewaysSettings { get; set; }

[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) for synchronous and asynchronous calls to `ClientGatewaysServiceClient.ListClientGateways` and `ClientGatewaysServiceClient.ListClientGatewaysAsync`.

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
    
    
    public ClientGatewaysServiceSettings Clone()

Creates a deep clone of this object, with all the same property values.

**Returns**  
---  
**Type** | **Description**  
`[ClientGatewaysServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BeyondCorp.ClientGateways.V1/latest/Google.Cloud.BeyondCorp.ClientGateways.V1.ClientGatewaysServiceSettings)` | A deep clone of this [ClientGatewaysServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BeyondCorp.ClientGateways.V1/latest/Google.Cloud.BeyondCorp.ClientGateways.V1.ClientGatewaysServiceSettings) object.  
  
### GetDefault()
    
    
    public static ClientGatewaysServiceSettings GetDefault()

Get a new instance of the default [ClientGatewaysServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BeyondCorp.ClientGateways.V1/latest/Google.Cloud.BeyondCorp.ClientGateways.V1.ClientGatewaysServiceSettings).

**Returns**  
---  
**Type** | **Description**  
`[ClientGatewaysServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BeyondCorp.ClientGateways.V1/latest/Google.Cloud.BeyondCorp.ClientGateways.V1.ClientGatewaysServiceSettings)` | A new instance of the default [ClientGatewaysServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BeyondCorp.ClientGateways.V1/latest/Google.Cloud.BeyondCorp.ClientGateways.V1.ClientGatewaysServiceSettings).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
