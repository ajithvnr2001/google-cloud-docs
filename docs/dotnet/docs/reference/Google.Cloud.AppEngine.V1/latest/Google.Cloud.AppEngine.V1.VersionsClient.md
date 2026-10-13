---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.VersionsClient
title: App Engine v1 API - Class VersionsClient (2.5.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:20:08.602932+00:00
---

# App Engine v1 API - Class VersionsClient (2.5.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.VersionsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  App Engine v1 API - Class VersionsClient (2.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.5.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.VersionsClient)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/2.4.0/Google.Cloud.AppEngine.V1.VersionsClient)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/2.3.0/Google.Cloud.AppEngine.V1.VersionsClient)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/2.2.0/Google.Cloud.AppEngine.V1.VersionsClient)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/2.1.0/Google.Cloud.AppEngine.V1.VersionsClient)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/2.0.0/Google.Cloud.AppEngine.V1.VersionsClient)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/1.4.0/Google.Cloud.AppEngine.V1.VersionsClient)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/1.3.0/Google.Cloud.AppEngine.V1.VersionsClient)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/1.2.0/Google.Cloud.AppEngine.V1.VersionsClient)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/1.1.0/Google.Cloud.AppEngine.V1.VersionsClient)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/1.0.0/Google.Cloud.AppEngine.V1.VersionsClient)


    
    
    public abstract class VersionsClient

Reference documentation and code samples for the App Engine v1 API class VersionsClient.

Versions client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > VersionsClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[VersionsClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.VersionsClientImpl)

## Namespace

[Google.Cloud.AppEngine.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1)

## Assembly

Google.Cloud.AppEngine.V1.dll

## Remarks

Manages versions of a service.

## Properties 

### CreateVersionOperationsClient
    
    
    public virtual OperationsClient CreateVersionOperationsClient { get; }

The long-running operations client for `CreateVersion`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the Versions service, which is a host of "appengine.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default Versions scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default Versions scopes are: 

  * <https://www.googleapis.com/auth/appengine.admin>
  * <https://www.googleapis.com/auth/cloud-platform>
  * <https://www.googleapis.com/auth/cloud-platform.read-only>



### DeleteVersionOperationsClient
    
    
    public virtual OperationsClient DeleteVersionOperationsClient { get; }

The long-running operations client for `DeleteVersion`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### GrpcClient
    
    
    public virtual Versions.VersionsClient GrpcClient { get; }

The underlying gRPC Versions client

**Property Value**  
---  
**Type** | **Description**  
`[Versions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.Versions)[VersionsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.Versions.VersionsClient)` |   
  
### ServiceMetadata
    
    
    public static ServiceMetadata ServiceMetadata { get; }

The service metadata associated with this client type.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceMetadata](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceMetadata.html)` |   
  
### UpdateVersionOperationsClient
    
    
    public virtual OperationsClient UpdateVersionOperationsClient { get; }

The long-running operations client for `UpdateVersion`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
## Methods 

### Create()
    
    
    public static VersionsClient Create()

Synchronously creates a [VersionsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.VersionsClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [VersionsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.VersionsClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[VersionsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.VersionsClient)` | The created [VersionsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.VersionsClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<VersionsClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [VersionsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.VersionsClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [VersionsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.VersionsClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[VersionsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.VersionsClient)` | The task representing the created [VersionsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.VersionsClient).  
  
### CreateVersion(CreateVersionRequest, CallSettings)
    
    
    public virtual Operation<Version, CreateVersionMetadataV1> CreateVersion(CreateVersionRequest request, CallSettings callSettings = null)

Deploys code and resource files to a new version.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.CreateVersionRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Version](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.Version)[CreateVersionMetadataV1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.CreateVersionMetadataV1)` | The RPC response.  
**Example**
    
    
    // Create client
    gcav::VersionsClient versionsClient = gcav::VersionsClient.Create();
    // Initialize request argument(s)
    gcav::CreateVersionRequest request = new gcav::CreateVersionRequest
    {
        Parent = "",
        Version = new gcav::Version(),
    };
    // Make the request
    Operation<gcav::Version, gcav::CreateVersionMetadataV1> response = versionsClient.CreateVersion(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcav::Version, gcav::CreateVersionMetadataV1> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcav::Version result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcav::Version, gcav::CreateVersionMetadataV1> retrievedResponse = versionsClient.PollOnceCreateVersion(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcav::Version retrievedResult = retrievedResponse.Result;
    }
    

### CreateVersionAsync(CreateVersionRequest, CallSettings)
    
    
    public virtual Task<Operation<Version, CreateVersionMetadataV1>> CreateVersionAsync(CreateVersionRequest request, CallSettings callSettings = null)

Deploys code and resource files to a new version.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.CreateVersionRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Version](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.Version)[CreateVersionMetadataV1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.CreateVersionMetadataV1)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::VersionsClient versionsClient = await gcav::VersionsClient.CreateAsync();
    // Initialize request argument(s)
    gcav::CreateVersionRequest request = new gcav::CreateVersionRequest
    {
        Parent = "",
        Version = new gcav::Version(),
    };
    // Make the request
    Operation<gcav::Version, gcav::CreateVersionMetadataV1> response = await versionsClient.CreateVersionAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcav::Version, gcav::CreateVersionMetadataV1> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcav::Version result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcav::Version, gcav::CreateVersionMetadataV1> retrievedResponse = await versionsClient.PollOnceCreateVersionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcav::Version retrievedResult = retrievedResponse.Result;
    }
    

### CreateVersionAsync(CreateVersionRequest, CancellationToken)
    
    
    public virtual Task<Operation<Version, CreateVersionMetadataV1>> CreateVersionAsync(CreateVersionRequest request, CancellationToken cancellationToken)

Deploys code and resource files to a new version.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.CreateVersionRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Version](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.Version)[CreateVersionMetadataV1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.CreateVersionMetadataV1)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::VersionsClient versionsClient = await gcav::VersionsClient.CreateAsync();
    // Initialize request argument(s)
    gcav::CreateVersionRequest request = new gcav::CreateVersionRequest
    {
        Parent = "",
        Version = new gcav::Version(),
    };
    // Make the request
    Operation<gcav::Version, gcav::CreateVersionMetadataV1> response = await versionsClient.CreateVersionAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcav::Version, gcav::CreateVersionMetadataV1> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcav::Version result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcav::Version, gcav::CreateVersionMetadataV1> retrievedResponse = await versionsClient.PollOnceCreateVersionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcav::Version retrievedResult = retrievedResponse.Result;
    }
    

