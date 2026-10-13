---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient
title: Google Cloud Tasks v2 API - Class CloudTasksClient (3.7.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:34:28.591043+00:00
---

# Google Cloud Tasks v2 API - Class CloudTasksClient (3.7.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Tasks v2 API - Class CloudTasksClient (3.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.7.0 (latest)  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public abstract class CloudTasksClient

Reference documentation and code samples for the Google Cloud Tasks v2 API class CloudTasksClient.

CloudTasks client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CloudTasksClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[CloudTasksClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClientImpl)

## Namespace

[Google.Cloud.Tasks.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2)

## Assembly

Google.Cloud.Tasks.V2.dll

## Remarks

Cloud Tasks allows developers to manage the execution of background work in their applications.

## Properties 

### BatchCreateTasksOperationsClient
    
    
    public virtual OperationsClient BatchCreateTasksOperationsClient { get; }

The long-running operations client for `BatchCreateTasks`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### BatchDeleteTasksOperationsClient
    
    
    public virtual OperationsClient BatchDeleteTasksOperationsClient { get; }

The long-running operations client for `BatchDeleteTasks`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the CloudTasks service, which is a host of "cloudtasks.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default CloudTasks scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default CloudTasks scopes are:

  * <https://www.googleapis.com/auth/cloud-platform>



### GrpcClient
    
    
    public virtual CloudTasks.CloudTasksClient GrpcClient { get; }

The underlying gRPC CloudTasks client

**Property Value**  
---  
**Type** | **Description**  
`[CloudTasks](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasks)[CloudTasksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasks.CloudTasksClient)` |   
  
### LocationsClient
    
    
    public virtual LocationsClient LocationsClient { get; }

The [LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.LocationsClient.html) associated with this client.

**Property Value**  
---  
**Type** | **Description**  
`[LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.LocationsClient.html)` |   
  
### ServiceMetadata
    
    
    public static ServiceMetadata ServiceMetadata { get; }

The service metadata associated with this client type.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceMetadata](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceMetadata.html)` |   
  
## Methods 

### BatchCreateTasks(BatchCreateTasksRequest, CallSettings)
    
    
    public virtual Operation<BatchCreateTasksResponse, BatchCreateTasksMetadata> BatchCreateTasks(BatchCreateTasksRequest request, CallSettings callSettings = null)

Creates a batch of tasks and adds them to a queue.

All tasks must be for the same queue. A maximum of 100 tasks can be created in a single batch.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchCreateTasksRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchCreateTasksRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchCreateTasksResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchCreateTasksResponse)[BatchCreateTasksMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchCreateTasksMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    gctv::BatchCreateTasksRequest request = new gctv::BatchCreateTasksRequest
    {
        ParentAsQueueName = gctv::QueueName.FromProjectLocationQueue("[PROJECT]", "[LOCATION]", "[QUEUE]"),
        Requests =
        {
            new gctv::CreateTaskRequest(),
        },
        RequestId = "",
    };
    // Make the request
    Operation<gctv::BatchCreateTasksResponse, gctv::BatchCreateTasksMetadata> response = cloudTasksClient.BatchCreateTasks(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gctv::BatchCreateTasksResponse, gctv::BatchCreateTasksMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gctv::BatchCreateTasksResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gctv::BatchCreateTasksResponse, gctv::BatchCreateTasksMetadata> retrievedResponse = cloudTasksClient.PollOnceBatchCreateTasks(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gctv::BatchCreateTasksResponse retrievedResult = retrievedResponse.Result;
    }
    

### BatchCreateTasks(QueueName, IEnumerable<CreateTaskRequest>, CallSettings)
    
    
    public virtual Operation<BatchCreateTasksResponse, BatchCreateTasksMetadata> BatchCreateTasks(QueueName parent, IEnumerable<CreateTaskRequest> requests, CallSettings callSettings = null)

Creates a batch of tasks and adds them to a queue.

All tasks must be for the same queue. A maximum of 100 tasks can be created in a single batch.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[QueueName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.QueueName)`  
Required. The queue name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID` The queue must already exist.  
`requests` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[CreateTaskRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CreateTaskRequest)`  
Required. The list of requests to create tasks. The queue specified in parent field of each CreateTaskRequest will be the same. This validation happens on the client side as well as in the handler. BatchCreateTasksRequest.parent will also be the same value as the individual CreateTaskRequest.parent. The maximum number of requests is 100.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchCreateTasksResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchCreateTasksResponse)[BatchCreateTasksMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchCreateTasksMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    gctv::QueueName parent = gctv::QueueName.FromProjectLocationQueue("[PROJECT]", "[LOCATION]", "[QUEUE]");
    IEnumerable<gctv::CreateTaskRequest> requests = new gctv::CreateTaskRequest[]
    {
        new gctv::CreateTaskRequest(),
    };
    // Make the request
    Operation<gctv::BatchCreateTasksResponse, gctv::BatchCreateTasksMetadata> response = cloudTasksClient.BatchCreateTasks(parent, requests);
    
    // Poll until the returned long-running operation is complete
    Operation<gctv::BatchCreateTasksResponse, gctv::BatchCreateTasksMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gctv::BatchCreateTasksResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gctv::BatchCreateTasksResponse, gctv::BatchCreateTasksMetadata> retrievedResponse = cloudTasksClient.PollOnceBatchCreateTasks(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gctv::BatchCreateTasksResponse retrievedResult = retrievedResponse.Result;
    }
    

### BatchCreateTasks(string, IEnumerable<CreateTaskRequest>, CallSettings)
    
    
    public virtual Operation<BatchCreateTasksResponse, BatchCreateTasksMetadata> BatchCreateTasks(string parent, IEnumerable<CreateTaskRequest> requests, CallSettings callSettings = null)

Creates a batch of tasks and adds them to a queue.

All tasks must be for the same queue. A maximum of 100 tasks can be created in a single batch.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The queue name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID` The queue must already exist.  
`requests` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[CreateTaskRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CreateTaskRequest)`  
Required. The list of requests to create tasks. The queue specified in parent field of each CreateTaskRequest will be the same. This validation happens on the client side as well as in the handler. BatchCreateTasksRequest.parent will also be the same value as the individual CreateTaskRequest.parent. The maximum number of requests is 100.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchCreateTasksResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchCreateTasksResponse)[BatchCreateTasksMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchCreateTasksMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/queues/[QUEUE]";
    IEnumerable<gctv::CreateTaskRequest> requests = new gctv::CreateTaskRequest[]
    {
        new gctv::CreateTaskRequest(),
    };
    // Make the request
    Operation<gctv::BatchCreateTasksResponse, gctv::BatchCreateTasksMetadata> response = cloudTasksClient.BatchCreateTasks(parent, requests);
    
    // Poll until the returned long-running operation is complete
    Operation<gctv::BatchCreateTasksResponse, gctv::BatchCreateTasksMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gctv::BatchCreateTasksResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gctv::BatchCreateTasksResponse, gctv::BatchCreateTasksMetadata> retrievedResponse = cloudTasksClient.PollOnceBatchCreateTasks(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gctv::BatchCreateTasksResponse retrievedResult = retrievedResponse.Result;
    }
    

### BatchCreateTasksAsync(BatchCreateTasksRequest, CallSettings)
    
    
    public virtual Task<Operation<BatchCreateTasksResponse, BatchCreateTasksMetadata>> BatchCreateTasksAsync(BatchCreateTasksRequest request, CallSettings callSettings = null)

Creates a batch of tasks and adds them to a queue.

All tasks must be for the same queue. A maximum of 100 tasks can be created in a single batch.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchCreateTasksRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchCreateTasksRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchCreateTasksResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchCreateTasksResponse)[BatchCreateTasksMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchCreateTasksMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::BatchCreateTasksRequest request = new gctv::BatchCreateTasksRequest
    {
        ParentAsQueueName = gctv::QueueName.FromProjectLocationQueue("[PROJECT]", "[LOCATION]", "[QUEUE]"),
        Requests =
        {
            new gctv::CreateTaskRequest(),
        },
        RequestId = "",
    };
    // Make the request
    Operation<gctv::BatchCreateTasksResponse, gctv::BatchCreateTasksMetadata> response = await cloudTasksClient.BatchCreateTasksAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gctv::BatchCreateTasksResponse, gctv::BatchCreateTasksMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gctv::BatchCreateTasksResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gctv::BatchCreateTasksResponse, gctv::BatchCreateTasksMetadata> retrievedResponse = await cloudTasksClient.PollOnceBatchCreateTasksAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gctv::BatchCreateTasksResponse retrievedResult = retrievedResponse.Result;
    }
    

### BatchCreateTasksAsync(BatchCreateTasksRequest, CancellationToken)
    
    
    public virtual Task<Operation<BatchCreateTasksResponse, BatchCreateTasksMetadata>> BatchCreateTasksAsync(BatchCreateTasksRequest request, CancellationToken cancellationToken)

Creates a batch of tasks and adds them to a queue.

All tasks must be for the same queue. A maximum of 100 tasks can be created in a single batch.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchCreateTasksRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchCreateTasksRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchCreateTasksResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchCreateTasksResponse)[BatchCreateTasksMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchCreateTasksMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::BatchCreateTasksRequest request = new gctv::BatchCreateTasksRequest
    {
        ParentAsQueueName = gctv::QueueName.FromProjectLocationQueue("[PROJECT]", "[LOCATION]", "[QUEUE]"),
        Requests =
        {
            new gctv::CreateTaskRequest(),
        },
        RequestId = "",
    };
    // Make the request
    Operation<gctv::BatchCreateTasksResponse, gctv::BatchCreateTasksMetadata> response = await cloudTasksClient.BatchCreateTasksAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gctv::BatchCreateTasksResponse, gctv::BatchCreateTasksMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gctv::BatchCreateTasksResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gctv::BatchCreateTasksResponse, gctv::BatchCreateTasksMetadata> retrievedResponse = await cloudTasksClient.PollOnceBatchCreateTasksAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gctv::BatchCreateTasksResponse retrievedResult = retrievedResponse.Result;
    }
    

### BatchCreateTasksAsync(QueueName, IEnumerable<CreateTaskRequest>, CallSettings)
    
    
    public virtual Task<Operation<BatchCreateTasksResponse, BatchCreateTasksMetadata>> BatchCreateTasksAsync(QueueName parent, IEnumerable<CreateTaskRequest> requests, CallSettings callSettings = null)

Creates a batch of tasks and adds them to a queue.

All tasks must be for the same queue. A maximum of 100 tasks can be created in a single batch.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[QueueName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.QueueName)`  
Required. The queue name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID` The queue must already exist.  
`requests` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[CreateTaskRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CreateTaskRequest)`  
Required. The list of requests to create tasks. The queue specified in parent field of each CreateTaskRequest will be the same. This validation happens on the client side as well as in the handler. BatchCreateTasksRequest.parent will also be the same value as the individual CreateTaskRequest.parent. The maximum number of requests is 100.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchCreateTasksResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchCreateTasksResponse)[BatchCreateTasksMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchCreateTasksMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::QueueName parent = gctv::QueueName.FromProjectLocationQueue("[PROJECT]", "[LOCATION]", "[QUEUE]");
    IEnumerable<gctv::CreateTaskRequest> requests = new gctv::CreateTaskRequest[]
    {
        new gctv::CreateTaskRequest(),
    };
    // Make the request
    Operation<gctv::BatchCreateTasksResponse, gctv::BatchCreateTasksMetadata> response = await cloudTasksClient.BatchCreateTasksAsync(parent, requests);
    
    // Poll until the returned long-running operation is complete
    Operation<gctv::BatchCreateTasksResponse, gctv::BatchCreateTasksMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gctv::BatchCreateTasksResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gctv::BatchCreateTasksResponse, gctv::BatchCreateTasksMetadata> retrievedResponse = await cloudTasksClient.PollOnceBatchCreateTasksAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gctv::BatchCreateTasksResponse retrievedResult = retrievedResponse.Result;
    }
    

### BatchCreateTasksAsync(QueueName, IEnumerable<CreateTaskRequest>, CancellationToken)
    
    
    public virtual Task<Operation<BatchCreateTasksResponse, BatchCreateTasksMetadata>> BatchCreateTasksAsync(QueueName parent, IEnumerable<CreateTaskRequest> requests, CancellationToken cancellationToken)

Creates a batch of tasks and adds them to a queue.

All tasks must be for the same queue. A maximum of 100 tasks can be created in a single batch.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[QueueName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.QueueName)`  
Required. The queue name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID` The queue must already exist.  
`requests` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[CreateTaskRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CreateTaskRequest)`  
Required. The list of requests to create tasks. The queue specified in parent field of each CreateTaskRequest will be the same. This validation happens on the client side as well as in the handler. BatchCreateTasksRequest.parent will also be the same value as the individual CreateTaskRequest.parent. The maximum number of requests is 100.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchCreateTasksResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchCreateTasksResponse)[BatchCreateTasksMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchCreateTasksMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::QueueName parent = gctv::QueueName.FromProjectLocationQueue("[PROJECT]", "[LOCATION]", "[QUEUE]");
    IEnumerable<gctv::CreateTaskRequest> requests = new gctv::CreateTaskRequest[]
    {
        new gctv::CreateTaskRequest(),
    };
    // Make the request
    Operation<gctv::BatchCreateTasksResponse, gctv::BatchCreateTasksMetadata> response = await cloudTasksClient.BatchCreateTasksAsync(parent, requests);
    
    // Poll until the returned long-running operation is complete
    Operation<gctv::BatchCreateTasksResponse, gctv::BatchCreateTasksMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gctv::BatchCreateTasksResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gctv::BatchCreateTasksResponse, gctv::BatchCreateTasksMetadata> retrievedResponse = await cloudTasksClient.PollOnceBatchCreateTasksAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gctv::BatchCreateTasksResponse retrievedResult = retrievedResponse.Result;
    }
    

### BatchCreateTasksAsync(string, IEnumerable<CreateTaskRequest>, CallSettings)
    
    
    public virtual Task<Operation<BatchCreateTasksResponse, BatchCreateTasksMetadata>> BatchCreateTasksAsync(string parent, IEnumerable<CreateTaskRequest> requests, CallSettings callSettings = null)

Creates a batch of tasks and adds them to a queue.

All tasks must be for the same queue. A maximum of 100 tasks can be created in a single batch.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The queue name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID` The queue must already exist.  
`requests` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[CreateTaskRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CreateTaskRequest)`  
Required. The list of requests to create tasks. The queue specified in parent field of each CreateTaskRequest will be the same. This validation happens on the client side as well as in the handler. BatchCreateTasksRequest.parent will also be the same value as the individual CreateTaskRequest.parent. The maximum number of requests is 100.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchCreateTasksResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchCreateTasksResponse)[BatchCreateTasksMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchCreateTasksMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/queues/[QUEUE]";
    IEnumerable<gctv::CreateTaskRequest> requests = new gctv::CreateTaskRequest[]
    {
        new gctv::CreateTaskRequest(),
    };
    // Make the request
    Operation<gctv::BatchCreateTasksResponse, gctv::BatchCreateTasksMetadata> response = await cloudTasksClient.BatchCreateTasksAsync(parent, requests);
    
    // Poll until the returned long-running operation is complete
    Operation<gctv::BatchCreateTasksResponse, gctv::BatchCreateTasksMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gctv::BatchCreateTasksResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gctv::BatchCreateTasksResponse, gctv::BatchCreateTasksMetadata> retrievedResponse = await cloudTasksClient.PollOnceBatchCreateTasksAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gctv::BatchCreateTasksResponse retrievedResult = retrievedResponse.Result;
    }
    

### BatchCreateTasksAsync(string, IEnumerable<CreateTaskRequest>, CancellationToken)
    
    
    public virtual Task<Operation<BatchCreateTasksResponse, BatchCreateTasksMetadata>> BatchCreateTasksAsync(string parent, IEnumerable<CreateTaskRequest> requests, CancellationToken cancellationToken)

Creates a batch of tasks and adds them to a queue.

All tasks must be for the same queue. A maximum of 100 tasks can be created in a single batch.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The queue name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID` The queue must already exist.  
`requests` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[CreateTaskRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CreateTaskRequest)`  
Required. The list of requests to create tasks. The queue specified in parent field of each CreateTaskRequest will be the same. This validation happens on the client side as well as in the handler. BatchCreateTasksRequest.parent will also be the same value as the individual CreateTaskRequest.parent. The maximum number of requests is 100.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchCreateTasksResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchCreateTasksResponse)[BatchCreateTasksMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchCreateTasksMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/queues/[QUEUE]";
    IEnumerable<gctv::CreateTaskRequest> requests = new gctv::CreateTaskRequest[]
    {
        new gctv::CreateTaskRequest(),
    };
    // Make the request
    Operation<gctv::BatchCreateTasksResponse, gctv::BatchCreateTasksMetadata> response = await cloudTasksClient.BatchCreateTasksAsync(parent, requests);
    
    // Poll until the returned long-running operation is complete
    Operation<gctv::BatchCreateTasksResponse, gctv::BatchCreateTasksMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gctv::BatchCreateTasksResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gctv::BatchCreateTasksResponse, gctv::BatchCreateTasksMetadata> retrievedResponse = await cloudTasksClient.PollOnceBatchCreateTasksAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gctv::BatchCreateTasksResponse retrievedResult = retrievedResponse.Result;
    }
    

### BatchDeleteTasks(BatchDeleteTasksRequest, CallSettings)
    
    
    public virtual Operation<Empty, BatchDeleteTasksMetadata> BatchDeleteTasks(BatchDeleteTasksRequest request, CallSettings callSettings = null)

