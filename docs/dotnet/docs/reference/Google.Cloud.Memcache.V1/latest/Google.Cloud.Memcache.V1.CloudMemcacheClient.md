---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.CloudMemcacheClient
title: Cloud Memorystore for Memcached v1 API - Class CloudMemcacheClient (2.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:15:57.692388+00:00
---

# Cloud Memorystore for Memcached v1 API - Class CloudMemcacheClient (2.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.CloudMemcacheClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Memorystore for Memcached v1 API - Class CloudMemcacheClient (2.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.6.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.CloudMemcacheClient)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/2.5.0/Google.Cloud.Memcache.V1.CloudMemcacheClient)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/2.4.0/Google.Cloud.Memcache.V1.CloudMemcacheClient)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/2.3.0/Google.Cloud.Memcache.V1.CloudMemcacheClient)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/2.2.0/Google.Cloud.Memcache.V1.CloudMemcacheClient)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/2.1.0/Google.Cloud.Memcache.V1.CloudMemcacheClient)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/2.0.0/Google.Cloud.Memcache.V1.CloudMemcacheClient)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/1.2.0/Google.Cloud.Memcache.V1.CloudMemcacheClient)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/1.1.0/Google.Cloud.Memcache.V1.CloudMemcacheClient)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/1.0.0/Google.Cloud.Memcache.V1.CloudMemcacheClient)


    
    
    public abstract class CloudMemcacheClient

Reference documentation and code samples for the Cloud Memorystore for Memcached v1 API class CloudMemcacheClient.

CloudMemcache client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CloudMemcacheClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[CloudMemcacheClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.CloudMemcacheClientImpl)

## Namespace

[Google.Cloud.Memcache.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1)

## Assembly

Google.Cloud.Memcache.V1.dll

## Remarks

Configures and manages Cloud Memorystore for Memcached instances.

The `memcache.googleapis.com` service implements the Google Cloud Memorystore for Memcached API and defines the following resource model for managing Memorystore Memcached (also called Memcached below) instances:

  * The service works with a collection of cloud projects, named: `/projects/*`
  * Each project has a collection of available locations, named: `/locations/*`
  * Each location has a collection of Memcached instances, named: `/instances/*`
  * As such, Memcached instances are resources of the form: `/projects/{project_id}/locations/{location_id}/instances/{instance_id}`



Note that location_id must be a GCP `region`; for example:

  * `projects/my-memcached-project/locations/us-central1/instances/my-memcached`



## Properties 

### ApplyParametersOperationsClient
    
    
    public virtual OperationsClient ApplyParametersOperationsClient { get; }

The long-running operations client for `ApplyParameters`.

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
  
### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the CloudMemcache service, which is a host of "memcache.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default CloudMemcache scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default CloudMemcache scopes are: 

  * <https://www.googleapis.com/auth/cloud-platform>



### DeleteInstanceOperationsClient
    
    
    public virtual OperationsClient DeleteInstanceOperationsClient { get; }

The long-running operations client for `DeleteInstance`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### GrpcClient
    
    
    public virtual CloudMemcache.CloudMemcacheClient GrpcClient { get; }

The underlying gRPC CloudMemcache client

**Property Value**  
---  
**Type** | **Description**  
`[CloudMemcache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.CloudMemcache)[CloudMemcacheClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.CloudMemcache.CloudMemcacheClient)` |   
  
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
  
### UpdateParametersOperationsClient
    
    
    public virtual OperationsClient UpdateParametersOperationsClient { get; }

The long-running operations client for `UpdateParameters`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
## Methods 

### ApplyParameters(ApplyParametersRequest, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> ApplyParameters(ApplyParametersRequest request, CallSettings callSettings = null)

`ApplyParameters` restarts the set of specified nodes in order to update them to the current set of parameters for the Memcached Instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ApplyParametersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.ApplyParametersRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = CloudMemcacheClient.Create();
    // Initialize request argument(s)
    ApplyParametersRequest request = new ApplyParametersRequest
    {
        InstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
        NodeIds = { "", },
        ApplyAll = false,
    };
    // Make the request
    Operation<Instance, OperationMetadata> response = cloudMemcacheClient.ApplyParameters(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = cloudMemcacheClient.PollOnceApplyParameters(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### ApplyParameters(InstanceName, IEnumerable<string>, bool, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> ApplyParameters(InstanceName name, IEnumerable<string> nodeIds, bool applyAll, CallSettings callSettings = null)

`ApplyParameters` restarts the set of specified nodes in order to update them to the current set of parameters for the Memcached Instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.InstanceName)`  
Required. Resource name of the Memcached instance for which parameter group updates should be applied.  
`nodeIds` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Nodes to which the instance-level parameter group is applied.  
`applyAll` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
Whether to apply instance-level parameter group to all nodes. If set to true, users are restricted from specifying individual nodes, and `ApplyParameters` updates all nodes within the instance.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = CloudMemcacheClient.Create();
    // Initialize request argument(s)
    InstanceName name = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    IEnumerable<string> nodeIds = new string[] { "", };
    bool applyAll = false;
    // Make the request
    Operation<Instance, OperationMetadata> response = cloudMemcacheClient.ApplyParameters(name, nodeIds, applyAll);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = cloudMemcacheClient.PollOnceApplyParameters(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### ApplyParameters(string, IEnumerable<string>, bool, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> ApplyParameters(string name, IEnumerable<string> nodeIds, bool applyAll, CallSettings callSettings = null)

`ApplyParameters` restarts the set of specified nodes in order to update them to the current set of parameters for the Memcached Instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Resource name of the Memcached instance for which parameter group updates should be applied.  
`nodeIds` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Nodes to which the instance-level parameter group is applied.  
`applyAll` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
Whether to apply instance-level parameter group to all nodes. If set to true, users are restricted from specifying individual nodes, and `ApplyParameters` updates all nodes within the instance.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = CloudMemcacheClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]";
    IEnumerable<string> nodeIds = new string[] { "", };
    bool applyAll = false;
    // Make the request
    Operation<Instance, OperationMetadata> response = cloudMemcacheClient.ApplyParameters(name, nodeIds, applyAll);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = cloudMemcacheClient.PollOnceApplyParameters(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### ApplyParametersAsync(ApplyParametersRequest, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> ApplyParametersAsync(ApplyParametersRequest request, CallSettings callSettings = null)

`ApplyParameters` restarts the set of specified nodes in order to update them to the current set of parameters for the Memcached Instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ApplyParametersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.ApplyParametersRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = await CloudMemcacheClient.CreateAsync();
    // Initialize request argument(s)
    ApplyParametersRequest request = new ApplyParametersRequest
    {
        InstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
        NodeIds = { "", },
        ApplyAll = false,
    };
    // Make the request
    Operation<Instance, OperationMetadata> response = await cloudMemcacheClient.ApplyParametersAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await cloudMemcacheClient.PollOnceApplyParametersAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### ApplyParametersAsync(ApplyParametersRequest, CancellationToken)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> ApplyParametersAsync(ApplyParametersRequest request, CancellationToken cancellationToken)

`ApplyParameters` restarts the set of specified nodes in order to update them to the current set of parameters for the Memcached Instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ApplyParametersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.ApplyParametersRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = await CloudMemcacheClient.CreateAsync();
    // Initialize request argument(s)
    ApplyParametersRequest request = new ApplyParametersRequest
    {
        InstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
        NodeIds = { "", },
        ApplyAll = false,
    };
    // Make the request
    Operation<Instance, OperationMetadata> response = await cloudMemcacheClient.ApplyParametersAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await cloudMemcacheClient.PollOnceApplyParametersAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### ApplyParametersAsync(InstanceName, IEnumerable<string>, bool, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> ApplyParametersAsync(InstanceName name, IEnumerable<string> nodeIds, bool applyAll, CallSettings callSettings = null)

`ApplyParameters` restarts the set of specified nodes in order to update them to the current set of parameters for the Memcached Instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.InstanceName)`  
Required. Resource name of the Memcached instance for which parameter group updates should be applied.  
`nodeIds` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Nodes to which the instance-level parameter group is applied.  
`applyAll` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
Whether to apply instance-level parameter group to all nodes. If set to true, users are restricted from specifying individual nodes, and `ApplyParameters` updates all nodes within the instance.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = await CloudMemcacheClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName name = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    IEnumerable<string> nodeIds = new string[] { "", };
    bool applyAll = false;
    // Make the request
    Operation<Instance, OperationMetadata> response = await cloudMemcacheClient.ApplyParametersAsync(name, nodeIds, applyAll);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await cloudMemcacheClient.PollOnceApplyParametersAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### ApplyParametersAsync(InstanceName, IEnumerable<string>, bool, CancellationToken)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> ApplyParametersAsync(InstanceName name, IEnumerable<string> nodeIds, bool applyAll, CancellationToken cancellationToken)

`ApplyParameters` restarts the set of specified nodes in order to update them to the current set of parameters for the Memcached Instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.InstanceName)`  
Required. Resource name of the Memcached instance for which parameter group updates should be applied.  
`nodeIds` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Nodes to which the instance-level parameter group is applied.  
`applyAll` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
Whether to apply instance-level parameter group to all nodes. If set to true, users are restricted from specifying individual nodes, and `ApplyParameters` updates all nodes within the instance.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = await CloudMemcacheClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName name = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    IEnumerable<string> nodeIds = new string[] { "", };
    bool applyAll = false;
    // Make the request
    Operation<Instance, OperationMetadata> response = await cloudMemcacheClient.ApplyParametersAsync(name, nodeIds, applyAll);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await cloudMemcacheClient.PollOnceApplyParametersAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### ApplyParametersAsync(string, IEnumerable<string>, bool, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> ApplyParametersAsync(string name, IEnumerable<string> nodeIds, bool applyAll, CallSettings callSettings = null)

`ApplyParameters` restarts the set of specified nodes in order to update them to the current set of parameters for the Memcached Instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Resource name of the Memcached instance for which parameter group updates should be applied.  
`nodeIds` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Nodes to which the instance-level parameter group is applied.  
`applyAll` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
Whether to apply instance-level parameter group to all nodes. If set to true, users are restricted from specifying individual nodes, and `ApplyParameters` updates all nodes within the instance.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = await CloudMemcacheClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]";
    IEnumerable<string> nodeIds = new string[] { "", };
    bool applyAll = false;
    // Make the request
    Operation<Instance, OperationMetadata> response = await cloudMemcacheClient.ApplyParametersAsync(name, nodeIds, applyAll);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await cloudMemcacheClient.PollOnceApplyParametersAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### ApplyParametersAsync(string, IEnumerable<string>, bool, CancellationToken)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> ApplyParametersAsync(string name, IEnumerable<string> nodeIds, bool applyAll, CancellationToken cancellationToken)

`ApplyParameters` restarts the set of specified nodes in order to update them to the current set of parameters for the Memcached Instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Resource name of the Memcached instance for which parameter group updates should be applied.  
`nodeIds` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Nodes to which the instance-level parameter group is applied.  
`applyAll` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
Whether to apply instance-level parameter group to all nodes. If set to true, users are restricted from specifying individual nodes, and `ApplyParameters` updates all nodes within the instance.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = await CloudMemcacheClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]";
    IEnumerable<string> nodeIds = new string[] { "", };
    bool applyAll = false;
    // Make the request
    Operation<Instance, OperationMetadata> response = await cloudMemcacheClient.ApplyParametersAsync(name, nodeIds, applyAll);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await cloudMemcacheClient.PollOnceApplyParametersAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### Create()
    
    
    public static CloudMemcacheClient Create()

Synchronously creates a [CloudMemcacheClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.CloudMemcacheClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [CloudMemcacheClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.CloudMemcacheClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[CloudMemcacheClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.CloudMemcacheClient)` | The created [CloudMemcacheClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.CloudMemcacheClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<CloudMemcacheClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [CloudMemcacheClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.CloudMemcacheClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [CloudMemcacheClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.CloudMemcacheClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CloudMemcacheClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.CloudMemcacheClient)` | The task representing the created [CloudMemcacheClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.CloudMemcacheClient).  
  
### CreateInstance(LocationName, Instance, string, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> CreateInstance(LocationName parent, Instance instance, string instanceId, CallSettings callSettings = null)

Creates a new Instance in a given location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The resource name of the instance location using the form: `projects/{project_id}/locations/{location_id}` where `location_id` refers to a GCP region  
`instance` | `[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)`  
Required. A Memcached Instance  
`instanceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The logical name of the Memcached instance in the user project with the following restrictions:

  * Must contain only lowercase letters, numbers, and hyphens.
  * Must start with a letter.
  * Must be between 1-40 characters.
  * Must end with a number or a letter.
  * Must be unique within the user project / location.

If any of the above are not met, the API raises an invalid argument error.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = CloudMemcacheClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Instance instance = new Instance();
    string instanceId = "";
    // Make the request
    Operation<Instance, OperationMetadata> response = cloudMemcacheClient.CreateInstance(parent, instance, instanceId);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = cloudMemcacheClient.PollOnceCreateInstance(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### CreateInstance(CreateInstanceRequest, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> CreateInstance(CreateInstanceRequest request, CallSettings callSettings = null)

Creates a new Instance in a given location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.CreateInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = CloudMemcacheClient.Create();
    // Initialize request argument(s)
    CreateInstanceRequest request = new CreateInstanceRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        InstanceId = "",
        Instance = new Instance(),
    };
    // Make the request
    Operation<Instance, OperationMetadata> response = cloudMemcacheClient.CreateInstance(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = cloudMemcacheClient.PollOnceCreateInstance(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### CreateInstance(string, Instance, string, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> CreateInstance(string parent, Instance instance, string instanceId, CallSettings callSettings = null)

Creates a new Instance in a given location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the instance location using the form: `projects/{project_id}/locations/{location_id}` where `location_id` refers to a GCP region  
`instance` | `[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)`  
Required. A Memcached Instance  
`instanceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The logical name of the Memcached instance in the user project with the following restrictions:

  * Must contain only lowercase letters, numbers, and hyphens.
  * Must start with a letter.
  * Must be between 1-40 characters.
  * Must end with a number or a letter.
  * Must be unique within the user project / location.

If any of the above are not met, the API raises an invalid argument error.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = CloudMemcacheClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Instance instance = new Instance();
    string instanceId = "";
    // Make the request
    Operation<Instance, OperationMetadata> response = cloudMemcacheClient.CreateInstance(parent, instance, instanceId);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = cloudMemcacheClient.PollOnceCreateInstance(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### CreateInstanceAsync(LocationName, Instance, string, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> CreateInstanceAsync(LocationName parent, Instance instance, string instanceId, CallSettings callSettings = null)

Creates a new Instance in a given location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The resource name of the instance location using the form: `projects/{project_id}/locations/{location_id}` where `location_id` refers to a GCP region  
`instance` | `[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)`  
Required. A Memcached Instance  
`instanceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The logical name of the Memcached instance in the user project with the following restrictions:

  * Must contain only lowercase letters, numbers, and hyphens.
  * Must start with a letter.
  * Must be between 1-40 characters.
  * Must end with a number or a letter.
  * Must be unique within the user project / location.

If any of the above are not met, the API raises an invalid argument error.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = await CloudMemcacheClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Instance instance = new Instance();
    string instanceId = "";
    // Make the request
    Operation<Instance, OperationMetadata> response = await cloudMemcacheClient.CreateInstanceAsync(parent, instance, instanceId);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await cloudMemcacheClient.PollOnceCreateInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### CreateInstanceAsync(LocationName, Instance, string, CancellationToken)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> CreateInstanceAsync(LocationName parent, Instance instance, string instanceId, CancellationToken cancellationToken)

Creates a new Instance in a given location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The resource name of the instance location using the form: `projects/{project_id}/locations/{location_id}` where `location_id` refers to a GCP region  
`instance` | `[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)`  
Required. A Memcached Instance  
`instanceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The logical name of the Memcached instance in the user project with the following restrictions:

  * Must contain only lowercase letters, numbers, and hyphens.
  * Must start with a letter.
  * Must be between 1-40 characters.
  * Must end with a number or a letter.
  * Must be unique within the user project / location.

If any of the above are not met, the API raises an invalid argument error.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = await CloudMemcacheClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Instance instance = new Instance();
    string instanceId = "";
    // Make the request
    Operation<Instance, OperationMetadata> response = await cloudMemcacheClient.CreateInstanceAsync(parent, instance, instanceId);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await cloudMemcacheClient.PollOnceCreateInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### CreateInstanceAsync(CreateInstanceRequest, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> CreateInstanceAsync(CreateInstanceRequest request, CallSettings callSettings = null)

Creates a new Instance in a given location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.CreateInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = await CloudMemcacheClient.CreateAsync();
    // Initialize request argument(s)
    CreateInstanceRequest request = new CreateInstanceRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        InstanceId = "",
        Instance = new Instance(),
    };
    // Make the request
    Operation<Instance, OperationMetadata> response = await cloudMemcacheClient.CreateInstanceAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await cloudMemcacheClient.PollOnceCreateInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### CreateInstanceAsync(CreateInstanceRequest, CancellationToken)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> CreateInstanceAsync(CreateInstanceRequest request, CancellationToken cancellationToken)

Creates a new Instance in a given location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.CreateInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = await CloudMemcacheClient.CreateAsync();
    // Initialize request argument(s)
    CreateInstanceRequest request = new CreateInstanceRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        InstanceId = "",
        Instance = new Instance(),
    };
    // Make the request
    Operation<Instance, OperationMetadata> response = await cloudMemcacheClient.CreateInstanceAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await cloudMemcacheClient.PollOnceCreateInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### CreateInstanceAsync(string, Instance, string, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> CreateInstanceAsync(string parent, Instance instance, string instanceId, CallSettings callSettings = null)

Creates a new Instance in a given location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the instance location using the form: `projects/{project_id}/locations/{location_id}` where `location_id` refers to a GCP region  
`instance` | `[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)`  
Required. A Memcached Instance  
`instanceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The logical name of the Memcached instance in the user project with the following restrictions:

  * Must contain only lowercase letters, numbers, and hyphens.
  * Must start with a letter.
  * Must be between 1-40 characters.
  * Must end with a number or a letter.
  * Must be unique within the user project / location.

If any of the above are not met, the API raises an invalid argument error.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = await CloudMemcacheClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Instance instance = new Instance();
    string instanceId = "";
    // Make the request
    Operation<Instance, OperationMetadata> response = await cloudMemcacheClient.CreateInstanceAsync(parent, instance, instanceId);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await cloudMemcacheClient.PollOnceCreateInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### CreateInstanceAsync(string, Instance, string, CancellationToken)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> CreateInstanceAsync(string parent, Instance instance, string instanceId, CancellationToken cancellationToken)

Creates a new Instance in a given location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the instance location using the form: `projects/{project_id}/locations/{location_id}` where `location_id` refers to a GCP region  
`instance` | `[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)`  
Required. A Memcached Instance  
`instanceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The logical name of the Memcached instance in the user project with the following restrictions:

  * Must contain only lowercase letters, numbers, and hyphens.
  * Must start with a letter.
  * Must be between 1-40 characters.
  * Must end with a number or a letter.
  * Must be unique within the user project / location.

If any of the above are not met, the API raises an invalid argument error.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = await CloudMemcacheClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Instance instance = new Instance();
    string instanceId = "";
    // Make the request
    Operation<Instance, OperationMetadata> response = await cloudMemcacheClient.CreateInstanceAsync(parent, instance, instanceId);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await cloudMemcacheClient.PollOnceCreateInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### DeleteInstance(DeleteInstanceRequest, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteInstance(DeleteInstanceRequest request, CallSettings callSettings = null)

Deletes a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.DeleteInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = CloudMemcacheClient.Create();
    // Initialize request argument(s)
    DeleteInstanceRequest request = new DeleteInstanceRequest
    {
        InstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = cloudMemcacheClient.DeleteInstance(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = cloudMemcacheClient.PollOnceDeleteInstance(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteInstance(InstanceName, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteInstance(InstanceName name, CallSettings callSettings = null)

Deletes a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.InstanceName)`  
Required. Memcached instance resource name in the format: `projects/{project_id}/locations/{location_id}/instances/{instance_id}` where `location_id` refers to a GCP region  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = CloudMemcacheClient.Create();
    // Initialize request argument(s)
    InstanceName name = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    // Make the request
    Operation<Empty, OperationMetadata> response = cloudMemcacheClient.DeleteInstance(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = cloudMemcacheClient.PollOnceDeleteInstance(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteInstance(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteInstance(string name, CallSettings callSettings = null)

Deletes a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Memcached instance resource name in the format: `projects/{project_id}/locations/{location_id}/instances/{instance_id}` where `location_id` refers to a GCP region  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = CloudMemcacheClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]";
    // Make the request
    Operation<Empty, OperationMetadata> response = cloudMemcacheClient.DeleteInstance(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = cloudMemcacheClient.PollOnceDeleteInstance(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteInstanceAsync(DeleteInstanceRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteInstanceAsync(DeleteInstanceRequest request, CallSettings callSettings = null)

Deletes a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.DeleteInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = await CloudMemcacheClient.CreateAsync();
    // Initialize request argument(s)
    DeleteInstanceRequest request = new DeleteInstanceRequest
    {
        InstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await cloudMemcacheClient.DeleteInstanceAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await cloudMemcacheClient.PollOnceDeleteInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteInstanceAsync(DeleteInstanceRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteInstanceAsync(DeleteInstanceRequest request, CancellationToken cancellationToken)

Deletes a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.DeleteInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = await CloudMemcacheClient.CreateAsync();
    // Initialize request argument(s)
    DeleteInstanceRequest request = new DeleteInstanceRequest
    {
        InstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await cloudMemcacheClient.DeleteInstanceAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await cloudMemcacheClient.PollOnceDeleteInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteInstanceAsync(InstanceName, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteInstanceAsync(InstanceName name, CallSettings callSettings = null)

Deletes a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.InstanceName)`  
Required. Memcached instance resource name in the format: `projects/{project_id}/locations/{location_id}/instances/{instance_id}` where `location_id` refers to a GCP region  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = await CloudMemcacheClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName name = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await cloudMemcacheClient.DeleteInstanceAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await cloudMemcacheClient.PollOnceDeleteInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteInstanceAsync(InstanceName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteInstanceAsync(InstanceName name, CancellationToken cancellationToken)

Deletes a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.InstanceName)`  
Required. Memcached instance resource name in the format: `projects/{project_id}/locations/{location_id}/instances/{instance_id}` where `location_id` refers to a GCP region  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = await CloudMemcacheClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName name = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await cloudMemcacheClient.DeleteInstanceAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await cloudMemcacheClient.PollOnceDeleteInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteInstanceAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteInstanceAsync(string name, CallSettings callSettings = null)

Deletes a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Memcached instance resource name in the format: `projects/{project_id}/locations/{location_id}/instances/{instance_id}` where `location_id` refers to a GCP region  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = await CloudMemcacheClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await cloudMemcacheClient.DeleteInstanceAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await cloudMemcacheClient.PollOnceDeleteInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteInstanceAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteInstanceAsync(string name, CancellationToken cancellationToken)

Deletes a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Memcached instance resource name in the format: `projects/{project_id}/locations/{location_id}/instances/{instance_id}` where `location_id` refers to a GCP region  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = await CloudMemcacheClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await cloudMemcacheClient.DeleteInstanceAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await cloudMemcacheClient.PollOnceDeleteInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### GetInstance(GetInstanceRequest, CallSettings)
    
    
    public virtual Instance GetInstance(GetInstanceRequest request, CallSettings callSettings = null)

Gets details of a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.GetInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = CloudMemcacheClient.Create();
    // Initialize request argument(s)
    GetInstanceRequest request = new GetInstanceRequest
    {
        InstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
    };
    // Make the request
    Instance response = cloudMemcacheClient.GetInstance(request);
    

### GetInstance(InstanceName, CallSettings)
    
    
    public virtual Instance GetInstance(InstanceName name, CallSettings callSettings = null)

Gets details of a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.InstanceName)`  
Required. Memcached instance resource name in the format: `projects/{project_id}/locations/{location_id}/instances/{instance_id}` where `location_id` refers to a GCP region  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = CloudMemcacheClient.Create();
    // Initialize request argument(s)
    InstanceName name = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    // Make the request
    Instance response = cloudMemcacheClient.GetInstance(name);
    

### GetInstance(string, CallSettings)
    
    
    public virtual Instance GetInstance(string name, CallSettings callSettings = null)

Gets details of a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Memcached instance resource name in the format: `projects/{project_id}/locations/{location_id}/instances/{instance_id}` where `location_id` refers to a GCP region  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = CloudMemcacheClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]";
    // Make the request
    Instance response = cloudMemcacheClient.GetInstance(name);
    

### GetInstanceAsync(GetInstanceRequest, CallSettings)
    
    
    public virtual Task<Instance> GetInstanceAsync(GetInstanceRequest request, CallSettings callSettings = null)

Gets details of a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.GetInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = await CloudMemcacheClient.CreateAsync();
    // Initialize request argument(s)
    GetInstanceRequest request = new GetInstanceRequest
    {
        InstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
    };
    // Make the request
    Instance response = await cloudMemcacheClient.GetInstanceAsync(request);
    

### GetInstanceAsync(GetInstanceRequest, CancellationToken)
    
    
    public virtual Task<Instance> GetInstanceAsync(GetInstanceRequest request, CancellationToken cancellationToken)

Gets details of a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.GetInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = await CloudMemcacheClient.CreateAsync();
    // Initialize request argument(s)
    GetInstanceRequest request = new GetInstanceRequest
    {
        InstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
    };
    // Make the request
    Instance response = await cloudMemcacheClient.GetInstanceAsync(request);
    

### GetInstanceAsync(InstanceName, CallSettings)
    
    
    public virtual Task<Instance> GetInstanceAsync(InstanceName name, CallSettings callSettings = null)

Gets details of a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.InstanceName)`  
Required. Memcached instance resource name in the format: `projects/{project_id}/locations/{location_id}/instances/{instance_id}` where `location_id` refers to a GCP region  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = await CloudMemcacheClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName name = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    // Make the request
    Instance response = await cloudMemcacheClient.GetInstanceAsync(name);
    

### GetInstanceAsync(InstanceName, CancellationToken)
    
    
    public virtual Task<Instance> GetInstanceAsync(InstanceName name, CancellationToken cancellationToken)

Gets details of a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.InstanceName)`  
Required. Memcached instance resource name in the format: `projects/{project_id}/locations/{location_id}/instances/{instance_id}` where `location_id` refers to a GCP region  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = await CloudMemcacheClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName name = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    // Make the request
    Instance response = await cloudMemcacheClient.GetInstanceAsync(name);
    

### GetInstanceAsync(string, CallSettings)
    
    
    public virtual Task<Instance> GetInstanceAsync(string name, CallSettings callSettings = null)

Gets details of a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Memcached instance resource name in the format: `projects/{project_id}/locations/{location_id}/instances/{instance_id}` where `location_id` refers to a GCP region  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = await CloudMemcacheClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]";
    // Make the request
    Instance response = await cloudMemcacheClient.GetInstanceAsync(name);
    

### GetInstanceAsync(string, CancellationToken)
    
    
    public virtual Task<Instance> GetInstanceAsync(string name, CancellationToken cancellationToken)

Gets details of a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Memcached instance resource name in the format: `projects/{project_id}/locations/{location_id}/instances/{instance_id}` where `location_id` refers to a GCP region  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = await CloudMemcacheClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]";
    // Make the request
    Instance response = await cloudMemcacheClient.GetInstanceAsync(name);
    

### ListInstances(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListInstancesResponse, Instance> ListInstances(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Instances in a given location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The resource name of the instance location using the form: `projects/{project_id}/locations/{location_id}` where `location_id` refers to a GCP region  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.ListInstancesResponse)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)` | A pageable sequence of [Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance) resources.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = CloudMemcacheClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListInstancesResponse, Instance> response = cloudMemcacheClient.ListInstances(parent);
    
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

Lists Instances in a given location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.ListInstancesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.ListInstancesResponse)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)` | A pageable sequence of [Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance) resources.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = CloudMemcacheClient.Create();
    // Initialize request argument(s)
    ListInstancesRequest request = new ListInstancesRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListInstancesResponse, Instance> response = cloudMemcacheClient.ListInstances(request);
    
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

Lists Instances in a given location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the instance location using the form: `projects/{project_id}/locations/{location_id}` where `location_id` refers to a GCP region  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.ListInstancesResponse)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)` | A pageable sequence of [Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance) resources.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = CloudMemcacheClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListInstancesResponse, Instance> response = cloudMemcacheClient.ListInstances(parent);
    
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

Lists Instances in a given location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The resource name of the instance location using the form: `projects/{project_id}/locations/{location_id}` where `location_id` refers to a GCP region  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.ListInstancesResponse)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)` | A pageable asynchronous sequence of [Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance) resources.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = await CloudMemcacheClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListInstancesResponse, Instance> response = cloudMemcacheClient.ListInstancesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Instance item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListInstancesResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Instance item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
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

Lists Instances in a given location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.ListInstancesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.ListInstancesResponse)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)` | A pageable asynchronous sequence of [Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance) resources.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = await CloudMemcacheClient.CreateAsync();
    // Initialize request argument(s)
    ListInstancesRequest request = new ListInstancesRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListInstancesResponse, Instance> response = cloudMemcacheClient.ListInstancesAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Instance item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListInstancesResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Instance item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
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

Lists Instances in a given location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the instance location using the form: `projects/{project_id}/locations/{location_id}` where `location_id` refers to a GCP region  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.ListInstancesResponse)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)` | A pageable asynchronous sequence of [Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance) resources.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = await CloudMemcacheClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListInstancesResponse, Instance> response = cloudMemcacheClient.ListInstancesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Instance item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListInstancesResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Instance item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
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
    

### PollOnceApplyParameters(string, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> PollOnceApplyParameters(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `ApplyParameters`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceApplyParametersAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> PollOnceApplyParametersAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `ApplyParameters`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | The result of polling the operation.  
  
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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | The result of polling the operation.  
  
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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | The result of polling the operation.  
  
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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | The result of polling the operation.  
  
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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceUpdateParameters(string, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> PollOnceUpdateParameters(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `UpdateParameters`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceUpdateParametersAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> PollOnceUpdateParametersAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `UpdateParameters`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### RescheduleMaintenance(InstanceName, RescheduleType, Timestamp, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> RescheduleMaintenance(InstanceName instance, RescheduleMaintenanceRequest.Types.RescheduleType rescheduleType, Timestamp scheduleTime, CallSettings callSettings = null)

Reschedules upcoming maintenance event.

**Parameters**  
---  
**Name** | **Description**  
`instance` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.InstanceName)`  
Required. Memcache instance resource name using the form: `projects/{project_id}/locations/{location_id}/instances/{instance_id}` where `location_id` refers to a GCP region.  
`rescheduleType` | `[RescheduleMaintenanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.RescheduleMaintenanceRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.RescheduleMaintenanceRequest.Types)[RescheduleType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.RescheduleMaintenanceRequest.Types.RescheduleType)`  
Required. If reschedule type is SPECIFIC_TIME, must set up schedule_time as well.  
`scheduleTime` | `[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)`  
Timestamp when the maintenance shall be rescheduled to if reschedule_type=SPECIFIC_TIME, in RFC 3339 format, for example `2012-11-15T16:19:00.094Z`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = CloudMemcacheClient.Create();
    // Initialize request argument(s)
    InstanceName instance = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    RescheduleMaintenanceRequest.Types.RescheduleType rescheduleType = RescheduleMaintenanceRequest.Types.RescheduleType.Unspecified;
    Timestamp scheduleTime = new Timestamp();
    // Make the request
    Operation<Instance, OperationMetadata> response = cloudMemcacheClient.RescheduleMaintenance(instance, rescheduleType, scheduleTime);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = cloudMemcacheClient.PollOnceRescheduleMaintenance(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### RescheduleMaintenance(RescheduleMaintenanceRequest, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> RescheduleMaintenance(RescheduleMaintenanceRequest request, CallSettings callSettings = null)

Reschedules upcoming maintenance event.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RescheduleMaintenanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.RescheduleMaintenanceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = CloudMemcacheClient.Create();
    // Initialize request argument(s)
    RescheduleMaintenanceRequest request = new RescheduleMaintenanceRequest
    {
        InstanceAsInstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
        RescheduleType = RescheduleMaintenanceRequest.Types.RescheduleType.Unspecified,
        ScheduleTime = new Timestamp(),
    };
    // Make the request
    Operation<Instance, OperationMetadata> response = cloudMemcacheClient.RescheduleMaintenance(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = cloudMemcacheClient.PollOnceRescheduleMaintenance(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### RescheduleMaintenance(string, RescheduleType, Timestamp, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> RescheduleMaintenance(string instance, RescheduleMaintenanceRequest.Types.RescheduleType rescheduleType, Timestamp scheduleTime, CallSettings callSettings = null)

Reschedules upcoming maintenance event.

**Parameters**  
---  
**Name** | **Description**  
`instance` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Memcache instance resource name using the form: `projects/{project_id}/locations/{location_id}/instances/{instance_id}` where `location_id` refers to a GCP region.  
`rescheduleType` | `[RescheduleMaintenanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.RescheduleMaintenanceRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.RescheduleMaintenanceRequest.Types)[RescheduleType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.RescheduleMaintenanceRequest.Types.RescheduleType)`  
Required. If reschedule type is SPECIFIC_TIME, must set up schedule_time as well.  
`scheduleTime` | `[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)`  
Timestamp when the maintenance shall be rescheduled to if reschedule_type=SPECIFIC_TIME, in RFC 3339 format, for example `2012-11-15T16:19:00.094Z`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = CloudMemcacheClient.Create();
    // Initialize request argument(s)
    string instance = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]";
    RescheduleMaintenanceRequest.Types.RescheduleType rescheduleType = RescheduleMaintenanceRequest.Types.RescheduleType.Unspecified;
    Timestamp scheduleTime = new Timestamp();
    // Make the request
    Operation<Instance, OperationMetadata> response = cloudMemcacheClient.RescheduleMaintenance(instance, rescheduleType, scheduleTime);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = cloudMemcacheClient.PollOnceRescheduleMaintenance(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### RescheduleMaintenanceAsync(InstanceName, RescheduleType, Timestamp, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> RescheduleMaintenanceAsync(InstanceName instance, RescheduleMaintenanceRequest.Types.RescheduleType rescheduleType, Timestamp scheduleTime, CallSettings callSettings = null)

Reschedules upcoming maintenance event.

**Parameters**  
---  
**Name** | **Description**  
`instance` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.InstanceName)`  
Required. Memcache instance resource name using the form: `projects/{project_id}/locations/{location_id}/instances/{instance_id}` where `location_id` refers to a GCP region.  
`rescheduleType` | `[RescheduleMaintenanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.RescheduleMaintenanceRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.RescheduleMaintenanceRequest.Types)[RescheduleType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.RescheduleMaintenanceRequest.Types.RescheduleType)`  
Required. If reschedule type is SPECIFIC_TIME, must set up schedule_time as well.  
`scheduleTime` | `[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)`  
Timestamp when the maintenance shall be rescheduled to if reschedule_type=SPECIFIC_TIME, in RFC 3339 format, for example `2012-11-15T16:19:00.094Z`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = await CloudMemcacheClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName instance = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    RescheduleMaintenanceRequest.Types.RescheduleType rescheduleType = RescheduleMaintenanceRequest.Types.RescheduleType.Unspecified;
    Timestamp scheduleTime = new Timestamp();
    // Make the request
    Operation<Instance, OperationMetadata> response = await cloudMemcacheClient.RescheduleMaintenanceAsync(instance, rescheduleType, scheduleTime);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await cloudMemcacheClient.PollOnceRescheduleMaintenanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### RescheduleMaintenanceAsync(InstanceName, RescheduleType, Timestamp, CancellationToken)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> RescheduleMaintenanceAsync(InstanceName instance, RescheduleMaintenanceRequest.Types.RescheduleType rescheduleType, Timestamp scheduleTime, CancellationToken cancellationToken)

Reschedules upcoming maintenance event.

**Parameters**  
---  
**Name** | **Description**  
`instance` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.InstanceName)`  
Required. Memcache instance resource name using the form: `projects/{project_id}/locations/{location_id}/instances/{instance_id}` where `location_id` refers to a GCP region.  
`rescheduleType` | `[RescheduleMaintenanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.RescheduleMaintenanceRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.RescheduleMaintenanceRequest.Types)[RescheduleType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.RescheduleMaintenanceRequest.Types.RescheduleType)`  
Required. If reschedule type is SPECIFIC_TIME, must set up schedule_time as well.  
`scheduleTime` | `[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)`  
Timestamp when the maintenance shall be rescheduled to if reschedule_type=SPECIFIC_TIME, in RFC 3339 format, for example `2012-11-15T16:19:00.094Z`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = await CloudMemcacheClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName instance = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    RescheduleMaintenanceRequest.Types.RescheduleType rescheduleType = RescheduleMaintenanceRequest.Types.RescheduleType.Unspecified;
    Timestamp scheduleTime = new Timestamp();
    // Make the request
    Operation<Instance, OperationMetadata> response = await cloudMemcacheClient.RescheduleMaintenanceAsync(instance, rescheduleType, scheduleTime);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await cloudMemcacheClient.PollOnceRescheduleMaintenanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### RescheduleMaintenanceAsync(RescheduleMaintenanceRequest, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> RescheduleMaintenanceAsync(RescheduleMaintenanceRequest request, CallSettings callSettings = null)

Reschedules upcoming maintenance event.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RescheduleMaintenanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.RescheduleMaintenanceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = await CloudMemcacheClient.CreateAsync();
    // Initialize request argument(s)
    RescheduleMaintenanceRequest request = new RescheduleMaintenanceRequest
    {
        InstanceAsInstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
        RescheduleType = RescheduleMaintenanceRequest.Types.RescheduleType.Unspecified,
        ScheduleTime = new Timestamp(),
    };
    // Make the request
    Operation<Instance, OperationMetadata> response = await cloudMemcacheClient.RescheduleMaintenanceAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await cloudMemcacheClient.PollOnceRescheduleMaintenanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### RescheduleMaintenanceAsync(RescheduleMaintenanceRequest, CancellationToken)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> RescheduleMaintenanceAsync(RescheduleMaintenanceRequest request, CancellationToken cancellationToken)

Reschedules upcoming maintenance event.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RescheduleMaintenanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.RescheduleMaintenanceRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = await CloudMemcacheClient.CreateAsync();
    // Initialize request argument(s)
    RescheduleMaintenanceRequest request = new RescheduleMaintenanceRequest
    {
        InstanceAsInstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
        RescheduleType = RescheduleMaintenanceRequest.Types.RescheduleType.Unspecified,
        ScheduleTime = new Timestamp(),
    };
    // Make the request
    Operation<Instance, OperationMetadata> response = await cloudMemcacheClient.RescheduleMaintenanceAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await cloudMemcacheClient.PollOnceRescheduleMaintenanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### RescheduleMaintenanceAsync(string, RescheduleType, Timestamp, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> RescheduleMaintenanceAsync(string instance, RescheduleMaintenanceRequest.Types.RescheduleType rescheduleType, Timestamp scheduleTime, CallSettings callSettings = null)

Reschedules upcoming maintenance event.

**Parameters**  
---  
**Name** | **Description**  
`instance` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Memcache instance resource name using the form: `projects/{project_id}/locations/{location_id}/instances/{instance_id}` where `location_id` refers to a GCP region.  
`rescheduleType` | `[RescheduleMaintenanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.RescheduleMaintenanceRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.RescheduleMaintenanceRequest.Types)[RescheduleType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.RescheduleMaintenanceRequest.Types.RescheduleType)`  
Required. If reschedule type is SPECIFIC_TIME, must set up schedule_time as well.  
`scheduleTime` | `[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)`  
Timestamp when the maintenance shall be rescheduled to if reschedule_type=SPECIFIC_TIME, in RFC 3339 format, for example `2012-11-15T16:19:00.094Z`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = await CloudMemcacheClient.CreateAsync();
    // Initialize request argument(s)
    string instance = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]";
    RescheduleMaintenanceRequest.Types.RescheduleType rescheduleType = RescheduleMaintenanceRequest.Types.RescheduleType.Unspecified;
    Timestamp scheduleTime = new Timestamp();
    // Make the request
    Operation<Instance, OperationMetadata> response = await cloudMemcacheClient.RescheduleMaintenanceAsync(instance, rescheduleType, scheduleTime);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await cloudMemcacheClient.PollOnceRescheduleMaintenanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### RescheduleMaintenanceAsync(string, RescheduleType, Timestamp, CancellationToken)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> RescheduleMaintenanceAsync(string instance, RescheduleMaintenanceRequest.Types.RescheduleType rescheduleType, Timestamp scheduleTime, CancellationToken cancellationToken)

Reschedules upcoming maintenance event.

**Parameters**  
---  
**Name** | **Description**  
`instance` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Memcache instance resource name using the form: `projects/{project_id}/locations/{location_id}/instances/{instance_id}` where `location_id` refers to a GCP region.  
`rescheduleType` | `[RescheduleMaintenanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.RescheduleMaintenanceRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.RescheduleMaintenanceRequest.Types)[RescheduleType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.RescheduleMaintenanceRequest.Types.RescheduleType)`  
Required. If reschedule type is SPECIFIC_TIME, must set up schedule_time as well.  
`scheduleTime` | `[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)`  
Timestamp when the maintenance shall be rescheduled to if reschedule_type=SPECIFIC_TIME, in RFC 3339 format, for example `2012-11-15T16:19:00.094Z`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = await CloudMemcacheClient.CreateAsync();
    // Initialize request argument(s)
    string instance = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]";
    RescheduleMaintenanceRequest.Types.RescheduleType rescheduleType = RescheduleMaintenanceRequest.Types.RescheduleType.Unspecified;
    Timestamp scheduleTime = new Timestamp();
    // Make the request
    Operation<Instance, OperationMetadata> response = await cloudMemcacheClient.RescheduleMaintenanceAsync(instance, rescheduleType, scheduleTime);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await cloudMemcacheClient.PollOnceRescheduleMaintenanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.CloudMemcacheClient#Google_Cloud_Memcache_V1_CloudMemcacheClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.CloudMemcacheClient#Google_Cloud_Memcache_V1_CloudMemcacheClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.CloudMemcacheClient#Google_Cloud_Memcache_V1_CloudMemcacheClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.CloudMemcacheClient#Google_Cloud_Memcache_V1_CloudMemcacheClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### UpdateInstance(Instance, FieldMask, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> UpdateInstance(Instance instance, FieldMask updateMask, CallSettings callSettings = null)

Updates an existing Instance in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`instance` | `[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)`  
Required. A Memcached Instance. Only fields specified in update_mask are updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. Mask of fields to update.

  * `displayName`

  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = CloudMemcacheClient.Create();
    // Initialize request argument(s)
    Instance instance = new Instance();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Instance, OperationMetadata> response = cloudMemcacheClient.UpdateInstance(instance, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = cloudMemcacheClient.PollOnceUpdateInstance(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### UpdateInstance(UpdateInstanceRequest, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> UpdateInstance(UpdateInstanceRequest request, CallSettings callSettings = null)

Updates an existing Instance in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.UpdateInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = CloudMemcacheClient.Create();
    // Initialize request argument(s)
    UpdateInstanceRequest request = new UpdateInstanceRequest
    {
        UpdateMask = new FieldMask(),
        Instance = new Instance(),
    };
    // Make the request
    Operation<Instance, OperationMetadata> response = cloudMemcacheClient.UpdateInstance(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = cloudMemcacheClient.PollOnceUpdateInstance(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### UpdateInstanceAsync(Instance, FieldMask, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> UpdateInstanceAsync(Instance instance, FieldMask updateMask, CallSettings callSettings = null)

Updates an existing Instance in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`instance` | `[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)`  
Required. A Memcached Instance. Only fields specified in update_mask are updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. Mask of fields to update.

  * `displayName`

  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = await CloudMemcacheClient.CreateAsync();
    // Initialize request argument(s)
    Instance instance = new Instance();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Instance, OperationMetadata> response = await cloudMemcacheClient.UpdateInstanceAsync(instance, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await cloudMemcacheClient.PollOnceUpdateInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### UpdateInstanceAsync(Instance, FieldMask, CancellationToken)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> UpdateInstanceAsync(Instance instance, FieldMask updateMask, CancellationToken cancellationToken)

Updates an existing Instance in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`instance` | `[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)`  
Required. A Memcached Instance. Only fields specified in update_mask are updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. Mask of fields to update.

  * `displayName`

  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = await CloudMemcacheClient.CreateAsync();
    // Initialize request argument(s)
    Instance instance = new Instance();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Instance, OperationMetadata> response = await cloudMemcacheClient.UpdateInstanceAsync(instance, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await cloudMemcacheClient.PollOnceUpdateInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### UpdateInstanceAsync(UpdateInstanceRequest, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> UpdateInstanceAsync(UpdateInstanceRequest request, CallSettings callSettings = null)

Updates an existing Instance in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.UpdateInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = await CloudMemcacheClient.CreateAsync();
    // Initialize request argument(s)
    UpdateInstanceRequest request = new UpdateInstanceRequest
    {
        UpdateMask = new FieldMask(),
        Instance = new Instance(),
    };
    // Make the request
    Operation<Instance, OperationMetadata> response = await cloudMemcacheClient.UpdateInstanceAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await cloudMemcacheClient.PollOnceUpdateInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### UpdateInstanceAsync(UpdateInstanceRequest, CancellationToken)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> UpdateInstanceAsync(UpdateInstanceRequest request, CancellationToken cancellationToken)

Updates an existing Instance in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.UpdateInstanceRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = await CloudMemcacheClient.CreateAsync();
    // Initialize request argument(s)
    UpdateInstanceRequest request = new UpdateInstanceRequest
    {
        UpdateMask = new FieldMask(),
        Instance = new Instance(),
    };
    // Make the request
    Operation<Instance, OperationMetadata> response = await cloudMemcacheClient.UpdateInstanceAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await cloudMemcacheClient.PollOnceUpdateInstanceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### UpdateParameters(InstanceName, FieldMask, MemcacheParameters, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> UpdateParameters(InstanceName name, FieldMask updateMask, MemcacheParameters parameters, CallSettings callSettings = null)

Updates the defined Memcached parameters for an existing instance. This method only stages the parameters, it must be followed by `ApplyParameters` to apply the parameters to nodes of the Memcached instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.InstanceName)`  
Required. Resource name of the Memcached instance for which the parameters should be updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. Mask of fields to update.  
`parameters` | `[MemcacheParameters](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.MemcacheParameters)`  
The parameters to apply to the instance.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = CloudMemcacheClient.Create();
    // Initialize request argument(s)
    InstanceName name = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    FieldMask updateMask = new FieldMask();
    MemcacheParameters parameters = new MemcacheParameters();
    // Make the request
    Operation<Instance, OperationMetadata> response = cloudMemcacheClient.UpdateParameters(name, updateMask, parameters);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = cloudMemcacheClient.PollOnceUpdateParameters(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### UpdateParameters(UpdateParametersRequest, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> UpdateParameters(UpdateParametersRequest request, CallSettings callSettings = null)

Updates the defined Memcached parameters for an existing instance. This method only stages the parameters, it must be followed by `ApplyParameters` to apply the parameters to nodes of the Memcached instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateParametersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.UpdateParametersRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = CloudMemcacheClient.Create();
    // Initialize request argument(s)
    UpdateParametersRequest request = new UpdateParametersRequest
    {
        InstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
        UpdateMask = new FieldMask(),
        Parameters = new MemcacheParameters(),
    };
    // Make the request
    Operation<Instance, OperationMetadata> response = cloudMemcacheClient.UpdateParameters(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = cloudMemcacheClient.PollOnceUpdateParameters(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### UpdateParameters(string, FieldMask, MemcacheParameters, CallSettings)
    
    
    public virtual Operation<Instance, OperationMetadata> UpdateParameters(string name, FieldMask updateMask, MemcacheParameters parameters, CallSettings callSettings = null)

Updates the defined Memcached parameters for an existing instance. This method only stages the parameters, it must be followed by `ApplyParameters` to apply the parameters to nodes of the Memcached instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Resource name of the Memcached instance for which the parameters should be updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. Mask of fields to update.  
`parameters` | `[MemcacheParameters](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.MemcacheParameters)`  
The parameters to apply to the instance.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = CloudMemcacheClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]";
    FieldMask updateMask = new FieldMask();
    MemcacheParameters parameters = new MemcacheParameters();
    // Make the request
    Operation<Instance, OperationMetadata> response = cloudMemcacheClient.UpdateParameters(name, updateMask, parameters);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = cloudMemcacheClient.PollOnceUpdateParameters(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### UpdateParametersAsync(InstanceName, FieldMask, MemcacheParameters, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> UpdateParametersAsync(InstanceName name, FieldMask updateMask, MemcacheParameters parameters, CallSettings callSettings = null)

Updates the defined Memcached parameters for an existing instance. This method only stages the parameters, it must be followed by `ApplyParameters` to apply the parameters to nodes of the Memcached instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.InstanceName)`  
Required. Resource name of the Memcached instance for which the parameters should be updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. Mask of fields to update.  
`parameters` | `[MemcacheParameters](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.MemcacheParameters)`  
The parameters to apply to the instance.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = await CloudMemcacheClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName name = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    FieldMask updateMask = new FieldMask();
    MemcacheParameters parameters = new MemcacheParameters();
    // Make the request
    Operation<Instance, OperationMetadata> response = await cloudMemcacheClient.UpdateParametersAsync(name, updateMask, parameters);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await cloudMemcacheClient.PollOnceUpdateParametersAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### UpdateParametersAsync(InstanceName, FieldMask, MemcacheParameters, CancellationToken)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> UpdateParametersAsync(InstanceName name, FieldMask updateMask, MemcacheParameters parameters, CancellationToken cancellationToken)

Updates the defined Memcached parameters for an existing instance. This method only stages the parameters, it must be followed by `ApplyParameters` to apply the parameters to nodes of the Memcached instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.InstanceName)`  
Required. Resource name of the Memcached instance for which the parameters should be updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. Mask of fields to update.  
`parameters` | `[MemcacheParameters](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.MemcacheParameters)`  
The parameters to apply to the instance.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = await CloudMemcacheClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName name = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    FieldMask updateMask = new FieldMask();
    MemcacheParameters parameters = new MemcacheParameters();
    // Make the request
    Operation<Instance, OperationMetadata> response = await cloudMemcacheClient.UpdateParametersAsync(name, updateMask, parameters);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await cloudMemcacheClient.PollOnceUpdateParametersAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### UpdateParametersAsync(UpdateParametersRequest, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> UpdateParametersAsync(UpdateParametersRequest request, CallSettings callSettings = null)

Updates the defined Memcached parameters for an existing instance. This method only stages the parameters, it must be followed by `ApplyParameters` to apply the parameters to nodes of the Memcached instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateParametersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.UpdateParametersRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = await CloudMemcacheClient.CreateAsync();
    // Initialize request argument(s)
    UpdateParametersRequest request = new UpdateParametersRequest
    {
        InstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
        UpdateMask = new FieldMask(),
        Parameters = new MemcacheParameters(),
    };
    // Make the request
    Operation<Instance, OperationMetadata> response = await cloudMemcacheClient.UpdateParametersAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await cloudMemcacheClient.PollOnceUpdateParametersAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### UpdateParametersAsync(UpdateParametersRequest, CancellationToken)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> UpdateParametersAsync(UpdateParametersRequest request, CancellationToken cancellationToken)

Updates the defined Memcached parameters for an existing instance. This method only stages the parameters, it must be followed by `ApplyParameters` to apply the parameters to nodes of the Memcached instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateParametersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.UpdateParametersRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = await CloudMemcacheClient.CreateAsync();
    // Initialize request argument(s)
    UpdateParametersRequest request = new UpdateParametersRequest
    {
        InstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
        UpdateMask = new FieldMask(),
        Parameters = new MemcacheParameters(),
    };
    // Make the request
    Operation<Instance, OperationMetadata> response = await cloudMemcacheClient.UpdateParametersAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await cloudMemcacheClient.PollOnceUpdateParametersAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### UpdateParametersAsync(string, FieldMask, MemcacheParameters, CallSettings)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> UpdateParametersAsync(string name, FieldMask updateMask, MemcacheParameters parameters, CallSettings callSettings = null)

Updates the defined Memcached parameters for an existing instance. This method only stages the parameters, it must be followed by `ApplyParameters` to apply the parameters to nodes of the Memcached instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Resource name of the Memcached instance for which the parameters should be updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. Mask of fields to update.  
`parameters` | `[MemcacheParameters](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.MemcacheParameters)`  
The parameters to apply to the instance.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = await CloudMemcacheClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]";
    FieldMask updateMask = new FieldMask();
    MemcacheParameters parameters = new MemcacheParameters();
    // Make the request
    Operation<Instance, OperationMetadata> response = await cloudMemcacheClient.UpdateParametersAsync(name, updateMask, parameters);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await cloudMemcacheClient.PollOnceUpdateParametersAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

### UpdateParametersAsync(string, FieldMask, MemcacheParameters, CancellationToken)
    
    
    public virtual Task<Operation<Instance, OperationMetadata>> UpdateParametersAsync(string name, FieldMask updateMask, MemcacheParameters parameters, CancellationToken cancellationToken)

Updates the defined Memcached parameters for an existing instance. This method only stages the parameters, it must be followed by `ApplyParameters` to apply the parameters to nodes of the Memcached instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Resource name of the Memcached instance for which the parameters should be updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. Mask of fields to update.  
`parameters` | `[MemcacheParameters](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.MemcacheParameters)`  
The parameters to apply to the instance.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudMemcacheClient cloudMemcacheClient = await CloudMemcacheClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]";
    FieldMask updateMask = new FieldMask();
    MemcacheParameters parameters = new MemcacheParameters();
    // Make the request
    Operation<Instance, OperationMetadata> response = await cloudMemcacheClient.UpdateParametersAsync(name, updateMask, parameters);
    
    // Poll until the returned long-running operation is complete
    Operation<Instance, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Instance result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Instance, OperationMetadata> retrievedResponse = await cloudMemcacheClient.PollOnceUpdateParametersAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Instance retrievedResult = retrievedResponse.Result;
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
