---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentServiceClient
title: Gemini Enterprise for Customer Experience v1beta API - Class AgentServiceClient (1.0.0-beta09) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:39:49.508412+00:00
---

# Gemini Enterprise for Customer Experience v1beta API - Class AgentServiceClient (1.0.0-beta09)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Gemini Enterprise for Customer Experience v1beta API - Class AgentServiceClient (1.0.0-beta09) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta09 (latest)  1.0.0-beta08 
    
    
    public abstract class AgentServiceClient

Reference documentation and code samples for the Gemini Enterprise for Customer Experience v1beta API class AgentServiceClient.

AgentService client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AgentServiceClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[AgentServiceClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentServiceClientImpl)

## Namespace

[Google.Cloud.Ces.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta)

## Assembly

Google.Cloud.Ces.V1Beta.dll

## Remarks

The service that manages agent-related resources in Gemini Enterprise for Customer Engagement (CES).

## Properties 

### BatchDeleteConversationsOperationsClient
    
    
    public virtual OperationsClient BatchDeleteConversationsOperationsClient { get; }

The long-running operations client for `BatchDeleteConversations`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### CreateAppOperationsClient
    
    
    public virtual OperationsClient CreateAppOperationsClient { get; }

The long-running operations client for `CreateApp`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the AgentService service, which is a host of "ces.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default AgentService scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default AgentService scopes are:

  * <https://www.googleapis.com/auth/ces>
  * <https://www.googleapis.com/auth/cloud-platform>



### DeleteAppOperationsClient
    
    
    public virtual OperationsClient DeleteAppOperationsClient { get; }

The long-running operations client for `DeleteApp`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### ExportAppOperationsClient
    
    
    public virtual OperationsClient ExportAppOperationsClient { get; }

The long-running operations client for `ExportApp`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### GenerateAppResourceOperationsClient
    
    
    public virtual OperationsClient GenerateAppResourceOperationsClient { get; }

The long-running operations client for `GenerateAppResource`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### GrpcClient
    
    
    public virtual AgentService.AgentServiceClient GrpcClient { get; }

The underlying gRPC AgentService client

**Property Value**  
---  
**Type** | **Description**  
`[AgentService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentService)[AgentServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentService.AgentServiceClient)` |   
  
### ImportAppOperationsClient
    
    
    public virtual OperationsClient ImportAppOperationsClient { get; }

The long-running operations client for `ImportApp`.

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
  
### RestoreAppVersionOperationsClient
    
    
    public virtual OperationsClient RestoreAppVersionOperationsClient { get; }

The long-running operations client for `RestoreAppVersion`.

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
  
## Methods 

### BatchDeleteConversations(AppName, CallSettings)
    
    
    public virtual Operation<BatchDeleteConversationsResponse, OperationMetadata> BatchDeleteConversations(AppName parent, CallSettings callSettings = null)

Batch deletes the specified conversations.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to delete conversations from. Format: `projects/{project}/locations/{location}/apps/{app}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchDeleteConversationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.BatchDeleteConversationsResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    // Make the request
    Operation<BatchDeleteConversationsResponse, OperationMetadata> response = agentServiceClient.BatchDeleteConversations(parent);
    
    // Poll until the returned long-running operation is complete
    Operation<BatchDeleteConversationsResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    BatchDeleteConversationsResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<BatchDeleteConversationsResponse, OperationMetadata> retrievedResponse = agentServiceClient.PollOnceBatchDeleteConversations(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        BatchDeleteConversationsResponse retrievedResult = retrievedResponse.Result;
    }
    

### BatchDeleteConversations(BatchDeleteConversationsRequest, CallSettings)
    
    
    public virtual Operation<BatchDeleteConversationsResponse, OperationMetadata> BatchDeleteConversations(BatchDeleteConversationsRequest request, CallSettings callSettings = null)

Batch deletes the specified conversations.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchDeleteConversationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.BatchDeleteConversationsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchDeleteConversationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.BatchDeleteConversationsResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    BatchDeleteConversationsRequest request = new BatchDeleteConversationsRequest
    {
        ParentAsAppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
        ConversationsAsConversationNames =
        {
            ConversationName.FromProjectLocationAppConversation("[PROJECT]", "[LOCATION]", "[APP]", "[CONVERSATION]"),
        },
    };
    // Make the request
    Operation<BatchDeleteConversationsResponse, OperationMetadata> response = agentServiceClient.BatchDeleteConversations(request);
    
    // Poll until the returned long-running operation is complete
    Operation<BatchDeleteConversationsResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    BatchDeleteConversationsResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<BatchDeleteConversationsResponse, OperationMetadata> retrievedResponse = agentServiceClient.PollOnceBatchDeleteConversations(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        BatchDeleteConversationsResponse retrievedResult = retrievedResponse.Result;
    }
    

### BatchDeleteConversations(string, CallSettings)
    
    
    public virtual Operation<BatchDeleteConversationsResponse, OperationMetadata> BatchDeleteConversations(string parent, CallSettings callSettings = null)

Batch deletes the specified conversations.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to delete conversations from. Format: `projects/{project}/locations/{location}/apps/{app}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchDeleteConversationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.BatchDeleteConversationsResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    // Make the request
    Operation<BatchDeleteConversationsResponse, OperationMetadata> response = agentServiceClient.BatchDeleteConversations(parent);
    
    // Poll until the returned long-running operation is complete
    Operation<BatchDeleteConversationsResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    BatchDeleteConversationsResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<BatchDeleteConversationsResponse, OperationMetadata> retrievedResponse = agentServiceClient.PollOnceBatchDeleteConversations(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        BatchDeleteConversationsResponse retrievedResult = retrievedResponse.Result;
    }
    

### BatchDeleteConversationsAsync(AppName, CallSettings)
    
    
    public virtual Task<Operation<BatchDeleteConversationsResponse, OperationMetadata>> BatchDeleteConversationsAsync(AppName parent, CallSettings callSettings = null)

Batch deletes the specified conversations.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to delete conversations from. Format: `projects/{project}/locations/{location}/apps/{app}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchDeleteConversationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.BatchDeleteConversationsResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    // Make the request
    Operation<BatchDeleteConversationsResponse, OperationMetadata> response = await agentServiceClient.BatchDeleteConversationsAsync(parent);
    
    // Poll until the returned long-running operation is complete
    Operation<BatchDeleteConversationsResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    BatchDeleteConversationsResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<BatchDeleteConversationsResponse, OperationMetadata> retrievedResponse = await agentServiceClient.PollOnceBatchDeleteConversationsAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        BatchDeleteConversationsResponse retrievedResult = retrievedResponse.Result;
    }
    

### BatchDeleteConversationsAsync(AppName, CancellationToken)
    
    
    public virtual Task<Operation<BatchDeleteConversationsResponse, OperationMetadata>> BatchDeleteConversationsAsync(AppName parent, CancellationToken cancellationToken)

Batch deletes the specified conversations.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to delete conversations from. Format: `projects/{project}/locations/{location}/apps/{app}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchDeleteConversationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.BatchDeleteConversationsResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    // Make the request
    Operation<BatchDeleteConversationsResponse, OperationMetadata> response = await agentServiceClient.BatchDeleteConversationsAsync(parent);
    
    // Poll until the returned long-running operation is complete
    Operation<BatchDeleteConversationsResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    BatchDeleteConversationsResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<BatchDeleteConversationsResponse, OperationMetadata> retrievedResponse = await agentServiceClient.PollOnceBatchDeleteConversationsAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        BatchDeleteConversationsResponse retrievedResult = retrievedResponse.Result;
    }
    

### BatchDeleteConversationsAsync(BatchDeleteConversationsRequest, CallSettings)
    
    
    public virtual Task<Operation<BatchDeleteConversationsResponse, OperationMetadata>> BatchDeleteConversationsAsync(BatchDeleteConversationsRequest request, CallSettings callSettings = null)

Batch deletes the specified conversations.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchDeleteConversationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.BatchDeleteConversationsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchDeleteConversationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.BatchDeleteConversationsResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    BatchDeleteConversationsRequest request = new BatchDeleteConversationsRequest
    {
        ParentAsAppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
        ConversationsAsConversationNames =
        {
            ConversationName.FromProjectLocationAppConversation("[PROJECT]", "[LOCATION]", "[APP]", "[CONVERSATION]"),
        },
    };
    // Make the request
    Operation<BatchDeleteConversationsResponse, OperationMetadata> response = await agentServiceClient.BatchDeleteConversationsAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<BatchDeleteConversationsResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    BatchDeleteConversationsResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<BatchDeleteConversationsResponse, OperationMetadata> retrievedResponse = await agentServiceClient.PollOnceBatchDeleteConversationsAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        BatchDeleteConversationsResponse retrievedResult = retrievedResponse.Result;
    }
    

### BatchDeleteConversationsAsync(BatchDeleteConversationsRequest, CancellationToken)
    
    
    public virtual Task<Operation<BatchDeleteConversationsResponse, OperationMetadata>> BatchDeleteConversationsAsync(BatchDeleteConversationsRequest request, CancellationToken cancellationToken)

Batch deletes the specified conversations.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchDeleteConversationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.BatchDeleteConversationsRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchDeleteConversationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.BatchDeleteConversationsResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    BatchDeleteConversationsRequest request = new BatchDeleteConversationsRequest
    {
        ParentAsAppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
        ConversationsAsConversationNames =
        {
            ConversationName.FromProjectLocationAppConversation("[PROJECT]", "[LOCATION]", "[APP]", "[CONVERSATION]"),
        },
    };
    // Make the request
    Operation<BatchDeleteConversationsResponse, OperationMetadata> response = await agentServiceClient.BatchDeleteConversationsAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<BatchDeleteConversationsResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    BatchDeleteConversationsResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<BatchDeleteConversationsResponse, OperationMetadata> retrievedResponse = await agentServiceClient.PollOnceBatchDeleteConversationsAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        BatchDeleteConversationsResponse retrievedResult = retrievedResponse.Result;
    }
    

### BatchDeleteConversationsAsync(string, CallSettings)
    
    
    public virtual Task<Operation<BatchDeleteConversationsResponse, OperationMetadata>> BatchDeleteConversationsAsync(string parent, CallSettings callSettings = null)

Batch deletes the specified conversations.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to delete conversations from. Format: `projects/{project}/locations/{location}/apps/{app}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchDeleteConversationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.BatchDeleteConversationsResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    // Make the request
    Operation<BatchDeleteConversationsResponse, OperationMetadata> response = await agentServiceClient.BatchDeleteConversationsAsync(parent);
    
    // Poll until the returned long-running operation is complete
    Operation<BatchDeleteConversationsResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    BatchDeleteConversationsResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<BatchDeleteConversationsResponse, OperationMetadata> retrievedResponse = await agentServiceClient.PollOnceBatchDeleteConversationsAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        BatchDeleteConversationsResponse retrievedResult = retrievedResponse.Result;
    }
    

### BatchDeleteConversationsAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<BatchDeleteConversationsResponse, OperationMetadata>> BatchDeleteConversationsAsync(string parent, CancellationToken cancellationToken)

Batch deletes the specified conversations.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to delete conversations from. Format: `projects/{project}/locations/{location}/apps/{app}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchDeleteConversationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.BatchDeleteConversationsResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    // Make the request
    Operation<BatchDeleteConversationsResponse, OperationMetadata> response = await agentServiceClient.BatchDeleteConversationsAsync(parent);
    
    // Poll until the returned long-running operation is complete
    Operation<BatchDeleteConversationsResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    BatchDeleteConversationsResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<BatchDeleteConversationsResponse, OperationMetadata> retrievedResponse = await agentServiceClient.PollOnceBatchDeleteConversationsAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        BatchDeleteConversationsResponse retrievedResult = retrievedResponse.Result;
    }
    

### Create()
    
    
    public static AgentServiceClient Create()

Synchronously creates a [AgentServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [AgentServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentServiceClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[AgentServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentServiceClient)` | The created [AgentServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentServiceClient).  
  
### CreateAgent(AppName, Agent, CallSettings)
    
    
    public virtual Agent CreateAgent(AppName parent, Agent agent, CallSettings callSettings = null)

Creates a new agent in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to create an agent in.  
`agent` | `[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)`  
Required. The agent to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    Agent agent = new Agent();
    // Make the request
    Agent response = agentServiceClient.CreateAgent(parent, agent);
    

### CreateAgent(AppName, Agent, string, CallSettings)
    
    
    public virtual Agent CreateAgent(AppName parent, Agent agent, string agentId, CallSettings callSettings = null)

Creates a new agent in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to create an agent in.  
`agent` | `[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)`  
Required. The agent to create.  
`agentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the agent, which will become the final component of the agent's resource name. If not provided, a unique ID will be automatically assigned for the agent.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    Agent agent = new Agent();
    string agentId = "";
    // Make the request
    Agent response = agentServiceClient.CreateAgent(parent, agent, agentId);
    

### CreateAgent(CreateAgentRequest, CallSettings)
    
    
    public virtual Agent CreateAgent(CreateAgentRequest request, CallSettings callSettings = null)

Creates a new agent in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateAgentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    CreateAgentRequest request = new CreateAgentRequest
    {
        ParentAsAppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
        AgentId = "",
        Agent = new Agent(),
    };
    // Make the request
    Agent response = agentServiceClient.CreateAgent(request);
    

### CreateAgent(string, Agent, CallSettings)
    
    
    public virtual Agent CreateAgent(string parent, Agent agent, CallSettings callSettings = null)

Creates a new agent in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to create an agent in.  
`agent` | `[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)`  
Required. The agent to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    Agent agent = new Agent();
    // Make the request
    Agent response = agentServiceClient.CreateAgent(parent, agent);
    

### CreateAgent(string, Agent, string, CallSettings)
    
    
    public virtual Agent CreateAgent(string parent, Agent agent, string agentId, CallSettings callSettings = null)

Creates a new agent in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to create an agent in.  
`agent` | `[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)`  
Required. The agent to create.  
`agentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the agent, which will become the final component of the agent's resource name. If not provided, a unique ID will be automatically assigned for the agent.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    Agent agent = new Agent();
    string agentId = "";
    // Make the request
    Agent response = agentServiceClient.CreateAgent(parent, agent, agentId);
    

### CreateAgentAsync(AppName, Agent, CallSettings)
    
    
    public virtual Task<Agent> CreateAgentAsync(AppName parent, Agent agent, CallSettings callSettings = null)

Creates a new agent in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to create an agent in.  
`agent` | `[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)`  
Required. The agent to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    Agent agent = new Agent();
    // Make the request
    Agent response = await agentServiceClient.CreateAgentAsync(parent, agent);
    

### CreateAgentAsync(AppName, Agent, string, CallSettings)
    
    
    public virtual Task<Agent> CreateAgentAsync(AppName parent, Agent agent, string agentId, CallSettings callSettings = null)

Creates a new agent in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to create an agent in.  
`agent` | `[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)`  
Required. The agent to create.  
`agentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the agent, which will become the final component of the agent's resource name. If not provided, a unique ID will be automatically assigned for the agent.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    Agent agent = new Agent();
    string agentId = "";
    // Make the request
    Agent response = await agentServiceClient.CreateAgentAsync(parent, agent, agentId);
    

### CreateAgentAsync(AppName, Agent, string, CancellationToken)
    
    
    public virtual Task<Agent> CreateAgentAsync(AppName parent, Agent agent, string agentId, CancellationToken cancellationToken)

Creates a new agent in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to create an agent in.  
`agent` | `[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)`  
Required. The agent to create.  
`agentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the agent, which will become the final component of the agent's resource name. If not provided, a unique ID will be automatically assigned for the agent.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    Agent agent = new Agent();
    string agentId = "";
    // Make the request
    Agent response = await agentServiceClient.CreateAgentAsync(parent, agent, agentId);
    

### CreateAgentAsync(AppName, Agent, CancellationToken)
    
    
    public virtual Task<Agent> CreateAgentAsync(AppName parent, Agent agent, CancellationToken cancellationToken)

Creates a new agent in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to create an agent in.  
`agent` | `[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)`  
Required. The agent to create.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    Agent agent = new Agent();
    // Make the request
    Agent response = await agentServiceClient.CreateAgentAsync(parent, agent);
    

### CreateAgentAsync(CreateAgentRequest, CallSettings)
    
    
    public virtual Task<Agent> CreateAgentAsync(CreateAgentRequest request, CallSettings callSettings = null)

Creates a new agent in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateAgentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateAgentRequest request = new CreateAgentRequest
    {
        ParentAsAppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
        AgentId = "",
        Agent = new Agent(),
    };
    // Make the request
    Agent response = await agentServiceClient.CreateAgentAsync(request);
    

### CreateAgentAsync(CreateAgentRequest, CancellationToken)
    
    
    public virtual Task<Agent> CreateAgentAsync(CreateAgentRequest request, CancellationToken cancellationToken)

Creates a new agent in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateAgentRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateAgentRequest request = new CreateAgentRequest
    {
        ParentAsAppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
        AgentId = "",
        Agent = new Agent(),
    };
    // Make the request
    Agent response = await agentServiceClient.CreateAgentAsync(request);
    

### CreateAgentAsync(string, Agent, CallSettings)
    
    
    public virtual Task<Agent> CreateAgentAsync(string parent, Agent agent, CallSettings callSettings = null)

Creates a new agent in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to create an agent in.  
`agent` | `[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)`  
Required. The agent to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    Agent agent = new Agent();
    // Make the request
    Agent response = await agentServiceClient.CreateAgentAsync(parent, agent);
    

### CreateAgentAsync(string, Agent, string, CallSettings)
    
    
    public virtual Task<Agent> CreateAgentAsync(string parent, Agent agent, string agentId, CallSettings callSettings = null)

Creates a new agent in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to create an agent in.  
`agent` | `[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)`  
Required. The agent to create.  
`agentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the agent, which will become the final component of the agent's resource name. If not provided, a unique ID will be automatically assigned for the agent.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    Agent agent = new Agent();
    string agentId = "";
    // Make the request
    Agent response = await agentServiceClient.CreateAgentAsync(parent, agent, agentId);
    

### CreateAgentAsync(string, Agent, string, CancellationToken)
    
    
    public virtual Task<Agent> CreateAgentAsync(string parent, Agent agent, string agentId, CancellationToken cancellationToken)

Creates a new agent in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to create an agent in.  
`agent` | `[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)`  
Required. The agent to create.  
`agentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the agent, which will become the final component of the agent's resource name. If not provided, a unique ID will be automatically assigned for the agent.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    Agent agent = new Agent();
    string agentId = "";
    // Make the request
    Agent response = await agentServiceClient.CreateAgentAsync(parent, agent, agentId);
    

### CreateAgentAsync(string, Agent, CancellationToken)
    
    
    public virtual Task<Agent> CreateAgentAsync(string parent, Agent agent, CancellationToken cancellationToken)

Creates a new agent in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to create an agent in.  
`agent` | `[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)`  
Required. The agent to create.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    Agent agent = new Agent();
    // Make the request
    Agent response = await agentServiceClient.CreateAgentAsync(parent, agent);
    

### CreateApp(LocationName, App, CallSettings)
    
    
    public virtual Operation<App, OperationMetadata> CreateApp(LocationName parent, App app, CallSettings callSettings = null)

Creates a new app in the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The resource name of the location to create an app in.  
`app` | `[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)`  
Required. The app to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    App app = new App();
    // Make the request
    Operation<App, OperationMetadata> response = agentServiceClient.CreateApp(parent, app);
    
    // Poll until the returned long-running operation is complete
    Operation<App, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    App result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<App, OperationMetadata> retrievedResponse = agentServiceClient.PollOnceCreateApp(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        App retrievedResult = retrievedResponse.Result;
    }
    

### CreateApp(LocationName, App, string, CallSettings)
    
    
    public virtual Operation<App, OperationMetadata> CreateApp(LocationName parent, App app, string appId, CallSettings callSettings = null)

Creates a new app in the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The resource name of the location to create an app in.  
`app` | `[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)`  
Required. The app to create.  
`appId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the app, which will become the final component of the app's resource name. If not provided, a unique ID will be automatically assigned for the app.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    App app = new App();
    string appId = "";
    // Make the request
    Operation<App, OperationMetadata> response = agentServiceClient.CreateApp(parent, app, appId);
    
    // Poll until the returned long-running operation is complete
    Operation<App, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    App result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<App, OperationMetadata> retrievedResponse = agentServiceClient.PollOnceCreateApp(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        App retrievedResult = retrievedResponse.Result;
    }
    

### CreateApp(CreateAppRequest, CallSettings)
    
    
    public virtual Operation<App, OperationMetadata> CreateApp(CreateAppRequest request, CallSettings callSettings = null)

Creates a new app in the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateAppRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    CreateAppRequest request = new CreateAppRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        AppId = "",
        App = new App(),
    };
    // Make the request
    Operation<App, OperationMetadata> response = agentServiceClient.CreateApp(request);
    
    // Poll until the returned long-running operation is complete
    Operation<App, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    App result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<App, OperationMetadata> retrievedResponse = agentServiceClient.PollOnceCreateApp(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        App retrievedResult = retrievedResponse.Result;
    }
    

### CreateApp(string, App, CallSettings)
    
    
    public virtual Operation<App, OperationMetadata> CreateApp(string parent, App app, CallSettings callSettings = null)

Creates a new app in the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the location to create an app in.  
`app` | `[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)`  
Required. The app to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    App app = new App();
    // Make the request
    Operation<App, OperationMetadata> response = agentServiceClient.CreateApp(parent, app);
    
    // Poll until the returned long-running operation is complete
    Operation<App, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    App result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<App, OperationMetadata> retrievedResponse = agentServiceClient.PollOnceCreateApp(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        App retrievedResult = retrievedResponse.Result;
    }
    

### CreateApp(string, App, string, CallSettings)
    
    
    public virtual Operation<App, OperationMetadata> CreateApp(string parent, App app, string appId, CallSettings callSettings = null)

Creates a new app in the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the location to create an app in.  
`app` | `[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)`  
Required. The app to create.  
`appId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the app, which will become the final component of the app's resource name. If not provided, a unique ID will be automatically assigned for the app.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    App app = new App();
    string appId = "";
    // Make the request
    Operation<App, OperationMetadata> response = agentServiceClient.CreateApp(parent, app, appId);
    
    // Poll until the returned long-running operation is complete
    Operation<App, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    App result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<App, OperationMetadata> retrievedResponse = agentServiceClient.PollOnceCreateApp(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        App retrievedResult = retrievedResponse.Result;
    }
    

### CreateAppAsync(LocationName, App, CallSettings)
    
    
    public virtual Task<Operation<App, OperationMetadata>> CreateAppAsync(LocationName parent, App app, CallSettings callSettings = null)

Creates a new app in the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The resource name of the location to create an app in.  
`app` | `[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)`  
Required. The app to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    App app = new App();
    // Make the request
    Operation<App, OperationMetadata> response = await agentServiceClient.CreateAppAsync(parent, app);
    
    // Poll until the returned long-running operation is complete
    Operation<App, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    App result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<App, OperationMetadata> retrievedResponse = await agentServiceClient.PollOnceCreateAppAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        App retrievedResult = retrievedResponse.Result;
    }
    

### CreateAppAsync(LocationName, App, string, CallSettings)
    
    
    public virtual Task<Operation<App, OperationMetadata>> CreateAppAsync(LocationName parent, App app, string appId, CallSettings callSettings = null)

Creates a new app in the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The resource name of the location to create an app in.  
`app` | `[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)`  
Required. The app to create.  
`appId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the app, which will become the final component of the app's resource name. If not provided, a unique ID will be automatically assigned for the app.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    App app = new App();
    string appId = "";
    // Make the request
    Operation<App, OperationMetadata> response = await agentServiceClient.CreateAppAsync(parent, app, appId);
    
    // Poll until the returned long-running operation is complete
    Operation<App, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    App result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<App, OperationMetadata> retrievedResponse = await agentServiceClient.PollOnceCreateAppAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        App retrievedResult = retrievedResponse.Result;
    }
    

### CreateAppAsync(LocationName, App, string, CancellationToken)
    
    
    public virtual Task<Operation<App, OperationMetadata>> CreateAppAsync(LocationName parent, App app, string appId, CancellationToken cancellationToken)

Creates a new app in the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The resource name of the location to create an app in.  
`app` | `[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)`  
Required. The app to create.  
`appId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the app, which will become the final component of the app's resource name. If not provided, a unique ID will be automatically assigned for the app.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    App app = new App();
    string appId = "";
    // Make the request
    Operation<App, OperationMetadata> response = await agentServiceClient.CreateAppAsync(parent, app, appId);
    
    // Poll until the returned long-running operation is complete
    Operation<App, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    App result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<App, OperationMetadata> retrievedResponse = await agentServiceClient.PollOnceCreateAppAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        App retrievedResult = retrievedResponse.Result;
    }
    

### CreateAppAsync(LocationName, App, CancellationToken)
    
    
    public virtual Task<Operation<App, OperationMetadata>> CreateAppAsync(LocationName parent, App app, CancellationToken cancellationToken)

Creates a new app in the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The resource name of the location to create an app in.  
`app` | `[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)`  
Required. The app to create.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    App app = new App();
    // Make the request
    Operation<App, OperationMetadata> response = await agentServiceClient.CreateAppAsync(parent, app);
    
    // Poll until the returned long-running operation is complete
    Operation<App, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    App result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<App, OperationMetadata> retrievedResponse = await agentServiceClient.PollOnceCreateAppAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        App retrievedResult = retrievedResponse.Result;
    }
    

### CreateAppAsync(CreateAppRequest, CallSettings)
    
    
    public virtual Task<Operation<App, OperationMetadata>> CreateAppAsync(CreateAppRequest request, CallSettings callSettings = null)

Creates a new app in the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateAppRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateAppRequest request = new CreateAppRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        AppId = "",
        App = new App(),
    };
    // Make the request
    Operation<App, OperationMetadata> response = await agentServiceClient.CreateAppAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<App, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    App result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<App, OperationMetadata> retrievedResponse = await agentServiceClient.PollOnceCreateAppAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        App retrievedResult = retrievedResponse.Result;
    }
    

### CreateAppAsync(CreateAppRequest, CancellationToken)
    
    
    public virtual Task<Operation<App, OperationMetadata>> CreateAppAsync(CreateAppRequest request, CancellationToken cancellationToken)

Creates a new app in the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateAppRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateAppRequest request = new CreateAppRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        AppId = "",
        App = new App(),
    };
    // Make the request
    Operation<App, OperationMetadata> response = await agentServiceClient.CreateAppAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<App, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    App result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<App, OperationMetadata> retrievedResponse = await agentServiceClient.PollOnceCreateAppAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        App retrievedResult = retrievedResponse.Result;
    }
    

### CreateAppAsync(string, App, CallSettings)
    
    
    public virtual Task<Operation<App, OperationMetadata>> CreateAppAsync(string parent, App app, CallSettings callSettings = null)

Creates a new app in the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the location to create an app in.  
`app` | `[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)`  
Required. The app to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    App app = new App();
    // Make the request
    Operation<App, OperationMetadata> response = await agentServiceClient.CreateAppAsync(parent, app);
    
    // Poll until the returned long-running operation is complete
    Operation<App, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    App result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<App, OperationMetadata> retrievedResponse = await agentServiceClient.PollOnceCreateAppAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        App retrievedResult = retrievedResponse.Result;
    }
    

### CreateAppAsync(string, App, string, CallSettings)
    
    
    public virtual Task<Operation<App, OperationMetadata>> CreateAppAsync(string parent, App app, string appId, CallSettings callSettings = null)

Creates a new app in the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the location to create an app in.  
`app` | `[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)`  
Required. The app to create.  
`appId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the app, which will become the final component of the app's resource name. If not provided, a unique ID will be automatically assigned for the app.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    App app = new App();
    string appId = "";
    // Make the request
    Operation<App, OperationMetadata> response = await agentServiceClient.CreateAppAsync(parent, app, appId);
    
    // Poll until the returned long-running operation is complete
    Operation<App, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    App result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<App, OperationMetadata> retrievedResponse = await agentServiceClient.PollOnceCreateAppAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        App retrievedResult = retrievedResponse.Result;
    }
    

### CreateAppAsync(string, App, string, CancellationToken)
    
    
    public virtual Task<Operation<App, OperationMetadata>> CreateAppAsync(string parent, App app, string appId, CancellationToken cancellationToken)

Creates a new app in the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the location to create an app in.  
`app` | `[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)`  
Required. The app to create.  
`appId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the app, which will become the final component of the app's resource name. If not provided, a unique ID will be automatically assigned for the app.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    App app = new App();
    string appId = "";
    // Make the request
    Operation<App, OperationMetadata> response = await agentServiceClient.CreateAppAsync(parent, app, appId);
    
    // Poll until the returned long-running operation is complete
    Operation<App, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    App result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<App, OperationMetadata> retrievedResponse = await agentServiceClient.PollOnceCreateAppAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        App retrievedResult = retrievedResponse.Result;
    }
    

### CreateAppAsync(string, App, CancellationToken)
    
    
    public virtual Task<Operation<App, OperationMetadata>> CreateAppAsync(string parent, App app, CancellationToken cancellationToken)

Creates a new app in the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the location to create an app in.  
`app` | `[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)`  
Required. The app to create.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    App app = new App();
    // Make the request
    Operation<App, OperationMetadata> response = await agentServiceClient.CreateAppAsync(parent, app);
    
    // Poll until the returned long-running operation is complete
    Operation<App, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    App result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<App, OperationMetadata> retrievedResponse = await agentServiceClient.PollOnceCreateAppAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        App retrievedResult = retrievedResponse.Result;
    }
    

### CreateAppVersion(AppName, AppVersion, CallSettings)
    
    
    public virtual AppVersion CreateAppVersion(AppName parent, AppVersion appVersion, CallSettings callSettings = null)

Creates a new app version in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to create an app version in.  
`appVersion` | `[AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion)`  
Required. The app version to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    AppVersion appVersion = new AppVersion();
    // Make the request
    AppVersion response = agentServiceClient.CreateAppVersion(parent, appVersion);
    

### CreateAppVersion(AppName, AppVersion, string, CallSettings)
    
    
    public virtual AppVersion CreateAppVersion(AppName parent, AppVersion appVersion, string appVersionId, CallSettings callSettings = null)

Creates a new app version in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to create an app version in.  
`appVersion` | `[AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion)`  
Required. The app version to create.  
`appVersionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the app version, which will become the final component of the app version's resource name. If not provided, a unique ID will be automatically assigned for the app version.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    AppVersion appVersion = new AppVersion();
    string appVersionId = "";
    // Make the request
    AppVersion response = agentServiceClient.CreateAppVersion(parent, appVersion, appVersionId);
    

### CreateAppVersion(CreateAppVersionRequest, CallSettings)
    
    
    public virtual AppVersion CreateAppVersion(CreateAppVersionRequest request, CallSettings callSettings = null)