Deletes a batch of tasks. This is a non-atomic operation: if deletion fails for some tasks, it can still succeed for others. The metadata field of google.longrunning.Operation contains details of failed deletions. A maximum of 1000 tasks can be deleted in a batch.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchDeleteTasksRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchDeleteTasksRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[BatchDeleteTasksMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchDeleteTasksMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    gctv::BatchDeleteTasksRequest request = new gctv::BatchDeleteTasksRequest
    {
        ParentAsQueueName = gctv::QueueName.FromProjectLocationQueue("[PROJECT]", "[LOCATION]", "[QUEUE]"),
        TaskNames =
        {
            gctv::TaskName.FromProjectLocationQueueTask("[PROJECT]", "[LOCATION]", "[QUEUE]", "[TASK]"),
        },
        RequestId = "",
    };
    // Make the request
    Operation<Empty, gctv::BatchDeleteTasksMetadata> response = cloudTasksClient.BatchDeleteTasks(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gctv::BatchDeleteTasksMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gctv::BatchDeleteTasksMetadata> retrievedResponse = cloudTasksClient.PollOnceBatchDeleteTasks(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### BatchDeleteTasks(QueueName, IEnumerable<TaskName>, CallSettings)
    
    
    public virtual Operation<Empty, BatchDeleteTasksMetadata> BatchDeleteTasks(QueueName parent, IEnumerable<TaskName> names, CallSettings callSettings = null)

Deletes a batch of tasks. This is a non-atomic operation: if deletion fails for some tasks, it can still succeed for others. The metadata field of google.longrunning.Operation contains details of failed deletions. A maximum of 1000 tasks can be deleted in a batch.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[QueueName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.QueueName)`  
Required. The queue name. For example: Format: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID`  
`names` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[TaskName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.TaskName)`  
Required. The names of the tasks to delete. A maximum of 1000 tasks can be deleted in a batch. For example: Format: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[BatchDeleteTasksMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchDeleteTasksMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    gctv::QueueName parent = gctv::QueueName.FromProjectLocationQueue("[PROJECT]", "[LOCATION]", "[QUEUE]");
    IEnumerable<gctv::TaskName> names = new gctv::TaskName[]
    {
        gctv::TaskName.FromProjectLocationQueueTask("[PROJECT]", "[LOCATION]", "[QUEUE]", "[TASK]"),
    };
    // Make the request
    Operation<Empty, gctv::BatchDeleteTasksMetadata> response = cloudTasksClient.BatchDeleteTasks(parent, names);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gctv::BatchDeleteTasksMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gctv::BatchDeleteTasksMetadata> retrievedResponse = cloudTasksClient.PollOnceBatchDeleteTasks(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### BatchDeleteTasks(string, IEnumerable<string>, CallSettings)
    
    
    public virtual Operation<Empty, BatchDeleteTasksMetadata> BatchDeleteTasks(string parent, IEnumerable<string> names, CallSettings callSettings = null)

Deletes a batch of tasks. This is a non-atomic operation: if deletion fails for some tasks, it can still succeed for others. The metadata field of google.longrunning.Operation contains details of failed deletions. A maximum of 1000 tasks can be deleted in a batch.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The queue name. For example: Format: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID`  
`names` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The names of the tasks to delete. A maximum of 1000 tasks can be deleted in a batch. For example: Format: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[BatchDeleteTasksMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchDeleteTasksMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/queues/[QUEUE]";
    IEnumerable<string> names = new string[]
    {
        "projects/[PROJECT]/locations/[LOCATION]/queues/[QUEUE]/tasks/[TASK]",
    };
    // Make the request
    Operation<Empty, gctv::BatchDeleteTasksMetadata> response = cloudTasksClient.BatchDeleteTasks(parent, names);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gctv::BatchDeleteTasksMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gctv::BatchDeleteTasksMetadata> retrievedResponse = cloudTasksClient.PollOnceBatchDeleteTasks(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### BatchDeleteTasksAsync(BatchDeleteTasksRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, BatchDeleteTasksMetadata>> BatchDeleteTasksAsync(BatchDeleteTasksRequest request, CallSettings callSettings = null)

Deletes a batch of tasks. This is a non-atomic operation: if deletion fails for some tasks, it can still succeed for others. The metadata field of google.longrunning.Operation contains details of failed deletions. A maximum of 1000 tasks can be deleted in a batch.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchDeleteTasksRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchDeleteTasksRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[BatchDeleteTasksMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchDeleteTasksMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::BatchDeleteTasksRequest request = new gctv::BatchDeleteTasksRequest
    {
        ParentAsQueueName = gctv::QueueName.FromProjectLocationQueue("[PROJECT]", "[LOCATION]", "[QUEUE]"),
        TaskNames =
        {
            gctv::TaskName.FromProjectLocationQueueTask("[PROJECT]", "[LOCATION]", "[QUEUE]", "[TASK]"),
        },
        RequestId = "",
    };
    // Make the request
    Operation<Empty, gctv::BatchDeleteTasksMetadata> response = await cloudTasksClient.BatchDeleteTasksAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gctv::BatchDeleteTasksMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gctv::BatchDeleteTasksMetadata> retrievedResponse = await cloudTasksClient.PollOnceBatchDeleteTasksAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### BatchDeleteTasksAsync(BatchDeleteTasksRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, BatchDeleteTasksMetadata>> BatchDeleteTasksAsync(BatchDeleteTasksRequest request, CancellationToken cancellationToken)

Deletes a batch of tasks. This is a non-atomic operation: if deletion fails for some tasks, it can still succeed for others. The metadata field of google.longrunning.Operation contains details of failed deletions. A maximum of 1000 tasks can be deleted in a batch.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchDeleteTasksRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchDeleteTasksRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[BatchDeleteTasksMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchDeleteTasksMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::BatchDeleteTasksRequest request = new gctv::BatchDeleteTasksRequest
    {
        ParentAsQueueName = gctv::QueueName.FromProjectLocationQueue("[PROJECT]", "[LOCATION]", "[QUEUE]"),
        TaskNames =
        {
            gctv::TaskName.FromProjectLocationQueueTask("[PROJECT]", "[LOCATION]", "[QUEUE]", "[TASK]"),
        },
        RequestId = "",
    };
    // Make the request
    Operation<Empty, gctv::BatchDeleteTasksMetadata> response = await cloudTasksClient.BatchDeleteTasksAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gctv::BatchDeleteTasksMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gctv::BatchDeleteTasksMetadata> retrievedResponse = await cloudTasksClient.PollOnceBatchDeleteTasksAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### BatchDeleteTasksAsync(QueueName, IEnumerable<TaskName>, CallSettings)
    
    
    public virtual Task<Operation<Empty, BatchDeleteTasksMetadata>> BatchDeleteTasksAsync(QueueName parent, IEnumerable<TaskName> names, CallSettings callSettings = null)

Deletes a batch of tasks. This is a non-atomic operation: if deletion fails for some tasks, it can still succeed for others. The metadata field of google.longrunning.Operation contains details of failed deletions. A maximum of 1000 tasks can be deleted in a batch.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[QueueName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.QueueName)`  
Required. The queue name. For example: Format: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID`  
`names` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[TaskName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.TaskName)`  
Required. The names of the tasks to delete. A maximum of 1000 tasks can be deleted in a batch. For example: Format: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[BatchDeleteTasksMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchDeleteTasksMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::QueueName parent = gctv::QueueName.FromProjectLocationQueue("[PROJECT]", "[LOCATION]", "[QUEUE]");
    IEnumerable<gctv::TaskName> names = new gctv::TaskName[]
    {
        gctv::TaskName.FromProjectLocationQueueTask("[PROJECT]", "[LOCATION]", "[QUEUE]", "[TASK]"),
    };
    // Make the request
    Operation<Empty, gctv::BatchDeleteTasksMetadata> response = await cloudTasksClient.BatchDeleteTasksAsync(parent, names);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gctv::BatchDeleteTasksMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gctv::BatchDeleteTasksMetadata> retrievedResponse = await cloudTasksClient.PollOnceBatchDeleteTasksAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### BatchDeleteTasksAsync(QueueName, IEnumerable<TaskName>, CancellationToken)
    
    
    public virtual Task<Operation<Empty, BatchDeleteTasksMetadata>> BatchDeleteTasksAsync(QueueName parent, IEnumerable<TaskName> names, CancellationToken cancellationToken)

Deletes a batch of tasks. This is a non-atomic operation: if deletion fails for some tasks, it can still succeed for others. The metadata field of google.longrunning.Operation contains details of failed deletions. A maximum of 1000 tasks can be deleted in a batch.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[QueueName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.QueueName)`  
Required. The queue name. For example: Format: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID`  
`names` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[TaskName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.TaskName)`  
Required. The names of the tasks to delete. A maximum of 1000 tasks can be deleted in a batch. For example: Format: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[BatchDeleteTasksMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchDeleteTasksMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::QueueName parent = gctv::QueueName.FromProjectLocationQueue("[PROJECT]", "[LOCATION]", "[QUEUE]");
    IEnumerable<gctv::TaskName> names = new gctv::TaskName[]
    {
        gctv::TaskName.FromProjectLocationQueueTask("[PROJECT]", "[LOCATION]", "[QUEUE]", "[TASK]"),
    };
    // Make the request
    Operation<Empty, gctv::BatchDeleteTasksMetadata> response = await cloudTasksClient.BatchDeleteTasksAsync(parent, names);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gctv::BatchDeleteTasksMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gctv::BatchDeleteTasksMetadata> retrievedResponse = await cloudTasksClient.PollOnceBatchDeleteTasksAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### BatchDeleteTasksAsync(string, IEnumerable<string>, CallSettings)
    
    
    public virtual Task<Operation<Empty, BatchDeleteTasksMetadata>> BatchDeleteTasksAsync(string parent, IEnumerable<string> names, CallSettings callSettings = null)

Deletes a batch of tasks. This is a non-atomic operation: if deletion fails for some tasks, it can still succeed for others. The metadata field of google.longrunning.Operation contains details of failed deletions. A maximum of 1000 tasks can be deleted in a batch.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The queue name. For example: Format: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID`  
`names` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The names of the tasks to delete. A maximum of 1000 tasks can be deleted in a batch. For example: Format: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[BatchDeleteTasksMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchDeleteTasksMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/queues/[QUEUE]";
    IEnumerable<string> names = new string[]
    {
        "projects/[PROJECT]/locations/[LOCATION]/queues/[QUEUE]/tasks/[TASK]",
    };
    // Make the request
    Operation<Empty, gctv::BatchDeleteTasksMetadata> response = await cloudTasksClient.BatchDeleteTasksAsync(parent, names);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gctv::BatchDeleteTasksMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gctv::BatchDeleteTasksMetadata> retrievedResponse = await cloudTasksClient.PollOnceBatchDeleteTasksAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### BatchDeleteTasksAsync(string, IEnumerable<string>, CancellationToken)
    
    
    public virtual Task<Operation<Empty, BatchDeleteTasksMetadata>> BatchDeleteTasksAsync(string parent, IEnumerable<string> names, CancellationToken cancellationToken)

Deletes a batch of tasks. This is a non-atomic operation: if deletion fails for some tasks, it can still succeed for others. The metadata field of google.longrunning.Operation contains details of failed deletions. A maximum of 1000 tasks can be deleted in a batch.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The queue name. For example: Format: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID`  
`names` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The names of the tasks to delete. A maximum of 1000 tasks can be deleted in a batch. For example: Format: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[BatchDeleteTasksMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchDeleteTasksMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/queues/[QUEUE]";
    IEnumerable<string> names = new string[]
    {
        "projects/[PROJECT]/locations/[LOCATION]/queues/[QUEUE]/tasks/[TASK]",
    };
    // Make the request
    Operation<Empty, gctv::BatchDeleteTasksMetadata> response = await cloudTasksClient.BatchDeleteTasksAsync(parent, names);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gctv::BatchDeleteTasksMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gctv::BatchDeleteTasksMetadata> retrievedResponse = await cloudTasksClient.PollOnceBatchDeleteTasksAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### Create()
    
    
    public static CloudTasksClient Create()

Synchronously creates a [CloudTasksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [CloudTasksClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[CloudTasksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient)` | The created [CloudTasksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<CloudTasksClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [CloudTasksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [CloudTasksClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CloudTasksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient)` | The task representing the created [CloudTasksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient).  
  
### CreateQueue(LocationName, Queue, CallSettings)
    
    
    public virtual Queue CreateQueue(LocationName parent, Queue queue, CallSettings callSettings = null)

Creates a queue.

Queues created with this method allow tasks to live for a maximum of 31 days. After a task is 31 days old, the task will be deleted regardless of whether it was dispatched or not.

WARNING: Using this method may have unintended side effects if you are using an App Engine `queue.yaml` or `queue.xml` file to manage your queues. Read [Overview of Queue Management and queue.yaml](https://cloud.google.com/tasks/docs/queue-yaml) before using this method.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The location name in which the queue will be created. For example: `projects/PROJECT_ID/locations/LOCATION_ID` The list of allowed locations can be obtained by calling Cloud Tasks' implementation of [ListLocations][google.cloud.location.Locations.ListLocations].  
`queue` | `[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)`  
Required. The queue to create. [Queue's name][google.cloud.tasks.v2.Queue.name] cannot be the same as an existing queue.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | The RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    gctv::Queue queue = new gctv::Queue();
    // Make the request
    gctv::Queue response = cloudTasksClient.CreateQueue(parent, queue);
    

### CreateQueue(CreateQueueRequest, CallSettings)
    
    
    public virtual Queue CreateQueue(CreateQueueRequest request, CallSettings callSettings = null)

Creates a queue.

Queues created with this method allow tasks to live for a maximum of 31 days. After a task is 31 days old, the task will be deleted regardless of whether it was dispatched or not.

WARNING: Using this method may have unintended side effects if you are using an App Engine `queue.yaml` or `queue.xml` file to manage your queues. Read [Overview of Queue Management and queue.yaml](https://cloud.google.com/tasks/docs/queue-yaml) before using this method.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateQueueRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CreateQueueRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | The RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    gctv::CreateQueueRequest request = new gctv::CreateQueueRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Queue = new gctv::Queue(),
    };
    // Make the request
    gctv::Queue response = cloudTasksClient.CreateQueue(request);
    

### CreateQueue(string, Queue, CallSettings)
    
    
    public virtual Queue CreateQueue(string parent, Queue queue, CallSettings callSettings = null)

Creates a queue.

Queues created with this method allow tasks to live for a maximum of 31 days. After a task is 31 days old, the task will be deleted regardless of whether it was dispatched or not.

WARNING: Using this method may have unintended side effects if you are using an App Engine `queue.yaml` or `queue.xml` file to manage your queues. Read [Overview of Queue Management and queue.yaml](https://cloud.google.com/tasks/docs/queue-yaml) before using this method.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The location name in which the queue will be created. For example: `projects/PROJECT_ID/locations/LOCATION_ID` The list of allowed locations can be obtained by calling Cloud Tasks' implementation of [ListLocations][google.cloud.location.Locations.ListLocations].  
`queue` | `[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)`  
Required. The queue to create. [Queue's name][google.cloud.tasks.v2.Queue.name] cannot be the same as an existing queue.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | The RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    gctv::Queue queue = new gctv::Queue();
    // Make the request
    gctv::Queue response = cloudTasksClient.CreateQueue(parent, queue);
    

### CreateQueueAsync(LocationName, Queue, CallSettings)
    
    
    public virtual Task<Queue> CreateQueueAsync(LocationName parent, Queue queue, CallSettings callSettings = null)

Creates a queue.

Queues created with this method allow tasks to live for a maximum of 31 days. After a task is 31 days old, the task will be deleted regardless of whether it was dispatched or not.

WARNING: Using this method may have unintended side effects if you are using an App Engine `queue.yaml` or `queue.xml` file to manage your queues. Read [Overview of Queue Management and queue.yaml](https://cloud.google.com/tasks/docs/queue-yaml) before using this method.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The location name in which the queue will be created. For example: `projects/PROJECT_ID/locations/LOCATION_ID` The list of allowed locations can be obtained by calling Cloud Tasks' implementation of [ListLocations][google.cloud.location.Locations.ListLocations].  
`queue` | `[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)`  
Required. The queue to create. [Queue's name][google.cloud.tasks.v2.Queue.name] cannot be the same as an existing queue.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    gctv::Queue queue = new gctv::Queue();
    // Make the request
    gctv::Queue response = await cloudTasksClient.CreateQueueAsync(parent, queue);
    

### CreateQueueAsync(LocationName, Queue, CancellationToken)
    
    
    public virtual Task<Queue> CreateQueueAsync(LocationName parent, Queue queue, CancellationToken cancellationToken)

Creates a queue.

Queues created with this method allow tasks to live for a maximum of 31 days. After a task is 31 days old, the task will be deleted regardless of whether it was dispatched or not.

WARNING: Using this method may have unintended side effects if you are using an App Engine `queue.yaml` or `queue.xml` file to manage your queues. Read [Overview of Queue Management and queue.yaml](https://cloud.google.com/tasks/docs/queue-yaml) before using this method.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The location name in which the queue will be created. For example: `projects/PROJECT_ID/locations/LOCATION_ID` The list of allowed locations can be obtained by calling Cloud Tasks' implementation of [ListLocations][google.cloud.location.Locations.ListLocations].  
`queue` | `[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)`  
Required. The queue to create. [Queue's name][google.cloud.tasks.v2.Queue.name] cannot be the same as an existing queue.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    gctv::Queue queue = new gctv::Queue();
    // Make the request
    gctv::Queue response = await cloudTasksClient.CreateQueueAsync(parent, queue);
    

### CreateQueueAsync(CreateQueueRequest, CallSettings)
    
    
    public virtual Task<Queue> CreateQueueAsync(CreateQueueRequest request, CallSettings callSettings = null)

Creates a queue.

Queues created with this method allow tasks to live for a maximum of 31 days. After a task is 31 days old, the task will be deleted regardless of whether it was dispatched or not.

WARNING: Using this method may have unintended side effects if you are using an App Engine `queue.yaml` or `queue.xml` file to manage your queues. Read [Overview of Queue Management and queue.yaml](https://cloud.google.com/tasks/docs/queue-yaml) before using this method.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateQueueRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CreateQueueRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::CreateQueueRequest request = new gctv::CreateQueueRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Queue = new gctv::Queue(),
    };
    // Make the request
    gctv::Queue response = await cloudTasksClient.CreateQueueAsync(request);
    

### CreateQueueAsync(CreateQueueRequest, CancellationToken)
    
    
    public virtual Task<Queue> CreateQueueAsync(CreateQueueRequest request, CancellationToken cancellationToken)

Creates a queue.

Queues created with this method allow tasks to live for a maximum of 31 days. After a task is 31 days old, the task will be deleted regardless of whether it was dispatched or not.

WARNING: Using this method may have unintended side effects if you are using an App Engine `queue.yaml` or `queue.xml` file to manage your queues. Read [Overview of Queue Management and queue.yaml](https://cloud.google.com/tasks/docs/queue-yaml) before using this method.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateQueueRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CreateQueueRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::CreateQueueRequest request = new gctv::CreateQueueRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Queue = new gctv::Queue(),
    };
    // Make the request
    gctv::Queue response = await cloudTasksClient.CreateQueueAsync(request);
    

### CreateQueueAsync(string, Queue, CallSettings)
    
    
    public virtual Task<Queue> CreateQueueAsync(string parent, Queue queue, CallSettings callSettings = null)

Creates a queue.

Queues created with this method allow tasks to live for a maximum of 31 days. After a task is 31 days old, the task will be deleted regardless of whether it was dispatched or not.

WARNING: Using this method may have unintended side effects if you are using an App Engine `queue.yaml` or `queue.xml` file to manage your queues. Read [Overview of Queue Management and queue.yaml](https://cloud.google.com/tasks/docs/queue-yaml) before using this method.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The location name in which the queue will be created. For example: `projects/PROJECT_ID/locations/LOCATION_ID` The list of allowed locations can be obtained by calling Cloud Tasks' implementation of [ListLocations][google.cloud.location.Locations.ListLocations].  
`queue` | `[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)`  
Required. The queue to create. [Queue's name][google.cloud.tasks.v2.Queue.name] cannot be the same as an existing queue.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    gctv::Queue queue = new gctv::Queue();
    // Make the request
    gctv::Queue response = await cloudTasksClient.CreateQueueAsync(parent, queue);
    

### CreateQueueAsync(string, Queue, CancellationToken)
    
    
    public virtual Task<Queue> CreateQueueAsync(string parent, Queue queue, CancellationToken cancellationToken)

Creates a queue.

Queues created with this method allow tasks to live for a maximum of 31 days. After a task is 31 days old, the task will be deleted regardless of whether it was dispatched or not.

WARNING: Using this method may have unintended side effects if you are using an App Engine `queue.yaml` or `queue.xml` file to manage your queues. Read [Overview of Queue Management and queue.yaml](https://cloud.google.com/tasks/docs/queue-yaml) before using this method.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The location name in which the queue will be created. For example: `projects/PROJECT_ID/locations/LOCATION_ID` The list of allowed locations can be obtained by calling Cloud Tasks' implementation of [ListLocations][google.cloud.location.Locations.ListLocations].  
`queue` | `[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)`  
Required. The queue to create. [Queue's name][google.cloud.tasks.v2.Queue.name] cannot be the same as an existing queue.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    gctv::Queue queue = new gctv::Queue();
    // Make the request
    gctv::Queue response = await cloudTasksClient.CreateQueueAsync(parent, queue);
    

### CreateTask(CreateTaskRequest, CallSettings)
    
    
    public virtual Task CreateTask(CreateTaskRequest request, CallSettings callSettings = null)

Creates a task and adds it to a queue.

Tasks cannot be updated after creation; there is no UpdateTask command.

  * The maximum task size is 100KB.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateTaskRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CreateTaskRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task)` | The RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    gctv::CreateTaskRequest request = new gctv::CreateTaskRequest
    {
        ParentAsQueueName = gctv::QueueName.FromProjectLocationQueue("[PROJECT]", "[LOCATION]", "[QUEUE]"),
        Task = new gctv::Task(),
        ResponseView = gctv::Task.Types.View.Unspecified,
    };
    // Make the request
    gctv::Task response = cloudTasksClient.CreateTask(request);
    

### CreateTask(QueueName, Task, CallSettings)
    
    
    public virtual Task CreateTask(QueueName parent, Task task, CallSettings callSettings = null)

Creates a task and adds it to a queue.

Tasks cannot be updated after creation; there is no UpdateTask command.

  * The maximum task size is 100KB.



**Parameters**  
---  
**Name** | **Description**  
`parent` | `[QueueName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.QueueName)`  
Required. The queue name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID` The queue must already exist.  
`task` | `[Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task)`  
Required. The task to add. Task names have the following format: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID`. The user can optionally specify a task [name][google.cloud.tasks.v2.Task.name]. If a name is not specified then the system will generate a random unique task id, which will be set in the task returned in the [response][google.cloud.tasks.v2.Task.name]. If [schedule_time][google.cloud.tasks.v2.Task.schedule_time] is not set or is in the past then Cloud Tasks will set it to the current time. Task De-duplication: Explicitly specifying a task ID enables task de-duplication. If a task's ID is identical to that of an existing task or a task that was deleted or executed recently then the call will fail with [ALREADY_EXISTS][google.rpc.Code.ALREADY_EXISTS]. The IDs of deleted tasks are not immediately available for reuse. It can take up to 24 hours (or 9 days if the task's queue was created using a queue.yaml or queue.xml) for the task ID to be released and made available again. Because there is an extra lookup cost to identify duplicate task names, these [CreateTask][google.cloud.tasks.v2.CloudTasks.CreateTask] calls have significantly increased latency. Using hashed strings for the task id or for the prefix of the task id is recommended. Choosing task ids that are sequential or have sequential prefixes, for example using a timestamp, causes an increase in latency and error rates in all task commands. The infrastructure relies on an approximately uniform distribution of task ids to store and serve tasks efficiently.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task)` | The RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    gctv::QueueName parent = gctv::QueueName.FromProjectLocationQueue("[PROJECT]", "[LOCATION]", "[QUEUE]");
    gctv::Task task = new gctv::Task();
    // Make the request
    gctv::Task response = cloudTasksClient.CreateTask(parent, task);
    

### CreateTask(string, Task, CallSettings)
    
    
    public virtual Task CreateTask(string parent, Task task, CallSettings callSettings = null)

Creates a task and adds it to a queue.

Tasks cannot be updated after creation; there is no UpdateTask command.

  * The maximum task size is 100KB.



**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The queue name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID` The queue must already exist.  
`task` | `[Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task)`  
Required. The task to add. Task names have the following format: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID`. The user can optionally specify a task [name][google.cloud.tasks.v2.Task.name]. If a name is not specified then the system will generate a random unique task id, which will be set in the task returned in the [response][google.cloud.tasks.v2.Task.name]. If [schedule_time][google.cloud.tasks.v2.Task.schedule_time] is not set or is in the past then Cloud Tasks will set it to the current time. Task De-duplication: Explicitly specifying a task ID enables task de-duplication. If a task's ID is identical to that of an existing task or a task that was deleted or executed recently then the call will fail with [ALREADY_EXISTS][google.rpc.Code.ALREADY_EXISTS]. The IDs of deleted tasks are not immediately available for reuse. It can take up to 24 hours (or 9 days if the task's queue was created using a queue.yaml or queue.xml) for the task ID to be released and made available again. Because there is an extra lookup cost to identify duplicate task names, these [CreateTask][google.cloud.tasks.v2.CloudTasks.CreateTask] calls have significantly increased latency. Using hashed strings for the task id or for the prefix of the task id is recommended. Choosing task ids that are sequential or have sequential prefixes, for example using a timestamp, causes an increase in latency and error rates in all task commands. The infrastructure relies on an approximately uniform distribution of task ids to store and serve tasks efficiently.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task)` | The RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/queues/[QUEUE]";
    gctv::Task task = new gctv::Task();
    // Make the request
    gctv::Task response = cloudTasksClient.CreateTask(parent, task);
    

### CreateTaskAsync(CreateTaskRequest, CallSettings)
    
    
    public virtual Task<Task> CreateTaskAsync(CreateTaskRequest request, CallSettings callSettings = null)

Creates a task and adds it to a queue.

Tasks cannot be updated after creation; there is no UpdateTask command.

  * The maximum task size is 100KB.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateTaskRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CreateTaskRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::CreateTaskRequest request = new gctv::CreateTaskRequest
    {
        ParentAsQueueName = gctv::QueueName.FromProjectLocationQueue("[PROJECT]", "[LOCATION]", "[QUEUE]"),
        Task = new gctv::Task(),
        ResponseView = gctv::Task.Types.View.Unspecified,
    };
    // Make the request
    gctv::Task response = await cloudTasksClient.CreateTaskAsync(request);
    

### CreateTaskAsync(CreateTaskRequest, CancellationToken)
    
    
    public virtual Task<Task> CreateTaskAsync(CreateTaskRequest request, CancellationToken cancellationToken)

Creates a task and adds it to a queue.

Tasks cannot be updated after creation; there is no UpdateTask command.

  * The maximum task size is 100KB.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateTaskRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CreateTaskRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::CreateTaskRequest request = new gctv::CreateTaskRequest
    {
        ParentAsQueueName = gctv::QueueName.FromProjectLocationQueue("[PROJECT]", "[LOCATION]", "[QUEUE]"),
        Task = new gctv::Task(),
        ResponseView = gctv::Task.Types.View.Unspecified,
    };
    // Make the request
    gctv::Task response = await cloudTasksClient.CreateTaskAsync(request);
    

### CreateTaskAsync(QueueName, Task, CallSettings)
    
    
    public virtual Task<Task> CreateTaskAsync(QueueName parent, Task task, CallSettings callSettings = null)

Creates a task and adds it to a queue.

Tasks cannot be updated after creation; there is no UpdateTask command.

  * The maximum task size is 100KB.



**Parameters**  
---  
**Name** | **Description**  
`parent` | `[QueueName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.QueueName)`  
Required. The queue name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID` The queue must already exist.  
`task` | `[Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task)`  
Required. The task to add. Task names have the following format: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID`. The user can optionally specify a task [name][google.cloud.tasks.v2.Task.name]. If a name is not specified then the system will generate a random unique task id, which will be set in the task returned in the [response][google.cloud.tasks.v2.Task.name]. If [schedule_time][google.cloud.tasks.v2.Task.schedule_time] is not set or is in the past then Cloud Tasks will set it to the current time. Task De-duplication: Explicitly specifying a task ID enables task de-duplication. If a task's ID is identical to that of an existing task or a task that was deleted or executed recently then the call will fail with [ALREADY_EXISTS][google.rpc.Code.ALREADY_EXISTS]. The IDs of deleted tasks are not immediately available for reuse. It can take up to 24 hours (or 9 days if the task's queue was created using a queue.yaml or queue.xml) for the task ID to be released and made available again. Because there is an extra lookup cost to identify duplicate task names, these [CreateTask][google.cloud.tasks.v2.CloudTasks.CreateTask] calls have significantly increased latency. Using hashed strings for the task id or for the prefix of the task id is recommended. Choosing task ids that are sequential or have sequential prefixes, for example using a timestamp, causes an increase in latency and error rates in all task commands. The infrastructure relies on an approximately uniform distribution of task ids to store and serve tasks efficiently.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::QueueName parent = gctv::QueueName.FromProjectLocationQueue("[PROJECT]", "[LOCATION]", "[QUEUE]");
    gctv::Task task = new gctv::Task();
    // Make the request
    gctv::Task response = await cloudTasksClient.CreateTaskAsync(parent, task);
    

### CreateTaskAsync(QueueName, Task, CancellationToken)
    
    
    public virtual Task<Task> CreateTaskAsync(QueueName parent, Task task, CancellationToken cancellationToken)

Creates a task and adds it to a queue.

Tasks cannot be updated after creation; there is no UpdateTask command.

  * The maximum task size is 100KB.



**Parameters**  
---  
**Name** | **Description**  
`parent` | `[QueueName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.QueueName)`  
Required. The queue name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID` The queue must already exist.  
`task` | `[Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task)`  
Required. The task to add. Task names have the following format: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID`. The user can optionally specify a task [name][google.cloud.tasks.v2.Task.name]. If a name is not specified then the system will generate a random unique task id, which will be set in the task returned in the [response][google.cloud.tasks.v2.Task.name]. If [schedule_time][google.cloud.tasks.v2.Task.schedule_time] is not set or is in the past then Cloud Tasks will set it to the current time. Task De-duplication: Explicitly specifying a task ID enables task de-duplication. If a task's ID is identical to that of an existing task or a task that was deleted or executed recently then the call will fail with [ALREADY_EXISTS][google.rpc.Code.ALREADY_EXISTS]. The IDs of deleted tasks are not immediately available for reuse. It can take up to 24 hours (or 9 days if the task's queue was created using a queue.yaml or queue.xml) for the task ID to be released and made available again. Because there is an extra lookup cost to identify duplicate task names, these [CreateTask][google.cloud.tasks.v2.CloudTasks.CreateTask] calls have significantly increased latency. Using hashed strings for the task id or for the prefix of the task id is recommended. Choosing task ids that are sequential or have sequential prefixes, for example using a timestamp, causes an increase in latency and error rates in all task commands. The infrastructure relies on an approximately uniform distribution of task ids to store and serve tasks efficiently.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::QueueName parent = gctv::QueueName.FromProjectLocationQueue("[PROJECT]", "[LOCATION]", "[QUEUE]");
    gctv::Task task = new gctv::Task();
    // Make the request
    gctv::Task response = await cloudTasksClient.CreateTaskAsync(parent, task);
    

### CreateTaskAsync(string, Task, CallSettings)
    
    
    public virtual Task<Task> CreateTaskAsync(string parent, Task task, CallSettings callSettings = null)

Creates a task and adds it to a queue.

Tasks cannot be updated after creation; there is no UpdateTask command.

  * The maximum task size is 100KB.



**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The queue name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID` The queue must already exist.  
`task` | `[Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task)`  
Required. The task to add. Task names have the following format: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID`. The user can optionally specify a task [name][google.cloud.tasks.v2.Task.name]. If a name is not specified then the system will generate a random unique task id, which will be set in the task returned in the [response][google.cloud.tasks.v2.Task.name]. If [schedule_time][google.cloud.tasks.v2.Task.schedule_time] is not set or is in the past then Cloud Tasks will set it to the current time. Task De-duplication: Explicitly specifying a task ID enables task de-duplication. If a task's ID is identical to that of an existing task or a task that was deleted or executed recently then the call will fail with [ALREADY_EXISTS][google.rpc.Code.ALREADY_EXISTS]. The IDs of deleted tasks are not immediately available for reuse. It can take up to 24 hours (or 9 days if the task's queue was created using a queue.yaml or queue.xml) for the task ID to be released and made available again. Because there is an extra lookup cost to identify duplicate task names, these [CreateTask][google.cloud.tasks.v2.CloudTasks.CreateTask] calls have significantly increased latency. Using hashed strings for the task id or for the prefix of the task id is recommended. Choosing task ids that are sequential or have sequential prefixes, for example using a timestamp, causes an increase in latency and error rates in all task commands. The infrastructure relies on an approximately uniform distribution of task ids to store and serve tasks efficiently.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/queues/[QUEUE]";
    gctv::Task task = new gctv::Task();
    // Make the request
    gctv::Task response = await cloudTasksClient.CreateTaskAsync(parent, task);
    

### CreateTaskAsync(string, Task, CancellationToken)
    
    
    public virtual Task<Task> CreateTaskAsync(string parent, Task task, CancellationToken cancellationToken)

Creates a task and adds it to a queue.

Tasks cannot be updated after creation; there is no UpdateTask command.

  * The maximum task size is 100KB.



**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The queue name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID` The queue must already exist.  
`task` | `[Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task)`  
Required. The task to add. Task names have the following format: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID`. The user can optionally specify a task [name][google.cloud.tasks.v2.Task.name]. If a name is not specified then the system will generate a random unique task id, which will be set in the task returned in the [response][google.cloud.tasks.v2.Task.name]. If [schedule_time][google.cloud.tasks.v2.Task.schedule_time] is not set or is in the past then Cloud Tasks will set it to the current time. Task De-duplication: Explicitly specifying a task ID enables task de-duplication. If a task's ID is identical to that of an existing task or a task that was deleted or executed recently then the call will fail with [ALREADY_EXISTS][google.rpc.Code.ALREADY_EXISTS]. The IDs of deleted tasks are not immediately available for reuse. It can take up to 24 hours (or 9 days if the task's queue was created using a queue.yaml or queue.xml) for the task ID to be released and made available again. Because there is an extra lookup cost to identify duplicate task names, these [CreateTask][google.cloud.tasks.v2.CloudTasks.CreateTask] calls have significantly increased latency. Using hashed strings for the task id or for the prefix of the task id is recommended. Choosing task ids that are sequential or have sequential prefixes, for example using a timestamp, causes an increase in latency and error rates in all task commands. The infrastructure relies on an approximately uniform distribution of task ids to store and serve tasks efficiently.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/queues/[QUEUE]";
    gctv::Task task = new gctv::Task();
    // Make the request
    gctv::Task response = await cloudTasksClient.CreateTaskAsync(parent, task);
    

### DeleteQueue(DeleteQueueRequest, CallSettings)
    
    
    public virtual void DeleteQueue(DeleteQueueRequest request, CallSettings callSettings = null)

Deletes a queue.

This command will delete the queue even if it has tasks in it.

Note: If you delete a queue, you may be prevented from creating a new queue with the same name as the deleted queue for a tombstone window of up to 3 days. During this window, the CreateQueue operation may appear to recreate the queue, but this can be misleading. If you attempt to create a queue with the same name as one that is in the tombstone window, run GetQueue to confirm that the queue creation was successful. If GetQueue returns 200 response code, your queue was successfully created with the name of the previously deleted queue. Otherwise, your queue did not successfully recreate.

WARNING: Using this method may have unintended side effects if you are using an App Engine `queue.yaml` or `queue.xml` file to manage your queues. Read [Overview of Queue Management and queue.yaml](https://cloud.google.com/tasks/docs/queue-yaml) before using this method.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteQueueRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.DeleteQueueRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    gctv::DeleteQueueRequest request = new gctv::DeleteQueueRequest
    {
        QueueName = gctv::QueueName.FromProjectLocationQueue("[PROJECT]", "[LOCATION]", "[QUEUE]"),
    };
    // Make the request
    cloudTasksClient.DeleteQueue(request);
    

### DeleteQueue(QueueName, CallSettings)
    
    
    public virtual void DeleteQueue(QueueName name, CallSettings callSettings = null)

Deletes a queue.

This command will delete the queue even if it has tasks in it.

Note: If you delete a queue, you may be prevented from creating a new queue with the same name as the deleted queue for a tombstone window of up to 3 days. During this window, the CreateQueue operation may appear to recreate the queue, but this can be misleading. If you attempt to create a queue with the same name as one that is in the tombstone window, run GetQueue to confirm that the queue creation was successful. If GetQueue returns 200 response code, your queue was successfully created with the name of the previously deleted queue. Otherwise, your queue did not successfully recreate.

WARNING: Using this method may have unintended side effects if you are using an App Engine `queue.yaml` or `queue.xml` file to manage your queues. Read [Overview of Queue Management and queue.yaml](https://cloud.google.com/tasks/docs/queue-yaml) before using this method.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[QueueName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.QueueName)`  
Required. The queue name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    gctv::QueueName name = gctv::QueueName.FromProjectLocationQueue("[PROJECT]", "[LOCATION]", "[QUEUE]");
    // Make the request
    cloudTasksClient.DeleteQueue(name);
    

### DeleteQueue(string, CallSettings)
    
    
    public virtual void DeleteQueue(string name, CallSettings callSettings = null)

Deletes a queue.

This command will delete the queue even if it has tasks in it.

Note: If you delete a queue, you may be prevented from creating a new queue with the same name as the deleted queue for a tombstone window of up to 3 days. During this window, the CreateQueue operation may appear to recreate the queue, but this can be misleading. If you attempt to create a queue with the same name as one that is in the tombstone window, run GetQueue to confirm that the queue creation was successful. If GetQueue returns 200 response code, your queue was successfully created with the name of the previously deleted queue. Otherwise, your queue did not successfully recreate.

WARNING: Using this method may have unintended side effects if you are using an App Engine `queue.yaml` or `queue.xml` file to manage your queues. Read [Overview of Queue Management and queue.yaml](https://cloud.google.com/tasks/docs/queue-yaml) before using this method.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The queue name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/queues/[QUEUE]";
    // Make the request
    cloudTasksClient.DeleteQueue(name);
    

### DeleteQueueAsync(DeleteQueueRequest, CallSettings)
    
    
    public virtual Task DeleteQueueAsync(DeleteQueueRequest request, CallSettings callSettings = null)

Deletes a queue.

This command will delete the queue even if it has tasks in it.

Note: If you delete a queue, you may be prevented from creating a new queue with the same name as the deleted queue for a tombstone window of up to 3 days. During this window, the CreateQueue operation may appear to recreate the queue, but this can be misleading. If you attempt to create a queue with the same name as one that is in the tombstone window, run GetQueue to confirm that the queue creation was successful. If GetQueue returns 200 response code, your queue was successfully created with the name of the previously deleted queue. Otherwise, your queue did not successfully recreate.

WARNING: Using this method may have unintended side effects if you are using an App Engine `queue.yaml` or `queue.xml` file to manage your queues. Read [Overview of Queue Management and queue.yaml](https://cloud.google.com/tasks/docs/queue-yaml) before using this method.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteQueueRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.DeleteQueueRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::DeleteQueueRequest request = new gctv::DeleteQueueRequest
    {
        QueueName = gctv::QueueName.FromProjectLocationQueue("[PROJECT]", "[LOCATION]", "[QUEUE]"),
    };
    // Make the request
    await cloudTasksClient.DeleteQueueAsync(request);
    

### DeleteQueueAsync(DeleteQueueRequest, CancellationToken)
    
    
    public virtual Task DeleteQueueAsync(DeleteQueueRequest request, CancellationToken cancellationToken)

Deletes a queue.

This command will delete the queue even if it has tasks in it.

Note: If you delete a queue, you may be prevented from creating a new queue with the same name as the deleted queue for a tombstone window of up to 3 days. During this window, the CreateQueue operation may appear to recreate the queue, but this can be misleading. If you attempt to create a queue with the same name as one that is in the tombstone window, run GetQueue to confirm that the queue creation was successful. If GetQueue returns 200 response code, your queue was successfully created with the name of the previously deleted queue. Otherwise, your queue did not successfully recreate.

WARNING: Using this method may have unintended side effects if you are using an App Engine `queue.yaml` or `queue.xml` file to manage your queues. Read [Overview of Queue Management and queue.yaml](https://cloud.google.com/tasks/docs/queue-yaml) before using this method.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteQueueRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.DeleteQueueRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::DeleteQueueRequest request = new gctv::DeleteQueueRequest
    {
        QueueName = gctv::QueueName.FromProjectLocationQueue("[PROJECT]", "[LOCATION]", "[QUEUE]"),
    };
    // Make the request
    await cloudTasksClient.DeleteQueueAsync(request);
    

### DeleteQueueAsync(QueueName, CallSettings)
    
    
    public virtual Task DeleteQueueAsync(QueueName name, CallSettings callSettings = null)

Deletes a queue.

This command will delete the queue even if it has tasks in it.

Note: If you delete a queue, you may be prevented from creating a new queue with the same name as the deleted queue for a tombstone window of up to 3 days. During this window, the CreateQueue operation may appear to recreate the queue, but this can be misleading. If you attempt to create a queue with the same name as one that is in the tombstone window, run GetQueue to confirm that the queue creation was successful. If GetQueue returns 200 response code, your queue was successfully created with the name of the previously deleted queue. Otherwise, your queue did not successfully recreate.

WARNING: Using this method may have unintended side effects if you are using an App Engine `queue.yaml` or `queue.xml` file to manage your queues. Read [Overview of Queue Management and queue.yaml](https://cloud.google.com/tasks/docs/queue-yaml) before using this method.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[QueueName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.QueueName)`  
Required. The queue name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::QueueName name = gctv::QueueName.FromProjectLocationQueue("[PROJECT]", "[LOCATION]", "[QUEUE]");
    // Make the request
    await cloudTasksClient.DeleteQueueAsync(name);
    

### DeleteQueueAsync(QueueName, CancellationToken)
    
    
    public virtual Task DeleteQueueAsync(QueueName name, CancellationToken cancellationToken)

Deletes a queue.

This command will delete the queue even if it has tasks in it.

Note: If you delete a queue, you may be prevented from creating a new queue with the same name as the deleted queue for a tombstone window of up to 3 days. During this window, the CreateQueue operation may appear to recreate the queue, but this can be misleading. If you attempt to create a queue with the same name as one that is in the tombstone window, run GetQueue to confirm that the queue creation was successful. If GetQueue returns 200 response code, your queue was successfully created with the name of the previously deleted queue. Otherwise, your queue did not successfully recreate.

WARNING: Using this method may have unintended side effects if you are using an App Engine `queue.yaml` or `queue.xml` file to manage your queues. Read [Overview of Queue Management and queue.yaml](https://cloud.google.com/tasks/docs/queue-yaml) before using this method.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[QueueName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.QueueName)`  
Required. The queue name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::QueueName name = gctv::QueueName.FromProjectLocationQueue("[PROJECT]", "[LOCATION]", "[QUEUE]");
    // Make the request
    await cloudTasksClient.DeleteQueueAsync(name);
    

### DeleteQueueAsync(string, CallSettings)
    
    
    public virtual Task DeleteQueueAsync(string name, CallSettings callSettings = null)

Deletes a queue.

This command will delete the queue even if it has tasks in it.

Note: If you delete a queue, you may be prevented from creating a new queue with the same name as the deleted queue for a tombstone window of up to 3 days. During this window, the CreateQueue operation may appear to recreate the queue, but this can be misleading. If you attempt to create a queue with the same name as one that is in the tombstone window, run GetQueue to confirm that the queue creation was successful. If GetQueue returns 200 response code, your queue was successfully created with the name of the previously deleted queue. Otherwise, your queue did not successfully recreate.

WARNING: Using this method may have unintended side effects if you are using an App Engine `queue.yaml` or `queue.xml` file to manage your queues. Read [Overview of Queue Management and queue.yaml](https://cloud.google.com/tasks/docs/queue-yaml) before using this method.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The queue name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/queues/[QUEUE]";
    // Make the request
    await cloudTasksClient.DeleteQueueAsync(name);
    

### DeleteQueueAsync(string, CancellationToken)
    
    
    public virtual Task DeleteQueueAsync(string name, CancellationToken cancellationToken)

Deletes a queue.

This command will delete the queue even if it has tasks in it.

Note: If you delete a queue, you may be prevented from creating a new queue with the same name as the deleted queue for a tombstone window of up to 3 days. During this window, the CreateQueue operation may appear to recreate the queue, but this can be misleading. If you attempt to create a queue with the same name as one that is in the tombstone window, run GetQueue to confirm that the queue creation was successful. If GetQueue returns 200 response code, your queue was successfully created with the name of the previously deleted queue. Otherwise, your queue did not successfully recreate.

WARNING: Using this method may have unintended side effects if you are using an App Engine `queue.yaml` or `queue.xml` file to manage your queues. Read [Overview of Queue Management and queue.yaml](https://cloud.google.com/tasks/docs/queue-yaml) before using this method.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The queue name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/queues/[QUEUE]";
    // Make the request
    await cloudTasksClient.DeleteQueueAsync(name);
    

### DeleteTask(DeleteTaskRequest, CallSettings)
    
    
    public virtual void DeleteTask(DeleteTaskRequest request, CallSettings callSettings = null)

Deletes a task.

A task can be deleted if it is scheduled or dispatched. A task cannot be deleted if it has executed successfully or permanently failed.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteTaskRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.DeleteTaskRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    gctv::DeleteTaskRequest request = new gctv::DeleteTaskRequest
    {
        TaskName = gctv::TaskName.FromProjectLocationQueueTask("[PROJECT]", "[LOCATION]", "[QUEUE]", "[TASK]"),
    };
    // Make the request
    cloudTasksClient.DeleteTask(request);
    

### DeleteTask(TaskName, CallSettings)
    
    
    public virtual void DeleteTask(TaskName name, CallSettings callSettings = null)

Deletes a task.

A task can be deleted if it is scheduled or dispatched. A task cannot be deleted if it has executed successfully or permanently failed.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[TaskName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.TaskName)`  
Required. The task name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    gctv::TaskName name = gctv::TaskName.FromProjectLocationQueueTask("[PROJECT]", "[LOCATION]", "[QUEUE]", "[TASK]");
    // Make the request
    cloudTasksClient.DeleteTask(name);
    

### DeleteTask(string, CallSettings)
    
    
    public virtual void DeleteTask(string name, CallSettings callSettings = null)

Deletes a task.

A task can be deleted if it is scheduled or dispatched. A task cannot be deleted if it has executed successfully or permanently failed.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The task name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/queues/[QUEUE]/tasks/[TASK]";
    // Make the request
    cloudTasksClient.DeleteTask(name);
    

### DeleteTaskAsync(DeleteTaskRequest, CallSettings)
    
    
    public virtual Task DeleteTaskAsync(DeleteTaskRequest request, CallSettings callSettings = null)

Deletes a task.

A task can be deleted if it is scheduled or dispatched. A task cannot be deleted if it has executed successfully or permanently failed.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteTaskRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.DeleteTaskRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::DeleteTaskRequest request = new gctv::DeleteTaskRequest
    {
        TaskName = gctv::TaskName.FromProjectLocationQueueTask("[PROJECT]", "[LOCATION]", "[QUEUE]", "[TASK]"),
    };
    // Make the request
    await cloudTasksClient.DeleteTaskAsync(request);
    

### DeleteTaskAsync(DeleteTaskRequest, CancellationToken)
    
    
    public virtual Task DeleteTaskAsync(DeleteTaskRequest request, CancellationToken cancellationToken)

Deletes a task.

A task can be deleted if it is scheduled or dispatched. A task cannot be deleted if it has executed successfully or permanently failed.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteTaskRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.DeleteTaskRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::DeleteTaskRequest request = new gctv::DeleteTaskRequest
    {
        TaskName = gctv::TaskName.FromProjectLocationQueueTask("[PROJECT]", "[LOCATION]", "[QUEUE]", "[TASK]"),
    };
    // Make the request
    await cloudTasksClient.DeleteTaskAsync(request);
    

### DeleteTaskAsync(TaskName, CallSettings)
    
    
    public virtual Task DeleteTaskAsync(TaskName name, CallSettings callSettings = null)

Deletes a task.

A task can be deleted if it is scheduled or dispatched. A task cannot be deleted if it has executed successfully or permanently failed.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[TaskName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.TaskName)`  
Required. The task name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::TaskName name = gctv::TaskName.FromProjectLocationQueueTask("[PROJECT]", "[LOCATION]", "[QUEUE]", "[TASK]");
    // Make the request
    await cloudTasksClient.DeleteTaskAsync(name);
    

### DeleteTaskAsync(TaskName, CancellationToken)
    
    
    public virtual Task DeleteTaskAsync(TaskName name, CancellationToken cancellationToken)

Deletes a task.

A task can be deleted if it is scheduled or dispatched. A task cannot be deleted if it has executed successfully or permanently failed.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[TaskName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.TaskName)`  
Required. The task name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::TaskName name = gctv::TaskName.FromProjectLocationQueueTask("[PROJECT]", "[LOCATION]", "[QUEUE]", "[TASK]");
    // Make the request
    await cloudTasksClient.DeleteTaskAsync(name);
    

### DeleteTaskAsync(string, CallSettings)
    
    
    public virtual Task DeleteTaskAsync(string name, CallSettings callSettings = null)

Deletes a task.

A task can be deleted if it is scheduled or dispatched. A task cannot be deleted if it has executed successfully or permanently failed.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The task name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/queues/[QUEUE]/tasks/[TASK]";
    // Make the request
    await cloudTasksClient.DeleteTaskAsync(name);
    

### DeleteTaskAsync(string, CancellationToken)
    
    
    public virtual Task DeleteTaskAsync(string name, CancellationToken cancellationToken)

Deletes a task.

A task can be deleted if it is scheduled or dispatched. A task cannot be deleted if it has executed successfully or permanently failed.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The task name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/queues/[QUEUE]/tasks/[TASK]";
    // Make the request
    await cloudTasksClient.DeleteTaskAsync(name);
    

### GetCmekConfig(CmekConfigName, CallSettings)
    
    
    public virtual CmekConfig GetCmekConfig(CmekConfigName name, CallSettings callSettings = null)

Gets the CMEK config.

Gets the Customer Managed Encryption Key configured with the Cloud Tasks location. By default there is no kms_key configured.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[CmekConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CmekConfigName)`  
Required. The config. For example: `projects/PROJECT_ID/locations/LOCATION_ID/CmekConfig`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[CmekConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CmekConfig)` | The RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    gctv::CmekConfigName name = gctv::CmekConfigName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    gctv::CmekConfig response = cloudTasksClient.GetCmekConfig(name);
    

### GetCmekConfig(GetCmekConfigRequest, CallSettings)
    
    
    public virtual CmekConfig GetCmekConfig(GetCmekConfigRequest request, CallSettings callSettings = null)

Gets the CMEK config.

Gets the Customer Managed Encryption Key configured with the Cloud Tasks location. By default there is no kms_key configured.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCmekConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.GetCmekConfigRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[CmekConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CmekConfig)` | The RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    gctv::GetCmekConfigRequest request = new gctv::GetCmekConfigRequest
    {
        CmekConfigName = gctv::CmekConfigName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    gctv::CmekConfig response = cloudTasksClient.GetCmekConfig(request);
    

### GetCmekConfig(string, CallSettings)
    
    
    public virtual CmekConfig GetCmekConfig(string name, CallSettings callSettings = null)

Gets the CMEK config.

Gets the Customer Managed Encryption Key configured with the Cloud Tasks location. By default there is no kms_key configured.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The config. For example: `projects/PROJECT_ID/locations/LOCATION_ID/CmekConfig`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[CmekConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CmekConfig)` | The RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/cmekConfig";
    // Make the request
    gctv::CmekConfig response = cloudTasksClient.GetCmekConfig(name);
    

### GetCmekConfigAsync(CmekConfigName, CallSettings)
    
    
    public virtual Task<CmekConfig> GetCmekConfigAsync(CmekConfigName name, CallSettings callSettings = null)

Gets the CMEK config.

Gets the Customer Managed Encryption Key configured with the Cloud Tasks location. By default there is no kms_key configured.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[CmekConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CmekConfigName)`  
Required. The config. For example: `projects/PROJECT_ID/locations/LOCATION_ID/CmekConfig`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CmekConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CmekConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::CmekConfigName name = gctv::CmekConfigName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    gctv::CmekConfig response = await cloudTasksClient.GetCmekConfigAsync(name);
    

### GetCmekConfigAsync(CmekConfigName, CancellationToken)
    
    
    public virtual Task<CmekConfig> GetCmekConfigAsync(CmekConfigName name, CancellationToken cancellationToken)

Gets the CMEK config.

Gets the Customer Managed Encryption Key configured with the Cloud Tasks location. By default there is no kms_key configured.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[CmekConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CmekConfigName)`  
Required. The config. For example: `projects/PROJECT_ID/locations/LOCATION_ID/CmekConfig`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CmekConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CmekConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::CmekConfigName name = gctv::CmekConfigName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    gctv::CmekConfig response = await cloudTasksClient.GetCmekConfigAsync(name);
    

### GetCmekConfigAsync(GetCmekConfigRequest, CallSettings)
    
    
    public virtual Task<CmekConfig> GetCmekConfigAsync(GetCmekConfigRequest request, CallSettings callSettings = null)

Gets the CMEK config.

Gets the Customer Managed Encryption Key configured with the Cloud Tasks location. By default there is no kms_key configured.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCmekConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.GetCmekConfigRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CmekConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CmekConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::GetCmekConfigRequest request = new gctv::GetCmekConfigRequest
    {
        CmekConfigName = gctv::CmekConfigName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    gctv::CmekConfig response = await cloudTasksClient.GetCmekConfigAsync(request);
    

### GetCmekConfigAsync(GetCmekConfigRequest, CancellationToken)
    
    
    public virtual Task<CmekConfig> GetCmekConfigAsync(GetCmekConfigRequest request, CancellationToken cancellationToken)

Gets the CMEK config.

Gets the Customer Managed Encryption Key configured with the Cloud Tasks location. By default there is no kms_key configured.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCmekConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.GetCmekConfigRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CmekConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CmekConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::GetCmekConfigRequest request = new gctv::GetCmekConfigRequest
    {
        CmekConfigName = gctv::CmekConfigName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    gctv::CmekConfig response = await cloudTasksClient.GetCmekConfigAsync(request);
    

### GetCmekConfigAsync(string, CallSettings)
    
    
    public virtual Task<CmekConfig> GetCmekConfigAsync(string name, CallSettings callSettings = null)

Gets the CMEK config.

Gets the Customer Managed Encryption Key configured with the Cloud Tasks location. By default there is no kms_key configured.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The config. For example: `projects/PROJECT_ID/locations/LOCATION_ID/CmekConfig`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CmekConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CmekConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/cmekConfig";
    // Make the request
    gctv::CmekConfig response = await cloudTasksClient.GetCmekConfigAsync(name);
    

### GetCmekConfigAsync(string, CancellationToken)
    
    
    public virtual Task<CmekConfig> GetCmekConfigAsync(string name, CancellationToken cancellationToken)

Gets the CMEK config.

Gets the Customer Managed Encryption Key configured with the Cloud Tasks location. By default there is no kms_key configured.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The config. For example: `projects/PROJECT_ID/locations/LOCATION_ID/CmekConfig`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CmekConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CmekConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/cmekConfig";
    // Make the request
    gctv::CmekConfig response = await cloudTasksClient.GetCmekConfigAsync(name);
    

### GetIamPolicy(IResourceName, CallSettings)
    
    
    public virtual Policy GetIamPolicy(IResourceName resource, CallSettings callSettings = null)

Gets the access control policy for a [Queue][google.cloud.tasks.v2.Queue]. Returns an empty policy if the resource exists and does not have a policy set.

Authorization requires the following [Google IAM](https://cloud.google.com/iam) permission on the specified resource parent:

  * `cloudtasks.queues.getIamPolicy`



**Parameters**  
---  
**Name** | **Description**  
`resource` | `[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html)`  
REQUIRED: The resource for which the policy is being requested. See the operation documentation for the appropriate value for this field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | The RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    IResourceName resource = new UnparsedResourceName("a/wildcard/resource");
    // Make the request
    Policy response = cloudTasksClient.GetIamPolicy(resource);
    

### GetIamPolicy(GetIamPolicyRequest, CallSettings)
    
    
    public virtual Policy GetIamPolicy(GetIamPolicyRequest request, CallSettings callSettings = null)

Gets the access control policy for a [Queue][google.cloud.tasks.v2.Queue]. Returns an empty policy if the resource exists and does not have a policy set.

Authorization requires the following [Google IAM](https://cloud.google.com/iam) permission on the specified resource parent:

  * `cloudtasks.queues.getIamPolicy`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetIamPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.GetIamPolicyRequest.html)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | The RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    GetIamPolicyRequest request = new GetIamPolicyRequest
    {
        ResourceAsResourceName = new UnparsedResourceName("a/wildcard/resource"),
        Options = new GetPolicyOptions(),
    };
    // Make the request
    Policy response = cloudTasksClient.GetIamPolicy(request);
    

### GetIamPolicy(QueueName, CallSettings)
    
    
    public virtual Policy GetIamPolicy(QueueName resource, CallSettings callSettings = null)

Gets the access control policy for a [Queue][google.cloud.tasks.v2.Queue]. Returns an empty policy if the resource exists and does not have a policy set.

Authorization requires the following [Google IAM](https://cloud.google.com/iam) permission on the specified resource parent:

  * `cloudtasks.queues.getIamPolicy`



**Parameters**  
---  
**Name** | **Description**  
`resource` | `[QueueName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.QueueName)`  
REQUIRED: The resource for which the policy is being requested. See the operation documentation for the appropriate value for this field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | The RPC response.  
  
### GetIamPolicy(string, CallSettings)
    
    
    public virtual Policy GetIamPolicy(string resource, CallSettings callSettings = null)

Gets the access control policy for a [Queue][google.cloud.tasks.v2.Queue]. Returns an empty policy if the resource exists and does not have a policy set.

Authorization requires the following [Google IAM](https://cloud.google.com/iam) permission on the specified resource parent:

  * `cloudtasks.queues.getIamPolicy`



**Parameters**  
---  
**Name** | **Description**  
`resource` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
REQUIRED: The resource for which the policy is being requested. See the operation documentation for the appropriate value for this field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | The RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    string resource = "a/wildcard/resource";
    // Make the request
    Policy response = cloudTasksClient.GetIamPolicy(resource);
    

### GetIamPolicyAsync(IResourceName, CallSettings)
    
    
    public virtual Task<Policy> GetIamPolicyAsync(IResourceName resource, CallSettings callSettings = null)

Gets the access control policy for a [Queue][google.cloud.tasks.v2.Queue]. Returns an empty policy if the resource exists and does not have a policy set.

Authorization requires the following [Google IAM](https://cloud.google.com/iam) permission on the specified resource parent:

  * `cloudtasks.queues.getIamPolicy`



**Parameters**  
---  
**Name** | **Description**  
`resource` | `[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html)`  
REQUIRED: The resource for which the policy is being requested. See the operation documentation for the appropriate value for this field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    IResourceName resource = new UnparsedResourceName("a/wildcard/resource");
    // Make the request
    Policy response = await cloudTasksClient.GetIamPolicyAsync(resource);
    

### GetIamPolicyAsync(IResourceName, CancellationToken)
    
    
    public virtual Task<Policy> GetIamPolicyAsync(IResourceName resource, CancellationToken cancellationToken)

Gets the access control policy for a [Queue][google.cloud.tasks.v2.Queue]. Returns an empty policy if the resource exists and does not have a policy set.

Authorization requires the following [Google IAM](https://cloud.google.com/iam) permission on the specified resource parent:

  * `cloudtasks.queues.getIamPolicy`



**Parameters**  
---  
**Name** | **Description**  
`resource` | `[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html)`  
REQUIRED: The resource for which the policy is being requested. See the operation documentation for the appropriate value for this field.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    IResourceName resource = new UnparsedResourceName("a/wildcard/resource");
    // Make the request
    Policy response = await cloudTasksClient.GetIamPolicyAsync(resource);
    

### GetIamPolicyAsync(GetIamPolicyRequest, CallSettings)
    
    
    public virtual Task<Policy> GetIamPolicyAsync(GetIamPolicyRequest request, CallSettings callSettings = null)

Gets the access control policy for a [Queue][google.cloud.tasks.v2.Queue]. Returns an empty policy if the resource exists and does not have a policy set.

Authorization requires the following [Google IAM](https://cloud.google.com/iam) permission on the specified resource parent:

  * `cloudtasks.queues.getIamPolicy`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetIamPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.GetIamPolicyRequest.html)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    GetIamPolicyRequest request = new GetIamPolicyRequest
    {
        ResourceAsResourceName = new UnparsedResourceName("a/wildcard/resource"),
        Options = new GetPolicyOptions(),
    };
    // Make the request
    Policy response = await cloudTasksClient.GetIamPolicyAsync(request);
    

### GetIamPolicyAsync(GetIamPolicyRequest, CancellationToken)
    
    
    public virtual Task<Policy> GetIamPolicyAsync(GetIamPolicyRequest request, CancellationToken cancellationToken)

Gets the access control policy for a [Queue][google.cloud.tasks.v2.Queue]. Returns an empty policy if the resource exists and does not have a policy set.

Authorization requires the following [Google IAM](https://cloud.google.com/iam) permission on the specified resource parent:

  * `cloudtasks.queues.getIamPolicy`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetIamPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.GetIamPolicyRequest.html)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    GetIamPolicyRequest request = new GetIamPolicyRequest
    {
        ResourceAsResourceName = new UnparsedResourceName("a/wildcard/resource"),
        Options = new GetPolicyOptions(),
    };
    // Make the request
    Policy response = await cloudTasksClient.GetIamPolicyAsync(request);
    

### GetIamPolicyAsync(QueueName, CallSettings)
    
    
    public virtual Task<Policy> GetIamPolicyAsync(QueueName resource, CallSettings callSettings = null)

Gets the access control policy for a [Queue][google.cloud.tasks.v2.Queue]. Returns an empty policy if the resource exists and does not have a policy set.

Authorization requires the following [Google IAM](https://cloud.google.com/iam) permission on the specified resource parent:

  * `cloudtasks.queues.getIamPolicy`



**Parameters**  
---  
**Name** | **Description**  
`resource` | `[QueueName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.QueueName)`  
REQUIRED: The resource for which the policy is being requested. See the operation documentation for the appropriate value for this field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | A Task containing the RPC response.  
  
### GetIamPolicyAsync(QueueName, CancellationToken)
    
    
    public virtual Task<Policy> GetIamPolicyAsync(QueueName resource, CancellationToken cancellationToken)

Gets the access control policy for a [Queue][google.cloud.tasks.v2.Queue]. Returns an empty policy if the resource exists and does not have a policy set.

Authorization requires the following [Google IAM](https://cloud.google.com/iam) permission on the specified resource parent:

  * `cloudtasks.queues.getIamPolicy`



**Parameters**  
---  
**Name** | **Description**  
`resource` | `[QueueName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.QueueName)`  
REQUIRED: The resource for which the policy is being requested. See the operation documentation for the appropriate value for this field.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | A Task containing the RPC response.  
  
### GetIamPolicyAsync(string, CallSettings)
    
    
    public virtual Task<Policy> GetIamPolicyAsync(string resource, CallSettings callSettings = null)

Gets the access control policy for a [Queue][google.cloud.tasks.v2.Queue]. Returns an empty policy if the resource exists and does not have a policy set.

Authorization requires the following [Google IAM](https://cloud.google.com/iam) permission on the specified resource parent:

  * `cloudtasks.queues.getIamPolicy`



**Parameters**  
---  
**Name** | **Description**  
`resource` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
REQUIRED: The resource for which the policy is being requested. See the operation documentation for the appropriate value for this field.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    string resource = "a/wildcard/resource";
    // Make the request
    Policy response = await cloudTasksClient.GetIamPolicyAsync(resource);
    

### GetIamPolicyAsync(string, CancellationToken)
    
    
    public virtual Task<Policy> GetIamPolicyAsync(string resource, CancellationToken cancellationToken)

Gets the access control policy for a [Queue][google.cloud.tasks.v2.Queue]. Returns an empty policy if the resource exists and does not have a policy set.

Authorization requires the following [Google IAM](https://cloud.google.com/iam) permission on the specified resource parent:

  * `cloudtasks.queues.getIamPolicy`



**Parameters**  
---  
**Name** | **Description**  
`resource` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
REQUIRED: The resource for which the policy is being requested. See the operation documentation for the appropriate value for this field.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    string resource = "a/wildcard/resource";
    // Make the request
    Policy response = await cloudTasksClient.GetIamPolicyAsync(resource);
    

### GetQueue(GetQueueRequest, CallSettings)
    
    
    public virtual Queue GetQueue(GetQueueRequest request, CallSettings callSettings = null)

Gets a queue.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetQueueRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.GetQueueRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | The RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    gctv::GetQueueRequest request = new gctv::GetQueueRequest
    {
        QueueName = gctv::QueueName.FromProjectLocationQueue("[PROJECT]", "[LOCATION]", "[QUEUE]"),
    };
    // Make the request
    gctv::Queue response = cloudTasksClient.GetQueue(request);
    

### GetQueue(QueueName, CallSettings)
    
    
    public virtual Queue GetQueue(QueueName name, CallSettings callSettings = null)

Gets a queue.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[QueueName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.QueueName)`  
Required. The resource name of the queue. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | The RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    gctv::QueueName name = gctv::QueueName.FromProjectLocationQueue("[PROJECT]", "[LOCATION]", "[QUEUE]");
    // Make the request
    gctv::Queue response = cloudTasksClient.GetQueue(name);
    

### GetQueue(string, CallSettings)
    
    
    public virtual Queue GetQueue(string name, CallSettings callSettings = null)

Gets a queue.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the queue. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | The RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/queues/[QUEUE]";
    // Make the request
    gctv::Queue response = cloudTasksClient.GetQueue(name);
    

### GetQueueAsync(GetQueueRequest, CallSettings)
    
    
    public virtual Task<Queue> GetQueueAsync(GetQueueRequest request, CallSettings callSettings = null)

Gets a queue.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetQueueRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.GetQueueRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::GetQueueRequest request = new gctv::GetQueueRequest
    {
        QueueName = gctv::QueueName.FromProjectLocationQueue("[PROJECT]", "[LOCATION]", "[QUEUE]"),
    };
    // Make the request
    gctv::Queue response = await cloudTasksClient.GetQueueAsync(request);
    

### GetQueueAsync(GetQueueRequest, CancellationToken)
    
    
    public virtual Task<Queue> GetQueueAsync(GetQueueRequest request, CancellationToken cancellationToken)

Gets a queue.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetQueueRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.GetQueueRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::GetQueueRequest request = new gctv::GetQueueRequest
    {
        QueueName = gctv::QueueName.FromProjectLocationQueue("[PROJECT]", "[LOCATION]", "[QUEUE]"),
    };
    // Make the request
    gctv::Queue response = await cloudTasksClient.GetQueueAsync(request);
    

### GetQueueAsync(QueueName, CallSettings)
    
    
    public virtual Task<Queue> GetQueueAsync(QueueName name, CallSettings callSettings = null)

Gets a queue.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[QueueName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.QueueName)`  
Required. The resource name of the queue. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::QueueName name = gctv::QueueName.FromProjectLocationQueue("[PROJECT]", "[LOCATION]", "[QUEUE]");
    // Make the request
    gctv::Queue response = await cloudTasksClient.GetQueueAsync(name);
    

### GetQueueAsync(QueueName, CancellationToken)
    
    
    public virtual Task<Queue> GetQueueAsync(QueueName name, CancellationToken cancellationToken)

Gets a queue.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[QueueName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.QueueName)`  
Required. The resource name of the queue. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::QueueName name = gctv::QueueName.FromProjectLocationQueue("[PROJECT]", "[LOCATION]", "[QUEUE]");
    // Make the request
    gctv::Queue response = await cloudTasksClient.GetQueueAsync(name);
    

### GetQueueAsync(string, CallSettings)
    
    
    public virtual Task<Queue> GetQueueAsync(string name, CallSettings callSettings = null)

Gets a queue.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the queue. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/queues/[QUEUE]";
    // Make the request
    gctv::Queue response = await cloudTasksClient.GetQueueAsync(name);
    

### GetQueueAsync(string, CancellationToken)
    
    
    public virtual Task<Queue> GetQueueAsync(string name, CancellationToken cancellationToken)

Gets a queue.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the queue. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/queues/[QUEUE]";
    // Make the request
    gctv::Queue response = await cloudTasksClient.GetQueueAsync(name);
    

### GetTask(GetTaskRequest, CallSettings)
    
    
    public virtual Task GetTask(GetTaskRequest request, CallSettings callSettings = null)

Gets a task.

After a task is successfully executed or has exhausted its retry attempts, the task is deleted. A `GetTask` request for a deleted task returns a `NOT_FOUND` error.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetTaskRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.GetTaskRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task)` | The RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    gctv::GetTaskRequest request = new gctv::GetTaskRequest
    {
        TaskName = gctv::TaskName.FromProjectLocationQueueTask("[PROJECT]", "[LOCATION]", "[QUEUE]", "[TASK]"),
        ResponseView = gctv::Task.Types.View.Unspecified,
    };
    // Make the request
    gctv::Task response = cloudTasksClient.GetTask(request);
    

### GetTask(TaskName, CallSettings)
    
    
    public virtual Task GetTask(TaskName name, CallSettings callSettings = null)

Gets a task.

After a task is successfully executed or has exhausted its retry attempts, the task is deleted. A `GetTask` request for a deleted task returns a `NOT_FOUND` error.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[TaskName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.TaskName)`  
Required. The task name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task)` | The RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    gctv::TaskName name = gctv::TaskName.FromProjectLocationQueueTask("[PROJECT]", "[LOCATION]", "[QUEUE]", "[TASK]");
    // Make the request
    gctv::Task response = cloudTasksClient.GetTask(name);
    

### GetTask(string, CallSettings)
    
    
    public virtual Task GetTask(string name, CallSettings callSettings = null)

Gets a task.

After a task is successfully executed or has exhausted its retry attempts, the task is deleted. A `GetTask` request for a deleted task returns a `NOT_FOUND` error.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The task name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task)` | The RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/queues/[QUEUE]/tasks/[TASK]";
    // Make the request
    gctv::Task response = cloudTasksClient.GetTask(name);
    

### GetTaskAsync(GetTaskRequest, CallSettings)
    
    
    public virtual Task<Task> GetTaskAsync(GetTaskRequest request, CallSettings callSettings = null)

Gets a task.

After a task is successfully executed or has exhausted its retry attempts, the task is deleted. A `GetTask` request for a deleted task returns a `NOT_FOUND` error.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetTaskRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.GetTaskRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::GetTaskRequest request = new gctv::GetTaskRequest
    {
        TaskName = gctv::TaskName.FromProjectLocationQueueTask("[PROJECT]", "[LOCATION]", "[QUEUE]", "[TASK]"),
        ResponseView = gctv::Task.Types.View.Unspecified,
    };
    // Make the request
    gctv::Task response = await cloudTasksClient.GetTaskAsync(request);
    

### GetTaskAsync(GetTaskRequest, CancellationToken)
    
    
    public virtual Task<Task> GetTaskAsync(GetTaskRequest request, CancellationToken cancellationToken)

Gets a task.

After a task is successfully executed or has exhausted its retry attempts, the task is deleted. A `GetTask` request for a deleted task returns a `NOT_FOUND` error.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetTaskRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.GetTaskRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::GetTaskRequest request = new gctv::GetTaskRequest
    {
        TaskName = gctv::TaskName.FromProjectLocationQueueTask("[PROJECT]", "[LOCATION]", "[QUEUE]", "[TASK]"),
        ResponseView = gctv::Task.Types.View.Unspecified,
    };
    // Make the request
    gctv::Task response = await cloudTasksClient.GetTaskAsync(request);
    

### GetTaskAsync(TaskName, CallSettings)
    
    
    public virtual Task<Task> GetTaskAsync(TaskName name, CallSettings callSettings = null)

Gets a task.

After a task is successfully executed or has exhausted its retry attempts, the task is deleted. A `GetTask` request for a deleted task returns a `NOT_FOUND` error.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[TaskName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.TaskName)`  
Required. The task name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::TaskName name = gctv::TaskName.FromProjectLocationQueueTask("[PROJECT]", "[LOCATION]", "[QUEUE]", "[TASK]");
    // Make the request
    gctv::Task response = await cloudTasksClient.GetTaskAsync(name);
    

### GetTaskAsync(TaskName, CancellationToken)
    
    
    public virtual Task<Task> GetTaskAsync(TaskName name, CancellationToken cancellationToken)

Gets a task.

After a task is successfully executed or has exhausted its retry attempts, the task is deleted. A `GetTask` request for a deleted task returns a `NOT_FOUND` error.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[TaskName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.TaskName)`  
Required. The task name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::TaskName name = gctv::TaskName.FromProjectLocationQueueTask("[PROJECT]", "[LOCATION]", "[QUEUE]", "[TASK]");
    // Make the request
    gctv::Task response = await cloudTasksClient.GetTaskAsync(name);
    

### GetTaskAsync(string, CallSettings)
    
    
    public virtual Task<Task> GetTaskAsync(string name, CallSettings callSettings = null)

Gets a task.

After a task is successfully executed or has exhausted its retry attempts, the task is deleted. A `GetTask` request for a deleted task returns a `NOT_FOUND` error.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The task name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/queues/[QUEUE]/tasks/[TASK]";
    // Make the request
    gctv::Task response = await cloudTasksClient.GetTaskAsync(name);
    

### GetTaskAsync(string, CancellationToken)
    
    
    public virtual Task<Task> GetTaskAsync(string name, CancellationToken cancellationToken)

Gets a task.

After a task is successfully executed or has exhausted its retry attempts, the task is deleted. A `GetTask` request for a deleted task returns a `NOT_FOUND` error.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The task name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/queues/[QUEUE]/tasks/[TASK]";
    // Make the request
    gctv::Task response = await cloudTasksClient.GetTaskAsync(name);
    

### ListQueues(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListQueuesResponse, Queue> ListQueues(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists queues.

Queues are returned in lexicographical order.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The location name. For example: `projects/PROJECT_ID/locations/LOCATION_ID`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListQueuesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.ListQueuesResponse)[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | A pageable sequence of [Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue) resources.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<gctv::ListQueuesResponse, gctv::Queue> response = cloudTasksClient.ListQueues(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gctv::Queue item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gctv::ListQueuesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gctv::Queue item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gctv::Queue> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gctv::Queue item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListQueues(ListQueuesRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListQueuesResponse, Queue> ListQueues(ListQueuesRequest request, CallSettings callSettings = null)

Lists queues.

Queues are returned in lexicographical order.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListQueuesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.ListQueuesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListQueuesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.ListQueuesResponse)[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | A pageable sequence of [Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue) resources.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    gctv::ListQueuesRequest request = new gctv::ListQueuesRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
    };
    // Make the request
    PagedEnumerable<gctv::ListQueuesResponse, gctv::Queue> response = cloudTasksClient.ListQueues(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gctv::Queue item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gctv::ListQueuesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gctv::Queue item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gctv::Queue> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gctv::Queue item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListQueues(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListQueuesResponse, Queue> ListQueues(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists queues.

Queues are returned in lexicographical order.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The location name. For example: `projects/PROJECT_ID/locations/LOCATION_ID`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListQueuesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.ListQueuesResponse)[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | A pageable sequence of [Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue) resources.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<gctv::ListQueuesResponse, gctv::Queue> response = cloudTasksClient.ListQueues(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gctv::Queue item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gctv::ListQueuesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gctv::Queue item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gctv::Queue> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gctv::Queue item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListQueuesAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListQueuesResponse, Queue> ListQueuesAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists queues.

Queues are returned in lexicographical order.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The location name. For example: `projects/PROJECT_ID/locations/LOCATION_ID`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListQueuesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.ListQueuesResponse)[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | A pageable asynchronous sequence of [Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue) resources.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<gctv::ListQueuesResponse, gctv::Queue> response = cloudTasksClient.ListQueuesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gctv::Queue item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gctv::ListQueuesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gctv::Queue item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gctv::Queue> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gctv::Queue item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListQueuesAsync(ListQueuesRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListQueuesResponse, Queue> ListQueuesAsync(ListQueuesRequest request, CallSettings callSettings = null)

Lists queues.

Queues are returned in lexicographical order.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListQueuesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.ListQueuesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListQueuesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.ListQueuesResponse)[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | A pageable asynchronous sequence of [Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue) resources.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::ListQueuesRequest request = new gctv::ListQueuesRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
    };
    // Make the request
    PagedAsyncEnumerable<gctv::ListQueuesResponse, gctv::Queue> response = cloudTasksClient.ListQueuesAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gctv::Queue item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gctv::ListQueuesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gctv::Queue item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gctv::Queue> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gctv::Queue item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListQueuesAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListQueuesResponse, Queue> ListQueuesAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists queues.

Queues are returned in lexicographical order.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The location name. For example: `projects/PROJECT_ID/locations/LOCATION_ID`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListQueuesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.ListQueuesResponse)[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | A pageable asynchronous sequence of [Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue) resources.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<gctv::ListQueuesResponse, gctv::Queue> response = cloudTasksClient.ListQueuesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gctv::Queue item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gctv::ListQueuesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gctv::Queue item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gctv::Queue> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gctv::Queue item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListTasks(ListTasksRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListTasksResponse, Task> ListTasks(ListTasksRequest request, CallSettings callSettings = null)

Lists the tasks in a queue.

By default, only the [BASIC][google.cloud.tasks.v2.Task.View.BASIC] view is retrieved due to performance considerations; [response_view][google.cloud.tasks.v2.ListTasksRequest.response_view] controls the subset of information which is returned.

The tasks may be returned in any order. The ordering may change at any time.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListTasksRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.ListTasksRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListTasksResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.ListTasksResponse)[Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task)` | A pageable sequence of [Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task) resources.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    gctv::ListTasksRequest request = new gctv::ListTasksRequest
    {
        ParentAsQueueName = gctv::QueueName.FromProjectLocationQueue("[PROJECT]", "[LOCATION]", "[QUEUE]"),
        ResponseView = gctv::Task.Types.View.Unspecified,
    };
    // Make the request
    PagedEnumerable<gctv::ListTasksResponse, gctv::Task> response = cloudTasksClient.ListTasks(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gctv::Task item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gctv::ListTasksResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gctv::Task item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gctv::Task> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gctv::Task item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListTasks(QueueName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListTasksResponse, Task> ListTasks(QueueName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the tasks in a queue.

By default, only the [BASIC][google.cloud.tasks.v2.Task.View.BASIC] view is retrieved due to performance considerations; [response_view][google.cloud.tasks.v2.ListTasksRequest.response_view] controls the subset of information which is returned.

The tasks may be returned in any order. The ordering may change at any time.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[QueueName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.QueueName)`  
Required. The queue name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListTasksResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.ListTasksResponse)[Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task)` | A pageable sequence of [Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task) resources.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    gctv::QueueName parent = gctv::QueueName.FromProjectLocationQueue("[PROJECT]", "[LOCATION]", "[QUEUE]");
    // Make the request
    PagedEnumerable<gctv::ListTasksResponse, gctv::Task> response = cloudTasksClient.ListTasks(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gctv::Task item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gctv::ListTasksResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gctv::Task item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gctv::Task> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gctv::Task item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListTasks(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListTasksResponse, Task> ListTasks(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the tasks in a queue.

By default, only the [BASIC][google.cloud.tasks.v2.Task.View.BASIC] view is retrieved due to performance considerations; [response_view][google.cloud.tasks.v2.ListTasksRequest.response_view] controls the subset of information which is returned.

The tasks may be returned in any order. The ordering may change at any time.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The queue name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListTasksResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.ListTasksResponse)[Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task)` | A pageable sequence of [Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task) resources.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/queues/[QUEUE]";
    // Make the request
    PagedEnumerable<gctv::ListTasksResponse, gctv::Task> response = cloudTasksClient.ListTasks(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gctv::Task item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gctv::ListTasksResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gctv::Task item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gctv::Task> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gctv::Task item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListTasksAsync(ListTasksRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListTasksResponse, Task> ListTasksAsync(ListTasksRequest request, CallSettings callSettings = null)

Lists the tasks in a queue.

By default, only the [BASIC][google.cloud.tasks.v2.Task.View.BASIC] view is retrieved due to performance considerations; [response_view][google.cloud.tasks.v2.ListTasksRequest.response_view] controls the subset of information which is returned.

The tasks may be returned in any order. The ordering may change at any time.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListTasksRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.ListTasksRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListTasksResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.ListTasksResponse)[Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task)` | A pageable asynchronous sequence of [Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task) resources.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::ListTasksRequest request = new gctv::ListTasksRequest
    {
        ParentAsQueueName = gctv::QueueName.FromProjectLocationQueue("[PROJECT]", "[LOCATION]", "[QUEUE]"),
        ResponseView = gctv::Task.Types.View.Unspecified,
    };
    // Make the request
    PagedAsyncEnumerable<gctv::ListTasksResponse, gctv::Task> response = cloudTasksClient.ListTasksAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gctv::Task item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gctv::ListTasksResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gctv::Task item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gctv::Task> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gctv::Task item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListTasksAsync(QueueName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListTasksResponse, Task> ListTasksAsync(QueueName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the tasks in a queue.

By default, only the [BASIC][google.cloud.tasks.v2.Task.View.BASIC] view is retrieved due to performance considerations; [response_view][google.cloud.tasks.v2.ListTasksRequest.response_view] controls the subset of information which is returned.

The tasks may be returned in any order. The ordering may change at any time.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[QueueName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.QueueName)`  
Required. The queue name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListTasksResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.ListTasksResponse)[Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task)` | A pageable asynchronous sequence of [Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task) resources.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::QueueName parent = gctv::QueueName.FromProjectLocationQueue("[PROJECT]", "[LOCATION]", "[QUEUE]");
    // Make the request
    PagedAsyncEnumerable<gctv::ListTasksResponse, gctv::Task> response = cloudTasksClient.ListTasksAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gctv::Task item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gctv::ListTasksResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gctv::Task item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gctv::Task> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gctv::Task item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListTasksAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListTasksResponse, Task> ListTasksAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the tasks in a queue.

By default, only the [BASIC][google.cloud.tasks.v2.Task.View.BASIC] view is retrieved due to performance considerations; [response_view][google.cloud.tasks.v2.ListTasksRequest.response_view] controls the subset of information which is returned.

The tasks may be returned in any order. The ordering may change at any time.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The queue name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListTasksResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.ListTasksResponse)[Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task)` | A pageable asynchronous sequence of [Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task) resources.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/queues/[QUEUE]";
    // Make the request
    PagedAsyncEnumerable<gctv::ListTasksResponse, gctv::Task> response = cloudTasksClient.ListTasksAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gctv::Task item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gctv::ListTasksResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gctv::Task item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gctv::Task> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gctv::Task item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### PauseQueue(PauseQueueRequest, CallSettings)
    
    
    public virtual Queue PauseQueue(PauseQueueRequest request, CallSettings callSettings = null)

Pauses the queue.

If a queue is paused then the system will stop dispatching tasks until the queue is resumed via [ResumeQueue][google.cloud.tasks.v2.CloudTasks.ResumeQueue]. Tasks can still be added when the queue is paused. A queue is paused if its [state][google.cloud.tasks.v2.Queue.state] is [PAUSED][google.cloud.tasks.v2.Queue.State.PAUSED].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PauseQueueRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.PauseQueueRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | The RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    gctv::PauseQueueRequest request = new gctv::PauseQueueRequest
    {
        QueueName = gctv::QueueName.FromProjectLocationQueue("[PROJECT]", "[LOCATION]", "[QUEUE]"),
    };
    // Make the request
    gctv::Queue response = cloudTasksClient.PauseQueue(request);
    

### PauseQueue(QueueName, CallSettings)
    
    
    public virtual Queue PauseQueue(QueueName name, CallSettings callSettings = null)

Pauses the queue.

If a queue is paused then the system will stop dispatching tasks until the queue is resumed via [ResumeQueue][google.cloud.tasks.v2.CloudTasks.ResumeQueue]. Tasks can still be added when the queue is paused. A queue is paused if its [state][google.cloud.tasks.v2.Queue.state] is [PAUSED][google.cloud.tasks.v2.Queue.State.PAUSED].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[QueueName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.QueueName)`  
Required. The queue name. For example: `projects/PROJECT_ID/location/LOCATION_ID/queues/QUEUE_ID`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | The RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    gctv::QueueName name = gctv::QueueName.FromProjectLocationQueue("[PROJECT]", "[LOCATION]", "[QUEUE]");
    // Make the request
    gctv::Queue response = cloudTasksClient.PauseQueue(name);
    

### PauseQueue(string, CallSettings)
    
    
    public virtual Queue PauseQueue(string name, CallSettings callSettings = null)

Pauses the queue.

If a queue is paused then the system will stop dispatching tasks until the queue is resumed via [ResumeQueue][google.cloud.tasks.v2.CloudTasks.ResumeQueue]. Tasks can still be added when the queue is paused. A queue is paused if its [state][google.cloud.tasks.v2.Queue.state] is [PAUSED][google.cloud.tasks.v2.Queue.State.PAUSED].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The queue name. For example: `projects/PROJECT_ID/location/LOCATION_ID/queues/QUEUE_ID`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | The RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/queues/[QUEUE]";
    // Make the request
    gctv::Queue response = cloudTasksClient.PauseQueue(name);
    

### PauseQueueAsync(PauseQueueRequest, CallSettings)
    
    
    public virtual Task<Queue> PauseQueueAsync(PauseQueueRequest request, CallSettings callSettings = null)

Pauses the queue.

If a queue is paused then the system will stop dispatching tasks until the queue is resumed via [ResumeQueue][google.cloud.tasks.v2.CloudTasks.ResumeQueue]. Tasks can still be added when the queue is paused. A queue is paused if its [state][google.cloud.tasks.v2.Queue.state] is [PAUSED][google.cloud.tasks.v2.Queue.State.PAUSED].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PauseQueueRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.PauseQueueRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::PauseQueueRequest request = new gctv::PauseQueueRequest
    {
        QueueName = gctv::QueueName.FromProjectLocationQueue("[PROJECT]", "[LOCATION]", "[QUEUE]"),
    };
    // Make the request
    gctv::Queue response = await cloudTasksClient.PauseQueueAsync(request);
    

### PauseQueueAsync(PauseQueueRequest, CancellationToken)
    
    
    public virtual Task<Queue> PauseQueueAsync(PauseQueueRequest request, CancellationToken cancellationToken)

Pauses the queue.

If a queue is paused then the system will stop dispatching tasks until the queue is resumed via [ResumeQueue][google.cloud.tasks.v2.CloudTasks.ResumeQueue]. Tasks can still be added when the queue is paused. A queue is paused if its [state][google.cloud.tasks.v2.Queue.state] is [PAUSED][google.cloud.tasks.v2.Queue.State.PAUSED].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PauseQueueRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.PauseQueueRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::PauseQueueRequest request = new gctv::PauseQueueRequest
    {
        QueueName = gctv::QueueName.FromProjectLocationQueue("[PROJECT]", "[LOCATION]", "[QUEUE]"),
    };
    // Make the request
    gctv::Queue response = await cloudTasksClient.PauseQueueAsync(request);
    

### PauseQueueAsync(QueueName, CallSettings)
    
    
    public virtual Task<Queue> PauseQueueAsync(QueueName name, CallSettings callSettings = null)

Pauses the queue.

If a queue is paused then the system will stop dispatching tasks until the queue is resumed via [ResumeQueue][google.cloud.tasks.v2.CloudTasks.ResumeQueue]. Tasks can still be added when the queue is paused. A queue is paused if its [state][google.cloud.tasks.v2.Queue.state] is [PAUSED][google.cloud.tasks.v2.Queue.State.PAUSED].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[QueueName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.QueueName)`  
Required. The queue name. For example: `projects/PROJECT_ID/location/LOCATION_ID/queues/QUEUE_ID`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::QueueName name = gctv::QueueName.FromProjectLocationQueue("[PROJECT]", "[LOCATION]", "[QUEUE]");
    // Make the request
    gctv::Queue response = await cloudTasksClient.PauseQueueAsync(name);
    

### PauseQueueAsync(QueueName, CancellationToken)
    
    
    public virtual Task<Queue> PauseQueueAsync(QueueName name, CancellationToken cancellationToken)

Pauses the queue.

If a queue is paused then the system will stop dispatching tasks until the queue is resumed via [ResumeQueue][google.cloud.tasks.v2.CloudTasks.ResumeQueue]. Tasks can still be added when the queue is paused. A queue is paused if its [state][google.cloud.tasks.v2.Queue.state] is [PAUSED][google.cloud.tasks.v2.Queue.State.PAUSED].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[QueueName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.QueueName)`  
Required. The queue name. For example: `projects/PROJECT_ID/location/LOCATION_ID/queues/QUEUE_ID`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::QueueName name = gctv::QueueName.FromProjectLocationQueue("[PROJECT]", "[LOCATION]", "[QUEUE]");
    // Make the request
    gctv::Queue response = await cloudTasksClient.PauseQueueAsync(name);
    

### PauseQueueAsync(string, CallSettings)
    
    
    public virtual Task<Queue> PauseQueueAsync(string name, CallSettings callSettings = null)

Pauses the queue.

If a queue is paused then the system will stop dispatching tasks until the queue is resumed via [ResumeQueue][google.cloud.tasks.v2.CloudTasks.ResumeQueue]. Tasks can still be added when the queue is paused. A queue is paused if its [state][google.cloud.tasks.v2.Queue.state] is [PAUSED][google.cloud.tasks.v2.Queue.State.PAUSED].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The queue name. For example: `projects/PROJECT_ID/location/LOCATION_ID/queues/QUEUE_ID`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/queues/[QUEUE]";
    // Make the request
    gctv::Queue response = await cloudTasksClient.PauseQueueAsync(name);
    

### PauseQueueAsync(string, CancellationToken)
    
    
    public virtual Task<Queue> PauseQueueAsync(string name, CancellationToken cancellationToken)

Pauses the queue.

If a queue is paused then the system will stop dispatching tasks until the queue is resumed via [ResumeQueue][google.cloud.tasks.v2.CloudTasks.ResumeQueue]. Tasks can still be added when the queue is paused. A queue is paused if its [state][google.cloud.tasks.v2.Queue.state] is [PAUSED][google.cloud.tasks.v2.Queue.State.PAUSED].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The queue name. For example: `projects/PROJECT_ID/location/LOCATION_ID/queues/QUEUE_ID`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/queues/[QUEUE]";
    // Make the request
    gctv::Queue response = await cloudTasksClient.PauseQueueAsync(name);
    

### PollOnceBatchCreateTasks(string, CallSettings)
    
    
    public virtual Operation<BatchCreateTasksResponse, BatchCreateTasksMetadata> PollOnceBatchCreateTasks(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `BatchCreateTasks`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchCreateTasksResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchCreateTasksResponse)[BatchCreateTasksMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchCreateTasksMetadata)` | The result of polling the operation.  
  
### PollOnceBatchCreateTasksAsync(string, CallSettings)
    
    
    public virtual Task<Operation<BatchCreateTasksResponse, BatchCreateTasksMetadata>> PollOnceBatchCreateTasksAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `BatchCreateTasks`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchCreateTasksResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchCreateTasksResponse)[BatchCreateTasksMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchCreateTasksMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceBatchDeleteTasks(string, CallSettings)
    
    
    public virtual Operation<Empty, BatchDeleteTasksMetadata> PollOnceBatchDeleteTasks(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `BatchDeleteTasks`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[BatchDeleteTasksMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchDeleteTasksMetadata)` | The result of polling the operation.  
  
### PollOnceBatchDeleteTasksAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, BatchDeleteTasksMetadata>> PollOnceBatchDeleteTasksAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `BatchDeleteTasks`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[BatchDeleteTasksMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchDeleteTasksMetadata)` | A task representing the result of polling the operation.  
  
### PurgeQueue(PurgeQueueRequest, CallSettings)
    
    
    public virtual Queue PurgeQueue(PurgeQueueRequest request, CallSettings callSettings = null)

Purges a queue by deleting all of its tasks.

All tasks created before this method is called are permanently deleted.

Purge operations can take up to one minute to take effect. Tasks might be dispatched before the purge takes effect. A purge is irreversible.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PurgeQueueRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.PurgeQueueRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | The RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    gctv::PurgeQueueRequest request = new gctv::PurgeQueueRequest
    {
        QueueName = gctv::QueueName.FromProjectLocationQueue("[PROJECT]", "[LOCATION]", "[QUEUE]"),
    };
    // Make the request
    gctv::Queue response = cloudTasksClient.PurgeQueue(request);
    

### PurgeQueue(QueueName, CallSettings)
    
    
    public virtual Queue PurgeQueue(QueueName name, CallSettings callSettings = null)

Purges a queue by deleting all of its tasks.

All tasks created before this method is called are permanently deleted.

Purge operations can take up to one minute to take effect. Tasks might be dispatched before the purge takes effect. A purge is irreversible.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[QueueName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.QueueName)`  
Required. The queue name. For example: `projects/PROJECT_ID/location/LOCATION_ID/queues/QUEUE_ID`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | The RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    gctv::QueueName name = gctv::QueueName.FromProjectLocationQueue("[PROJECT]", "[LOCATION]", "[QUEUE]");
    // Make the request
    gctv::Queue response = cloudTasksClient.PurgeQueue(name);
    

### PurgeQueue(string, CallSettings)
    
    
    public virtual Queue PurgeQueue(string name, CallSettings callSettings = null)

Purges a queue by deleting all of its tasks.

All tasks created before this method is called are permanently deleted.

Purge operations can take up to one minute to take effect. Tasks might be dispatched before the purge takes effect. A purge is irreversible.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The queue name. For example: `projects/PROJECT_ID/location/LOCATION_ID/queues/QUEUE_ID`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | The RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/queues/[QUEUE]";
    // Make the request
    gctv::Queue response = cloudTasksClient.PurgeQueue(name);
    

### PurgeQueueAsync(PurgeQueueRequest, CallSettings)
    
    
    public virtual Task<Queue> PurgeQueueAsync(PurgeQueueRequest request, CallSettings callSettings = null)

Purges a queue by deleting all of its tasks.

All tasks created before this method is called are permanently deleted.

Purge operations can take up to one minute to take effect. Tasks might be dispatched before the purge takes effect. A purge is irreversible.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PurgeQueueRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.PurgeQueueRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::PurgeQueueRequest request = new gctv::PurgeQueueRequest
    {
        QueueName = gctv::QueueName.FromProjectLocationQueue("[PROJECT]", "[LOCATION]", "[QUEUE]"),
    };
    // Make the request
    gctv::Queue response = await cloudTasksClient.PurgeQueueAsync(request);
    

### PurgeQueueAsync(PurgeQueueRequest, CancellationToken)
    
    
    public virtual Task<Queue> PurgeQueueAsync(PurgeQueueRequest request, CancellationToken cancellationToken)

Purges a queue by deleting all of its tasks.

All tasks created before this method is called are permanently deleted.

Purge operations can take up to one minute to take effect. Tasks might be dispatched before the purge takes effect. A purge is irreversible.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PurgeQueueRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.PurgeQueueRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::PurgeQueueRequest request = new gctv::PurgeQueueRequest
    {
        QueueName = gctv::QueueName.FromProjectLocationQueue("[PROJECT]", "[LOCATION]", "[QUEUE]"),
    };
    // Make the request
    gctv::Queue response = await cloudTasksClient.PurgeQueueAsync(request);
    

### PurgeQueueAsync(QueueName, CallSettings)
    
    
    public virtual Task<Queue> PurgeQueueAsync(QueueName name, CallSettings callSettings = null)

Purges a queue by deleting all of its tasks.

All tasks created before this method is called are permanently deleted.

Purge operations can take up to one minute to take effect. Tasks might be dispatched before the purge takes effect. A purge is irreversible.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[QueueName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.QueueName)`  
Required. The queue name. For example: `projects/PROJECT_ID/location/LOCATION_ID/queues/QUEUE_ID`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::QueueName name = gctv::QueueName.FromProjectLocationQueue("[PROJECT]", "[LOCATION]", "[QUEUE]");
    // Make the request
    gctv::Queue response = await cloudTasksClient.PurgeQueueAsync(name);
    

### PurgeQueueAsync(QueueName, CancellationToken)
    
    
    public virtual Task<Queue> PurgeQueueAsync(QueueName name, CancellationToken cancellationToken)

Purges a queue by deleting all of its tasks.

All tasks created before this method is called are permanently deleted.

Purge operations can take up to one minute to take effect. Tasks might be dispatched before the purge takes effect. A purge is irreversible.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[QueueName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.QueueName)`  
Required. The queue name. For example: `projects/PROJECT_ID/location/LOCATION_ID/queues/QUEUE_ID`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::QueueName name = gctv::QueueName.FromProjectLocationQueue("[PROJECT]", "[LOCATION]", "[QUEUE]");
    // Make the request
    gctv::Queue response = await cloudTasksClient.PurgeQueueAsync(name);
    

### PurgeQueueAsync(string, CallSettings)
    
    
    public virtual Task<Queue> PurgeQueueAsync(string name, CallSettings callSettings = null)

Purges a queue by deleting all of its tasks.

All tasks created before this method is called are permanently deleted.

Purge operations can take up to one minute to take effect. Tasks might be dispatched before the purge takes effect. A purge is irreversible.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The queue name. For example: `projects/PROJECT_ID/location/LOCATION_ID/queues/QUEUE_ID`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/queues/[QUEUE]";
    // Make the request
    gctv::Queue response = await cloudTasksClient.PurgeQueueAsync(name);
    

### PurgeQueueAsync(string, CancellationToken)
    
    
    public virtual Task<Queue> PurgeQueueAsync(string name, CancellationToken cancellationToken)

Purges a queue by deleting all of its tasks.

All tasks created before this method is called are permanently deleted.

Purge operations can take up to one minute to take effect. Tasks might be dispatched before the purge takes effect. A purge is irreversible.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The queue name. For example: `projects/PROJECT_ID/location/LOCATION_ID/queues/QUEUE_ID`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/queues/[QUEUE]";
    // Make the request
    gctv::Queue response = await cloudTasksClient.PurgeQueueAsync(name);
    

### ResumeQueue(QueueName, CallSettings)
    
    
    public virtual Queue ResumeQueue(QueueName name, CallSettings callSettings = null)

Resume a queue.

This method resumes a queue after it has been [PAUSED][google.cloud.tasks.v2.Queue.State.PAUSED] or [DISABLED][google.cloud.tasks.v2.Queue.State.DISABLED]. The state of a queue is stored in the queue's [state][google.cloud.tasks.v2.Queue.state]; after calling this method it will be set to [RUNNING][google.cloud.tasks.v2.Queue.State.RUNNING].

WARNING: Resuming many high-QPS queues at the same time can lead to target overloading. If you are resuming high-QPS queues, follow the 500/50/5 pattern described in [Managing Cloud Tasks Scaling Risks](https://cloud.google.com/tasks/docs/manage-cloud-task-scaling).

**Parameters**  
---  
**Name** | **Description**  
`name` | `[QueueName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.QueueName)`  
Required. The queue name. For example: `projects/PROJECT_ID/location/LOCATION_ID/queues/QUEUE_ID`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | The RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    gctv::QueueName name = gctv::QueueName.FromProjectLocationQueue("[PROJECT]", "[LOCATION]", "[QUEUE]");
    // Make the request
    gctv::Queue response = cloudTasksClient.ResumeQueue(name);
    

### ResumeQueue(ResumeQueueRequest, CallSettings)
    
    
    public virtual Queue ResumeQueue(ResumeQueueRequest request, CallSettings callSettings = null)

Resume a queue.

This method resumes a queue after it has been [PAUSED][google.cloud.tasks.v2.Queue.State.PAUSED] or [DISABLED][google.cloud.tasks.v2.Queue.State.DISABLED]. The state of a queue is stored in the queue's [state][google.cloud.tasks.v2.Queue.state]; after calling this method it will be set to [RUNNING][google.cloud.tasks.v2.Queue.State.RUNNING].

WARNING: Resuming many high-QPS queues at the same time can lead to target overloading. If you are resuming high-QPS queues, follow the 500/50/5 pattern described in [Managing Cloud Tasks Scaling Risks](https://cloud.google.com/tasks/docs/manage-cloud-task-scaling).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ResumeQueueRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.ResumeQueueRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | The RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    gctv::ResumeQueueRequest request = new gctv::ResumeQueueRequest
    {
        QueueName = gctv::QueueName.FromProjectLocationQueue("[PROJECT]", "[LOCATION]", "[QUEUE]"),
    };
    // Make the request
    gctv::Queue response = cloudTasksClient.ResumeQueue(request);
    

### ResumeQueue(string, CallSettings)
    
    
    public virtual Queue ResumeQueue(string name, CallSettings callSettings = null)

Resume a queue.

This method resumes a queue after it has been [PAUSED][google.cloud.tasks.v2.Queue.State.PAUSED] or [DISABLED][google.cloud.tasks.v2.Queue.State.DISABLED]. The state of a queue is stored in the queue's [state][google.cloud.tasks.v2.Queue.state]; after calling this method it will be set to [RUNNING][google.cloud.tasks.v2.Queue.State.RUNNING].

WARNING: Resuming many high-QPS queues at the same time can lead to target overloading. If you are resuming high-QPS queues, follow the 500/50/5 pattern described in [Managing Cloud Tasks Scaling Risks](https://cloud.google.com/tasks/docs/manage-cloud-task-scaling).

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The queue name. For example: `projects/PROJECT_ID/location/LOCATION_ID/queues/QUEUE_ID`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | The RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/queues/[QUEUE]";
    // Make the request
    gctv::Queue response = cloudTasksClient.ResumeQueue(name);
    

### ResumeQueueAsync(QueueName, CallSettings)
    
    
    public virtual Task<Queue> ResumeQueueAsync(QueueName name, CallSettings callSettings = null)

Resume a queue.

This method resumes a queue after it has been [PAUSED][google.cloud.tasks.v2.Queue.State.PAUSED] or [DISABLED][google.cloud.tasks.v2.Queue.State.DISABLED]. The state of a queue is stored in the queue's [state][google.cloud.tasks.v2.Queue.state]; after calling this method it will be set to [RUNNING][google.cloud.tasks.v2.Queue.State.RUNNING].

WARNING: Resuming many high-QPS queues at the same time can lead to target overloading. If you are resuming high-QPS queues, follow the 500/50/5 pattern described in [Managing Cloud Tasks Scaling Risks](https://cloud.google.com/tasks/docs/manage-cloud-task-scaling).

**Parameters**  
---  
**Name** | **Description**  
`name` | `[QueueName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.QueueName)`  
Required. The queue name. For example: `projects/PROJECT_ID/location/LOCATION_ID/queues/QUEUE_ID`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::QueueName name = gctv::QueueName.FromProjectLocationQueue("[PROJECT]", "[LOCATION]", "[QUEUE]");
    // Make the request
    gctv::Queue response = await cloudTasksClient.ResumeQueueAsync(name);
    

### ResumeQueueAsync(QueueName, CancellationToken)
    
    
    public virtual Task<Queue> ResumeQueueAsync(QueueName name, CancellationToken cancellationToken)

Resume a queue.

This method resumes a queue after it has been [PAUSED][google.cloud.tasks.v2.Queue.State.PAUSED] or [DISABLED][google.cloud.tasks.v2.Queue.State.DISABLED]. The state of a queue is stored in the queue's [state][google.cloud.tasks.v2.Queue.state]; after calling this method it will be set to [RUNNING][google.cloud.tasks.v2.Queue.State.RUNNING].

WARNING: Resuming many high-QPS queues at the same time can lead to target overloading. If you are resuming high-QPS queues, follow the 500/50/5 pattern described in [Managing Cloud Tasks Scaling Risks](https://cloud.google.com/tasks/docs/manage-cloud-task-scaling).

**Parameters**  
---  
**Name** | **Description**  
`name` | `[QueueName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.QueueName)`  
Required. The queue name. For example: `projects/PROJECT_ID/location/LOCATION_ID/queues/QUEUE_ID`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::QueueName name = gctv::QueueName.FromProjectLocationQueue("[PROJECT]", "[LOCATION]", "[QUEUE]");
    // Make the request
    gctv::Queue response = await cloudTasksClient.ResumeQueueAsync(name);
    

### ResumeQueueAsync(ResumeQueueRequest, CallSettings)
    
    
    public virtual Task<Queue> ResumeQueueAsync(ResumeQueueRequest request, CallSettings callSettings = null)

Resume a queue.

This method resumes a queue after it has been [PAUSED][google.cloud.tasks.v2.Queue.State.PAUSED] or [DISABLED][google.cloud.tasks.v2.Queue.State.DISABLED]. The state of a queue is stored in the queue's [state][google.cloud.tasks.v2.Queue.state]; after calling this method it will be set to [RUNNING][google.cloud.tasks.v2.Queue.State.RUNNING].

WARNING: Resuming many high-QPS queues at the same time can lead to target overloading. If you are resuming high-QPS queues, follow the 500/50/5 pattern described in [Managing Cloud Tasks Scaling Risks](https://cloud.google.com/tasks/docs/manage-cloud-task-scaling).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ResumeQueueRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.ResumeQueueRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::ResumeQueueRequest request = new gctv::ResumeQueueRequest
    {
        QueueName = gctv::QueueName.FromProjectLocationQueue("[PROJECT]", "[LOCATION]", "[QUEUE]"),
    };
    // Make the request
    gctv::Queue response = await cloudTasksClient.ResumeQueueAsync(request);
    

### ResumeQueueAsync(ResumeQueueRequest, CancellationToken)
    
    
    public virtual Task<Queue> ResumeQueueAsync(ResumeQueueRequest request, CancellationToken cancellationToken)

Resume a queue.

This method resumes a queue after it has been [PAUSED][google.cloud.tasks.v2.Queue.State.PAUSED] or [DISABLED][google.cloud.tasks.v2.Queue.State.DISABLED]. The state of a queue is stored in the queue's [state][google.cloud.tasks.v2.Queue.state]; after calling this method it will be set to [RUNNING][google.cloud.tasks.v2.Queue.State.RUNNING].

WARNING: Resuming many high-QPS queues at the same time can lead to target overloading. If you are resuming high-QPS queues, follow the 500/50/5 pattern described in [Managing Cloud Tasks Scaling Risks](https://cloud.google.com/tasks/docs/manage-cloud-task-scaling).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ResumeQueueRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.ResumeQueueRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::ResumeQueueRequest request = new gctv::ResumeQueueRequest
    {
        QueueName = gctv::QueueName.FromProjectLocationQueue("[PROJECT]", "[LOCATION]", "[QUEUE]"),
    };
    // Make the request
    gctv::Queue response = await cloudTasksClient.ResumeQueueAsync(request);
    

### ResumeQueueAsync(string, CallSettings)
    
    
    public virtual Task<Queue> ResumeQueueAsync(string name, CallSettings callSettings = null)

Resume a queue.

This method resumes a queue after it has been [PAUSED][google.cloud.tasks.v2.Queue.State.PAUSED] or [DISABLED][google.cloud.tasks.v2.Queue.State.DISABLED]. The state of a queue is stored in the queue's [state][google.cloud.tasks.v2.Queue.state]; after calling this method it will be set to [RUNNING][google.cloud.tasks.v2.Queue.State.RUNNING].

WARNING: Resuming many high-QPS queues at the same time can lead to target overloading. If you are resuming high-QPS queues, follow the 500/50/5 pattern described in [Managing Cloud Tasks Scaling Risks](https://cloud.google.com/tasks/docs/manage-cloud-task-scaling).

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The queue name. For example: `projects/PROJECT_ID/location/LOCATION_ID/queues/QUEUE_ID`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/queues/[QUEUE]";
    // Make the request
    gctv::Queue response = await cloudTasksClient.ResumeQueueAsync(name);
    

### ResumeQueueAsync(string, CancellationToken)
    
    
    public virtual Task<Queue> ResumeQueueAsync(string name, CancellationToken cancellationToken)

Resume a queue.

This method resumes a queue after it has been [PAUSED][google.cloud.tasks.v2.Queue.State.PAUSED] or [DISABLED][google.cloud.tasks.v2.Queue.State.DISABLED]. The state of a queue is stored in the queue's [state][google.cloud.tasks.v2.Queue.state]; after calling this method it will be set to [RUNNING][google.cloud.tasks.v2.Queue.State.RUNNING].

WARNING: Resuming many high-QPS queues at the same time can lead to target overloading. If you are resuming high-QPS queues, follow the 500/50/5 pattern described in [Managing Cloud Tasks Scaling Risks](https://cloud.google.com/tasks/docs/manage-cloud-task-scaling).

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The queue name. For example: `projects/PROJECT_ID/location/LOCATION_ID/queues/QUEUE_ID`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/queues/[QUEUE]";
    // Make the request
    gctv::Queue response = await cloudTasksClient.ResumeQueueAsync(name);
    

### RunTask(RunTaskRequest, CallSettings)
    
    
    public virtual Task RunTask(RunTaskRequest request, CallSettings callSettings = null)

Forces a task to run now.

When this method is called, Cloud Tasks will dispatch the task, even if the task is already running, the queue has reached its [RateLimits][google.cloud.tasks.v2.RateLimits] or is [PAUSED][google.cloud.tasks.v2.Queue.State.PAUSED].

This command is meant to be used for manual debugging. For example, [RunTask][google.cloud.tasks.v2.CloudTasks.RunTask] can be used to retry a failed task after a fix has been made or to manually force a task to be dispatched now.

If Cloud Tasks receives a successful response from the task's target, then the task will be deleted; otherwise the task's [schedule_time][google.cloud.tasks.v2.Task.schedule_time] will be reset to the time that [RunTask][google.cloud.tasks.v2.CloudTasks.RunTask] was called plus the retry delay specified in the queue's [RetryConfig][google.cloud.tasks.v2.RetryConfig].

[RunTask][google.cloud.tasks.v2.CloudTasks.RunTask] returns [NOT_FOUND][google.rpc.Code.NOT_FOUND] when it is called on a task that has already succeeded or permanently failed.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RunTaskRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.RunTaskRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task)` | The RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    gctv::RunTaskRequest request = new gctv::RunTaskRequest
    {
        TaskName = gctv::TaskName.FromProjectLocationQueueTask("[PROJECT]", "[LOCATION]", "[QUEUE]", "[TASK]"),
        ResponseView = gctv::Task.Types.View.Unspecified,
    };
    // Make the request
    gctv::Task response = cloudTasksClient.RunTask(request);
    

### RunTask(TaskName, CallSettings)
    
    
    public virtual Task RunTask(TaskName name, CallSettings callSettings = null)

Forces a task to run now.

When this method is called, Cloud Tasks will dispatch the task, even if the task is already running, the queue has reached its [RateLimits][google.cloud.tasks.v2.RateLimits] or is [PAUSED][google.cloud.tasks.v2.Queue.State.PAUSED].

This command is meant to be used for manual debugging. For example, [RunTask][google.cloud.tasks.v2.CloudTasks.RunTask] can be used to retry a failed task after a fix has been made or to manually force a task to be dispatched now.

If Cloud Tasks receives a successful response from the task's target, then the task will be deleted; otherwise the task's [schedule_time][google.cloud.tasks.v2.Task.schedule_time] will be reset to the time that [RunTask][google.cloud.tasks.v2.CloudTasks.RunTask] was called plus the retry delay specified in the queue's [RetryConfig][google.cloud.tasks.v2.RetryConfig].

[RunTask][google.cloud.tasks.v2.CloudTasks.RunTask] returns [NOT_FOUND][google.rpc.Code.NOT_FOUND] when it is called on a task that has already succeeded or permanently failed.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[TaskName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.TaskName)`  
Required. The task name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task)` | The RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    gctv::TaskName name = gctv::TaskName.FromProjectLocationQueueTask("[PROJECT]", "[LOCATION]", "[QUEUE]", "[TASK]");
    // Make the request
    gctv::Task response = cloudTasksClient.RunTask(name);
    

### RunTask(string, CallSettings)
    
    
    public virtual Task RunTask(string name, CallSettings callSettings = null)

Forces a task to run now.

When this method is called, Cloud Tasks will dispatch the task, even if the task is already running, the queue has reached its [RateLimits][google.cloud.tasks.v2.RateLimits] or is [PAUSED][google.cloud.tasks.v2.Queue.State.PAUSED].

This command is meant to be used for manual debugging. For example, [RunTask][google.cloud.tasks.v2.CloudTasks.RunTask] can be used to retry a failed task after a fix has been made or to manually force a task to be dispatched now.

If Cloud Tasks receives a successful response from the task's target, then the task will be deleted; otherwise the task's [schedule_time][google.cloud.tasks.v2.Task.schedule_time] will be reset to the time that [RunTask][google.cloud.tasks.v2.CloudTasks.RunTask] was called plus the retry delay specified in the queue's [RetryConfig][google.cloud.tasks.v2.RetryConfig].

[RunTask][google.cloud.tasks.v2.CloudTasks.RunTask] returns [NOT_FOUND][google.rpc.Code.NOT_FOUND] when it is called on a task that has already succeeded or permanently failed.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The task name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task)` | The RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/queues/[QUEUE]/tasks/[TASK]";
    // Make the request
    gctv::Task response = cloudTasksClient.RunTask(name);
    

### RunTaskAsync(RunTaskRequest, CallSettings)
    
    
    public virtual Task<Task> RunTaskAsync(RunTaskRequest request, CallSettings callSettings = null)

Forces a task to run now.

When this method is called, Cloud Tasks will dispatch the task, even if the task is already running, the queue has reached its [RateLimits][google.cloud.tasks.v2.RateLimits] or is [PAUSED][google.cloud.tasks.v2.Queue.State.PAUSED].

This command is meant to be used for manual debugging. For example, [RunTask][google.cloud.tasks.v2.CloudTasks.RunTask] can be used to retry a failed task after a fix has been made or to manually force a task to be dispatched now.

If Cloud Tasks receives a successful response from the task's target, then the task will be deleted; otherwise the task's [schedule_time][google.cloud.tasks.v2.Task.schedule_time] will be reset to the time that [RunTask][google.cloud.tasks.v2.CloudTasks.RunTask] was called plus the retry delay specified in the queue's [RetryConfig][google.cloud.tasks.v2.RetryConfig].

[RunTask][google.cloud.tasks.v2.CloudTasks.RunTask] returns [NOT_FOUND][google.rpc.Code.NOT_FOUND] when it is called on a task that has already succeeded or permanently failed.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RunTaskRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.RunTaskRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::RunTaskRequest request = new gctv::RunTaskRequest
    {
        TaskName = gctv::TaskName.FromProjectLocationQueueTask("[PROJECT]", "[LOCATION]", "[QUEUE]", "[TASK]"),
        ResponseView = gctv::Task.Types.View.Unspecified,
    };
    // Make the request
    gctv::Task response = await cloudTasksClient.RunTaskAsync(request);
    

### RunTaskAsync(RunTaskRequest, CancellationToken)
    
    
    public virtual Task<Task> RunTaskAsync(RunTaskRequest request, CancellationToken cancellationToken)

Forces a task to run now.

When this method is called, Cloud Tasks will dispatch the task, even if the task is already running, the queue has reached its [RateLimits][google.cloud.tasks.v2.RateLimits] or is [PAUSED][google.cloud.tasks.v2.Queue.State.PAUSED].

This command is meant to be used for manual debugging. For example, [RunTask][google.cloud.tasks.v2.CloudTasks.RunTask] can be used to retry a failed task after a fix has been made or to manually force a task to be dispatched now.

If Cloud Tasks receives a successful response from the task's target, then the task will be deleted; otherwise the task's [schedule_time][google.cloud.tasks.v2.Task.schedule_time] will be reset to the time that [RunTask][google.cloud.tasks.v2.CloudTasks.RunTask] was called plus the retry delay specified in the queue's [RetryConfig][google.cloud.tasks.v2.RetryConfig].

[RunTask][google.cloud.tasks.v2.CloudTasks.RunTask] returns [NOT_FOUND][google.rpc.Code.NOT_FOUND] when it is called on a task that has already succeeded or permanently failed.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RunTaskRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.RunTaskRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::RunTaskRequest request = new gctv::RunTaskRequest
    {
        TaskName = gctv::TaskName.FromProjectLocationQueueTask("[PROJECT]", "[LOCATION]", "[QUEUE]", "[TASK]"),
        ResponseView = gctv::Task.Types.View.Unspecified,
    };
    // Make the request
    gctv::Task response = await cloudTasksClient.RunTaskAsync(request);
    

### RunTaskAsync(TaskName, CallSettings)
    
    
    public virtual Task<Task> RunTaskAsync(TaskName name, CallSettings callSettings = null)

Forces a task to run now.

When this method is called, Cloud Tasks will dispatch the task, even if the task is already running, the queue has reached its [RateLimits][google.cloud.tasks.v2.RateLimits] or is [PAUSED][google.cloud.tasks.v2.Queue.State.PAUSED].

This command is meant to be used for manual debugging. For example, [RunTask][google.cloud.tasks.v2.CloudTasks.RunTask] can be used to retry a failed task after a fix has been made or to manually force a task to be dispatched now.

If Cloud Tasks receives a successful response from the task's target, then the task will be deleted; otherwise the task's [schedule_time][google.cloud.tasks.v2.Task.schedule_time] will be reset to the time that [RunTask][google.cloud.tasks.v2.CloudTasks.RunTask] was called plus the retry delay specified in the queue's [RetryConfig][google.cloud.tasks.v2.RetryConfig].

[RunTask][google.cloud.tasks.v2.CloudTasks.RunTask] returns [NOT_FOUND][google.rpc.Code.NOT_FOUND] when it is called on a task that has already succeeded or permanently failed.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[TaskName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.TaskName)`  
Required. The task name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::TaskName name = gctv::TaskName.FromProjectLocationQueueTask("[PROJECT]", "[LOCATION]", "[QUEUE]", "[TASK]");
    // Make the request
    gctv::Task response = await cloudTasksClient.RunTaskAsync(name);
    

### RunTaskAsync(TaskName, CancellationToken)
    
    
    public virtual Task<Task> RunTaskAsync(TaskName name, CancellationToken cancellationToken)

Forces a task to run now.

When this method is called, Cloud Tasks will dispatch the task, even if the task is already running, the queue has reached its [RateLimits][google.cloud.tasks.v2.RateLimits] or is [PAUSED][google.cloud.tasks.v2.Queue.State.PAUSED].

This command is meant to be used for manual debugging. For example, [RunTask][google.cloud.tasks.v2.CloudTasks.RunTask] can be used to retry a failed task after a fix has been made or to manually force a task to be dispatched now.

If Cloud Tasks receives a successful response from the task's target, then the task will be deleted; otherwise the task's [schedule_time][google.cloud.tasks.v2.Task.schedule_time] will be reset to the time that [RunTask][google.cloud.tasks.v2.CloudTasks.RunTask] was called plus the retry delay specified in the queue's [RetryConfig][google.cloud.tasks.v2.RetryConfig].

[RunTask][google.cloud.tasks.v2.CloudTasks.RunTask] returns [NOT_FOUND][google.rpc.Code.NOT_FOUND] when it is called on a task that has already succeeded or permanently failed.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[TaskName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.TaskName)`  
Required. The task name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::TaskName name = gctv::TaskName.FromProjectLocationQueueTask("[PROJECT]", "[LOCATION]", "[QUEUE]", "[TASK]");
    // Make the request
    gctv::Task response = await cloudTasksClient.RunTaskAsync(name);
    

### RunTaskAsync(string, CallSettings)
    
    
    public virtual Task<Task> RunTaskAsync(string name, CallSettings callSettings = null)

Forces a task to run now.

When this method is called, Cloud Tasks will dispatch the task, even if the task is already running, the queue has reached its [RateLimits][google.cloud.tasks.v2.RateLimits] or is [PAUSED][google.cloud.tasks.v2.Queue.State.PAUSED].

This command is meant to be used for manual debugging. For example, [RunTask][google.cloud.tasks.v2.CloudTasks.RunTask] can be used to retry a failed task after a fix has been made or to manually force a task to be dispatched now.

If Cloud Tasks receives a successful response from the task's target, then the task will be deleted; otherwise the task's [schedule_time][google.cloud.tasks.v2.Task.schedule_time] will be reset to the time that [RunTask][google.cloud.tasks.v2.CloudTasks.RunTask] was called plus the retry delay specified in the queue's [RetryConfig][google.cloud.tasks.v2.RetryConfig].

[RunTask][google.cloud.tasks.v2.CloudTasks.RunTask] returns [NOT_FOUND][google.rpc.Code.NOT_FOUND] when it is called on a task that has already succeeded or permanently failed.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The task name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/queues/[QUEUE]/tasks/[TASK]";
    // Make the request
    gctv::Task response = await cloudTasksClient.RunTaskAsync(name);
    

### RunTaskAsync(string, CancellationToken)
    
    
    public virtual Task<Task> RunTaskAsync(string name, CancellationToken cancellationToken)

Forces a task to run now.

When this method is called, Cloud Tasks will dispatch the task, even if the task is already running, the queue has reached its [RateLimits][google.cloud.tasks.v2.RateLimits] or is [PAUSED][google.cloud.tasks.v2.Queue.State.PAUSED].

This command is meant to be used for manual debugging. For example, [RunTask][google.cloud.tasks.v2.CloudTasks.RunTask] can be used to retry a failed task after a fix has been made or to manually force a task to be dispatched now.

If Cloud Tasks receives a successful response from the task's target, then the task will be deleted; otherwise the task's [schedule_time][google.cloud.tasks.v2.Task.schedule_time] will be reset to the time that [RunTask][google.cloud.tasks.v2.CloudTasks.RunTask] was called plus the retry delay specified in the queue's [RetryConfig][google.cloud.tasks.v2.RetryConfig].

[RunTask][google.cloud.tasks.v2.CloudTasks.RunTask] returns [NOT_FOUND][google.rpc.Code.NOT_FOUND] when it is called on a task that has already succeeded or permanently failed.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The task name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/queues/[QUEUE]/tasks/[TASK]";
    // Make the request
    gctv::Task response = await cloudTasksClient.RunTaskAsync(name);
    

### SetIamPolicy(IResourceName, Policy, CallSettings)
    
    
    public virtual Policy SetIamPolicy(IResourceName resource, Policy policy, CallSettings callSettings = null)

Sets the access control policy for a [Queue][google.cloud.tasks.v2.Queue]. Replaces any existing policy.

Note: The Cloud Console does not check queue-level IAM permissions yet. Project-level permissions are required to use the Cloud Console.

Authorization requires the following [Google IAM](https://cloud.google.com/iam) permission on the specified resource parent:

  * `cloudtasks.queues.setIamPolicy`



**Parameters**  
---  
**Name** | **Description**  
`resource` | `[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html)`  
REQUIRED: The resource for which the policy is being specified. See the operation documentation for the appropriate value for this field.  
`policy` | `[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)`  
REQUIRED: The complete policy to be applied to the `resource`. The size of the policy is limited to a few 10s of KB. An empty policy is a valid policy but certain Cloud Platform services (such as Projects) might reject them.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | The RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    IResourceName resource = new UnparsedResourceName("a/wildcard/resource");
    Policy policy = new Policy();
    // Make the request
    Policy response = cloudTasksClient.SetIamPolicy(resource, policy);
    

### SetIamPolicy(SetIamPolicyRequest, CallSettings)
    
    
    public virtual Policy SetIamPolicy(SetIamPolicyRequest request, CallSettings callSettings = null)

Sets the access control policy for a [Queue][google.cloud.tasks.v2.Queue]. Replaces any existing policy.

Note: The Cloud Console does not check queue-level IAM permissions yet. Project-level permissions are required to use the Cloud Console.

Authorization requires the following [Google IAM](https://cloud.google.com/iam) permission on the specified resource parent:

  * `cloudtasks.queues.setIamPolicy`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetIamPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.SetIamPolicyRequest.html)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | The RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    SetIamPolicyRequest request = new SetIamPolicyRequest
    {
        ResourceAsResourceName = new UnparsedResourceName("a/wildcard/resource"),
        Policy = new Policy(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Policy response = cloudTasksClient.SetIamPolicy(request);
    

### SetIamPolicy(QueueName, Policy, CallSettings)
    
    
    public virtual Policy SetIamPolicy(QueueName resource, Policy policy, CallSettings callSettings = null)

Sets the access control policy for a [Queue][google.cloud.tasks.v2.Queue]. Replaces any existing policy.

Note: The Cloud Console does not check queue-level IAM permissions yet. Project-level permissions are required to use the Cloud Console.

Authorization requires the following [Google IAM](https://cloud.google.com/iam) permission on the specified resource parent:

  * `cloudtasks.queues.setIamPolicy`



**Parameters**  
---  
**Name** | **Description**  
`resource` | `[QueueName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.QueueName)`  
REQUIRED: The resource for which the policy is being specified. See the operation documentation for the appropriate value for this field.  
`policy` | `[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)`  
REQUIRED: The complete policy to be applied to the `resource`. The size of the policy is limited to a few 10s of KB. An empty policy is a valid policy but certain Cloud Platform services (such as Projects) might reject them.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | The RPC response.  
  
### SetIamPolicy(string, Policy, CallSettings)
    
    
    public virtual Policy SetIamPolicy(string resource, Policy policy, CallSettings callSettings = null)

Sets the access control policy for a [Queue][google.cloud.tasks.v2.Queue]. Replaces any existing policy.

Note: The Cloud Console does not check queue-level IAM permissions yet. Project-level permissions are required to use the Cloud Console.

Authorization requires the following [Google IAM](https://cloud.google.com/iam) permission on the specified resource parent:

  * `cloudtasks.queues.setIamPolicy`



**Parameters**  
---  
**Name** | **Description**  
`resource` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
REQUIRED: The resource for which the policy is being specified. See the operation documentation for the appropriate value for this field.  
`policy` | `[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)`  
REQUIRED: The complete policy to be applied to the `resource`. The size of the policy is limited to a few 10s of KB. An empty policy is a valid policy but certain Cloud Platform services (such as Projects) might reject them.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | The RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    string resource = "a/wildcard/resource";
    Policy policy = new Policy();
    // Make the request
    Policy response = cloudTasksClient.SetIamPolicy(resource, policy);
    

### SetIamPolicyAsync(IResourceName, Policy, CallSettings)
    
    
    public virtual Task<Policy> SetIamPolicyAsync(IResourceName resource, Policy policy, CallSettings callSettings = null)

Sets the access control policy for a [Queue][google.cloud.tasks.v2.Queue]. Replaces any existing policy.

Note: The Cloud Console does not check queue-level IAM permissions yet. Project-level permissions are required to use the Cloud Console.

Authorization requires the following [Google IAM](https://cloud.google.com/iam) permission on the specified resource parent:

  * `cloudtasks.queues.setIamPolicy`



**Parameters**  
---  
**Name** | **Description**  
`resource` | `[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html)`  
REQUIRED: The resource for which the policy is being specified. See the operation documentation for the appropriate value for this field.  
`policy` | `[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)`  
REQUIRED: The complete policy to be applied to the `resource`. The size of the policy is limited to a few 10s of KB. An empty policy is a valid policy but certain Cloud Platform services (such as Projects) might reject them.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    IResourceName resource = new UnparsedResourceName("a/wildcard/resource");
    Policy policy = new Policy();
    // Make the request
    Policy response = await cloudTasksClient.SetIamPolicyAsync(resource, policy);
    

### SetIamPolicyAsync(IResourceName, Policy, CancellationToken)
    
    
    public virtual Task<Policy> SetIamPolicyAsync(IResourceName resource, Policy policy, CancellationToken cancellationToken)

Sets the access control policy for a [Queue][google.cloud.tasks.v2.Queue]. Replaces any existing policy.

Note: The Cloud Console does not check queue-level IAM permissions yet. Project-level permissions are required to use the Cloud Console.

Authorization requires the following [Google IAM](https://cloud.google.com/iam) permission on the specified resource parent:

  * `cloudtasks.queues.setIamPolicy`



**Parameters**  
---  
**Name** | **Description**  
`resource` | `[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html)`  
REQUIRED: The resource for which the policy is being specified. See the operation documentation for the appropriate value for this field.  
`policy` | `[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)`  
REQUIRED: The complete policy to be applied to the `resource`. The size of the policy is limited to a few 10s of KB. An empty policy is a valid policy but certain Cloud Platform services (such as Projects) might reject them.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    IResourceName resource = new UnparsedResourceName("a/wildcard/resource");
    Policy policy = new Policy();
    // Make the request
    Policy response = await cloudTasksClient.SetIamPolicyAsync(resource, policy);
    

### SetIamPolicyAsync(SetIamPolicyRequest, CallSettings)
    
    
    public virtual Task<Policy> SetIamPolicyAsync(SetIamPolicyRequest request, CallSettings callSettings = null)

Sets the access control policy for a [Queue][google.cloud.tasks.v2.Queue]. Replaces any existing policy.

Note: The Cloud Console does not check queue-level IAM permissions yet. Project-level permissions are required to use the Cloud Console.

Authorization requires the following [Google IAM](https://cloud.google.com/iam) permission on the specified resource parent:

  * `cloudtasks.queues.setIamPolicy`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetIamPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.SetIamPolicyRequest.html)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    SetIamPolicyRequest request = new SetIamPolicyRequest
    {
        ResourceAsResourceName = new UnparsedResourceName("a/wildcard/resource"),
        Policy = new Policy(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Policy response = await cloudTasksClient.SetIamPolicyAsync(request);
    

### SetIamPolicyAsync(SetIamPolicyRequest, CancellationToken)
    
    
    public virtual Task<Policy> SetIamPolicyAsync(SetIamPolicyRequest request, CancellationToken cancellationToken)

Sets the access control policy for a [Queue][google.cloud.tasks.v2.Queue]. Replaces any existing policy.

Note: The Cloud Console does not check queue-level IAM permissions yet. Project-level permissions are required to use the Cloud Console.

Authorization requires the following [Google IAM](https://cloud.google.com/iam) permission on the specified resource parent:

  * `cloudtasks.queues.setIamPolicy`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetIamPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.SetIamPolicyRequest.html)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    SetIamPolicyRequest request = new SetIamPolicyRequest
    {
        ResourceAsResourceName = new UnparsedResourceName("a/wildcard/resource"),
        Policy = new Policy(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Policy response = await cloudTasksClient.SetIamPolicyAsync(request);
    

### SetIamPolicyAsync(QueueName, Policy, CallSettings)
    
    
    public virtual Task<Policy> SetIamPolicyAsync(QueueName resource, Policy policy, CallSettings callSettings = null)

Sets the access control policy for a [Queue][google.cloud.tasks.v2.Queue]. Replaces any existing policy.

Note: The Cloud Console does not check queue-level IAM permissions yet. Project-level permissions are required to use the Cloud Console.

Authorization requires the following [Google IAM](https://cloud.google.com/iam) permission on the specified resource parent:

  * `cloudtasks.queues.setIamPolicy`



**Parameters**  
---  
**Name** | **Description**  
`resource` | `[QueueName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.QueueName)`  
REQUIRED: The resource for which the policy is being specified. See the operation documentation for the appropriate value for this field.  
`policy` | `[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)`  
REQUIRED: The complete policy to be applied to the `resource`. The size of the policy is limited to a few 10s of KB. An empty policy is a valid policy but certain Cloud Platform services (such as Projects) might reject them.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | A Task containing the RPC response.  
  
### SetIamPolicyAsync(QueueName, Policy, CancellationToken)
    
    
    public virtual Task<Policy> SetIamPolicyAsync(QueueName resource, Policy policy, CancellationToken cancellationToken)

Sets the access control policy for a [Queue][google.cloud.tasks.v2.Queue]. Replaces any existing policy.

Note: The Cloud Console does not check queue-level IAM permissions yet. Project-level permissions are required to use the Cloud Console.

Authorization requires the following [Google IAM](https://cloud.google.com/iam) permission on the specified resource parent:

  * `cloudtasks.queues.setIamPolicy`



**Parameters**  
---  
**Name** | **Description**  
`resource` | `[QueueName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.QueueName)`  
REQUIRED: The resource for which the policy is being specified. See the operation documentation for the appropriate value for this field.  
`policy` | `[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)`  
REQUIRED: The complete policy to be applied to the `resource`. The size of the policy is limited to a few 10s of KB. An empty policy is a valid policy but certain Cloud Platform services (such as Projects) might reject them.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | A Task containing the RPC response.  
  
### SetIamPolicyAsync(string, Policy, CallSettings)
    
    
    public virtual Task<Policy> SetIamPolicyAsync(string resource, Policy policy, CallSettings callSettings = null)

Sets the access control policy for a [Queue][google.cloud.tasks.v2.Queue]. Replaces any existing policy.

Note: The Cloud Console does not check queue-level IAM permissions yet. Project-level permissions are required to use the Cloud Console.

Authorization requires the following [Google IAM](https://cloud.google.com/iam) permission on the specified resource parent:

  * `cloudtasks.queues.setIamPolicy`



**Parameters**  
---  
**Name** | **Description**  
`resource` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
REQUIRED: The resource for which the policy is being specified. See the operation documentation for the appropriate value for this field.  
`policy` | `[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)`  
REQUIRED: The complete policy to be applied to the `resource`. The size of the policy is limited to a few 10s of KB. An empty policy is a valid policy but certain Cloud Platform services (such as Projects) might reject them.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    string resource = "a/wildcard/resource";
    Policy policy = new Policy();
    // Make the request
    Policy response = await cloudTasksClient.SetIamPolicyAsync(resource, policy);
    

### SetIamPolicyAsync(string, Policy, CancellationToken)
    
    
    public virtual Task<Policy> SetIamPolicyAsync(string resource, Policy policy, CancellationToken cancellationToken)

Sets the access control policy for a [Queue][google.cloud.tasks.v2.Queue]. Replaces any existing policy.

Note: The Cloud Console does not check queue-level IAM permissions yet. Project-level permissions are required to use the Cloud Console.

Authorization requires the following [Google IAM](https://cloud.google.com/iam) permission on the specified resource parent:

  * `cloudtasks.queues.setIamPolicy`



**Parameters**  
---  
**Name** | **Description**  
`resource` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
REQUIRED: The resource for which the policy is being specified. See the operation documentation for the appropriate value for this field.  
`policy` | `[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)`  
REQUIRED: The complete policy to be applied to the `resource`. The size of the policy is limited to a few 10s of KB. An empty policy is a valid policy but certain Cloud Platform services (such as Projects) might reject them.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    string resource = "a/wildcard/resource";
    Policy policy = new Policy();
    // Make the request
    Policy response = await cloudTasksClient.SetIamPolicyAsync(resource, policy);
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CloudTasksClient#Google_Cloud_Tasks_V2_CloudTasksClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### TestIamPermissions(IResourceName, IEnumerable<string>, CallSettings)
    
    
    public virtual TestIamPermissionsResponse TestIamPermissions(IResourceName resource, IEnumerable<string> permissions, CallSettings callSettings = null)

Returns permissions that a caller has on a [Queue][google.cloud.tasks.v2.Queue]. If the resource does not exist, this will return an empty set of permissions, not a [NOT_FOUND][google.rpc.Code.NOT_FOUND] error.

Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

**Parameters**  
---  
**Name** | **Description**  
`resource` | `[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html)`  
REQUIRED: The resource for which the policy detail is being requested. See the operation documentation for the appropriate value for this field.  
`permissions` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The set of permissions to check for the `resource`. Permissions with wildcards (such as '_' or 'storage._ ') are not allowed. For more information see [IAM Overview](https://cloud.google.com/iam/docs/overview#permissions).  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[TestIamPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsResponse.html)` | The RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    IResourceName resource = new UnparsedResourceName("a/wildcard/resource");
    IEnumerable<string> permissions = new string[] { "", };
    // Make the request
    TestIamPermissionsResponse response = cloudTasksClient.TestIamPermissions(resource, permissions);
    

### TestIamPermissions(TestIamPermissionsRequest, CallSettings)
    
    
    public virtual TestIamPermissionsResponse TestIamPermissions(TestIamPermissionsRequest request, CallSettings callSettings = null)

Returns permissions that a caller has on a [Queue][google.cloud.tasks.v2.Queue]. If the resource does not exist, this will return an empty set of permissions, not a [NOT_FOUND][google.rpc.Code.NOT_FOUND] error.

Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsRequest.html)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[TestIamPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsResponse.html)` | The RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    TestIamPermissionsRequest request = new TestIamPermissionsRequest
    {
        ResourceAsResourceName = new UnparsedResourceName("a/wildcard/resource"),
        Permissions = { "", },
    };
    // Make the request
    TestIamPermissionsResponse response = cloudTasksClient.TestIamPermissions(request);
    

### TestIamPermissions(QueueName, IEnumerable<string>, CallSettings)
    
    
    public virtual TestIamPermissionsResponse TestIamPermissions(QueueName resource, IEnumerable<string> permissions, CallSettings callSettings = null)

Returns permissions that a caller has on a [Queue][google.cloud.tasks.v2.Queue]. If the resource does not exist, this will return an empty set of permissions, not a [NOT_FOUND][google.rpc.Code.NOT_FOUND] error.

Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

**Parameters**  
---  
**Name** | **Description**  
`resource` | `[QueueName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.QueueName)`  
REQUIRED: The resource for which the policy detail is being requested. See the operation documentation for the appropriate value for this field.  
`permissions` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The set of permissions to check for the `resource`. Permissions with wildcards (such as '_' or 'storage._ ') are not allowed. For more information see [IAM Overview](https://cloud.google.com/iam/docs/overview#permissions).  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[TestIamPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsResponse.html)` | The RPC response.  
  
### TestIamPermissions(string, IEnumerable<string>, CallSettings)
    
    
    public virtual TestIamPermissionsResponse TestIamPermissions(string resource, IEnumerable<string> permissions, CallSettings callSettings = null)

Returns permissions that a caller has on a [Queue][google.cloud.tasks.v2.Queue]. If the resource does not exist, this will return an empty set of permissions, not a [NOT_FOUND][google.rpc.Code.NOT_FOUND] error.

Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

**Parameters**  
---  
**Name** | **Description**  
`resource` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
REQUIRED: The resource for which the policy detail is being requested. See the operation documentation for the appropriate value for this field.  
`permissions` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The set of permissions to check for the `resource`. Permissions with wildcards (such as '_' or 'storage._ ') are not allowed. For more information see [IAM Overview](https://cloud.google.com/iam/docs/overview#permissions).  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[TestIamPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsResponse.html)` | The RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    string resource = "a/wildcard/resource";
    IEnumerable<string> permissions = new string[] { "", };
    // Make the request
    TestIamPermissionsResponse response = cloudTasksClient.TestIamPermissions(resource, permissions);
    

### TestIamPermissionsAsync(IResourceName, IEnumerable<string>, CallSettings)
    
    
    public virtual Task<TestIamPermissionsResponse> TestIamPermissionsAsync(IResourceName resource, IEnumerable<string> permissions, CallSettings callSettings = null)

Returns permissions that a caller has on a [Queue][google.cloud.tasks.v2.Queue]. If the resource does not exist, this will return an empty set of permissions, not a [NOT_FOUND][google.rpc.Code.NOT_FOUND] error.

Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

**Parameters**  
---  
**Name** | **Description**  
`resource` | `[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html)`  
REQUIRED: The resource for which the policy detail is being requested. See the operation documentation for the appropriate value for this field.  
`permissions` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The set of permissions to check for the `resource`. Permissions with wildcards (such as '_' or 'storage._ ') are not allowed. For more information see [IAM Overview](https://cloud.google.com/iam/docs/overview#permissions).  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[TestIamPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsResponse.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    IResourceName resource = new UnparsedResourceName("a/wildcard/resource");
    IEnumerable<string> permissions = new string[] { "", };
    // Make the request
    TestIamPermissionsResponse response = await cloudTasksClient.TestIamPermissionsAsync(resource, permissions);
    

### TestIamPermissionsAsync(IResourceName, IEnumerable<string>, CancellationToken)
    
    
    public virtual Task<TestIamPermissionsResponse> TestIamPermissionsAsync(IResourceName resource, IEnumerable<string> permissions, CancellationToken cancellationToken)

Returns permissions that a caller has on a [Queue][google.cloud.tasks.v2.Queue]. If the resource does not exist, this will return an empty set of permissions, not a [NOT_FOUND][google.rpc.Code.NOT_FOUND] error.

Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

**Parameters**  
---  
**Name** | **Description**  
`resource` | `[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html)`  
REQUIRED: The resource for which the policy detail is being requested. See the operation documentation for the appropriate value for this field.  
`permissions` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The set of permissions to check for the `resource`. Permissions with wildcards (such as '_' or 'storage._ ') are not allowed. For more information see [IAM Overview](https://cloud.google.com/iam/docs/overview#permissions).  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[TestIamPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsResponse.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    IResourceName resource = new UnparsedResourceName("a/wildcard/resource");
    IEnumerable<string> permissions = new string[] { "", };
    // Make the request
    TestIamPermissionsResponse response = await cloudTasksClient.TestIamPermissionsAsync(resource, permissions);
    

### TestIamPermissionsAsync(TestIamPermissionsRequest, CallSettings)
    
    
    public virtual Task<TestIamPermissionsResponse> TestIamPermissionsAsync(TestIamPermissionsRequest request, CallSettings callSettings = null)

Returns permissions that a caller has on a [Queue][google.cloud.tasks.v2.Queue]. If the resource does not exist, this will return an empty set of permissions, not a [NOT_FOUND][google.rpc.Code.NOT_FOUND] error.

Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsRequest.html)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[TestIamPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsResponse.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    TestIamPermissionsRequest request = new TestIamPermissionsRequest
    {
        ResourceAsResourceName = new UnparsedResourceName("a/wildcard/resource"),
        Permissions = { "", },
    };
    // Make the request
    TestIamPermissionsResponse response = await cloudTasksClient.TestIamPermissionsAsync(request);
    

### TestIamPermissionsAsync(TestIamPermissionsRequest, CancellationToken)
    
    
    public virtual Task<TestIamPermissionsResponse> TestIamPermissionsAsync(TestIamPermissionsRequest request, CancellationToken cancellationToken)

Returns permissions that a caller has on a [Queue][google.cloud.tasks.v2.Queue]. If the resource does not exist, this will return an empty set of permissions, not a [NOT_FOUND][google.rpc.Code.NOT_FOUND] error.

Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsRequest.html)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[TestIamPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsResponse.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    TestIamPermissionsRequest request = new TestIamPermissionsRequest
    {
        ResourceAsResourceName = new UnparsedResourceName("a/wildcard/resource"),
        Permissions = { "", },
    };
    // Make the request
    TestIamPermissionsResponse response = await cloudTasksClient.TestIamPermissionsAsync(request);
    

### TestIamPermissionsAsync(QueueName, IEnumerable<string>, CallSettings)
    
    
    public virtual Task<TestIamPermissionsResponse> TestIamPermissionsAsync(QueueName resource, IEnumerable<string> permissions, CallSettings callSettings = null)

Returns permissions that a caller has on a [Queue][google.cloud.tasks.v2.Queue]. If the resource does not exist, this will return an empty set of permissions, not a [NOT_FOUND][google.rpc.Code.NOT_FOUND] error.

Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

**Parameters**  
---  
**Name** | **Description**  
`resource` | `[QueueName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.QueueName)`  
REQUIRED: The resource for which the policy detail is being requested. See the operation documentation for the appropriate value for this field.  
`permissions` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The set of permissions to check for the `resource`. Permissions with wildcards (such as '_' or 'storage._ ') are not allowed. For more information see [IAM Overview](https://cloud.google.com/iam/docs/overview#permissions).  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[TestIamPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsResponse.html)` | A Task containing the RPC response.  
  
### TestIamPermissionsAsync(QueueName, IEnumerable<string>, CancellationToken)
    
    
    public virtual Task<TestIamPermissionsResponse> TestIamPermissionsAsync(QueueName resource, IEnumerable<string> permissions, CancellationToken cancellationToken)

Returns permissions that a caller has on a [Queue][google.cloud.tasks.v2.Queue]. If the resource does not exist, this will return an empty set of permissions, not a [NOT_FOUND][google.rpc.Code.NOT_FOUND] error.

Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

**Parameters**  
---  
**Name** | **Description**  
`resource` | `[QueueName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.QueueName)`  
REQUIRED: The resource for which the policy detail is being requested. See the operation documentation for the appropriate value for this field.  
`permissions` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The set of permissions to check for the `resource`. Permissions with wildcards (such as '_' or 'storage._ ') are not allowed. For more information see [IAM Overview](https://cloud.google.com/iam/docs/overview#permissions).  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[TestIamPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsResponse.html)` | A Task containing the RPC response.  
  
### TestIamPermissionsAsync(string, IEnumerable<string>, CallSettings)
    
    
    public virtual Task<TestIamPermissionsResponse> TestIamPermissionsAsync(string resource, IEnumerable<string> permissions, CallSettings callSettings = null)

Returns permissions that a caller has on a [Queue][google.cloud.tasks.v2.Queue]. If the resource does not exist, this will return an empty set of permissions, not a [NOT_FOUND][google.rpc.Code.NOT_FOUND] error.

Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

**Parameters**  
---  
**Name** | **Description**  
`resource` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
REQUIRED: The resource for which the policy detail is being requested. See the operation documentation for the appropriate value for this field.  
`permissions` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The set of permissions to check for the `resource`. Permissions with wildcards (such as '_' or 'storage._ ') are not allowed. For more information see [IAM Overview](https://cloud.google.com/iam/docs/overview#permissions).  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[TestIamPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsResponse.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    string resource = "a/wildcard/resource";
    IEnumerable<string> permissions = new string[] { "", };
    // Make the request
    TestIamPermissionsResponse response = await cloudTasksClient.TestIamPermissionsAsync(resource, permissions);
    

### TestIamPermissionsAsync(string, IEnumerable<string>, CancellationToken)
    
    
    public virtual Task<TestIamPermissionsResponse> TestIamPermissionsAsync(string resource, IEnumerable<string> permissions, CancellationToken cancellationToken)

Returns permissions that a caller has on a [Queue][google.cloud.tasks.v2.Queue]. If the resource does not exist, this will return an empty set of permissions, not a [NOT_FOUND][google.rpc.Code.NOT_FOUND] error.

Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

**Parameters**  
---  
**Name** | **Description**  
`resource` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
REQUIRED: The resource for which the policy detail is being requested. See the operation documentation for the appropriate value for this field.  
`permissions` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The set of permissions to check for the `resource`. Permissions with wildcards (such as '_' or 'storage._ ') are not allowed. For more information see [IAM Overview](https://cloud.google.com/iam/docs/overview#permissions).  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[TestIamPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsResponse.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    string resource = "a/wildcard/resource";
    IEnumerable<string> permissions = new string[] { "", };
    // Make the request
    TestIamPermissionsResponse response = await cloudTasksClient.TestIamPermissionsAsync(resource, permissions);
    

### UpdateCmekConfig(CmekConfig, FieldMask, CallSettings)
    
    
    public virtual CmekConfig UpdateCmekConfig(CmekConfig cmekConfig, FieldMask updateMask, CallSettings callSettings = null)

Creates or Updates a CMEK config.

Updates the Customer Managed Encryption Key associated with the Cloud Tasks location (Creates if the key does not already exist). All new tasks created in the location will be encrypted at-rest with the KMS-key provided in the config.

**Parameters**  
---  
**Name** | **Description**  
`cmekConfig` | `[CmekConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CmekConfig)`  
Required. The config to update. Its name attribute distinguishes it.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
List of fields to be updated in this request.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[CmekConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CmekConfig)` | The RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    gctv::CmekConfig cmekConfig = new gctv::CmekConfig();
    FieldMask updateMask = new FieldMask();
    // Make the request
    gctv::CmekConfig response = cloudTasksClient.UpdateCmekConfig(cmekConfig, updateMask);
    

### UpdateCmekConfig(UpdateCmekConfigRequest, CallSettings)
    
    
    public virtual CmekConfig UpdateCmekConfig(UpdateCmekConfigRequest request, CallSettings callSettings = null)

Creates or Updates a CMEK config.

Updates the Customer Managed Encryption Key associated with the Cloud Tasks location (Creates if the key does not already exist). All new tasks created in the location will be encrypted at-rest with the KMS-key provided in the config.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateCmekConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.UpdateCmekConfigRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[CmekConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CmekConfig)` | The RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    gctv::UpdateCmekConfigRequest request = new gctv::UpdateCmekConfigRequest
    {
        CmekConfig = new gctv::CmekConfig(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    gctv::CmekConfig response = cloudTasksClient.UpdateCmekConfig(request);
    

### UpdateCmekConfigAsync(CmekConfig, FieldMask, CallSettings)
    
    
    public virtual Task<CmekConfig> UpdateCmekConfigAsync(CmekConfig cmekConfig, FieldMask updateMask, CallSettings callSettings = null)

Creates or Updates a CMEK config.

Updates the Customer Managed Encryption Key associated with the Cloud Tasks location (Creates if the key does not already exist). All new tasks created in the location will be encrypted at-rest with the KMS-key provided in the config.

**Parameters**  
---  
**Name** | **Description**  
`cmekConfig` | `[CmekConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CmekConfig)`  
Required. The config to update. Its name attribute distinguishes it.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
List of fields to be updated in this request.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CmekConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CmekConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::CmekConfig cmekConfig = new gctv::CmekConfig();
    FieldMask updateMask = new FieldMask();
    // Make the request
    gctv::CmekConfig response = await cloudTasksClient.UpdateCmekConfigAsync(cmekConfig, updateMask);
    

### UpdateCmekConfigAsync(CmekConfig, FieldMask, CancellationToken)
    
    
    public virtual Task<CmekConfig> UpdateCmekConfigAsync(CmekConfig cmekConfig, FieldMask updateMask, CancellationToken cancellationToken)

Creates or Updates a CMEK config.

Updates the Customer Managed Encryption Key associated with the Cloud Tasks location (Creates if the key does not already exist). All new tasks created in the location will be encrypted at-rest with the KMS-key provided in the config.

**Parameters**  
---  
**Name** | **Description**  
`cmekConfig` | `[CmekConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CmekConfig)`  
Required. The config to update. Its name attribute distinguishes it.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
List of fields to be updated in this request.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CmekConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CmekConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::CmekConfig cmekConfig = new gctv::CmekConfig();
    FieldMask updateMask = new FieldMask();
    // Make the request
    gctv::CmekConfig response = await cloudTasksClient.UpdateCmekConfigAsync(cmekConfig, updateMask);
    

### UpdateCmekConfigAsync(UpdateCmekConfigRequest, CallSettings)
    
    
    public virtual Task<CmekConfig> UpdateCmekConfigAsync(UpdateCmekConfigRequest request, CallSettings callSettings = null)

Creates or Updates a CMEK config.

Updates the Customer Managed Encryption Key associated with the Cloud Tasks location (Creates if the key does not already exist). All new tasks created in the location will be encrypted at-rest with the KMS-key provided in the config.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateCmekConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.UpdateCmekConfigRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CmekConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CmekConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::UpdateCmekConfigRequest request = new gctv::UpdateCmekConfigRequest
    {
        CmekConfig = new gctv::CmekConfig(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    gctv::CmekConfig response = await cloudTasksClient.UpdateCmekConfigAsync(request);
    

### UpdateCmekConfigAsync(UpdateCmekConfigRequest, CancellationToken)
    
    
    public virtual Task<CmekConfig> UpdateCmekConfigAsync(UpdateCmekConfigRequest request, CancellationToken cancellationToken)

Creates or Updates a CMEK config.

Updates the Customer Managed Encryption Key associated with the Cloud Tasks location (Creates if the key does not already exist). All new tasks created in the location will be encrypted at-rest with the KMS-key provided in the config.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateCmekConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.UpdateCmekConfigRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CmekConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CmekConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::UpdateCmekConfigRequest request = new gctv::UpdateCmekConfigRequest
    {
        CmekConfig = new gctv::CmekConfig(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    gctv::CmekConfig response = await cloudTasksClient.UpdateCmekConfigAsync(request);
    

### UpdateQueue(Queue, FieldMask, CallSettings)
    
    
    public virtual Queue UpdateQueue(Queue queue, FieldMask updateMask, CallSettings callSettings = null)

Updates a queue.

This method creates the queue if it does not exist and updates the queue if it does exist.

Queues created with this method allow tasks to live for a maximum of 31 days. After a task is 31 days old, the task will be deleted regardless of whether it was dispatched or not.

WARNING: Using this method may have unintended side effects if you are using an App Engine `queue.yaml` or `queue.xml` file to manage your queues. Read [Overview of Queue Management and queue.yaml](https://cloud.google.com/tasks/docs/queue-yaml) before using this method.

**Parameters**  
---  
**Name** | **Description**  
`queue` | `[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)`  
Required. The queue to create or update. The queue's [name][google.cloud.tasks.v2.Queue.name] must be specified. Output only fields cannot be modified using UpdateQueue. Any value specified for an output only field will be ignored. The queue's [name][google.cloud.tasks.v2.Queue.name] cannot be changed.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
A mask used to specify which fields of the queue are being updated. If empty, then all fields will be updated.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | The RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    gctv::Queue queue = new gctv::Queue();
    FieldMask updateMask = new FieldMask();
    // Make the request
    gctv::Queue response = cloudTasksClient.UpdateQueue(queue, updateMask);
    

### UpdateQueue(UpdateQueueRequest, CallSettings)
    
    
    public virtual Queue UpdateQueue(UpdateQueueRequest request, CallSettings callSettings = null)

Updates a queue.

This method creates the queue if it does not exist and updates the queue if it does exist.

Queues created with this method allow tasks to live for a maximum of 31 days. After a task is 31 days old, the task will be deleted regardless of whether it was dispatched or not.

WARNING: Using this method may have unintended side effects if you are using an App Engine `queue.yaml` or `queue.xml` file to manage your queues. Read [Overview of Queue Management and queue.yaml](https://cloud.google.com/tasks/docs/queue-yaml) before using this method.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateQueueRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.UpdateQueueRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | The RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = gctv::CloudTasksClient.Create();
    // Initialize request argument(s)
    gctv::UpdateQueueRequest request = new gctv::UpdateQueueRequest
    {
        Queue = new gctv::Queue(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    gctv::Queue response = cloudTasksClient.UpdateQueue(request);
    

### UpdateQueueAsync(Queue, FieldMask, CallSettings)
    
    
    public virtual Task<Queue> UpdateQueueAsync(Queue queue, FieldMask updateMask, CallSettings callSettings = null)

Updates a queue.

This method creates the queue if it does not exist and updates the queue if it does exist.

Queues created with this method allow tasks to live for a maximum of 31 days. After a task is 31 days old, the task will be deleted regardless of whether it was dispatched or not.

WARNING: Using this method may have unintended side effects if you are using an App Engine `queue.yaml` or `queue.xml` file to manage your queues. Read [Overview of Queue Management and queue.yaml](https://cloud.google.com/tasks/docs/queue-yaml) before using this method.

**Parameters**  
---  
**Name** | **Description**  
`queue` | `[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)`  
Required. The queue to create or update. The queue's [name][google.cloud.tasks.v2.Queue.name] must be specified. Output only fields cannot be modified using UpdateQueue. Any value specified for an output only field will be ignored. The queue's [name][google.cloud.tasks.v2.Queue.name] cannot be changed.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
A mask used to specify which fields of the queue are being updated. If empty, then all fields will be updated.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::Queue queue = new gctv::Queue();
    FieldMask updateMask = new FieldMask();
    // Make the request
    gctv::Queue response = await cloudTasksClient.UpdateQueueAsync(queue, updateMask);
    

### UpdateQueueAsync(Queue, FieldMask, CancellationToken)
    
    
    public virtual Task<Queue> UpdateQueueAsync(Queue queue, FieldMask updateMask, CancellationToken cancellationToken)

Updates a queue.

This method creates the queue if it does not exist and updates the queue if it does exist.

Queues created with this method allow tasks to live for a maximum of 31 days. After a task is 31 days old, the task will be deleted regardless of whether it was dispatched or not.

WARNING: Using this method may have unintended side effects if you are using an App Engine `queue.yaml` or `queue.xml` file to manage your queues. Read [Overview of Queue Management and queue.yaml](https://cloud.google.com/tasks/docs/queue-yaml) before using this method.

**Parameters**  
---  
**Name** | **Description**  
`queue` | `[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)`  
Required. The queue to create or update. The queue's [name][google.cloud.tasks.v2.Queue.name] must be specified. Output only fields cannot be modified using UpdateQueue. Any value specified for an output only field will be ignored. The queue's [name][google.cloud.tasks.v2.Queue.name] cannot be changed.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
A mask used to specify which fields of the queue are being updated. If empty, then all fields will be updated.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::Queue queue = new gctv::Queue();
    FieldMask updateMask = new FieldMask();
    // Make the request
    gctv::Queue response = await cloudTasksClient.UpdateQueueAsync(queue, updateMask);
    

### UpdateQueueAsync(UpdateQueueRequest, CallSettings)
    
    
    public virtual Task<Queue> UpdateQueueAsync(UpdateQueueRequest request, CallSettings callSettings = null)

Updates a queue.

This method creates the queue if it does not exist and updates the queue if it does exist.

Queues created with this method allow tasks to live for a maximum of 31 days. After a task is 31 days old, the task will be deleted regardless of whether it was dispatched or not.

WARNING: Using this method may have unintended side effects if you are using an App Engine `queue.yaml` or `queue.xml` file to manage your queues. Read [Overview of Queue Management and queue.yaml](https://cloud.google.com/tasks/docs/queue-yaml) before using this method.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateQueueRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.UpdateQueueRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::UpdateQueueRequest request = new gctv::UpdateQueueRequest
    {
        Queue = new gctv::Queue(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    gctv::Queue response = await cloudTasksClient.UpdateQueueAsync(request);
    

### UpdateQueueAsync(UpdateQueueRequest, CancellationToken)
    
    
    public virtual Task<Queue> UpdateQueueAsync(UpdateQueueRequest request, CancellationToken cancellationToken)

Updates a queue.

This method creates the queue if it does not exist and updates the queue if it does exist.

Queues created with this method allow tasks to live for a maximum of 31 days. After a task is 31 days old, the task will be deleted regardless of whether it was dispatched or not.

WARNING: Using this method may have unintended side effects if you are using an App Engine `queue.yaml` or `queue.xml` file to manage your queues. Read [Overview of Queue Management and queue.yaml](https://cloud.google.com/tasks/docs/queue-yaml) before using this method.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateQueueRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.UpdateQueueRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gctv::CloudTasksClient cloudTasksClient = await gctv::CloudTasksClient.CreateAsync();
    // Initialize request argument(s)
    gctv::UpdateQueueRequest request = new gctv::UpdateQueueRequest
    {
        Queue = new gctv::Queue(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    gctv::Queue response = await cloudTasksClient.UpdateQueueAsync(request);
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
