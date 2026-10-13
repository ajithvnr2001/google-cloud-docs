---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiRegistry.V1Beta/latest/Google.Cloud.ApiRegistry.V1Beta.CloudApiRegistry.CloudApiRegistryClient
title: Cloud API Registry v1beta API - Class CloudApiRegistry.CloudApiRegistryClient (1.0.0-beta01) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:20:55.971335+00:00
---

# Cloud API Registry v1beta API - Class CloudApiRegistry.CloudApiRegistryClient (1.0.0-beta01)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiRegistry.V1Beta/latest/Google.Cloud.ApiRegistry.V1Beta.CloudApiRegistry.CloudApiRegistryClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud API Registry v1beta API - Class CloudApiRegistry.CloudApiRegistryClient (1.0.0-beta01) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public class CloudApiRegistry.CloudApiRegistryClient : ClientBase<CloudApiRegistry.CloudApiRegistryClient>

Reference documentation and code samples for the Cloud API Registry v1beta API class CloudApiRegistry.CloudApiRegistryClient.

Client for CloudApiRegistry

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html)[CloudApiRegistry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiRegistry.V1Beta/latest/Google.Cloud.ApiRegistry.V1Beta.CloudApiRegistry)[CloudApiRegistryClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiRegistry.V1Beta/latest/Google.Cloud.ApiRegistry.V1Beta.CloudApiRegistry.CloudApiRegistryClient) > CloudApiRegistry.CloudApiRegistryClient

## Inherited Members