### DeleteVersion(DeleteVersionRequest, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadataV1> DeleteVersion(DeleteVersionRequest request, CallSettings callSettings = null)

Deletes an existing Version resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.DeleteVersionRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadataV1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.OperationMetadataV1)` | The RPC response.  
**Example**
    
    
    // Create client
    gcav::VersionsClient versionsClient = gcav::VersionsClient.Create();
    // Initialize request argument(s)
    gcav::DeleteVersionRequest request = new gcav::DeleteVersionRequest { Name = "", };
    // Make the request
    Operation<Empty, gcav::OperationMetadataV1> response = versionsClient.DeleteVersion(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcav::OperationMetadataV1> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcav::OperationMetadataV1> retrievedResponse = versionsClient.PollOnceDeleteVersion(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteVersionAsync(DeleteVersionRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadataV1>> DeleteVersionAsync(DeleteVersionRequest request, CallSettings callSettings = null)

Deletes an existing Version resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.DeleteVersionRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadataV1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.OperationMetadataV1)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::VersionsClient versionsClient = await gcav::VersionsClient.CreateAsync();
    // Initialize request argument(s)
    gcav::DeleteVersionRequest request = new gcav::DeleteVersionRequest { Name = "", };
    // Make the request
    Operation<Empty, gcav::OperationMetadataV1> response = await versionsClient.DeleteVersionAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcav::OperationMetadataV1> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcav::OperationMetadataV1> retrievedResponse = await versionsClient.PollOnceDeleteVersionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteVersionAsync(DeleteVersionRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadataV1>> DeleteVersionAsync(DeleteVersionRequest request, CancellationToken cancellationToken)

Deletes an existing Version resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.DeleteVersionRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadataV1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.OperationMetadataV1)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::VersionsClient versionsClient = await gcav::VersionsClient.CreateAsync();
    // Initialize request argument(s)
    gcav::DeleteVersionRequest request = new gcav::DeleteVersionRequest { Name = "", };
    // Make the request
    Operation<Empty, gcav::OperationMetadataV1> response = await versionsClient.DeleteVersionAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcav::OperationMetadataV1> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcav::OperationMetadataV1> retrievedResponse = await versionsClient.PollOnceDeleteVersionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### GetVersion(GetVersionRequest, CallSettings)
    
    
    public virtual Version GetVersion(GetVersionRequest request, CallSettings callSettings = null)

Gets the specified Version resource. By default, only a `BASIC_VIEW` will be returned. Specify the `FULL_VIEW` parameter to get the full resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.GetVersionRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Version](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.Version)` | The RPC response.  
**Example**
    
    
    // Create client
    gcav::VersionsClient versionsClient = gcav::VersionsClient.Create();
    // Initialize request argument(s)
    gcav::GetVersionRequest request = new gcav::GetVersionRequest
    {
        Name = "",
        View = gcav::VersionView.Basic,
    };
    // Make the request
    gcav::Version response = versionsClient.GetVersion(request);
    