Creates a new app version in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAppVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateAppVersionRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    CreateAppVersionRequest request = new CreateAppVersionRequest
    {
        ParentAsAppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
        AppVersionId = "",
        AppVersion = new AppVersion(),
    };
    // Make the request
    AppVersion response = agentServiceClient.CreateAppVersion(request);
    

### CreateAppVersion(string, AppVersion, CallSettings)
    
    
    public virtual AppVersion CreateAppVersion(string parent, AppVersion appVersion, CallSettings callSettings = null)

Creates a new app version in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to create an app version in.  
`appVersion` | `[AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion)`  
Required. The app version to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    AppVersion appVersion = new AppVersion();
    // Make the request
    AppVersion response = agentServiceClient.CreateAppVersion(parent, appVersion);
    

### CreateAppVersion(string, AppVersion, string, CallSettings)
    
    
    public virtual AppVersion CreateAppVersion(string parent, AppVersion appVersion, string appVersionId, CallSettings callSettings = null)

Creates a new app version in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to create an app version in.  
`appVersion` | `[AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion)`  
Required. The app version to create.  
`appVersionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the app version, which will become the final component of the app version's resource name. If not provided, a unique ID will be automatically assigned for the app version.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    AppVersion appVersion = new AppVersion();
    string appVersionId = "";
    // Make the request
    AppVersion response = agentServiceClient.CreateAppVersion(parent, appVersion, appVersionId);
    

### CreateAppVersionAsync(AppName, AppVersion, CallSettings)
    
    
    public virtual Task<AppVersion> CreateAppVersionAsync(AppName parent, AppVersion appVersion, CallSettings callSettings = null)

Creates a new app version in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to create an app version in.  
`appVersion` | `[AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion)`  
Required. The app version to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    AppVersion appVersion = new AppVersion();
    // Make the request
    AppVersion response = await agentServiceClient.CreateAppVersionAsync(parent, appVersion);
    

### CreateAppVersionAsync(AppName, AppVersion, string, CallSettings)
    
    
    public virtual Task<AppVersion> CreateAppVersionAsync(AppName parent, AppVersion appVersion, string appVersionId, CallSettings callSettings = null)

Creates a new app version in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to create an app version in.  
`appVersion` | `[AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion)`  
Required. The app version to create.  
`appVersionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the app version, which will become the final component of the app version's resource name. If not provided, a unique ID will be automatically assigned for the app version.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    AppVersion appVersion = new AppVersion();
    string appVersionId = "";
    // Make the request
    AppVersion response = await agentServiceClient.CreateAppVersionAsync(parent, appVersion, appVersionId);
    

### CreateAppVersionAsync(AppName, AppVersion, string, CancellationToken)
    
    
    public virtual Task<AppVersion> CreateAppVersionAsync(AppName parent, AppVersion appVersion, string appVersionId, CancellationToken cancellationToken)

Creates a new app version in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to create an app version in.  
`appVersion` | `[AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion)`  
Required. The app version to create.  
`appVersionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the app version, which will become the final component of the app version's resource name. If not provided, a unique ID will be automatically assigned for the app version.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    AppVersion appVersion = new AppVersion();
    string appVersionId = "";
    // Make the request
    AppVersion response = await agentServiceClient.CreateAppVersionAsync(parent, appVersion, appVersionId);
    

### CreateAppVersionAsync(AppName, AppVersion, CancellationToken)
    
    
    public virtual Task<AppVersion> CreateAppVersionAsync(AppName parent, AppVersion appVersion, CancellationToken cancellationToken)

Creates a new app version in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to create an app version in.  
`appVersion` | `[AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion)`  
Required. The app version to create.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    AppVersion appVersion = new AppVersion();
    // Make the request
    AppVersion response = await agentServiceClient.CreateAppVersionAsync(parent, appVersion);
    

### CreateAppVersionAsync(CreateAppVersionRequest, CallSettings)
    
    
    public virtual Task<AppVersion> CreateAppVersionAsync(CreateAppVersionRequest request, CallSettings callSettings = null)

Creates a new app version in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAppVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateAppVersionRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateAppVersionRequest request = new CreateAppVersionRequest
    {
        ParentAsAppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
        AppVersionId = "",
        AppVersion = new AppVersion(),
    };
    // Make the request
    AppVersion response = await agentServiceClient.CreateAppVersionAsync(request);
    

### CreateAppVersionAsync(CreateAppVersionRequest, CancellationToken)
    
    
    public virtual Task<AppVersion> CreateAppVersionAsync(CreateAppVersionRequest request, CancellationToken cancellationToken)

Creates a new app version in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAppVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateAppVersionRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateAppVersionRequest request = new CreateAppVersionRequest
    {
        ParentAsAppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
        AppVersionId = "",
        AppVersion = new AppVersion(),
    };
    // Make the request
    AppVersion response = await agentServiceClient.CreateAppVersionAsync(request);
    

### CreateAppVersionAsync(string, AppVersion, CallSettings)
    
    
    public virtual Task<AppVersion> CreateAppVersionAsync(string parent, AppVersion appVersion, CallSettings callSettings = null)

Creates a new app version in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to create an app version in.  
`appVersion` | `[AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion)`  
Required. The app version to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    AppVersion appVersion = new AppVersion();
    // Make the request
    AppVersion response = await agentServiceClient.CreateAppVersionAsync(parent, appVersion);
    

### CreateAppVersionAsync(string, AppVersion, string, CallSettings)
    
    
    public virtual Task<AppVersion> CreateAppVersionAsync(string parent, AppVersion appVersion, string appVersionId, CallSettings callSettings = null)

Creates a new app version in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to create an app version in.  
`appVersion` | `[AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion)`  
Required. The app version to create.  
`appVersionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the app version, which will become the final component of the app version's resource name. If not provided, a unique ID will be automatically assigned for the app version.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    AppVersion appVersion = new AppVersion();
    string appVersionId = "";
    // Make the request
    AppVersion response = await agentServiceClient.CreateAppVersionAsync(parent, appVersion, appVersionId);
    

### CreateAppVersionAsync(string, AppVersion, string, CancellationToken)
    
    
    public virtual Task<AppVersion> CreateAppVersionAsync(string parent, AppVersion appVersion, string appVersionId, CancellationToken cancellationToken)

Creates a new app version in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to create an app version in.  
`appVersion` | `[AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion)`  
Required. The app version to create.  
`appVersionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the app version, which will become the final component of the app version's resource name. If not provided, a unique ID will be automatically assigned for the app version.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    AppVersion appVersion = new AppVersion();
    string appVersionId = "";
    // Make the request
    AppVersion response = await agentServiceClient.CreateAppVersionAsync(parent, appVersion, appVersionId);
    

### CreateAppVersionAsync(string, AppVersion, CancellationToken)
    
    
    public virtual Task<AppVersion> CreateAppVersionAsync(string parent, AppVersion appVersion, CancellationToken cancellationToken)

Creates a new app version in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to create an app version in.  
`appVersion` | `[AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion)`  
Required. The app version to create.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    AppVersion appVersion = new AppVersion();
    // Make the request
    AppVersion response = await agentServiceClient.CreateAppVersionAsync(parent, appVersion);
    

### CreateAsync(CancellationToken)
    
    
    public static Task<AgentServiceClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [AgentServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [AgentServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentServiceClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AgentServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentServiceClient)` | The task representing the created [AgentServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentServiceClient).  
  
### CreateDeployment(AppName, Deployment, CallSettings)
    
    
    public virtual Deployment CreateDeployment(AppName parent, Deployment deployment, CallSettings callSettings = null)

Creates a new deployment in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The parent app. Format: `projects/{project}/locations/{location}/apps/{app}`  
`deployment` | `[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)`  
Required. The deployment to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    Deployment deployment = new Deployment();
    // Make the request
    Deployment response = agentServiceClient.CreateDeployment(parent, deployment);
    

### CreateDeployment(AppName, Deployment, string, CallSettings)
    
    
    public virtual Deployment CreateDeployment(AppName parent, Deployment deployment, string deploymentId, CallSettings callSettings = null)

Creates a new deployment in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The parent app. Format: `projects/{project}/locations/{location}/apps/{app}`  
`deployment` | `[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)`  
Required. The deployment to create.  
`deploymentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the deployment, which will become the final component of the deployment's resource name. If not provided, a unique ID will be automatically assigned for the deployment.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    Deployment deployment = new Deployment();
    string deploymentId = "";
    // Make the request
    Deployment response = agentServiceClient.CreateDeployment(parent, deployment, deploymentId);
    

### CreateDeployment(CreateDeploymentRequest, CallSettings)
    
    
    public virtual Deployment CreateDeployment(CreateDeploymentRequest request, CallSettings callSettings = null)

Creates a new deployment in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateDeploymentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    CreateDeploymentRequest request = new CreateDeploymentRequest
    {
        ParentAsAppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
        Deployment = new Deployment(),
        DeploymentId = "",
    };
    // Make the request
    Deployment response = agentServiceClient.CreateDeployment(request);
    

### CreateDeployment(string, Deployment, CallSettings)
    
    
    public virtual Deployment CreateDeployment(string parent, Deployment deployment, CallSettings callSettings = null)

Creates a new deployment in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent app. Format: `projects/{project}/locations/{location}/apps/{app}`  
`deployment` | `[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)`  
Required. The deployment to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    Deployment deployment = new Deployment();
    // Make the request
    Deployment response = agentServiceClient.CreateDeployment(parent, deployment);
    

### CreateDeployment(string, Deployment, string, CallSettings)
    
    
    public virtual Deployment CreateDeployment(string parent, Deployment deployment, string deploymentId, CallSettings callSettings = null)

Creates a new deployment in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent app. Format: `projects/{project}/locations/{location}/apps/{app}`  
`deployment` | `[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)`  
Required. The deployment to create.  
`deploymentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the deployment, which will become the final component of the deployment's resource name. If not provided, a unique ID will be automatically assigned for the deployment.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    Deployment deployment = new Deployment();
    string deploymentId = "";
    // Make the request
    Deployment response = agentServiceClient.CreateDeployment(parent, deployment, deploymentId);
    

### CreateDeploymentAsync(AppName, Deployment, CallSettings)
    
    
    public virtual Task<Deployment> CreateDeploymentAsync(AppName parent, Deployment deployment, CallSettings callSettings = null)

Creates a new deployment in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The parent app. Format: `projects/{project}/locations/{location}/apps/{app}`  
`deployment` | `[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)`  
Required. The deployment to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    Deployment deployment = new Deployment();
    // Make the request
    Deployment response = await agentServiceClient.CreateDeploymentAsync(parent, deployment);
    

### CreateDeploymentAsync(AppName, Deployment, string, CallSettings)
    
    
    public virtual Task<Deployment> CreateDeploymentAsync(AppName parent, Deployment deployment, string deploymentId, CallSettings callSettings = null)

Creates a new deployment in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The parent app. Format: `projects/{project}/locations/{location}/apps/{app}`  
`deployment` | `[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)`  
Required. The deployment to create.  
`deploymentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the deployment, which will become the final component of the deployment's resource name. If not provided, a unique ID will be automatically assigned for the deployment.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    Deployment deployment = new Deployment();
    string deploymentId = "";
    // Make the request
    Deployment response = await agentServiceClient.CreateDeploymentAsync(parent, deployment, deploymentId);
    

### CreateDeploymentAsync(AppName, Deployment, string, CancellationToken)
    
    
    public virtual Task<Deployment> CreateDeploymentAsync(AppName parent, Deployment deployment, string deploymentId, CancellationToken cancellationToken)

Creates a new deployment in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The parent app. Format: `projects/{project}/locations/{location}/apps/{app}`  
`deployment` | `[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)`  
Required. The deployment to create.  
`deploymentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the deployment, which will become the final component of the deployment's resource name. If not provided, a unique ID will be automatically assigned for the deployment.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    Deployment deployment = new Deployment();
    string deploymentId = "";
    // Make the request
    Deployment response = await agentServiceClient.CreateDeploymentAsync(parent, deployment, deploymentId);
    

### CreateDeploymentAsync(AppName, Deployment, CancellationToken)
    
    
    public virtual Task<Deployment> CreateDeploymentAsync(AppName parent, Deployment deployment, CancellationToken cancellationToken)

Creates a new deployment in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The parent app. Format: `projects/{project}/locations/{location}/apps/{app}`  
`deployment` | `[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)`  
Required. The deployment to create.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    Deployment deployment = new Deployment();
    // Make the request
    Deployment response = await agentServiceClient.CreateDeploymentAsync(parent, deployment);
    

### CreateDeploymentAsync(CreateDeploymentRequest, CallSettings)
    
    
    public virtual Task<Deployment> CreateDeploymentAsync(CreateDeploymentRequest request, CallSettings callSettings = null)

Creates a new deployment in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateDeploymentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateDeploymentRequest request = new CreateDeploymentRequest
    {
        ParentAsAppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
        Deployment = new Deployment(),
        DeploymentId = "",
    };
    // Make the request
    Deployment response = await agentServiceClient.CreateDeploymentAsync(request);
    

### CreateDeploymentAsync(CreateDeploymentRequest, CancellationToken)
    
    
    public virtual Task<Deployment> CreateDeploymentAsync(CreateDeploymentRequest request, CancellationToken cancellationToken)

Creates a new deployment in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateDeploymentRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateDeploymentRequest request = new CreateDeploymentRequest
    {
        ParentAsAppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
        Deployment = new Deployment(),
        DeploymentId = "",
    };
    // Make the request
    Deployment response = await agentServiceClient.CreateDeploymentAsync(request);
    

### CreateDeploymentAsync(string, Deployment, CallSettings)
    
    
    public virtual Task<Deployment> CreateDeploymentAsync(string parent, Deployment deployment, CallSettings callSettings = null)

Creates a new deployment in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent app. Format: `projects/{project}/locations/{location}/apps/{app}`  
`deployment` | `[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)`  
Required. The deployment to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    Deployment deployment = new Deployment();
    // Make the request
    Deployment response = await agentServiceClient.CreateDeploymentAsync(parent, deployment);
    

### CreateDeploymentAsync(string, Deployment, string, CallSettings)
    
    
    public virtual Task<Deployment> CreateDeploymentAsync(string parent, Deployment deployment, string deploymentId, CallSettings callSettings = null)

Creates a new deployment in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent app. Format: `projects/{project}/locations/{location}/apps/{app}`  
`deployment` | `[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)`  
Required. The deployment to create.  
`deploymentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the deployment, which will become the final component of the deployment's resource name. If not provided, a unique ID will be automatically assigned for the deployment.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    Deployment deployment = new Deployment();
    string deploymentId = "";
    // Make the request
    Deployment response = await agentServiceClient.CreateDeploymentAsync(parent, deployment, deploymentId);
    

### CreateDeploymentAsync(string, Deployment, string, CancellationToken)
    
    
    public virtual Task<Deployment> CreateDeploymentAsync(string parent, Deployment deployment, string deploymentId, CancellationToken cancellationToken)

Creates a new deployment in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent app. Format: `projects/{project}/locations/{location}/apps/{app}`  
`deployment` | `[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)`  
Required. The deployment to create.  
`deploymentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the deployment, which will become the final component of the deployment's resource name. If not provided, a unique ID will be automatically assigned for the deployment.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    Deployment deployment = new Deployment();
    string deploymentId = "";
    // Make the request
    Deployment response = await agentServiceClient.CreateDeploymentAsync(parent, deployment, deploymentId);
    

### CreateDeploymentAsync(string, Deployment, CancellationToken)
    
    
    public virtual Task<Deployment> CreateDeploymentAsync(string parent, Deployment deployment, CancellationToken cancellationToken)

Creates a new deployment in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent app. Format: `projects/{project}/locations/{location}/apps/{app}`  
`deployment` | `[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)`  
Required. The deployment to create.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    Deployment deployment = new Deployment();
    // Make the request
    Deployment response = await agentServiceClient.CreateDeploymentAsync(parent, deployment);
    

### CreateExample(AppName, Example, CallSettings)
    
    
    public virtual Example CreateExample(AppName parent, Example example, CallSettings callSettings = null)

Creates a new example in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to create an example in.  
`example` | `[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)`  
Required. The example to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    Example example = new Example();
    // Make the request
    Example response = agentServiceClient.CreateExample(parent, example);
    

### CreateExample(AppName, Example, string, CallSettings)
    
    
    public virtual Example CreateExample(AppName parent, Example example, string exampleId, CallSettings callSettings = null)

Creates a new example in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to create an example in.  
`example` | `[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)`  
Required. The example to create.  
`exampleId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the example, which will become the final component of the example's resource name. If not provided, a unique ID will be automatically assigned for the example.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    Example example = new Example();
    string exampleId = "";
    // Make the request
    Example response = agentServiceClient.CreateExample(parent, example, exampleId);
    

### CreateExample(CreateExampleRequest, CallSettings)
    
    
    public virtual Example CreateExample(CreateExampleRequest request, CallSettings callSettings = null)

Creates a new example in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateExampleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateExampleRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    CreateExampleRequest request = new CreateExampleRequest
    {
        ParentAsAppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
        ExampleId = "",
        Example = new Example(),
    };
    // Make the request
    Example response = agentServiceClient.CreateExample(request);
    

### CreateExample(string, Example, CallSettings)
    
    
    public virtual Example CreateExample(string parent, Example example, CallSettings callSettings = null)

Creates a new example in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to create an example in.  
`example` | `[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)`  
Required. The example to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    Example example = new Example();
    // Make the request
    Example response = agentServiceClient.CreateExample(parent, example);
    

### CreateExample(string, Example, string, CallSettings)
    
    
    public virtual Example CreateExample(string parent, Example example, string exampleId, CallSettings callSettings = null)

Creates a new example in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to create an example in.  
`example` | `[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)`  
Required. The example to create.  
`exampleId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the example, which will become the final component of the example's resource name. If not provided, a unique ID will be automatically assigned for the example.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    Example example = new Example();
    string exampleId = "";
    // Make the request
    Example response = agentServiceClient.CreateExample(parent, example, exampleId);
    

### CreateExampleAsync(AppName, Example, CallSettings)
    
    
    public virtual Task<Example> CreateExampleAsync(AppName parent, Example example, CallSettings callSettings = null)

Creates a new example in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to create an example in.  
`example` | `[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)`  
Required. The example to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    Example example = new Example();
    // Make the request
    Example response = await agentServiceClient.CreateExampleAsync(parent, example);
    

### CreateExampleAsync(AppName, Example, string, CallSettings)
    
    
    public virtual Task<Example> CreateExampleAsync(AppName parent, Example example, string exampleId, CallSettings callSettings = null)

Creates a new example in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to create an example in.  
`example` | `[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)`  
Required. The example to create.  
`exampleId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the example, which will become the final component of the example's resource name. If not provided, a unique ID will be automatically assigned for the example.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    Example example = new Example();
    string exampleId = "";
    // Make the request
    Example response = await agentServiceClient.CreateExampleAsync(parent, example, exampleId);
    

### CreateExampleAsync(AppName, Example, string, CancellationToken)
    
    
    public virtual Task<Example> CreateExampleAsync(AppName parent, Example example, string exampleId, CancellationToken cancellationToken)

Creates a new example in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to create an example in.  
`example` | `[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)`  
Required. The example to create.  
`exampleId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the example, which will become the final component of the example's resource name. If not provided, a unique ID will be automatically assigned for the example.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    Example example = new Example();
    string exampleId = "";
    // Make the request
    Example response = await agentServiceClient.CreateExampleAsync(parent, example, exampleId);
    

### CreateExampleAsync(AppName, Example, CancellationToken)
    
    
    public virtual Task<Example> CreateExampleAsync(AppName parent, Example example, CancellationToken cancellationToken)

Creates a new example in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to create an example in.  
`example` | `[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)`  
Required. The example to create.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    Example example = new Example();
    // Make the request
    Example response = await agentServiceClient.CreateExampleAsync(parent, example);
    

### CreateExampleAsync(CreateExampleRequest, CallSettings)
    
    
    public virtual Task<Example> CreateExampleAsync(CreateExampleRequest request, CallSettings callSettings = null)

Creates a new example in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateExampleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateExampleRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateExampleRequest request = new CreateExampleRequest
    {
        ParentAsAppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
        ExampleId = "",
        Example = new Example(),
    };
    // Make the request
    Example response = await agentServiceClient.CreateExampleAsync(request);
    

### CreateExampleAsync(CreateExampleRequest, CancellationToken)
    
    
    public virtual Task<Example> CreateExampleAsync(CreateExampleRequest request, CancellationToken cancellationToken)

Creates a new example in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateExampleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateExampleRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateExampleRequest request = new CreateExampleRequest
    {
        ParentAsAppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
        ExampleId = "",
        Example = new Example(),
    };
    // Make the request
    Example response = await agentServiceClient.CreateExampleAsync(request);
    

### CreateExampleAsync(string, Example, CallSettings)
    
    
    public virtual Task<Example> CreateExampleAsync(string parent, Example example, CallSettings callSettings = null)

Creates a new example in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to create an example in.  
`example` | `[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)`  
Required. The example to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    Example example = new Example();
    // Make the request
    Example response = await agentServiceClient.CreateExampleAsync(parent, example);
    

### CreateExampleAsync(string, Example, string, CallSettings)
    
    
    public virtual Task<Example> CreateExampleAsync(string parent, Example example, string exampleId, CallSettings callSettings = null)

Creates a new example in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to create an example in.  
`example` | `[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)`  
Required. The example to create.  
`exampleId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the example, which will become the final component of the example's resource name. If not provided, a unique ID will be automatically assigned for the example.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    Example example = new Example();
    string exampleId = "";
    // Make the request
    Example response = await agentServiceClient.CreateExampleAsync(parent, example, exampleId);
    

### CreateExampleAsync(string, Example, string, CancellationToken)
    
    
    public virtual Task<Example> CreateExampleAsync(string parent, Example example, string exampleId, CancellationToken cancellationToken)

Creates a new example in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to create an example in.  
`example` | `[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)`  
Required. The example to create.  
`exampleId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the example, which will become the final component of the example's resource name. If not provided, a unique ID will be automatically assigned for the example.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    Example example = new Example();
    string exampleId = "";
    // Make the request
    Example response = await agentServiceClient.CreateExampleAsync(parent, example, exampleId);
    

### CreateExampleAsync(string, Example, CancellationToken)
    
    
    public virtual Task<Example> CreateExampleAsync(string parent, Example example, CancellationToken cancellationToken)

Creates a new example in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to create an example in.  
`example` | `[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)`  
Required. The example to create.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    Example example = new Example();
    // Make the request
    Example response = await agentServiceClient.CreateExampleAsync(parent, example);
    

### CreateGuardrail(AppName, Guardrail, CallSettings)
    
    
    public virtual Guardrail CreateGuardrail(AppName parent, Guardrail guardrail, CallSettings callSettings = null)

Creates a new guardrail in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to create a guardrail in.  
`guardrail` | `[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)`  
Required. The guardrail to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    Guardrail guardrail = new Guardrail();
    // Make the request
    Guardrail response = agentServiceClient.CreateGuardrail(parent, guardrail);
    

### CreateGuardrail(AppName, Guardrail, string, CallSettings)
    
    
    public virtual Guardrail CreateGuardrail(AppName parent, Guardrail guardrail, string guardrailId, CallSettings callSettings = null)

Creates a new guardrail in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to create a guardrail in.  
`guardrail` | `[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)`  
Required. The guardrail to create.  
`guardrailId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the guardrail, which will become the final component of the guardrail's resource name. If not provided, a unique ID will be automatically assigned for the guardrail.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    Guardrail guardrail = new Guardrail();
    string guardrailId = "";
    // Make the request
    Guardrail response = agentServiceClient.CreateGuardrail(parent, guardrail, guardrailId);
    

### CreateGuardrail(CreateGuardrailRequest, CallSettings)
    
    
    public virtual Guardrail CreateGuardrail(CreateGuardrailRequest request, CallSettings callSettings = null)

Creates a new guardrail in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateGuardrailRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateGuardrailRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    CreateGuardrailRequest request = new CreateGuardrailRequest
    {
        ParentAsAppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
        GuardrailId = "",
        Guardrail = new Guardrail(),
    };
    // Make the request
    Guardrail response = agentServiceClient.CreateGuardrail(request);
    

### CreateGuardrail(string, Guardrail, CallSettings)
    
    
    public virtual Guardrail CreateGuardrail(string parent, Guardrail guardrail, CallSettings callSettings = null)

Creates a new guardrail in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to create a guardrail in.  
`guardrail` | `[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)`  
Required. The guardrail to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    Guardrail guardrail = new Guardrail();
    // Make the request
    Guardrail response = agentServiceClient.CreateGuardrail(parent, guardrail);
    

### CreateGuardrail(string, Guardrail, string, CallSettings)
    
    
    public virtual Guardrail CreateGuardrail(string parent, Guardrail guardrail, string guardrailId, CallSettings callSettings = null)

Creates a new guardrail in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to create a guardrail in.  
`guardrail` | `[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)`  
Required. The guardrail to create.  
`guardrailId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the guardrail, which will become the final component of the guardrail's resource name. If not provided, a unique ID will be automatically assigned for the guardrail.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    Guardrail guardrail = new Guardrail();
    string guardrailId = "";
    // Make the request
    Guardrail response = agentServiceClient.CreateGuardrail(parent, guardrail, guardrailId);
    

### CreateGuardrailAsync(AppName, Guardrail, CallSettings)
    
    
    public virtual Task<Guardrail> CreateGuardrailAsync(AppName parent, Guardrail guardrail, CallSettings callSettings = null)

Creates a new guardrail in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to create a guardrail in.  
`guardrail` | `[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)`  
Required. The guardrail to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    Guardrail guardrail = new Guardrail();
    // Make the request
    Guardrail response = await agentServiceClient.CreateGuardrailAsync(parent, guardrail);
    

### CreateGuardrailAsync(AppName, Guardrail, string, CallSettings)
    
    
    public virtual Task<Guardrail> CreateGuardrailAsync(AppName parent, Guardrail guardrail, string guardrailId, CallSettings callSettings = null)

Creates a new guardrail in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to create a guardrail in.  
`guardrail` | `[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)`  
Required. The guardrail to create.  
`guardrailId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the guardrail, which will become the final component of the guardrail's resource name. If not provided, a unique ID will be automatically assigned for the guardrail.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    Guardrail guardrail = new Guardrail();
    string guardrailId = "";
    // Make the request
    Guardrail response = await agentServiceClient.CreateGuardrailAsync(parent, guardrail, guardrailId);
    

### CreateGuardrailAsync(AppName, Guardrail, string, CancellationToken)
    
    
    public virtual Task<Guardrail> CreateGuardrailAsync(AppName parent, Guardrail guardrail, string guardrailId, CancellationToken cancellationToken)

Creates a new guardrail in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to create a guardrail in.  
`guardrail` | `[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)`  
Required. The guardrail to create.  
`guardrailId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the guardrail, which will become the final component of the guardrail's resource name. If not provided, a unique ID will be automatically assigned for the guardrail.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    Guardrail guardrail = new Guardrail();
    string guardrailId = "";
    // Make the request
    Guardrail response = await agentServiceClient.CreateGuardrailAsync(parent, guardrail, guardrailId);
    

### CreateGuardrailAsync(AppName, Guardrail, CancellationToken)
    
    
    public virtual Task<Guardrail> CreateGuardrailAsync(AppName parent, Guardrail guardrail, CancellationToken cancellationToken)

Creates a new guardrail in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to create a guardrail in.  
`guardrail` | `[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)`  
Required. The guardrail to create.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    Guardrail guardrail = new Guardrail();
    // Make the request
    Guardrail response = await agentServiceClient.CreateGuardrailAsync(parent, guardrail);
    

### CreateGuardrailAsync(CreateGuardrailRequest, CallSettings)
    
    
    public virtual Task<Guardrail> CreateGuardrailAsync(CreateGuardrailRequest request, CallSettings callSettings = null)

Creates a new guardrail in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateGuardrailRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateGuardrailRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateGuardrailRequest request = new CreateGuardrailRequest
    {
        ParentAsAppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
        GuardrailId = "",
        Guardrail = new Guardrail(),
    };
    // Make the request
    Guardrail response = await agentServiceClient.CreateGuardrailAsync(request);
    

### CreateGuardrailAsync(CreateGuardrailRequest, CancellationToken)
    
    
    public virtual Task<Guardrail> CreateGuardrailAsync(CreateGuardrailRequest request, CancellationToken cancellationToken)

Creates a new guardrail in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateGuardrailRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateGuardrailRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateGuardrailRequest request = new CreateGuardrailRequest
    {
        ParentAsAppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
        GuardrailId = "",
        Guardrail = new Guardrail(),
    };
    // Make the request
    Guardrail response = await agentServiceClient.CreateGuardrailAsync(request);
    

### CreateGuardrailAsync(string, Guardrail, CallSettings)
    
    
    public virtual Task<Guardrail> CreateGuardrailAsync(string parent, Guardrail guardrail, CallSettings callSettings = null)

Creates a new guardrail in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to create a guardrail in.  
`guardrail` | `[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)`  
Required. The guardrail to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    Guardrail guardrail = new Guardrail();
    // Make the request
    Guardrail response = await agentServiceClient.CreateGuardrailAsync(parent, guardrail);
    

### CreateGuardrailAsync(string, Guardrail, string, CallSettings)
    
    
    public virtual Task<Guardrail> CreateGuardrailAsync(string parent, Guardrail guardrail, string guardrailId, CallSettings callSettings = null)

Creates a new guardrail in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to create a guardrail in.  
`guardrail` | `[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)`  
Required. The guardrail to create.  
`guardrailId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the guardrail, which will become the final component of the guardrail's resource name. If not provided, a unique ID will be automatically assigned for the guardrail.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    Guardrail guardrail = new Guardrail();
    string guardrailId = "";
    // Make the request
    Guardrail response = await agentServiceClient.CreateGuardrailAsync(parent, guardrail, guardrailId);
    

### CreateGuardrailAsync(string, Guardrail, string, CancellationToken)
    
    
    public virtual Task<Guardrail> CreateGuardrailAsync(string parent, Guardrail guardrail, string guardrailId, CancellationToken cancellationToken)

Creates a new guardrail in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to create a guardrail in.  
`guardrail` | `[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)`  
Required. The guardrail to create.  
`guardrailId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the guardrail, which will become the final component of the guardrail's resource name. If not provided, a unique ID will be automatically assigned for the guardrail.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    Guardrail guardrail = new Guardrail();
    string guardrailId = "";
    // Make the request
    Guardrail response = await agentServiceClient.CreateGuardrailAsync(parent, guardrail, guardrailId);
    

### CreateGuardrailAsync(string, Guardrail, CancellationToken)
    
    
    public virtual Task<Guardrail> CreateGuardrailAsync(string parent, Guardrail guardrail, CancellationToken cancellationToken)

Creates a new guardrail in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to create a guardrail in.  
`guardrail` | `[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)`  
Required. The guardrail to create.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    Guardrail guardrail = new Guardrail();
    // Make the request
    Guardrail response = await agentServiceClient.CreateGuardrailAsync(parent, guardrail);
    