[ClientBase<CloudApiRegistry.CloudApiRegistryClient>.WithHost(string)](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html#Grpc_Core_ClientBase_1_WithHost_System_String_)

[ClientBase.CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html#Grpc_Core_ClientBase_CallInvoker)

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ApiRegistry.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiRegistry.V1Beta/latest/Google.Cloud.ApiRegistry.V1Beta)

## Assembly

Google.Cloud.ApiRegistry.V1Beta.dll

## Constructors 

### CloudApiRegistryClient()
    
    
    protected CloudApiRegistryClient()

Protected parameterless constructor to allow creation of test doubles.

### CloudApiRegistryClient(CallInvoker)
    
    
    public CloudApiRegistryClient(CallInvoker callInvoker)

Creates a new client for CloudApiRegistry that uses a custom `CallInvoker`.

**Parameter**  
---  
**Name** | **Description**  
`callInvoker` | `[CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallInvoker.html)`  
The callInvoker to use to make remote calls.  
  
### CloudApiRegistryClient(ChannelBase)
    
    
    public CloudApiRegistryClient(ChannelBase channel)

Creates a new client for CloudApiRegistry

**Parameter**  
---  
**Name** | **Description**  
`channel` | `[ChannelBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ChannelBase.html)`  
The channel to use to make remote calls.  
  
### CloudApiRegistryClient(ClientBaseConfiguration)
    
    
    protected CloudApiRegistryClient(ClientBase.ClientBaseConfiguration configuration)

Protected constructor to allow creation of configured clients.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
The client configuration.  
  
## Methods 

### CreateLocationsClient()
    
    
    public virtual Locations.LocationsClient CreateLocationsClient()

Creates a new instance of [Locations.LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.Locations.LocationsClient.html) using the same call invoker as this client.

**Returns**  
---  
**Type** | **Description**  
`[Locations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.Locations.html)[LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.Locations.LocationsClient.html)` | A new [Locations.LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.Locations.LocationsClient.html) for the same target as this client.  
  
### GetMcpServer(GetMcpServerRequest, CallOptions)
    
    
    public virtual McpServer GetMcpServer(GetMcpServerRequest request, CallOptions options)

Gets a single McpServer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetMcpServerRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiRegistry.V1Beta/latest/Google.Cloud.ApiRegistry.V1Beta.GetMcpServerRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[McpServer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiRegistry.V1Beta/latest/Google.Cloud.ApiRegistry.V1Beta.McpServer)` | The response received from the server.  
  
### GetMcpServer(GetMcpServerRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual McpServer GetMcpServer(GetMcpServerRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets a single McpServer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetMcpServerRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiRegistry.V1Beta/latest/Google.Cloud.ApiRegistry.V1Beta.GetMcpServerRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[McpServer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiRegistry.V1Beta/latest/Google.Cloud.ApiRegistry.V1Beta.McpServer)` | The response received from the server.  
  
### GetMcpServerAsync(GetMcpServerRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<McpServer> GetMcpServerAsync(GetMcpServerRequest request, CallOptions options)

Gets a single McpServer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetMcpServerRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiRegistry.V1Beta/latest/Google.Cloud.ApiRegistry.V1Beta.GetMcpServerRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[McpServer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiRegistry.V1Beta/latest/Google.Cloud.ApiRegistry.V1Beta.McpServer)` | The call object.  
  
### GetMcpServerAsync(GetMcpServerRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<McpServer> GetMcpServerAsync(GetMcpServerRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets a single McpServer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetMcpServerRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiRegistry.V1Beta/latest/Google.Cloud.ApiRegistry.V1Beta.GetMcpServerRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[McpServer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiRegistry.V1Beta/latest/Google.Cloud.ApiRegistry.V1Beta.McpServer)` | The call object.  
  
### GetMcpTool(GetMcpToolRequest, CallOptions)
    
    
    public virtual McpTool GetMcpTool(GetMcpToolRequest request, CallOptions options)

Gets a single McpTool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetMcpToolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiRegistry.V1Beta/latest/Google.Cloud.ApiRegistry.V1Beta.GetMcpToolRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[McpTool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiRegistry.V1Beta/latest/Google.Cloud.ApiRegistry.V1Beta.McpTool)` | The response received from the server.  
  
### GetMcpTool(GetMcpToolRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual McpTool GetMcpTool(GetMcpToolRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets a single McpTool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetMcpToolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiRegistry.V1Beta/latest/Google.Cloud.ApiRegistry.V1Beta.GetMcpToolRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[McpTool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiRegistry.V1Beta/latest/Google.Cloud.ApiRegistry.V1Beta.McpTool)` | The response received from the server.  
  
### GetMcpToolAsync(GetMcpToolRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<McpTool> GetMcpToolAsync(GetMcpToolRequest request, CallOptions options)

Gets a single McpTool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetMcpToolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiRegistry.V1Beta/latest/Google.Cloud.ApiRegistry.V1Beta.GetMcpToolRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[McpTool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiRegistry.V1Beta/latest/Google.Cloud.ApiRegistry.V1Beta.McpTool)` | The call object.  
  
### GetMcpToolAsync(GetMcpToolRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<McpTool> GetMcpToolAsync(GetMcpToolRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets a single McpTool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetMcpToolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiRegistry.V1Beta/latest/Google.Cloud.ApiRegistry.V1Beta.GetMcpToolRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[McpTool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiRegistry.V1Beta/latest/Google.Cloud.ApiRegistry.V1Beta.McpTool)` | The call object.  
  
### ListMcpServers(ListMcpServersRequest, CallOptions)
    
    
    public virtual ListMcpServersResponse ListMcpServers(ListMcpServersRequest request, CallOptions options)

Lists McpServers in a given Project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListMcpServersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiRegistry.V1Beta/latest/Google.Cloud.ApiRegistry.V1Beta.ListMcpServersRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListMcpServersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiRegistry.V1Beta/latest/Google.Cloud.ApiRegistry.V1Beta.ListMcpServersResponse)` | The response received from the server.  
  
### ListMcpServers(ListMcpServersRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListMcpServersResponse ListMcpServers(ListMcpServersRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists McpServers in a given Project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListMcpServersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiRegistry.V1Beta/latest/Google.Cloud.ApiRegistry.V1Beta.ListMcpServersRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListMcpServersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiRegistry.V1Beta/latest/Google.Cloud.ApiRegistry.V1Beta.ListMcpServersResponse)` | The response received from the server.  
  
