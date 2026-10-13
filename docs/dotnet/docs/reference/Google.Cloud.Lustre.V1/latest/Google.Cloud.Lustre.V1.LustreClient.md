---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.LustreClient
title: Google Cloud Managed Lustre v1 API - Class LustreClient (1.1.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:07:39.690626+00:00
---

# Google Cloud Managed Lustre v1 API - Class LustreClient (1.1.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.LustreClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Managed Lustre v1 API - Class LustreClient (1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0 
    
    
    public abstract class LustreClient

Reference documentation and code samples for the Google Cloud Managed Lustre v1 API class LustreClient.

Lustre client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > LustreClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[LustreClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.LustreClientImpl)

## Namespace

[Google.Cloud.Lustre.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1)

## Assembly

Google.Cloud.Lustre.V1.dll

## Remarks

Service describing handlers for resources

## Properties 

### CreateDirectoryPolicyOperationsClient
    
    
    public virtual OperationsClient CreateDirectoryPolicyOperationsClient { get; }

The long-running operations client for `CreateDirectoryPolicy`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### CreateInstanceOperationsClient
    
    
    public virtual OperationsClient CreateInstanceOperationsClient { get; }

The long-running operations client for `CreateInstance`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### CreateMirrorOperationsClient
    
    
    public virtual OperationsClient CreateMirrorOperationsClient { get; }

The long-running operations client for `CreateMirror`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the Lustre service, which is a host of "lustre.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default Lustre scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default Lustre scopes are:

  * <https://www.googleapis.com/auth/cloud-platform>



### DeleteDirectoryPolicyOperationsClient
    
    
    public virtual OperationsClient DeleteDirectoryPolicyOperationsClient { get; }

The long-running operations client for `DeleteDirectoryPolicy`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DeleteInstanceOperationsClient
    
    
    public virtual OperationsClient DeleteInstanceOperationsClient { get; }

The long-running operations client for `DeleteInstance`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DeleteMirrorOperationsClient
    
    
    public virtual OperationsClient DeleteMirrorOperationsClient { get; }

The long-running operations client for `DeleteMirror`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### ExportDataOperationsClient
    
    
    public virtual OperationsClient ExportDataOperationsClient { get; }

The long-running operations client for `ExportData`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### GrpcClient
    
    
    public virtual Lustre.LustreClient GrpcClient { get; }

The underlying gRPC Lustre client

**Property Value**  
---  
**Type** | **Description**  
`[Lustre](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Lustre)[LustreClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Lustre.LustreClient)` |   
  
### IAMPolicyClient
    
    
    public virtual IAMPolicyClient IAMPolicyClient { get; }

The [IAMPolicyClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.IAMPolicyClient.html) associated with this client.

**Property Value**  
---  
**Type** | **Description**  
`[IAMPolicyClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.IAMPolicyClient.html)` |   
  
### ImportDataOperationsClient
    
    
    public virtual OperationsClient ImportDataOperationsClient { get; }

The long-running operations client for `ImportData`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### LocationsClient
    
    
    public virtual LocationsClient LocationsClient { get; }

The [LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.LocationsClient.html) associated with this client.

**Property Value**  
---  
**Type** | **Description**  
`[LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.LocationsClient.html)` |   
  
### RescheduleMaintenanceOperationsClient
    
    
    public virtual OperationsClient RescheduleMaintenanceOperationsClient { get; }

The long-running operations client for `RescheduleMaintenance`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### ServiceMetadata
    
    
    public static ServiceMetadata ServiceMetadata { get; }

The service metadata associated with this client type.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceMetadata](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceMetadata.html)` |   
  
### UpdateInstanceOperationsClient
    
    
    public virtual OperationsClient UpdateInstanceOperationsClient { get; }

The long-running operations client for `UpdateInstance`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### UpdateMirrorOperationsClient
    
    
    public virtual OperationsClient UpdateMirrorOperationsClient { get; }

The long-running operations client for `UpdateMirror`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
## Methods 

### Create()
    
    
    public static LustreClient Create()

Synchronously creates a [LustreClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.LustreClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [LustreClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.LustreClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[LustreClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.LustreClient)` | The created [LustreClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.LustreClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<LustreClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [LustreClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.LustreClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [LustreClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.LustreClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[LustreClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.LustreClient)` | The task representing the created [LustreClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.LustreClient).  
  
### CreateDirectoryPolicy(CreateDirectoryPolicyRequest, CallSettings)
    
    
    public virtual Operation<DirectoryPolicy, OperationMetadata> CreateDirectoryPolicy(CreateDirectoryPolicyRequest request, CallSettings callSettings = null)

Creates a directory policy resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDirectoryPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.CreateDirectoryPolicyRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DirectoryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.DirectoryPolicy)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = LustreClient.Create();
    // Initialize request argument(s)
    CreateDirectoryPolicyRequest request = new CreateDirectoryPolicyRequest
    {
        ParentAsInstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
        DirectoryPolicyId = "",
        DirectoryPolicy = new DirectoryPolicy(),
    };
    // Make the request
    Operation<DirectoryPolicy, OperationMetadata> response = lustreClient.CreateDirectoryPolicy(request);
    
    // Poll until the returned long-running operation is complete
    Operation<DirectoryPolicy, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    DirectoryPolicy result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<DirectoryPolicy, OperationMetadata> retrievedResponse = lustreClient.PollOnceCreateDirectoryPolicy(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        DirectoryPolicy retrievedResult = retrievedResponse.Result;
    }
    

### CreateDirectoryPolicy(InstanceName, DirectoryPolicy, string, CallSettings)
    
    
    public virtual Operation<DirectoryPolicy, OperationMetadata> CreateDirectoryPolicy(InstanceName parent, DirectoryPolicy directoryPolicy, string directoryPolicyId, CallSettings callSettings = null)

Creates a directory policy resource.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.InstanceName)`  
Required. The parent instance. It must be in the format of `projects/{project}/locations/{location}/instances/{instance}`.  
`directoryPolicy` | `[DirectoryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.DirectoryPolicy)`  
Required. The directory policy to create.  
`directoryPolicyId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID for the DirectoryPolicy to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DirectoryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.DirectoryPolicy)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = LustreClient.Create();
    // Initialize request argument(s)
    InstanceName parent = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    DirectoryPolicy directoryPolicy = new DirectoryPolicy();
    string directoryPolicyId = "";
    // Make the request
    Operation<DirectoryPolicy, OperationMetadata> response = lustreClient.CreateDirectoryPolicy(parent, directoryPolicy, directoryPolicyId);
    
    // Poll until the returned long-running operation is complete
    Operation<DirectoryPolicy, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    DirectoryPolicy result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<DirectoryPolicy, OperationMetadata> retrievedResponse = lustreClient.PollOnceCreateDirectoryPolicy(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        DirectoryPolicy retrievedResult = retrievedResponse.Result;
    }
    

### CreateDirectoryPolicy(string, DirectoryPolicy, string, CallSettings)
    
    
    public virtual Operation<DirectoryPolicy, OperationMetadata> CreateDirectoryPolicy(string parent, DirectoryPolicy directoryPolicy, string directoryPolicyId, CallSettings callSettings = null)

Creates a directory policy resource.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent instance. It must be in the format of `projects/{project}/locations/{location}/instances/{instance}`.  
`directoryPolicy` | `[DirectoryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.DirectoryPolicy)`  
Required. The directory policy to create.  
`directoryPolicyId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID for the DirectoryPolicy to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DirectoryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.DirectoryPolicy)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = LustreClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]";
    DirectoryPolicy directoryPolicy = new DirectoryPolicy();
    string directoryPolicyId = "";
    // Make the request
    Operation<DirectoryPolicy, OperationMetadata> response = lustreClient.CreateDirectoryPolicy(parent, directoryPolicy, directoryPolicyId);
    
    // Poll until the returned long-running operation is complete
    Operation<DirectoryPolicy, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    DirectoryPolicy result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<DirectoryPolicy, OperationMetadata> retrievedResponse = lustreClient.PollOnceCreateDirectoryPolicy(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        DirectoryPolicy retrievedResult = retrievedResponse.Result;
    }
    

### CreateDirectoryPolicyAsync(CreateDirectoryPolicyRequest, CallSettings)
    
    
    public virtual Task<Operation<DirectoryPolicy, OperationMetadata>> CreateDirectoryPolicyAsync(CreateDirectoryPolicyRequest request, CallSettings callSettings = null)

Creates a directory policy resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDirectoryPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.CreateDirectoryPolicyRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DirectoryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.DirectoryPolicy)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    CreateDirectoryPolicyRequest request = new CreateDirectoryPolicyRequest
    {
        ParentAsInstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
        DirectoryPolicyId = "",
        DirectoryPolicy = new DirectoryPolicy(),
    };
    // Make the request
    Operation<DirectoryPolicy, OperationMetadata> response = await lustreClient.CreateDirectoryPolicyAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<DirectoryPolicy, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    DirectoryPolicy result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<DirectoryPolicy, OperationMetadata> retrievedResponse = await lustreClient.PollOnceCreateDirectoryPolicyAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        DirectoryPolicy retrievedResult = retrievedResponse.Result;
    }
    

### CreateDirectoryPolicyAsync(CreateDirectoryPolicyRequest, CancellationToken)
    
    
    public virtual Task<Operation<DirectoryPolicy, OperationMetadata>> CreateDirectoryPolicyAsync(CreateDirectoryPolicyRequest request, CancellationToken cancellationToken)

Creates a directory policy resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDirectoryPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.CreateDirectoryPolicyRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DirectoryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.DirectoryPolicy)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    CreateDirectoryPolicyRequest request = new CreateDirectoryPolicyRequest
    {
        ParentAsInstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
        DirectoryPolicyId = "",
        DirectoryPolicy = new DirectoryPolicy(),
    };
    // Make the request
    Operation<DirectoryPolicy, OperationMetadata> response = await lustreClient.CreateDirectoryPolicyAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<DirectoryPolicy, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    DirectoryPolicy result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<DirectoryPolicy, OperationMetadata> retrievedResponse = await lustreClient.PollOnceCreateDirectoryPolicyAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        DirectoryPolicy retrievedResult = retrievedResponse.Result;
    }
    

### CreateDirectoryPolicyAsync(InstanceName, DirectoryPolicy, string, CallSettings)
    
    
    public virtual Task<Operation<DirectoryPolicy, OperationMetadata>> CreateDirectoryPolicyAsync(InstanceName parent, DirectoryPolicy directoryPolicy, string directoryPolicyId, CallSettings callSettings = null)

Creates a directory policy resource.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.InstanceName)`  
Required. The parent instance. It must be in the format of `projects/{project}/locations/{location}/instances/{instance}`.  
`directoryPolicy` | `[DirectoryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.DirectoryPolicy)`  
Required. The directory policy to create.  
`directoryPolicyId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID for the DirectoryPolicy to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DirectoryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.DirectoryPolicy)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName parent = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    DirectoryPolicy directoryPolicy = new DirectoryPolicy();
    string directoryPolicyId = "";
    // Make the request
    Operation<DirectoryPolicy, OperationMetadata> response = await lustreClient.CreateDirectoryPolicyAsync(parent, directoryPolicy, directoryPolicyId);
    
    // Poll until the returned long-running operation is complete
    Operation<DirectoryPolicy, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    DirectoryPolicy result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<DirectoryPolicy, OperationMetadata> retrievedResponse = await lustreClient.PollOnceCreateDirectoryPolicyAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        DirectoryPolicy retrievedResult = retrievedResponse.Result;
    }
    

### CreateDirectoryPolicyAsync(InstanceName, DirectoryPolicy, string, CancellationToken)
    
    
    public virtual Task<Operation<DirectoryPolicy, OperationMetadata>> CreateDirectoryPolicyAsync(InstanceName parent, DirectoryPolicy directoryPolicy, string directoryPolicyId, CancellationToken cancellationToken)

Creates a directory policy resource.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.InstanceName)`  
Required. The parent instance. It must be in the format of `projects/{project}/locations/{location}/instances/{instance}`.  
`directoryPolicy` | `[DirectoryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.DirectoryPolicy)`  
Required. The directory policy to create.  
`directoryPolicyId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID for the DirectoryPolicy to create.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DirectoryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.DirectoryPolicy)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName parent = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    DirectoryPolicy directoryPolicy = new DirectoryPolicy();
    string directoryPolicyId = "";
    // Make the request
    Operation<DirectoryPolicy, OperationMetadata> response = await lustreClient.CreateDirectoryPolicyAsync(parent, directoryPolicy, directoryPolicyId);
    
    // Poll until the returned long-running operation is complete
    Operation<DirectoryPolicy, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    DirectoryPolicy result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<DirectoryPolicy, OperationMetadata> retrievedResponse = await lustreClient.PollOnceCreateDirectoryPolicyAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        DirectoryPolicy retrievedResult = retrievedResponse.Result;
    }
    

### CreateDirectoryPolicyAsync(string, DirectoryPolicy, string, CallSettings)
    
    
    public virtual Task<Operation<DirectoryPolicy, OperationMetadata>> CreateDirectoryPolicyAsync(string parent, DirectoryPolicy directoryPolicy, string directoryPolicyId, CallSettings callSettings = null)