### CreateTool(AppName, Tool, CallSettings)
    
    
    public virtual Tool CreateTool(AppName parent, Tool tool, CallSettings callSettings = null)

Creates a new tool in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to create a tool in.  
`tool` | `[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)`  
Required. The tool to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    Tool tool = new Tool();
    // Make the request
    Tool response = agentServiceClient.CreateTool(parent, tool);
    

### CreateTool(AppName, Tool, string, CallSettings)
    
    
    public virtual Tool CreateTool(AppName parent, Tool tool, string toolId, CallSettings callSettings = null)

Creates a new tool in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to create a tool in.  
`tool` | `[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)`  
Required. The tool to create.  
`toolId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the tool, which will become the final component of the tool's resource name. If not provided, a unique ID will be automatically assigned for the tool.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    Tool tool = new Tool();
    string toolId = "";
    // Make the request
    Tool response = agentServiceClient.CreateTool(parent, tool, toolId);
    

### CreateTool(CreateToolRequest, CallSettings)
    
    
    public virtual Tool CreateTool(CreateToolRequest request, CallSettings callSettings = null)

Creates a new tool in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateToolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateToolRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    CreateToolRequest request = new CreateToolRequest
    {
        ParentAsAppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
        ToolId = "",
        Tool = new Tool(),
    };
    // Make the request
    Tool response = agentServiceClient.CreateTool(request);
    

### CreateTool(string, Tool, CallSettings)
    
    
    public virtual Tool CreateTool(string parent, Tool tool, CallSettings callSettings = null)

Creates a new tool in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to create a tool in.  
`tool` | `[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)`  
Required. The tool to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    Tool tool = new Tool();
    // Make the request
    Tool response = agentServiceClient.CreateTool(parent, tool);
    

### CreateTool(string, Tool, string, CallSettings)
    
    
    public virtual Tool CreateTool(string parent, Tool tool, string toolId, CallSettings callSettings = null)

Creates a new tool in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to create a tool in.  
`tool` | `[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)`  
Required. The tool to create.  
`toolId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the tool, which will become the final component of the tool's resource name. If not provided, a unique ID will be automatically assigned for the tool.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    Tool tool = new Tool();
    string toolId = "";
    // Make the request
    Tool response = agentServiceClient.CreateTool(parent, tool, toolId);
    

### CreateToolAsync(AppName, Tool, CallSettings)
    
    
    public virtual Task<Tool> CreateToolAsync(AppName parent, Tool tool, CallSettings callSettings = null)

Creates a new tool in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to create a tool in.  
`tool` | `[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)`  
Required. The tool to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    Tool tool = new Tool();
    // Make the request
    Tool response = await agentServiceClient.CreateToolAsync(parent, tool);
    

### CreateToolAsync(AppName, Tool, string, CallSettings)
    
    
    public virtual Task<Tool> CreateToolAsync(AppName parent, Tool tool, string toolId, CallSettings callSettings = null)

Creates a new tool in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to create a tool in.  
`tool` | `[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)`  
Required. The tool to create.  
`toolId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the tool, which will become the final component of the tool's resource name. If not provided, a unique ID will be automatically assigned for the tool.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    Tool tool = new Tool();
    string toolId = "";
    // Make the request
    Tool response = await agentServiceClient.CreateToolAsync(parent, tool, toolId);
    

### CreateToolAsync(AppName, Tool, string, CancellationToken)
    
    
    public virtual Task<Tool> CreateToolAsync(AppName parent, Tool tool, string toolId, CancellationToken cancellationToken)

Creates a new tool in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to create a tool in.  
`tool` | `[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)`  
Required. The tool to create.  
`toolId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the tool, which will become the final component of the tool's resource name. If not provided, a unique ID will be automatically assigned for the tool.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    Tool tool = new Tool();
    string toolId = "";
    // Make the request
    Tool response = await agentServiceClient.CreateToolAsync(parent, tool, toolId);
    

### CreateToolAsync(AppName, Tool, CancellationToken)
    
    
    public virtual Task<Tool> CreateToolAsync(AppName parent, Tool tool, CancellationToken cancellationToken)

Creates a new tool in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to create a tool in.  
`tool` | `[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)`  
Required. The tool to create.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    Tool tool = new Tool();
    // Make the request
    Tool response = await agentServiceClient.CreateToolAsync(parent, tool);
    

### CreateToolAsync(CreateToolRequest, CallSettings)
    
    
    public virtual Task<Tool> CreateToolAsync(CreateToolRequest request, CallSettings callSettings = null)

Creates a new tool in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateToolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateToolRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateToolRequest request = new CreateToolRequest
    {
        ParentAsAppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
        ToolId = "",
        Tool = new Tool(),
    };
    // Make the request
    Tool response = await agentServiceClient.CreateToolAsync(request);
    

### CreateToolAsync(CreateToolRequest, CancellationToken)
    
    
    public virtual Task<Tool> CreateToolAsync(CreateToolRequest request, CancellationToken cancellationToken)

Creates a new tool in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateToolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateToolRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateToolRequest request = new CreateToolRequest
    {
        ParentAsAppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
        ToolId = "",
        Tool = new Tool(),
    };
    // Make the request
    Tool response = await agentServiceClient.CreateToolAsync(request);
    

### CreateToolAsync(string, Tool, CallSettings)
    
    
    public virtual Task<Tool> CreateToolAsync(string parent, Tool tool, CallSettings callSettings = null)

Creates a new tool in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to create a tool in.  
`tool` | `[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)`  
Required. The tool to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    Tool tool = new Tool();
    // Make the request
    Tool response = await agentServiceClient.CreateToolAsync(parent, tool);
    

### CreateToolAsync(string, Tool, string, CallSettings)
    
    
    public virtual Task<Tool> CreateToolAsync(string parent, Tool tool, string toolId, CallSettings callSettings = null)

Creates a new tool in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to create a tool in.  
`tool` | `[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)`  
Required. The tool to create.  
`toolId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the tool, which will become the final component of the tool's resource name. If not provided, a unique ID will be automatically assigned for the tool.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    Tool tool = new Tool();
    string toolId = "";
    // Make the request
    Tool response = await agentServiceClient.CreateToolAsync(parent, tool, toolId);
    

### CreateToolAsync(string, Tool, string, CancellationToken)
    
    
    public virtual Task<Tool> CreateToolAsync(string parent, Tool tool, string toolId, CancellationToken cancellationToken)

Creates a new tool in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to create a tool in.  
`tool` | `[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)`  
Required. The tool to create.  
`toolId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the tool, which will become the final component of the tool's resource name. If not provided, a unique ID will be automatically assigned for the tool.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    Tool tool = new Tool();
    string toolId = "";
    // Make the request
    Tool response = await agentServiceClient.CreateToolAsync(parent, tool, toolId);
    

### CreateToolAsync(string, Tool, CancellationToken)
    
    
    public virtual Task<Tool> CreateToolAsync(string parent, Tool tool, CancellationToken cancellationToken)

Creates a new tool in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to create a tool in.  
`tool` | `[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)`  
Required. The tool to create.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    Tool tool = new Tool();
    // Make the request
    Tool response = await agentServiceClient.CreateToolAsync(parent, tool);
    

### CreateToolset(AppName, Toolset, CallSettings)
    
    
    public virtual Toolset CreateToolset(AppName parent, Toolset toolset, CallSettings callSettings = null)

Creates a new toolset in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to create a toolset in.  
`toolset` | `[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)`  
Required. The toolset to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    Toolset toolset = new Toolset();
    // Make the request
    Toolset response = agentServiceClient.CreateToolset(parent, toolset);
    

### CreateToolset(AppName, Toolset, string, CallSettings)
    
    
    public virtual Toolset CreateToolset(AppName parent, Toolset toolset, string toolsetId, CallSettings callSettings = null)

Creates a new toolset in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to create a toolset in.  
`toolset` | `[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)`  
Required. The toolset to create.  
`toolsetId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the toolset, which will become the final component of the toolset's resource name. If not provided, a unique ID will be automatically assigned for the toolset.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    Toolset toolset = new Toolset();
    string toolsetId = "";
    // Make the request
    Toolset response = agentServiceClient.CreateToolset(parent, toolset, toolsetId);
    

### CreateToolset(CreateToolsetRequest, CallSettings)
    
    
    public virtual Toolset CreateToolset(CreateToolsetRequest request, CallSettings callSettings = null)

Creates a new toolset in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateToolsetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateToolsetRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    CreateToolsetRequest request = new CreateToolsetRequest
    {
        ParentAsAppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
        ToolsetId = "",
        Toolset = new Toolset(),
    };
    // Make the request
    Toolset response = agentServiceClient.CreateToolset(request);
    

### CreateToolset(string, Toolset, CallSettings)
    
    
    public virtual Toolset CreateToolset(string parent, Toolset toolset, CallSettings callSettings = null)

Creates a new toolset in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to create a toolset in.  
`toolset` | `[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)`  
Required. The toolset to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    Toolset toolset = new Toolset();
    // Make the request
    Toolset response = agentServiceClient.CreateToolset(parent, toolset);
    

### CreateToolset(string, Toolset, string, CallSettings)
    
    
    public virtual Toolset CreateToolset(string parent, Toolset toolset, string toolsetId, CallSettings callSettings = null)

Creates a new toolset in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to create a toolset in.  
`toolset` | `[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)`  
Required. The toolset to create.  
`toolsetId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the toolset, which will become the final component of the toolset's resource name. If not provided, a unique ID will be automatically assigned for the toolset.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    Toolset toolset = new Toolset();
    string toolsetId = "";
    // Make the request
    Toolset response = agentServiceClient.CreateToolset(parent, toolset, toolsetId);
    

### CreateToolsetAsync(AppName, Toolset, CallSettings)
    
    
    public virtual Task<Toolset> CreateToolsetAsync(AppName parent, Toolset toolset, CallSettings callSettings = null)

Creates a new toolset in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to create a toolset in.  
`toolset` | `[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)`  
Required. The toolset to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    Toolset toolset = new Toolset();
    // Make the request
    Toolset response = await agentServiceClient.CreateToolsetAsync(parent, toolset);
    

### CreateToolsetAsync(AppName, Toolset, string, CallSettings)
    
    
    public virtual Task<Toolset> CreateToolsetAsync(AppName parent, Toolset toolset, string toolsetId, CallSettings callSettings = null)

Creates a new toolset in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to create a toolset in.  
`toolset` | `[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)`  
Required. The toolset to create.  
`toolsetId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the toolset, which will become the final component of the toolset's resource name. If not provided, a unique ID will be automatically assigned for the toolset.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    Toolset toolset = new Toolset();
    string toolsetId = "";
    // Make the request
    Toolset response = await agentServiceClient.CreateToolsetAsync(parent, toolset, toolsetId);
    

### CreateToolsetAsync(AppName, Toolset, string, CancellationToken)
    
    
    public virtual Task<Toolset> CreateToolsetAsync(AppName parent, Toolset toolset, string toolsetId, CancellationToken cancellationToken)

Creates a new toolset in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to create a toolset in.  
`toolset` | `[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)`  
Required. The toolset to create.  
`toolsetId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the toolset, which will become the final component of the toolset's resource name. If not provided, a unique ID will be automatically assigned for the toolset.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    Toolset toolset = new Toolset();
    string toolsetId = "";
    // Make the request
    Toolset response = await agentServiceClient.CreateToolsetAsync(parent, toolset, toolsetId);
    

### CreateToolsetAsync(AppName, Toolset, CancellationToken)
    
    
    public virtual Task<Toolset> CreateToolsetAsync(AppName parent, Toolset toolset, CancellationToken cancellationToken)

Creates a new toolset in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to create a toolset in.  
`toolset` | `[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)`  
Required. The toolset to create.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    Toolset toolset = new Toolset();
    // Make the request
    Toolset response = await agentServiceClient.CreateToolsetAsync(parent, toolset);
    

### CreateToolsetAsync(CreateToolsetRequest, CallSettings)
    
    
    public virtual Task<Toolset> CreateToolsetAsync(CreateToolsetRequest request, CallSettings callSettings = null)

Creates a new toolset in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateToolsetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateToolsetRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateToolsetRequest request = new CreateToolsetRequest
    {
        ParentAsAppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
        ToolsetId = "",
        Toolset = new Toolset(),
    };
    // Make the request
    Toolset response = await agentServiceClient.CreateToolsetAsync(request);
    

### CreateToolsetAsync(CreateToolsetRequest, CancellationToken)
    
    
    public virtual Task<Toolset> CreateToolsetAsync(CreateToolsetRequest request, CancellationToken cancellationToken)

Creates a new toolset in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateToolsetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateToolsetRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateToolsetRequest request = new CreateToolsetRequest
    {
        ParentAsAppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
        ToolsetId = "",
        Toolset = new Toolset(),
    };
    // Make the request
    Toolset response = await agentServiceClient.CreateToolsetAsync(request);
    

### CreateToolsetAsync(string, Toolset, CallSettings)
    
    
    public virtual Task<Toolset> CreateToolsetAsync(string parent, Toolset toolset, CallSettings callSettings = null)

Creates a new toolset in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to create a toolset in.  
`toolset` | `[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)`  
Required. The toolset to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    Toolset toolset = new Toolset();
    // Make the request
    Toolset response = await agentServiceClient.CreateToolsetAsync(parent, toolset);
    

### CreateToolsetAsync(string, Toolset, string, CallSettings)
    
    
    public virtual Task<Toolset> CreateToolsetAsync(string parent, Toolset toolset, string toolsetId, CallSettings callSettings = null)

Creates a new toolset in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to create a toolset in.  
`toolset` | `[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)`  
Required. The toolset to create.  
`toolsetId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the toolset, which will become the final component of the toolset's resource name. If not provided, a unique ID will be automatically assigned for the toolset.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    Toolset toolset = new Toolset();
    string toolsetId = "";
    // Make the request
    Toolset response = await agentServiceClient.CreateToolsetAsync(parent, toolset, toolsetId);
    

### CreateToolsetAsync(string, Toolset, string, CancellationToken)
    
    
    public virtual Task<Toolset> CreateToolsetAsync(string parent, Toolset toolset, string toolsetId, CancellationToken cancellationToken)

Creates a new toolset in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to create a toolset in.  
`toolset` | `[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)`  
Required. The toolset to create.  
`toolsetId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the toolset, which will become the final component of the toolset's resource name. If not provided, a unique ID will be automatically assigned for the toolset.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    Toolset toolset = new Toolset();
    string toolsetId = "";
    // Make the request
    Toolset response = await agentServiceClient.CreateToolsetAsync(parent, toolset, toolsetId);
    

### CreateToolsetAsync(string, Toolset, CancellationToken)
    
    
    public virtual Task<Toolset> CreateToolsetAsync(string parent, Toolset toolset, CancellationToken cancellationToken)

Creates a new toolset in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to create a toolset in.  
`toolset` | `[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)`  
Required. The toolset to create.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    Toolset toolset = new Toolset();
    // Make the request
    Toolset response = await agentServiceClient.CreateToolsetAsync(parent, toolset);
    

### DeleteAgent(AgentName, CallSettings)
    
    
    public virtual void DeleteAgent(AgentName name, CallSettings callSettings = null)

Deletes the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AgentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentName)`  
Required. The resource name of the agent to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    AgentName name = AgentName.FromProjectLocationAppAgent("[PROJECT]", "[LOCATION]", "[APP]", "[AGENT]");
    // Make the request
    agentServiceClient.DeleteAgent(name);
    

### DeleteAgent(DeleteAgentRequest, CallSettings)
    
    
    public virtual void DeleteAgent(DeleteAgentRequest request, CallSettings callSettings = null)

Deletes the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteAgentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    DeleteAgentRequest request = new DeleteAgentRequest
    {
        AgentName = AgentName.FromProjectLocationAppAgent("[PROJECT]", "[LOCATION]", "[APP]", "[AGENT]"),
        Force = false,
        Etag = "",
    };
    // Make the request
    agentServiceClient.DeleteAgent(request);
    

### DeleteAgent(string, CallSettings)
    
    
    public virtual void DeleteAgent(string name, CallSettings callSettings = null)

Deletes the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the agent to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/agents/[AGENT]";
    // Make the request
    agentServiceClient.DeleteAgent(name);
    

### DeleteAgentAsync(AgentName, CallSettings)
    
    
    public virtual Task DeleteAgentAsync(AgentName name, CallSettings callSettings = null)

Deletes the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AgentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentName)`  
Required. The resource name of the agent to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AgentName name = AgentName.FromProjectLocationAppAgent("[PROJECT]", "[LOCATION]", "[APP]", "[AGENT]");
    // Make the request
    await agentServiceClient.DeleteAgentAsync(name);
    

### DeleteAgentAsync(AgentName, CancellationToken)
    
    
    public virtual Task DeleteAgentAsync(AgentName name, CancellationToken cancellationToken)

Deletes the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AgentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentName)`  
Required. The resource name of the agent to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AgentName name = AgentName.FromProjectLocationAppAgent("[PROJECT]", "[LOCATION]", "[APP]", "[AGENT]");
    // Make the request
    await agentServiceClient.DeleteAgentAsync(name);
    

### DeleteAgentAsync(DeleteAgentRequest, CallSettings)
    
    
    public virtual Task DeleteAgentAsync(DeleteAgentRequest request, CallSettings callSettings = null)

Deletes the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteAgentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteAgentRequest request = new DeleteAgentRequest
    {
        AgentName = AgentName.FromProjectLocationAppAgent("[PROJECT]", "[LOCATION]", "[APP]", "[AGENT]"),
        Force = false,
        Etag = "",
    };
    // Make the request
    await agentServiceClient.DeleteAgentAsync(request);
    

### DeleteAgentAsync(DeleteAgentRequest, CancellationToken)
    
    
    public virtual Task DeleteAgentAsync(DeleteAgentRequest request, CancellationToken cancellationToken)

Deletes the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteAgentRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteAgentRequest request = new DeleteAgentRequest
    {
        AgentName = AgentName.FromProjectLocationAppAgent("[PROJECT]", "[LOCATION]", "[APP]", "[AGENT]"),
        Force = false,
        Etag = "",
    };
    // Make the request
    await agentServiceClient.DeleteAgentAsync(request);
    

### DeleteAgentAsync(string, CallSettings)
    
    
    public virtual Task DeleteAgentAsync(string name, CallSettings callSettings = null)

Deletes the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the agent to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/agents/[AGENT]";
    // Make the request
    await agentServiceClient.DeleteAgentAsync(name);
    

### DeleteAgentAsync(string, CancellationToken)
    
    
    public virtual Task DeleteAgentAsync(string name, CancellationToken cancellationToken)

Deletes the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the agent to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/agents/[AGENT]";
    // Make the request
    await agentServiceClient.DeleteAgentAsync(name);
    

### DeleteApp(AppName, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteApp(AppName name, CallSettings callSettings = null)

Deletes the specified app.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    AppName name = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    // Make the request
    Operation<Empty, OperationMetadata> response = agentServiceClient.DeleteApp(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = agentServiceClient.PollOnceDeleteApp(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteApp(DeleteAppRequest, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteApp(DeleteAppRequest request, CallSettings callSettings = null)

Deletes the specified app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteAppRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    DeleteAppRequest request = new DeleteAppRequest
    {
        AppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
        Etag = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = agentServiceClient.DeleteApp(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = agentServiceClient.PollOnceDeleteApp(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteApp(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteApp(string name, CallSettings callSettings = null)

Deletes the specified app.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    // Make the request
    Operation<Empty, OperationMetadata> response = agentServiceClient.DeleteApp(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = agentServiceClient.PollOnceDeleteApp(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteAppAsync(AppName, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteAppAsync(AppName name, CallSettings callSettings = null)

Deletes the specified app.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AppName name = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await agentServiceClient.DeleteAppAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await agentServiceClient.PollOnceDeleteAppAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteAppAsync(AppName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteAppAsync(AppName name, CancellationToken cancellationToken)

Deletes the specified app.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AppName name = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await agentServiceClient.DeleteAppAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await agentServiceClient.PollOnceDeleteAppAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteAppAsync(DeleteAppRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteAppAsync(DeleteAppRequest request, CallSettings callSettings = null)

Deletes the specified app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteAppRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteAppRequest request = new DeleteAppRequest
    {
        AppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
        Etag = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await agentServiceClient.DeleteAppAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await agentServiceClient.PollOnceDeleteAppAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteAppAsync(DeleteAppRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteAppAsync(DeleteAppRequest request, CancellationToken cancellationToken)

Deletes the specified app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteAppRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteAppRequest request = new DeleteAppRequest
    {
        AppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
        Etag = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await agentServiceClient.DeleteAppAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await agentServiceClient.PollOnceDeleteAppAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteAppAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteAppAsync(string name, CallSettings callSettings = null)

Deletes the specified app.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await agentServiceClient.DeleteAppAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await agentServiceClient.PollOnceDeleteAppAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteAppAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteAppAsync(string name, CancellationToken cancellationToken)

Deletes the specified app.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await agentServiceClient.DeleteAppAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await agentServiceClient.PollOnceDeleteAppAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteAppVersion(AppVersionName, CallSettings)
    
    
    public virtual void DeleteAppVersion(AppVersionName name, CallSettings callSettings = null)

Deletes the specified app version.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AppVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersionName)`  
Required. The resource name of the app version to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    AppVersionName name = AppVersionName.FromProjectLocationAppVersion("[PROJECT]", "[LOCATION]", "[APP]", "[VERSION]");
    // Make the request
    agentServiceClient.DeleteAppVersion(name);
    

### DeleteAppVersion(DeleteAppVersionRequest, CallSettings)
    
    
    public virtual void DeleteAppVersion(DeleteAppVersionRequest request, CallSettings callSettings = null)

Deletes the specified app version.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAppVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteAppVersionRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    DeleteAppVersionRequest request = new DeleteAppVersionRequest
    {
        AppVersionName = AppVersionName.FromProjectLocationAppVersion("[PROJECT]", "[LOCATION]", "[APP]", "[VERSION]"),
        Etag = "",
    };
    // Make the request
    agentServiceClient.DeleteAppVersion(request);
    

### DeleteAppVersion(string, CallSettings)
    
    
    public virtual void DeleteAppVersion(string name, CallSettings callSettings = null)

Deletes the specified app version.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app version to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/versions/[VERSION]";
    // Make the request
    agentServiceClient.DeleteAppVersion(name);
    

### DeleteAppVersionAsync(AppVersionName, CallSettings)
    
    
    public virtual Task DeleteAppVersionAsync(AppVersionName name, CallSettings callSettings = null)

Deletes the specified app version.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AppVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersionName)`  
Required. The resource name of the app version to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AppVersionName name = AppVersionName.FromProjectLocationAppVersion("[PROJECT]", "[LOCATION]", "[APP]", "[VERSION]");
    // Make the request
    await agentServiceClient.DeleteAppVersionAsync(name);
    

### DeleteAppVersionAsync(AppVersionName, CancellationToken)
    
    
    public virtual Task DeleteAppVersionAsync(AppVersionName name, CancellationToken cancellationToken)

Deletes the specified app version.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AppVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersionName)`  
Required. The resource name of the app version to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AppVersionName name = AppVersionName.FromProjectLocationAppVersion("[PROJECT]", "[LOCATION]", "[APP]", "[VERSION]");
    // Make the request
    await agentServiceClient.DeleteAppVersionAsync(name);
    

### DeleteAppVersionAsync(DeleteAppVersionRequest, CallSettings)
    
    
    public virtual Task DeleteAppVersionAsync(DeleteAppVersionRequest request, CallSettings callSettings = null)

Deletes the specified app version.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAppVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteAppVersionRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteAppVersionRequest request = new DeleteAppVersionRequest
    {
        AppVersionName = AppVersionName.FromProjectLocationAppVersion("[PROJECT]", "[LOCATION]", "[APP]", "[VERSION]"),
        Etag = "",
    };
    // Make the request
    await agentServiceClient.DeleteAppVersionAsync(request);
    

### DeleteAppVersionAsync(DeleteAppVersionRequest, CancellationToken)
    
    
    public virtual Task DeleteAppVersionAsync(DeleteAppVersionRequest request, CancellationToken cancellationToken)

Deletes the specified app version.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAppVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteAppVersionRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteAppVersionRequest request = new DeleteAppVersionRequest
    {
        AppVersionName = AppVersionName.FromProjectLocationAppVersion("[PROJECT]", "[LOCATION]", "[APP]", "[VERSION]"),
        Etag = "",
    };
    // Make the request
    await agentServiceClient.DeleteAppVersionAsync(request);
    

### DeleteAppVersionAsync(string, CallSettings)
    
    
    public virtual Task DeleteAppVersionAsync(string name, CallSettings callSettings = null)

Deletes the specified app version.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app version to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/versions/[VERSION]";
    // Make the request
    await agentServiceClient.DeleteAppVersionAsync(name);
    

### DeleteAppVersionAsync(string, CancellationToken)
    
    
    public virtual Task DeleteAppVersionAsync(string name, CancellationToken cancellationToken)

Deletes the specified app version.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app version to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/versions/[VERSION]";
    // Make the request
    await agentServiceClient.DeleteAppVersionAsync(name);
    

### DeleteConversation(ConversationName, CallSettings)
    
    
    public virtual void DeleteConversation(ConversationName name, CallSettings callSettings = null)

Deletes the specified conversation.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ConversationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ConversationName)`  
Required. The resource name of the conversation to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    ConversationName name = ConversationName.FromProjectLocationAppConversation("[PROJECT]", "[LOCATION]", "[APP]", "[CONVERSATION]");
    // Make the request
    agentServiceClient.DeleteConversation(name);
    

### DeleteConversation(DeleteConversationRequest, CallSettings)
    
    
    public virtual void DeleteConversation(DeleteConversationRequest request, CallSettings callSettings = null)

Deletes the specified conversation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteConversationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteConversationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    DeleteConversationRequest request = new DeleteConversationRequest
    {
        ConversationName = ConversationName.FromProjectLocationAppConversation("[PROJECT]", "[LOCATION]", "[APP]", "[CONVERSATION]"),
    };
    // Make the request
    agentServiceClient.DeleteConversation(request);
    

### DeleteConversation(string, CallSettings)
    
    
    public virtual void DeleteConversation(string name, CallSettings callSettings = null)

Deletes the specified conversation.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the conversation to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/conversations/[CONVERSATION]";
    // Make the request
    agentServiceClient.DeleteConversation(name);
    

### DeleteConversationAsync(ConversationName, CallSettings)
    
    
    public virtual Task DeleteConversationAsync(ConversationName name, CallSettings callSettings = null)

Deletes the specified conversation.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ConversationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ConversationName)`  
Required. The resource name of the conversation to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    ConversationName name = ConversationName.FromProjectLocationAppConversation("[PROJECT]", "[LOCATION]", "[APP]", "[CONVERSATION]");
    // Make the request
    await agentServiceClient.DeleteConversationAsync(name);
    

### DeleteConversationAsync(ConversationName, CancellationToken)
    
    
    public virtual Task DeleteConversationAsync(ConversationName name, CancellationToken cancellationToken)

Deletes the specified conversation.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ConversationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ConversationName)`  
Required. The resource name of the conversation to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    ConversationName name = ConversationName.FromProjectLocationAppConversation("[PROJECT]", "[LOCATION]", "[APP]", "[CONVERSATION]");
    // Make the request
    await agentServiceClient.DeleteConversationAsync(name);
    

### DeleteConversationAsync(DeleteConversationRequest, CallSettings)
    
    
    public virtual Task DeleteConversationAsync(DeleteConversationRequest request, CallSettings callSettings = null)

Deletes the specified conversation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteConversationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteConversationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteConversationRequest request = new DeleteConversationRequest
    {
        ConversationName = ConversationName.FromProjectLocationAppConversation("[PROJECT]", "[LOCATION]", "[APP]", "[CONVERSATION]"),
    };
    // Make the request
    await agentServiceClient.DeleteConversationAsync(request);
    

### DeleteConversationAsync(DeleteConversationRequest, CancellationToken)
    
    
    public virtual Task DeleteConversationAsync(DeleteConversationRequest request, CancellationToken cancellationToken)

Deletes the specified conversation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteConversationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteConversationRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteConversationRequest request = new DeleteConversationRequest
    {
        ConversationName = ConversationName.FromProjectLocationAppConversation("[PROJECT]", "[LOCATION]", "[APP]", "[CONVERSATION]"),
    };
    // Make the request
    await agentServiceClient.DeleteConversationAsync(request);
    

### DeleteConversationAsync(string, CallSettings)
    
    
    public virtual Task DeleteConversationAsync(string name, CallSettings callSettings = null)

Deletes the specified conversation.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the conversation to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/conversations/[CONVERSATION]";
    // Make the request
    await agentServiceClient.DeleteConversationAsync(name);
    

### DeleteConversationAsync(string, CancellationToken)
    
    
    public virtual Task DeleteConversationAsync(string name, CancellationToken cancellationToken)

Deletes the specified conversation.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the conversation to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/conversations/[CONVERSATION]";
    // Make the request
    await agentServiceClient.DeleteConversationAsync(name);
    

### DeleteDeployment(DeleteDeploymentRequest, CallSettings)
    
    
    public virtual void DeleteDeployment(DeleteDeploymentRequest request, CallSettings callSettings = null)

Deletes the specified deployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteDeploymentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    DeleteDeploymentRequest request = new DeleteDeploymentRequest
    {
        DeploymentName = DeploymentName.FromProjectLocationAppDeployment("[PROJECT]", "[LOCATION]", "[APP]", "[DEPLOYMENT]"),
        Etag = "",
    };
    // Make the request
    agentServiceClient.DeleteDeployment(request);
    

### DeleteDeployment(DeploymentName, CallSettings)
    
    
    public virtual void DeleteDeployment(DeploymentName name, CallSettings callSettings = null)

Deletes the specified deployment.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DeploymentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeploymentName)`  
Required. The name of the deployment to delete. Format: `projects/{project}/locations/{location}/apps/{app}/deployments/{deployment}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    DeploymentName name = DeploymentName.FromProjectLocationAppDeployment("[PROJECT]", "[LOCATION]", "[APP]", "[DEPLOYMENT]");
    // Make the request
    agentServiceClient.DeleteDeployment(name);
    

### DeleteDeployment(string, CallSettings)
    
    
    public virtual void DeleteDeployment(string name, CallSettings callSettings = null)

Deletes the specified deployment.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the deployment to delete. Format: `projects/{project}/locations/{location}/apps/{app}/deployments/{deployment}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/deployments/[DEPLOYMENT]";
    // Make the request
    agentServiceClient.DeleteDeployment(name);
    

### DeleteDeploymentAsync(DeleteDeploymentRequest, CallSettings)
    
    
    public virtual Task DeleteDeploymentAsync(DeleteDeploymentRequest request, CallSettings callSettings = null)

Deletes the specified deployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteDeploymentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteDeploymentRequest request = new DeleteDeploymentRequest
    {
        DeploymentName = DeploymentName.FromProjectLocationAppDeployment("[PROJECT]", "[LOCATION]", "[APP]", "[DEPLOYMENT]"),
        Etag = "",
    };
    // Make the request
    await agentServiceClient.DeleteDeploymentAsync(request);
    

