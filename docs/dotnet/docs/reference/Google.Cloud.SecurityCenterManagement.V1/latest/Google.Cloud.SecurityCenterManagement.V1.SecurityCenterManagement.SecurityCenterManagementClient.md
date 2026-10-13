---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SecurityCenterManagement.SecurityCenterManagementClient
title: Security Center Management v1 API - Class SecurityCenterManagement.SecurityCenterManagementClient (1.3.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:11:01.880460+00:00
---

# Security Center Management v1 API - Class SecurityCenterManagement.SecurityCenterManagementClient (1.3.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SecurityCenterManagement.SecurityCenterManagementClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Security Center Management v1 API - Class SecurityCenterManagement.SecurityCenterManagementClient (1.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.3.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SecurityCenterManagement.SecurityCenterManagementClient)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/1.2.0/Google.Cloud.SecurityCenterManagement.V1.SecurityCenterManagement.SecurityCenterManagementClient)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/1.1.0/Google.Cloud.SecurityCenterManagement.V1.SecurityCenterManagement.SecurityCenterManagementClient)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/1.0.0/Google.Cloud.SecurityCenterManagement.V1.SecurityCenterManagement.SecurityCenterManagementClient)


    
    
    public class SecurityCenterManagement.SecurityCenterManagementClient : ClientBase<SecurityCenterManagement.SecurityCenterManagementClient>

Reference documentation and code samples for the Security Center Management v1 API class SecurityCenterManagement.SecurityCenterManagementClient.

Client for SecurityCenterManagement

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html)[SecurityCenterManagement](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SecurityCenterManagement)[SecurityCenterManagementClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SecurityCenterManagement.SecurityCenterManagementClient) > SecurityCenterManagement.SecurityCenterManagementClient

## Inherited Members

[ClientBase<SecurityCenterManagement.SecurityCenterManagementClient>.WithHost(string)](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html#Grpc_Core_ClientBase_1_WithHost_System_String_)

[ClientBase.CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html#Grpc_Core_ClientBase_CallInvoker)

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.SecurityCenterManagement.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1)

## Assembly

Google.Cloud.SecurityCenterManagement.V1.dll

## Constructors 

### SecurityCenterManagementClient()
    
    
    protected SecurityCenterManagementClient()

Protected parameterless constructor to allow creation of test doubles.

### SecurityCenterManagementClient(CallInvoker)
    
    
    public SecurityCenterManagementClient(CallInvoker callInvoker)

Creates a new client for SecurityCenterManagement that uses a custom `CallInvoker`.

**Parameter**  
---  
**Name** | **Description**  
`callInvoker` | `[CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallInvoker.html)`  
The callInvoker to use to make remote calls.  
  
### SecurityCenterManagementClient(ChannelBase)
    
    
    public SecurityCenterManagementClient(ChannelBase channel)

Creates a new client for SecurityCenterManagement

**Parameter**  
---  
**Name** | **Description**  
`channel` | `[ChannelBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ChannelBase.html)`  
The channel to use to make remote calls.  
  
### SecurityCenterManagementClient(ClientBaseConfiguration)
    
    
    protected SecurityCenterManagementClient(ClientBase.ClientBaseConfiguration configuration)

Protected constructor to allow creation of configured clients.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
The client configuration.  
  
## Methods 

### CreateEventThreatDetectionCustomModule(CreateEventThreatDetectionCustomModuleRequest, CallOptions)
    
    
    public virtual EventThreatDetectionCustomModule CreateEventThreatDetectionCustomModule(CreateEventThreatDetectionCustomModuleRequest request, CallOptions options)

Creates a resident Event Threat Detection custom module at the scope of the given organization, folder, or project, and creates inherited custom modules for all descendants of the given parent. These modules are enabled by default.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.CreateEventThreatDetectionCustomModuleRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[EventThreatDetectionCustomModule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.EventThreatDetectionCustomModule)` | The response received from the server.  
  
### CreateEventThreatDetectionCustomModule(CreateEventThreatDetectionCustomModuleRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual EventThreatDetectionCustomModule CreateEventThreatDetectionCustomModule(CreateEventThreatDetectionCustomModuleRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a resident Event Threat Detection custom module at the scope of the given organization, folder, or project, and creates inherited custom modules for all descendants of the given parent. These modules are enabled by default.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.CreateEventThreatDetectionCustomModuleRequest)`  
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
`[EventThreatDetectionCustomModule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.EventThreatDetectionCustomModule)` | The response received from the server.  
  
### CreateEventThreatDetectionCustomModuleAsync(CreateEventThreatDetectionCustomModuleRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<EventThreatDetectionCustomModule> CreateEventThreatDetectionCustomModuleAsync(CreateEventThreatDetectionCustomModuleRequest request, CallOptions options)

Creates a resident Event Threat Detection custom module at the scope of the given organization, folder, or project, and creates inherited custom modules for all descendants of the given parent. These modules are enabled by default.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.CreateEventThreatDetectionCustomModuleRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[EventThreatDetectionCustomModule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.EventThreatDetectionCustomModule)` | The call object.  
  
### CreateEventThreatDetectionCustomModuleAsync(CreateEventThreatDetectionCustomModuleRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<EventThreatDetectionCustomModule> CreateEventThreatDetectionCustomModuleAsync(CreateEventThreatDetectionCustomModuleRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a resident Event Threat Detection custom module at the scope of the given organization, folder, or project, and creates inherited custom modules for all descendants of the given parent. These modules are enabled by default.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.CreateEventThreatDetectionCustomModuleRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[EventThreatDetectionCustomModule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.EventThreatDetectionCustomModule)` | The call object.  
  
### CreateLocationsClient()
    
    
    public virtual Locations.LocationsClient CreateLocationsClient()

Creates a new instance of [Locations.LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.Locations.LocationsClient.html) using the same call invoker as this client.

**Returns**  
---  
**Type** | **Description**  
`[Locations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.Locations.html)[LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.Locations.LocationsClient.html)` | A new [Locations.LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.Locations.LocationsClient.html) for the same target as this client.  
  
### CreateSecurityHealthAnalyticsCustomModule(CreateSecurityHealthAnalyticsCustomModuleRequest, CallOptions)
    
    
    public virtual SecurityHealthAnalyticsCustomModule CreateSecurityHealthAnalyticsCustomModule(CreateSecurityHealthAnalyticsCustomModuleRequest request, CallOptions options)

Creates a resident [SecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule] at the scope of the given organization, folder, or project, and also creates inherited `SecurityHealthAnalyticsCustomModule` resources for all folders and projects that are descendants of the given parent. These modules are enabled by default.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.CreateSecurityHealthAnalyticsCustomModuleRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SecurityHealthAnalyticsCustomModule)` | The response received from the server.  
  
### CreateSecurityHealthAnalyticsCustomModule(CreateSecurityHealthAnalyticsCustomModuleRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual SecurityHealthAnalyticsCustomModule CreateSecurityHealthAnalyticsCustomModule(CreateSecurityHealthAnalyticsCustomModuleRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a resident [SecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule] at the scope of the given organization, folder, or project, and also creates inherited `SecurityHealthAnalyticsCustomModule` resources for all folders and projects that are descendants of the given parent. These modules are enabled by default.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.CreateSecurityHealthAnalyticsCustomModuleRequest)`  
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
`[SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SecurityHealthAnalyticsCustomModule)` | The response received from the server.  
  