Creates a directory policy resource.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent instance. It must be in the format of `projects/{project}/locations/{location}/instances/{instance}`.  
`directoryPolicy` | `[DirectoryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.DirectoryPolicy)`  
Required. The directory policy to create.  
`directoryPolicyId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID for the DirectoryPolicy to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DirectoryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.DirectoryPolicy)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]";
    DirectoryPolicy directoryPolicy = new DirectoryPolicy();
    string directoryPolicyId = "";
    // Make the request
    Operation<DirectoryPolicy, OperationMetadata> response = await lustreClient.CreateDirectoryPolicyAsync(parent, directoryPolicy, directoryPolicyId);
    
    // Poll until the returned long-running operation is complete
    Operation<DirectoryPolicy, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    DirectoryPolicy result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<DirectoryPolicy, OperationMetadata> retrievedResponse = await lustreClient.PollOnceCreateDirectoryPolicyAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        DirectoryPolicy retrievedResult = retrievedResponse.Result;
    }
    

### CreateDirectoryPolicyAsync(string, DirectoryPolicy, string, CancellationToken)
    
    
    public virtual Task<Operation<DirectoryPolicy, OperationMetadata>> CreateDirectoryPolicyAsync(string parent, DirectoryPolicy directoryPolicy, string directoryPolicyId, CancellationToken cancellationToken)

Creates a directory policy resource.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent instance. It must be in the format of `projects/{project}/locations/{location}/instances/{instance}`.  
`directoryPolicy` | `[DirectoryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.DirectoryPolicy)`  
Required. The directory policy to create.  
`directoryPolicyId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID for the DirectoryPolicy to create.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DirectoryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.DirectoryPolicy)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]";
    DirectoryPolicy directoryPolicy = new DirectoryPolicy();
    string directoryPolicyId = "";
    // Make the request
    Operation<DirectoryPolicy, OperationMetadata> response = await lustreClient.CreateDirectoryPolicyAsync(parent, directoryPolicy, directoryPolicyId);
    
    // Poll until the returned long-running operation is complete
    Operation<DirectoryPolicy, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    DirectoryPolicy result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<DirectoryPolicy, OperationMetadata> retrievedResponse = await lustreClient.PollOnceCreateDirectoryPolicyAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        DirectoryPolicy retrievedResult = retrievedResponse.Result;
    }
    

### CreateInstance(LocationName, Instance, string, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> CreateInstance(LocationName parent, Instance instance, string instanceId, CallSettings callSettings = null)

Creates a new instance in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The instance's project and location, in the format `projects/{project}/locations/{location}`. Locations map to Google Cloud zones; for example, `us-west1-b`.  
`instance` | `[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)`  
Required. The resource being created  
`instanceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Managed Lustre instance.

  * Must contain only lowercase letters, numbers, and hyphens.
  * Must start with a letter.
  * Must be between 1-63 characters.
  * Must end with a number or a letter.

  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = LustreClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Instance instance = new Instance();
    string instanceId = "";
    // Make the request
    Operation<Instance, OperationMetadata> response = lustreClient.CreateInstance(parent, instance, instanceId);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = lustreClient.PollOnceCreateInstance(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### CreateInstance(CreateInstanceRequest, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> CreateInstance(CreateInstanceRequest request, CallSettings callSettings = null)

Creates a new instance in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.CreateInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = LustreClient.Create();
    // Initialize request argument(s)
    CreateInstanceRequest request = new CreateInstanceRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        InstanceId = "",
        Instance = new Instance(),
        RequestId = "",
    };
    // Make the request
    Operation<Instance, OperationMetadata> response = lustreClient.CreateInstance(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = lustreClient.PollOnceCreateInstance(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### CreateInstance(string, Instance, string, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> CreateInstance(string parent, Instance instance, string instanceId, CallSettings callSettings = null)

Creates a new instance in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The instance's project and location, in the format `projects/{project}/locations/{location}`. Locations map to Google Cloud zones; for example, `us-west1-b`.  
`instance` | `[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)`  
Required. The resource being created  
`instanceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Managed Lustre instance.

  * Must contain only lowercase letters, numbers, and hyphens.
  * Must start with a letter.
  * Must be between 1-63 characters.
  * Must end with a number or a letter.

  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = LustreClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Instance instance = new Instance();
    string instanceId = "";
    // Make the request
    Operation<Instance, OperationMetadata> response = lustreClient.CreateInstance(parent, instance, instanceId);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = lustreClient.PollOnceCreateInstance(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### CreateInstanceAsync(LocationName, Instance, string, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> CreateInstanceAsync(LocationName parent, Instance instance, string instanceId, CallSettings callSettings = null)

Creates a new instance in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The instance's project and location, in the format `projects/{project}/locations/{location}`. Locations map to Google Cloud zones; for example, `us-west1-b`.  
`instance` | `[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)`  
Required. The resource being created  
`instanceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Managed Lustre instance.

  * Must contain only lowercase letters, numbers, and hyphens.
  * Must start with a letter.
  * Must be between 1-63 characters.
  * Must end with a number or a letter.

  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Instance instance = new Instance();
    string instanceId = "";
    // Make the request
    Operation<Instance, OperationMetadata> response = await lustreClient.CreateInstanceAsync(parent, instance, instanceId);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await lustreClient.PollOnceCreateInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### CreateInstanceAsync(LocationName, Instance, string, CancellationToken)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> CreateInstanceAsync(LocationName parent, Instance instance, string instanceId, CancellationToken cancellationToken)

Creates a new instance in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The instance's project and location, in the format `projects/{project}/locations/{location}`. Locations map to Google Cloud zones; for example, `us-west1-b`.  
`instance` | `[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)`  
Required. The resource being created  
`instanceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Managed Lustre instance.

  * Must contain only lowercase letters, numbers, and hyphens.
  * Must start with a letter.
  * Must be between 1-63 characters.
  * Must end with a number or a letter.

  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Instance instance = new Instance();
    string instanceId = "";
    // Make the request
    Operation<Instance, OperationMetadata> response = await lustreClient.CreateInstanceAsync(parent, instance, instanceId);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await lustreClient.PollOnceCreateInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### CreateInstanceAsync(CreateInstanceRequest, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> CreateInstanceAsync(CreateInstanceRequest request, CallSettings callSettings = null)

Creates a new instance in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.CreateInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    CreateInstanceRequest request = new CreateInstanceRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        InstanceId = "",
        Instance = new Instance(),
        RequestId = "",
    };
    // Make the request
    Operation<Instance, OperationMetadata> response = await lustreClient.CreateInstanceAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await lustreClient.PollOnceCreateInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### CreateInstanceAsync(CreateInstanceRequest, CancellationToken)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> CreateInstanceAsync(CreateInstanceRequest request, CancellationToken cancellationToken)

Creates a new instance in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.CreateInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    CreateInstanceRequest request = new CreateInstanceRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        InstanceId = "",
        Instance = new Instance(),
        RequestId = "",
    };
    // Make the request
    Operation<Instance, OperationMetadata> response = await lustreClient.CreateInstanceAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await lustreClient.PollOnceCreateInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### CreateInstanceAsync(string, Instance, string, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> CreateInstanceAsync(string parent, Instance instance, string instanceId, CallSettings callSettings = null)

Creates a new instance in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The instance's project and location, in the format `projects/{project}/locations/{location}`. Locations map to Google Cloud zones; for example, `us-west1-b`.  
`instance` | `[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)`  
Required. The resource being created  
`instanceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Managed Lustre instance.

  * Must contain only lowercase letters, numbers, and hyphens.
  * Must start with a letter.
  * Must be between 1-63 characters.
  * Must end with a number or a letter.

  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Instance instance = new Instance();
    string instanceId = "";
    // Make the request
    Operation<Instance, OperationMetadata> response = await lustreClient.CreateInstanceAsync(parent, instance, instanceId);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await lustreClient.PollOnceCreateInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### CreateInstanceAsync(string, Instance, string, CancellationToken)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> CreateInstanceAsync(string parent, Instance instance, string instanceId, CancellationToken cancellationToken)

Creates a new instance in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The instance's project and location, in the format `projects/{project}/locations/{location}`. Locations map to Google Cloud zones; for example, `us-west1-b`.  
`instance` | `[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)`  
Required. The resource being created  
`instanceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Managed Lustre instance.

  * Must contain only lowercase letters, numbers, and hyphens.
  * Must start with a letter.
  * Must be between 1-63 characters.
  * Must end with a number or a letter.

  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Instance instance = new Instance();
    string instanceId = "";
    // Make the request
    Operation<Instance, OperationMetadata> response = await lustreClient.CreateInstanceAsync(parent, instance, instanceId);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await lustreClient.PollOnceCreateInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### CreateMirror(CreateMirrorRequest, CallSettings)
    
    
    public virtual Operation<Mirror, CreateMirrorMetadata> CreateMirror(CreateMirrorRequest request, CallSettings callSettings = null)