### DeleteDeploymentAsync(DeleteDeploymentRequest, CancellationToken)
    
    
    public virtual Task DeleteDeploymentAsync(DeleteDeploymentRequest request, CancellationToken cancellationToken)

Deletes the specified deployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteDeploymentRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteDeploymentRequest request = new DeleteDeploymentRequest
    {
        DeploymentName = DeploymentName.FromProjectLocationAppDeployment("[PROJECT]", "[LOCATION]", "[APP]", "[DEPLOYMENT]"),
        Etag = "",
    };
    // Make the request
    await agentServiceClient.DeleteDeploymentAsync(request);
    

### DeleteDeploymentAsync(DeploymentName, CallSettings)
    
    
    public virtual Task DeleteDeploymentAsync(DeploymentName name, CallSettings callSettings = null)

Deletes the specified deployment.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DeploymentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeploymentName)`  
Required. The name of the deployment to delete. Format: `projects/{project}/locations/{location}/apps/{app}/deployments/{deployment}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeploymentName name = DeploymentName.FromProjectLocationAppDeployment("[PROJECT]", "[LOCATION]", "[APP]", "[DEPLOYMENT]");
    // Make the request
    await agentServiceClient.DeleteDeploymentAsync(name);
    

### DeleteDeploymentAsync(DeploymentName, CancellationToken)
    
    
    public virtual Task DeleteDeploymentAsync(DeploymentName name, CancellationToken cancellationToken)

Deletes the specified deployment.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DeploymentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeploymentName)`  
Required. The name of the deployment to delete. Format: `projects/{project}/locations/{location}/apps/{app}/deployments/{deployment}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeploymentName name = DeploymentName.FromProjectLocationAppDeployment("[PROJECT]", "[LOCATION]", "[APP]", "[DEPLOYMENT]");
    // Make the request
    await agentServiceClient.DeleteDeploymentAsync(name);
    

### DeleteDeploymentAsync(string, CallSettings)
    
    
    public virtual Task DeleteDeploymentAsync(string name, CallSettings callSettings = null)

Deletes the specified deployment.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the deployment to delete. Format: `projects/{project}/locations/{location}/apps/{app}/deployments/{deployment}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/deployments/[DEPLOYMENT]";
    // Make the request
    await agentServiceClient.DeleteDeploymentAsync(name);
    

### DeleteDeploymentAsync(string, CancellationToken)
    
    
    public virtual Task DeleteDeploymentAsync(string name, CancellationToken cancellationToken)

Deletes the specified deployment.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the deployment to delete. Format: `projects/{project}/locations/{location}/apps/{app}/deployments/{deployment}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/deployments/[DEPLOYMENT]";
    // Make the request
    await agentServiceClient.DeleteDeploymentAsync(name);
    

### DeleteExample(DeleteExampleRequest, CallSettings)
    
    
    public virtual void DeleteExample(DeleteExampleRequest request, CallSettings callSettings = null)

Deletes the specified example.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteExampleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteExampleRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    DeleteExampleRequest request = new DeleteExampleRequest
    {
        ExampleName = ExampleName.FromProjectLocationAppExample("[PROJECT]", "[LOCATION]", "[APP]", "[EXAMPLE]"),
        Etag = "",
    };
    // Make the request
    agentServiceClient.DeleteExample(request);
    

### DeleteExample(ExampleName, CallSettings)
    
    
    public virtual void DeleteExample(ExampleName name, CallSettings callSettings = null)

Deletes the specified example.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ExampleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExampleName)`  
Required. The resource name of the example to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    ExampleName name = ExampleName.FromProjectLocationAppExample("[PROJECT]", "[LOCATION]", "[APP]", "[EXAMPLE]");
    // Make the request
    agentServiceClient.DeleteExample(name);
    

### DeleteExample(string, CallSettings)
    
    
    public virtual void DeleteExample(string name, CallSettings callSettings = null)

Deletes the specified example.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the example to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/examples/[EXAMPLE]";
    // Make the request
    agentServiceClient.DeleteExample(name);
    

### DeleteExampleAsync(DeleteExampleRequest, CallSettings)
    
    
    public virtual Task DeleteExampleAsync(DeleteExampleRequest request, CallSettings callSettings = null)

Deletes the specified example.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteExampleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteExampleRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteExampleRequest request = new DeleteExampleRequest
    {
        ExampleName = ExampleName.FromProjectLocationAppExample("[PROJECT]", "[LOCATION]", "[APP]", "[EXAMPLE]"),
        Etag = "",
    };
    // Make the request
    await agentServiceClient.DeleteExampleAsync(request);
    

### DeleteExampleAsync(DeleteExampleRequest, CancellationToken)
    
    
    public virtual Task DeleteExampleAsync(DeleteExampleRequest request, CancellationToken cancellationToken)

Deletes the specified example.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteExampleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteExampleRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteExampleRequest request = new DeleteExampleRequest
    {
        ExampleName = ExampleName.FromProjectLocationAppExample("[PROJECT]", "[LOCATION]", "[APP]", "[EXAMPLE]"),
        Etag = "",
    };
    // Make the request
    await agentServiceClient.DeleteExampleAsync(request);
    

### DeleteExampleAsync(ExampleName, CallSettings)
    
    
    public virtual Task DeleteExampleAsync(ExampleName name, CallSettings callSettings = null)

Deletes the specified example.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ExampleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExampleName)`  
Required. The resource name of the example to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    ExampleName name = ExampleName.FromProjectLocationAppExample("[PROJECT]", "[LOCATION]", "[APP]", "[EXAMPLE]");
    // Make the request
    await agentServiceClient.DeleteExampleAsync(name);
    

### DeleteExampleAsync(ExampleName, CancellationToken)
    
    
    public virtual Task DeleteExampleAsync(ExampleName name, CancellationToken cancellationToken)

Deletes the specified example.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ExampleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExampleName)`  
Required. The resource name of the example to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    ExampleName name = ExampleName.FromProjectLocationAppExample("[PROJECT]", "[LOCATION]", "[APP]", "[EXAMPLE]");
    // Make the request
    await agentServiceClient.DeleteExampleAsync(name);
    

### DeleteExampleAsync(string, CallSettings)
    
    
    public virtual Task DeleteExampleAsync(string name, CallSettings callSettings = null)

Deletes the specified example.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the example to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/examples/[EXAMPLE]";
    // Make the request
    await agentServiceClient.DeleteExampleAsync(name);
    

### DeleteExampleAsync(string, CancellationToken)
    
    
    public virtual Task DeleteExampleAsync(string name, CancellationToken cancellationToken)

Deletes the specified example.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the example to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/examples/[EXAMPLE]";
    // Make the request
    await agentServiceClient.DeleteExampleAsync(name);
    

### DeleteGuardrail(DeleteGuardrailRequest, CallSettings)
    
    
    public virtual void DeleteGuardrail(DeleteGuardrailRequest request, CallSettings callSettings = null)

Deletes the specified guardrail.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteGuardrailRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteGuardrailRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    DeleteGuardrailRequest request = new DeleteGuardrailRequest
    {
        GuardrailName = GuardrailName.FromProjectLocationAppGuardrail("[PROJECT]", "[LOCATION]", "[APP]", "[GUARDRAIL]"),
        Force = false,
        Etag = "",
    };
    // Make the request
    agentServiceClient.DeleteGuardrail(request);
    

### DeleteGuardrail(GuardrailName, CallSettings)
    
    
    public virtual void DeleteGuardrail(GuardrailName name, CallSettings callSettings = null)

Deletes the specified guardrail.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[GuardrailName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GuardrailName)`  
Required. The resource name of the guardrail to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    GuardrailName name = GuardrailName.FromProjectLocationAppGuardrail("[PROJECT]", "[LOCATION]", "[APP]", "[GUARDRAIL]");
    // Make the request
    agentServiceClient.DeleteGuardrail(name);
    

### DeleteGuardrail(string, CallSettings)
    
    
    public virtual void DeleteGuardrail(string name, CallSettings callSettings = null)

Deletes the specified guardrail.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the guardrail to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/guardrails/[GUARDRAIL]";
    // Make the request
    agentServiceClient.DeleteGuardrail(name);
    

### DeleteGuardrailAsync(DeleteGuardrailRequest, CallSettings)
    
    
    public virtual Task DeleteGuardrailAsync(DeleteGuardrailRequest request, CallSettings callSettings = null)

Deletes the specified guardrail.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteGuardrailRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteGuardrailRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteGuardrailRequest request = new DeleteGuardrailRequest
    {
        GuardrailName = GuardrailName.FromProjectLocationAppGuardrail("[PROJECT]", "[LOCATION]", "[APP]", "[GUARDRAIL]"),
        Force = false,
        Etag = "",
    };
    // Make the request
    await agentServiceClient.DeleteGuardrailAsync(request);
    

### DeleteGuardrailAsync(DeleteGuardrailRequest, CancellationToken)
    
    
    public virtual Task DeleteGuardrailAsync(DeleteGuardrailRequest request, CancellationToken cancellationToken)

Deletes the specified guardrail.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteGuardrailRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteGuardrailRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteGuardrailRequest request = new DeleteGuardrailRequest
    {
        GuardrailName = GuardrailName.FromProjectLocationAppGuardrail("[PROJECT]", "[LOCATION]", "[APP]", "[GUARDRAIL]"),
        Force = false,
        Etag = "",
    };
    // Make the request
    await agentServiceClient.DeleteGuardrailAsync(request);
    

### DeleteGuardrailAsync(GuardrailName, CallSettings)
    
    
    public virtual Task DeleteGuardrailAsync(GuardrailName name, CallSettings callSettings = null)

Deletes the specified guardrail.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[GuardrailName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GuardrailName)`  
Required. The resource name of the guardrail to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    GuardrailName name = GuardrailName.FromProjectLocationAppGuardrail("[PROJECT]", "[LOCATION]", "[APP]", "[GUARDRAIL]");
    // Make the request
    await agentServiceClient.DeleteGuardrailAsync(name);
    

### DeleteGuardrailAsync(GuardrailName, CancellationToken)
    
    
    public virtual Task DeleteGuardrailAsync(GuardrailName name, CancellationToken cancellationToken)

Deletes the specified guardrail.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[GuardrailName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GuardrailName)`  
Required. The resource name of the guardrail to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    GuardrailName name = GuardrailName.FromProjectLocationAppGuardrail("[PROJECT]", "[LOCATION]", "[APP]", "[GUARDRAIL]");
    // Make the request
    await agentServiceClient.DeleteGuardrailAsync(name);
    

### DeleteGuardrailAsync(string, CallSettings)
    
    
    public virtual Task DeleteGuardrailAsync(string name, CallSettings callSettings = null)

Deletes the specified guardrail.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the guardrail to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/guardrails/[GUARDRAIL]";
    // Make the request
    await agentServiceClient.DeleteGuardrailAsync(name);
    

### DeleteGuardrailAsync(string, CancellationToken)
    
    
    public virtual Task DeleteGuardrailAsync(string name, CancellationToken cancellationToken)

Deletes the specified guardrail.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the guardrail to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/guardrails/[GUARDRAIL]";
    // Make the request
    await agentServiceClient.DeleteGuardrailAsync(name);
    

### DeleteTool(DeleteToolRequest, CallSettings)
    
    
    public virtual void DeleteTool(DeleteToolRequest request, CallSettings callSettings = null)

Deletes the specified tool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteToolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteToolRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    DeleteToolRequest request = new DeleteToolRequest
    {
        ToolName = ToolName.FromProjectLocationAppTool("[PROJECT]", "[LOCATION]", "[APP]", "[TOOL]"),
        Force = false,
        Etag = "",
    };
    // Make the request
    agentServiceClient.DeleteTool(request);
    

### DeleteTool(ToolName, CallSettings)
    
    
    public virtual void DeleteTool(ToolName name, CallSettings callSettings = null)

Deletes the specified tool.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ToolName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ToolName)`  
Required. The resource name of the tool to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    ToolName name = ToolName.FromProjectLocationAppTool("[PROJECT]", "[LOCATION]", "[APP]", "[TOOL]");
    // Make the request
    agentServiceClient.DeleteTool(name);
    

### DeleteTool(string, CallSettings)
    
    
    public virtual void DeleteTool(string name, CallSettings callSettings = null)

Deletes the specified tool.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the tool to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/tools/[TOOL]";
    // Make the request
    agentServiceClient.DeleteTool(name);
    

### DeleteToolAsync(DeleteToolRequest, CallSettings)
    
    
    public virtual Task DeleteToolAsync(DeleteToolRequest request, CallSettings callSettings = null)

Deletes the specified tool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteToolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteToolRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteToolRequest request = new DeleteToolRequest
    {
        ToolName = ToolName.FromProjectLocationAppTool("[PROJECT]", "[LOCATION]", "[APP]", "[TOOL]"),
        Force = false,
        Etag = "",
    };
    // Make the request
    await agentServiceClient.DeleteToolAsync(request);
    

### DeleteToolAsync(DeleteToolRequest, CancellationToken)
    
    
    public virtual Task DeleteToolAsync(DeleteToolRequest request, CancellationToken cancellationToken)

Deletes the specified tool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteToolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteToolRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteToolRequest request = new DeleteToolRequest
    {
        ToolName = ToolName.FromProjectLocationAppTool("[PROJECT]", "[LOCATION]", "[APP]", "[TOOL]"),
        Force = false,
        Etag = "",
    };
    // Make the request
    await agentServiceClient.DeleteToolAsync(request);
    

### DeleteToolAsync(ToolName, CallSettings)
    
    
    public virtual Task DeleteToolAsync(ToolName name, CallSettings callSettings = null)

Deletes the specified tool.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ToolName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ToolName)`  
Required. The resource name of the tool to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    ToolName name = ToolName.FromProjectLocationAppTool("[PROJECT]", "[LOCATION]", "[APP]", "[TOOL]");
    // Make the request
    await agentServiceClient.DeleteToolAsync(name);
    

### DeleteToolAsync(ToolName, CancellationToken)
    
    
    public virtual Task DeleteToolAsync(ToolName name, CancellationToken cancellationToken)

Deletes the specified tool.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ToolName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ToolName)`  
Required. The resource name of the tool to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    ToolName name = ToolName.FromProjectLocationAppTool("[PROJECT]", "[LOCATION]", "[APP]", "[TOOL]");
    // Make the request
    await agentServiceClient.DeleteToolAsync(name);
    

### DeleteToolAsync(string, CallSettings)
    
    
    public virtual Task DeleteToolAsync(string name, CallSettings callSettings = null)

Deletes the specified tool.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the tool to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/tools/[TOOL]";
    // Make the request
    await agentServiceClient.DeleteToolAsync(name);
    

### DeleteToolAsync(string, CancellationToken)
    
    
    public virtual Task DeleteToolAsync(string name, CancellationToken cancellationToken)

Deletes the specified tool.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the tool to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/tools/[TOOL]";
    // Make the request
    await agentServiceClient.DeleteToolAsync(name);
    

### DeleteToolset(DeleteToolsetRequest, CallSettings)
    
    
    public virtual void DeleteToolset(DeleteToolsetRequest request, CallSettings callSettings = null)

Deletes the specified toolset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteToolsetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteToolsetRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    DeleteToolsetRequest request = new DeleteToolsetRequest
    {
        ToolsetName = ToolsetName.FromProjectLocationAppToolset("[PROJECT]", "[LOCATION]", "[APP]", "[TOOLSET]"),
        Force = false,
        Etag = "",
    };
    // Make the request
    agentServiceClient.DeleteToolset(request);
    

### DeleteToolset(ToolsetName, CallSettings)
    
    
    public virtual void DeleteToolset(ToolsetName name, CallSettings callSettings = null)

Deletes the specified toolset.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ToolsetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ToolsetName)`  
Required. The resource name of the toolset to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    ToolsetName name = ToolsetName.FromProjectLocationAppToolset("[PROJECT]", "[LOCATION]", "[APP]", "[TOOLSET]");
    // Make the request
    agentServiceClient.DeleteToolset(name);
    

### DeleteToolset(string, CallSettings)
    
    
    public virtual void DeleteToolset(string name, CallSettings callSettings = null)

Deletes the specified toolset.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the toolset to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/toolsets/[TOOLSET]";
    // Make the request
    agentServiceClient.DeleteToolset(name);
    

### DeleteToolsetAsync(DeleteToolsetRequest, CallSettings)
    
    
    public virtual Task DeleteToolsetAsync(DeleteToolsetRequest request, CallSettings callSettings = null)

Deletes the specified toolset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteToolsetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteToolsetRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteToolsetRequest request = new DeleteToolsetRequest
    {
        ToolsetName = ToolsetName.FromProjectLocationAppToolset("[PROJECT]", "[LOCATION]", "[APP]", "[TOOLSET]"),
        Force = false,
        Etag = "",
    };
    // Make the request
    await agentServiceClient.DeleteToolsetAsync(request);
    

### DeleteToolsetAsync(DeleteToolsetRequest, CancellationToken)
    
    
    public virtual Task DeleteToolsetAsync(DeleteToolsetRequest request, CancellationToken cancellationToken)

Deletes the specified toolset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteToolsetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteToolsetRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteToolsetRequest request = new DeleteToolsetRequest
    {
        ToolsetName = ToolsetName.FromProjectLocationAppToolset("[PROJECT]", "[LOCATION]", "[APP]", "[TOOLSET]"),
        Force = false,
        Etag = "",
    };
    // Make the request
    await agentServiceClient.DeleteToolsetAsync(request);
    

### DeleteToolsetAsync(ToolsetName, CallSettings)
    
    
    public virtual Task DeleteToolsetAsync(ToolsetName name, CallSettings callSettings = null)

Deletes the specified toolset.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ToolsetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ToolsetName)`  
Required. The resource name of the toolset to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    ToolsetName name = ToolsetName.FromProjectLocationAppToolset("[PROJECT]", "[LOCATION]", "[APP]", "[TOOLSET]");
    // Make the request
    await agentServiceClient.DeleteToolsetAsync(name);
    

### DeleteToolsetAsync(ToolsetName, CancellationToken)
    
    
    public virtual Task DeleteToolsetAsync(ToolsetName name, CancellationToken cancellationToken)

Deletes the specified toolset.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ToolsetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ToolsetName)`  
Required. The resource name of the toolset to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    ToolsetName name = ToolsetName.FromProjectLocationAppToolset("[PROJECT]", "[LOCATION]", "[APP]", "[TOOLSET]");
    // Make the request
    await agentServiceClient.DeleteToolsetAsync(name);
    

### DeleteToolsetAsync(string, CallSettings)
    
    
    public virtual Task DeleteToolsetAsync(string name, CallSettings callSettings = null)

Deletes the specified toolset.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the toolset to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/toolsets/[TOOLSET]";
    // Make the request
    await agentServiceClient.DeleteToolsetAsync(name);
    

### DeleteToolsetAsync(string, CancellationToken)
    
    
    public virtual Task DeleteToolsetAsync(string name, CancellationToken cancellationToken)

Deletes the specified toolset.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the toolset to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/toolsets/[TOOLSET]";
    // Make the request
    await agentServiceClient.DeleteToolsetAsync(name);
    

### ExportApp(AppName, CallSettings)
    
    
    public virtual Operation<ExportAppResponse, OperationMetadata> ExportApp(AppName name, CallSettings callSettings = null)

Exports the specified app.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to export.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportAppResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExportAppResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    AppName name = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    // Make the request
    Operation<ExportAppResponse, OperationMetadata> response = agentServiceClient.ExportApp(name);
    
    // Poll until the returned long-running operation is complete
    Operation<ExportAppResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    ExportAppResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ExportAppResponse, OperationMetadata> retrievedResponse = agentServiceClient.PollOnceExportApp(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ExportAppResponse retrievedResult = retrievedResponse.Result;
    }
    

### ExportApp(ExportAppRequest, CallSettings)
    
    
    public virtual Operation<ExportAppResponse, OperationMetadata> ExportApp(ExportAppRequest request, CallSettings callSettings = null)

Exports the specified app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExportAppRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportAppResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExportAppResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    ExportAppRequest request = new ExportAppRequest
    {
        AppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
        ExportFormat = ExportAppRequest.Types.ExportFormat.Unspecified,
        GcsUri = "",
        AppVersionAsAppVersionName = AppVersionName.FromProjectLocationAppVersion("[PROJECT]", "[LOCATION]", "[APP]", "[VERSION]"),
    };
    // Make the request
    Operation<ExportAppResponse, OperationMetadata> response = agentServiceClient.ExportApp(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ExportAppResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    ExportAppResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ExportAppResponse, OperationMetadata> retrievedResponse = agentServiceClient.PollOnceExportApp(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ExportAppResponse retrievedResult = retrievedResponse.Result;
    }
    

### ExportApp(string, CallSettings)
    
    
    public virtual Operation<ExportAppResponse, OperationMetadata> ExportApp(string name, CallSettings callSettings = null)

Exports the specified app.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to export.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportAppResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExportAppResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    // Make the request
    Operation<ExportAppResponse, OperationMetadata> response = agentServiceClient.ExportApp(name);
    
    // Poll until the returned long-running operation is complete
    Operation<ExportAppResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    ExportAppResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ExportAppResponse, OperationMetadata> retrievedResponse = agentServiceClient.PollOnceExportApp(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ExportAppResponse retrievedResult = retrievedResponse.Result;
    }
    

### ExportAppAsync(AppName, CallSettings)
    
    
    public virtual Task<Operation<ExportAppResponse, OperationMetadata>> ExportAppAsync(AppName name, CallSettings callSettings = null)

Exports the specified app.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to export.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportAppResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExportAppResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AppName name = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    // Make the request
    Operation<ExportAppResponse, OperationMetadata> response = await agentServiceClient.ExportAppAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<ExportAppResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ExportAppResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ExportAppResponse, OperationMetadata> retrievedResponse = await agentServiceClient.PollOnceExportAppAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ExportAppResponse retrievedResult = retrievedResponse.Result;
    }
    

### ExportAppAsync(AppName, CancellationToken)
    
    
    public virtual Task<Operation<ExportAppResponse, OperationMetadata>> ExportAppAsync(AppName name, CancellationToken cancellationToken)

Exports the specified app.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to export.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportAppResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExportAppResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AppName name = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    // Make the request
    Operation<ExportAppResponse, OperationMetadata> response = await agentServiceClient.ExportAppAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<ExportAppResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ExportAppResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ExportAppResponse, OperationMetadata> retrievedResponse = await agentServiceClient.PollOnceExportAppAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ExportAppResponse retrievedResult = retrievedResponse.Result;
    }
    

### ExportAppAsync(ExportAppRequest, CallSettings)
    
    
    public virtual Task<Operation<ExportAppResponse, OperationMetadata>> ExportAppAsync(ExportAppRequest request, CallSettings callSettings = null)

Exports the specified app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExportAppRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportAppResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExportAppResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    ExportAppRequest request = new ExportAppRequest
    {
        AppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
        ExportFormat = ExportAppRequest.Types.ExportFormat.Unspecified,
        GcsUri = "",
        AppVersionAsAppVersionName = AppVersionName.FromProjectLocationAppVersion("[PROJECT]", "[LOCATION]", "[APP]", "[VERSION]"),
    };
    // Make the request
    Operation<ExportAppResponse, OperationMetadata> response = await agentServiceClient.ExportAppAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ExportAppResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ExportAppResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ExportAppResponse, OperationMetadata> retrievedResponse = await agentServiceClient.PollOnceExportAppAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ExportAppResponse retrievedResult = retrievedResponse.Result;
    }
    

### ExportAppAsync(ExportAppRequest, CancellationToken)
    
    
    public virtual Task<Operation<ExportAppResponse, OperationMetadata>> ExportAppAsync(ExportAppRequest request, CancellationToken cancellationToken)

Exports the specified app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExportAppRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportAppResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExportAppResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    ExportAppRequest request = new ExportAppRequest
    {
        AppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
        ExportFormat = ExportAppRequest.Types.ExportFormat.Unspecified,
        GcsUri = "",
        AppVersionAsAppVersionName = AppVersionName.FromProjectLocationAppVersion("[PROJECT]", "[LOCATION]", "[APP]", "[VERSION]"),
    };
    // Make the request
    Operation<ExportAppResponse, OperationMetadata> response = await agentServiceClient.ExportAppAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ExportAppResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ExportAppResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ExportAppResponse, OperationMetadata> retrievedResponse = await agentServiceClient.PollOnceExportAppAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ExportAppResponse retrievedResult = retrievedResponse.Result;
    }
    

### ExportAppAsync(string, CallSettings)
    
    
    public virtual Task<Operation<ExportAppResponse, OperationMetadata>> ExportAppAsync(string name, CallSettings callSettings = null)

Exports the specified app.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to export.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportAppResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExportAppResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    // Make the request
    Operation<ExportAppResponse, OperationMetadata> response = await agentServiceClient.ExportAppAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<ExportAppResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ExportAppResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ExportAppResponse, OperationMetadata> retrievedResponse = await agentServiceClient.PollOnceExportAppAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ExportAppResponse retrievedResult = retrievedResponse.Result;
    }
    

### ExportAppAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<ExportAppResponse, OperationMetadata>> ExportAppAsync(string name, CancellationToken cancellationToken)

Exports the specified app.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to export.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportAppResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExportAppResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    // Make the request
    Operation<ExportAppResponse, OperationMetadata> response = await agentServiceClient.ExportAppAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<ExportAppResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ExportAppResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ExportAppResponse, OperationMetadata> retrievedResponse = await agentServiceClient.PollOnceExportAppAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ExportAppResponse retrievedResult = retrievedResponse.Result;
    }
    

### GenerateAppResource(AppName, CallSettings)
    
    
    public virtual Operation<GenerateAppResourceResponse, GenerateAppResourceOperationMetadata> GenerateAppResource(AppName parent, CallSettings callSettings = null)