### CreateSecurityHealthAnalyticsCustomModuleAsync(CreateSecurityHealthAnalyticsCustomModuleRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<SecurityHealthAnalyticsCustomModule> CreateSecurityHealthAnalyticsCustomModuleAsync(CreateSecurityHealthAnalyticsCustomModuleRequest request, CallOptions options)

Creates a resident [SecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule] at the scope of the given organization, folder, or project, and also creates inherited `SecurityHealthAnalyticsCustomModule` resources for all folders and projects that are descendants of the given parent. These modules are enabled by default.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.CreateSecurityHealthAnalyticsCustomModuleRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SecurityHealthAnalyticsCustomModule)` | The call object.  
  
### CreateSecurityHealthAnalyticsCustomModuleAsync(CreateSecurityHealthAnalyticsCustomModuleRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<SecurityHealthAnalyticsCustomModule> CreateSecurityHealthAnalyticsCustomModuleAsync(CreateSecurityHealthAnalyticsCustomModuleRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a resident [SecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule] at the scope of the given organization, folder, or project, and also creates inherited `SecurityHealthAnalyticsCustomModule` resources for all folders and projects that are descendants of the given parent. These modules are enabled by default.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.CreateSecurityHealthAnalyticsCustomModuleRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SecurityHealthAnalyticsCustomModule)` | The call object.  
  
### DeleteEventThreatDetectionCustomModule(DeleteEventThreatDetectionCustomModuleRequest, CallOptions)
    
    
    public virtual Empty DeleteEventThreatDetectionCustomModule(DeleteEventThreatDetectionCustomModuleRequest request, CallOptions options)

Deletes the specified Event Threat Detection custom module and all of its descendants in the resource hierarchy. This method is only supported for resident custom modules.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.DeleteEventThreatDetectionCustomModuleRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response received from the server.  
  
### DeleteEventThreatDetectionCustomModule(DeleteEventThreatDetectionCustomModuleRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Empty DeleteEventThreatDetectionCustomModule(DeleteEventThreatDetectionCustomModuleRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes the specified Event Threat Detection custom module and all of its descendants in the resource hierarchy. This method is only supported for resident custom modules.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.DeleteEventThreatDetectionCustomModuleRequest)`  
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
  
### DeleteEventThreatDetectionCustomModuleAsync(DeleteEventThreatDetectionCustomModuleRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteEventThreatDetectionCustomModuleAsync(DeleteEventThreatDetectionCustomModuleRequest request, CallOptions options)

Deletes the specified Event Threat Detection custom module and all of its descendants in the resource hierarchy. This method is only supported for resident custom modules.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.DeleteEventThreatDetectionCustomModuleRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The call object.  
  
### DeleteEventThreatDetectionCustomModuleAsync(DeleteEventThreatDetectionCustomModuleRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteEventThreatDetectionCustomModuleAsync(DeleteEventThreatDetectionCustomModuleRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes the specified Event Threat Detection custom module and all of its descendants in the resource hierarchy. This method is only supported for resident custom modules.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.DeleteEventThreatDetectionCustomModuleRequest)`  
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
  
### DeleteSecurityHealthAnalyticsCustomModule(DeleteSecurityHealthAnalyticsCustomModuleRequest, CallOptions)
    
    
    public virtual Empty DeleteSecurityHealthAnalyticsCustomModule(DeleteSecurityHealthAnalyticsCustomModuleRequest request, CallOptions options)

Deletes the specified [SecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule] and all of its descendants in the resource hierarchy. This method is only supported for resident custom modules.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.DeleteSecurityHealthAnalyticsCustomModuleRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response received from the server.  
  
### DeleteSecurityHealthAnalyticsCustomModule(DeleteSecurityHealthAnalyticsCustomModuleRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Empty DeleteSecurityHealthAnalyticsCustomModule(DeleteSecurityHealthAnalyticsCustomModuleRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes the specified [SecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule] and all of its descendants in the resource hierarchy. This method is only supported for resident custom modules.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.DeleteSecurityHealthAnalyticsCustomModuleRequest)`  
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
  
### DeleteSecurityHealthAnalyticsCustomModuleAsync(DeleteSecurityHealthAnalyticsCustomModuleRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteSecurityHealthAnalyticsCustomModuleAsync(DeleteSecurityHealthAnalyticsCustomModuleRequest request, CallOptions options)

Deletes the specified [SecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule] and all of its descendants in the resource hierarchy. This method is only supported for resident custom modules.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.DeleteSecurityHealthAnalyticsCustomModuleRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The call object.  
  
### DeleteSecurityHealthAnalyticsCustomModuleAsync(DeleteSecurityHealthAnalyticsCustomModuleRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteSecurityHealthAnalyticsCustomModuleAsync(DeleteSecurityHealthAnalyticsCustomModuleRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes the specified [SecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule] and all of its descendants in the resource hierarchy. This method is only supported for resident custom modules.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.DeleteSecurityHealthAnalyticsCustomModuleRequest)`  
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
  
### GetEffectiveEventThreatDetectionCustomModule(GetEffectiveEventThreatDetectionCustomModuleRequest, CallOptions)
    
    
    public virtual EffectiveEventThreatDetectionCustomModule GetEffectiveEventThreatDetectionCustomModule(GetEffectiveEventThreatDetectionCustomModuleRequest request, CallOptions options)

Gets the effective Event Threat Detection custom module at the given level.

The difference between an [EffectiveEventThreatDetectionCustomModule][google.cloud.securitycentermanagement.v1.EffectiveEventThreatDetectionCustomModule] and an [EventThreatDetectionCustomModule][google.cloud.securitycentermanagement.v1.EventThreatDetectionCustomModule] is that the fields for an `EffectiveEventThreatDetectionCustomModule` are computed from ancestors if needed. For example, the enablement state for an `EventThreatDetectionCustomModule` can be `ENABLED`, `DISABLED`, or `INHERITED`. In contrast, the enablement state for an `EffectiveEventThreatDetectionCustomModule` is always computed as `ENABLED` or `DISABLED`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetEffectiveEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.GetEffectiveEventThreatDetectionCustomModuleRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[EffectiveEventThreatDetectionCustomModule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.EffectiveEventThreatDetectionCustomModule)` | The response received from the server.  
  
### GetEffectiveEventThreatDetectionCustomModule(GetEffectiveEventThreatDetectionCustomModuleRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual EffectiveEventThreatDetectionCustomModule GetEffectiveEventThreatDetectionCustomModule(GetEffectiveEventThreatDetectionCustomModuleRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets the effective Event Threat Detection custom module at the given level.

The difference between an [EffectiveEventThreatDetectionCustomModule][google.cloud.securitycentermanagement.v1.EffectiveEventThreatDetectionCustomModule] and an [EventThreatDetectionCustomModule][google.cloud.securitycentermanagement.v1.EventThreatDetectionCustomModule] is that the fields for an `EffectiveEventThreatDetectionCustomModule` are computed from ancestors if needed. For example, the enablement state for an `EventThreatDetectionCustomModule` can be `ENABLED`, `DISABLED`, or `INHERITED`. In contrast, the enablement state for an `EffectiveEventThreatDetectionCustomModule` is always computed as `ENABLED` or `DISABLED`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetEffectiveEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.GetEffectiveEventThreatDetectionCustomModuleRequest)`  
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
`[EffectiveEventThreatDetectionCustomModule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.EffectiveEventThreatDetectionCustomModule)` | The response received from the server.  
  