Creates a new mirror in a given instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateMirrorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.CreateMirrorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Mirror](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Mirror)[CreateMirrorMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.CreateMirrorMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = LustreClient.Create();
    // Initialize request argument(s)
    CreateMirrorRequest request = new CreateMirrorRequest
    {
        ParentAsInstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
        MirrorId = "",
        Mirror = new Mirror(),
        RequestId = "",
    };
    // Make the request
    Operation<Mirror, CreateMirrorMetadata> response = lustreClient.CreateMirror(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Mirror, CreateMirrorMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Mirror result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Mirror, CreateMirrorMetadata> retrievedResponse = lustreClient.PollOnceCreateMirror(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Mirror retrievedResult = retrievedResponse.Result;
    }
    

### CreateMirror(InstanceName, Mirror, string, CallSettings)
    
    
    public virtual Operation<Mirror, CreateMirrorMetadata> CreateMirror(InstanceName parent, Mirror mirror, string mirrorId, CallSettings callSettings = null)

Creates a new mirror in a given instance.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.InstanceName)`  
Required. Parent instance resource where the mirror will be created, in the format: `projects/{project}/locations/{location}/instances/{instance}`  
`mirror` | `[Mirror](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Mirror)`  
Required. The mirror to create.  
`mirrorId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the mirror.

  * Must contain only lowercase letters, numbers, and hyphens.
  * Must start with a letter.
  * Must be between 1-63 characters.
  * Must end with a number or a letter.

The ID cannot be changed after the mirror is created.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Mirror](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Mirror)[CreateMirrorMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.CreateMirrorMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = LustreClient.Create();
    // Initialize request argument(s)
    InstanceName parent = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    Mirror mirror = new Mirror();
    string mirrorId = "";
    // Make the request
    Operation<Mirror, CreateMirrorMetadata> response = lustreClient.CreateMirror(parent, mirror, mirrorId);
    
    // Poll until the returned long-running operation is complete
    Operation<Mirror, CreateMirrorMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Mirror result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Mirror, CreateMirrorMetadata> retrievedResponse = lustreClient.PollOnceCreateMirror(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Mirror retrievedResult = retrievedResponse.Result;
    }
    

### CreateMirror(string, Mirror, string, CallSettings)
    
    
    public virtual Operation<Mirror, CreateMirrorMetadata> CreateMirror(string parent, Mirror mirror, string mirrorId, CallSettings callSettings = null)

Creates a new mirror in a given instance.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Parent instance resource where the mirror will be created, in the format: `projects/{project}/locations/{location}/instances/{instance}`  
`mirror` | `[Mirror](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Mirror)`  
Required. The mirror to create.  
`mirrorId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the mirror.

  * Must contain only lowercase letters, numbers, and hyphens.
  * Must start with a letter.
  * Must be between 1-63 characters.
  * Must end with a number or a letter.

The ID cannot be changed after the mirror is created.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Mirror](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Mirror)[CreateMirrorMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.CreateMirrorMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = LustreClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]";
    Mirror mirror = new Mirror();
    string mirrorId = "";
    // Make the request
    Operation<Mirror, CreateMirrorMetadata> response = lustreClient.CreateMirror(parent, mirror, mirrorId);
    
    // Poll until the returned long-running operation is complete
    Operation<Mirror, CreateMirrorMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Mirror result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Mirror, CreateMirrorMetadata> retrievedResponse = lustreClient.PollOnceCreateMirror(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Mirror retrievedResult = retrievedResponse.Result;
    }
    

### CreateMirrorAsync(CreateMirrorRequest, CallSettings)
    
    
    public virtual Task<Operation<Mirror, CreateMirrorMetadata>> CreateMirrorAsync(CreateMirrorRequest request, CallSettings callSettings = null)

Creates a new mirror in a given instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateMirrorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.CreateMirrorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Mirror](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Mirror)[CreateMirrorMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.CreateMirrorMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    CreateMirrorRequest request = new CreateMirrorRequest
    {
        ParentAsInstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
        MirrorId = "",
        Mirror = new Mirror(),
        RequestId = "",
    };
    // Make the request
    Operation<Mirror, CreateMirrorMetadata> response = await lustreClient.CreateMirrorAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Mirror, CreateMirrorMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Mirror result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Mirror, CreateMirrorMetadata> retrievedResponse = await lustreClient.PollOnceCreateMirrorAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Mirror retrievedResult = retrievedResponse.Result;
    }
    

### CreateMirrorAsync(CreateMirrorRequest, CancellationToken)
    
    
    public virtual Task<Operation<Mirror, CreateMirrorMetadata>> CreateMirrorAsync(CreateMirrorRequest request, CancellationToken cancellationToken)

Creates a new mirror in a given instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateMirrorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.CreateMirrorRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Mirror](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Mirror)[CreateMirrorMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.CreateMirrorMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    CreateMirrorRequest request = new CreateMirrorRequest
    {
        ParentAsInstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
        MirrorId = "",
        Mirror = new Mirror(),
        RequestId = "",
    };
    // Make the request
    Operation<Mirror, CreateMirrorMetadata> response = await lustreClient.CreateMirrorAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Mirror, CreateMirrorMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Mirror result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Mirror, CreateMirrorMetadata> retrievedResponse = await lustreClient.PollOnceCreateMirrorAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Mirror retrievedResult = retrievedResponse.Result;
    }
    

### CreateMirrorAsync(InstanceName, Mirror, string, CallSettings)
    
    
    public virtual Task<Operation<Mirror, CreateMirrorMetadata>> CreateMirrorAsync(InstanceName parent, Mirror mirror, string mirrorId, CallSettings callSettings = null)

Creates a new mirror in a given instance.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.InstanceName)`  
Required. Parent instance resource where the mirror will be created, in the format: `projects/{project}/locations/{location}/instances/{instance}`  
`mirror` | `[Mirror](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Mirror)`  
Required. The mirror to create.  
`mirrorId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the mirror.

  * Must contain only lowercase letters, numbers, and hyphens.
  * Must start with a letter.
  * Must be between 1-63 characters.
  * Must end with a number or a letter.

The ID cannot be changed after the mirror is created.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Mirror](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Mirror)[CreateMirrorMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.CreateMirrorMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName parent = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    Mirror mirror = new Mirror();
    string mirrorId = "";
    // Make the request
    Operation<Mirror, CreateMirrorMetadata> response = await lustreClient.CreateMirrorAsync(parent, mirror, mirrorId);
    
    // Poll until the returned long-running operation is complete
    Operation<Mirror, CreateMirrorMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Mirror result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Mirror, CreateMirrorMetadata> retrievedResponse = await lustreClient.PollOnceCreateMirrorAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Mirror retrievedResult = retrievedResponse.Result;
    }
    

### CreateMirrorAsync(InstanceName, Mirror, string, CancellationToken)
    
    
    public virtual Task<Operation<Mirror, CreateMirrorMetadata>> CreateMirrorAsync(InstanceName parent, Mirror mirror, string mirrorId, CancellationToken cancellationToken)

Creates a new mirror in a given instance.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.InstanceName)`  
Required. Parent instance resource where the mirror will be created, in the format: `projects/{project}/locations/{location}/instances/{instance}`  
`mirror` | `[Mirror](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Mirror)`  
Required. The mirror to create.  
`mirrorId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the mirror.

  * Must contain only lowercase letters, numbers, and hyphens.
  * Must start with a letter.
  * Must be between 1-63 characters.
  * Must end with a number or a letter.

The ID cannot be changed after the mirror is created.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Mirror](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Mirror)[CreateMirrorMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.CreateMirrorMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName parent = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    Mirror mirror = new Mirror();
    string mirrorId = "";
    // Make the request
    Operation<Mirror, CreateMirrorMetadata> response = await lustreClient.CreateMirrorAsync(parent, mirror, mirrorId);
    
    // Poll until the returned long-running operation is complete
    Operation<Mirror, CreateMirrorMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Mirror result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Mirror, CreateMirrorMetadata> retrievedResponse = await lustreClient.PollOnceCreateMirrorAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Mirror retrievedResult = retrievedResponse.Result;
    }
    

### CreateMirrorAsync(string, Mirror, string, CallSettings)
    
    
    public virtual Task<Operation<Mirror, CreateMirrorMetadata>> CreateMirrorAsync(string parent, Mirror mirror, string mirrorId, CallSettings callSettings = null)

Creates a new mirror in a given instance.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Parent instance resource where the mirror will be created, in the format: `projects/{project}/locations/{location}/instances/{instance}`  
`mirror` | `[Mirror](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Mirror)`  
Required. The mirror to create.  
`mirrorId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the mirror.

  * Must contain only lowercase letters, numbers, and hyphens.
  * Must start with a letter.
  * Must be between 1-63 characters.
  * Must end with a number or a letter.

The ID cannot be changed after the mirror is created.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Mirror](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Mirror)[CreateMirrorMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.CreateMirrorMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]";
    Mirror mirror = new Mirror();
    string mirrorId = "";
    // Make the request
    Operation<Mirror, CreateMirrorMetadata> response = await lustreClient.CreateMirrorAsync(parent, mirror, mirrorId);
    
    // Poll until the returned long-running operation is complete
    Operation<Mirror, CreateMirrorMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Mirror result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Mirror, CreateMirrorMetadata> retrievedResponse = await lustreClient.PollOnceCreateMirrorAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Mirror retrievedResult = retrievedResponse.Result;
    }
    

### CreateMirrorAsync(string, Mirror, string, CancellationToken)
    
    
    public virtual Task<Operation<Mirror, CreateMirrorMetadata>> CreateMirrorAsync(string parent, Mirror mirror, string mirrorId, CancellationToken cancellationToken)

