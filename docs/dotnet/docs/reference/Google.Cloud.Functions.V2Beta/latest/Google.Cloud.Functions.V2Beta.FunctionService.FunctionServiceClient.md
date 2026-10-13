---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.FunctionService.FunctionServiceClient
title: Cloud Functions v2beta API - Class FunctionService.FunctionServiceClient (1.0.0-beta08) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:17:24.451198+00:00
---

# Cloud Functions v2beta API - Class FunctionService.FunctionServiceClient (1.0.0-beta08)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.FunctionService.FunctionServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Functions v2beta API - Class FunctionService.FunctionServiceClient (1.0.0-beta08) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.0.0-beta08 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.FunctionService.FunctionServiceClient)
  * [ 1.0.0-beta07 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/1.0.0-beta07/Google.Cloud.Functions.V2Beta.FunctionService.FunctionServiceClient)


    
    
    public class FunctionService.FunctionServiceClient : ClientBase<FunctionService.FunctionServiceClient>

Reference documentation and code samples for the Cloud Functions v2beta API class FunctionService.FunctionServiceClient.

Client for FunctionService

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html)[FunctionService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.FunctionService)[FunctionServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.FunctionService.FunctionServiceClient) > FunctionService.FunctionServiceClient

## Inherited Members

[ClientBase<FunctionService.FunctionServiceClient>.WithHost(string)](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html#Grpc_Core_ClientBase_1_WithHost_System_String_)

[ClientBase.CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html#Grpc_Core_ClientBase_CallInvoker)

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Functions.V2Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta)

## Assembly

Google.Cloud.Functions.V2Beta.dll

## Constructors 

### FunctionServiceClient()
    
    
    protected FunctionServiceClient()

Protected parameterless constructor to allow creation of test doubles.

### FunctionServiceClient(CallInvoker)
    
    
    public FunctionServiceClient(CallInvoker callInvoker)

Creates a new client for FunctionService that uses a custom `CallInvoker`.

**Parameter**  
---  
**Name** | **Description**  
`callInvoker` | `[CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallInvoker.html)`  
The callInvoker to use to make remote calls.  
  
### FunctionServiceClient(ChannelBase)
    
    
    public FunctionServiceClient(ChannelBase channel)

Creates a new client for FunctionService

**Parameter**  
---  
**Name** | **Description**  
`channel` | `[ChannelBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ChannelBase.html)`  
The channel to use to make remote calls.  
  
### FunctionServiceClient(ClientBaseConfiguration)
    
    
    protected FunctionServiceClient(ClientBase.ClientBaseConfiguration configuration)

Protected constructor to allow creation of configured clients.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
The client configuration.  
  
## Methods 

### CreateFunction(CreateFunctionRequest, CallOptions)
    
    
    public virtual Operation CreateFunction(CreateFunctionRequest request, CallOptions options)

Creates a new function. If a function with the given name already exists in the specified project, the long running operation will return `ALREADY_EXISTS` error.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFunctionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.CreateFunctionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateFunction(CreateFunctionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation CreateFunction(CreateFunctionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new function. If a function with the given name already exists in the specified project, the long running operation will return `ALREADY_EXISTS` error.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFunctionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.CreateFunctionRequest)`  
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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateFunctionAsync(CreateFunctionRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> CreateFunctionAsync(CreateFunctionRequest request, CallOptions options)

Creates a new function. If a function with the given name already exists in the specified project, the long running operation will return `ALREADY_EXISTS` error.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFunctionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.CreateFunctionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateFunctionAsync(CreateFunctionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> CreateFunctionAsync(CreateFunctionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new function. If a function with the given name already exists in the specified project, the long running operation will return `ALREADY_EXISTS` error.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFunctionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.CreateFunctionRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateIAMPolicyClient()
    
    
    public virtual IAMPolicy.IAMPolicyClient CreateIAMPolicyClient()

Creates a new instance of [IAMPolicy.IAMPolicyClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.IAMPolicy.IAMPolicyClient.html) using the same call invoker as this client.

**Returns**  
---  
**Type** | **Description**  
`[IAMPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.IAMPolicy.html)[IAMPolicyClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.IAMPolicy.IAMPolicyClient.html)` | A new [IAMPolicy.IAMPolicyClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.IAMPolicy.IAMPolicyClient.html) for the same target as this client.  
  
### CreateLocationsClient()
    
    
    public virtual Locations.LocationsClient CreateLocationsClient()

Creates a new instance of [Locations.LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.Locations.LocationsClient.html) using the same call invoker as this client.

**Returns**  
---  
**Type** | **Description**  
`[Locations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.Locations.html)[LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.Locations.LocationsClient.html)` | A new [Locations.LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.Locations.LocationsClient.html) for the same target as this client.  
  
### CreateOperationsClient()
    
    
    public virtual Operations.OperationsClient CreateOperationsClient()

Creates a new instance of [Operations.OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operations.OperationsClient.html) using the same call invoker as this client.

**Returns**  
---  
**Type** | **Description**  
`[Operations](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operations.html)[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operations.OperationsClient.html)` | A new Operations client for the same target as this client.  
  
### DeleteFunction(DeleteFunctionRequest, CallOptions)
    
    
    public virtual Operation DeleteFunction(DeleteFunctionRequest request, CallOptions options)

Deletes a function with the given name from the specified project. If the given function is used by some trigger, the trigger will be updated to remove this function.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFunctionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.DeleteFunctionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteFunction(DeleteFunctionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeleteFunction(DeleteFunctionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a function with the given name from the specified project. If the given function is used by some trigger, the trigger will be updated to remove this function.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFunctionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.DeleteFunctionRequest)`  
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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteFunctionAsync(DeleteFunctionRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteFunctionAsync(DeleteFunctionRequest request, CallOptions options)

Deletes a function with the given name from the specified project. If the given function is used by some trigger, the trigger will be updated to remove this function.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFunctionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.DeleteFunctionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteFunctionAsync(DeleteFunctionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteFunctionAsync(DeleteFunctionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a function with the given name from the specified project. If the given function is used by some trigger, the trigger will be updated to remove this function.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFunctionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.DeleteFunctionRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### GenerateDownloadUrl(GenerateDownloadUrlRequest, CallOptions)
    
    
    public virtual GenerateDownloadUrlResponse GenerateDownloadUrl(GenerateDownloadUrlRequest request, CallOptions options)

Returns a signed URL for downloading deployed function source code. The URL is only valid for a limited period and should be used within 30 minutes of generation. For more information about the signed URL usage see: <https://cloud.google.com/storage/docs/access-control/signed-urls>

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateDownloadUrlRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.GenerateDownloadUrlRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[GenerateDownloadUrlResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.GenerateDownloadUrlResponse)` | The response received from the server.  
  
### GenerateDownloadUrl(GenerateDownloadUrlRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual GenerateDownloadUrlResponse GenerateDownloadUrl(GenerateDownloadUrlRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns a signed URL for downloading deployed function source code. The URL is only valid for a limited period and should be used within 30 minutes of generation. For more information about the signed URL usage see: <https://cloud.google.com/storage/docs/access-control/signed-urls>

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateDownloadUrlRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.GenerateDownloadUrlRequest)`  
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
`[GenerateDownloadUrlResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.GenerateDownloadUrlResponse)` | The response received from the server.  
  
### GenerateDownloadUrlAsync(GenerateDownloadUrlRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<GenerateDownloadUrlResponse> GenerateDownloadUrlAsync(GenerateDownloadUrlRequest request, CallOptions options)

Returns a signed URL for downloading deployed function source code. The URL is only valid for a limited period and should be used within 30 minutes of generation. For more information about the signed URL usage see: <https://cloud.google.com/storage/docs/access-control/signed-urls>

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateDownloadUrlRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.GenerateDownloadUrlRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[GenerateDownloadUrlResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.GenerateDownloadUrlResponse)` | The call object.  
  
### GenerateDownloadUrlAsync(GenerateDownloadUrlRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<GenerateDownloadUrlResponse> GenerateDownloadUrlAsync(GenerateDownloadUrlRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns a signed URL for downloading deployed function source code. The URL is only valid for a limited period and should be used within 30 minutes of generation. For more information about the signed URL usage see: <https://cloud.google.com/storage/docs/access-control/signed-urls>

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateDownloadUrlRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.GenerateDownloadUrlRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[GenerateDownloadUrlResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.GenerateDownloadUrlResponse)` | The call object.  
  
### GenerateUploadUrl(GenerateUploadUrlRequest, CallOptions)
    
    
    public virtual GenerateUploadUrlResponse GenerateUploadUrl(GenerateUploadUrlRequest request, CallOptions options)

Returns a signed URL for uploading a function source code. For more information about the signed URL usage see: <https://cloud.google.com/storage/docs/access-control/signed-urls>. Once the function source code upload is complete, the used signed URL should be provided in CreateFunction or UpdateFunction request as a reference to the function source code.

When uploading source code to the generated signed URL, please follow these restrictions:

  * Source file type should be a zip file.
  * No credentials should be attached - the signed URLs provide access to the target bucket using internal service identity; if credentials were attached, the identity from the credentials would be used, but that identity does not have permissions to upload files to the URL.



When making a HTTP PUT request, specify this header:

  * `content-type: application/zip`



Do not specify this header:

  * `Authorization: Bearer YOUR_TOKEN`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateUploadUrlRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.GenerateUploadUrlRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[GenerateUploadUrlResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.GenerateUploadUrlResponse)` | The response received from the server.  
  
### GenerateUploadUrl(GenerateUploadUrlRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual GenerateUploadUrlResponse GenerateUploadUrl(GenerateUploadUrlRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns a signed URL for uploading a function source code. For more information about the signed URL usage see: <https://cloud.google.com/storage/docs/access-control/signed-urls>. Once the function source code upload is complete, the used signed URL should be provided in CreateFunction or UpdateFunction request as a reference to the function source code.

When uploading source code to the generated signed URL, please follow these restrictions:

  * Source file type should be a zip file.
  * No credentials should be attached - the signed URLs provide access to the target bucket using internal service identity; if credentials were attached, the identity from the credentials would be used, but that identity does not have permissions to upload files to the URL.



When making a HTTP PUT request, specify this header:

  * `content-type: application/zip`



Do not specify this header:

  * `Authorization: Bearer YOUR_TOKEN`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateUploadUrlRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.GenerateUploadUrlRequest)`  
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
`[GenerateUploadUrlResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.GenerateUploadUrlResponse)` | The response received from the server.  
  
### GenerateUploadUrlAsync(GenerateUploadUrlRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<GenerateUploadUrlResponse> GenerateUploadUrlAsync(GenerateUploadUrlRequest request, CallOptions options)

Returns a signed URL for uploading a function source code. For more information about the signed URL usage see: <https://cloud.google.com/storage/docs/access-control/signed-urls>. Once the function source code upload is complete, the used signed URL should be provided in CreateFunction or UpdateFunction request as a reference to the function source code.

When uploading source code to the generated signed URL, please follow these restrictions:

  * Source file type should be a zip file.
  * No credentials should be attached - the signed URLs provide access to the target bucket using internal service identity; if credentials were attached, the identity from the credentials would be used, but that identity does not have permissions to upload files to the URL.



When making a HTTP PUT request, specify this header:

  * `content-type: application/zip`



Do not specify this header:

  * `Authorization: Bearer YOUR_TOKEN`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateUploadUrlRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.GenerateUploadUrlRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[GenerateUploadUrlResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.GenerateUploadUrlResponse)` | The call object.  
  
### GenerateUploadUrlAsync(GenerateUploadUrlRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<GenerateUploadUrlResponse> GenerateUploadUrlAsync(GenerateUploadUrlRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns a signed URL for uploading a function source code. For more information about the signed URL usage see: <https://cloud.google.com/storage/docs/access-control/signed-urls>. Once the function source code upload is complete, the used signed URL should be provided in CreateFunction or UpdateFunction request as a reference to the function source code.

When uploading source code to the generated signed URL, please follow these restrictions:

  * Source file type should be a zip file.
  * No credentials should be attached - the signed URLs provide access to the target bucket using internal service identity; if credentials were attached, the identity from the credentials would be used, but that identity does not have permissions to upload files to the URL.



When making a HTTP PUT request, specify this header:

  * `content-type: application/zip`



Do not specify this header:

  * `Authorization: Bearer YOUR_TOKEN`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateUploadUrlRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.GenerateUploadUrlRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[GenerateUploadUrlResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.GenerateUploadUrlResponse)` | The call object.  
  
### GetFunction(GetFunctionRequest, CallOptions)
    
    
    public virtual Function GetFunction(GetFunctionRequest request, CallOptions options)

Returns a function with the given name from the requested project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFunctionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.GetFunctionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.Function)` | The response received from the server.  
  
### GetFunction(GetFunctionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Function GetFunction(GetFunctionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns a function with the given name from the requested project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFunctionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.GetFunctionRequest)`  
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
`[Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.Function)` | The response received from the server.  
  
### GetFunctionAsync(GetFunctionRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Function> GetFunctionAsync(GetFunctionRequest request, CallOptions options)

Returns a function with the given name from the requested project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFunctionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.GetFunctionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.Function)` | The call object.  
  
### GetFunctionAsync(GetFunctionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Function> GetFunctionAsync(GetFunctionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns a function with the given name from the requested project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFunctionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.GetFunctionRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Function](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.Function)` | The call object.  
  
### ListFunctions(ListFunctionsRequest, CallOptions)
    
    
    public virtual ListFunctionsResponse ListFunctions(ListFunctionsRequest request, CallOptions options)

Returns a list of functions that belong to the requested project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFunctionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ListFunctionsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListFunctionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ListFunctionsResponse)` | The response received from the server.  
  
### ListFunctions(ListFunctionsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListFunctionsResponse ListFunctions(ListFunctionsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns a list of functions that belong to the requested project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFunctionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ListFunctionsRequest)`  
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
`[ListFunctionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ListFunctionsResponse)` | The response received from the server.  
  
### ListFunctionsAsync(ListFunctionsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListFunctionsResponse> ListFunctionsAsync(ListFunctionsRequest request, CallOptions options)

Returns a list of functions that belong to the requested project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFunctionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ListFunctionsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListFunctionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ListFunctionsResponse)` | The call object.  
  
### ListFunctionsAsync(ListFunctionsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListFunctionsResponse> ListFunctionsAsync(ListFunctionsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns a list of functions that belong to the requested project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFunctionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ListFunctionsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListFunctionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ListFunctionsResponse)` | The call object.  
  
### ListRuntimes(ListRuntimesRequest, CallOptions)
    
    
    public virtual ListRuntimesResponse ListRuntimes(ListRuntimesRequest request, CallOptions options)

Returns a list of runtimes that are supported for the requested project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRuntimesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ListRuntimesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListRuntimesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ListRuntimesResponse)` | The response received from the server.  
  
### ListRuntimes(ListRuntimesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListRuntimesResponse ListRuntimes(ListRuntimesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns a list of runtimes that are supported for the requested project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRuntimesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ListRuntimesRequest)`  
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
`[ListRuntimesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ListRuntimesResponse)` | The response received from the server.  
  