### GetVersionAsync(GetVersionRequest, CallSettings)
    
    
    public virtual Task<Version> GetVersionAsync(GetVersionRequest request, CallSettings callSettings = null)

Gets the specified Version resource. By default, only a `BASIC_VIEW` will be returned. Specify the `FULL_VIEW` parameter to get the full resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.GetVersionRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Version](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.Version)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::VersionsClient versionsClient = await gcav::VersionsClient.CreateAsync();
    // Initialize request argument(s)
    gcav::GetVersionRequest request = new gcav::GetVersionRequest
    {
        Name = "",
        View = gcav::VersionView.Basic,
    };
    // Make the request
    gcav::Version response = await versionsClient.GetVersionAsync(request);
    

### GetVersionAsync(GetVersionRequest, CancellationToken)
    
    
    public virtual Task<Version> GetVersionAsync(GetVersionRequest request, CancellationToken cancellationToken)

Gets the specified Version resource. By default, only a `BASIC_VIEW` will be returned. Specify the `FULL_VIEW` parameter to get the full resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.GetVersionRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Version](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.Version)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::VersionsClient versionsClient = await gcav::VersionsClient.CreateAsync();
    // Initialize request argument(s)
    gcav::GetVersionRequest request = new gcav::GetVersionRequest
    {
        Name = "",
        View = gcav::VersionView.Basic,
    };
    // Make the request
    gcav::Version response = await versionsClient.GetVersionAsync(request);
    

### ListVersions(ListVersionsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListVersionsResponse, Version> ListVersions(ListVersionsRequest request, CallSettings callSettings = null)

