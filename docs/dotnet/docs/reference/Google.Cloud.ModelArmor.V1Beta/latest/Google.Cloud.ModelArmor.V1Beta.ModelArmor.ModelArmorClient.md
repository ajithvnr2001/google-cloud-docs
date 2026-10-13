---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.ModelArmor.ModelArmorClient
title: Model Armor v1beta API - Class ModelArmor.ModelArmorClient (1.0.0-beta06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:44:25.128970+00:00
---

# Model Armor v1beta API - Class ModelArmor.ModelArmorClient (1.0.0-beta06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.ModelArmor.ModelArmorClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Model Armor v1beta API - Class ModelArmor.ModelArmorClient (1.0.0-beta06) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta06 (latest)  1.0.0-beta05 
    
    
    public class ModelArmor.ModelArmorClient : ClientBase<ModelArmor.ModelArmorClient>

Reference documentation and code samples for the Model Armor v1beta API class ModelArmor.ModelArmorClient.

Client for ModelArmor

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html)[ModelArmor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.ModelArmor)[ModelArmorClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.ModelArmor.ModelArmorClient) > ModelArmor.ModelArmorClient

## Inherited Members

[ClientBase<ModelArmor.ModelArmorClient>.WithHost(string)](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html#Grpc_Core_ClientBase_1_WithHost_System_String_)

[ClientBase.CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html#Grpc_Core_ClientBase_CallInvoker)

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ModelArmor.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta)

## Assembly

Google.Cloud.ModelArmor.V1Beta.dll

## Constructors 

### ModelArmorClient()
    
    
    protected ModelArmorClient()

Protected parameterless constructor to allow creation of test doubles.

### ModelArmorClient(CallInvoker)
    
    
    public ModelArmorClient(CallInvoker callInvoker)

Creates a new client for ModelArmor that uses a custom `CallInvoker`.

**Parameter**  
---  
**Name** | **Description**  
`callInvoker` | `[CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallInvoker.html)`  
The callInvoker to use to make remote calls.  
  
### ModelArmorClient(ChannelBase)
    
    
    public ModelArmorClient(ChannelBase channel)

Creates a new client for ModelArmor

**Parameter**  
---  
**Name** | **Description**  
`channel` | `[ChannelBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ChannelBase.html)`  
The channel to use to make remote calls.  
  
### ModelArmorClient(ClientBaseConfiguration)
    
    
    protected ModelArmorClient(ClientBase.ClientBaseConfiguration configuration)

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
  
### CreateTemplate(CreateTemplateRequest, CallOptions)
    
    
    public virtual Template CreateTemplate(CreateTemplateRequest request, CallOptions options)

Creates a new Template in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.CreateTemplateRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)` | The response received from the server.  
  
### CreateTemplate(CreateTemplateRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Template CreateTemplate(CreateTemplateRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new Template in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.CreateTemplateRequest)`  
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
`[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)` | The response received from the server.  
  
### CreateTemplateAsync(CreateTemplateRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Template> CreateTemplateAsync(CreateTemplateRequest request, CallOptions options)

Creates a new Template in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.CreateTemplateRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)` | The call object.  
  
### CreateTemplateAsync(CreateTemplateRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Template> CreateTemplateAsync(CreateTemplateRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new Template in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.CreateTemplateRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)` | The call object.  
  
### DeleteTemplate(DeleteTemplateRequest, CallOptions)
    
    
    public virtual Empty DeleteTemplate(DeleteTemplateRequest request, CallOptions options)

Deletes a single Template.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.DeleteTemplateRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response received from the server.  
  
### DeleteTemplate(DeleteTemplateRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Empty DeleteTemplate(DeleteTemplateRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single Template.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.DeleteTemplateRequest)`  
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
`[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response received from the server.  
  
### DeleteTemplateAsync(DeleteTemplateRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteTemplateAsync(DeleteTemplateRequest request, CallOptions options)

Deletes a single Template.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.DeleteTemplateRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The call object.  
  
### DeleteTemplateAsync(DeleteTemplateRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteTemplateAsync(DeleteTemplateRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single Template.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.DeleteTemplateRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The call object.  
  
### GetFloorSetting(GetFloorSettingRequest, CallOptions)
    
    
    public virtual FloorSetting GetFloorSetting(GetFloorSettingRequest request, CallOptions options)

Gets details of a single floor setting of a project

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFloorSettingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.GetFloorSettingRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[FloorSetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.FloorSetting)` | The response received from the server.  
  
### GetFloorSetting(GetFloorSettingRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual FloorSetting GetFloorSetting(GetFloorSettingRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single floor setting of a project

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFloorSettingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.GetFloorSettingRequest)`  
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
`[FloorSetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.FloorSetting)` | The response received from the server.  
  
### GetFloorSettingAsync(GetFloorSettingRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<FloorSetting> GetFloorSettingAsync(GetFloorSettingRequest request, CallOptions options)

Gets details of a single floor setting of a project

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFloorSettingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.GetFloorSettingRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[FloorSetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.FloorSetting)` | The call object.  
  