### GetEffectiveEventThreatDetectionCustomModuleAsync(GetEffectiveEventThreatDetectionCustomModuleRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<EffectiveEventThreatDetectionCustomModule> GetEffectiveEventThreatDetectionCustomModuleAsync(GetEffectiveEventThreatDetectionCustomModuleRequest request, CallOptions options)

Gets the effective Event Threat Detection custom module at the given level.

The difference between an [EffectiveEventThreatDetectionCustomModule][google.cloud.securitycentermanagement.v1.EffectiveEventThreatDetectionCustomModule] and an [EventThreatDetectionCustomModule][google.cloud.securitycentermanagement.v1.EventThreatDetectionCustomModule] is that the fields for an `EffectiveEventThreatDetectionCustomModule` are computed from ancestors if needed. For example, the enablement state for an `EventThreatDetectionCustomModule` can be `ENABLED`, `DISABLED`, or `INHERITED`. In contrast, the enablement state for an `EffectiveEventThreatDetectionCustomModule` is always computed as `ENABLED` or `DISABLED`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetEffectiveEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.GetEffectiveEventThreatDetectionCustomModuleRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[EffectiveEventThreatDetectionCustomModule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.EffectiveEventThreatDetectionCustomModule)` | The call object.  
  
### GetEffectiveEventThreatDetectionCustomModuleAsync(GetEffectiveEventThreatDetectionCustomModuleRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<EffectiveEventThreatDetectionCustomModule> GetEffectiveEventThreatDetectionCustomModuleAsync(GetEffectiveEventThreatDetectionCustomModuleRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets the effective Event Threat Detection custom module at the given level.

The difference between an [EffectiveEventThreatDetectionCustomModule][google.cloud.securitycentermanagement.v1.EffectiveEventThreatDetectionCustomModule] and an [EventThreatDetectionCustomModule][google.cloud.securitycentermanagement.v1.EventThreatDetectionCustomModule] is that the fields for an `EffectiveEventThreatDetectionCustomModule` are computed from ancestors if needed. For example, the enablement state for an `EventThreatDetectionCustomModule` can be `ENABLED`, `DISABLED`, or `INHERITED`. In contrast, the enablement state for an `EffectiveEventThreatDetectionCustomModule` is always computed as `ENABLED` or `DISABLED`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetEffectiveEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.GetEffectiveEventThreatDetectionCustomModuleRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[EffectiveEventThreatDetectionCustomModule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.EffectiveEventThreatDetectionCustomModule)` | The call object.  
  
### GetEffectiveSecurityHealthAnalyticsCustomModule(GetEffectiveSecurityHealthAnalyticsCustomModuleRequest, CallOptions)
    
    
    public virtual EffectiveSecurityHealthAnalyticsCustomModule GetEffectiveSecurityHealthAnalyticsCustomModule(GetEffectiveSecurityHealthAnalyticsCustomModuleRequest request, CallOptions options)

Gets details of a single [EffectiveSecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.EffectiveSecurityHealthAnalyticsCustomModule].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetEffectiveSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.GetEffectiveSecurityHealthAnalyticsCustomModuleRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[EffectiveSecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.EffectiveSecurityHealthAnalyticsCustomModule)` | The response received from the server.  
  
### GetEffectiveSecurityHealthAnalyticsCustomModule(GetEffectiveSecurityHealthAnalyticsCustomModuleRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual EffectiveSecurityHealthAnalyticsCustomModule GetEffectiveSecurityHealthAnalyticsCustomModule(GetEffectiveSecurityHealthAnalyticsCustomModuleRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single [EffectiveSecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.EffectiveSecurityHealthAnalyticsCustomModule].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetEffectiveSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.GetEffectiveSecurityHealthAnalyticsCustomModuleRequest)`  
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
`[EffectiveSecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.EffectiveSecurityHealthAnalyticsCustomModule)` | The response received from the server.  
  
### GetEffectiveSecurityHealthAnalyticsCustomModuleAsync(GetEffectiveSecurityHealthAnalyticsCustomModuleRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<EffectiveSecurityHealthAnalyticsCustomModule> GetEffectiveSecurityHealthAnalyticsCustomModuleAsync(GetEffectiveSecurityHealthAnalyticsCustomModuleRequest request, CallOptions options)

Gets details of a single [EffectiveSecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.EffectiveSecurityHealthAnalyticsCustomModule].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetEffectiveSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.GetEffectiveSecurityHealthAnalyticsCustomModuleRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[EffectiveSecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.EffectiveSecurityHealthAnalyticsCustomModule)` | The call object.  
  
### GetEffectiveSecurityHealthAnalyticsCustomModuleAsync(GetEffectiveSecurityHealthAnalyticsCustomModuleRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<EffectiveSecurityHealthAnalyticsCustomModule> GetEffectiveSecurityHealthAnalyticsCustomModuleAsync(GetEffectiveSecurityHealthAnalyticsCustomModuleRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single [EffectiveSecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.EffectiveSecurityHealthAnalyticsCustomModule].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetEffectiveSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.GetEffectiveSecurityHealthAnalyticsCustomModuleRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[EffectiveSecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.EffectiveSecurityHealthAnalyticsCustomModule)` | The call object.  
  
### GetEventThreatDetectionCustomModule(GetEventThreatDetectionCustomModuleRequest, CallOptions)
    
    
    public virtual EventThreatDetectionCustomModule GetEventThreatDetectionCustomModule(GetEventThreatDetectionCustomModuleRequest request, CallOptions options)

Gets an Event Threat Detection custom module.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.GetEventThreatDetectionCustomModuleRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[EventThreatDetectionCustomModule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.EventThreatDetectionCustomModule)` | The response received from the server.  
  
### GetEventThreatDetectionCustomModule(GetEventThreatDetectionCustomModuleRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual EventThreatDetectionCustomModule GetEventThreatDetectionCustomModule(GetEventThreatDetectionCustomModuleRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets an Event Threat Detection custom module.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.GetEventThreatDetectionCustomModuleRequest)`  
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
`[EventThreatDetectionCustomModule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.EventThreatDetectionCustomModule)` | The response received from the server.  
  
### GetEventThreatDetectionCustomModuleAsync(GetEventThreatDetectionCustomModuleRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<EventThreatDetectionCustomModule> GetEventThreatDetectionCustomModuleAsync(GetEventThreatDetectionCustomModuleRequest request, CallOptions options)