Creates a new mirror in a given instance.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Parent instance resource where the mirror will be created, in the format: `projects/{project}/locations/{location}/instances/{instance}`  
`mirror` | `[Mirror](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Mirror)`  
Required. The mirror to create.  
`mirrorId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the mirror.

  * Must contain only lowercase letters, numbers, and hyphens.
  * Must start with a letter.
  * Must be between 1-63 characters.
  * Must end with a number or a letter.

The ID cannot be changed after the mirror is created.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Mirror](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Mirror)[CreateMirrorMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.CreateMirrorMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]";
    Mirror mirror = new Mirror();
    string mirrorId = "";
    // Make the request
    Operation<Mirror, CreateMirrorMetadata> response = await lustreClient.CreateMirrorAsync(parent, mirror, mirrorId);
    
    // Poll until the returned long-running operation is complete
    Operation<Mirror, CreateMirrorMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Mirror result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Mirror, CreateMirrorMetadata> retrievedResponse = await lustreClient.PollOnceCreateMirrorAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Mirror retrievedResult = retrievedResponse.Result;
    }
    

### DeleteDirectoryPolicy(DeleteDirectoryPolicyRequest, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteDirectoryPolicy(DeleteDirectoryPolicyRequest request, CallSettings callSettings = null)

Deletes a directory policy resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDirectoryPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.DeleteDirectoryPolicyRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = LustreClient.Create();
    // Initialize request argument(s)
    DeleteDirectoryPolicyRequest request = new DeleteDirectoryPolicyRequest
    {
        DirectoryPolicyName = DirectoryPolicyName.FromProjectLocationInstanceDirectoryPolicy("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[DIRECTORY_POLICY]"),
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = lustreClient.DeleteDirectoryPolicy(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = lustreClient.PollOnceDeleteDirectoryPolicy(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteDirectoryPolicy(DirectoryPolicyName, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteDirectoryPolicy(DirectoryPolicyName name, CallSettings callSettings = null)

Deletes a directory policy resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DirectoryPolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.DirectoryPolicyName)`  
Required. The resource name of the directory policy. DirectoryPolicy names have the form `projects/{project}/locations/{location}/instances/{instance}/directoryPolicies/{id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = LustreClient.Create();
    // Initialize request argument(s)
    DirectoryPolicyName name = DirectoryPolicyName.FromProjectLocationInstanceDirectoryPolicy("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[DIRECTORY_POLICY]");
    // Make the request
    Operation<Empty, OperationMetadata> response = lustreClient.DeleteDirectoryPolicy(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = lustreClient.PollOnceDeleteDirectoryPolicy(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteDirectoryPolicy(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteDirectoryPolicy(string name, CallSettings callSettings = null)

Deletes a directory policy resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the directory policy. DirectoryPolicy names have the form `projects/{project}/locations/{location}/instances/{instance}/directoryPolicies/{id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = LustreClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]/directoryPolicies/[DIRECTORY_POLICY]";
    // Make the request
    Operation<Empty, OperationMetadata> response = lustreClient.DeleteDirectoryPolicy(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = lustreClient.PollOnceDeleteDirectoryPolicy(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteDirectoryPolicyAsync(DeleteDirectoryPolicyRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteDirectoryPolicyAsync(DeleteDirectoryPolicyRequest request, CallSettings callSettings = null)

Deletes a directory policy resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDirectoryPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.DeleteDirectoryPolicyRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    DeleteDirectoryPolicyRequest request = new DeleteDirectoryPolicyRequest
    {
        DirectoryPolicyName = DirectoryPolicyName.FromProjectLocationInstanceDirectoryPolicy("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[DIRECTORY_POLICY]"),
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await lustreClient.DeleteDirectoryPolicyAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await lustreClient.PollOnceDeleteDirectoryPolicyAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteDirectoryPolicyAsync(DeleteDirectoryPolicyRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteDirectoryPolicyAsync(DeleteDirectoryPolicyRequest request, CancellationToken cancellationToken)

Deletes a directory policy resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDirectoryPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.DeleteDirectoryPolicyRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    DeleteDirectoryPolicyRequest request = new DeleteDirectoryPolicyRequest
    {
        DirectoryPolicyName = DirectoryPolicyName.FromProjectLocationInstanceDirectoryPolicy("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[DIRECTORY_POLICY]"),
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await lustreClient.DeleteDirectoryPolicyAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await lustreClient.PollOnceDeleteDirectoryPolicyAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteDirectoryPolicyAsync(DirectoryPolicyName, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteDirectoryPolicyAsync(DirectoryPolicyName name, CallSettings callSettings = null)

Deletes a directory policy resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DirectoryPolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.DirectoryPolicyName)`  
Required. The resource name of the directory policy. DirectoryPolicy names have the form `projects/{project}/locations/{location}/instances/{instance}/directoryPolicies/{id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    DirectoryPolicyName name = DirectoryPolicyName.FromProjectLocationInstanceDirectoryPolicy("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[DIRECTORY_POLICY]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await lustreClient.DeleteDirectoryPolicyAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await lustreClient.PollOnceDeleteDirectoryPolicyAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteDirectoryPolicyAsync(DirectoryPolicyName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteDirectoryPolicyAsync(DirectoryPolicyName name, CancellationToken cancellationToken)

Deletes a directory policy resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DirectoryPolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.DirectoryPolicyName)`  
Required. The resource name of the directory policy. DirectoryPolicy names have the form `projects/{project}/locations/{location}/instances/{instance}/directoryPolicies/{id}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    DirectoryPolicyName name = DirectoryPolicyName.FromProjectLocationInstanceDirectoryPolicy("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[DIRECTORY_POLICY]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await lustreClient.DeleteDirectoryPolicyAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await lustreClient.PollOnceDeleteDirectoryPolicyAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteDirectoryPolicyAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteDirectoryPolicyAsync(string name, CallSettings callSettings = null)

Deletes a directory policy resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the directory policy. DirectoryPolicy names have the form `projects/{project}/locations/{location}/instances/{instance}/directoryPolicies/{id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]/directoryPolicies/[DIRECTORY_POLICY]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await lustreClient.DeleteDirectoryPolicyAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await lustreClient.PollOnceDeleteDirectoryPolicyAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteDirectoryPolicyAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteDirectoryPolicyAsync(string name, CancellationToken cancellationToken)

Deletes a directory policy resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the directory policy. DirectoryPolicy names have the form `projects/{project}/locations/{location}/instances/{instance}/directoryPolicies/{id}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]/directoryPolicies/[DIRECTORY_POLICY]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await lustreClient.DeleteDirectoryPolicyAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await lustreClient.PollOnceDeleteDirectoryPolicyAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteInstance(DeleteInstanceRequest, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteInstance(DeleteInstanceRequest request, CallSettings callSettings = null)

Deletes a single instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.DeleteInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = LustreClient.Create();
    // Initialize request argument(s)
    DeleteInstanceRequest request = new DeleteInstanceRequest
    {
        InstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
        RequestId = "",
        Force = false,
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = lustreClient.DeleteInstance(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = lustreClient.PollOnceDeleteInstance(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteInstance(InstanceName, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteInstance(InstanceName name, CallSettings callSettings = null)

Deletes a single instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.InstanceName)`  
Required. The resource name of the instance to delete, in the format `projects/{projectId}/locations/{location}/instances/{instanceId}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = LustreClient.Create();
    // Initialize request argument(s)
    InstanceName name = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    // Make the request
    Operation<Empty, OperationMetadata> response = lustreClient.DeleteInstance(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = lustreClient.PollOnceDeleteInstance(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteInstance(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteInstance(string name, CallSettings callSettings = null)

Deletes a single instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the instance to delete, in the format `projects/{projectId}/locations/{location}/instances/{instanceId}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = LustreClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]";
    // Make the request
    Operation<Empty, OperationMetadata> response = lustreClient.DeleteInstance(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = lustreClient.PollOnceDeleteInstance(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteInstanceAsync(DeleteInstanceRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteInstanceAsync(DeleteInstanceRequest request, CallSettings callSettings = null)

Deletes a single instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.DeleteInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    DeleteInstanceRequest request = new DeleteInstanceRequest
    {
        InstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
        RequestId = "",
        Force = false,
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await lustreClient.DeleteInstanceAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await lustreClient.PollOnceDeleteInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteInstanceAsync(DeleteInstanceRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteInstanceAsync(DeleteInstanceRequest request, CancellationToken cancellationToken)

Deletes a single instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.DeleteInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    DeleteInstanceRequest request = new DeleteInstanceRequest
    {
        InstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
        RequestId = "",
        Force = false,
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await lustreClient.DeleteInstanceAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await lustreClient.PollOnceDeleteInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteInstanceAsync(InstanceName, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteInstanceAsync(InstanceName name, CallSettings callSettings = null)

Deletes a single instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.InstanceName)`  
Required. The resource name of the instance to delete, in the format `projects/{projectId}/locations/{location}/instances/{instanceId}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName name = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await lustreClient.DeleteInstanceAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await lustreClient.PollOnceDeleteInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteInstanceAsync(InstanceName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteInstanceAsync(InstanceName name, CancellationToken cancellationToken)

Deletes a single instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.InstanceName)`  
Required. The resource name of the instance to delete, in the format `projects/{projectId}/locations/{location}/instances/{instanceId}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName name = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await lustreClient.DeleteInstanceAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await lustreClient.PollOnceDeleteInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteInstanceAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteInstanceAsync(string name, CallSettings callSettings = null)

Deletes a single instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the instance to delete, in the format `projects/{projectId}/locations/{location}/instances/{instanceId}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await lustreClient.DeleteInstanceAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await lustreClient.PollOnceDeleteInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteInstanceAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteInstanceAsync(string name, CancellationToken cancellationToken)

Deletes a single instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the instance to delete, in the format `projects/{projectId}/locations/{location}/instances/{instanceId}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await lustreClient.DeleteInstanceAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await lustreClient.PollOnceDeleteInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteMirror(DeleteMirrorRequest, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteMirror(DeleteMirrorRequest request, CallSettings callSettings = null)

Deletes a single mirror.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteMirrorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.DeleteMirrorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = LustreClient.Create();
    // Initialize request argument(s)
    DeleteMirrorRequest request = new DeleteMirrorRequest
    {
        MirrorName = MirrorName.FromProjectLocationInstanceMirror("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[MIRROR]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = lustreClient.DeleteMirror(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = lustreClient.PollOnceDeleteMirror(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteMirror(MirrorName, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteMirror(MirrorName name, CallSettings callSettings = null)

Deletes a single mirror.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[MirrorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.MirrorName)`  
Required. Name of the mirror to delete, in the format: `projects/{project}/locations/{location}/instances/{instance}/mirrors/{mirror}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = LustreClient.Create();
    // Initialize request argument(s)
    MirrorName name = MirrorName.FromProjectLocationInstanceMirror("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[MIRROR]");
    // Make the request
    Operation<Empty, OperationMetadata> response = lustreClient.DeleteMirror(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = lustreClient.PollOnceDeleteMirror(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteMirror(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteMirror(string name, CallSettings callSettings = null)

Deletes a single mirror.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the mirror to delete, in the format: `projects/{project}/locations/{location}/instances/{instance}/mirrors/{mirror}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = LustreClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]/mirrors/[MIRROR]";
    // Make the request
    Operation<Empty, OperationMetadata> response = lustreClient.DeleteMirror(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = lustreClient.PollOnceDeleteMirror(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteMirrorAsync(DeleteMirrorRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteMirrorAsync(DeleteMirrorRequest request, CallSettings callSettings = null)

Deletes a single mirror.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteMirrorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.DeleteMirrorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    DeleteMirrorRequest request = new DeleteMirrorRequest
    {
        MirrorName = MirrorName.FromProjectLocationInstanceMirror("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[MIRROR]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await lustreClient.DeleteMirrorAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await lustreClient.PollOnceDeleteMirrorAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteMirrorAsync(DeleteMirrorRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteMirrorAsync(DeleteMirrorRequest request, CancellationToken cancellationToken)

Deletes a single mirror.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteMirrorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.DeleteMirrorRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    DeleteMirrorRequest request = new DeleteMirrorRequest
    {
        MirrorName = MirrorName.FromProjectLocationInstanceMirror("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[MIRROR]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await lustreClient.DeleteMirrorAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await lustreClient.PollOnceDeleteMirrorAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteMirrorAsync(MirrorName, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteMirrorAsync(MirrorName name, CallSettings callSettings = null)

Deletes a single mirror.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[MirrorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.MirrorName)`  
Required. Name of the mirror to delete, in the format: `projects/{project}/locations/{location}/instances/{instance}/mirrors/{mirror}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    MirrorName name = MirrorName.FromProjectLocationInstanceMirror("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[MIRROR]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await lustreClient.DeleteMirrorAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await lustreClient.PollOnceDeleteMirrorAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteMirrorAsync(MirrorName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteMirrorAsync(MirrorName name, CancellationToken cancellationToken)

Deletes a single mirror.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[MirrorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.MirrorName)`  
Required. Name of the mirror to delete, in the format: `projects/{project}/locations/{location}/instances/{instance}/mirrors/{mirror}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    MirrorName name = MirrorName.FromProjectLocationInstanceMirror("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[MIRROR]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await lustreClient.DeleteMirrorAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await lustreClient.PollOnceDeleteMirrorAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteMirrorAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteMirrorAsync(string name, CallSettings callSettings = null)

Deletes a single mirror.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the mirror to delete, in the format: `projects/{project}/locations/{location}/instances/{instance}/mirrors/{mirror}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]/mirrors/[MIRROR]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await lustreClient.DeleteMirrorAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await lustreClient.PollOnceDeleteMirrorAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteMirrorAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteMirrorAsync(string name, CancellationToken cancellationToken)

Deletes a single mirror.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the mirror to delete, in the format: `projects/{project}/locations/{location}/instances/{instance}/mirrors/{mirror}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]/mirrors/[MIRROR]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await lustreClient.DeleteMirrorAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await lustreClient.PollOnceDeleteMirrorAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### ExportData(ExportDataRequest, CallSettings)
    
    
    public virtual Operation<ExportDataResponse, ExportDataMetadata> ExportData(ExportDataRequest request, CallSettings callSettings = null)

Exports data from a Managed Lustre instance to Cloud Storage.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportDataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ExportDataRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportDataResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ExportDataResponse)[ExportDataMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ExportDataMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = LustreClient.Create();
    // Initialize request argument(s)
    ExportDataRequest request = new ExportDataRequest
    {
        InstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
        LustrePath = new LustrePath(),
        GcsPath = new GcsPath(),
        RequestId = "",
        ServiceAccountAsServiceAccountName = ServiceAccountName.FromProjectServiceAccount("[PROJECT]", "[SERVICE_ACCOUNT]"),
    };
    // Make the request
    Operation<ExportDataResponse, ExportDataMetadata> response = lustreClient.ExportData(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ExportDataResponse, ExportDataMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    ExportDataResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ExportDataResponse, ExportDataMetadata> retrievedResponse = lustreClient.PollOnceExportData(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ExportDataResponse retrievedResult = retrievedResponse.Result;
    }
    

### ExportDataAsync(ExportDataRequest, CallSettings)
    
    
    public virtual Task<Operation<ExportDataResponse, ExportDataMetadata>> ExportDataAsync(ExportDataRequest request, CallSettings callSettings = null)

Exports data from a Managed Lustre instance to Cloud Storage.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportDataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ExportDataRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportDataResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ExportDataResponse)[ExportDataMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ExportDataMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    ExportDataRequest request = new ExportDataRequest
    {
        InstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
        LustrePath = new LustrePath(),
        GcsPath = new GcsPath(),
        RequestId = "",
        ServiceAccountAsServiceAccountName = ServiceAccountName.FromProjectServiceAccount("[PROJECT]", "[SERVICE_ACCOUNT]"),
    };
    // Make the request
    Operation<ExportDataResponse, ExportDataMetadata> response = await lustreClient.ExportDataAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ExportDataResponse, ExportDataMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ExportDataResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ExportDataResponse, ExportDataMetadata> retrievedResponse = await lustreClient.PollOnceExportDataAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ExportDataResponse retrievedResult = retrievedResponse.Result;
    }
    

### ExportDataAsync(ExportDataRequest, CancellationToken)
    
    
    public virtual Task<Operation<ExportDataResponse, ExportDataMetadata>> ExportDataAsync(ExportDataRequest request, CancellationToken cancellationToken)

Exports data from a Managed Lustre instance to Cloud Storage.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportDataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ExportDataRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportDataResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ExportDataResponse)[ExportDataMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ExportDataMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    ExportDataRequest request = new ExportDataRequest
    {
        InstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
        LustrePath = new LustrePath(),
        GcsPath = new GcsPath(),
        RequestId = "",
        ServiceAccountAsServiceAccountName = ServiceAccountName.FromProjectServiceAccount("[PROJECT]", "[SERVICE_ACCOUNT]"),
    };
    // Make the request
    Operation<ExportDataResponse, ExportDataMetadata> response = await lustreClient.ExportDataAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ExportDataResponse, ExportDataMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ExportDataResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ExportDataResponse, ExportDataMetadata> retrievedResponse = await lustreClient.PollOnceExportDataAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ExportDataResponse retrievedResult = retrievedResponse.Result;
    }
    

### GetDirectoryPolicy(DirectoryPolicyName, CallSettings)
    
    
    public virtual DirectoryPolicy GetDirectoryPolicy(DirectoryPolicyName name, CallSettings callSettings = null)

Gets details of a single directory policy.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DirectoryPolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.DirectoryPolicyName)`  
Required. The resource name of the directory policy. DirectoryPolicy names have the form `projects/{project}/locations/{location}/instances/{instance}/directoryPolicies/{id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[DirectoryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.DirectoryPolicy)` | The RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = LustreClient.Create();
    // Initialize request argument(s)
    DirectoryPolicyName name = DirectoryPolicyName.FromProjectLocationInstanceDirectoryPolicy("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[DIRECTORY_POLICY]");
    // Make the request
    DirectoryPolicy response = lustreClient.GetDirectoryPolicy(name);
    

### GetDirectoryPolicy(GetDirectoryPolicyRequest, CallSettings)
    
    
    public virtual DirectoryPolicy GetDirectoryPolicy(GetDirectoryPolicyRequest request, CallSettings callSettings = null)

Gets details of a single directory policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDirectoryPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.GetDirectoryPolicyRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[DirectoryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.DirectoryPolicy)` | The RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = LustreClient.Create();
    // Initialize request argument(s)
    GetDirectoryPolicyRequest request = new GetDirectoryPolicyRequest
    {
        DirectoryPolicyName = DirectoryPolicyName.FromProjectLocationInstanceDirectoryPolicy("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[DIRECTORY_POLICY]"),
    };
    // Make the request
    DirectoryPolicy response = lustreClient.GetDirectoryPolicy(request);
    

### GetDirectoryPolicy(string, CallSettings)
    
    
    public virtual DirectoryPolicy GetDirectoryPolicy(string name, CallSettings callSettings = null)

Gets details of a single directory policy.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the directory policy. DirectoryPolicy names have the form `projects/{project}/locations/{location}/instances/{instance}/directoryPolicies/{id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[DirectoryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.DirectoryPolicy)` | The RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = LustreClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]/directoryPolicies/[DIRECTORY_POLICY]";
    // Make the request
    DirectoryPolicy response = lustreClient.GetDirectoryPolicy(name);
    

### GetDirectoryPolicyAsync(DirectoryPolicyName, CallSettings)
    
    
    public virtual Task<DirectoryPolicy> GetDirectoryPolicyAsync(DirectoryPolicyName name, CallSettings callSettings = null)

Gets details of a single directory policy.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DirectoryPolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.DirectoryPolicyName)`  
Required. The resource name of the directory policy. DirectoryPolicy names have the form `projects/{project}/locations/{location}/instances/{instance}/directoryPolicies/{id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DirectoryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.DirectoryPolicy)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    DirectoryPolicyName name = DirectoryPolicyName.FromProjectLocationInstanceDirectoryPolicy("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[DIRECTORY_POLICY]");
    // Make the request
    DirectoryPolicy response = await lustreClient.GetDirectoryPolicyAsync(name);
    

### GetDirectoryPolicyAsync(DirectoryPolicyName, CancellationToken)
    
    
    public virtual Task<DirectoryPolicy> GetDirectoryPolicyAsync(DirectoryPolicyName name, CancellationToken cancellationToken)

Gets details of a single directory policy.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DirectoryPolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.DirectoryPolicyName)`  
Required. The resource name of the directory policy. DirectoryPolicy names have the form `projects/{project}/locations/{location}/instances/{instance}/directoryPolicies/{id}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DirectoryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.DirectoryPolicy)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    DirectoryPolicyName name = DirectoryPolicyName.FromProjectLocationInstanceDirectoryPolicy("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[DIRECTORY_POLICY]");
    // Make the request
    DirectoryPolicy response = await lustreClient.GetDirectoryPolicyAsync(name);
    

### GetDirectoryPolicyAsync(GetDirectoryPolicyRequest, CallSettings)
    
    
    public virtual Task<DirectoryPolicy> GetDirectoryPolicyAsync(GetDirectoryPolicyRequest request, CallSettings callSettings = null)

Gets details of a single directory policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDirectoryPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.GetDirectoryPolicyRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DirectoryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.DirectoryPolicy)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    GetDirectoryPolicyRequest request = new GetDirectoryPolicyRequest
    {
        DirectoryPolicyName = DirectoryPolicyName.FromProjectLocationInstanceDirectoryPolicy("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[DIRECTORY_POLICY]"),
    };
    // Make the request
    DirectoryPolicy response = await lustreClient.GetDirectoryPolicyAsync(request);
    

### GetDirectoryPolicyAsync(GetDirectoryPolicyRequest, CancellationToken)
    
    
    public virtual Task<DirectoryPolicy> GetDirectoryPolicyAsync(GetDirectoryPolicyRequest request, CancellationToken cancellationToken)

Gets details of a single directory policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDirectoryPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.GetDirectoryPolicyRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DirectoryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.DirectoryPolicy)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    GetDirectoryPolicyRequest request = new GetDirectoryPolicyRequest
    {
        DirectoryPolicyName = DirectoryPolicyName.FromProjectLocationInstanceDirectoryPolicy("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[DIRECTORY_POLICY]"),
    };
    // Make the request
    DirectoryPolicy response = await lustreClient.GetDirectoryPolicyAsync(request);
    

### GetDirectoryPolicyAsync(string, CallSettings)
    
    
    public virtual Task<DirectoryPolicy> GetDirectoryPolicyAsync(string name, CallSettings callSettings = null)

Gets details of a single directory policy.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the directory policy. DirectoryPolicy names have the form `projects/{project}/locations/{location}/instances/{instance}/directoryPolicies/{id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DirectoryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.DirectoryPolicy)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]/directoryPolicies/[DIRECTORY_POLICY]";
    // Make the request
    DirectoryPolicy response = await lustreClient.GetDirectoryPolicyAsync(name);
    

### GetDirectoryPolicyAsync(string, CancellationToken)
    
    
    public virtual Task<DirectoryPolicy> GetDirectoryPolicyAsync(string name, CancellationToken cancellationToken)

Gets details of a single directory policy.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the directory policy. DirectoryPolicy names have the form `projects/{project}/locations/{location}/instances/{instance}/directoryPolicies/{id}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DirectoryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.DirectoryPolicy)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]/directoryPolicies/[DIRECTORY_POLICY]";
    // Make the request
    DirectoryPolicy response = await lustreClient.GetDirectoryPolicyAsync(name);
    

### GetInstance(GetInstanceRequest, CallSettings)
    
    
    public virtual Instance GetInstance(GetInstanceRequest request, CallSettings callSettings = null)

Gets details of a single instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.GetInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)` | The RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = LustreClient.Create();
    // Initialize request argument(s)
    GetInstanceRequest request = new GetInstanceRequest
    {
        InstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
    };
    // Make the request
    Instance response = lustreClient.GetInstance(request);
    

### GetInstance(InstanceName, CallSettings)
    
    
    public virtual Instance GetInstance(InstanceName name, CallSettings callSettings = null)

Gets details of a single instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.InstanceName)`  
Required. The instance resource name, in the format `projects/{projectId}/locations/{location}/instances/{instanceId}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)` | The RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = LustreClient.Create();
    // Initialize request argument(s)
    InstanceName name = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    // Make the request
    Instance response = lustreClient.GetInstance(name);
    

### GetInstance(string, CallSettings)
    
    
    public virtual Instance GetInstance(string name, CallSettings callSettings = null)

Gets details of a single instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The instance resource name, in the format `projects/{projectId}/locations/{location}/instances/{instanceId}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)` | The RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = LustreClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]";
    // Make the request
    Instance response = lustreClient.GetInstance(name);
    

### GetInstanceAsync(GetInstanceRequest, CallSettings)
    
    
    public virtual Task<Instance> GetInstanceAsync(GetInstanceRequest request, CallSettings callSettings = null)

Gets details of a single instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.GetInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    GetInstanceRequest request = new GetInstanceRequest
    {
        InstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
    };
    // Make the request
    Instance response = await lustreClient.GetInstanceAsync(request);
    

### GetInstanceAsync(GetInstanceRequest, CancellationToken)
    
    
    public virtual Task<Instance> GetInstanceAsync(GetInstanceRequest request, CancellationToken cancellationToken)

Gets details of a single instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.GetInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    GetInstanceRequest request = new GetInstanceRequest
    {
        InstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
    };
    // Make the request
    Instance response = await lustreClient.GetInstanceAsync(request);
    

### GetInstanceAsync(InstanceName, CallSettings)
    
    
    public virtual Task<Instance> GetInstanceAsync(InstanceName name, CallSettings callSettings = null)

Gets details of a single instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.InstanceName)`  
Required. The instance resource name, in the format `projects/{projectId}/locations/{location}/instances/{instanceId}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName name = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    // Make the request
    Instance response = await lustreClient.GetInstanceAsync(name);
    

### GetInstanceAsync(InstanceName, CancellationToken)
    
    
    public virtual Task<Instance> GetInstanceAsync(InstanceName name, CancellationToken cancellationToken)

Gets details of a single instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.InstanceName)`  
Required. The instance resource name, in the format `projects/{projectId}/locations/{location}/instances/{instanceId}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName name = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    // Make the request
    Instance response = await lustreClient.GetInstanceAsync(name);
    

### GetInstanceAsync(string, CallSettings)
    
    
    public virtual Task<Instance> GetInstanceAsync(string name, CallSettings callSettings = null)

Gets details of a single instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The instance resource name, in the format `projects/{projectId}/locations/{location}/instances/{instanceId}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]";
    // Make the request
    Instance response = await lustreClient.GetInstanceAsync(name);
    

### GetInstanceAsync(string, CancellationToken)
    
    
    public virtual Task<Instance> GetInstanceAsync(string name, CancellationToken cancellationToken)

Gets details of a single instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The instance resource name, in the format `projects/{projectId}/locations/{location}/instances/{instanceId}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]";
    // Make the request
    Instance response = await lustreClient.GetInstanceAsync(name);
    

### GetMirror(GetMirrorRequest, CallSettings)
    
    
    public virtual Mirror GetMirror(GetMirrorRequest request, CallSettings callSettings = null)

Gets details of a single mirror.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetMirrorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.GetMirrorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Mirror](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Mirror)` | The RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = LustreClient.Create();
    // Initialize request argument(s)
    GetMirrorRequest request = new GetMirrorRequest
    {
        MirrorName = MirrorName.FromProjectLocationInstanceMirror("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[MIRROR]"),
    };
    // Make the request
    Mirror response = lustreClient.GetMirror(request);
    

### GetMirror(MirrorName, CallSettings)
    
    
    public virtual Mirror GetMirror(MirrorName name, CallSettings callSettings = null)

Gets details of a single mirror.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[MirrorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.MirrorName)`  
Required. Name of the mirror to retrieve, in the format: `projects/{project}/locations/{location}/instances/{instance}/mirrors/{mirror}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Mirror](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Mirror)` | The RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = LustreClient.Create();
    // Initialize request argument(s)
    MirrorName name = MirrorName.FromProjectLocationInstanceMirror("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[MIRROR]");
    // Make the request
    Mirror response = lustreClient.GetMirror(name);
    

### GetMirror(string, CallSettings)
    
    
    public virtual Mirror GetMirror(string name, CallSettings callSettings = null)

Gets details of a single mirror.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the mirror to retrieve, in the format: `projects/{project}/locations/{location}/instances/{instance}/mirrors/{mirror}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Mirror](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Mirror)` | The RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = LustreClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]/mirrors/[MIRROR]";
    // Make the request
    Mirror response = lustreClient.GetMirror(name);
    

### GetMirrorAsync(GetMirrorRequest, CallSettings)
    
    
    public virtual Task<Mirror> GetMirrorAsync(GetMirrorRequest request, CallSettings callSettings = null)

Gets details of a single mirror.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetMirrorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.GetMirrorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Mirror](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Mirror)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    GetMirrorRequest request = new GetMirrorRequest
    {
        MirrorName = MirrorName.FromProjectLocationInstanceMirror("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[MIRROR]"),
    };
    // Make the request
    Mirror response = await lustreClient.GetMirrorAsync(request);
    

### GetMirrorAsync(GetMirrorRequest, CancellationToken)
    
    
    public virtual Task<Mirror> GetMirrorAsync(GetMirrorRequest request, CancellationToken cancellationToken)

Gets details of a single mirror.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetMirrorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.GetMirrorRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Mirror](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Mirror)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    GetMirrorRequest request = new GetMirrorRequest
    {
        MirrorName = MirrorName.FromProjectLocationInstanceMirror("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[MIRROR]"),
    };
    // Make the request
    Mirror response = await lustreClient.GetMirrorAsync(request);
    

### GetMirrorAsync(MirrorName, CallSettings)
    
    
    public virtual Task<Mirror> GetMirrorAsync(MirrorName name, CallSettings callSettings = null)

Gets details of a single mirror.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[MirrorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.MirrorName)`  
Required. Name of the mirror to retrieve, in the format: `projects/{project}/locations/{location}/instances/{instance}/mirrors/{mirror}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Mirror](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Mirror)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    MirrorName name = MirrorName.FromProjectLocationInstanceMirror("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[MIRROR]");
    // Make the request
    Mirror response = await lustreClient.GetMirrorAsync(name);
    

### GetMirrorAsync(MirrorName, CancellationToken)
    
    
    public virtual Task<Mirror> GetMirrorAsync(MirrorName name, CancellationToken cancellationToken)

Gets details of a single mirror.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[MirrorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.MirrorName)`  
Required. Name of the mirror to retrieve, in the format: `projects/{project}/locations/{location}/instances/{instance}/mirrors/{mirror}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Mirror](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Mirror)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    MirrorName name = MirrorName.FromProjectLocationInstanceMirror("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[MIRROR]");
    // Make the request
    Mirror response = await lustreClient.GetMirrorAsync(name);
    

### GetMirrorAsync(string, CallSettings)
    
    
    public virtual Task<Mirror> GetMirrorAsync(string name, CallSettings callSettings = null)

Gets details of a single mirror.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the mirror to retrieve, in the format: `projects/{project}/locations/{location}/instances/{instance}/mirrors/{mirror}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Mirror](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Mirror)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]/mirrors/[MIRROR]";
    // Make the request
    Mirror response = await lustreClient.GetMirrorAsync(name);
    

### GetMirrorAsync(string, CancellationToken)
    
    
    public virtual Task<Mirror> GetMirrorAsync(string name, CancellationToken cancellationToken)

Gets details of a single mirror.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the mirror to retrieve, in the format: `projects/{project}/locations/{location}/instances/{instance}/mirrors/{mirror}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Mirror](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Mirror)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]/mirrors/[MIRROR]";
    // Make the request
    Mirror response = await lustreClient.GetMirrorAsync(name);
    