### GetFloorSettingAsync(GetFloorSettingRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<FloorSetting> GetFloorSettingAsync(GetFloorSettingRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single floor setting of a project

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFloorSettingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.GetFloorSettingRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[FloorSetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.FloorSetting)` | The call object.  
  
### GetTemplate(GetTemplateRequest, CallOptions)
    
    
    public virtual Template GetTemplate(GetTemplateRequest request, CallOptions options)

Gets details of a single Template.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.GetTemplateRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)` | The response received from the server.  
  
### GetTemplate(GetTemplateRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Template GetTemplate(GetTemplateRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single Template.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.GetTemplateRequest)`  
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
`[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)` | The response received from the server.  
  
### GetTemplateAsync(GetTemplateRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Template> GetTemplateAsync(GetTemplateRequest request, CallOptions options)

Gets details of a single Template.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.GetTemplateRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)` | The call object.  
  
### GetTemplateAsync(GetTemplateRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Template> GetTemplateAsync(GetTemplateRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single Template.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.GetTemplateRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)` | The call object.  
  
### ListTemplates(ListTemplatesRequest, CallOptions)
    
    
    public virtual ListTemplatesResponse ListTemplates(ListTemplatesRequest request, CallOptions options)

Lists Templates in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListTemplatesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.ListTemplatesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListTemplatesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.ListTemplatesResponse)` | The response received from the server.  
  
### ListTemplates(ListTemplatesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListTemplatesResponse ListTemplates(ListTemplatesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists Templates in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListTemplatesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.ListTemplatesRequest)`  
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
`[ListTemplatesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.ListTemplatesResponse)` | The response received from the server.  
  
### ListTemplatesAsync(ListTemplatesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListTemplatesResponse> ListTemplatesAsync(ListTemplatesRequest request, CallOptions options)

Lists Templates in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListTemplatesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.ListTemplatesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListTemplatesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.ListTemplatesResponse)` | The call object.  
  
### ListTemplatesAsync(ListTemplatesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListTemplatesResponse> ListTemplatesAsync(ListTemplatesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists Templates in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListTemplatesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.ListTemplatesRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListTemplatesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.ListTemplatesResponse)` | The call object.  
  
### NewInstance(ClientBaseConfiguration)
    
    
    protected override ModelArmor.ModelArmorClient NewInstance(ClientBase.ClientBaseConfiguration configuration)

Creates a new instance of client from given `ClientBaseConfiguration`.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ModelArmor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.ModelArmor)[ModelArmorClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.ModelArmor.ModelArmorClient)` |   
**Overrides**

Grpc.Core.ClientBase<Google.Cloud.ModelArmor.V1Beta.ModelArmor.ModelArmorClient>.NewInstance(Grpc.Core.ClientBase.ClientBaseConfiguration)

### SanitizeModelResponse(SanitizeModelResponseRequest, CallOptions)
    
    
    public virtual SanitizeModelResponseResponse SanitizeModelResponse(SanitizeModelResponseRequest request, CallOptions options)

Sanitizes Model Response.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SanitizeModelResponseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.SanitizeModelResponseRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[SanitizeModelResponseResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.SanitizeModelResponseResponse)` | The response received from the server.  
  
### SanitizeModelResponse(SanitizeModelResponseRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual SanitizeModelResponseResponse SanitizeModelResponse(SanitizeModelResponseRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Sanitizes Model Response.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SanitizeModelResponseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.SanitizeModelResponseRequest)`  
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
`[SanitizeModelResponseResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.SanitizeModelResponseResponse)` | The response received from the server.  
  
### SanitizeModelResponseAsync(SanitizeModelResponseRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<SanitizeModelResponseResponse> SanitizeModelResponseAsync(SanitizeModelResponseRequest request, CallOptions options)

Sanitizes Model Response.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SanitizeModelResponseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.SanitizeModelResponseRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[SanitizeModelResponseResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.SanitizeModelResponseResponse)` | The call object.  
  
### SanitizeModelResponseAsync(SanitizeModelResponseRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<SanitizeModelResponseResponse> SanitizeModelResponseAsync(SanitizeModelResponseRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Sanitizes Model Response.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SanitizeModelResponseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.SanitizeModelResponseRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[SanitizeModelResponseResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.SanitizeModelResponseResponse)` | The call object.  
  
### SanitizeUserPrompt(SanitizeUserPromptRequest, CallOptions)
    
    
    public virtual SanitizeUserPromptResponse SanitizeUserPrompt(SanitizeUserPromptRequest request, CallOptions options)

Sanitizes User Prompt.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SanitizeUserPromptRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.SanitizeUserPromptRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[SanitizeUserPromptResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.SanitizeUserPromptResponse)` | The response received from the server.  
  
### SanitizeUserPrompt(SanitizeUserPromptRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual SanitizeUserPromptResponse SanitizeUserPrompt(SanitizeUserPromptRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Sanitizes User Prompt.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SanitizeUserPromptRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.SanitizeUserPromptRequest)`  
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
`[SanitizeUserPromptResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.SanitizeUserPromptResponse)` | The response received from the server.  
  
### SanitizeUserPromptAsync(SanitizeUserPromptRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<SanitizeUserPromptResponse> SanitizeUserPromptAsync(SanitizeUserPromptRequest request, CallOptions options)

