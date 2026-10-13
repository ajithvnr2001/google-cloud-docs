---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.WidgetServiceClientImpl
title: Gemini Enterprise for Customer Experience v1 API - Class WidgetServiceClientImpl (1.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:44:25.827583+00:00
---

# Gemini Enterprise for Customer Experience v1 API - Class WidgetServiceClientImpl (1.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.WidgetServiceClientImpl

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Gemini Enterprise for Customer Experience v1 API - Class WidgetServiceClientImpl (1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  1.0.0-beta04 
    
    
    public sealed class WidgetServiceClientImpl : WidgetServiceClient

Reference documentation and code samples for the Gemini Enterprise for Customer Experience v1 API class WidgetServiceClientImpl.

WidgetService client wrapper implementation, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [WidgetServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.WidgetServiceClient) > WidgetServiceClientImpl

## Inherited Members

[WidgetServiceClient.DefaultEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.WidgetServiceClient#Google_Cloud_Ces_V1_WidgetServiceClient_DefaultEndpoint)

[WidgetServiceClient.DefaultScopes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.WidgetServiceClient#Google_Cloud_Ces_V1_WidgetServiceClient_DefaultScopes)

[WidgetServiceClient.ServiceMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.WidgetServiceClient#Google_Cloud_Ces_V1_WidgetServiceClient_ServiceMetadata)

[WidgetServiceClient.CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.WidgetServiceClient#Google_Cloud_Ces_V1_WidgetServiceClient_CreateAsync_System_Threading_CancellationToken_)

[WidgetServiceClient.Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.WidgetServiceClient#Google_Cloud_Ces_V1_WidgetServiceClient_Create)

[WidgetServiceClient.ShutdownDefaultChannelsAsync()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.WidgetServiceClient#Google_Cloud_Ces_V1_WidgetServiceClient_ShutdownDefaultChannelsAsync)

[WidgetServiceClient.GenerateChatTokenAsync(GenerateChatTokenRequest, CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.WidgetServiceClient#Google_Cloud_Ces_V1_WidgetServiceClient_GenerateChatTokenAsync_Google_Cloud_Ces_V1_GenerateChatTokenRequest_System_Threading_CancellationToken_)

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Ces.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1)

## Assembly

Google.Cloud.Ces.V1.dll

## Remarks

Provides APIs for widgets to interact with CES APIs.

## Constructors 

### WidgetServiceClientImpl(WidgetServiceClient, WidgetServiceSettings, ILogger)
    
    
    public WidgetServiceClientImpl(WidgetService.WidgetServiceClient grpcClient, WidgetServiceSettings settings, ILogger logger)

Constructs a client wrapper for the WidgetService service, with the specified gRPC client and settings.

**Parameters**  
---  
**Name** | **Description**  
`grpcClient` | `[WidgetService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.WidgetService)[WidgetServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.WidgetService.WidgetServiceClient)`  
The underlying gRPC client.  
`settings` | `[WidgetServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.WidgetServiceSettings)`  
The base [WidgetServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.WidgetServiceSettings) used within this client.  
`logger` | `[ILogger](https://learn.microsoft.com/dotnet/api/microsoft.extensions.logging.ilogger)`  
Optional [ILogger](https://learn.microsoft.com/dotnet/api/microsoft.extensions.logging.ilogger) to use within this client.  
  
## Properties 

### GrpcClient
    
    
    public override WidgetService.WidgetServiceClient GrpcClient { get; }

The underlying gRPC WidgetService client

**Property Value**  
---  
**Type** | **Description**  
`[WidgetService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.WidgetService)[WidgetServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.WidgetService.WidgetServiceClient)` |   
**Overrides**

[WidgetServiceClient.GrpcClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.WidgetServiceClient#Google_Cloud_Ces_V1_WidgetServiceClient_GrpcClient)

### LocationsClient
    
    
    public override LocationsClient LocationsClient { get; }

The [LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.LocationsClient.html) associated with this client.

**Property Value**  
---  
**Type** | **Description**  
`[LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.LocationsClient.html)` |   
**Overrides**

[WidgetServiceClient.LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.WidgetServiceClient#Google_Cloud_Ces_V1_WidgetServiceClient_LocationsClient)

## Methods 

### GenerateChatToken(GenerateChatTokenRequest, CallSettings)
    
    
    public override GenerateChatTokenResponse GenerateChatToken(GenerateChatTokenRequest request, CallSettings callSettings = null)

Generates a session scoped token for chat widget to authenticate with Session APIs.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateChatTokenRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.GenerateChatTokenRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[GenerateChatTokenResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.GenerateChatTokenResponse)` | The RPC response.  
**Overrides**

[WidgetServiceClient.GenerateChatToken(GenerateChatTokenRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.WidgetServiceClient#Google_Cloud_Ces_V1_WidgetServiceClient_GenerateChatToken_Google_Cloud_Ces_V1_GenerateChatTokenRequest_Google_Api_Gax_Grpc_CallSettings_)

### GenerateChatTokenAsync(GenerateChatTokenRequest, CallSettings)
    
    
    public override Task<GenerateChatTokenResponse> GenerateChatTokenAsync(GenerateChatTokenRequest request, CallSettings callSettings = null)

Generates a session scoped token for chat widget to authenticate with Session APIs.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateChatTokenRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.GenerateChatTokenRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GenerateChatTokenResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.GenerateChatTokenResponse)` | A Task containing the RPC response.  
**Overrides**

[WidgetServiceClient.GenerateChatTokenAsync(GenerateChatTokenRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.WidgetServiceClient#Google_Cloud_Ces_V1_WidgetServiceClient_GenerateChatTokenAsync_Google_Cloud_Ces_V1_GenerateChatTokenRequest_Google_Api_Gax_Grpc_CallSettings_)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