### ImportData(ImportDataRequest, CallSettings)
    
    
    public virtual Operation<ImportDataResponse, ImportDataMetadata> ImportData(ImportDataRequest request, CallSettings callSettings = null)

Imports data from Cloud Storage to a Managed Lustre instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportDataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ImportDataRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportDataResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ImportDataResponse)[ImportDataMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ImportDataMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = LustreClient.Create();
    // Initialize request argument(s)
    ImportDataRequest request = new ImportDataRequest
    {
        InstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
        GcsPath = new GcsPath(),
        LustrePath = new LustrePath(),
        RequestId = "",
        ServiceAccountAsServiceAccountName = ServiceAccountName.FromProjectServiceAccount("[PROJECT]", "[SERVICE_ACCOUNT]"),
    };
    // Make the request
    Operation<ImportDataResponse, ImportDataMetadata> response = lustreClient.ImportData(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ImportDataResponse, ImportDataMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    ImportDataResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ImportDataResponse, ImportDataMetadata> retrievedResponse = lustreClient.PollOnceImportData(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ImportDataResponse retrievedResult = retrievedResponse.Result;
    }
    

### ImportData(InstanceName, CallSettings)
    
    
    public virtual Operation<ImportDataResponse, ImportDataMetadata> ImportData(InstanceName name, CallSettings callSettings = null)

Imports data from Cloud Storage to a Managed Lustre instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.InstanceName)`  
Required. The name of the Managed Lustre instance in the format `projects/{project}/locations/{location}/instances/{instance}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportDataResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ImportDataResponse)[ImportDataMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ImportDataMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = LustreClient.Create();
    // Initialize request argument(s)
    InstanceName name = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    // Make the request
    Operation<ImportDataResponse, ImportDataMetadata> response = lustreClient.ImportData(name);
    
    // Poll until the returned long-running operation is complete
    Operation<ImportDataResponse, ImportDataMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    ImportDataResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ImportDataResponse, ImportDataMetadata> retrievedResponse = lustreClient.PollOnceImportData(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ImportDataResponse retrievedResult = retrievedResponse.Result;
    }
    

### ImportData(string, CallSettings)
    
    
    public virtual Operation<ImportDataResponse, ImportDataMetadata> ImportData(string name, CallSettings callSettings = null)

Imports data from Cloud Storage to a Managed Lustre instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Managed Lustre instance in the format `projects/{project}/locations/{location}/instances/{instance}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportDataResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ImportDataResponse)[ImportDataMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ImportDataMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = LustreClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]";
    // Make the request
    Operation<ImportDataResponse, ImportDataMetadata> response = lustreClient.ImportData(name);
    
    // Poll until the returned long-running operation is complete
    Operation<ImportDataResponse, ImportDataMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    ImportDataResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ImportDataResponse, ImportDataMetadata> retrievedResponse = lustreClient.PollOnceImportData(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ImportDataResponse retrievedResult = retrievedResponse.Result;
    }
    

### ImportDataAsync(ImportDataRequest, CallSettings)
    
    
    public virtual Task<Operation<ImportDataResponse, ImportDataMetadata>> ImportDataAsync(ImportDataRequest request, CallSettings callSettings = null)

Imports data from Cloud Storage to a Managed Lustre instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportDataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ImportDataRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportDataResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ImportDataResponse)[ImportDataMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ImportDataMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    ImportDataRequest request = new ImportDataRequest
    {
        InstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
        GcsPath = new GcsPath(),
        LustrePath = new LustrePath(),
        RequestId = "",
        ServiceAccountAsServiceAccountName = ServiceAccountName.FromProjectServiceAccount("[PROJECT]", "[SERVICE_ACCOUNT]"),
    };
    // Make the request
    Operation<ImportDataResponse, ImportDataMetadata> response = await lustreClient.ImportDataAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ImportDataResponse, ImportDataMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ImportDataResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ImportDataResponse, ImportDataMetadata> retrievedResponse = await lustreClient.PollOnceImportDataAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ImportDataResponse retrievedResult = retrievedResponse.Result;
    }
    

### ImportDataAsync(ImportDataRequest, CancellationToken)
    
    
    public virtual Task<Operation<ImportDataResponse, ImportDataMetadata>> ImportDataAsync(ImportDataRequest request, CancellationToken cancellationToken)

Imports data from Cloud Storage to a Managed Lustre instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportDataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ImportDataRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportDataResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ImportDataResponse)[ImportDataMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ImportDataMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    ImportDataRequest request = new ImportDataRequest
    {
        InstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
        GcsPath = new GcsPath(),
        LustrePath = new LustrePath(),
        RequestId = "",
        ServiceAccountAsServiceAccountName = ServiceAccountName.FromProjectServiceAccount("[PROJECT]", "[SERVICE_ACCOUNT]"),
    };
    // Make the request
    Operation<ImportDataResponse, ImportDataMetadata> response = await lustreClient.ImportDataAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ImportDataResponse, ImportDataMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ImportDataResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ImportDataResponse, ImportDataMetadata> retrievedResponse = await lustreClient.PollOnceImportDataAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ImportDataResponse retrievedResult = retrievedResponse.Result;
    }
    

### ImportDataAsync(InstanceName, CallSettings)
    
    
    public virtual Task<Operation<ImportDataResponse, ImportDataMetadata>> ImportDataAsync(InstanceName name, CallSettings callSettings = null)

Imports data from Cloud Storage to a Managed Lustre instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.InstanceName)`  
Required. The name of the Managed Lustre instance in the format `projects/{project}/locations/{location}/instances/{instance}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportDataResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ImportDataResponse)[ImportDataMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ImportDataMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName name = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    // Make the request
    Operation<ImportDataResponse, ImportDataMetadata> response = await lustreClient.ImportDataAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<ImportDataResponse, ImportDataMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ImportDataResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ImportDataResponse, ImportDataMetadata> retrievedResponse = await lustreClient.PollOnceImportDataAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ImportDataResponse retrievedResult = retrievedResponse.Result;
    }
    

### ImportDataAsync(InstanceName, CancellationToken)
    
    
    public virtual Task<Operation<ImportDataResponse, ImportDataMetadata>> ImportDataAsync(InstanceName name, CancellationToken cancellationToken)

Imports data from Cloud Storage to a Managed Lustre instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.InstanceName)`  
Required. The name of the Managed Lustre instance in the format `projects/{project}/locations/{location}/instances/{instance}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportDataResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ImportDataResponse)[ImportDataMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ImportDataMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName name = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    // Make the request
    Operation<ImportDataResponse, ImportDataMetadata> response = await lustreClient.ImportDataAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<ImportDataResponse, ImportDataMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ImportDataResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ImportDataResponse, ImportDataMetadata> retrievedResponse = await lustreClient.PollOnceImportDataAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ImportDataResponse retrievedResult = retrievedResponse.Result;
    }
    

### ImportDataAsync(string, CallSettings)
    
    
    public virtual Task<Operation<ImportDataResponse, ImportDataMetadata>> ImportDataAsync(string name, CallSettings callSettings = null)

Imports data from Cloud Storage to a Managed Lustre instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Managed Lustre instance in the format `projects/{project}/locations/{location}/instances/{instance}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportDataResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ImportDataResponse)[ImportDataMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ImportDataMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]";
    // Make the request
    Operation<ImportDataResponse, ImportDataMetadata> response = await lustreClient.ImportDataAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<ImportDataResponse, ImportDataMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ImportDataResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ImportDataResponse, ImportDataMetadata> retrievedResponse = await lustreClient.PollOnceImportDataAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ImportDataResponse retrievedResult = retrievedResponse.Result;
    }
    

### ImportDataAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<ImportDataResponse, ImportDataMetadata>> ImportDataAsync(string name, CancellationToken cancellationToken)

Imports data from Cloud Storage to a Managed Lustre instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Managed Lustre instance in the format `projects/{project}/locations/{location}/instances/{instance}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportDataResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ImportDataResponse)[ImportDataMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ImportDataMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]";
    // Make the request
    Operation<ImportDataResponse, ImportDataMetadata> response = await lustreClient.ImportDataAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<ImportDataResponse, ImportDataMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ImportDataResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ImportDataResponse, ImportDataMetadata> retrievedResponse = await lustreClient.PollOnceImportDataAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ImportDataResponse retrievedResult = retrievedResponse.Result;
    }
    

### ListDirectoryPolicies(InstanceName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListDirectoryPoliciesResponse, DirectoryPolicy> ListDirectoryPolicies(InstanceName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Gets details of multiple directory policies under a given instance.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.InstanceName)`  
Required. The parent instance. It must be in the format of `projects/{project}/locations/{location}/instances/{instance}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListDirectoryPoliciesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ListDirectoryPoliciesResponse)[DirectoryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.DirectoryPolicy)` | A pageable sequence of [DirectoryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.DirectoryPolicy) resources.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = LustreClient.Create();
    // Initialize request argument(s)
    InstanceName parent = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    // Make the request
    PagedEnumerable<ListDirectoryPoliciesResponse, DirectoryPolicy> response = lustreClient.ListDirectoryPolicies(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (DirectoryPolicy item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListDirectoryPoliciesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (DirectoryPolicy item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<DirectoryPolicy> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (DirectoryPolicy item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDirectoryPolicies(ListDirectoryPoliciesRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListDirectoryPoliciesResponse, DirectoryPolicy> ListDirectoryPolicies(ListDirectoryPoliciesRequest request, CallSettings callSettings = null)

Gets details of multiple directory policies under a given instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDirectoryPoliciesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ListDirectoryPoliciesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListDirectoryPoliciesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ListDirectoryPoliciesResponse)[DirectoryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.DirectoryPolicy)` | A pageable sequence of [DirectoryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.DirectoryPolicy) resources.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = LustreClient.Create();
    // Initialize request argument(s)
    ListDirectoryPoliciesRequest request = new ListDirectoryPoliciesRequest
    {
        ParentAsInstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
    };
    // Make the request
    PagedEnumerable<ListDirectoryPoliciesResponse, DirectoryPolicy> response = lustreClient.ListDirectoryPolicies(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (DirectoryPolicy item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListDirectoryPoliciesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (DirectoryPolicy item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<DirectoryPolicy> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (DirectoryPolicy item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDirectoryPolicies(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListDirectoryPoliciesResponse, DirectoryPolicy> ListDirectoryPolicies(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Gets details of multiple directory policies under a given instance.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent instance. It must be in the format of `projects/{project}/locations/{location}/instances/{instance}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListDirectoryPoliciesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ListDirectoryPoliciesResponse)[DirectoryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.DirectoryPolicy)` | A pageable sequence of [DirectoryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.DirectoryPolicy) resources.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = LustreClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]";
    // Make the request
    PagedEnumerable<ListDirectoryPoliciesResponse, DirectoryPolicy> response = lustreClient.ListDirectoryPolicies(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (DirectoryPolicy item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListDirectoryPoliciesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (DirectoryPolicy item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<DirectoryPolicy> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (DirectoryPolicy item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDirectoryPoliciesAsync(InstanceName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListDirectoryPoliciesResponse, DirectoryPolicy> ListDirectoryPoliciesAsync(InstanceName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Gets details of multiple directory policies under a given instance.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.InstanceName)`  
Required. The parent instance. It must be in the format of `projects/{project}/locations/{location}/instances/{instance}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListDirectoryPoliciesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ListDirectoryPoliciesResponse)[DirectoryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.DirectoryPolicy)` | A pageable asynchronous sequence of [DirectoryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.DirectoryPolicy) resources.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName parent = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    // Make the request
    PagedAsyncEnumerable<ListDirectoryPoliciesResponse, DirectoryPolicy> response = lustreClient.ListDirectoryPoliciesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (DirectoryPolicy item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListDirectoryPoliciesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (DirectoryPolicy item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<DirectoryPolicy> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (DirectoryPolicy item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDirectoryPoliciesAsync(ListDirectoryPoliciesRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListDirectoryPoliciesResponse, DirectoryPolicy> ListDirectoryPoliciesAsync(ListDirectoryPoliciesRequest request, CallSettings callSettings = null)

Gets details of multiple directory policies under a given instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDirectoryPoliciesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ListDirectoryPoliciesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListDirectoryPoliciesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ListDirectoryPoliciesResponse)[DirectoryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.DirectoryPolicy)` | A pageable asynchronous sequence of [DirectoryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.DirectoryPolicy) resources.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    ListDirectoryPoliciesRequest request = new ListDirectoryPoliciesRequest
    {
        ParentAsInstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
    };
    // Make the request
    PagedAsyncEnumerable<ListDirectoryPoliciesResponse, DirectoryPolicy> response = lustreClient.ListDirectoryPoliciesAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (DirectoryPolicy item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListDirectoryPoliciesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (DirectoryPolicy item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<DirectoryPolicy> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (DirectoryPolicy item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDirectoryPoliciesAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListDirectoryPoliciesResponse, DirectoryPolicy> ListDirectoryPoliciesAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Gets details of multiple directory policies under a given instance.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent instance. It must be in the format of `projects/{project}/locations/{location}/instances/{instance}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListDirectoryPoliciesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ListDirectoryPoliciesResponse)[DirectoryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.DirectoryPolicy)` | A pageable asynchronous sequence of [DirectoryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.DirectoryPolicy) resources.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]";
    // Make the request
    PagedAsyncEnumerable<ListDirectoryPoliciesResponse, DirectoryPolicy> response = lustreClient.ListDirectoryPoliciesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (DirectoryPolicy item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListDirectoryPoliciesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (DirectoryPolicy item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<DirectoryPolicy> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (DirectoryPolicy item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListInstances(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListInstancesResponse, Instance> ListInstances(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists instances in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The project and location for which to retrieve a list of instances, in the format `projects/{projectId}/locations/{location}`. To retrieve instance information for all locations, use "-" as the value of `{location}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ListInstancesResponse)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)` | A pageable sequence of [Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance) resources.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = LustreClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListInstancesResponse, Instance> response = lustreClient.ListInstances(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Instance item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListInstancesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Instance item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Instance> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Instance item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListInstances(ListInstancesRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListInstancesResponse, Instance> ListInstances(ListInstancesRequest request, CallSettings callSettings = null)

Lists instances in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ListInstancesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ListInstancesResponse)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)` | A pageable sequence of [Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance) resources.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = LustreClient.Create();
    // Initialize request argument(s)
    ListInstancesRequest request = new ListInstancesRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListInstancesResponse, Instance> response = lustreClient.ListInstances(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Instance item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListInstancesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Instance item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Instance> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Instance item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListInstances(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListInstancesResponse, Instance> ListInstances(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists instances in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The project and location for which to retrieve a list of instances, in the format `projects/{projectId}/locations/{location}`. To retrieve instance information for all locations, use "-" as the value of `{location}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ListInstancesResponse)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)` | A pageable sequence of [Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance) resources.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = LustreClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListInstancesResponse, Instance> response = lustreClient.ListInstances(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Instance item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListInstancesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Instance item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Instance> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Instance item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListInstancesAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListInstancesResponse, Instance> ListInstancesAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists instances in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The project and location for which to retrieve a list of instances, in the format `projects/{projectId}/locations/{location}`. To retrieve instance information for all locations, use "-" as the value of `{location}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ListInstancesResponse)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)` | A pageable asynchronous sequence of [Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance) resources.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListInstancesResponse, Instance> response = lustreClient.ListInstancesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Instance item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListInstancesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Instance item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Instance> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Instance item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListInstancesAsync(ListInstancesRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListInstancesResponse, Instance> ListInstancesAsync(ListInstancesRequest request, CallSettings callSettings = null)

Lists instances in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ListInstancesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ListInstancesResponse)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)` | A pageable asynchronous sequence of [Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance) resources.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    ListInstancesRequest request = new ListInstancesRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListInstancesResponse, Instance> response = lustreClient.ListInstancesAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Instance item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListInstancesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Instance item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Instance> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Instance item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListInstancesAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListInstancesResponse, Instance> ListInstancesAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists instances in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The project and location for which to retrieve a list of instances, in the format `projects/{projectId}/locations/{location}`. To retrieve instance information for all locations, use "-" as the value of `{location}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ListInstancesResponse)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)` | A pageable asynchronous sequence of [Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance) resources.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListInstancesResponse, Instance> response = lustreClient.ListInstancesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Instance item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListInstancesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Instance item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Instance> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Instance item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListMirrors(InstanceName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListMirrorsResponse, Mirror> ListMirrors(InstanceName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Gets details of multiple mirrors under a given instance.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.InstanceName)`  
Required. Parent instance resource where the mirrors will be listed, in the format: `projects/{project}/locations/{location}/instances/{instance}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListMirrorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ListMirrorsResponse)[Mirror](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Mirror)` | A pageable sequence of [Mirror](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Mirror) resources.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = LustreClient.Create();
    // Initialize request argument(s)
    InstanceName parent = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    // Make the request
    PagedEnumerable<ListMirrorsResponse, Mirror> response = lustreClient.ListMirrors(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Mirror item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListMirrorsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Mirror item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Mirror> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Mirror item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListMirrors(ListMirrorsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListMirrorsResponse, Mirror> ListMirrors(ListMirrorsRequest request, CallSettings callSettings = null)

Gets details of multiple mirrors under a given instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListMirrorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ListMirrorsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListMirrorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ListMirrorsResponse)[Mirror](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Mirror)` | A pageable sequence of [Mirror](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Mirror) resources.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = LustreClient.Create();
    // Initialize request argument(s)
    ListMirrorsRequest request = new ListMirrorsRequest
    {
        ParentAsInstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
        OrderBy = "",
        Filter = "",
    };
    // Make the request
    PagedEnumerable<ListMirrorsResponse, Mirror> response = lustreClient.ListMirrors(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Mirror item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListMirrorsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Mirror item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Mirror> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Mirror item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListMirrors(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListMirrorsResponse, Mirror> ListMirrors(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Gets details of multiple mirrors under a given instance.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Parent instance resource where the mirrors will be listed, in the format: `projects/{project}/locations/{location}/instances/{instance}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListMirrorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ListMirrorsResponse)[Mirror](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Mirror)` | A pageable sequence of [Mirror](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Mirror) resources.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = LustreClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]";
    // Make the request
    PagedEnumerable<ListMirrorsResponse, Mirror> response = lustreClient.ListMirrors(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Mirror item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListMirrorsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Mirror item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Mirror> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Mirror item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListMirrorsAsync(InstanceName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListMirrorsResponse, Mirror> ListMirrorsAsync(InstanceName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Gets details of multiple mirrors under a given instance.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.InstanceName)`  
Required. Parent instance resource where the mirrors will be listed, in the format: `projects/{project}/locations/{location}/instances/{instance}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListMirrorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ListMirrorsResponse)[Mirror](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Mirror)` | A pageable asynchronous sequence of [Mirror](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Mirror) resources.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName parent = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    // Make the request
    PagedAsyncEnumerable<ListMirrorsResponse, Mirror> response = lustreClient.ListMirrorsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Mirror item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListMirrorsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Mirror item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Mirror> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Mirror item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListMirrorsAsync(ListMirrorsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListMirrorsResponse, Mirror> ListMirrorsAsync(ListMirrorsRequest request, CallSettings callSettings = null)

Gets details of multiple mirrors under a given instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListMirrorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ListMirrorsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListMirrorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ListMirrorsResponse)[Mirror](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Mirror)` | A pageable asynchronous sequence of [Mirror](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Mirror) resources.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    ListMirrorsRequest request = new ListMirrorsRequest
    {
        ParentAsInstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
        OrderBy = "",
        Filter = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListMirrorsResponse, Mirror> response = lustreClient.ListMirrorsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Mirror item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListMirrorsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Mirror item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Mirror> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Mirror item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListMirrorsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListMirrorsResponse, Mirror> ListMirrorsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Gets details of multiple mirrors under a given instance.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Parent instance resource where the mirrors will be listed, in the format: `projects/{project}/locations/{location}/instances/{instance}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListMirrorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ListMirrorsResponse)[Mirror](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Mirror)` | A pageable asynchronous sequence of [Mirror](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Mirror) resources.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]";
    // Make the request
    PagedAsyncEnumerable<ListMirrorsResponse, Mirror> response = lustreClient.ListMirrorsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Mirror item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListMirrorsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Mirror item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Mirror> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Mirror item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### PollOnceCreateDirectoryPolicy(string, CallSettings)
    
    
    public virtual Operation<DirectoryPolicy, OperationMetadata> PollOnceCreateDirectoryPolicy(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateDirectoryPolicy` .

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DirectoryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.DirectoryPolicy)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceCreateDirectoryPolicyAsync(string, CallSettings)
    
    
    public virtual Task<Operation<DirectoryPolicy, OperationMetadata>> PollOnceCreateDirectoryPolicyAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateDirectoryPolicy`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DirectoryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.DirectoryPolicy)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceCreateInstance(string, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> PollOnceCreateInstance(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateInstance`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceCreateInstanceAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> PollOnceCreateInstanceAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateInstance`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceCreateMirror(string, CallSettings)
    
    
    public virtual Operation<Mirror, CreateMirrorMetadata> PollOnceCreateMirror(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateMirror`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Mirror](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Mirror)[CreateMirrorMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.CreateMirrorMetadata)` | The result of polling the operation.  
  
### PollOnceCreateMirrorAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Mirror, CreateMirrorMetadata>> PollOnceCreateMirrorAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateMirror`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Mirror](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Mirror)[CreateMirrorMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.CreateMirrorMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteDirectoryPolicy(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> PollOnceDeleteDirectoryPolicy(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteDirectoryPolicy` .

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteDirectoryPolicyAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> PollOnceDeleteDirectoryPolicyAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteDirectoryPolicy`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteInstance(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> PollOnceDeleteInstance(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteInstance`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteInstanceAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> PollOnceDeleteInstanceAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteInstance`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteMirror(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> PollOnceDeleteMirror(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteMirror`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteMirrorAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> PollOnceDeleteMirrorAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteMirror`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceExportData(string, CallSettings)
    
    
    public virtual Operation<ExportDataResponse, ExportDataMetadata> PollOnceExportData(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `ExportData`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportDataResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ExportDataResponse)[ExportDataMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ExportDataMetadata)` | The result of polling the operation.  
  
### PollOnceExportDataAsync(string, CallSettings)
    
    
    public virtual Task<Operation<ExportDataResponse, ExportDataMetadata>> PollOnceExportDataAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `ExportData`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportDataResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ExportDataResponse)[ExportDataMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ExportDataMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceImportData(string, CallSettings)
    
    
    public virtual Operation<ImportDataResponse, ImportDataMetadata> PollOnceImportData(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `ImportData`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportDataResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ImportDataResponse)[ImportDataMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ImportDataMetadata)` | The result of polling the operation.  
  
### PollOnceImportDataAsync(string, CallSettings)
    
    
    public virtual Task<Operation<ImportDataResponse, ImportDataMetadata>> PollOnceImportDataAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `ImportData`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportDataResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ImportDataResponse)[ImportDataMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ImportDataMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceRescheduleMaintenance(string, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> PollOnceRescheduleMaintenance(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `RescheduleMaintenance` .

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceRescheduleMaintenanceAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> PollOnceRescheduleMaintenanceAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `RescheduleMaintenance`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceUpdateInstance(string, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> PollOnceUpdateInstance(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `UpdateInstance`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceUpdateInstanceAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> PollOnceUpdateInstanceAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `UpdateInstance`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceUpdateMirror(string, CallSettings)
    
    
    public virtual Operation<Mirror, OperationMetadata> PollOnceUpdateMirror(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `UpdateMirror`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Mirror](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Mirror)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceUpdateMirrorAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Mirror, OperationMetadata>> PollOnceUpdateMirrorAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `UpdateMirror`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Mirror](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Mirror)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### RescheduleMaintenance(InstanceName, Reschedule, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> RescheduleMaintenance(InstanceName name, RescheduleMaintenanceRequest.Types.Reschedule reschedule, CallSettings callSettings = null)

Reschedules a planned maintenance event for a specific instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.InstanceName)`  
Required. Format: projects/{project}/locations/{location}/instances/{instance}  
`reschedule` | `[RescheduleMaintenanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.RescheduleMaintenanceRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.RescheduleMaintenanceRequest.Types)[Reschedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.RescheduleMaintenanceRequest.Types.Reschedule)`  
Required. The desired reschedule settings.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = LustreClient.Create();
    // Initialize request argument(s)
    InstanceName name = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    RescheduleMaintenanceRequest.Types.Reschedule reschedule = new RescheduleMaintenanceRequest.Types.Reschedule();
    // Make the request
    Operation<Instance, OperationMetadata> response = lustreClient.RescheduleMaintenance(name, reschedule);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = lustreClient.PollOnceRescheduleMaintenance(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### RescheduleMaintenance(RescheduleMaintenanceRequest, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> RescheduleMaintenance(RescheduleMaintenanceRequest request, CallSettings callSettings = null)

Reschedules a planned maintenance event for a specific instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RescheduleMaintenanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.RescheduleMaintenanceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = LustreClient.Create();
    // Initialize request argument(s)
    RescheduleMaintenanceRequest request = new RescheduleMaintenanceRequest
    {
        InstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
        Reschedule = new RescheduleMaintenanceRequest.Types.Reschedule(),
        RequestId = "",
    };
    // Make the request
    Operation<Instance, OperationMetadata> response = lustreClient.RescheduleMaintenance(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = lustreClient.PollOnceRescheduleMaintenance(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### RescheduleMaintenance(string, Reschedule, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> RescheduleMaintenance(string name, RescheduleMaintenanceRequest.Types.Reschedule reschedule, CallSettings callSettings = null)

Reschedules a planned maintenance event for a specific instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Format: projects/{project}/locations/{location}/instances/{instance}  
`reschedule` | `[RescheduleMaintenanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.RescheduleMaintenanceRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.RescheduleMaintenanceRequest.Types)[Reschedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.RescheduleMaintenanceRequest.Types.Reschedule)`  
Required. The desired reschedule settings.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = LustreClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]";
    RescheduleMaintenanceRequest.Types.Reschedule reschedule = new RescheduleMaintenanceRequest.Types.Reschedule();
    // Make the request
    Operation<Instance, OperationMetadata> response = lustreClient.RescheduleMaintenance(name, reschedule);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = lustreClient.PollOnceRescheduleMaintenance(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### RescheduleMaintenanceAsync(InstanceName, Reschedule, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> RescheduleMaintenanceAsync(InstanceName name, RescheduleMaintenanceRequest.Types.Reschedule reschedule, CallSettings callSettings = null)

Reschedules a planned maintenance event for a specific instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.InstanceName)`  
Required. Format: projects/{project}/locations/{location}/instances/{instance}  
`reschedule` | `[RescheduleMaintenanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.RescheduleMaintenanceRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.RescheduleMaintenanceRequest.Types)[Reschedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.RescheduleMaintenanceRequest.Types.Reschedule)`  
Required. The desired reschedule settings.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName name = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    RescheduleMaintenanceRequest.Types.Reschedule reschedule = new RescheduleMaintenanceRequest.Types.Reschedule();
    // Make the request
    Operation<Instance, OperationMetadata> response = await lustreClient.RescheduleMaintenanceAsync(name, reschedule);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await lustreClient.PollOnceRescheduleMaintenanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### RescheduleMaintenanceAsync(InstanceName, Reschedule, CancellationToken)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> RescheduleMaintenanceAsync(InstanceName name, RescheduleMaintenanceRequest.Types.Reschedule reschedule, CancellationToken cancellationToken)

Reschedules a planned maintenance event for a specific instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.InstanceName)`  
Required. Format: projects/{project}/locations/{location}/instances/{instance}  
`reschedule` | `[RescheduleMaintenanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.RescheduleMaintenanceRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.RescheduleMaintenanceRequest.Types)[Reschedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.RescheduleMaintenanceRequest.Types.Reschedule)`  
Required. The desired reschedule settings.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName name = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    RescheduleMaintenanceRequest.Types.Reschedule reschedule = new RescheduleMaintenanceRequest.Types.Reschedule();
    // Make the request
    Operation<Instance, OperationMetadata> response = await lustreClient.RescheduleMaintenanceAsync(name, reschedule);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await lustreClient.PollOnceRescheduleMaintenanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### RescheduleMaintenanceAsync(RescheduleMaintenanceRequest, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> RescheduleMaintenanceAsync(RescheduleMaintenanceRequest request, CallSettings callSettings = null)

Reschedules a planned maintenance event for a specific instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RescheduleMaintenanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.RescheduleMaintenanceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    RescheduleMaintenanceRequest request = new RescheduleMaintenanceRequest
    {
        InstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
        Reschedule = new RescheduleMaintenanceRequest.Types.Reschedule(),
        RequestId = "",
    };
    // Make the request
    Operation<Instance, OperationMetadata> response = await lustreClient.RescheduleMaintenanceAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await lustreClient.PollOnceRescheduleMaintenanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### RescheduleMaintenanceAsync(RescheduleMaintenanceRequest, CancellationToken)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> RescheduleMaintenanceAsync(RescheduleMaintenanceRequest request, CancellationToken cancellationToken)

Reschedules a planned maintenance event for a specific instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RescheduleMaintenanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.RescheduleMaintenanceRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    RescheduleMaintenanceRequest request = new RescheduleMaintenanceRequest
    {
        InstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
        Reschedule = new RescheduleMaintenanceRequest.Types.Reschedule(),
        RequestId = "",
    };
    // Make the request
    Operation<Instance, OperationMetadata> response = await lustreClient.RescheduleMaintenanceAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await lustreClient.PollOnceRescheduleMaintenanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### RescheduleMaintenanceAsync(string, Reschedule, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> RescheduleMaintenanceAsync(string name, RescheduleMaintenanceRequest.Types.Reschedule reschedule, CallSettings callSettings = null)

Reschedules a planned maintenance event for a specific instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Format: projects/{project}/locations/{location}/instances/{instance}  
`reschedule` | `[RescheduleMaintenanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.RescheduleMaintenanceRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.RescheduleMaintenanceRequest.Types)[Reschedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.RescheduleMaintenanceRequest.Types.Reschedule)`  
Required. The desired reschedule settings.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]";
    RescheduleMaintenanceRequest.Types.Reschedule reschedule = new RescheduleMaintenanceRequest.Types.Reschedule();
    // Make the request
    Operation<Instance, OperationMetadata> response = await lustreClient.RescheduleMaintenanceAsync(name, reschedule);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await lustreClient.PollOnceRescheduleMaintenanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### RescheduleMaintenanceAsync(string, Reschedule, CancellationToken)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> RescheduleMaintenanceAsync(string name, RescheduleMaintenanceRequest.Types.Reschedule reschedule, CancellationToken cancellationToken)

Reschedules a planned maintenance event for a specific instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Format: projects/{project}/locations/{location}/instances/{instance}  
`reschedule` | `[RescheduleMaintenanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.RescheduleMaintenanceRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.RescheduleMaintenanceRequest.Types)[Reschedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.RescheduleMaintenanceRequest.Types.Reschedule)`  
Required. The desired reschedule settings.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]";
    RescheduleMaintenanceRequest.Types.Reschedule reschedule = new RescheduleMaintenanceRequest.Types.Reschedule();
    // Make the request
    Operation<Instance, OperationMetadata> response = await lustreClient.RescheduleMaintenanceAsync(name, reschedule);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await lustreClient.PollOnceRescheduleMaintenanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.LustreClient#Google_Cloud_Lustre_V1_LustreClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.LustreClient#Google_Cloud_Lustre_V1_LustreClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.LustreClient#Google_Cloud_Lustre_V1_LustreClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.LustreClient#Google_Cloud_Lustre_V1_LustreClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### UpdateInstance(Instance, FieldMask, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> UpdateInstance(Instance instance, FieldMask updateMask, CallSettings callSettings = null)

Updates the parameters of a single instance.

**Parameters**  
---  
**Name** | **Description**  
`instance` | `[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)`  
Required. The resource name of the instance to update, in the format `projects/{projectId}/locations/{location}/instances/{instanceId}`.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Specifies the fields to be overwritten in the instance resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If no mask is provided then all fields present in the request are overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = LustreClient.Create();
    // Initialize request argument(s)
    Instance instance = new Instance();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Instance, OperationMetadata> response = lustreClient.UpdateInstance(instance, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = lustreClient.PollOnceUpdateInstance(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### UpdateInstance(UpdateInstanceRequest, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> UpdateInstance(UpdateInstanceRequest request, CallSettings callSettings = null)

Updates the parameters of a single instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.UpdateInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = LustreClient.Create();
    // Initialize request argument(s)
    UpdateInstanceRequest request = new UpdateInstanceRequest
    {
        UpdateMask = new FieldMask(),
        Instance = new Instance(),
        RequestId = "",
    };
    // Make the request
    Operation<Instance, OperationMetadata> response = lustreClient.UpdateInstance(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = lustreClient.PollOnceUpdateInstance(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### UpdateInstanceAsync(Instance, FieldMask, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> UpdateInstanceAsync(Instance instance, FieldMask updateMask, CallSettings callSettings = null)

Updates the parameters of a single instance.

**Parameters**  
---  
**Name** | **Description**  
`instance` | `[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)`  
Required. The resource name of the instance to update, in the format `projects/{projectId}/locations/{location}/instances/{instanceId}`.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Specifies the fields to be overwritten in the instance resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If no mask is provided then all fields present in the request are overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    Instance instance = new Instance();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Instance, OperationMetadata> response = await lustreClient.UpdateInstanceAsync(instance, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await lustreClient.PollOnceUpdateInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### UpdateInstanceAsync(Instance, FieldMask, CancellationToken)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> UpdateInstanceAsync(Instance instance, FieldMask updateMask, CancellationToken cancellationToken)

Updates the parameters of a single instance.

**Parameters**  
---  
**Name** | **Description**  
`instance` | `[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)`  
Required. The resource name of the instance to update, in the format `projects/{projectId}/locations/{location}/instances/{instanceId}`.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Specifies the fields to be overwritten in the instance resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If no mask is provided then all fields present in the request are overwritten.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    Instance instance = new Instance();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Instance, OperationMetadata> response = await lustreClient.UpdateInstanceAsync(instance, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await lustreClient.PollOnceUpdateInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### UpdateInstanceAsync(UpdateInstanceRequest, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> UpdateInstanceAsync(UpdateInstanceRequest request, CallSettings callSettings = null)

Updates the parameters of a single instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.UpdateInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    UpdateInstanceRequest request = new UpdateInstanceRequest
    {
        UpdateMask = new FieldMask(),
        Instance = new Instance(),
        RequestId = "",
    };
    // Make the request
    Operation<Instance, OperationMetadata> response = await lustreClient.UpdateInstanceAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await lustreClient.PollOnceUpdateInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### UpdateInstanceAsync(UpdateInstanceRequest, CancellationToken)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> UpdateInstanceAsync(UpdateInstanceRequest request, CancellationToken cancellationToken)

Updates the parameters of a single instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.UpdateInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    UpdateInstanceRequest request = new UpdateInstanceRequest
    {
        UpdateMask = new FieldMask(),
        Instance = new Instance(),
        RequestId = "",
    };
    // Make the request
    Operation<Instance, OperationMetadata> response = await lustreClient.UpdateInstanceAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await lustreClient.PollOnceUpdateInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### UpdateMirror(Mirror, FieldMask, CallSettings)
    
    
    public virtual Operation<Mirror, OperationMetadata> UpdateMirror(Mirror mirror, FieldMask updateMask, CallSettings callSettings = null)

Updates the parameters of a single mirror.

**Parameters**  
---  
**Name** | **Description**  
`mirror` | `[Mirror](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Mirror)`  
Required. Mirror to update. The mirror's `name` field is used to identify the mirror to update, in the format: `projects/{project}/locations/{location}/instances/{instance}/mirrors/{mirror}`  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If no mask is provided then all fields present in the request are overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Mirror](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Mirror)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = LustreClient.Create();
    // Initialize request argument(s)
    Mirror mirror = new Mirror();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Mirror, OperationMetadata> response = lustreClient.UpdateMirror(mirror, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Mirror, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Mirror result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Mirror, OperationMetadata> retrievedResponse = lustreClient.PollOnceUpdateMirror(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Mirror retrievedResult = retrievedResponse.Result;
    }
    

### UpdateMirror(UpdateMirrorRequest, CallSettings)
    
    
    public virtual Operation<Mirror, OperationMetadata> UpdateMirror(UpdateMirrorRequest request, CallSettings callSettings = null)

Updates the parameters of a single mirror.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateMirrorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.UpdateMirrorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Mirror](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Mirror)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = LustreClient.Create();
    // Initialize request argument(s)
    UpdateMirrorRequest request = new UpdateMirrorRequest
    {
        Mirror = new Mirror(),
        UpdateMask = new FieldMask(),
        RequestId = "",
    };
    // Make the request
    Operation<Mirror, OperationMetadata> response = lustreClient.UpdateMirror(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Mirror, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Mirror result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Mirror, OperationMetadata> retrievedResponse = lustreClient.PollOnceUpdateMirror(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Mirror retrievedResult = retrievedResponse.Result;
    }
    

### UpdateMirrorAsync(Mirror, FieldMask, CallSettings)
    
    
    public virtual Task<Operation<Mirror, OperationMetadata>> UpdateMirrorAsync(Mirror mirror, FieldMask updateMask, CallSettings callSettings = null)

Updates the parameters of a single mirror.

**Parameters**  
---  
**Name** | **Description**  
`mirror` | `[Mirror](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Mirror)`  
Required. Mirror to update. The mirror's `name` field is used to identify the mirror to update, in the format: `projects/{project}/locations/{location}/instances/{instance}/mirrors/{mirror}`  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If no mask is provided then all fields present in the request are overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Mirror](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Mirror)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    Mirror mirror = new Mirror();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Mirror, OperationMetadata> response = await lustreClient.UpdateMirrorAsync(mirror, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Mirror, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Mirror result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Mirror, OperationMetadata> retrievedResponse = await lustreClient.PollOnceUpdateMirrorAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Mirror retrievedResult = retrievedResponse.Result;
    }
    

### UpdateMirrorAsync(Mirror, FieldMask, CancellationToken)
    
    
    public virtual Task<Operation<Mirror, OperationMetadata>> UpdateMirrorAsync(Mirror mirror, FieldMask updateMask, CancellationToken cancellationToken)

Updates the parameters of a single mirror.

**Parameters**  
---  
**Name** | **Description**  
`mirror` | `[Mirror](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Mirror)`  
Required. Mirror to update. The mirror's `name` field is used to identify the mirror to update, in the format: `projects/{project}/locations/{location}/instances/{instance}/mirrors/{mirror}`  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If no mask is provided then all fields present in the request are overwritten.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Mirror](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Mirror)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    Mirror mirror = new Mirror();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Mirror, OperationMetadata> response = await lustreClient.UpdateMirrorAsync(mirror, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Mirror, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Mirror result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Mirror, OperationMetadata> retrievedResponse = await lustreClient.PollOnceUpdateMirrorAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Mirror retrievedResult = retrievedResponse.Result;
    }
    

### UpdateMirrorAsync(UpdateMirrorRequest, CallSettings)
    
    
    public virtual Task<Operation<Mirror, OperationMetadata>> UpdateMirrorAsync(UpdateMirrorRequest request, CallSettings callSettings = null)

Updates the parameters of a single mirror.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateMirrorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.UpdateMirrorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Mirror](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Mirror)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    UpdateMirrorRequest request = new UpdateMirrorRequest
    {
        Mirror = new Mirror(),
        UpdateMask = new FieldMask(),
        RequestId = "",
    };
    // Make the request
    Operation<Mirror, OperationMetadata> response = await lustreClient.UpdateMirrorAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Mirror, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Mirror result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Mirror, OperationMetadata> retrievedResponse = await lustreClient.PollOnceUpdateMirrorAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Mirror retrievedResult = retrievedResponse.Result;
    }
    

### UpdateMirrorAsync(UpdateMirrorRequest, CancellationToken)
    
    
    public virtual Task<Operation<Mirror, OperationMetadata>> UpdateMirrorAsync(UpdateMirrorRequest request, CancellationToken cancellationToken)

Updates the parameters of a single mirror.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateMirrorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.UpdateMirrorRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Mirror](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.Mirror)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LustreClient lustreClient = await LustreClient.CreateAsync();
    // Initialize request argument(s)
    UpdateMirrorRequest request = new UpdateMirrorRequest
    {
        Mirror = new Mirror(),
        UpdateMask = new FieldMask(),
        RequestId = "",
    };
    // Make the request
    Operation<Mirror, OperationMetadata> response = await lustreClient.UpdateMirrorAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Mirror, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Mirror result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Mirror, OperationMetadata> retrievedResponse = await lustreClient.PollOnceUpdateMirrorAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Mirror retrievedResult = retrievedResponse.Result;
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