Sanitizes User Prompt.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SanitizeUserPromptRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.SanitizeUserPromptRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[SanitizeUserPromptResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.SanitizeUserPromptResponse)` | The call object.  
  
### SanitizeUserPromptAsync(SanitizeUserPromptRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<SanitizeUserPromptResponse> SanitizeUserPromptAsync(SanitizeUserPromptRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Sanitizes User Prompt.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SanitizeUserPromptRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.SanitizeUserPromptRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[SanitizeUserPromptResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.SanitizeUserPromptResponse)` | The call object.  
  
### StreamSanitizeModelResponse(CallOptions)
    
    
    public virtual AsyncDuplexStreamingCall<SanitizeModelResponseRequest, SanitizeModelResponseResponse> StreamSanitizeModelResponse(CallOptions options)

Streaming version of Sanitizes Model Response.

**Parameter**  
---  
**Name** | **Description**  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncDuplexStreamingCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncDuplexStreamingCall-2.html)[SanitizeModelResponseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.SanitizeModelResponseRequest)[SanitizeModelResponseResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.SanitizeModelResponseResponse)` | The call object.  
  
### StreamSanitizeModelResponse(Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncDuplexStreamingCall<SanitizeModelResponseRequest, SanitizeModelResponseResponse> StreamSanitizeModelResponse(Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Streaming version of Sanitizes Model Response.

**Parameters**  
---  
**Name** | **Description**  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncDuplexStreamingCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncDuplexStreamingCall-2.html)[SanitizeModelResponseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.SanitizeModelResponseRequest)[SanitizeModelResponseResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.SanitizeModelResponseResponse)` | The call object.  
  
### StreamSanitizeUserPrompt(CallOptions)
    
    
    public virtual AsyncDuplexStreamingCall<SanitizeUserPromptRequest, SanitizeUserPromptResponse> StreamSanitizeUserPrompt(CallOptions options)

Streaming version of Sanitize User Prompt.

**Parameter**  
---  
**Name** | **Description**  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncDuplexStreamingCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncDuplexStreamingCall-2.html)[SanitizeUserPromptRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.SanitizeUserPromptRequest)[SanitizeUserPromptResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.SanitizeUserPromptResponse)` | The call object.  
  
### StreamSanitizeUserPrompt(Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncDuplexStreamingCall<SanitizeUserPromptRequest, SanitizeUserPromptResponse> StreamSanitizeUserPrompt(Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Streaming version of Sanitize User Prompt.

**Parameters**  
---  
**Name** | **Description**  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncDuplexStreamingCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncDuplexStreamingCall-2.html)[SanitizeUserPromptRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.SanitizeUserPromptRequest)[SanitizeUserPromptResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.SanitizeUserPromptResponse)` | The call object.  
  
### UpdateFloorSetting(UpdateFloorSettingRequest, CallOptions)
    
    
    public virtual FloorSetting UpdateFloorSetting(UpdateFloorSettingRequest request, CallOptions options)

Updates the parameters of a single floor setting of a project

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFloorSettingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.UpdateFloorSettingRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[FloorSetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.FloorSetting)` | The response received from the server.  
  
### UpdateFloorSetting(UpdateFloorSettingRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual FloorSetting UpdateFloorSetting(UpdateFloorSettingRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the parameters of a single floor setting of a project

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFloorSettingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.UpdateFloorSettingRequest)`  
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
`[FloorSetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.FloorSetting)` | The response received from the server.  
  
### UpdateFloorSettingAsync(UpdateFloorSettingRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<FloorSetting> UpdateFloorSettingAsync(UpdateFloorSettingRequest request, CallOptions options)

Updates the parameters of a single floor setting of a project

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFloorSettingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.UpdateFloorSettingRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[FloorSetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.FloorSetting)` | The call object.  
  
### UpdateFloorSettingAsync(UpdateFloorSettingRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<FloorSetting> UpdateFloorSettingAsync(UpdateFloorSettingRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the parameters of a single floor setting of a project

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFloorSettingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.UpdateFloorSettingRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[FloorSetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.FloorSetting)` | The call object.  
  
### UpdateTemplate(UpdateTemplateRequest, CallOptions)
    
    
    public virtual Template UpdateTemplate(UpdateTemplateRequest request, CallOptions options)

Updates the parameters of a single Template.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.UpdateTemplateRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)` | The response received from the server.  
  
### UpdateTemplate(UpdateTemplateRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Template UpdateTemplate(UpdateTemplateRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the parameters of a single Template.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.UpdateTemplateRequest)`  
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
`[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)` | The response received from the server.  
  
### UpdateTemplateAsync(UpdateTemplateRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Template> UpdateTemplateAsync(UpdateTemplateRequest request, CallOptions options)

Updates the parameters of a single Template.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.UpdateTemplateRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)` | The call object.  
  
### UpdateTemplateAsync(UpdateTemplateRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Template> UpdateTemplateAsync(UpdateTemplateRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the parameters of a single Template.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.UpdateTemplateRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Template](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.Template)` | The call object.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-05 UTC."],[],[]] 