Generates specific resources (e.g. agent) in the app using LLM assistant.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to generate the resource for.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[GenerateAppResourceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceResponse)[GenerateAppResourceOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    // Make the request
    Operation<GenerateAppResourceResponse, GenerateAppResourceOperationMetadata> response = agentServiceClient.GenerateAppResource(parent);
    
    // Poll until the returned long-running operation is complete
    Operation<GenerateAppResourceResponse, GenerateAppResourceOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    GenerateAppResourceResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<GenerateAppResourceResponse, GenerateAppResourceOperationMetadata> retrievedResponse = agentServiceClient.PollOnceGenerateAppResource(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        GenerateAppResourceResponse retrievedResult = retrievedResponse.Result;
    }
    

### GenerateAppResource(GenerateAppResourceRequest, CallSettings)
    
    
    public virtual Operation<GenerateAppResourceResponse, GenerateAppResourceOperationMetadata> GenerateAppResource(GenerateAppResourceRequest request, CallSettings callSettings = null)

Generates specific resources (e.g. agent) in the app using LLM assistant.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateAppResourceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[GenerateAppResourceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceResponse)[GenerateAppResourceOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    GenerateAppResourceRequest request = new GenerateAppResourceRequest
    {
        ParentAsAppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
        Agent = new Agent(),
        RefineInstructions =
        {
            new GenerateAppResourceRequest.Types.RefineInstructions(),
        },
        ToolGenerationConfig = new GenerateAppResourceRequest.Types.ToolGenerationConfig(),
        AppGenerationConfig = new GenerateAppResourceRequest.Types.AppGenerationConfig(),
        EvaluationGenerationConfig = new GenerateAppResourceRequest.Types.EvaluationGenerationConfig(),
        EvaluationPersonasGenerationConfig = new GenerateAppResourceRequest.Types.EvaluationPersonasGenerationConfig(),
        QualityReportGenerationConfig = new GenerateAppResourceRequest.Types.QualityReportGenerationConfig(),
        HillClimbingFixConfig = new GenerateAppResourceRequest.Types.HillClimbingFixConfig(),
    };
    // Make the request
    Operation<GenerateAppResourceResponse, GenerateAppResourceOperationMetadata> response = agentServiceClient.GenerateAppResource(request);
    
    // Poll until the returned long-running operation is complete
    Operation<GenerateAppResourceResponse, GenerateAppResourceOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    GenerateAppResourceResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<GenerateAppResourceResponse, GenerateAppResourceOperationMetadata> retrievedResponse = agentServiceClient.PollOnceGenerateAppResource(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        GenerateAppResourceResponse retrievedResult = retrievedResponse.Result;
    }
    

### GenerateAppResource(string, CallSettings)
    
    
    public virtual Operation<GenerateAppResourceResponse, GenerateAppResourceOperationMetadata> GenerateAppResource(string parent, CallSettings callSettings = null)

Generates specific resources (e.g. agent) in the app using LLM assistant.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to generate the resource for.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[GenerateAppResourceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceResponse)[GenerateAppResourceOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    // Make the request
    Operation<GenerateAppResourceResponse, GenerateAppResourceOperationMetadata> response = agentServiceClient.GenerateAppResource(parent);
    
    // Poll until the returned long-running operation is complete
    Operation<GenerateAppResourceResponse, GenerateAppResourceOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    GenerateAppResourceResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<GenerateAppResourceResponse, GenerateAppResourceOperationMetadata> retrievedResponse = agentServiceClient.PollOnceGenerateAppResource(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        GenerateAppResourceResponse retrievedResult = retrievedResponse.Result;
    }
    

### GenerateAppResourceAsync(AppName, CallSettings)
    
    
    public virtual Task<Operation<GenerateAppResourceResponse, GenerateAppResourceOperationMetadata>> GenerateAppResourceAsync(AppName parent, CallSettings callSettings = null)

Generates specific resources (e.g. agent) in the app using LLM assistant.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to generate the resource for.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[GenerateAppResourceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceResponse)[GenerateAppResourceOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    // Make the request
    Operation<GenerateAppResourceResponse, GenerateAppResourceOperationMetadata> response = await agentServiceClient.GenerateAppResourceAsync(parent);
    
    // Poll until the returned long-running operation is complete
    Operation<GenerateAppResourceResponse, GenerateAppResourceOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    GenerateAppResourceResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<GenerateAppResourceResponse, GenerateAppResourceOperationMetadata> retrievedResponse = await agentServiceClient.PollOnceGenerateAppResourceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        GenerateAppResourceResponse retrievedResult = retrievedResponse.Result;
    }
    

### GenerateAppResourceAsync(AppName, CancellationToken)
    
    
    public virtual Task<Operation<GenerateAppResourceResponse, GenerateAppResourceOperationMetadata>> GenerateAppResourceAsync(AppName parent, CancellationToken cancellationToken)

Generates specific resources (e.g. agent) in the app using LLM assistant.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to generate the resource for.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[GenerateAppResourceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceResponse)[GenerateAppResourceOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    // Make the request
    Operation<GenerateAppResourceResponse, GenerateAppResourceOperationMetadata> response = await agentServiceClient.GenerateAppResourceAsync(parent);
    
    // Poll until the returned long-running operation is complete
    Operation<GenerateAppResourceResponse, GenerateAppResourceOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    GenerateAppResourceResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<GenerateAppResourceResponse, GenerateAppResourceOperationMetadata> retrievedResponse = await agentServiceClient.PollOnceGenerateAppResourceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        GenerateAppResourceResponse retrievedResult = retrievedResponse.Result;
    }
    

### GenerateAppResourceAsync(GenerateAppResourceRequest, CallSettings)
    
    
    public virtual Task<Operation<GenerateAppResourceResponse, GenerateAppResourceOperationMetadata>> GenerateAppResourceAsync(GenerateAppResourceRequest request, CallSettings callSettings = null)

Generates specific resources (e.g. agent) in the app using LLM assistant.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateAppResourceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[GenerateAppResourceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceResponse)[GenerateAppResourceOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    GenerateAppResourceRequest request = new GenerateAppResourceRequest
    {
        ParentAsAppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
        Agent = new Agent(),
        RefineInstructions =
        {
            new GenerateAppResourceRequest.Types.RefineInstructions(),
        },
        ToolGenerationConfig = new GenerateAppResourceRequest.Types.ToolGenerationConfig(),
        AppGenerationConfig = new GenerateAppResourceRequest.Types.AppGenerationConfig(),
        EvaluationGenerationConfig = new GenerateAppResourceRequest.Types.EvaluationGenerationConfig(),
        EvaluationPersonasGenerationConfig = new GenerateAppResourceRequest.Types.EvaluationPersonasGenerationConfig(),
        QualityReportGenerationConfig = new GenerateAppResourceRequest.Types.QualityReportGenerationConfig(),
        HillClimbingFixConfig = new GenerateAppResourceRequest.Types.HillClimbingFixConfig(),
    };
    // Make the request
    Operation<GenerateAppResourceResponse, GenerateAppResourceOperationMetadata> response = await agentServiceClient.GenerateAppResourceAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<GenerateAppResourceResponse, GenerateAppResourceOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    GenerateAppResourceResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<GenerateAppResourceResponse, GenerateAppResourceOperationMetadata> retrievedResponse = await agentServiceClient.PollOnceGenerateAppResourceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        GenerateAppResourceResponse retrievedResult = retrievedResponse.Result;
    }
    

### GenerateAppResourceAsync(GenerateAppResourceRequest, CancellationToken)
    
    
    public virtual Task<Operation<GenerateAppResourceResponse, GenerateAppResourceOperationMetadata>> GenerateAppResourceAsync(GenerateAppResourceRequest request, CancellationToken cancellationToken)

Generates specific resources (e.g. agent) in the app using LLM assistant.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateAppResourceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[GenerateAppResourceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceResponse)[GenerateAppResourceOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    GenerateAppResourceRequest request = new GenerateAppResourceRequest
    {
        ParentAsAppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
        Agent = new Agent(),
        RefineInstructions =
        {
            new GenerateAppResourceRequest.Types.RefineInstructions(),
        },
        ToolGenerationConfig = new GenerateAppResourceRequest.Types.ToolGenerationConfig(),
        AppGenerationConfig = new GenerateAppResourceRequest.Types.AppGenerationConfig(),
        EvaluationGenerationConfig = new GenerateAppResourceRequest.Types.EvaluationGenerationConfig(),
        EvaluationPersonasGenerationConfig = new GenerateAppResourceRequest.Types.EvaluationPersonasGenerationConfig(),
        QualityReportGenerationConfig = new GenerateAppResourceRequest.Types.QualityReportGenerationConfig(),
        HillClimbingFixConfig = new GenerateAppResourceRequest.Types.HillClimbingFixConfig(),
    };
    // Make the request
    Operation<GenerateAppResourceResponse, GenerateAppResourceOperationMetadata> response = await agentServiceClient.GenerateAppResourceAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<GenerateAppResourceResponse, GenerateAppResourceOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    GenerateAppResourceResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<GenerateAppResourceResponse, GenerateAppResourceOperationMetadata> retrievedResponse = await agentServiceClient.PollOnceGenerateAppResourceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        GenerateAppResourceResponse retrievedResult = retrievedResponse.Result;
    }
    

### GenerateAppResourceAsync(string, CallSettings)
    
    
    public virtual Task<Operation<GenerateAppResourceResponse, GenerateAppResourceOperationMetadata>> GenerateAppResourceAsync(string parent, CallSettings callSettings = null)

Generates specific resources (e.g. agent) in the app using LLM assistant.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to generate the resource for.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[GenerateAppResourceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceResponse)[GenerateAppResourceOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    // Make the request
    Operation<GenerateAppResourceResponse, GenerateAppResourceOperationMetadata> response = await agentServiceClient.GenerateAppResourceAsync(parent);
    
    // Poll until the returned long-running operation is complete
    Operation<GenerateAppResourceResponse, GenerateAppResourceOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    GenerateAppResourceResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<GenerateAppResourceResponse, GenerateAppResourceOperationMetadata> retrievedResponse = await agentServiceClient.PollOnceGenerateAppResourceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        GenerateAppResourceResponse retrievedResult = retrievedResponse.Result;
    }
    

### GenerateAppResourceAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<GenerateAppResourceResponse, GenerateAppResourceOperationMetadata>> GenerateAppResourceAsync(string parent, CancellationToken cancellationToken)

Generates specific resources (e.g. agent) in the app using LLM assistant.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to generate the resource for.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[GenerateAppResourceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceResponse)[GenerateAppResourceOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    // Make the request
    Operation<GenerateAppResourceResponse, GenerateAppResourceOperationMetadata> response = await agentServiceClient.GenerateAppResourceAsync(parent);
    
    // Poll until the returned long-running operation is complete
    Operation<GenerateAppResourceResponse, GenerateAppResourceOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    GenerateAppResourceResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<GenerateAppResourceResponse, GenerateAppResourceOperationMetadata> retrievedResponse = await agentServiceClient.PollOnceGenerateAppResourceAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        GenerateAppResourceResponse retrievedResult = retrievedResponse.Result;
    }
    

### GetAgent(AgentName, CallSettings)
    
    
    public virtual Agent GetAgent(AgentName name, CallSettings callSettings = null)

Gets details of the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AgentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentName)`  
Required. The resource name of the agent to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    AgentName name = AgentName.FromProjectLocationAppAgent("[PROJECT]", "[LOCATION]", "[APP]", "[AGENT]");
    // Make the request
    Agent response = agentServiceClient.GetAgent(name);
    

### GetAgent(GetAgentRequest, CallSettings)
    
    
    public virtual Agent GetAgent(GetAgentRequest request, CallSettings callSettings = null)

Gets details of the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetAgentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    GetAgentRequest request = new GetAgentRequest
    {
        AgentName = AgentName.FromProjectLocationAppAgent("[PROJECT]", "[LOCATION]", "[APP]", "[AGENT]"),
    };
    // Make the request
    Agent response = agentServiceClient.GetAgent(request);
    

### GetAgent(string, CallSettings)
    
    
    public virtual Agent GetAgent(string name, CallSettings callSettings = null)

Gets details of the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the agent to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/agents/[AGENT]";
    // Make the request
    Agent response = agentServiceClient.GetAgent(name);
    

### GetAgentAsync(AgentName, CallSettings)
    
    
    public virtual Task<Agent> GetAgentAsync(AgentName name, CallSettings callSettings = null)

Gets details of the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AgentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentName)`  
Required. The resource name of the agent to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AgentName name = AgentName.FromProjectLocationAppAgent("[PROJECT]", "[LOCATION]", "[APP]", "[AGENT]");
    // Make the request
    Agent response = await agentServiceClient.GetAgentAsync(name);
    

### GetAgentAsync(AgentName, CancellationToken)
    
    
    public virtual Task<Agent> GetAgentAsync(AgentName name, CancellationToken cancellationToken)

Gets details of the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AgentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentName)`  
Required. The resource name of the agent to retrieve.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AgentName name = AgentName.FromProjectLocationAppAgent("[PROJECT]", "[LOCATION]", "[APP]", "[AGENT]");
    // Make the request
    Agent response = await agentServiceClient.GetAgentAsync(name);
    

### GetAgentAsync(GetAgentRequest, CallSettings)
    
    
    public virtual Task<Agent> GetAgentAsync(GetAgentRequest request, CallSettings callSettings = null)

Gets details of the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetAgentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetAgentRequest request = new GetAgentRequest
    {
        AgentName = AgentName.FromProjectLocationAppAgent("[PROJECT]", "[LOCATION]", "[APP]", "[AGENT]"),
    };
    // Make the request
    Agent response = await agentServiceClient.GetAgentAsync(request);
    

### GetAgentAsync(GetAgentRequest, CancellationToken)
    
    
    public virtual Task<Agent> GetAgentAsync(GetAgentRequest request, CancellationToken cancellationToken)

Gets details of the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetAgentRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetAgentRequest request = new GetAgentRequest
    {
        AgentName = AgentName.FromProjectLocationAppAgent("[PROJECT]", "[LOCATION]", "[APP]", "[AGENT]"),
    };
    // Make the request
    Agent response = await agentServiceClient.GetAgentAsync(request);
    

### GetAgentAsync(string, CallSettings)
    
    
    public virtual Task<Agent> GetAgentAsync(string name, CallSettings callSettings = null)

Gets details of the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the agent to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/agents/[AGENT]";
    // Make the request
    Agent response = await agentServiceClient.GetAgentAsync(name);
    

### GetAgentAsync(string, CancellationToken)
    
    
    public virtual Task<Agent> GetAgentAsync(string name, CancellationToken cancellationToken)

Gets details of the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the agent to retrieve.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/agents/[AGENT]";
    // Make the request
    Agent response = await agentServiceClient.GetAgentAsync(name);
    

### GetApp(AppName, CallSettings)
    
    
    public virtual App GetApp(AppName name, CallSettings callSettings = null)

Gets details of the specified app.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    AppName name = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    // Make the request
    App response = agentServiceClient.GetApp(name);
    

### GetApp(GetAppRequest, CallSettings)
    
    
    public virtual App GetApp(GetAppRequest request, CallSettings callSettings = null)

Gets details of the specified app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetAppRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    GetAppRequest request = new GetAppRequest
    {
        AppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
    };
    // Make the request
    App response = agentServiceClient.GetApp(request);
    

### GetApp(string, CallSettings)
    
    
    public virtual App GetApp(string name, CallSettings callSettings = null)

Gets details of the specified app.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    // Make the request
    App response = agentServiceClient.GetApp(name);
    

### GetAppAsync(AppName, CallSettings)
    
    
    public virtual Task<App> GetAppAsync(AppName name, CallSettings callSettings = null)

Gets details of the specified app.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AppName name = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    // Make the request
    App response = await agentServiceClient.GetAppAsync(name);
    

### GetAppAsync(AppName, CancellationToken)
    
    
    public virtual Task<App> GetAppAsync(AppName name, CancellationToken cancellationToken)

Gets details of the specified app.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to retrieve.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AppName name = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    // Make the request
    App response = await agentServiceClient.GetAppAsync(name);
    

### GetAppAsync(GetAppRequest, CallSettings)
    
    
    public virtual Task<App> GetAppAsync(GetAppRequest request, CallSettings callSettings = null)

Gets details of the specified app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetAppRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetAppRequest request = new GetAppRequest
    {
        AppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
    };
    // Make the request
    App response = await agentServiceClient.GetAppAsync(request);
    

### GetAppAsync(GetAppRequest, CancellationToken)
    
    
    public virtual Task<App> GetAppAsync(GetAppRequest request, CancellationToken cancellationToken)

Gets details of the specified app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetAppRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetAppRequest request = new GetAppRequest
    {
        AppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
    };
    // Make the request
    App response = await agentServiceClient.GetAppAsync(request);
    

### GetAppAsync(string, CallSettings)
    
    
    public virtual Task<App> GetAppAsync(string name, CallSettings callSettings = null)

Gets details of the specified app.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    // Make the request
    App response = await agentServiceClient.GetAppAsync(name);
    

### GetAppAsync(string, CancellationToken)
    
    
    public virtual Task<App> GetAppAsync(string name, CancellationToken cancellationToken)

Gets details of the specified app.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to retrieve.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    // Make the request
    App response = await agentServiceClient.GetAppAsync(name);
    

### GetAppVersion(AppVersionName, CallSettings)
    
    
    public virtual AppVersion GetAppVersion(AppVersionName name, CallSettings callSettings = null)

Gets details of the specified app version.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AppVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersionName)`  
Required. The resource name of the app version to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    AppVersionName name = AppVersionName.FromProjectLocationAppVersion("[PROJECT]", "[LOCATION]", "[APP]", "[VERSION]");
    // Make the request
    AppVersion response = agentServiceClient.GetAppVersion(name);
    

### GetAppVersion(GetAppVersionRequest, CallSettings)
    
    
    public virtual AppVersion GetAppVersion(GetAppVersionRequest request, CallSettings callSettings = null)

Gets details of the specified app version.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAppVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetAppVersionRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    GetAppVersionRequest request = new GetAppVersionRequest
    {
        AppVersionName = AppVersionName.FromProjectLocationAppVersion("[PROJECT]", "[LOCATION]", "[APP]", "[VERSION]"),
    };
    // Make the request
    AppVersion response = agentServiceClient.GetAppVersion(request);
    

### GetAppVersion(string, CallSettings)
    
    
    public virtual AppVersion GetAppVersion(string name, CallSettings callSettings = null)

Gets details of the specified app version.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app version to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/versions/[VERSION]";
    // Make the request
    AppVersion response = agentServiceClient.GetAppVersion(name);
    

### GetAppVersionAsync(AppVersionName, CallSettings)
    
    
    public virtual Task<AppVersion> GetAppVersionAsync(AppVersionName name, CallSettings callSettings = null)

Gets details of the specified app version.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AppVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersionName)`  
Required. The resource name of the app version to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AppVersionName name = AppVersionName.FromProjectLocationAppVersion("[PROJECT]", "[LOCATION]", "[APP]", "[VERSION]");
    // Make the request
    AppVersion response = await agentServiceClient.GetAppVersionAsync(name);
    

### GetAppVersionAsync(AppVersionName, CancellationToken)
    
    
    public virtual Task<AppVersion> GetAppVersionAsync(AppVersionName name, CancellationToken cancellationToken)

Gets details of the specified app version.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AppVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersionName)`  
Required. The resource name of the app version to retrieve.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AppVersionName name = AppVersionName.FromProjectLocationAppVersion("[PROJECT]", "[LOCATION]", "[APP]", "[VERSION]");
    // Make the request
    AppVersion response = await agentServiceClient.GetAppVersionAsync(name);
    

### GetAppVersionAsync(GetAppVersionRequest, CallSettings)
    
    
    public virtual Task<AppVersion> GetAppVersionAsync(GetAppVersionRequest request, CallSettings callSettings = null)

Gets details of the specified app version.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAppVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetAppVersionRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetAppVersionRequest request = new GetAppVersionRequest
    {
        AppVersionName = AppVersionName.FromProjectLocationAppVersion("[PROJECT]", "[LOCATION]", "[APP]", "[VERSION]"),
    };
    // Make the request
    AppVersion response = await agentServiceClient.GetAppVersionAsync(request);
    

### GetAppVersionAsync(GetAppVersionRequest, CancellationToken)
    
    
    public virtual Task<AppVersion> GetAppVersionAsync(GetAppVersionRequest request, CancellationToken cancellationToken)

Gets details of the specified app version.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAppVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetAppVersionRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetAppVersionRequest request = new GetAppVersionRequest
    {
        AppVersionName = AppVersionName.FromProjectLocationAppVersion("[PROJECT]", "[LOCATION]", "[APP]", "[VERSION]"),
    };
    // Make the request
    AppVersion response = await agentServiceClient.GetAppVersionAsync(request);
    

### GetAppVersionAsync(string, CallSettings)
    
    
    public virtual Task<AppVersion> GetAppVersionAsync(string name, CallSettings callSettings = null)

Gets details of the specified app version.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app version to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/versions/[VERSION]";
    // Make the request
    AppVersion response = await agentServiceClient.GetAppVersionAsync(name);
    

### GetAppVersionAsync(string, CancellationToken)
    
    
    public virtual Task<AppVersion> GetAppVersionAsync(string name, CancellationToken cancellationToken)

Gets details of the specified app version.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app version to retrieve.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/versions/[VERSION]";
    // Make the request
    AppVersion response = await agentServiceClient.GetAppVersionAsync(name);
    

### GetChangelog(ChangelogName, CallSettings)
    
    
    public virtual Changelog GetChangelog(ChangelogName name, CallSettings callSettings = null)

Gets the specified changelog.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ChangelogName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ChangelogName)`  
Required. The resource name of the changelog to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Changelog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Changelog)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    ChangelogName name = ChangelogName.FromProjectLocationAppChangelog("[PROJECT]", "[LOCATION]", "[APP]", "[CHANGELOG]");
    // Make the request
    Changelog response = agentServiceClient.GetChangelog(name);
    

### GetChangelog(GetChangelogRequest, CallSettings)
    
    
    public virtual Changelog GetChangelog(GetChangelogRequest request, CallSettings callSettings = null)

Gets the specified changelog.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetChangelogRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetChangelogRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Changelog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Changelog)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    GetChangelogRequest request = new GetChangelogRequest
    {
        ChangelogName = ChangelogName.FromProjectLocationAppChangelog("[PROJECT]", "[LOCATION]", "[APP]", "[CHANGELOG]"),
    };
    // Make the request
    Changelog response = agentServiceClient.GetChangelog(request);
    

### GetChangelog(string, CallSettings)
    
    
    public virtual Changelog GetChangelog(string name, CallSettings callSettings = null)

Gets the specified changelog.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the changelog to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Changelog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Changelog)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/changelogs/[CHANGELOG]";
    // Make the request
    Changelog response = agentServiceClient.GetChangelog(name);
    

### GetChangelogAsync(ChangelogName, CallSettings)
    
    
    public virtual Task<Changelog> GetChangelogAsync(ChangelogName name, CallSettings callSettings = null)

Gets the specified changelog.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ChangelogName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ChangelogName)`  
Required. The resource name of the changelog to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Changelog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Changelog)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    ChangelogName name = ChangelogName.FromProjectLocationAppChangelog("[PROJECT]", "[LOCATION]", "[APP]", "[CHANGELOG]");
    // Make the request
    Changelog response = await agentServiceClient.GetChangelogAsync(name);
    

### GetChangelogAsync(ChangelogName, CancellationToken)
    
    
    public virtual Task<Changelog> GetChangelogAsync(ChangelogName name, CancellationToken cancellationToken)

Gets the specified changelog.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ChangelogName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ChangelogName)`  
Required. The resource name of the changelog to retrieve.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Changelog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Changelog)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    ChangelogName name = ChangelogName.FromProjectLocationAppChangelog("[PROJECT]", "[LOCATION]", "[APP]", "[CHANGELOG]");
    // Make the request
    Changelog response = await agentServiceClient.GetChangelogAsync(name);
    

### GetChangelogAsync(GetChangelogRequest, CallSettings)
    
    
    public virtual Task<Changelog> GetChangelogAsync(GetChangelogRequest request, CallSettings callSettings = null)

Gets the specified changelog.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetChangelogRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetChangelogRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Changelog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Changelog)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetChangelogRequest request = new GetChangelogRequest
    {
        ChangelogName = ChangelogName.FromProjectLocationAppChangelog("[PROJECT]", "[LOCATION]", "[APP]", "[CHANGELOG]"),
    };
    // Make the request
    Changelog response = await agentServiceClient.GetChangelogAsync(request);
    

### GetChangelogAsync(GetChangelogRequest, CancellationToken)
    
    
    public virtual Task<Changelog> GetChangelogAsync(GetChangelogRequest request, CancellationToken cancellationToken)

Gets the specified changelog.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetChangelogRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetChangelogRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Changelog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Changelog)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetChangelogRequest request = new GetChangelogRequest
    {
        ChangelogName = ChangelogName.FromProjectLocationAppChangelog("[PROJECT]", "[LOCATION]", "[APP]", "[CHANGELOG]"),
    };
    // Make the request
    Changelog response = await agentServiceClient.GetChangelogAsync(request);
    

### GetChangelogAsync(string, CallSettings)
    
    
    public virtual Task<Changelog> GetChangelogAsync(string name, CallSettings callSettings = null)

Gets the specified changelog.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the changelog to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Changelog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Changelog)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/changelogs/[CHANGELOG]";
    // Make the request
    Changelog response = await agentServiceClient.GetChangelogAsync(name);
    

### GetChangelogAsync(string, CancellationToken)
    
    
    public virtual Task<Changelog> GetChangelogAsync(string name, CancellationToken cancellationToken)

Gets the specified changelog.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the changelog to retrieve.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Changelog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Changelog)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/changelogs/[CHANGELOG]";
    // Make the request
    Changelog response = await agentServiceClient.GetChangelogAsync(name);
    

### GetConversation(ConversationName, CallSettings)
    
    
    public virtual Conversation GetConversation(ConversationName name, CallSettings callSettings = null)

Gets details of the specified conversation.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ConversationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ConversationName)`  
Required. The resource name of the conversation to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    ConversationName name = ConversationName.FromProjectLocationAppConversation("[PROJECT]", "[LOCATION]", "[APP]", "[CONVERSATION]");
    // Make the request
    Conversation response = agentServiceClient.GetConversation(name);
    

### GetConversation(GetConversationRequest, CallSettings)
    
    
    public virtual Conversation GetConversation(GetConversationRequest request, CallSettings callSettings = null)

Gets details of the specified conversation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetConversationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetConversationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    GetConversationRequest request = new GetConversationRequest
    {
        ConversationName = ConversationName.FromProjectLocationAppConversation("[PROJECT]", "[LOCATION]", "[APP]", "[CONVERSATION]"),
    };
    // Make the request
    Conversation response = agentServiceClient.GetConversation(request);
    

### GetConversation(string, CallSettings)
    
    
    public virtual Conversation GetConversation(string name, CallSettings callSettings = null)

Gets details of the specified conversation.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the conversation to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/conversations/[CONVERSATION]";
    // Make the request
    Conversation response = agentServiceClient.GetConversation(name);
    

### GetConversationAsync(ConversationName, CallSettings)
    
    
    public virtual Task<Conversation> GetConversationAsync(ConversationName name, CallSettings callSettings = null)

Gets details of the specified conversation.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ConversationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ConversationName)`  
Required. The resource name of the conversation to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    ConversationName name = ConversationName.FromProjectLocationAppConversation("[PROJECT]", "[LOCATION]", "[APP]", "[CONVERSATION]");
    // Make the request
    Conversation response = await agentServiceClient.GetConversationAsync(name);
    

### GetConversationAsync(ConversationName, CancellationToken)
    
    
    public virtual Task<Conversation> GetConversationAsync(ConversationName name, CancellationToken cancellationToken)

Gets details of the specified conversation.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ConversationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ConversationName)`  
Required. The resource name of the conversation to retrieve.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    ConversationName name = ConversationName.FromProjectLocationAppConversation("[PROJECT]", "[LOCATION]", "[APP]", "[CONVERSATION]");
    // Make the request
    Conversation response = await agentServiceClient.GetConversationAsync(name);
    

### GetConversationAsync(GetConversationRequest, CallSettings)
    
    
    public virtual Task<Conversation> GetConversationAsync(GetConversationRequest request, CallSettings callSettings = null)

Gets details of the specified conversation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetConversationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetConversationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetConversationRequest request = new GetConversationRequest
    {
        ConversationName = ConversationName.FromProjectLocationAppConversation("[PROJECT]", "[LOCATION]", "[APP]", "[CONVERSATION]"),
    };
    // Make the request
    Conversation response = await agentServiceClient.GetConversationAsync(request);
    

### GetConversationAsync(GetConversationRequest, CancellationToken)
    
    
    public virtual Task<Conversation> GetConversationAsync(GetConversationRequest request, CancellationToken cancellationToken)

Gets details of the specified conversation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetConversationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetConversationRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetConversationRequest request = new GetConversationRequest
    {
        ConversationName = ConversationName.FromProjectLocationAppConversation("[PROJECT]", "[LOCATION]", "[APP]", "[CONVERSATION]"),
    };
    // Make the request
    Conversation response = await agentServiceClient.GetConversationAsync(request);
    

### GetConversationAsync(string, CallSettings)
    
    
    public virtual Task<Conversation> GetConversationAsync(string name, CallSettings callSettings = null)

Gets details of the specified conversation.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the conversation to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/conversations/[CONVERSATION]";
    // Make the request
    Conversation response = await agentServiceClient.GetConversationAsync(name);
    

### GetConversationAsync(string, CancellationToken)
    
    
    public virtual Task<Conversation> GetConversationAsync(string name, CancellationToken cancellationToken)

Gets details of the specified conversation.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the conversation to retrieve.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/conversations/[CONVERSATION]";
    // Make the request
    Conversation response = await agentServiceClient.GetConversationAsync(name);
    

### GetDeployment(DeploymentName, CallSettings)
    
    
    public virtual Deployment GetDeployment(DeploymentName name, CallSettings callSettings = null)

Gets details of the specified deployment.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DeploymentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeploymentName)`  
Required. The name of the deployment. Format: `projects/{project}/locations/{location}/apps/{app}/deployments/{deployment}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    DeploymentName name = DeploymentName.FromProjectLocationAppDeployment("[PROJECT]", "[LOCATION]", "[APP]", "[DEPLOYMENT]");
    // Make the request
    Deployment response = agentServiceClient.GetDeployment(name);
    

### GetDeployment(GetDeploymentRequest, CallSettings)
    
    
    public virtual Deployment GetDeployment(GetDeploymentRequest request, CallSettings callSettings = null)

Gets details of the specified deployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetDeploymentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    GetDeploymentRequest request = new GetDeploymentRequest
    {
        DeploymentName = DeploymentName.FromProjectLocationAppDeployment("[PROJECT]", "[LOCATION]", "[APP]", "[DEPLOYMENT]"),
    };
    // Make the request
    Deployment response = agentServiceClient.GetDeployment(request);
    

### GetDeployment(string, CallSettings)
    
    
    public virtual Deployment GetDeployment(string name, CallSettings callSettings = null)

Gets details of the specified deployment.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the deployment. Format: `projects/{project}/locations/{location}/apps/{app}/deployments/{deployment}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/deployments/[DEPLOYMENT]";
    // Make the request
    Deployment response = agentServiceClient.GetDeployment(name);
    

### GetDeploymentAsync(DeploymentName, CallSettings)
    
    
    public virtual Task<Deployment> GetDeploymentAsync(DeploymentName name, CallSettings callSettings = null)

Gets details of the specified deployment.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DeploymentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeploymentName)`  
Required. The name of the deployment. Format: `projects/{project}/locations/{location}/apps/{app}/deployments/{deployment}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeploymentName name = DeploymentName.FromProjectLocationAppDeployment("[PROJECT]", "[LOCATION]", "[APP]", "[DEPLOYMENT]");
    // Make the request
    Deployment response = await agentServiceClient.GetDeploymentAsync(name);
    

### GetDeploymentAsync(DeploymentName, CancellationToken)
    
    
    public virtual Task<Deployment> GetDeploymentAsync(DeploymentName name, CancellationToken cancellationToken)

Gets details of the specified deployment.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DeploymentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeploymentName)`  
Required. The name of the deployment. Format: `projects/{project}/locations/{location}/apps/{app}/deployments/{deployment}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeploymentName name = DeploymentName.FromProjectLocationAppDeployment("[PROJECT]", "[LOCATION]", "[APP]", "[DEPLOYMENT]");
    // Make the request
    Deployment response = await agentServiceClient.GetDeploymentAsync(name);
    

### GetDeploymentAsync(GetDeploymentRequest, CallSettings)
    
    
    public virtual Task<Deployment> GetDeploymentAsync(GetDeploymentRequest request, CallSettings callSettings = null)

Gets details of the specified deployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetDeploymentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetDeploymentRequest request = new GetDeploymentRequest
    {
        DeploymentName = DeploymentName.FromProjectLocationAppDeployment("[PROJECT]", "[LOCATION]", "[APP]", "[DEPLOYMENT]"),
    };
    // Make the request
    Deployment response = await agentServiceClient.GetDeploymentAsync(request);
    

### GetDeploymentAsync(GetDeploymentRequest, CancellationToken)
    
    
    public virtual Task<Deployment> GetDeploymentAsync(GetDeploymentRequest request, CancellationToken cancellationToken)

Gets details of the specified deployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetDeploymentRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetDeploymentRequest request = new GetDeploymentRequest
    {
        DeploymentName = DeploymentName.FromProjectLocationAppDeployment("[PROJECT]", "[LOCATION]", "[APP]", "[DEPLOYMENT]"),
    };
    // Make the request
    Deployment response = await agentServiceClient.GetDeploymentAsync(request);
    

### GetDeploymentAsync(string, CallSettings)
    
    
    public virtual Task<Deployment> GetDeploymentAsync(string name, CallSettings callSettings = null)

Gets details of the specified deployment.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the deployment. Format: `projects/{project}/locations/{location}/apps/{app}/deployments/{deployment}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/deployments/[DEPLOYMENT]";
    // Make the request
    Deployment response = await agentServiceClient.GetDeploymentAsync(name);
    

### GetDeploymentAsync(string, CancellationToken)
    
    
    public virtual Task<Deployment> GetDeploymentAsync(string name, CancellationToken cancellationToken)

Gets details of the specified deployment.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the deployment. Format: `projects/{project}/locations/{location}/apps/{app}/deployments/{deployment}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/deployments/[DEPLOYMENT]";
    // Make the request
    Deployment response = await agentServiceClient.GetDeploymentAsync(name);
    

### GetExample(ExampleName, CallSettings)
    
    
    public virtual Example GetExample(ExampleName name, CallSettings callSettings = null)

Gets details of the specified example.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ExampleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExampleName)`  
Required. The resource name of the example to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    ExampleName name = ExampleName.FromProjectLocationAppExample("[PROJECT]", "[LOCATION]", "[APP]", "[EXAMPLE]");
    // Make the request
    Example response = agentServiceClient.GetExample(name);
    

### GetExample(GetExampleRequest, CallSettings)
    
    
    public virtual Example GetExample(GetExampleRequest request, CallSettings callSettings = null)

Gets details of the specified example.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetExampleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetExampleRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    GetExampleRequest request = new GetExampleRequest
    {
        ExampleName = ExampleName.FromProjectLocationAppExample("[PROJECT]", "[LOCATION]", "[APP]", "[EXAMPLE]"),
    };
    // Make the request
    Example response = agentServiceClient.GetExample(request);
    

### GetExample(string, CallSettings)
    
    
    public virtual Example GetExample(string name, CallSettings callSettings = null)

Gets details of the specified example.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the example to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/examples/[EXAMPLE]";
    // Make the request
    Example response = agentServiceClient.GetExample(name);
    

### GetExampleAsync(ExampleName, CallSettings)
    
    
    public virtual Task<Example> GetExampleAsync(ExampleName name, CallSettings callSettings = null)