Lists the versions of a service.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListVersionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.ListVersionsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.ListVersionsResponse)[Version](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.Version)` | A pageable sequence of [Version](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.Version) resources.  
**Example**
    
    
    // Create client
    gcav::VersionsClient versionsClient = gcav::VersionsClient.Create();
    // Initialize request argument(s)
    gcav::ListVersionsRequest request = new gcav::ListVersionsRequest
    {
        Parent = "",
        View = gcav::VersionView.Basic,
    };
    // Make the request
    PagedEnumerable<gcav::ListVersionsResponse, gcav::Version> response = versionsClient.ListVersions(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcav::Version item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcav::ListVersionsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcav::Version item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcav::Version> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcav::Version item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListVersionsAsync(ListVersionsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListVersionsResponse, Version> ListVersionsAsync(ListVersionsRequest request, CallSettings callSettings = null)

Lists the versions of a service.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListVersionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.ListVersionsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.ListVersionsResponse)[Version](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.Version)` | A pageable asynchronous sequence of [Version](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.Version) resources.  
**Example**
    
    
    // Create client
    gcav::VersionsClient versionsClient = await gcav::VersionsClient.CreateAsync();
    // Initialize request argument(s)
    gcav::ListVersionsRequest request = new gcav::ListVersionsRequest
    {
        Parent = "",
        View = gcav::VersionView.Basic,
    };
    // Make the request
    PagedAsyncEnumerable<gcav::ListVersionsResponse, gcav::Version> response = versionsClient.ListVersionsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((gcav::Version item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((gcav::ListVersionsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcav::Version item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcav::Version> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcav::Version item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### PollOnceCreateVersion(string, CallSettings)
    
    
    public virtual Operation<Version, CreateVersionMetadataV1> PollOnceCreateVersion(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateVersion`.

**Parameters**  
---  
**Name** | **Description**  
`operationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of a previously invoked operation. Must not be `null` or empty.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Version](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.Version)[CreateVersionMetadataV1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.CreateVersionMetadataV1)` | The result of polling the operation.  
  
### PollOnceCreateVersionAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Version, CreateVersionMetadataV1>> PollOnceCreateVersionAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateVersion`.

**Parameters**  
---  
**Name** | **Description**  
`operationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of a previously invoked operation. Must not be `null` or empty.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Version](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.Version)[CreateVersionMetadataV1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.CreateVersionMetadataV1)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteVersion(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadataV1> PollOnceDeleteVersion(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteVersion`.

**Parameters**  
---  
**Name** | **Description**  
`operationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of a previously invoked operation. Must not be `null` or empty.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadataV1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.OperationMetadataV1)` | The result of polling the operation.  
  
### PollOnceDeleteVersionAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadataV1>> PollOnceDeleteVersionAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteVersion`.

**Parameters**  
---  
**Name** | **Description**  
`operationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of a previously invoked operation. Must not be `null` or empty.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadataV1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.OperationMetadataV1)` | A task representing the result of polling the operation.  
  
### PollOnceUpdateVersion(string, CallSettings)
    
    
    public virtual Operation<Version, OperationMetadataV1> PollOnceUpdateVersion(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `UpdateVersion`.

**Parameters**  
---  
**Name** | **Description**  
`operationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of a previously invoked operation. Must not be `null` or empty.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Version](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.Version)[OperationMetadataV1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.OperationMetadataV1)` | The result of polling the operation.  
  
### PollOnceUpdateVersionAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Version, OperationMetadataV1>> PollOnceUpdateVersionAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `UpdateVersion`.

**Parameters**  
---  
**Name** | **Description**  
`operationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of a previously invoked operation. Must not be `null` or empty.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Version](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.Version)[OperationMetadataV1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.OperationMetadataV1)` | A task representing the result of polling the operation.  
  
### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.VersionsClient#Google_Cloud_AppEngine_V1_VersionsClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.VersionsClient#Google_Cloud_AppEngine_V1_VersionsClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.VersionsClient#Google_Cloud_AppEngine_V1_VersionsClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.VersionsClient#Google_Cloud_AppEngine_V1_VersionsClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### UpdateVersion(UpdateVersionRequest, CallSettings)
    
    
    public virtual Operation<Version, OperationMetadataV1> UpdateVersion(UpdateVersionRequest request, CallSettings callSettings = null)

Updates the specified Version resource. You can specify the following fields depending on the App Engine environment and type of scaling that the version resource uses:

**Standard environment**

  * [`instance_class`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.instance_class)



_automatic scaling_ in the standard environment:

  * [`automatic_scaling.min_idle_instances`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.automatic_scaling)
  * [`automatic_scaling.max_idle_instances`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.automatic_scaling)
  * [`automaticScaling.standard_scheduler_settings.max_instances`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#StandardSchedulerSettings)
  * [`automaticScaling.standard_scheduler_settings.min_instances`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#StandardSchedulerSettings)
  * [`automaticScaling.standard_scheduler_settings.target_cpu_utilization`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#StandardSchedulerSettings)
  * [`automaticScaling.standard_scheduler_settings.target_throughput_utilization`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#StandardSchedulerSettings)



_basic scaling_ or _manual scaling_ in the standard environment:

  * [`serving_status`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.serving_status)
  * [`manual_scaling.instances`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#manualscaling)



**Flexible environment**

  * [`serving_status`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.serving_status)



_automatic scaling_ in the flexible environment:

  * [`automatic_scaling.min_total_instances`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.automatic_scaling)
  * [`automatic_scaling.max_total_instances`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.automatic_scaling)
  * [`automatic_scaling.cool_down_period_sec`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.automatic_scaling)
  * [`automatic_scaling.cpu_utilization.target_utilization`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.automatic_scaling)



_manual scaling_ in the flexible environment:

  * [`manual_scaling.instances`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#manualscaling)



**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.UpdateVersionRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Version](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.Version)[OperationMetadataV1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.OperationMetadataV1)` | The RPC response.  
**Example**
    
    
    // Create client
    gcav::VersionsClient versionsClient = gcav::VersionsClient.Create();
    // Initialize request argument(s)
    gcav::UpdateVersionRequest request = new gcav::UpdateVersionRequest
    {
        Name = "",
        Version = new gcav::Version(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Operation<gcav::Version, gcav::OperationMetadataV1> response = versionsClient.UpdateVersion(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcav::Version, gcav::OperationMetadataV1> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcav::Version result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcav::Version, gcav::OperationMetadataV1> retrievedResponse = versionsClient.PollOnceUpdateVersion(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcav::Version retrievedResult = retrievedResponse.Result;
    }
    

### UpdateVersionAsync(UpdateVersionRequest, CallSettings)
    
    
    public virtual Task<Operation<Version, OperationMetadataV1>> UpdateVersionAsync(UpdateVersionRequest request, CallSettings callSettings = null)

Updates the specified Version resource. You can specify the following fields depending on the App Engine environment and type of scaling that the version resource uses:

**Standard environment**

  * [`instance_class`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.instance_class)



_automatic scaling_ in the standard environment:

  * [`automatic_scaling.min_idle_instances`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.automatic_scaling)
  * [`automatic_scaling.max_idle_instances`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.automatic_scaling)
  * [`automaticScaling.standard_scheduler_settings.max_instances`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#StandardSchedulerSettings)
  * [`automaticScaling.standard_scheduler_settings.min_instances`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#StandardSchedulerSettings)
  * [`automaticScaling.standard_scheduler_settings.target_cpu_utilization`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#StandardSchedulerSettings)
  * [`automaticScaling.standard_scheduler_settings.target_throughput_utilization`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#StandardSchedulerSettings)



_basic scaling_ or _manual scaling_ in the standard environment:

  * [`serving_status`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.serving_status)
  * [`manual_scaling.instances`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#manualscaling)



**Flexible environment**

  * [`serving_status`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.serving_status)



_automatic scaling_ in the flexible environment:

  * [`automatic_scaling.min_total_instances`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.automatic_scaling)
  * [`automatic_scaling.max_total_instances`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.automatic_scaling)
  * [`automatic_scaling.cool_down_period_sec`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.automatic_scaling)
  * [`automatic_scaling.cpu_utilization.target_utilization`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.automatic_scaling)



_manual scaling_ in the flexible environment:

  * [`manual_scaling.instances`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#manualscaling)



**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.UpdateVersionRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Version](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.Version)[OperationMetadataV1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.OperationMetadataV1)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::VersionsClient versionsClient = await gcav::VersionsClient.CreateAsync();
    // Initialize request argument(s)
    gcav::UpdateVersionRequest request = new gcav::UpdateVersionRequest
    {
        Name = "",
        Version = new gcav::Version(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Operation<gcav::Version, gcav::OperationMetadataV1> response = await versionsClient.UpdateVersionAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcav::Version, gcav::OperationMetadataV1> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcav::Version result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcav::Version, gcav::OperationMetadataV1> retrievedResponse = await versionsClient.PollOnceUpdateVersionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcav::Version retrievedResult = retrievedResponse.Result;
    }
    

### UpdateVersionAsync(UpdateVersionRequest, CancellationToken)
    
    
    public virtual Task<Operation<Version, OperationMetadataV1>> UpdateVersionAsync(UpdateVersionRequest request, CancellationToken cancellationToken)

Updates the specified Version resource. You can specify the following fields depending on the App Engine environment and type of scaling that the version resource uses:

**Standard environment**

  * [`instance_class`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.instance_class)



_automatic scaling_ in the standard environment:

  * [`automatic_scaling.min_idle_instances`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.automatic_scaling)
  * [`automatic_scaling.max_idle_instances`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.automatic_scaling)
  * [`automaticScaling.standard_scheduler_settings.max_instances`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#StandardSchedulerSettings)
  * [`automaticScaling.standard_scheduler_settings.min_instances`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#StandardSchedulerSettings)
  * [`automaticScaling.standard_scheduler_settings.target_cpu_utilization`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#StandardSchedulerSettings)
  * [`automaticScaling.standard_scheduler_settings.target_throughput_utilization`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#StandardSchedulerSettings)



_basic scaling_ or _manual scaling_ in the standard environment:

  * [`serving_status`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.serving_status)
  * [`manual_scaling.instances`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#manualscaling)



**Flexible environment**

  * [`serving_status`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.serving_status)



_automatic scaling_ in the flexible environment:

  * [`automatic_scaling.min_total_instances`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.automatic_scaling)
  * [`automatic_scaling.max_total_instances`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.automatic_scaling)
  * [`automatic_scaling.cool_down_period_sec`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.automatic_scaling)
  * [`automatic_scaling.cpu_utilization.target_utilization`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.automatic_scaling)



_manual scaling_ in the flexible environment:

  * [`manual_scaling.instances`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#manualscaling)



**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.UpdateVersionRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Version](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.Version)[OperationMetadataV1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.OperationMetadataV1)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::VersionsClient versionsClient = await gcav::VersionsClient.CreateAsync();
    // Initialize request argument(s)
    gcav::UpdateVersionRequest request = new gcav::UpdateVersionRequest
    {
        Name = "",
        Version = new gcav::Version(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Operation<gcav::Version, gcav::OperationMetadataV1> response = await versionsClient.UpdateVersionAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcav::Version, gcav::OperationMetadataV1> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcav::Version result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcav::Version, gcav::OperationMetadataV1> retrievedResponse = await versionsClient.PollOnceUpdateVersionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcav::Version retrievedResult = retrievedResponse.Result;
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