### ListRuntimesAsync(ListRuntimesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListRuntimesResponse> ListRuntimesAsync(ListRuntimesRequest request, CallOptions options)

Returns a list of runtimes that are supported for the requested project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRuntimesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ListRuntimesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListRuntimesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ListRuntimesResponse)` | The call object.  
  
### ListRuntimesAsync(ListRuntimesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListRuntimesResponse> ListRuntimesAsync(ListRuntimesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns a list of runtimes that are supported for the requested project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRuntimesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ListRuntimesRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListRuntimesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ListRuntimesResponse)` | The call object.  
  
### NewInstance(ClientBaseConfiguration)
    
    
    protected override FunctionService.FunctionServiceClient NewInstance(ClientBase.ClientBaseConfiguration configuration)

Creates a new instance of client from given `ClientBaseConfiguration`.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FunctionService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.FunctionService)[FunctionServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.FunctionService.FunctionServiceClient)` |   
**Overrides**

Grpc.Core.ClientBase<Google.Cloud.Functions.V2Beta.FunctionService.FunctionServiceClient>.NewInstance(Grpc.Core.ClientBase.ClientBaseConfiguration)

### UpdateFunction(UpdateFunctionRequest, CallOptions)
    
    
    public virtual Operation UpdateFunction(UpdateFunctionRequest request, CallOptions options)

Updates existing function.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFunctionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.UpdateFunctionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### UpdateFunction(UpdateFunctionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation UpdateFunction(UpdateFunctionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates existing function.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFunctionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.UpdateFunctionRequest)`  
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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### UpdateFunctionAsync(UpdateFunctionRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateFunctionAsync(UpdateFunctionRequest request, CallOptions options)

Updates existing function.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFunctionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.UpdateFunctionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### UpdateFunctionAsync(UpdateFunctionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateFunctionAsync(UpdateFunctionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates existing function.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFunctionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.UpdateFunctionRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