Gets an Event Threat Detection custom module.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.GetEventThreatDetectionCustomModuleRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[EventThreatDetectionCustomModule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.EventThreatDetectionCustomModule)` | The call object.  
  
### GetEventThreatDetectionCustomModuleAsync(GetEventThreatDetectionCustomModuleRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<EventThreatDetectionCustomModule> GetEventThreatDetectionCustomModuleAsync(GetEventThreatDetectionCustomModuleRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets an Event Threat Detection custom module.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.GetEventThreatDetectionCustomModuleRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[EventThreatDetectionCustomModule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.EventThreatDetectionCustomModule)` | The call object.  
  
### GetSecurityCenterService(GetSecurityCenterServiceRequest, CallOptions)
    
    
    public virtual SecurityCenterService GetSecurityCenterService(GetSecurityCenterServiceRequest request, CallOptions options)

Gets service settings for the specified Security Command Center service.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSecurityCenterServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.GetSecurityCenterServiceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SecurityCenterService)` | The response received from the server.  
  
### GetSecurityCenterService(GetSecurityCenterServiceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual SecurityCenterService GetSecurityCenterService(GetSecurityCenterServiceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets service settings for the specified Security Command Center service.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSecurityCenterServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.GetSecurityCenterServiceRequest)`  
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
`[SecurityCenterService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SecurityCenterService)` | The response received from the server.  
  
### GetSecurityCenterServiceAsync(GetSecurityCenterServiceRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<SecurityCenterService> GetSecurityCenterServiceAsync(GetSecurityCenterServiceRequest request, CallOptions options)

Gets service settings for the specified Security Command Center service.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSecurityCenterServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.GetSecurityCenterServiceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[SecurityCenterService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SecurityCenterService)` | The call object.  
  
### GetSecurityCenterServiceAsync(GetSecurityCenterServiceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<SecurityCenterService> GetSecurityCenterServiceAsync(GetSecurityCenterServiceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets service settings for the specified Security Command Center service.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSecurityCenterServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.GetSecurityCenterServiceRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[SecurityCenterService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SecurityCenterService)` | The call object.  
  
### GetSecurityHealthAnalyticsCustomModule(GetSecurityHealthAnalyticsCustomModuleRequest, CallOptions)
    
    
    public virtual SecurityHealthAnalyticsCustomModule GetSecurityHealthAnalyticsCustomModule(GetSecurityHealthAnalyticsCustomModuleRequest request, CallOptions options)

Retrieves a [SecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.GetSecurityHealthAnalyticsCustomModuleRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SecurityHealthAnalyticsCustomModule)` | The response received from the server.  
  
### GetSecurityHealthAnalyticsCustomModule(GetSecurityHealthAnalyticsCustomModuleRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual SecurityHealthAnalyticsCustomModule GetSecurityHealthAnalyticsCustomModule(GetSecurityHealthAnalyticsCustomModuleRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Retrieves a [SecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.GetSecurityHealthAnalyticsCustomModuleRequest)`  
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
`[SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SecurityHealthAnalyticsCustomModule)` | The response received from the server.  
  
### GetSecurityHealthAnalyticsCustomModuleAsync(GetSecurityHealthAnalyticsCustomModuleRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<SecurityHealthAnalyticsCustomModule> GetSecurityHealthAnalyticsCustomModuleAsync(GetSecurityHealthAnalyticsCustomModuleRequest request, CallOptions options)

Retrieves a [SecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.GetSecurityHealthAnalyticsCustomModuleRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SecurityHealthAnalyticsCustomModule)` | The call object.  
  
### GetSecurityHealthAnalyticsCustomModuleAsync(GetSecurityHealthAnalyticsCustomModuleRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<SecurityHealthAnalyticsCustomModule> GetSecurityHealthAnalyticsCustomModuleAsync(GetSecurityHealthAnalyticsCustomModuleRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Retrieves a [SecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.GetSecurityHealthAnalyticsCustomModuleRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SecurityHealthAnalyticsCustomModule)` | The call object.  
  
### ListDescendantEventThreatDetectionCustomModules(ListDescendantEventThreatDetectionCustomModulesRequest, CallOptions)
    
    
    public virtual ListDescendantEventThreatDetectionCustomModulesResponse ListDescendantEventThreatDetectionCustomModules(ListDescendantEventThreatDetectionCustomModulesRequest request, CallOptions options)

Lists all resident Event Threat Detection custom modules for the given organization, folder, or project and its descendants.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDescendantEventThreatDetectionCustomModulesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListDescendantEventThreatDetectionCustomModulesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListDescendantEventThreatDetectionCustomModulesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListDescendantEventThreatDetectionCustomModulesResponse)` | The response received from the server.  
  
### ListDescendantEventThreatDetectionCustomModules(ListDescendantEventThreatDetectionCustomModulesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListDescendantEventThreatDetectionCustomModulesResponse ListDescendantEventThreatDetectionCustomModules(ListDescendantEventThreatDetectionCustomModulesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all resident Event Threat Detection custom modules for the given organization, folder, or project and its descendants.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDescendantEventThreatDetectionCustomModulesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListDescendantEventThreatDetectionCustomModulesRequest)`  
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
`[ListDescendantEventThreatDetectionCustomModulesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListDescendantEventThreatDetectionCustomModulesResponse)` | The response received from the server.  
  
### ListDescendantEventThreatDetectionCustomModulesAsync(ListDescendantEventThreatDetectionCustomModulesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListDescendantEventThreatDetectionCustomModulesResponse> ListDescendantEventThreatDetectionCustomModulesAsync(ListDescendantEventThreatDetectionCustomModulesRequest request, CallOptions options)

Lists all resident Event Threat Detection custom modules for the given organization, folder, or project and its descendants.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDescendantEventThreatDetectionCustomModulesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListDescendantEventThreatDetectionCustomModulesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListDescendantEventThreatDetectionCustomModulesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListDescendantEventThreatDetectionCustomModulesResponse)` | The call object.  
  
### ListDescendantEventThreatDetectionCustomModulesAsync(ListDescendantEventThreatDetectionCustomModulesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListDescendantEventThreatDetectionCustomModulesResponse> ListDescendantEventThreatDetectionCustomModulesAsync(ListDescendantEventThreatDetectionCustomModulesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all resident Event Threat Detection custom modules for the given organization, folder, or project and its descendants.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDescendantEventThreatDetectionCustomModulesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListDescendantEventThreatDetectionCustomModulesRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListDescendantEventThreatDetectionCustomModulesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListDescendantEventThreatDetectionCustomModulesResponse)` | The call object.  
  
### ListDescendantSecurityHealthAnalyticsCustomModules(ListDescendantSecurityHealthAnalyticsCustomModulesRequest, CallOptions)
    
    
    public virtual ListDescendantSecurityHealthAnalyticsCustomModulesResponse ListDescendantSecurityHealthAnalyticsCustomModules(ListDescendantSecurityHealthAnalyticsCustomModulesRequest request, CallOptions options)