Gets details of the specified example.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ExampleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExampleName)`  
Required. The resource name of the example to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    ExampleName name = ExampleName.FromProjectLocationAppExample("[PROJECT]", "[LOCATION]", "[APP]", "[EXAMPLE]");
    // Make the request
    Example response = await agentServiceClient.GetExampleAsync(name);
    

### GetExampleAsync(ExampleName, CancellationToken)
    
    
    public virtual Task<Example> GetExampleAsync(ExampleName name, CancellationToken cancellationToken)

Gets details of the specified example.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ExampleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExampleName)`  
Required. The resource name of the example to retrieve.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    ExampleName name = ExampleName.FromProjectLocationAppExample("[PROJECT]", "[LOCATION]", "[APP]", "[EXAMPLE]");
    // Make the request
    Example response = await agentServiceClient.GetExampleAsync(name);
    

### GetExampleAsync(GetExampleRequest, CallSettings)
    
    
    public virtual Task<Example> GetExampleAsync(GetExampleRequest request, CallSettings callSettings = null)

Gets details of the specified example.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetExampleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetExampleRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetExampleRequest request = new GetExampleRequest
    {
        ExampleName = ExampleName.FromProjectLocationAppExample("[PROJECT]", "[LOCATION]", "[APP]", "[EXAMPLE]"),
    };
    // Make the request
    Example response = await agentServiceClient.GetExampleAsync(request);
    

### GetExampleAsync(GetExampleRequest, CancellationToken)
    
    
    public virtual Task<Example> GetExampleAsync(GetExampleRequest request, CancellationToken cancellationToken)

Gets details of the specified example.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetExampleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetExampleRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetExampleRequest request = new GetExampleRequest
    {
        ExampleName = ExampleName.FromProjectLocationAppExample("[PROJECT]", "[LOCATION]", "[APP]", "[EXAMPLE]"),
    };
    // Make the request
    Example response = await agentServiceClient.GetExampleAsync(request);
    

### GetExampleAsync(string, CallSettings)
    
    
    public virtual Task<Example> GetExampleAsync(string name, CallSettings callSettings = null)

Gets details of the specified example.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the example to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/examples/[EXAMPLE]";
    // Make the request
    Example response = await agentServiceClient.GetExampleAsync(name);
    

### GetExampleAsync(string, CancellationToken)
    
    
    public virtual Task<Example> GetExampleAsync(string name, CancellationToken cancellationToken)

Gets details of the specified example.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the example to retrieve.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/examples/[EXAMPLE]";
    // Make the request
    Example response = await agentServiceClient.GetExampleAsync(name);
    

### GetGuardrail(GetGuardrailRequest, CallSettings)
    
    
    public virtual Guardrail GetGuardrail(GetGuardrailRequest request, CallSettings callSettings = null)

Gets details of the specified guardrail.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGuardrailRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetGuardrailRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    GetGuardrailRequest request = new GetGuardrailRequest
    {
        GuardrailName = GuardrailName.FromProjectLocationAppGuardrail("[PROJECT]", "[LOCATION]", "[APP]", "[GUARDRAIL]"),
    };
    // Make the request
    Guardrail response = agentServiceClient.GetGuardrail(request);
    

### GetGuardrail(GuardrailName, CallSettings)
    
    
    public virtual Guardrail GetGuardrail(GuardrailName name, CallSettings callSettings = null)

Gets details of the specified guardrail.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[GuardrailName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GuardrailName)`  
Required. The resource name of the guardrail to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    GuardrailName name = GuardrailName.FromProjectLocationAppGuardrail("[PROJECT]", "[LOCATION]", "[APP]", "[GUARDRAIL]");
    // Make the request
    Guardrail response = agentServiceClient.GetGuardrail(name);
    

### GetGuardrail(string, CallSettings)
    
    
    public virtual Guardrail GetGuardrail(string name, CallSettings callSettings = null)

Gets details of the specified guardrail.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the guardrail to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/guardrails/[GUARDRAIL]";
    // Make the request
    Guardrail response = agentServiceClient.GetGuardrail(name);
    

### GetGuardrailAsync(GetGuardrailRequest, CallSettings)
    
    
    public virtual Task<Guardrail> GetGuardrailAsync(GetGuardrailRequest request, CallSettings callSettings = null)

Gets details of the specified guardrail.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGuardrailRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetGuardrailRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetGuardrailRequest request = new GetGuardrailRequest
    {
        GuardrailName = GuardrailName.FromProjectLocationAppGuardrail("[PROJECT]", "[LOCATION]", "[APP]", "[GUARDRAIL]"),
    };
    // Make the request
    Guardrail response = await agentServiceClient.GetGuardrailAsync(request);
    

### GetGuardrailAsync(GetGuardrailRequest, CancellationToken)
    
    
    public virtual Task<Guardrail> GetGuardrailAsync(GetGuardrailRequest request, CancellationToken cancellationToken)

Gets details of the specified guardrail.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGuardrailRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetGuardrailRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetGuardrailRequest request = new GetGuardrailRequest
    {
        GuardrailName = GuardrailName.FromProjectLocationAppGuardrail("[PROJECT]", "[LOCATION]", "[APP]", "[GUARDRAIL]"),
    };
    // Make the request
    Guardrail response = await agentServiceClient.GetGuardrailAsync(request);
    

### GetGuardrailAsync(GuardrailName, CallSettings)
    
    
    public virtual Task<Guardrail> GetGuardrailAsync(GuardrailName name, CallSettings callSettings = null)

Gets details of the specified guardrail.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[GuardrailName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GuardrailName)`  
Required. The resource name of the guardrail to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    GuardrailName name = GuardrailName.FromProjectLocationAppGuardrail("[PROJECT]", "[LOCATION]", "[APP]", "[GUARDRAIL]");
    // Make the request
    Guardrail response = await agentServiceClient.GetGuardrailAsync(name);
    

### GetGuardrailAsync(GuardrailName, CancellationToken)
    
    
    public virtual Task<Guardrail> GetGuardrailAsync(GuardrailName name, CancellationToken cancellationToken)

Gets details of the specified guardrail.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[GuardrailName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GuardrailName)`  
Required. The resource name of the guardrail to retrieve.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    GuardrailName name = GuardrailName.FromProjectLocationAppGuardrail("[PROJECT]", "[LOCATION]", "[APP]", "[GUARDRAIL]");
    // Make the request
    Guardrail response = await agentServiceClient.GetGuardrailAsync(name);
    

### GetGuardrailAsync(string, CallSettings)
    
    
    public virtual Task<Guardrail> GetGuardrailAsync(string name, CallSettings callSettings = null)

Gets details of the specified guardrail.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the guardrail to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/guardrails/[GUARDRAIL]";
    // Make the request
    Guardrail response = await agentServiceClient.GetGuardrailAsync(name);
    

### GetGuardrailAsync(string, CancellationToken)
    
    
    public virtual Task<Guardrail> GetGuardrailAsync(string name, CancellationToken cancellationToken)

Gets details of the specified guardrail.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the guardrail to retrieve.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/guardrails/[GUARDRAIL]";
    // Make the request
    Guardrail response = await agentServiceClient.GetGuardrailAsync(name);
    

### GetSecuritySettings(GetSecuritySettingsRequest, CallSettings)
    
    
    public virtual SecuritySettings GetSecuritySettings(GetSecuritySettingsRequest request, CallSettings callSettings = null)

Retrieves the security settings for the project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSecuritySettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetSecuritySettingsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[SecuritySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SecuritySettings)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    GetSecuritySettingsRequest request = new GetSecuritySettingsRequest
    {
        SecuritySettingsName = SecuritySettingsName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    SecuritySettings response = agentServiceClient.GetSecuritySettings(request);
    

### GetSecuritySettings(SecuritySettingsName, CallSettings)
    
    
    public virtual SecuritySettings GetSecuritySettings(SecuritySettingsName name, CallSettings callSettings = null)

Retrieves the security settings for the project and location.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[SecuritySettingsName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SecuritySettingsName)`  
Required. The resource name of the security settings to retrieve. Format: `projects/{project}/locations/{location}/securitySettings`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[SecuritySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SecuritySettings)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    SecuritySettingsName name = SecuritySettingsName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    SecuritySettings response = agentServiceClient.GetSecuritySettings(name);
    

### GetSecuritySettings(string, CallSettings)
    
    
    public virtual SecuritySettings GetSecuritySettings(string name, CallSettings callSettings = null)

Retrieves the security settings for the project and location.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the security settings to retrieve. Format: `projects/{project}/locations/{location}/securitySettings`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[SecuritySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SecuritySettings)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/securitySettings";
    // Make the request
    SecuritySettings response = agentServiceClient.GetSecuritySettings(name);
    

### GetSecuritySettingsAsync(GetSecuritySettingsRequest, CallSettings)
    
    
    public virtual Task<SecuritySettings> GetSecuritySettingsAsync(GetSecuritySettingsRequest request, CallSettings callSettings = null)

Retrieves the security settings for the project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSecuritySettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetSecuritySettingsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SecuritySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SecuritySettings)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetSecuritySettingsRequest request = new GetSecuritySettingsRequest
    {
        SecuritySettingsName = SecuritySettingsName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    SecuritySettings response = await agentServiceClient.GetSecuritySettingsAsync(request);
    

### GetSecuritySettingsAsync(GetSecuritySettingsRequest, CancellationToken)
    
    
    public virtual Task<SecuritySettings> GetSecuritySettingsAsync(GetSecuritySettingsRequest request, CancellationToken cancellationToken)

Retrieves the security settings for the project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSecuritySettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetSecuritySettingsRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SecuritySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SecuritySettings)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetSecuritySettingsRequest request = new GetSecuritySettingsRequest
    {
        SecuritySettingsName = SecuritySettingsName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    SecuritySettings response = await agentServiceClient.GetSecuritySettingsAsync(request);
    

### GetSecuritySettingsAsync(SecuritySettingsName, CallSettings)
    
    
    public virtual Task<SecuritySettings> GetSecuritySettingsAsync(SecuritySettingsName name, CallSettings callSettings = null)

Retrieves the security settings for the project and location.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[SecuritySettingsName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SecuritySettingsName)`  
Required. The resource name of the security settings to retrieve. Format: `projects/{project}/locations/{location}/securitySettings`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SecuritySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SecuritySettings)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    SecuritySettingsName name = SecuritySettingsName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    SecuritySettings response = await agentServiceClient.GetSecuritySettingsAsync(name);
    

### GetSecuritySettingsAsync(SecuritySettingsName, CancellationToken)
    
    
    public virtual Task<SecuritySettings> GetSecuritySettingsAsync(SecuritySettingsName name, CancellationToken cancellationToken)

Retrieves the security settings for the project and location.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[SecuritySettingsName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SecuritySettingsName)`  
Required. The resource name of the security settings to retrieve. Format: `projects/{project}/locations/{location}/securitySettings`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SecuritySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SecuritySettings)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    SecuritySettingsName name = SecuritySettingsName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    SecuritySettings response = await agentServiceClient.GetSecuritySettingsAsync(name);
    

### GetSecuritySettingsAsync(string, CallSettings)
    
    
    public virtual Task<SecuritySettings> GetSecuritySettingsAsync(string name, CallSettings callSettings = null)

Retrieves the security settings for the project and location.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the security settings to retrieve. Format: `projects/{project}/locations/{location}/securitySettings`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SecuritySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SecuritySettings)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/securitySettings";
    // Make the request
    SecuritySettings response = await agentServiceClient.GetSecuritySettingsAsync(name);
    

### GetSecuritySettingsAsync(string, CancellationToken)
    
    
    public virtual Task<SecuritySettings> GetSecuritySettingsAsync(string name, CancellationToken cancellationToken)

Retrieves the security settings for the project and location.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the security settings to retrieve. Format: `projects/{project}/locations/{location}/securitySettings`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SecuritySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SecuritySettings)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/securitySettings";
    // Make the request
    SecuritySettings response = await agentServiceClient.GetSecuritySettingsAsync(name);
    

### GetTool(GetToolRequest, CallSettings)
    
    
    public virtual Tool GetTool(GetToolRequest request, CallSettings callSettings = null)

Gets details of the specified tool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetToolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetToolRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    GetToolRequest request = new GetToolRequest
    {
        ToolName = ToolName.FromProjectLocationAppTool("[PROJECT]", "[LOCATION]", "[APP]", "[TOOL]"),
    };
    // Make the request
    Tool response = agentServiceClient.GetTool(request);
    

### GetTool(ToolName, CallSettings)
    
    
    public virtual Tool GetTool(ToolName name, CallSettings callSettings = null)

Gets details of the specified tool.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ToolName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ToolName)`  
Required. The resource name of the tool to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    ToolName name = ToolName.FromProjectLocationAppTool("[PROJECT]", "[LOCATION]", "[APP]", "[TOOL]");
    // Make the request
    Tool response = agentServiceClient.GetTool(name);
    

### GetTool(string, CallSettings)
    
    
    public virtual Tool GetTool(string name, CallSettings callSettings = null)

Gets details of the specified tool.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the tool to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/tools/[TOOL]";
    // Make the request
    Tool response = agentServiceClient.GetTool(name);
    

### GetToolAsync(GetToolRequest, CallSettings)
    
    
    public virtual Task<Tool> GetToolAsync(GetToolRequest request, CallSettings callSettings = null)

Gets details of the specified tool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetToolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetToolRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetToolRequest request = new GetToolRequest
    {
        ToolName = ToolName.FromProjectLocationAppTool("[PROJECT]", "[LOCATION]", "[APP]", "[TOOL]"),
    };
    // Make the request
    Tool response = await agentServiceClient.GetToolAsync(request);
    

### GetToolAsync(GetToolRequest, CancellationToken)
    
    
    public virtual Task<Tool> GetToolAsync(GetToolRequest request, CancellationToken cancellationToken)

Gets details of the specified tool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetToolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetToolRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetToolRequest request = new GetToolRequest
    {
        ToolName = ToolName.FromProjectLocationAppTool("[PROJECT]", "[LOCATION]", "[APP]", "[TOOL]"),
    };
    // Make the request
    Tool response = await agentServiceClient.GetToolAsync(request);
    

### GetToolAsync(ToolName, CallSettings)
    
    
    public virtual Task<Tool> GetToolAsync(ToolName name, CallSettings callSettings = null)

Gets details of the specified tool.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ToolName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ToolName)`  
Required. The resource name of the tool to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    ToolName name = ToolName.FromProjectLocationAppTool("[PROJECT]", "[LOCATION]", "[APP]", "[TOOL]");
    // Make the request
    Tool response = await agentServiceClient.GetToolAsync(name);
    

### GetToolAsync(ToolName, CancellationToken)
    
    
    public virtual Task<Tool> GetToolAsync(ToolName name, CancellationToken cancellationToken)

Gets details of the specified tool.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ToolName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ToolName)`  
Required. The resource name of the tool to retrieve.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    ToolName name = ToolName.FromProjectLocationAppTool("[PROJECT]", "[LOCATION]", "[APP]", "[TOOL]");
    // Make the request
    Tool response = await agentServiceClient.GetToolAsync(name);
    

### GetToolAsync(string, CallSettings)
    
    
    public virtual Task<Tool> GetToolAsync(string name, CallSettings callSettings = null)

Gets details of the specified tool.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the tool to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/tools/[TOOL]";
    // Make the request
    Tool response = await agentServiceClient.GetToolAsync(name);
    

### GetToolAsync(string, CancellationToken)
    
    
    public virtual Task<Tool> GetToolAsync(string name, CancellationToken cancellationToken)

Gets details of the specified tool.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the tool to retrieve.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/tools/[TOOL]";
    // Make the request
    Tool response = await agentServiceClient.GetToolAsync(name);
    

### GetToolset(GetToolsetRequest, CallSettings)
    
    
    public virtual Toolset GetToolset(GetToolsetRequest request, CallSettings callSettings = null)

Gets details of the specified toolset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetToolsetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetToolsetRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    GetToolsetRequest request = new GetToolsetRequest
    {
        ToolsetName = ToolsetName.FromProjectLocationAppToolset("[PROJECT]", "[LOCATION]", "[APP]", "[TOOLSET]"),
    };
    // Make the request
    Toolset response = agentServiceClient.GetToolset(request);
    

### GetToolset(ToolsetName, CallSettings)
    
    
    public virtual Toolset GetToolset(ToolsetName name, CallSettings callSettings = null)

Gets details of the specified toolset.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ToolsetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ToolsetName)`  
Required. The resource name of the toolset to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    ToolsetName name = ToolsetName.FromProjectLocationAppToolset("[PROJECT]", "[LOCATION]", "[APP]", "[TOOLSET]");
    // Make the request
    Toolset response = agentServiceClient.GetToolset(name);
    

### GetToolset(string, CallSettings)
    
    
    public virtual Toolset GetToolset(string name, CallSettings callSettings = null)

Gets details of the specified toolset.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the toolset to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/toolsets/[TOOLSET]";
    // Make the request
    Toolset response = agentServiceClient.GetToolset(name);
    

### GetToolsetAsync(GetToolsetRequest, CallSettings)
    
    
    public virtual Task<Toolset> GetToolsetAsync(GetToolsetRequest request, CallSettings callSettings = null)

Gets details of the specified toolset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetToolsetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetToolsetRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetToolsetRequest request = new GetToolsetRequest
    {
        ToolsetName = ToolsetName.FromProjectLocationAppToolset("[PROJECT]", "[LOCATION]", "[APP]", "[TOOLSET]"),
    };
    // Make the request
    Toolset response = await agentServiceClient.GetToolsetAsync(request);
    

### GetToolsetAsync(GetToolsetRequest, CancellationToken)
    
    
    public virtual Task<Toolset> GetToolsetAsync(GetToolsetRequest request, CancellationToken cancellationToken)

Gets details of the specified toolset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetToolsetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetToolsetRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetToolsetRequest request = new GetToolsetRequest
    {
        ToolsetName = ToolsetName.FromProjectLocationAppToolset("[PROJECT]", "[LOCATION]", "[APP]", "[TOOLSET]"),
    };
    // Make the request
    Toolset response = await agentServiceClient.GetToolsetAsync(request);
    

### GetToolsetAsync(ToolsetName, CallSettings)
    
    
    public virtual Task<Toolset> GetToolsetAsync(ToolsetName name, CallSettings callSettings = null)

Gets details of the specified toolset.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ToolsetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ToolsetName)`  
Required. The resource name of the toolset to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    ToolsetName name = ToolsetName.FromProjectLocationAppToolset("[PROJECT]", "[LOCATION]", "[APP]", "[TOOLSET]");
    // Make the request
    Toolset response = await agentServiceClient.GetToolsetAsync(name);
    

### GetToolsetAsync(ToolsetName, CancellationToken)
    
    
    public virtual Task<Toolset> GetToolsetAsync(ToolsetName name, CancellationToken cancellationToken)

Gets details of the specified toolset.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ToolsetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ToolsetName)`  
Required. The resource name of the toolset to retrieve.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    ToolsetName name = ToolsetName.FromProjectLocationAppToolset("[PROJECT]", "[LOCATION]", "[APP]", "[TOOLSET]");
    // Make the request
    Toolset response = await agentServiceClient.GetToolsetAsync(name);
    

### GetToolsetAsync(string, CallSettings)
    
    
    public virtual Task<Toolset> GetToolsetAsync(string name, CallSettings callSettings = null)

Gets details of the specified toolset.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the toolset to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/toolsets/[TOOLSET]";
    // Make the request
    Toolset response = await agentServiceClient.GetToolsetAsync(name);
    

### GetToolsetAsync(string, CancellationToken)
    
    
    public virtual Task<Toolset> GetToolsetAsync(string name, CancellationToken cancellationToken)

Gets details of the specified toolset.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the toolset to retrieve.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/toolsets/[TOOLSET]";
    // Make the request
    Toolset response = await agentServiceClient.GetToolsetAsync(name);
    

### ImportApp(LocationName, string, string, CallSettings)
    
    
    public virtual Operation<ImportAppResponse, OperationMetadata> ImportApp(LocationName parent, string displayName, string appId, CallSettings callSettings = null)

Imports the specified app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent resource name with the location of the app to import.  
`displayName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The display name of the app to import.

  * If the app is created on import, and the display name is specified, the imported app will use this display name. If a conflict is detected with an existing app, a timestamp will be appended to the display name to make it unique.
  * If the app is a reimport, this field should not be set. Providing a display name during reimport will result in an INVALID_ARGUMENT error.

  
`appId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the imported app.

  * If not specified, a unique ID will be automatically assigned for the app.
  * Otherwise, the imported app will use this ID as the final component of its resource name. If an app with the same ID already exists at the specified location in the project, the content of the existing app will be replaced.

  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportAppResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ImportAppResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    string displayName = "";
    string appId = "";
    // Make the request
    Operation<ImportAppResponse, OperationMetadata> response = agentServiceClient.ImportApp(parent, displayName, appId);
    
    // Poll until the returned long-running operation is complete
    Operation<ImportAppResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    ImportAppResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ImportAppResponse, OperationMetadata> retrievedResponse = agentServiceClient.PollOnceImportApp(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ImportAppResponse retrievedResult = retrievedResponse.Result;
    }
    

### ImportApp(ImportAppRequest, CallSettings)
    
    
    public virtual Operation<ImportAppResponse, OperationMetadata> ImportApp(ImportAppRequest request, CallSettings callSettings = null)

Imports the specified app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ImportAppRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportAppResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ImportAppResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    ImportAppRequest request = new ImportAppRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        DisplayName = "",
        AppId = "",
        GcsUri = "",
        ImportOptions = new ImportAppRequest.Types.ImportOptions(),
        IgnoreAppLock = false,
    };
    // Make the request
    Operation<ImportAppResponse, OperationMetadata> response = agentServiceClient.ImportApp(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ImportAppResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    ImportAppResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ImportAppResponse, OperationMetadata> retrievedResponse = agentServiceClient.PollOnceImportApp(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ImportAppResponse retrievedResult = retrievedResponse.Result;
    }
    

### ImportApp(string, string, string, CallSettings)
    
    
    public virtual Operation<ImportAppResponse, OperationMetadata> ImportApp(string parent, string displayName, string appId, CallSettings callSettings = null)

Imports the specified app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource name with the location of the app to import.  
`displayName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The display name of the app to import.

  * If the app is created on import, and the display name is specified, the imported app will use this display name. If a conflict is detected with an existing app, a timestamp will be appended to the display name to make it unique.
  * If the app is a reimport, this field should not be set. Providing a display name during reimport will result in an INVALID_ARGUMENT error.

  
`appId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the imported app.

  * If not specified, a unique ID will be automatically assigned for the app.
  * Otherwise, the imported app will use this ID as the final component of its resource name. If an app with the same ID already exists at the specified location in the project, the content of the existing app will be replaced.

  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportAppResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ImportAppResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    string displayName = "";
    string appId = "";
    // Make the request
    Operation<ImportAppResponse, OperationMetadata> response = agentServiceClient.ImportApp(parent, displayName, appId);
    
    // Poll until the returned long-running operation is complete
    Operation<ImportAppResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    ImportAppResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ImportAppResponse, OperationMetadata> retrievedResponse = agentServiceClient.PollOnceImportApp(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ImportAppResponse retrievedResult = retrievedResponse.Result;
    }
    

### ImportAppAsync(LocationName, string, string, CallSettings)
    
    
    public virtual Task<Operation<ImportAppResponse, OperationMetadata>> ImportAppAsync(LocationName parent, string displayName, string appId, CallSettings callSettings = null)

Imports the specified app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent resource name with the location of the app to import.  
`displayName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The display name of the app to import.

  * If the app is created on import, and the display name is specified, the imported app will use this display name. If a conflict is detected with an existing app, a timestamp will be appended to the display name to make it unique.
  * If the app is a reimport, this field should not be set. Providing a display name during reimport will result in an INVALID_ARGUMENT error.

  
`appId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the imported app.

  * If not specified, a unique ID will be automatically assigned for the app.
  * Otherwise, the imported app will use this ID as the final component of its resource name. If an app with the same ID already exists at the specified location in the project, the content of the existing app will be replaced.

  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportAppResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ImportAppResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    string displayName = "";
    string appId = "";
    // Make the request
    Operation<ImportAppResponse, OperationMetadata> response = await agentServiceClient.ImportAppAsync(parent, displayName, appId);
    
    // Poll until the returned long-running operation is complete
    Operation<ImportAppResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ImportAppResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ImportAppResponse, OperationMetadata> retrievedResponse = await agentServiceClient.PollOnceImportAppAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ImportAppResponse retrievedResult = retrievedResponse.Result;
    }
    

### ImportAppAsync(LocationName, string, string, CancellationToken)
    
    
    public virtual Task<Operation<ImportAppResponse, OperationMetadata>> ImportAppAsync(LocationName parent, string displayName, string appId, CancellationToken cancellationToken)

Imports the specified app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent resource name with the location of the app to import.  
`displayName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The display name of the app to import.

  * If the app is created on import, and the display name is specified, the imported app will use this display name. If a conflict is detected with an existing app, a timestamp will be appended to the display name to make it unique.
  * If the app is a reimport, this field should not be set. Providing a display name during reimport will result in an INVALID_ARGUMENT error.

  
`appId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the imported app.

  * If not specified, a unique ID will be automatically assigned for the app.
  * Otherwise, the imported app will use this ID as the final component of its resource name. If an app with the same ID already exists at the specified location in the project, the content of the existing app will be replaced.

  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportAppResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ImportAppResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    string displayName = "";
    string appId = "";
    // Make the request
    Operation<ImportAppResponse, OperationMetadata> response = await agentServiceClient.ImportAppAsync(parent, displayName, appId);
    
    // Poll until the returned long-running operation is complete
    Operation<ImportAppResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ImportAppResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ImportAppResponse, OperationMetadata> retrievedResponse = await agentServiceClient.PollOnceImportAppAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ImportAppResponse retrievedResult = retrievedResponse.Result;
    }
    

### ImportAppAsync(ImportAppRequest, CallSettings)
    
    
    public virtual Task<Operation<ImportAppResponse, OperationMetadata>> ImportAppAsync(ImportAppRequest request, CallSettings callSettings = null)

Imports the specified app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ImportAppRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportAppResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ImportAppResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    ImportAppRequest request = new ImportAppRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        DisplayName = "",
        AppId = "",
        GcsUri = "",
        ImportOptions = new ImportAppRequest.Types.ImportOptions(),
        IgnoreAppLock = false,
    };
    // Make the request
    Operation<ImportAppResponse, OperationMetadata> response = await agentServiceClient.ImportAppAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ImportAppResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ImportAppResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ImportAppResponse, OperationMetadata> retrievedResponse = await agentServiceClient.PollOnceImportAppAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ImportAppResponse retrievedResult = retrievedResponse.Result;
    }
    

### ImportAppAsync(ImportAppRequest, CancellationToken)
    
    
    public virtual Task<Operation<ImportAppResponse, OperationMetadata>> ImportAppAsync(ImportAppRequest request, CancellationToken cancellationToken)

Imports the specified app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ImportAppRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportAppResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ImportAppResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    ImportAppRequest request = new ImportAppRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        DisplayName = "",
        AppId = "",
        GcsUri = "",
        ImportOptions = new ImportAppRequest.Types.ImportOptions(),
        IgnoreAppLock = false,
    };
    // Make the request
    Operation<ImportAppResponse, OperationMetadata> response = await agentServiceClient.ImportAppAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ImportAppResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ImportAppResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ImportAppResponse, OperationMetadata> retrievedResponse = await agentServiceClient.PollOnceImportAppAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ImportAppResponse retrievedResult = retrievedResponse.Result;
    }
    

### ImportAppAsync(string, string, string, CallSettings)
    
    
    public virtual Task<Operation<ImportAppResponse, OperationMetadata>> ImportAppAsync(string parent, string displayName, string appId, CallSettings callSettings = null)

Imports the specified app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource name with the location of the app to import.  
`displayName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The display name of the app to import.

  * If the app is created on import, and the display name is specified, the imported app will use this display name. If a conflict is detected with an existing app, a timestamp will be appended to the display name to make it unique.
  * If the app is a reimport, this field should not be set. Providing a display name during reimport will result in an INVALID_ARGUMENT error.

  
`appId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the imported app.

  * If not specified, a unique ID will be automatically assigned for the app.
  * Otherwise, the imported app will use this ID as the final component of its resource name. If an app with the same ID already exists at the specified location in the project, the content of the existing app will be replaced.

  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportAppResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ImportAppResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    string displayName = "";
    string appId = "";
    // Make the request
    Operation<ImportAppResponse, OperationMetadata> response = await agentServiceClient.ImportAppAsync(parent, displayName, appId);
    
    // Poll until the returned long-running operation is complete
    Operation<ImportAppResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ImportAppResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ImportAppResponse, OperationMetadata> retrievedResponse = await agentServiceClient.PollOnceImportAppAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ImportAppResponse retrievedResult = retrievedResponse.Result;
    }
    

### ImportAppAsync(string, string, string, CancellationToken)
    
    
    public virtual Task<Operation<ImportAppResponse, OperationMetadata>> ImportAppAsync(string parent, string displayName, string appId, CancellationToken cancellationToken)

Imports the specified app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource name with the location of the app to import.  
`displayName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The display name of the app to import.

  * If the app is created on import, and the display name is specified, the imported app will use this display name. If a conflict is detected with an existing app, a timestamp will be appended to the display name to make it unique.
  * If the app is a reimport, this field should not be set. Providing a display name during reimport will result in an INVALID_ARGUMENT error.

  
`appId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the imported app.

  * If not specified, a unique ID will be automatically assigned for the app.
  * Otherwise, the imported app will use this ID as the final component of its resource name. If an app with the same ID already exists at the specified location in the project, the content of the existing app will be replaced.

  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportAppResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ImportAppResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    string displayName = "";
    string appId = "";
    // Make the request
    Operation<ImportAppResponse, OperationMetadata> response = await agentServiceClient.ImportAppAsync(parent, displayName, appId);
    
    // Poll until the returned long-running operation is complete
    Operation<ImportAppResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ImportAppResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ImportAppResponse, OperationMetadata> retrievedResponse = await agentServiceClient.PollOnceImportAppAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ImportAppResponse retrievedResult = retrievedResponse.Result;
    }
    

