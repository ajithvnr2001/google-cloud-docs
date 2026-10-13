---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ServingConfigService.ServingConfigServiceBase
title: Discovery Engine v1beta API - Class ServingConfigService.ServingConfigServiceBase (1.0.0-beta25) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:05:12.968581+00:00
---

# Discovery Engine v1beta API - Class ServingConfigService.ServingConfigServiceBase (1.0.0-beta25)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ServingConfigService.ServingConfigServiceBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Discovery Engine v1beta API - Class ServingConfigService.ServingConfigServiceBase (1.0.0-beta25) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta25 (latest)  1.0.0-beta24 
    
    
    [BindServiceMethod(typeof(ServingConfigService), "BindService")]
    public abstract class ServingConfigService.ServingConfigServiceBase

Reference documentation and code samples for the Discovery Engine v1beta API class ServingConfigService.ServingConfigServiceBase.

Base class for server-side implementations of ServingConfigService

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ServingConfigService.ServingConfigServiceBase

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DiscoveryEngine.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta)

## Assembly

Google.Cloud.DiscoveryEngine.V1Beta.dll

## Methods 

### CreateServingConfig(CreateServingConfigRequest, ServerCallContext)
    
    
    public virtual Task<ServingConfig> CreateServingConfig(CreateServingConfigRequest request, ServerCallContext context)

Creates a ServingConfig.

Note: The Google Cloud console works only with the default serving config. Additional ServingConfigs can be created and managed only via the API.

A maximum of 100 [ServingConfig][google.cloud.discoveryengine.v1beta.ServingConfig]s are allowed in an [Engine][google.cloud.discoveryengine.v1beta.Engine], otherwise a RESOURCE_EXHAUSTED error is returned.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateServingConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.CreateServingConfigRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ServingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ServingConfig)` | The response to send back to the client (wrapped by a task).  
  
### DeleteServingConfig(DeleteServingConfigRequest, ServerCallContext)
    
    
    public virtual Task<Empty> DeleteServingConfig(DeleteServingConfigRequest request, ServerCallContext context)

Deletes a ServingConfig.

Returns a NOT_FOUND error if the ServingConfig does not exist.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteServingConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DeleteServingConfigRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response to send back to the client (wrapped by a task).  
  
### GetServingConfig(GetServingConfigRequest, ServerCallContext)
    
    
    public virtual Task<ServingConfig> GetServingConfig(GetServingConfigRequest request, ServerCallContext context)

Gets a ServingConfig.

Returns a NotFound error if the ServingConfig does not exist.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetServingConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.GetServingConfigRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ServingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ServingConfig)` | The response to send back to the client (wrapped by a task).  
  
### ListServingConfigs(ListServingConfigsRequest, ServerCallContext)
    
    
    public virtual Task<ListServingConfigsResponse> ListServingConfigs(ListServingConfigsRequest request, ServerCallContext context)

Lists all ServingConfigs linked to this dataStore.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListServingConfigsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ListServingConfigsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListServingConfigsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ListServingConfigsResponse)` | The response to send back to the client (wrapped by a task).  
  
### UpdateServingConfig(UpdateServingConfigRequest, ServerCallContext)
    
    
    public virtual Task<ServingConfig> UpdateServingConfig(UpdateServingConfigRequest request, ServerCallContext context)

Updates a ServingConfig.

Returns a NOT_FOUND error if the ServingConfig does not exist.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateServingConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.UpdateServingConfigRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ServingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ServingConfig)` | The response to send back to the client (wrapped by a task).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-24 UTC."],[],[]] 