Returns a list of all resident [SecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule] resources under the given organization, folder, or project and all of its descendants.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDescendantSecurityHealthAnalyticsCustomModulesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListDescendantSecurityHealthAnalyticsCustomModulesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListDescendantSecurityHealthAnalyticsCustomModulesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListDescendantSecurityHealthAnalyticsCustomModulesResponse)` | The response received from the server.  
  
### ListDescendantSecurityHealthAnalyticsCustomModules(ListDescendantSecurityHealthAnalyticsCustomModulesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListDescendantSecurityHealthAnalyticsCustomModulesResponse ListDescendantSecurityHealthAnalyticsCustomModules(ListDescendantSecurityHealthAnalyticsCustomModulesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns a list of all resident [SecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule] resources under the given organization, folder, or project and all of its descendants.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDescendantSecurityHealthAnalyticsCustomModulesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListDescendantSecurityHealthAnalyticsCustomModulesRequest)`  
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
`[ListDescendantSecurityHealthAnalyticsCustomModulesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListDescendantSecurityHealthAnalyticsCustomModulesResponse)` | The response received from the server.  
  
### ListDescendantSecurityHealthAnalyticsCustomModulesAsync(ListDescendantSecurityHealthAnalyticsCustomModulesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListDescendantSecurityHealthAnalyticsCustomModulesResponse> ListDescendantSecurityHealthAnalyticsCustomModulesAsync(ListDescendantSecurityHealthAnalyticsCustomModulesRequest request, CallOptions options)

Returns a list of all resident [SecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule] resources under the given organization, folder, or project and all of its descendants.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDescendantSecurityHealthAnalyticsCustomModulesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListDescendantSecurityHealthAnalyticsCustomModulesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListDescendantSecurityHealthAnalyticsCustomModulesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListDescendantSecurityHealthAnalyticsCustomModulesResponse)` | The call object.  
  
### ListDescendantSecurityHealthAnalyticsCustomModulesAsync(ListDescendantSecurityHealthAnalyticsCustomModulesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListDescendantSecurityHealthAnalyticsCustomModulesResponse> ListDescendantSecurityHealthAnalyticsCustomModulesAsync(ListDescendantSecurityHealthAnalyticsCustomModulesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns a list of all resident [SecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule] resources under the given organization, folder, or project and all of its descendants.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDescendantSecurityHealthAnalyticsCustomModulesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListDescendantSecurityHealthAnalyticsCustomModulesRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListDescendantSecurityHealthAnalyticsCustomModulesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListDescendantSecurityHealthAnalyticsCustomModulesResponse)` | The call object.  
  
### ListEffectiveEventThreatDetectionCustomModules(ListEffectiveEventThreatDetectionCustomModulesRequest, CallOptions)
    
    
    public virtual ListEffectiveEventThreatDetectionCustomModulesResponse ListEffectiveEventThreatDetectionCustomModules(ListEffectiveEventThreatDetectionCustomModulesRequest request, CallOptions options)

Lists all effective Event Threat Detection custom modules for the given parent. This includes resident modules defined at the scope of the parent along with modules inherited from its ancestors.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListEffectiveEventThreatDetectionCustomModulesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListEffectiveEventThreatDetectionCustomModulesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListEffectiveEventThreatDetectionCustomModulesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListEffectiveEventThreatDetectionCustomModulesResponse)` | The response received from the server.  
  
### ListEffectiveEventThreatDetectionCustomModules(ListEffectiveEventThreatDetectionCustomModulesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListEffectiveEventThreatDetectionCustomModulesResponse ListEffectiveEventThreatDetectionCustomModules(ListEffectiveEventThreatDetectionCustomModulesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all effective Event Threat Detection custom modules for the given parent. This includes resident modules defined at the scope of the parent along with modules inherited from its ancestors.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListEffectiveEventThreatDetectionCustomModulesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListEffectiveEventThreatDetectionCustomModulesRequest)`  
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
`[ListEffectiveEventThreatDetectionCustomModulesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListEffectiveEventThreatDetectionCustomModulesResponse)` | The response received from the server.  
  
### ListEffectiveEventThreatDetectionCustomModulesAsync(ListEffectiveEventThreatDetectionCustomModulesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListEffectiveEventThreatDetectionCustomModulesResponse> ListEffectiveEventThreatDetectionCustomModulesAsync(ListEffectiveEventThreatDetectionCustomModulesRequest request, CallOptions options)

Lists all effective Event Threat Detection custom modules for the given parent. This includes resident modules defined at the scope of the parent along with modules inherited from its ancestors.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListEffectiveEventThreatDetectionCustomModulesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListEffectiveEventThreatDetectionCustomModulesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListEffectiveEventThreatDetectionCustomModulesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListEffectiveEventThreatDetectionCustomModulesResponse)` | The call object.  
  
### ListEffectiveEventThreatDetectionCustomModulesAsync(ListEffectiveEventThreatDetectionCustomModulesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListEffectiveEventThreatDetectionCustomModulesResponse> ListEffectiveEventThreatDetectionCustomModulesAsync(ListEffectiveEventThreatDetectionCustomModulesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all effective Event Threat Detection custom modules for the given parent. This includes resident modules defined at the scope of the parent along with modules inherited from its ancestors.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListEffectiveEventThreatDetectionCustomModulesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListEffectiveEventThreatDetectionCustomModulesRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListEffectiveEventThreatDetectionCustomModulesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListEffectiveEventThreatDetectionCustomModulesResponse)` | The call object.  
  
### ListEffectiveSecurityHealthAnalyticsCustomModules(ListEffectiveSecurityHealthAnalyticsCustomModulesRequest, CallOptions)
    
    
    public virtual ListEffectiveSecurityHealthAnalyticsCustomModulesResponse ListEffectiveSecurityHealthAnalyticsCustomModules(ListEffectiveSecurityHealthAnalyticsCustomModulesRequest request, CallOptions options)

Returns a list of all [EffectiveSecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.EffectiveSecurityHealthAnalyticsCustomModule] resources for the given parent. This includes resident modules defined at the scope of the parent, and inherited modules, inherited from ancestor organizations, folders, and projects (no descendants).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListEffectiveSecurityHealthAnalyticsCustomModulesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListEffectiveSecurityHealthAnalyticsCustomModulesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListEffectiveSecurityHealthAnalyticsCustomModulesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListEffectiveSecurityHealthAnalyticsCustomModulesResponse)` | The response received from the server.  
  
### ListEffectiveSecurityHealthAnalyticsCustomModules(ListEffectiveSecurityHealthAnalyticsCustomModulesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListEffectiveSecurityHealthAnalyticsCustomModulesResponse ListEffectiveSecurityHealthAnalyticsCustomModules(ListEffectiveSecurityHealthAnalyticsCustomModulesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns a list of all [EffectiveSecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.EffectiveSecurityHealthAnalyticsCustomModule] resources for the given parent. This includes resident modules defined at the scope of the parent, and inherited modules, inherited from ancestor organizations, folders, and projects (no descendants).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListEffectiveSecurityHealthAnalyticsCustomModulesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListEffectiveSecurityHealthAnalyticsCustomModulesRequest)`  
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
`[ListEffectiveSecurityHealthAnalyticsCustomModulesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListEffectiveSecurityHealthAnalyticsCustomModulesResponse)` | The response received from the server.  
  