### ListAgents(AppName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListAgentsResponse, Agent> ListAgents(AppName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists agents in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to list agents from.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListAgentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAgentsResponse)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)` | A pageable sequence of [Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    // Make the request
    PagedEnumerable<ListAgentsResponse, Agent> response = agentServiceClient.ListAgents(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Agent item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListAgentsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Agent item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Agent> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Agent item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAgents(ListAgentsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListAgentsResponse, Agent> ListAgents(ListAgentsRequest request, CallSettings callSettings = null)

Lists agents in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAgentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAgentsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListAgentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAgentsResponse)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)` | A pageable sequence of [Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    ListAgentsRequest request = new ListAgentsRequest
    {
        ParentAsAppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListAgentsResponse, Agent> response = agentServiceClient.ListAgents(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Agent item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListAgentsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Agent item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Agent> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Agent item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAgents(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListAgentsResponse, Agent> ListAgents(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists agents in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to list agents from.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListAgentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAgentsResponse)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)` | A pageable sequence of [Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    // Make the request
    PagedEnumerable<ListAgentsResponse, Agent> response = agentServiceClient.ListAgents(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Agent item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListAgentsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Agent item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Agent> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Agent item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAgentsAsync(AppName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListAgentsResponse, Agent> ListAgentsAsync(AppName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists agents in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to list agents from.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListAgentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAgentsResponse)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)` | A pageable asynchronous sequence of [Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    // Make the request
    PagedAsyncEnumerable<ListAgentsResponse, Agent> response = agentServiceClient.ListAgentsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Agent item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListAgentsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Agent item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Agent> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Agent item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAgentsAsync(ListAgentsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListAgentsResponse, Agent> ListAgentsAsync(ListAgentsRequest request, CallSettings callSettings = null)

Lists agents in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAgentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAgentsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListAgentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAgentsResponse)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)` | A pageable asynchronous sequence of [Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    ListAgentsRequest request = new ListAgentsRequest
    {
        ParentAsAppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListAgentsResponse, Agent> response = agentServiceClient.ListAgentsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Agent item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListAgentsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Agent item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Agent> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Agent item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAgentsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListAgentsResponse, Agent> ListAgentsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists agents in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to list agents from.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListAgentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAgentsResponse)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)` | A pageable asynchronous sequence of [Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    // Make the request
    PagedAsyncEnumerable<ListAgentsResponse, Agent> response = agentServiceClient.ListAgentsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Agent item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListAgentsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Agent item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Agent> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Agent item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAppVersions(AppName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListAppVersionsResponse, AppVersion> ListAppVersions(AppName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists all app versions in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to list app versions from.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListAppVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAppVersionsResponse)[AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion)` | A pageable sequence of [AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    // Make the request
    PagedEnumerable<ListAppVersionsResponse, AppVersion> response = agentServiceClient.ListAppVersions(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (AppVersion item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListAppVersionsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (AppVersion item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<AppVersion> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (AppVersion item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAppVersions(ListAppVersionsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListAppVersionsResponse, AppVersion> ListAppVersions(ListAppVersionsRequest request, CallSettings callSettings = null)

Lists all app versions in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAppVersionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAppVersionsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListAppVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAppVersionsResponse)[AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion)` | A pageable sequence of [AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    ListAppVersionsRequest request = new ListAppVersionsRequest
    {
        ParentAsAppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListAppVersionsResponse, AppVersion> response = agentServiceClient.ListAppVersions(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (AppVersion item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListAppVersionsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (AppVersion item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<AppVersion> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (AppVersion item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAppVersions(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListAppVersionsResponse, AppVersion> ListAppVersions(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists all app versions in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to list app versions from.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListAppVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAppVersionsResponse)[AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion)` | A pageable sequence of [AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    // Make the request
    PagedEnumerable<ListAppVersionsResponse, AppVersion> response = agentServiceClient.ListAppVersions(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (AppVersion item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListAppVersionsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (AppVersion item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<AppVersion> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (AppVersion item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAppVersionsAsync(AppName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListAppVersionsResponse, AppVersion> ListAppVersionsAsync(AppName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists all app versions in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to list app versions from.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListAppVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAppVersionsResponse)[AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion)` | A pageable asynchronous sequence of [AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    // Make the request
    PagedAsyncEnumerable<ListAppVersionsResponse, AppVersion> response = agentServiceClient.ListAppVersionsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (AppVersion item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListAppVersionsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (AppVersion item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<AppVersion> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (AppVersion item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAppVersionsAsync(ListAppVersionsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListAppVersionsResponse, AppVersion> ListAppVersionsAsync(ListAppVersionsRequest request, CallSettings callSettings = null)

Lists all app versions in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAppVersionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAppVersionsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListAppVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAppVersionsResponse)[AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion)` | A pageable asynchronous sequence of [AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    ListAppVersionsRequest request = new ListAppVersionsRequest
    {
        ParentAsAppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListAppVersionsResponse, AppVersion> response = agentServiceClient.ListAppVersionsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (AppVersion item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListAppVersionsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (AppVersion item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<AppVersion> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (AppVersion item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAppVersionsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListAppVersionsResponse, AppVersion> ListAppVersionsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists all app versions in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to list app versions from.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListAppVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAppVersionsResponse)[AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion)` | A pageable asynchronous sequence of [AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    // Make the request
    PagedAsyncEnumerable<ListAppVersionsResponse, AppVersion> response = agentServiceClient.ListAppVersionsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (AppVersion item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListAppVersionsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (AppVersion item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<AppVersion> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (AppVersion item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListApps(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListAppsResponse, App> ListApps(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists apps in the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The resource name of the location to list apps from.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListAppsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAppsResponse)[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)` | A pageable sequence of [App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListAppsResponse, App> response = agentServiceClient.ListApps(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (App item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListAppsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (App item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<App> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (App item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListApps(ListAppsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListAppsResponse, App> ListApps(ListAppsRequest request, CallSettings callSettings = null)

Lists apps in the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAppsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAppsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListAppsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAppsResponse)[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)` | A pageable sequence of [App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    ListAppsRequest request = new ListAppsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListAppsResponse, App> response = agentServiceClient.ListApps(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (App item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListAppsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (App item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<App> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (App item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListApps(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListAppsResponse, App> ListApps(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists apps in the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the location to list apps from.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListAppsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAppsResponse)[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)` | A pageable sequence of [App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListAppsResponse, App> response = agentServiceClient.ListApps(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (App item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListAppsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (App item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<App> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (App item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAppsAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListAppsResponse, App> ListAppsAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists apps in the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The resource name of the location to list apps from.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListAppsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAppsResponse)[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)` | A pageable asynchronous sequence of [App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListAppsResponse, App> response = agentServiceClient.ListAppsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (App item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListAppsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (App item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<App> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (App item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAppsAsync(ListAppsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListAppsResponse, App> ListAppsAsync(ListAppsRequest request, CallSettings callSettings = null)

Lists apps in the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAppsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAppsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListAppsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAppsResponse)[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)` | A pageable asynchronous sequence of [App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    ListAppsRequest request = new ListAppsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListAppsResponse, App> response = agentServiceClient.ListAppsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (App item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListAppsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (App item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<App> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (App item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAppsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListAppsResponse, App> ListAppsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists apps in the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the location to list apps from.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListAppsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAppsResponse)[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)` | A pageable asynchronous sequence of [App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListAppsResponse, App> response = agentServiceClient.ListAppsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (App item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListAppsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (App item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<App> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (App item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListChangelogs(AppName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListChangelogsResponse, Changelog> ListChangelogs(AppName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the changelogs of the specified app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to list changelogs from.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListChangelogsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListChangelogsResponse)[Changelog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Changelog)` | A pageable sequence of [Changelog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Changelog) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    // Make the request
    PagedEnumerable<ListChangelogsResponse, Changelog> response = agentServiceClient.ListChangelogs(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Changelog item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListChangelogsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Changelog item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Changelog> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Changelog item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListChangelogs(ListChangelogsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListChangelogsResponse, Changelog> ListChangelogs(ListChangelogsRequest request, CallSettings callSettings = null)

Lists the changelogs of the specified app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListChangelogsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListChangelogsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListChangelogsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListChangelogsResponse)[Changelog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Changelog)` | A pageable sequence of [Changelog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Changelog) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    ListChangelogsRequest request = new ListChangelogsRequest
    {
        ParentAsAppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListChangelogsResponse, Changelog> response = agentServiceClient.ListChangelogs(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Changelog item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListChangelogsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Changelog item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Changelog> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Changelog item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListChangelogs(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListChangelogsResponse, Changelog> ListChangelogs(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the changelogs of the specified app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to list changelogs from.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListChangelogsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListChangelogsResponse)[Changelog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Changelog)` | A pageable sequence of [Changelog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Changelog) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    // Make the request
    PagedEnumerable<ListChangelogsResponse, Changelog> response = agentServiceClient.ListChangelogs(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Changelog item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListChangelogsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Changelog item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Changelog> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Changelog item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListChangelogsAsync(AppName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListChangelogsResponse, Changelog> ListChangelogsAsync(AppName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the changelogs of the specified app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to list changelogs from.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListChangelogsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListChangelogsResponse)[Changelog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Changelog)` | A pageable asynchronous sequence of [Changelog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Changelog) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    // Make the request
    PagedAsyncEnumerable<ListChangelogsResponse, Changelog> response = agentServiceClient.ListChangelogsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Changelog item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListChangelogsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Changelog item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Changelog> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Changelog item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListChangelogsAsync(ListChangelogsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListChangelogsResponse, Changelog> ListChangelogsAsync(ListChangelogsRequest request, CallSettings callSettings = null)

Lists the changelogs of the specified app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListChangelogsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListChangelogsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListChangelogsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListChangelogsResponse)[Changelog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Changelog)` | A pageable asynchronous sequence of [Changelog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Changelog) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    ListChangelogsRequest request = new ListChangelogsRequest
    {
        ParentAsAppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListChangelogsResponse, Changelog> response = agentServiceClient.ListChangelogsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Changelog item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListChangelogsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Changelog item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Changelog> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Changelog item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListChangelogsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListChangelogsResponse, Changelog> ListChangelogsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the changelogs of the specified app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to list changelogs from.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListChangelogsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListChangelogsResponse)[Changelog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Changelog)` | A pageable asynchronous sequence of [Changelog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Changelog) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    // Make the request
    PagedAsyncEnumerable<ListChangelogsResponse, Changelog> response = agentServiceClient.ListChangelogsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Changelog item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListChangelogsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Changelog item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Changelog> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Changelog item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListConversations(AppName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListConversationsResponse, Conversation> ListConversations(AppName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists conversations in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to list conversations from.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListConversationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListConversationsResponse)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation)` | A pageable sequence of [Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    // Make the request
    PagedEnumerable<ListConversationsResponse, Conversation> response = agentServiceClient.ListConversations(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Conversation item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListConversationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Conversation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Conversation> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Conversation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListConversations(ListConversationsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListConversationsResponse, Conversation> ListConversations(ListConversationsRequest request, CallSettings callSettings = null)

Lists conversations in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListConversationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListConversationsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListConversationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListConversationsResponse)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation)` | A pageable sequence of [Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    ListConversationsRequest request = new ListConversationsRequest
    {
        ParentAsAppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
        Filter = "",
        Source = Conversation.Types.Source.Unspecified,
        Sources =
        {
            Conversation.Types.Source.Unspecified,
        },
    };
    // Make the request
    PagedEnumerable<ListConversationsResponse, Conversation> response = agentServiceClient.ListConversations(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Conversation item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListConversationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Conversation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Conversation> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Conversation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListConversations(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListConversationsResponse, Conversation> ListConversations(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists conversations in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to list conversations from.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListConversationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListConversationsResponse)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation)` | A pageable sequence of [Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    // Make the request
    PagedEnumerable<ListConversationsResponse, Conversation> response = agentServiceClient.ListConversations(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Conversation item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListConversationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Conversation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Conversation> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Conversation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListConversationsAsync(AppName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListConversationsResponse, Conversation> ListConversationsAsync(AppName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists conversations in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to list conversations from.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListConversationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListConversationsResponse)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation)` | A pageable asynchronous sequence of [Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    // Make the request
    PagedAsyncEnumerable<ListConversationsResponse, Conversation> response = agentServiceClient.ListConversationsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Conversation item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListConversationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Conversation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Conversation> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Conversation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListConversationsAsync(ListConversationsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListConversationsResponse, Conversation> ListConversationsAsync(ListConversationsRequest request, CallSettings callSettings = null)

Lists conversations in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListConversationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListConversationsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListConversationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListConversationsResponse)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation)` | A pageable asynchronous sequence of [Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    ListConversationsRequest request = new ListConversationsRequest
    {
        ParentAsAppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
        Filter = "",
        Source = Conversation.Types.Source.Unspecified,
        Sources =
        {
            Conversation.Types.Source.Unspecified,
        },
    };
    // Make the request
    PagedAsyncEnumerable<ListConversationsResponse, Conversation> response = agentServiceClient.ListConversationsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Conversation item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListConversationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Conversation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Conversation> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Conversation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListConversationsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListConversationsResponse, Conversation> ListConversationsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists conversations in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to list conversations from.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListConversationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListConversationsResponse)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation)` | A pageable asynchronous sequence of [Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    // Make the request
    PagedAsyncEnumerable<ListConversationsResponse, Conversation> response = agentServiceClient.ListConversationsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Conversation item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListConversationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Conversation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Conversation> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Conversation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDeployments(AppName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListDeploymentsResponse, Deployment> ListDeployments(AppName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists deployments in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The parent app. Format: `projects/{project}/locations/{location}/apps/{app}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListDeploymentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListDeploymentsResponse)[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)` | A pageable sequence of [Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    // Make the request
    PagedEnumerable<ListDeploymentsResponse, Deployment> response = agentServiceClient.ListDeployments(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Deployment item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListDeploymentsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Deployment item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Deployment> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Deployment item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDeployments(ListDeploymentsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListDeploymentsResponse, Deployment> ListDeployments(ListDeploymentsRequest request, CallSettings callSettings = null)

Lists deployments in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDeploymentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListDeploymentsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListDeploymentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListDeploymentsResponse)[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)` | A pageable sequence of [Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    ListDeploymentsRequest request = new ListDeploymentsRequest
    {
        ParentAsAppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListDeploymentsResponse, Deployment> response = agentServiceClient.ListDeployments(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Deployment item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListDeploymentsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Deployment item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Deployment> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Deployment item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDeployments(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListDeploymentsResponse, Deployment> ListDeployments(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists deployments in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent app. Format: `projects/{project}/locations/{location}/apps/{app}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListDeploymentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListDeploymentsResponse)[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)` | A pageable sequence of [Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    // Make the request
    PagedEnumerable<ListDeploymentsResponse, Deployment> response = agentServiceClient.ListDeployments(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Deployment item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListDeploymentsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Deployment item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Deployment> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Deployment item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDeploymentsAsync(AppName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListDeploymentsResponse, Deployment> ListDeploymentsAsync(AppName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists deployments in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The parent app. Format: `projects/{project}/locations/{location}/apps/{app}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListDeploymentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListDeploymentsResponse)[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)` | A pageable asynchronous sequence of [Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    // Make the request
    PagedAsyncEnumerable<ListDeploymentsResponse, Deployment> response = agentServiceClient.ListDeploymentsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Deployment item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListDeploymentsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Deployment item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Deployment> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Deployment item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDeploymentsAsync(ListDeploymentsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListDeploymentsResponse, Deployment> ListDeploymentsAsync(ListDeploymentsRequest request, CallSettings callSettings = null)

Lists deployments in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDeploymentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListDeploymentsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListDeploymentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListDeploymentsResponse)[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)` | A pageable asynchronous sequence of [Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    ListDeploymentsRequest request = new ListDeploymentsRequest
    {
        ParentAsAppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListDeploymentsResponse, Deployment> response = agentServiceClient.ListDeploymentsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Deployment item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListDeploymentsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Deployment item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Deployment> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Deployment item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDeploymentsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListDeploymentsResponse, Deployment> ListDeploymentsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists deployments in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent app. Format: `projects/{project}/locations/{location}/apps/{app}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListDeploymentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListDeploymentsResponse)[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)` | A pageable asynchronous sequence of [Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    // Make the request
    PagedAsyncEnumerable<ListDeploymentsResponse, Deployment> response = agentServiceClient.ListDeploymentsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Deployment item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListDeploymentsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Deployment item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Deployment> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Deployment item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListExamples(AppName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListExamplesResponse, Example> ListExamples(AppName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists examples in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to list examples from.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListExamplesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListExamplesResponse)[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)` | A pageable sequence of [Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    // Make the request
    PagedEnumerable<ListExamplesResponse, Example> response = agentServiceClient.ListExamples(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Example item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListExamplesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Example item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Example> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Example item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListExamples(ListExamplesRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListExamplesResponse, Example> ListExamples(ListExamplesRequest request, CallSettings callSettings = null)

Lists examples in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListExamplesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListExamplesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListExamplesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListExamplesResponse)[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)` | A pageable sequence of [Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    ListExamplesRequest request = new ListExamplesRequest
    {
        ParentAsAppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListExamplesResponse, Example> response = agentServiceClient.ListExamples(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Example item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListExamplesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Example item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Example> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Example item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListExamples(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListExamplesResponse, Example> ListExamples(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists examples in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to list examples from.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListExamplesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListExamplesResponse)[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)` | A pageable sequence of [Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    // Make the request
    PagedEnumerable<ListExamplesResponse, Example> response = agentServiceClient.ListExamples(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Example item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListExamplesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Example item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Example> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Example item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListExamplesAsync(AppName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListExamplesResponse, Example> ListExamplesAsync(AppName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists examples in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to list examples from.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListExamplesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListExamplesResponse)[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)` | A pageable asynchronous sequence of [Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    // Make the request
    PagedAsyncEnumerable<ListExamplesResponse, Example> response = agentServiceClient.ListExamplesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Example item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListExamplesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Example item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Example> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Example item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListExamplesAsync(ListExamplesRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListExamplesResponse, Example> ListExamplesAsync(ListExamplesRequest request, CallSettings callSettings = null)

Lists examples in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListExamplesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListExamplesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListExamplesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListExamplesResponse)[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)` | A pageable asynchronous sequence of [Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    ListExamplesRequest request = new ListExamplesRequest
    {
        ParentAsAppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListExamplesResponse, Example> response = agentServiceClient.ListExamplesAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Example item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListExamplesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Example item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Example> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Example item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListExamplesAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListExamplesResponse, Example> ListExamplesAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists examples in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to list examples from.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListExamplesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListExamplesResponse)[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)` | A pageable asynchronous sequence of [Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    // Make the request
    PagedAsyncEnumerable<ListExamplesResponse, Example> response = agentServiceClient.ListExamplesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Example item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListExamplesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Example item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Example> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Example item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListGuardrails(AppName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListGuardrailsResponse, Guardrail> ListGuardrails(AppName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists guardrails in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to list guardrails from.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListGuardrailsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListGuardrailsResponse)[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)` | A pageable sequence of [Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    // Make the request
    PagedEnumerable<ListGuardrailsResponse, Guardrail> response = agentServiceClient.ListGuardrails(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Guardrail item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListGuardrailsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Guardrail item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Guardrail> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Guardrail item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListGuardrails(ListGuardrailsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListGuardrailsResponse, Guardrail> ListGuardrails(ListGuardrailsRequest request, CallSettings callSettings = null)

Lists guardrails in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGuardrailsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListGuardrailsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListGuardrailsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListGuardrailsResponse)[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)` | A pageable sequence of [Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    ListGuardrailsRequest request = new ListGuardrailsRequest
    {
        ParentAsAppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListGuardrailsResponse, Guardrail> response = agentServiceClient.ListGuardrails(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Guardrail item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListGuardrailsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Guardrail item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Guardrail> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Guardrail item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListGuardrails(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListGuardrailsResponse, Guardrail> ListGuardrails(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists guardrails in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to list guardrails from.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListGuardrailsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListGuardrailsResponse)[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)` | A pageable sequence of [Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    // Make the request
    PagedEnumerable<ListGuardrailsResponse, Guardrail> response = agentServiceClient.ListGuardrails(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Guardrail item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListGuardrailsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Guardrail item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Guardrail> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Guardrail item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListGuardrailsAsync(AppName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListGuardrailsResponse, Guardrail> ListGuardrailsAsync(AppName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists guardrails in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to list guardrails from.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListGuardrailsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListGuardrailsResponse)[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)` | A pageable asynchronous sequence of [Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    // Make the request
    PagedAsyncEnumerable<ListGuardrailsResponse, Guardrail> response = agentServiceClient.ListGuardrailsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Guardrail item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListGuardrailsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Guardrail item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Guardrail> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Guardrail item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListGuardrailsAsync(ListGuardrailsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListGuardrailsResponse, Guardrail> ListGuardrailsAsync(ListGuardrailsRequest request, CallSettings callSettings = null)

Lists guardrails in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGuardrailsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListGuardrailsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListGuardrailsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListGuardrailsResponse)[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)` | A pageable asynchronous sequence of [Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    ListGuardrailsRequest request = new ListGuardrailsRequest
    {
        ParentAsAppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListGuardrailsResponse, Guardrail> response = agentServiceClient.ListGuardrailsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Guardrail item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListGuardrailsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Guardrail item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Guardrail> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Guardrail item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListGuardrailsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListGuardrailsResponse, Guardrail> ListGuardrailsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists guardrails in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to list guardrails from.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListGuardrailsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListGuardrailsResponse)[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)` | A pageable asynchronous sequence of [Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    // Make the request
    PagedAsyncEnumerable<ListGuardrailsResponse, Guardrail> response = agentServiceClient.ListGuardrailsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Guardrail item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListGuardrailsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Guardrail item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Guardrail> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Guardrail item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListTools(AppName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListToolsResponse, Tool> ListTools(AppName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists tools in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to list tools from.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListToolsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListToolsResponse)[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)` | A pageable sequence of [Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    // Make the request
    PagedEnumerable<ListToolsResponse, Tool> response = agentServiceClient.ListTools(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Tool item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListToolsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Tool item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Tool> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Tool item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListTools(ListToolsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListToolsResponse, Tool> ListTools(ListToolsRequest request, CallSettings callSettings = null)

Lists tools in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListToolsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListToolsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListToolsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListToolsResponse)[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)` | A pageable sequence of [Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    ListToolsRequest request = new ListToolsRequest
    {
        ParentAsAppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListToolsResponse, Tool> response = agentServiceClient.ListTools(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Tool item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListToolsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Tool item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Tool> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Tool item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListTools(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListToolsResponse, Tool> ListTools(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists tools in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to list tools from.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListToolsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListToolsResponse)[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)` | A pageable sequence of [Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    // Make the request
    PagedEnumerable<ListToolsResponse, Tool> response = agentServiceClient.ListTools(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Tool item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListToolsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Tool item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Tool> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Tool item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListToolsAsync(AppName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListToolsResponse, Tool> ListToolsAsync(AppName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists tools in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to list tools from.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListToolsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListToolsResponse)[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)` | A pageable asynchronous sequence of [Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    // Make the request
    PagedAsyncEnumerable<ListToolsResponse, Tool> response = agentServiceClient.ListToolsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Tool item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListToolsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Tool item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Tool> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Tool item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListToolsAsync(ListToolsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListToolsResponse, Tool> ListToolsAsync(ListToolsRequest request, CallSettings callSettings = null)

Lists tools in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListToolsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListToolsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListToolsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListToolsResponse)[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)` | A pageable asynchronous sequence of [Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    ListToolsRequest request = new ListToolsRequest
    {
        ParentAsAppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListToolsResponse, Tool> response = agentServiceClient.ListToolsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Tool item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListToolsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Tool item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Tool> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Tool item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListToolsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListToolsResponse, Tool> ListToolsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists tools in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to list tools from.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListToolsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListToolsResponse)[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)` | A pageable asynchronous sequence of [Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    // Make the request
    PagedAsyncEnumerable<ListToolsResponse, Tool> response = agentServiceClient.ListToolsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Tool item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListToolsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Tool item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Tool> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Tool item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListToolsets(AppName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListToolsetsResponse, Toolset> ListToolsets(AppName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists toolsets in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to list toolsets from.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListToolsetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListToolsetsResponse)[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)` | A pageable sequence of [Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    // Make the request
    PagedEnumerable<ListToolsetsResponse, Toolset> response = agentServiceClient.ListToolsets(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Toolset item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListToolsetsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Toolset item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Toolset> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Toolset item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListToolsets(ListToolsetsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListToolsetsResponse, Toolset> ListToolsets(ListToolsetsRequest request, CallSettings callSettings = null)

Lists toolsets in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListToolsetsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListToolsetsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListToolsetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListToolsetsResponse)[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)` | A pageable sequence of [Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    ListToolsetsRequest request = new ListToolsetsRequest
    {
        ParentAsAppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListToolsetsResponse, Toolset> response = agentServiceClient.ListToolsets(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Toolset item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListToolsetsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Toolset item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Toolset> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Toolset item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListToolsets(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListToolsetsResponse, Toolset> ListToolsets(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists toolsets in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to list toolsets from.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListToolsetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListToolsetsResponse)[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)` | A pageable sequence of [Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    // Make the request
    PagedEnumerable<ListToolsetsResponse, Toolset> response = agentServiceClient.ListToolsets(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Toolset item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListToolsetsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Toolset item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Toolset> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Toolset item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListToolsetsAsync(AppName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListToolsetsResponse, Toolset> ListToolsetsAsync(AppName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists toolsets in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)`  
Required. The resource name of the app to list toolsets from.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListToolsetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListToolsetsResponse)[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)` | A pageable asynchronous sequence of [Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AppName parent = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]");
    // Make the request
    PagedAsyncEnumerable<ListToolsetsResponse, Toolset> response = agentServiceClient.ListToolsetsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Toolset item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListToolsetsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Toolset item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Toolset> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Toolset item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListToolsetsAsync(ListToolsetsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListToolsetsResponse, Toolset> ListToolsetsAsync(ListToolsetsRequest request, CallSettings callSettings = null)

Lists toolsets in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListToolsetsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListToolsetsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListToolsetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListToolsetsResponse)[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)` | A pageable asynchronous sequence of [Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    ListToolsetsRequest request = new ListToolsetsRequest
    {
        ParentAsAppName = AppName.FromProjectLocationApp("[PROJECT]", "[LOCATION]", "[APP]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListToolsetsResponse, Toolset> response = agentServiceClient.ListToolsetsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Toolset item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListToolsetsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Toolset item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Toolset> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Toolset item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListToolsetsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListToolsetsResponse, Toolset> ListToolsetsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists toolsets in the given app.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app to list toolsets from.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListToolsetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListToolsetsResponse)[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)` | A pageable asynchronous sequence of [Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset) resources.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]";
    // Make the request
    PagedAsyncEnumerable<ListToolsetsResponse, Toolset> response = agentServiceClient.ListToolsetsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Toolset item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListToolsetsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Toolset item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Toolset> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Toolset item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### PollOnceBatchDeleteConversations(string, CallSettings)
    
    
    public virtual Operation<BatchDeleteConversationsResponse, OperationMetadata> PollOnceBatchDeleteConversations(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `BatchDeleteConversations`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchDeleteConversationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.BatchDeleteConversationsResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceBatchDeleteConversationsAsync(string, CallSettings)
    
    
    public virtual Task<Operation<BatchDeleteConversationsResponse, OperationMetadata>> PollOnceBatchDeleteConversationsAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `BatchDeleteConversations`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchDeleteConversationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.BatchDeleteConversationsResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceCreateApp(string, CallSettings)
    
    
    public virtual Operation<App, OperationMetadata> PollOnceCreateApp(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateApp`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceCreateAppAsync(string, CallSettings)
    
    
    public virtual Task<Operation<App, OperationMetadata>> PollOnceCreateAppAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateApp`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteApp(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> PollOnceDeleteApp(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteApp`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteAppAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> PollOnceDeleteAppAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteApp`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceExportApp(string, CallSettings)
    
    
    public virtual Operation<ExportAppResponse, OperationMetadata> PollOnceExportApp(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `ExportApp`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportAppResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExportAppResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceExportAppAsync(string, CallSettings)
    
    
    public virtual Task<Operation<ExportAppResponse, OperationMetadata>> PollOnceExportAppAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `ExportApp`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportAppResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExportAppResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceGenerateAppResource(string, CallSettings)
    
    
    public virtual Operation<GenerateAppResourceResponse, GenerateAppResourceOperationMetadata> PollOnceGenerateAppResource(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `GenerateAppResource` .

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[GenerateAppResourceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceResponse)[GenerateAppResourceOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceOperationMetadata)` | The result of polling the operation.  
  
### PollOnceGenerateAppResourceAsync(string, CallSettings)
    
    
    public virtual Task<Operation<GenerateAppResourceResponse, GenerateAppResourceOperationMetadata>> PollOnceGenerateAppResourceAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `GenerateAppResource`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[GenerateAppResourceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceResponse)[GenerateAppResourceOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceOperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceImportApp(string, CallSettings)
    
    
    public virtual Operation<ImportAppResponse, OperationMetadata> PollOnceImportApp(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `ImportApp`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportAppResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ImportAppResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceImportAppAsync(string, CallSettings)
    
    
    public virtual Task<Operation<ImportAppResponse, OperationMetadata>> PollOnceImportAppAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `ImportApp`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportAppResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ImportAppResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceRestoreAppVersion(string, CallSettings)
    
    
    public virtual Operation<RestoreAppVersionResponse, OperationMetadata> PollOnceRestoreAppVersion(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `RestoreAppVersion` .

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RestoreAppVersionResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.RestoreAppVersionResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceRestoreAppVersionAsync(string, CallSettings)
    
    
    public virtual Task<Operation<RestoreAppVersionResponse, OperationMetadata>> PollOnceRestoreAppVersionAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `RestoreAppVersion`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RestoreAppVersionResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.RestoreAppVersionResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### RestoreAppVersion(AppVersionName, CallSettings)
    
    
    public virtual Operation<RestoreAppVersionResponse, OperationMetadata> RestoreAppVersion(AppVersionName name, CallSettings callSettings = null)

Restores the specified app version. This will create a new app version from the current draft app and overwrite the current draft with the specified app version.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AppVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersionName)`  
Required. The resource name of the app version to restore.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RestoreAppVersionResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.RestoreAppVersionResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    AppVersionName name = AppVersionName.FromProjectLocationAppVersion("[PROJECT]", "[LOCATION]", "[APP]", "[VERSION]");
    // Make the request
    Operation<RestoreAppVersionResponse, OperationMetadata> response = agentServiceClient.RestoreAppVersion(name);
    
    // Poll until the returned long-running operation is complete
    Operation<RestoreAppVersionResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    RestoreAppVersionResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<RestoreAppVersionResponse, OperationMetadata> retrievedResponse = agentServiceClient.PollOnceRestoreAppVersion(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        RestoreAppVersionResponse retrievedResult = retrievedResponse.Result;
    }
    

### RestoreAppVersion(RestoreAppVersionRequest, CallSettings)
    
    
    public virtual Operation<RestoreAppVersionResponse, OperationMetadata> RestoreAppVersion(RestoreAppVersionRequest request, CallSettings callSettings = null)

Restores the specified app version. This will create a new app version from the current draft app and overwrite the current draft with the specified app version.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RestoreAppVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.RestoreAppVersionRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RestoreAppVersionResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.RestoreAppVersionResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    RestoreAppVersionRequest request = new RestoreAppVersionRequest
    {
        AppVersionName = AppVersionName.FromProjectLocationAppVersion("[PROJECT]", "[LOCATION]", "[APP]", "[VERSION]"),
    };
    // Make the request
    Operation<RestoreAppVersionResponse, OperationMetadata> response = agentServiceClient.RestoreAppVersion(request);
    
    // Poll until the returned long-running operation is complete
    Operation<RestoreAppVersionResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    RestoreAppVersionResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<RestoreAppVersionResponse, OperationMetadata> retrievedResponse = agentServiceClient.PollOnceRestoreAppVersion(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        RestoreAppVersionResponse retrievedResult = retrievedResponse.Result;
    }
    

### RestoreAppVersion(string, CallSettings)
    
    
    public virtual Operation<RestoreAppVersionResponse, OperationMetadata> RestoreAppVersion(string name, CallSettings callSettings = null)

Restores the specified app version. This will create a new app version from the current draft app and overwrite the current draft with the specified app version.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app version to restore.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RestoreAppVersionResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.RestoreAppVersionResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/versions/[VERSION]";
    // Make the request
    Operation<RestoreAppVersionResponse, OperationMetadata> response = agentServiceClient.RestoreAppVersion(name);
    
    // Poll until the returned long-running operation is complete
    Operation<RestoreAppVersionResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    RestoreAppVersionResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<RestoreAppVersionResponse, OperationMetadata> retrievedResponse = agentServiceClient.PollOnceRestoreAppVersion(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        RestoreAppVersionResponse retrievedResult = retrievedResponse.Result;
    }
    

### RestoreAppVersionAsync(AppVersionName, CallSettings)
    
    
    public virtual Task<Operation<RestoreAppVersionResponse, OperationMetadata>> RestoreAppVersionAsync(AppVersionName name, CallSettings callSettings = null)

Restores the specified app version. This will create a new app version from the current draft app and overwrite the current draft with the specified app version.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AppVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersionName)`  
Required. The resource name of the app version to restore.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RestoreAppVersionResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.RestoreAppVersionResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AppVersionName name = AppVersionName.FromProjectLocationAppVersion("[PROJECT]", "[LOCATION]", "[APP]", "[VERSION]");
    // Make the request
    Operation<RestoreAppVersionResponse, OperationMetadata> response = await agentServiceClient.RestoreAppVersionAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<RestoreAppVersionResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    RestoreAppVersionResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<RestoreAppVersionResponse, OperationMetadata> retrievedResponse = await agentServiceClient.PollOnceRestoreAppVersionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        RestoreAppVersionResponse retrievedResult = retrievedResponse.Result;
    }
    

### RestoreAppVersionAsync(AppVersionName, CancellationToken)
    
    
    public virtual Task<Operation<RestoreAppVersionResponse, OperationMetadata>> RestoreAppVersionAsync(AppVersionName name, CancellationToken cancellationToken)

Restores the specified app version. This will create a new app version from the current draft app and overwrite the current draft with the specified app version.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AppVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersionName)`  
Required. The resource name of the app version to restore.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RestoreAppVersionResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.RestoreAppVersionResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    AppVersionName name = AppVersionName.FromProjectLocationAppVersion("[PROJECT]", "[LOCATION]", "[APP]", "[VERSION]");
    // Make the request
    Operation<RestoreAppVersionResponse, OperationMetadata> response = await agentServiceClient.RestoreAppVersionAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<RestoreAppVersionResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    RestoreAppVersionResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<RestoreAppVersionResponse, OperationMetadata> retrievedResponse = await agentServiceClient.PollOnceRestoreAppVersionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        RestoreAppVersionResponse retrievedResult = retrievedResponse.Result;
    }
    

### RestoreAppVersionAsync(RestoreAppVersionRequest, CallSettings)
    
    
    public virtual Task<Operation<RestoreAppVersionResponse, OperationMetadata>> RestoreAppVersionAsync(RestoreAppVersionRequest request, CallSettings callSettings = null)

Restores the specified app version. This will create a new app version from the current draft app and overwrite the current draft with the specified app version.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RestoreAppVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.RestoreAppVersionRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RestoreAppVersionResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.RestoreAppVersionResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    RestoreAppVersionRequest request = new RestoreAppVersionRequest
    {
        AppVersionName = AppVersionName.FromProjectLocationAppVersion("[PROJECT]", "[LOCATION]", "[APP]", "[VERSION]"),
    };
    // Make the request
    Operation<RestoreAppVersionResponse, OperationMetadata> response = await agentServiceClient.RestoreAppVersionAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<RestoreAppVersionResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    RestoreAppVersionResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<RestoreAppVersionResponse, OperationMetadata> retrievedResponse = await agentServiceClient.PollOnceRestoreAppVersionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        RestoreAppVersionResponse retrievedResult = retrievedResponse.Result;
    }
    

### RestoreAppVersionAsync(RestoreAppVersionRequest, CancellationToken)
    
    
    public virtual Task<Operation<RestoreAppVersionResponse, OperationMetadata>> RestoreAppVersionAsync(RestoreAppVersionRequest request, CancellationToken cancellationToken)

Restores the specified app version. This will create a new app version from the current draft app and overwrite the current draft with the specified app version.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RestoreAppVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.RestoreAppVersionRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RestoreAppVersionResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.RestoreAppVersionResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    RestoreAppVersionRequest request = new RestoreAppVersionRequest
    {
        AppVersionName = AppVersionName.FromProjectLocationAppVersion("[PROJECT]", "[LOCATION]", "[APP]", "[VERSION]"),
    };
    // Make the request
    Operation<RestoreAppVersionResponse, OperationMetadata> response = await agentServiceClient.RestoreAppVersionAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<RestoreAppVersionResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    RestoreAppVersionResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<RestoreAppVersionResponse, OperationMetadata> retrievedResponse = await agentServiceClient.PollOnceRestoreAppVersionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        RestoreAppVersionResponse retrievedResult = retrievedResponse.Result;
    }
    

### RestoreAppVersionAsync(string, CallSettings)
    
    
    public virtual Task<Operation<RestoreAppVersionResponse, OperationMetadata>> RestoreAppVersionAsync(string name, CallSettings callSettings = null)

Restores the specified app version. This will create a new app version from the current draft app and overwrite the current draft with the specified app version.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app version to restore.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RestoreAppVersionResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.RestoreAppVersionResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/versions/[VERSION]";
    // Make the request
    Operation<RestoreAppVersionResponse, OperationMetadata> response = await agentServiceClient.RestoreAppVersionAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<RestoreAppVersionResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    RestoreAppVersionResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<RestoreAppVersionResponse, OperationMetadata> retrievedResponse = await agentServiceClient.PollOnceRestoreAppVersionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        RestoreAppVersionResponse retrievedResult = retrievedResponse.Result;
    }
    

### RestoreAppVersionAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<RestoreAppVersionResponse, OperationMetadata>> RestoreAppVersionAsync(string name, CancellationToken cancellationToken)

Restores the specified app version. This will create a new app version from the current draft app and overwrite the current draft with the specified app version.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the app version to restore.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RestoreAppVersionResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.RestoreAppVersionResponse)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/apps/[APP]/versions/[VERSION]";
    // Make the request
    Operation<RestoreAppVersionResponse, OperationMetadata> response = await agentServiceClient.RestoreAppVersionAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<RestoreAppVersionResponse, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    RestoreAppVersionResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<RestoreAppVersionResponse, OperationMetadata> retrievedResponse = await agentServiceClient.PollOnceRestoreAppVersionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        RestoreAppVersionResponse retrievedResult = retrievedResponse.Result;
    }
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentServiceClient#Google_Cloud_Ces_V1Beta_AgentServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentServiceClient#Google_Cloud_Ces_V1Beta_AgentServiceClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentServiceClient#Google_Cloud_Ces_V1Beta_AgentServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentServiceClient#Google_Cloud_Ces_V1Beta_AgentServiceClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### UpdateAgent(Agent, FieldMask, CallSettings)
    
    
    public virtual Agent UpdateAgent(Agent agent, FieldMask updateMask, CallSettings callSettings = null)

Updates the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`agent` | `[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)`  
Required. The agent to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to control which fields get updated. If the mask is not present, all fields will be updated.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    Agent agent = new Agent();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Agent response = agentServiceClient.UpdateAgent(agent, updateMask);
    

### UpdateAgent(UpdateAgentRequest, CallSettings)
    
    
    public virtual Agent UpdateAgent(UpdateAgentRequest request, CallSettings callSettings = null)

Updates the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateAgentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    UpdateAgentRequest request = new UpdateAgentRequest
    {
        Agent = new Agent(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Agent response = agentServiceClient.UpdateAgent(request);
    

### UpdateAgentAsync(Agent, FieldMask, CallSettings)
    
    
    public virtual Task<Agent> UpdateAgentAsync(Agent agent, FieldMask updateMask, CallSettings callSettings = null)

Updates the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`agent` | `[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)`  
Required. The agent to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to control which fields get updated. If the mask is not present, all fields will be updated.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    Agent agent = new Agent();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Agent response = await agentServiceClient.UpdateAgentAsync(agent, updateMask);
    

### UpdateAgentAsync(Agent, FieldMask, CancellationToken)
    
    
    public virtual Task<Agent> UpdateAgentAsync(Agent agent, FieldMask updateMask, CancellationToken cancellationToken)

Updates the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`agent` | `[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)`  
Required. The agent to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to control which fields get updated. If the mask is not present, all fields will be updated.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    Agent agent = new Agent();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Agent response = await agentServiceClient.UpdateAgentAsync(agent, updateMask);
    

### UpdateAgentAsync(UpdateAgentRequest, CallSettings)
    
    
    public virtual Task<Agent> UpdateAgentAsync(UpdateAgentRequest request, CallSettings callSettings = null)

Updates the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateAgentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateAgentRequest request = new UpdateAgentRequest
    {
        Agent = new Agent(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Agent response = await agentServiceClient.UpdateAgentAsync(request);
    

### UpdateAgentAsync(UpdateAgentRequest, CancellationToken)
    
    
    public virtual Task<Agent> UpdateAgentAsync(UpdateAgentRequest request, CancellationToken cancellationToken)

Updates the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateAgentRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateAgentRequest request = new UpdateAgentRequest
    {
        Agent = new Agent(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Agent response = await agentServiceClient.UpdateAgentAsync(request);
    

### UpdateApp(App, FieldMask, CallSettings)
    
    
    public virtual App UpdateApp(App app, FieldMask updateMask, CallSettings callSettings = null)

Updates the specified app.

**Parameters**  
---  
**Name** | **Description**  
`app` | `[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)`  
Required. The app to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to control which fields get updated. If the mask is not present, all fields will be updated.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    App app = new App();
    FieldMask updateMask = new FieldMask();
    // Make the request
    App response = agentServiceClient.UpdateApp(app, updateMask);
    

### UpdateApp(UpdateAppRequest, CallSettings)
    
    
    public virtual App UpdateApp(UpdateAppRequest request, CallSettings callSettings = null)

Updates the specified app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateAppRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    UpdateAppRequest request = new UpdateAppRequest
    {
        App = new App(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    App response = agentServiceClient.UpdateApp(request);
    

### UpdateAppAsync(App, FieldMask, CallSettings)
    
    
    public virtual Task<App> UpdateAppAsync(App app, FieldMask updateMask, CallSettings callSettings = null)

Updates the specified app.

**Parameters**  
---  
**Name** | **Description**  
`app` | `[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)`  
Required. The app to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to control which fields get updated. If the mask is not present, all fields will be updated.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    App app = new App();
    FieldMask updateMask = new FieldMask();
    // Make the request
    App response = await agentServiceClient.UpdateAppAsync(app, updateMask);
    

### UpdateAppAsync(App, FieldMask, CancellationToken)
    
    
    public virtual Task<App> UpdateAppAsync(App app, FieldMask updateMask, CancellationToken cancellationToken)

Updates the specified app.

**Parameters**  
---  
**Name** | **Description**  
`app` | `[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)`  
Required. The app to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to control which fields get updated. If the mask is not present, all fields will be updated.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    App app = new App();
    FieldMask updateMask = new FieldMask();
    // Make the request
    App response = await agentServiceClient.UpdateAppAsync(app, updateMask);
    

### UpdateAppAsync(UpdateAppRequest, CallSettings)
    
    
    public virtual Task<App> UpdateAppAsync(UpdateAppRequest request, CallSettings callSettings = null)

Updates the specified app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateAppRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateAppRequest request = new UpdateAppRequest
    {
        App = new App(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    App response = await agentServiceClient.UpdateAppAsync(request);
    

### UpdateAppAsync(UpdateAppRequest, CancellationToken)
    
    
    public virtual Task<App> UpdateAppAsync(UpdateAppRequest request, CancellationToken cancellationToken)

Updates the specified app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateAppRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateAppRequest request = new UpdateAppRequest
    {
        App = new App(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    App response = await agentServiceClient.UpdateAppAsync(request);
    

### UpdateDeployment(Deployment, FieldMask, CallSettings)
    
    
    public virtual Deployment UpdateDeployment(Deployment deployment, FieldMask updateMask, CallSettings callSettings = null)

Updates the specified deployment.

**Parameters**  
---  
**Name** | **Description**  
`deployment` | `[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)`  
Required. The deployment to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. The list of fields to update.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    Deployment deployment = new Deployment();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Deployment response = agentServiceClient.UpdateDeployment(deployment, updateMask);
    

### UpdateDeployment(UpdateDeploymentRequest, CallSettings)
    
    
    public virtual Deployment UpdateDeployment(UpdateDeploymentRequest request, CallSettings callSettings = null)

Updates the specified deployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateDeploymentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    UpdateDeploymentRequest request = new UpdateDeploymentRequest
    {
        Deployment = new Deployment(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Deployment response = agentServiceClient.UpdateDeployment(request);
    

### UpdateDeploymentAsync(Deployment, FieldMask, CallSettings)
    
    
    public virtual Task<Deployment> UpdateDeploymentAsync(Deployment deployment, FieldMask updateMask, CallSettings callSettings = null)

Updates the specified deployment.

**Parameters**  
---  
**Name** | **Description**  
`deployment` | `[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)`  
Required. The deployment to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. The list of fields to update.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    Deployment deployment = new Deployment();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Deployment response = await agentServiceClient.UpdateDeploymentAsync(deployment, updateMask);
    

### UpdateDeploymentAsync(Deployment, FieldMask, CancellationToken)
    
    
    public virtual Task<Deployment> UpdateDeploymentAsync(Deployment deployment, FieldMask updateMask, CancellationToken cancellationToken)

Updates the specified deployment.

**Parameters**  
---  
**Name** | **Description**  
`deployment` | `[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)`  
Required. The deployment to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. The list of fields to update.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    Deployment deployment = new Deployment();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Deployment response = await agentServiceClient.UpdateDeploymentAsync(deployment, updateMask);
    

### UpdateDeploymentAsync(UpdateDeploymentRequest, CallSettings)
    
    
    public virtual Task<Deployment> UpdateDeploymentAsync(UpdateDeploymentRequest request, CallSettings callSettings = null)

Updates the specified deployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateDeploymentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateDeploymentRequest request = new UpdateDeploymentRequest
    {
        Deployment = new Deployment(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Deployment response = await agentServiceClient.UpdateDeploymentAsync(request);
    

### UpdateDeploymentAsync(UpdateDeploymentRequest, CancellationToken)
    
    
    public virtual Task<Deployment> UpdateDeploymentAsync(UpdateDeploymentRequest request, CancellationToken cancellationToken)

Updates the specified deployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateDeploymentRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateDeploymentRequest request = new UpdateDeploymentRequest
    {
        Deployment = new Deployment(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Deployment response = await agentServiceClient.UpdateDeploymentAsync(request);
    

### UpdateExample(Example, FieldMask, CallSettings)
    
    
    public virtual Example UpdateExample(Example example, FieldMask updateMask, CallSettings callSettings = null)

Updates the specified example.

**Parameters**  
---  
**Name** | **Description**  
`example` | `[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)`  
Required. The example to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to control which fields get updated. If the mask is not present, all fields will be updated.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    Example example = new Example();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Example response = agentServiceClient.UpdateExample(example, updateMask);
    

### UpdateExample(UpdateExampleRequest, CallSettings)
    
    
    public virtual Example UpdateExample(UpdateExampleRequest request, CallSettings callSettings = null)

Updates the specified example.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateExampleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateExampleRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    UpdateExampleRequest request = new UpdateExampleRequest
    {
        Example = new Example(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Example response = agentServiceClient.UpdateExample(request);
    

### UpdateExampleAsync(Example, FieldMask, CallSettings)
    
    
    public virtual Task<Example> UpdateExampleAsync(Example example, FieldMask updateMask, CallSettings callSettings = null)

Updates the specified example.

**Parameters**  
---  
**Name** | **Description**  
`example` | `[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)`  
Required. The example to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to control which fields get updated. If the mask is not present, all fields will be updated.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    Example example = new Example();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Example response = await agentServiceClient.UpdateExampleAsync(example, updateMask);
    

### UpdateExampleAsync(Example, FieldMask, CancellationToken)
    
    
    public virtual Task<Example> UpdateExampleAsync(Example example, FieldMask updateMask, CancellationToken cancellationToken)

Updates the specified example.

**Parameters**  
---  
**Name** | **Description**  
`example` | `[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)`  
Required. The example to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to control which fields get updated. If the mask is not present, all fields will be updated.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    Example example = new Example();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Example response = await agentServiceClient.UpdateExampleAsync(example, updateMask);
    

### UpdateExampleAsync(UpdateExampleRequest, CallSettings)
    
    
    public virtual Task<Example> UpdateExampleAsync(UpdateExampleRequest request, CallSettings callSettings = null)

Updates the specified example.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateExampleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateExampleRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateExampleRequest request = new UpdateExampleRequest
    {
        Example = new Example(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Example response = await agentServiceClient.UpdateExampleAsync(request);
    

### UpdateExampleAsync(UpdateExampleRequest, CancellationToken)
    
    
    public virtual Task<Example> UpdateExampleAsync(UpdateExampleRequest request, CancellationToken cancellationToken)

Updates the specified example.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateExampleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateExampleRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateExampleRequest request = new UpdateExampleRequest
    {
        Example = new Example(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Example response = await agentServiceClient.UpdateExampleAsync(request);
    

### UpdateGuardrail(Guardrail, FieldMask, CallSettings)
    
    
    public virtual Guardrail UpdateGuardrail(Guardrail guardrail, FieldMask updateMask, CallSettings callSettings = null)

Updates the specified guardrail.

**Parameters**  
---  
**Name** | **Description**  
`guardrail` | `[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)`  
Required. The guardrail to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to control which fields get updated. If the mask is not present, all fields will be updated.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    Guardrail guardrail = new Guardrail();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Guardrail response = agentServiceClient.UpdateGuardrail(guardrail, updateMask);
    

### UpdateGuardrail(UpdateGuardrailRequest, CallSettings)
    
    
    public virtual Guardrail UpdateGuardrail(UpdateGuardrailRequest request, CallSettings callSettings = null)

Updates the specified guardrail.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateGuardrailRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateGuardrailRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    UpdateGuardrailRequest request = new UpdateGuardrailRequest
    {
        Guardrail = new Guardrail(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Guardrail response = agentServiceClient.UpdateGuardrail(request);
    

### UpdateGuardrailAsync(Guardrail, FieldMask, CallSettings)
    
    
    public virtual Task<Guardrail> UpdateGuardrailAsync(Guardrail guardrail, FieldMask updateMask, CallSettings callSettings = null)

Updates the specified guardrail.

**Parameters**  
---  
**Name** | **Description**  
`guardrail` | `[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)`  
Required. The guardrail to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to control which fields get updated. If the mask is not present, all fields will be updated.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    Guardrail guardrail = new Guardrail();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Guardrail response = await agentServiceClient.UpdateGuardrailAsync(guardrail, updateMask);
    

### UpdateGuardrailAsync(Guardrail, FieldMask, CancellationToken)
    
    
    public virtual Task<Guardrail> UpdateGuardrailAsync(Guardrail guardrail, FieldMask updateMask, CancellationToken cancellationToken)

Updates the specified guardrail.

**Parameters**  
---  
**Name** | **Description**  
`guardrail` | `[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)`  
Required. The guardrail to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to control which fields get updated. If the mask is not present, all fields will be updated.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    Guardrail guardrail = new Guardrail();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Guardrail response = await agentServiceClient.UpdateGuardrailAsync(guardrail, updateMask);
    

### UpdateGuardrailAsync(UpdateGuardrailRequest, CallSettings)
    
    
    public virtual Task<Guardrail> UpdateGuardrailAsync(UpdateGuardrailRequest request, CallSettings callSettings = null)

Updates the specified guardrail.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateGuardrailRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateGuardrailRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateGuardrailRequest request = new UpdateGuardrailRequest
    {
        Guardrail = new Guardrail(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Guardrail response = await agentServiceClient.UpdateGuardrailAsync(request);
    

### UpdateGuardrailAsync(UpdateGuardrailRequest, CancellationToken)
    
    
    public virtual Task<Guardrail> UpdateGuardrailAsync(UpdateGuardrailRequest request, CancellationToken cancellationToken)

Updates the specified guardrail.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateGuardrailRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateGuardrailRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateGuardrailRequest request = new UpdateGuardrailRequest
    {
        Guardrail = new Guardrail(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Guardrail response = await agentServiceClient.UpdateGuardrailAsync(request);
    

### UpdateSecuritySettings(SecuritySettings, FieldMask, CallSettings)
    
    
    public virtual SecuritySettings UpdateSecuritySettings(SecuritySettings securitySettings, FieldMask updateMask, CallSettings callSettings = null)

Updates the security settings for the project and location.

**Parameters**  
---  
**Name** | **Description**  
`securitySettings` | `[SecuritySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SecuritySettings)`  
Required. The security settings to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to control which fields get updated. If the mask is not present, all fields will be updated.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[SecuritySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SecuritySettings)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    SecuritySettings securitySettings = new SecuritySettings();
    FieldMask updateMask = new FieldMask();
    // Make the request
    SecuritySettings response = agentServiceClient.UpdateSecuritySettings(securitySettings, updateMask);
    

### UpdateSecuritySettings(UpdateSecuritySettingsRequest, CallSettings)
    
    
    public virtual SecuritySettings UpdateSecuritySettings(UpdateSecuritySettingsRequest request, CallSettings callSettings = null)

Updates the security settings for the project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSecuritySettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateSecuritySettingsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[SecuritySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SecuritySettings)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    UpdateSecuritySettingsRequest request = new UpdateSecuritySettingsRequest
    {
        SecuritySettings = new SecuritySettings(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    SecuritySettings response = agentServiceClient.UpdateSecuritySettings(request);
    

### UpdateSecuritySettingsAsync(SecuritySettings, FieldMask, CallSettings)
    
    
    public virtual Task<SecuritySettings> UpdateSecuritySettingsAsync(SecuritySettings securitySettings, FieldMask updateMask, CallSettings callSettings = null)

Updates the security settings for the project and location.

**Parameters**  
---  
**Name** | **Description**  
`securitySettings` | `[SecuritySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SecuritySettings)`  
Required. The security settings to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to control which fields get updated. If the mask is not present, all fields will be updated.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SecuritySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SecuritySettings)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    SecuritySettings securitySettings = new SecuritySettings();
    FieldMask updateMask = new FieldMask();
    // Make the request
    SecuritySettings response = await agentServiceClient.UpdateSecuritySettingsAsync(securitySettings, updateMask);
    

### UpdateSecuritySettingsAsync(SecuritySettings, FieldMask, CancellationToken)
    
    
    public virtual Task<SecuritySettings> UpdateSecuritySettingsAsync(SecuritySettings securitySettings, FieldMask updateMask, CancellationToken cancellationToken)

Updates the security settings for the project and location.

**Parameters**  
---  
**Name** | **Description**  
`securitySettings` | `[SecuritySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SecuritySettings)`  
Required. The security settings to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to control which fields get updated. If the mask is not present, all fields will be updated.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SecuritySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SecuritySettings)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    SecuritySettings securitySettings = new SecuritySettings();
    FieldMask updateMask = new FieldMask();
    // Make the request
    SecuritySettings response = await agentServiceClient.UpdateSecuritySettingsAsync(securitySettings, updateMask);
    

### UpdateSecuritySettingsAsync(UpdateSecuritySettingsRequest, CallSettings)
    
    
    public virtual Task<SecuritySettings> UpdateSecuritySettingsAsync(UpdateSecuritySettingsRequest request, CallSettings callSettings = null)

Updates the security settings for the project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSecuritySettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateSecuritySettingsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SecuritySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SecuritySettings)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateSecuritySettingsRequest request = new UpdateSecuritySettingsRequest
    {
        SecuritySettings = new SecuritySettings(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    SecuritySettings response = await agentServiceClient.UpdateSecuritySettingsAsync(request);
    

### UpdateSecuritySettingsAsync(UpdateSecuritySettingsRequest, CancellationToken)
    
    
    public virtual Task<SecuritySettings> UpdateSecuritySettingsAsync(UpdateSecuritySettingsRequest request, CancellationToken cancellationToken)

Updates the security settings for the project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSecuritySettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateSecuritySettingsRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SecuritySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SecuritySettings)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateSecuritySettingsRequest request = new UpdateSecuritySettingsRequest
    {
        SecuritySettings = new SecuritySettings(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    SecuritySettings response = await agentServiceClient.UpdateSecuritySettingsAsync(request);
    

### UpdateTool(Tool, FieldMask, CallSettings)
    
    
    public virtual Tool UpdateTool(Tool tool, FieldMask updateMask, CallSettings callSettings = null)

Updates the specified tool.

**Parameters**  
---  
**Name** | **Description**  
`tool` | `[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)`  
Required. The tool to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to control which fields get updated. If the mask is not present, all fields will be updated.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    Tool tool = new Tool();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Tool response = agentServiceClient.UpdateTool(tool, updateMask);
    

### UpdateTool(UpdateToolRequest, CallSettings)
    
    
    public virtual Tool UpdateTool(UpdateToolRequest request, CallSettings callSettings = null)

Updates the specified tool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateToolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateToolRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    UpdateToolRequest request = new UpdateToolRequest
    {
        Tool = new Tool(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Tool response = agentServiceClient.UpdateTool(request);
    

### UpdateToolAsync(Tool, FieldMask, CallSettings)
    
    
    public virtual Task<Tool> UpdateToolAsync(Tool tool, FieldMask updateMask, CallSettings callSettings = null)

Updates the specified tool.

**Parameters**  
---  
**Name** | **Description**  
`tool` | `[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)`  
Required. The tool to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to control which fields get updated. If the mask is not present, all fields will be updated.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    Tool tool = new Tool();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Tool response = await agentServiceClient.UpdateToolAsync(tool, updateMask);
    

### UpdateToolAsync(Tool, FieldMask, CancellationToken)
    
    
    public virtual Task<Tool> UpdateToolAsync(Tool tool, FieldMask updateMask, CancellationToken cancellationToken)

Updates the specified tool.

**Parameters**  
---  
**Name** | **Description**  
`tool` | `[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)`  
Required. The tool to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to control which fields get updated. If the mask is not present, all fields will be updated.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    Tool tool = new Tool();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Tool response = await agentServiceClient.UpdateToolAsync(tool, updateMask);
    

### UpdateToolAsync(UpdateToolRequest, CallSettings)
    
    
    public virtual Task<Tool> UpdateToolAsync(UpdateToolRequest request, CallSettings callSettings = null)

Updates the specified tool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateToolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateToolRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateToolRequest request = new UpdateToolRequest
    {
        Tool = new Tool(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Tool response = await agentServiceClient.UpdateToolAsync(request);
    

### UpdateToolAsync(UpdateToolRequest, CancellationToken)
    
    
    public virtual Task<Tool> UpdateToolAsync(UpdateToolRequest request, CancellationToken cancellationToken)

Updates the specified tool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateToolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateToolRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateToolRequest request = new UpdateToolRequest
    {
        Tool = new Tool(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Tool response = await agentServiceClient.UpdateToolAsync(request);
    

### UpdateToolset(Toolset, FieldMask, CallSettings)
    
    
    public virtual Toolset UpdateToolset(Toolset toolset, FieldMask updateMask, CallSettings callSettings = null)

Updates the specified toolset.

**Parameters**  
---  
**Name** | **Description**  
`toolset` | `[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)`  
Required. The toolset to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to control which fields get updated. If the mask is not present, all fields will be updated.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    Toolset toolset = new Toolset();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Toolset response = agentServiceClient.UpdateToolset(toolset, updateMask);
    

### UpdateToolset(UpdateToolsetRequest, CallSettings)
    
    
    public virtual Toolset UpdateToolset(UpdateToolsetRequest request, CallSettings callSettings = null)

Updates the specified toolset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateToolsetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateToolsetRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = AgentServiceClient.Create();
    // Initialize request argument(s)
    UpdateToolsetRequest request = new UpdateToolsetRequest
    {
        Toolset = new Toolset(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Toolset response = agentServiceClient.UpdateToolset(request);
    

### UpdateToolsetAsync(Toolset, FieldMask, CallSettings)
    
    
    public virtual Task<Toolset> UpdateToolsetAsync(Toolset toolset, FieldMask updateMask, CallSettings callSettings = null)

Updates the specified toolset.

**Parameters**  
---  
**Name** | **Description**  
`toolset` | `[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)`  
Required. The toolset to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to control which fields get updated. If the mask is not present, all fields will be updated.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    Toolset toolset = new Toolset();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Toolset response = await agentServiceClient.UpdateToolsetAsync(toolset, updateMask);
    

### UpdateToolsetAsync(Toolset, FieldMask, CancellationToken)
    
    
    public virtual Task<Toolset> UpdateToolsetAsync(Toolset toolset, FieldMask updateMask, CancellationToken cancellationToken)

Updates the specified toolset.

**Parameters**  
---  
**Name** | **Description**  
`toolset` | `[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)`  
Required. The toolset to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to control which fields get updated. If the mask is not present, all fields will be updated.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    Toolset toolset = new Toolset();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Toolset response = await agentServiceClient.UpdateToolsetAsync(toolset, updateMask);
    

### UpdateToolsetAsync(UpdateToolsetRequest, CallSettings)
    
    
    public virtual Task<Toolset> UpdateToolsetAsync(UpdateToolsetRequest request, CallSettings callSettings = null)

Updates the specified toolset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateToolsetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateToolsetRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateToolsetRequest request = new UpdateToolsetRequest
    {
        Toolset = new Toolset(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Toolset response = await agentServiceClient.UpdateToolsetAsync(request);
    

### UpdateToolsetAsync(UpdateToolsetRequest, CancellationToken)
    
    
    public virtual Task<Toolset> UpdateToolsetAsync(UpdateToolsetRequest request, CancellationToken cancellationToken)

Updates the specified toolset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateToolsetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateToolsetRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentServiceClient agentServiceClient = await AgentServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateToolsetRequest request = new UpdateToolsetRequest
    {
        Toolset = new Toolset(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Toolset response = await agentServiceClient.UpdateToolsetAsync(request);
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