### ListMcpServersAsync(ListMcpServersRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListMcpServersResponse> ListMcpServersAsync(ListMcpServersRequest request, CallOptions options)

Lists McpServers in a given Project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListMcpServersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiRegistry.V1Beta/latest/Google.Cloud.ApiRegistry.V1Beta.ListMcpServersRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListMcpServersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiRegistry.V1Beta/latest/Google.Cloud.ApiRegistry.V1Beta.ListMcpServersResponse)` | The call object.  
  
### ListMcpServersAsync(ListMcpServersRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListMcpServersResponse> ListMcpServersAsync(ListMcpServersRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists McpServers in a given Project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListMcpServersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiRegistry.V1Beta/latest/Google.Cloud.ApiRegistry.V1Beta.ListMcpServersRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListMcpServersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiRegistry.V1Beta/latest/Google.Cloud.ApiRegistry.V1Beta.ListMcpServersResponse)` | The call object.  
  
### ListMcpTools(ListMcpToolsRequest, CallOptions)
    
    
    public virtual ListMcpToolsResponse ListMcpTools(ListMcpToolsRequest request, CallOptions options)

Lists McpTools in a given McpServer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListMcpToolsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiRegistry.V1Beta/latest/Google.Cloud.ApiRegistry.V1Beta.ListMcpToolsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListMcpToolsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiRegistry.V1Beta/latest/Google.Cloud.ApiRegistry.V1Beta.ListMcpToolsResponse)` | The response received from the server.  
  
### ListMcpTools(ListMcpToolsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListMcpToolsResponse ListMcpTools(ListMcpToolsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists McpTools in a given McpServer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListMcpToolsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiRegistry.V1Beta/latest/Google.Cloud.ApiRegistry.V1Beta.ListMcpToolsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListMcpToolsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiRegistry.V1Beta/latest/Google.Cloud.ApiRegistry.V1Beta.ListMcpToolsResponse)` | The response received from the server.  
  
### ListMcpToolsAsync(ListMcpToolsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListMcpToolsResponse> ListMcpToolsAsync(ListMcpToolsRequest request, CallOptions options)

Lists McpTools in a given McpServer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListMcpToolsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiRegistry.V1Beta/latest/Google.Cloud.ApiRegistry.V1Beta.ListMcpToolsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListMcpToolsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiRegistry.V1Beta/latest/Google.Cloud.ApiRegistry.V1Beta.ListMcpToolsResponse)` | The call object.  
  
### ListMcpToolsAsync(ListMcpToolsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListMcpToolsResponse> ListMcpToolsAsync(ListMcpToolsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists McpTools in a given McpServer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListMcpToolsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiRegistry.V1Beta/latest/Google.Cloud.ApiRegistry.V1Beta.ListMcpToolsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListMcpToolsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiRegistry.V1Beta/latest/Google.Cloud.ApiRegistry.V1Beta.ListMcpToolsResponse)` | The call object.  
  
### NewInstance(ClientBaseConfiguration)
    
    
    protected override CloudApiRegistry.CloudApiRegistryClient NewInstance(ClientBase.ClientBaseConfiguration configuration)

Creates a new instance of client from given `ClientBaseConfiguration`.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CloudApiRegistry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiRegistry.V1Beta/latest/Google.Cloud.ApiRegistry.V1Beta.CloudApiRegistry)[CloudApiRegistryClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiRegistry.V1Beta/latest/Google.Cloud.ApiRegistry.V1Beta.CloudApiRegistry.CloudApiRegistryClient)` |   
**Overrides**

Grpc.Core.ClientBase<Google.Cloud.ApiRegistry.V1Beta.CloudApiRegistry.CloudApiRegistryClient>.NewInstance(Grpc.Core.ClientBase.ClientBaseConfiguration)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-29 UTC."],[],[]] 