### ListEffectiveSecurityHealthAnalyticsCustomModulesAsync(ListEffectiveSecurityHealthAnalyticsCustomModulesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListEffectiveSecurityHealthAnalyticsCustomModulesResponse> ListEffectiveSecurityHealthAnalyticsCustomModulesAsync(ListEffectiveSecurityHealthAnalyticsCustomModulesRequest request, CallOptions options)

Returns a list of all [EffectiveSecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.EffectiveSecurityHealthAnalyticsCustomModule] resources for the given parent. This includes resident modules defined at the scope of the parent, and inherited modules, inherited from ancestor organizations, folders, and projects (no descendants).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListEffectiveSecurityHealthAnalyticsCustomModulesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListEffectiveSecurityHealthAnalyticsCustomModulesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListEffectiveSecurityHealthAnalyticsCustomModulesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListEffectiveSecurityHealthAnalyticsCustomModulesResponse)` | The call object.  
  
### ListEffectiveSecurityHealthAnalyticsCustomModulesAsync(ListEffectiveSecurityHealthAnalyticsCustomModulesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListEffectiveSecurityHealthAnalyticsCustomModulesResponse> ListEffectiveSecurityHealthAnalyticsCustomModulesAsync(ListEffectiveSecurityHealthAnalyticsCustomModulesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns a list of all [EffectiveSecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.EffectiveSecurityHealthAnalyticsCustomModule] resources for the given parent. This includes resident modules defined at the scope of the parent, and inherited modules, inherited from ancestor organizations, folders, and projects (no descendants).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListEffectiveSecurityHealthAnalyticsCustomModulesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListEffectiveSecurityHealthAnalyticsCustomModulesRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListEffectiveSecurityHealthAnalyticsCustomModulesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListEffectiveSecurityHealthAnalyticsCustomModulesResponse)` | The call object.  
  
### ListEventThreatDetectionCustomModules(ListEventThreatDetectionCustomModulesRequest, CallOptions)
    
    
    public virtual ListEventThreatDetectionCustomModulesResponse ListEventThreatDetectionCustomModules(ListEventThreatDetectionCustomModulesRequest request, CallOptions options)

Lists all Event Threat Detection custom modules for the given organization, folder, or project. This includes resident modules defined at the scope of the parent along with modules inherited from ancestors.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListEventThreatDetectionCustomModulesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListEventThreatDetectionCustomModulesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListEventThreatDetectionCustomModulesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListEventThreatDetectionCustomModulesResponse)` | The response received from the server.  
  
### ListEventThreatDetectionCustomModules(ListEventThreatDetectionCustomModulesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListEventThreatDetectionCustomModulesResponse ListEventThreatDetectionCustomModules(ListEventThreatDetectionCustomModulesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all Event Threat Detection custom modules for the given organization, folder, or project. This includes resident modules defined at the scope of the parent along with modules inherited from ancestors.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListEventThreatDetectionCustomModulesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListEventThreatDetectionCustomModulesRequest)`  
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
`[ListEventThreatDetectionCustomModulesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListEventThreatDetectionCustomModulesResponse)` | The response received from the server.  
  
### ListEventThreatDetectionCustomModulesAsync(ListEventThreatDetectionCustomModulesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListEventThreatDetectionCustomModulesResponse> ListEventThreatDetectionCustomModulesAsync(ListEventThreatDetectionCustomModulesRequest request, CallOptions options)

Lists all Event Threat Detection custom modules for the given organization, folder, or project. This includes resident modules defined at the scope of the parent along with modules inherited from ancestors.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListEventThreatDetectionCustomModulesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListEventThreatDetectionCustomModulesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListEventThreatDetectionCustomModulesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListEventThreatDetectionCustomModulesResponse)` | The call object.  
  
### ListEventThreatDetectionCustomModulesAsync(ListEventThreatDetectionCustomModulesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListEventThreatDetectionCustomModulesResponse> ListEventThreatDetectionCustomModulesAsync(ListEventThreatDetectionCustomModulesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all Event Threat Detection custom modules for the given organization, folder, or project. This includes resident modules defined at the scope of the parent along with modules inherited from ancestors.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListEventThreatDetectionCustomModulesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListEventThreatDetectionCustomModulesRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListEventThreatDetectionCustomModulesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListEventThreatDetectionCustomModulesResponse)` | The call object.  
  
### ListSecurityCenterServices(ListSecurityCenterServicesRequest, CallOptions)
    
    
    public virtual ListSecurityCenterServicesResponse ListSecurityCenterServices(ListSecurityCenterServicesRequest request, CallOptions options)

Returns a list of all Security Command Center services for the given parent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSecurityCenterServicesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListSecurityCenterServicesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListSecurityCenterServicesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListSecurityCenterServicesResponse)` | The response received from the server.  
  
### ListSecurityCenterServices(ListSecurityCenterServicesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListSecurityCenterServicesResponse ListSecurityCenterServices(ListSecurityCenterServicesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns a list of all Security Command Center services for the given parent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSecurityCenterServicesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListSecurityCenterServicesRequest)`  
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
`[ListSecurityCenterServicesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListSecurityCenterServicesResponse)` | The response received from the server.  
  
### ListSecurityCenterServicesAsync(ListSecurityCenterServicesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListSecurityCenterServicesResponse> ListSecurityCenterServicesAsync(ListSecurityCenterServicesRequest request, CallOptions options)

Returns a list of all Security Command Center services for the given parent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSecurityCenterServicesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListSecurityCenterServicesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListSecurityCenterServicesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListSecurityCenterServicesResponse)` | The call object.  
  
### ListSecurityCenterServicesAsync(ListSecurityCenterServicesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListSecurityCenterServicesResponse> ListSecurityCenterServicesAsync(ListSecurityCenterServicesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns a list of all Security Command Center services for the given parent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSecurityCenterServicesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListSecurityCenterServicesRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListSecurityCenterServicesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListSecurityCenterServicesResponse)` | The call object.  
  
### ListSecurityHealthAnalyticsCustomModules(ListSecurityHealthAnalyticsCustomModulesRequest, CallOptions)
    
    
    public virtual ListSecurityHealthAnalyticsCustomModulesResponse ListSecurityHealthAnalyticsCustomModules(ListSecurityHealthAnalyticsCustomModulesRequest request, CallOptions options)

Returns a list of all [SecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule] resources for the given parent. This includes resident modules defined at the scope of the parent, and inherited modules, inherited from ancestor organizations, folders, and projects (no descendants).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSecurityHealthAnalyticsCustomModulesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListSecurityHealthAnalyticsCustomModulesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListSecurityHealthAnalyticsCustomModulesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListSecurityHealthAnalyticsCustomModulesResponse)` | The response received from the server.  
  
### ListSecurityHealthAnalyticsCustomModules(ListSecurityHealthAnalyticsCustomModulesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListSecurityHealthAnalyticsCustomModulesResponse ListSecurityHealthAnalyticsCustomModules(ListSecurityHealthAnalyticsCustomModulesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns a list of all [SecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule] resources for the given parent. This includes resident modules defined at the scope of the parent, and inherited modules, inherited from ancestor organizations, folders, and projects (no descendants).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSecurityHealthAnalyticsCustomModulesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListSecurityHealthAnalyticsCustomModulesRequest)`  
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
`[ListSecurityHealthAnalyticsCustomModulesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListSecurityHealthAnalyticsCustomModulesResponse)` | The response received from the server.  
  
### ListSecurityHealthAnalyticsCustomModulesAsync(ListSecurityHealthAnalyticsCustomModulesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListSecurityHealthAnalyticsCustomModulesResponse> ListSecurityHealthAnalyticsCustomModulesAsync(ListSecurityHealthAnalyticsCustomModulesRequest request, CallOptions options)

Returns a list of all [SecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule] resources for the given parent. This includes resident modules defined at the scope of the parent, and inherited modules, inherited from ancestor organizations, folders, and projects (no descendants).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSecurityHealthAnalyticsCustomModulesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListSecurityHealthAnalyticsCustomModulesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListSecurityHealthAnalyticsCustomModulesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListSecurityHealthAnalyticsCustomModulesResponse)` | The call object.  
  
### ListSecurityHealthAnalyticsCustomModulesAsync(ListSecurityHealthAnalyticsCustomModulesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListSecurityHealthAnalyticsCustomModulesResponse> ListSecurityHealthAnalyticsCustomModulesAsync(ListSecurityHealthAnalyticsCustomModulesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns a list of all [SecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule] resources for the given parent. This includes resident modules defined at the scope of the parent, and inherited modules, inherited from ancestor organizations, folders, and projects (no descendants).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSecurityHealthAnalyticsCustomModulesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListSecurityHealthAnalyticsCustomModulesRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListSecurityHealthAnalyticsCustomModulesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ListSecurityHealthAnalyticsCustomModulesResponse)` | The call object.  
  
### NewInstance(ClientBaseConfiguration)
    
    
    protected override SecurityCenterManagement.SecurityCenterManagementClient NewInstance(ClientBase.ClientBaseConfiguration configuration)

Creates a new instance of client from given `ClientBaseConfiguration`.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterManagement](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SecurityCenterManagement)[SecurityCenterManagementClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SecurityCenterManagement.SecurityCenterManagementClient)` |   
**Overrides**

Grpc.Core.ClientBase<Google.Cloud.SecurityCenterManagement.V1.SecurityCenterManagement.SecurityCenterManagementClient>.NewInstance(Grpc.Core.ClientBase.ClientBaseConfiguration)

### SimulateSecurityHealthAnalyticsCustomModule(SimulateSecurityHealthAnalyticsCustomModuleRequest, CallOptions)
    
    
    public virtual SimulateSecurityHealthAnalyticsCustomModuleResponse SimulateSecurityHealthAnalyticsCustomModule(SimulateSecurityHealthAnalyticsCustomModuleRequest request, CallOptions options)

Simulates the result of using a [SecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule] to check a resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SimulateSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SimulateSecurityHealthAnalyticsCustomModuleRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[SimulateSecurityHealthAnalyticsCustomModuleResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SimulateSecurityHealthAnalyticsCustomModuleResponse)` | The response received from the server.  
  
### SimulateSecurityHealthAnalyticsCustomModule(SimulateSecurityHealthAnalyticsCustomModuleRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual SimulateSecurityHealthAnalyticsCustomModuleResponse SimulateSecurityHealthAnalyticsCustomModule(SimulateSecurityHealthAnalyticsCustomModuleRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Simulates the result of using a [SecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule] to check a resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SimulateSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SimulateSecurityHealthAnalyticsCustomModuleRequest)`  
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
`[SimulateSecurityHealthAnalyticsCustomModuleResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SimulateSecurityHealthAnalyticsCustomModuleResponse)` | The response received from the server.  
  
### SimulateSecurityHealthAnalyticsCustomModuleAsync(SimulateSecurityHealthAnalyticsCustomModuleRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<SimulateSecurityHealthAnalyticsCustomModuleResponse> SimulateSecurityHealthAnalyticsCustomModuleAsync(SimulateSecurityHealthAnalyticsCustomModuleRequest request, CallOptions options)

Simulates the result of using a [SecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule] to check a resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SimulateSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SimulateSecurityHealthAnalyticsCustomModuleRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[SimulateSecurityHealthAnalyticsCustomModuleResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SimulateSecurityHealthAnalyticsCustomModuleResponse)` | The call object.  
  
### SimulateSecurityHealthAnalyticsCustomModuleAsync(SimulateSecurityHealthAnalyticsCustomModuleRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<SimulateSecurityHealthAnalyticsCustomModuleResponse> SimulateSecurityHealthAnalyticsCustomModuleAsync(SimulateSecurityHealthAnalyticsCustomModuleRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Simulates the result of using a [SecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule] to check a resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SimulateSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SimulateSecurityHealthAnalyticsCustomModuleRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[SimulateSecurityHealthAnalyticsCustomModuleResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SimulateSecurityHealthAnalyticsCustomModuleResponse)` | The call object.  
  
### UpdateEventThreatDetectionCustomModule(UpdateEventThreatDetectionCustomModuleRequest, CallOptions)
    
    
    public virtual EventThreatDetectionCustomModule UpdateEventThreatDetectionCustomModule(UpdateEventThreatDetectionCustomModuleRequest request, CallOptions options)

Updates the Event Threat Detection custom module with the given name based on the given update mask. Updating the enablement state is supported for both resident and inherited modules (though resident modules cannot have an enablement state of "inherited"). Updating the display name or configuration of a module is supported for resident modules only. The type of a module cannot be changed.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.UpdateEventThreatDetectionCustomModuleRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[EventThreatDetectionCustomModule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.EventThreatDetectionCustomModule)` | The response received from the server.  
  
### UpdateEventThreatDetectionCustomModule(UpdateEventThreatDetectionCustomModuleRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual EventThreatDetectionCustomModule UpdateEventThreatDetectionCustomModule(UpdateEventThreatDetectionCustomModuleRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the Event Threat Detection custom module with the given name based on the given update mask. Updating the enablement state is supported for both resident and inherited modules (though resident modules cannot have an enablement state of "inherited"). Updating the display name or configuration of a module is supported for resident modules only. The type of a module cannot be changed.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.UpdateEventThreatDetectionCustomModuleRequest)`  
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
`[EventThreatDetectionCustomModule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.EventThreatDetectionCustomModule)` | The response received from the server.  
  
### UpdateEventThreatDetectionCustomModuleAsync(UpdateEventThreatDetectionCustomModuleRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<EventThreatDetectionCustomModule> UpdateEventThreatDetectionCustomModuleAsync(UpdateEventThreatDetectionCustomModuleRequest request, CallOptions options)

Updates the Event Threat Detection custom module with the given name based on the given update mask. Updating the enablement state is supported for both resident and inherited modules (though resident modules cannot have an enablement state of "inherited"). Updating the display name or configuration of a module is supported for resident modules only. The type of a module cannot be changed.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.UpdateEventThreatDetectionCustomModuleRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[EventThreatDetectionCustomModule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.EventThreatDetectionCustomModule)` | The call object.  
  
### UpdateEventThreatDetectionCustomModuleAsync(UpdateEventThreatDetectionCustomModuleRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<EventThreatDetectionCustomModule> UpdateEventThreatDetectionCustomModuleAsync(UpdateEventThreatDetectionCustomModuleRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the Event Threat Detection custom module with the given name based on the given update mask. Updating the enablement state is supported for both resident and inherited modules (though resident modules cannot have an enablement state of "inherited"). Updating the display name or configuration of a module is supported for resident modules only. The type of a module cannot be changed.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.UpdateEventThreatDetectionCustomModuleRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[EventThreatDetectionCustomModule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.EventThreatDetectionCustomModule)` | The call object.  
  
### UpdateSecurityCenterService(UpdateSecurityCenterServiceRequest, CallOptions)
    
    
    public virtual SecurityCenterService UpdateSecurityCenterService(UpdateSecurityCenterServiceRequest request, CallOptions options)

Updates a Security Command Center service using the given update mask.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSecurityCenterServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.UpdateSecurityCenterServiceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SecurityCenterService)` | The response received from the server.  
  
### UpdateSecurityCenterService(UpdateSecurityCenterServiceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual SecurityCenterService UpdateSecurityCenterService(UpdateSecurityCenterServiceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates a Security Command Center service using the given update mask.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSecurityCenterServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.UpdateSecurityCenterServiceRequest)`  
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
`[SecurityCenterService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SecurityCenterService)` | The response received from the server.  
  
### UpdateSecurityCenterServiceAsync(UpdateSecurityCenterServiceRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<SecurityCenterService> UpdateSecurityCenterServiceAsync(UpdateSecurityCenterServiceRequest request, CallOptions options)

Updates a Security Command Center service using the given update mask.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSecurityCenterServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.UpdateSecurityCenterServiceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[SecurityCenterService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SecurityCenterService)` | The call object.  
  
### UpdateSecurityCenterServiceAsync(UpdateSecurityCenterServiceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<SecurityCenterService> UpdateSecurityCenterServiceAsync(UpdateSecurityCenterServiceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates a Security Command Center service using the given update mask.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSecurityCenterServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.UpdateSecurityCenterServiceRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[SecurityCenterService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SecurityCenterService)` | The call object.  
  
### UpdateSecurityHealthAnalyticsCustomModule(UpdateSecurityHealthAnalyticsCustomModuleRequest, CallOptions)
    
    
    public virtual SecurityHealthAnalyticsCustomModule UpdateSecurityHealthAnalyticsCustomModule(UpdateSecurityHealthAnalyticsCustomModuleRequest request, CallOptions options)

Updates the [SecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule] under the given name based on the given update mask. Updating the enablement state is supported on both resident and inherited modules (though resident modules cannot have an enablement state of "inherited"). Updating the display name and custom configuration of a module is supported on resident modules only.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.UpdateSecurityHealthAnalyticsCustomModuleRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SecurityHealthAnalyticsCustomModule)` | The response received from the server.  
  
### UpdateSecurityHealthAnalyticsCustomModule(UpdateSecurityHealthAnalyticsCustomModuleRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual SecurityHealthAnalyticsCustomModule UpdateSecurityHealthAnalyticsCustomModule(UpdateSecurityHealthAnalyticsCustomModuleRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the [SecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule] under the given name based on the given update mask. Updating the enablement state is supported on both resident and inherited modules (though resident modules cannot have an enablement state of "inherited"). Updating the display name and custom configuration of a module is supported on resident modules only.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.UpdateSecurityHealthAnalyticsCustomModuleRequest)`  
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
`[SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SecurityHealthAnalyticsCustomModule)` | The response received from the server.  
  
### UpdateSecurityHealthAnalyticsCustomModuleAsync(UpdateSecurityHealthAnalyticsCustomModuleRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<SecurityHealthAnalyticsCustomModule> UpdateSecurityHealthAnalyticsCustomModuleAsync(UpdateSecurityHealthAnalyticsCustomModuleRequest request, CallOptions options)

Updates the [SecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule] under the given name based on the given update mask. Updating the enablement state is supported on both resident and inherited modules (though resident modules cannot have an enablement state of "inherited"). Updating the display name and custom configuration of a module is supported on resident modules only.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.UpdateSecurityHealthAnalyticsCustomModuleRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SecurityHealthAnalyticsCustomModule)` | The call object.  
  
### UpdateSecurityHealthAnalyticsCustomModuleAsync(UpdateSecurityHealthAnalyticsCustomModuleRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<SecurityHealthAnalyticsCustomModule> UpdateSecurityHealthAnalyticsCustomModuleAsync(UpdateSecurityHealthAnalyticsCustomModuleRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the [SecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule] under the given name based on the given update mask. Updating the enablement state is supported on both resident and inherited modules (though resident modules cannot have an enablement state of "inherited"). Updating the display name and custom configuration of a module is supported on resident modules only.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.UpdateSecurityHealthAnalyticsCustomModuleRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.SecurityHealthAnalyticsCustomModule)` | The call object.  
  
### ValidateEventThreatDetectionCustomModule(ValidateEventThreatDetectionCustomModuleRequest, CallOptions)
    
    
    public virtual ValidateEventThreatDetectionCustomModuleResponse ValidateEventThreatDetectionCustomModule(ValidateEventThreatDetectionCustomModuleRequest request, CallOptions options)

Validates the given Event Threat Detection custom module.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ValidateEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ValidateEventThreatDetectionCustomModuleRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ValidateEventThreatDetectionCustomModuleResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ValidateEventThreatDetectionCustomModuleResponse)` | The response received from the server.  
  
### ValidateEventThreatDetectionCustomModule(ValidateEventThreatDetectionCustomModuleRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ValidateEventThreatDetectionCustomModuleResponse ValidateEventThreatDetectionCustomModule(ValidateEventThreatDetectionCustomModuleRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Validates the given Event Threat Detection custom module.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ValidateEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ValidateEventThreatDetectionCustomModuleRequest)`  
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
`[ValidateEventThreatDetectionCustomModuleResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ValidateEventThreatDetectionCustomModuleResponse)` | The response received from the server.  
  
### ValidateEventThreatDetectionCustomModuleAsync(ValidateEventThreatDetectionCustomModuleRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ValidateEventThreatDetectionCustomModuleResponse> ValidateEventThreatDetectionCustomModuleAsync(ValidateEventThreatDetectionCustomModuleRequest request, CallOptions options)

Validates the given Event Threat Detection custom module.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ValidateEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ValidateEventThreatDetectionCustomModuleRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ValidateEventThreatDetectionCustomModuleResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ValidateEventThreatDetectionCustomModuleResponse)` | The call object.  
  
### ValidateEventThreatDetectionCustomModuleAsync(ValidateEventThreatDetectionCustomModuleRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ValidateEventThreatDetectionCustomModuleResponse> ValidateEventThreatDetectionCustomModuleAsync(ValidateEventThreatDetectionCustomModuleRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Validates the given Event Threat Detection custom module.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ValidateEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ValidateEventThreatDetectionCustomModuleRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ValidateEventThreatDetectionCustomModuleResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenterManagement.V1/latest/Google.Cloud.SecurityCenterManagement.V1.ValidateEventThreatDetectionCustomModuleResponse)` | The call object.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
