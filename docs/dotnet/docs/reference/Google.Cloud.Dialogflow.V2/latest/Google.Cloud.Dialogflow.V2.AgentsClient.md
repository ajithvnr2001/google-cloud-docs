---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentsClient
title: Google Cloud Dialogflow v2 API - Class AgentsClient (4.33.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:58:03.924448+00:00
---

# Google Cloud Dialogflow v2 API - Class AgentsClient (4.33.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Dialogflow v2 API - Class AgentsClient (4.33.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.33.0 (latest)  4.32.0  4.31.0  4.30.0  4.29.0  4.28.0  4.27.0  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.16.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.0  4.8.0  4.7.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0 
    
    
    public abstract class AgentsClient

Reference documentation and code samples for the Google Cloud Dialogflow v2 API class AgentsClient.

Agents client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AgentsClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[AgentsClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentsClientImpl)

## Namespace

[Google.Cloud.Dialogflow.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2)

## Assembly

Google.Cloud.Dialogflow.V2.dll

## Remarks

Service for managing [Agents][google.cloud.dialogflow.v2.Agent].

## Properties 

### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the Agents service, which is a host of "dialogflow.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default Agents scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default Agents scopes are:

  * <https://www.googleapis.com/auth/cloud-platform>
  * <https://www.googleapis.com/auth/dialogflow>



### ExportAgentOperationsClient
    
    
    public virtual OperationsClient ExportAgentOperationsClient { get; }

The long-running operations client for `ExportAgent`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### GrpcClient
    
    
    public virtual Agents.AgentsClient GrpcClient { get; }

The underlying gRPC Agents client

**Property Value**  
---  
**Type** | **Description**  
`[Agents](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.Agents)[AgentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.Agents.AgentsClient)` |   
  
### ImportAgentOperationsClient
    
    
    public virtual OperationsClient ImportAgentOperationsClient { get; }

The long-running operations client for `ImportAgent`.

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
  
### RestoreAgentOperationsClient
    
    
    public virtual OperationsClient RestoreAgentOperationsClient { get; }

The long-running operations client for `RestoreAgent`.

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
  
### TrainAgentOperationsClient
    
    
    public virtual OperationsClient TrainAgentOperationsClient { get; }

The long-running operations client for `TrainAgent`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
## Methods 

### Create()
    
    
    public static AgentsClient Create()

Synchronously creates a [AgentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentsClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [AgentsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentsClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[AgentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentsClient)` | The created [AgentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentsClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<AgentsClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [AgentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentsClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [AgentsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentsClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AgentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentsClient)` | The task representing the created [AgentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentsClient).  
  
### DeleteAgent(LocationName, CallSettings)
    
    
    public virtual void DeleteAgent(LocationName parent, CallSettings callSettings = null)

Deletes the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The project that the agent to delete is associated with. Format: `projects/<Project ID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = AgentsClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    agentsClient.DeleteAgent(parent);
    

### DeleteAgent(ProjectName, CallSettings)
    
    
    public virtual void DeleteAgent(ProjectName parent, CallSettings callSettings = null)

Deletes the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)`  
Required. The project that the agent to delete is associated with. Format: `projects/<Project ID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = AgentsClient.Create();
    // Initialize request argument(s)
    ProjectName parent = ProjectName.FromProject("[PROJECT]");
    // Make the request
    agentsClient.DeleteAgent(parent);
    

### DeleteAgent(DeleteAgentRequest, CallSettings)
    
    
    public virtual void DeleteAgent(DeleteAgentRequest request, CallSettings callSettings = null)

Deletes the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.DeleteAgentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = AgentsClient.Create();
    // Initialize request argument(s)
    DeleteAgentRequest request = new DeleteAgentRequest
    {
        ParentAsProjectName = ProjectName.FromProject("[PROJECT]"),
    };
    // Make the request
    agentsClient.DeleteAgent(request);
    

### DeleteAgent(string, CallSettings)
    
    
    public virtual void DeleteAgent(string parent, CallSettings callSettings = null)

Deletes the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The project that the agent to delete is associated with. Format: `projects/<Project ID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = AgentsClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]";
    // Make the request
    agentsClient.DeleteAgent(parent);
    

### DeleteAgentAsync(LocationName, CallSettings)
    
    
    public virtual Task DeleteAgentAsync(LocationName parent, CallSettings callSettings = null)

Deletes the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The project that the agent to delete is associated with. Format: `projects/<Project ID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    await agentsClient.DeleteAgentAsync(parent);
    

### DeleteAgentAsync(LocationName, CancellationToken)
    
    
    public virtual Task DeleteAgentAsync(LocationName parent, CancellationToken cancellationToken)

Deletes the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The project that the agent to delete is associated with. Format: `projects/<Project ID>`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    await agentsClient.DeleteAgentAsync(parent);
    

### DeleteAgentAsync(ProjectName, CallSettings)
    
    
    public virtual Task DeleteAgentAsync(ProjectName parent, CallSettings callSettings = null)

Deletes the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)`  
Required. The project that the agent to delete is associated with. Format: `projects/<Project ID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    ProjectName parent = ProjectName.FromProject("[PROJECT]");
    // Make the request
    await agentsClient.DeleteAgentAsync(parent);
    

### DeleteAgentAsync(ProjectName, CancellationToken)
    
    
    public virtual Task DeleteAgentAsync(ProjectName parent, CancellationToken cancellationToken)

Deletes the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)`  
Required. The project that the agent to delete is associated with. Format: `projects/<Project ID>`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    ProjectName parent = ProjectName.FromProject("[PROJECT]");
    // Make the request
    await agentsClient.DeleteAgentAsync(parent);
    

### DeleteAgentAsync(DeleteAgentRequest, CallSettings)
    
    
    public virtual Task DeleteAgentAsync(DeleteAgentRequest request, CallSettings callSettings = null)

Deletes the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.DeleteAgentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    DeleteAgentRequest request = new DeleteAgentRequest
    {
        ParentAsProjectName = ProjectName.FromProject("[PROJECT]"),
    };
    // Make the request
    await agentsClient.DeleteAgentAsync(request);
    

### DeleteAgentAsync(DeleteAgentRequest, CancellationToken)
    
    
    public virtual Task DeleteAgentAsync(DeleteAgentRequest request, CancellationToken cancellationToken)

Deletes the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.DeleteAgentRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    DeleteAgentRequest request = new DeleteAgentRequest
    {
        ParentAsProjectName = ProjectName.FromProject("[PROJECT]"),
    };
    // Make the request
    await agentsClient.DeleteAgentAsync(request);
    

### DeleteAgentAsync(string, CallSettings)
    
    
    public virtual Task DeleteAgentAsync(string parent, CallSettings callSettings = null)

Deletes the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The project that the agent to delete is associated with. Format: `projects/<Project ID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]";
    // Make the request
    await agentsClient.DeleteAgentAsync(parent);
    

### DeleteAgentAsync(string, CancellationToken)
    
    
    public virtual Task DeleteAgentAsync(string parent, CancellationToken cancellationToken)

Deletes the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The project that the agent to delete is associated with. Format: `projects/<Project ID>`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]";
    // Make the request
    await agentsClient.DeleteAgentAsync(parent);
    

### ExportAgent(LocationName, CallSettings)
    
    
    public virtual Operation<ExportAgentResponse, Struct> ExportAgent(LocationName parent, CallSettings callSettings = null)

Exports the specified agent to a ZIP file.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
  * `response`: [ExportAgentResponse][google.cloud.dialogflow.v2.ExportAgentResponse]



**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The project that the agent to export is associated with. Format: `projects/<Project ID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportAgentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ExportAgentResponse)[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = AgentsClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    Operation<ExportAgentResponse, Struct> response = agentsClient.ExportAgent(parent);
    
    // Poll until the returned long-running operation is complete
    Operation<ExportAgentResponse, Struct> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    ExportAgentResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ExportAgentResponse, Struct> retrievedResponse = agentsClient.PollOnceExportAgent(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ExportAgentResponse retrievedResult = retrievedResponse.Result;
    }
    

### ExportAgent(ProjectName, CallSettings)
    
    
    public virtual Operation<ExportAgentResponse, Struct> ExportAgent(ProjectName parent, CallSettings callSettings = null)

Exports the specified agent to a ZIP file.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
  * `response`: [ExportAgentResponse][google.cloud.dialogflow.v2.ExportAgentResponse]



**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)`  
Required. The project that the agent to export is associated with. Format: `projects/<Project ID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportAgentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ExportAgentResponse)[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = AgentsClient.Create();
    // Initialize request argument(s)
    ProjectName parent = ProjectName.FromProject("[PROJECT]");
    // Make the request
    Operation<ExportAgentResponse, Struct> response = agentsClient.ExportAgent(parent);
    
    // Poll until the returned long-running operation is complete
    Operation<ExportAgentResponse, Struct> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    ExportAgentResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ExportAgentResponse, Struct> retrievedResponse = agentsClient.PollOnceExportAgent(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ExportAgentResponse retrievedResult = retrievedResponse.Result;
    }
    

### ExportAgent(ExportAgentRequest, CallSettings)
    
    
    public virtual Operation<ExportAgentResponse, Struct> ExportAgent(ExportAgentRequest request, CallSettings callSettings = null)

Exports the specified agent to a ZIP file.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
  * `response`: [ExportAgentResponse][google.cloud.dialogflow.v2.ExportAgentResponse]



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ExportAgentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportAgentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ExportAgentResponse)[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = AgentsClient.Create();
    // Initialize request argument(s)
    ExportAgentRequest request = new ExportAgentRequest
    {
        ParentAsProjectName = ProjectName.FromProject("[PROJECT]"),
        AgentUri = "",
    };
    // Make the request
    Operation<ExportAgentResponse, Struct> response = agentsClient.ExportAgent(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ExportAgentResponse, Struct> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    ExportAgentResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ExportAgentResponse, Struct> retrievedResponse = agentsClient.PollOnceExportAgent(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ExportAgentResponse retrievedResult = retrievedResponse.Result;
    }
    

### ExportAgent(string, CallSettings)
    
    
    public virtual Operation<ExportAgentResponse, Struct> ExportAgent(string parent, CallSettings callSettings = null)

Exports the specified agent to a ZIP file.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
  * `response`: [ExportAgentResponse][google.cloud.dialogflow.v2.ExportAgentResponse]



**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The project that the agent to export is associated with. Format: `projects/<Project ID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportAgentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ExportAgentResponse)[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = AgentsClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]";
    // Make the request
    Operation<ExportAgentResponse, Struct> response = agentsClient.ExportAgent(parent);
    
    // Poll until the returned long-running operation is complete
    Operation<ExportAgentResponse, Struct> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    ExportAgentResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ExportAgentResponse, Struct> retrievedResponse = agentsClient.PollOnceExportAgent(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ExportAgentResponse retrievedResult = retrievedResponse.Result;
    }
    

### ExportAgentAsync(LocationName, CallSettings)
    
    
    public virtual Task<Operation<ExportAgentResponse, Struct>> ExportAgentAsync(LocationName parent, CallSettings callSettings = null)

Exports the specified agent to a ZIP file.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
  * `response`: [ExportAgentResponse][google.cloud.dialogflow.v2.ExportAgentResponse]



**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The project that the agent to export is associated with. Format: `projects/<Project ID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportAgentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ExportAgentResponse)[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    Operation<ExportAgentResponse, Struct> response = await agentsClient.ExportAgentAsync(parent);
    
    // Poll until the returned long-running operation is complete
    Operation<ExportAgentResponse, Struct> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ExportAgentResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ExportAgentResponse, Struct> retrievedResponse = await agentsClient.PollOnceExportAgentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ExportAgentResponse retrievedResult = retrievedResponse.Result;
    }
    

### ExportAgentAsync(LocationName, CancellationToken)
    
    
    public virtual Task<Operation<ExportAgentResponse, Struct>> ExportAgentAsync(LocationName parent, CancellationToken cancellationToken)

Exports the specified agent to a ZIP file.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
  * `response`: [ExportAgentResponse][google.cloud.dialogflow.v2.ExportAgentResponse]



**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The project that the agent to export is associated with. Format: `projects/<Project ID>`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportAgentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ExportAgentResponse)[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    Operation<ExportAgentResponse, Struct> response = await agentsClient.ExportAgentAsync(parent);
    
    // Poll until the returned long-running operation is complete
    Operation<ExportAgentResponse, Struct> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ExportAgentResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ExportAgentResponse, Struct> retrievedResponse = await agentsClient.PollOnceExportAgentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ExportAgentResponse retrievedResult = retrievedResponse.Result;
    }
    

### ExportAgentAsync(ProjectName, CallSettings)
    
    
    public virtual Task<Operation<ExportAgentResponse, Struct>> ExportAgentAsync(ProjectName parent, CallSettings callSettings = null)

Exports the specified agent to a ZIP file.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
  * `response`: [ExportAgentResponse][google.cloud.dialogflow.v2.ExportAgentResponse]



**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)`  
Required. The project that the agent to export is associated with. Format: `projects/<Project ID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportAgentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ExportAgentResponse)[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    ProjectName parent = ProjectName.FromProject("[PROJECT]");
    // Make the request
    Operation<ExportAgentResponse, Struct> response = await agentsClient.ExportAgentAsync(parent);
    
    // Poll until the returned long-running operation is complete
    Operation<ExportAgentResponse, Struct> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ExportAgentResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ExportAgentResponse, Struct> retrievedResponse = await agentsClient.PollOnceExportAgentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ExportAgentResponse retrievedResult = retrievedResponse.Result;
    }
    

### ExportAgentAsync(ProjectName, CancellationToken)
    
    
    public virtual Task<Operation<ExportAgentResponse, Struct>> ExportAgentAsync(ProjectName parent, CancellationToken cancellationToken)

Exports the specified agent to a ZIP file.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
  * `response`: [ExportAgentResponse][google.cloud.dialogflow.v2.ExportAgentResponse]



**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)`  
Required. The project that the agent to export is associated with. Format: `projects/<Project ID>`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportAgentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ExportAgentResponse)[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    ProjectName parent = ProjectName.FromProject("[PROJECT]");
    // Make the request
    Operation<ExportAgentResponse, Struct> response = await agentsClient.ExportAgentAsync(parent);
    
    // Poll until the returned long-running operation is complete
    Operation<ExportAgentResponse, Struct> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ExportAgentResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ExportAgentResponse, Struct> retrievedResponse = await agentsClient.PollOnceExportAgentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ExportAgentResponse retrievedResult = retrievedResponse.Result;
    }
    

### ExportAgentAsync(ExportAgentRequest, CallSettings)
    
    
    public virtual Task<Operation<ExportAgentResponse, Struct>> ExportAgentAsync(ExportAgentRequest request, CallSettings callSettings = null)

Exports the specified agent to a ZIP file.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
  * `response`: [ExportAgentResponse][google.cloud.dialogflow.v2.ExportAgentResponse]



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ExportAgentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportAgentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ExportAgentResponse)[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    ExportAgentRequest request = new ExportAgentRequest
    {
        ParentAsProjectName = ProjectName.FromProject("[PROJECT]"),
        AgentUri = "",
    };
    // Make the request
    Operation<ExportAgentResponse, Struct> response = await agentsClient.ExportAgentAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ExportAgentResponse, Struct> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ExportAgentResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ExportAgentResponse, Struct> retrievedResponse = await agentsClient.PollOnceExportAgentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ExportAgentResponse retrievedResult = retrievedResponse.Result;
    }
    

### ExportAgentAsync(ExportAgentRequest, CancellationToken)
    
    
    public virtual Task<Operation<ExportAgentResponse, Struct>> ExportAgentAsync(ExportAgentRequest request, CancellationToken cancellationToken)

Exports the specified agent to a ZIP file.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
  * `response`: [ExportAgentResponse][google.cloud.dialogflow.v2.ExportAgentResponse]



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ExportAgentRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportAgentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ExportAgentResponse)[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    ExportAgentRequest request = new ExportAgentRequest
    {
        ParentAsProjectName = ProjectName.FromProject("[PROJECT]"),
        AgentUri = "",
    };
    // Make the request
    Operation<ExportAgentResponse, Struct> response = await agentsClient.ExportAgentAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ExportAgentResponse, Struct> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ExportAgentResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ExportAgentResponse, Struct> retrievedResponse = await agentsClient.PollOnceExportAgentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ExportAgentResponse retrievedResult = retrievedResponse.Result;
    }
    

### ExportAgentAsync(string, CallSettings)
    
    
    public virtual Task<Operation<ExportAgentResponse, Struct>> ExportAgentAsync(string parent, CallSettings callSettings = null)

Exports the specified agent to a ZIP file.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
  * `response`: [ExportAgentResponse][google.cloud.dialogflow.v2.ExportAgentResponse]



**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The project that the agent to export is associated with. Format: `projects/<Project ID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportAgentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ExportAgentResponse)[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]";
    // Make the request
    Operation<ExportAgentResponse, Struct> response = await agentsClient.ExportAgentAsync(parent);
    
    // Poll until the returned long-running operation is complete
    Operation<ExportAgentResponse, Struct> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ExportAgentResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ExportAgentResponse, Struct> retrievedResponse = await agentsClient.PollOnceExportAgentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ExportAgentResponse retrievedResult = retrievedResponse.Result;
    }
    

### ExportAgentAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<ExportAgentResponse, Struct>> ExportAgentAsync(string parent, CancellationToken cancellationToken)

Exports the specified agent to a ZIP file.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
  * `response`: [ExportAgentResponse][google.cloud.dialogflow.v2.ExportAgentResponse]



**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The project that the agent to export is associated with. Format: `projects/<Project ID>`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportAgentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ExportAgentResponse)[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]";
    // Make the request
    Operation<ExportAgentResponse, Struct> response = await agentsClient.ExportAgentAsync(parent);
    
    // Poll until the returned long-running operation is complete
    Operation<ExportAgentResponse, Struct> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ExportAgentResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ExportAgentResponse, Struct> retrievedResponse = await agentsClient.PollOnceExportAgentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ExportAgentResponse retrievedResult = retrievedResponse.Result;
    }
    

### GetAgent(LocationName, CallSettings)
    
    
    public virtual Agent GetAgent(LocationName parent, CallSettings callSettings = null)

Retrieves the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The project that the agent to fetch is associated with. Format: `projects/<Project ID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.Agent)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = AgentsClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    Agent response = agentsClient.GetAgent(parent);
    

### GetAgent(ProjectName, CallSettings)
    
    
    public virtual Agent GetAgent(ProjectName parent, CallSettings callSettings = null)

Retrieves the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)`  
Required. The project that the agent to fetch is associated with. Format: `projects/<Project ID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.Agent)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = AgentsClient.Create();
    // Initialize request argument(s)
    ProjectName parent = ProjectName.FromProject("[PROJECT]");
    // Make the request
    Agent response = agentsClient.GetAgent(parent);
    

### GetAgent(GetAgentRequest, CallSettings)
    
    
    public virtual Agent GetAgent(GetAgentRequest request, CallSettings callSettings = null)

Retrieves the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.GetAgentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.Agent)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = AgentsClient.Create();
    // Initialize request argument(s)
    GetAgentRequest request = new GetAgentRequest
    {
        ParentAsProjectName = ProjectName.FromProject("[PROJECT]"),
    };
    // Make the request
    Agent response = agentsClient.GetAgent(request);
    

### GetAgent(string, CallSettings)
    
    
    public virtual Agent GetAgent(string parent, CallSettings callSettings = null)

Retrieves the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The project that the agent to fetch is associated with. Format: `projects/<Project ID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.Agent)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = AgentsClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]";
    // Make the request
    Agent response = agentsClient.GetAgent(parent);
    

### GetAgentAsync(LocationName, CallSettings)
    
    
    public virtual Task<Agent> GetAgentAsync(LocationName parent, CallSettings callSettings = null)

Retrieves the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The project that the agent to fetch is associated with. Format: `projects/<Project ID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.Agent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    Agent response = await agentsClient.GetAgentAsync(parent);
    

### GetAgentAsync(LocationName, CancellationToken)
    
    
    public virtual Task<Agent> GetAgentAsync(LocationName parent, CancellationToken cancellationToken)

Retrieves the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The project that the agent to fetch is associated with. Format: `projects/<Project ID>`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.Agent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    Agent response = await agentsClient.GetAgentAsync(parent);
    

### GetAgentAsync(ProjectName, CallSettings)
    
    
    public virtual Task<Agent> GetAgentAsync(ProjectName parent, CallSettings callSettings = null)

Retrieves the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)`  
Required. The project that the agent to fetch is associated with. Format: `projects/<Project ID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.Agent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    ProjectName parent = ProjectName.FromProject("[PROJECT]");
    // Make the request
    Agent response = await agentsClient.GetAgentAsync(parent);
    

### GetAgentAsync(ProjectName, CancellationToken)
    
    
    public virtual Task<Agent> GetAgentAsync(ProjectName parent, CancellationToken cancellationToken)

Retrieves the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)`  
Required. The project that the agent to fetch is associated with. Format: `projects/<Project ID>`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.Agent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    ProjectName parent = ProjectName.FromProject("[PROJECT]");
    // Make the request
    Agent response = await agentsClient.GetAgentAsync(parent);
    

### GetAgentAsync(GetAgentRequest, CallSettings)
    
    
    public virtual Task<Agent> GetAgentAsync(GetAgentRequest request, CallSettings callSettings = null)

Retrieves the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.GetAgentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.Agent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    GetAgentRequest request = new GetAgentRequest
    {
        ParentAsProjectName = ProjectName.FromProject("[PROJECT]"),
    };
    // Make the request
    Agent response = await agentsClient.GetAgentAsync(request);
    

### GetAgentAsync(GetAgentRequest, CancellationToken)
    
    
    public virtual Task<Agent> GetAgentAsync(GetAgentRequest request, CancellationToken cancellationToken)

Retrieves the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.GetAgentRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.Agent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    GetAgentRequest request = new GetAgentRequest
    {
        ParentAsProjectName = ProjectName.FromProject("[PROJECT]"),
    };
    // Make the request
    Agent response = await agentsClient.GetAgentAsync(request);
    

### GetAgentAsync(string, CallSettings)
    
    
    public virtual Task<Agent> GetAgentAsync(string parent, CallSettings callSettings = null)

Retrieves the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The project that the agent to fetch is associated with. Format: `projects/<Project ID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.Agent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]";
    // Make the request
    Agent response = await agentsClient.GetAgentAsync(parent);
    

### GetAgentAsync(string, CancellationToken)
    
    
    public virtual Task<Agent> GetAgentAsync(string parent, CancellationToken cancellationToken)

Retrieves the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The project that the agent to fetch is associated with. Format: `projects/<Project ID>`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.Agent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]";
    // Make the request
    Agent response = await agentsClient.GetAgentAsync(parent);
    

### GetValidationResult(GetValidationResultRequest, CallSettings)
    
    
    public virtual ValidationResult GetValidationResult(GetValidationResultRequest request, CallSettings callSettings = null)

Gets agent validation result. Agent validation is performed during training time and is updated automatically when training is completed.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetValidationResultRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.GetValidationResultRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ValidationResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ValidationResult)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = AgentsClient.Create();
    // Initialize request argument(s)
    GetValidationResultRequest request = new GetValidationResultRequest
    {
        ParentAsProjectName = ProjectName.FromProject("[PROJECT]"),
        LanguageCode = "",
    };
    // Make the request
    ValidationResult response = agentsClient.GetValidationResult(request);
    

### GetValidationResultAsync(GetValidationResultRequest, CallSettings)
    
    
    public virtual Task<ValidationResult> GetValidationResultAsync(GetValidationResultRequest request, CallSettings callSettings = null)

Gets agent validation result. Agent validation is performed during training time and is updated automatically when training is completed.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetValidationResultRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.GetValidationResultRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ValidationResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ValidationResult)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    GetValidationResultRequest request = new GetValidationResultRequest
    {
        ParentAsProjectName = ProjectName.FromProject("[PROJECT]"),
        LanguageCode = "",
    };
    // Make the request
    ValidationResult response = await agentsClient.GetValidationResultAsync(request);
    

### GetValidationResultAsync(GetValidationResultRequest, CancellationToken)
    
    
    public virtual Task<ValidationResult> GetValidationResultAsync(GetValidationResultRequest request, CancellationToken cancellationToken)

Gets agent validation result. Agent validation is performed during training time and is updated automatically when training is completed.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetValidationResultRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.GetValidationResultRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ValidationResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ValidationResult)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    GetValidationResultRequest request = new GetValidationResultRequest
    {
        ParentAsProjectName = ProjectName.FromProject("[PROJECT]"),
        LanguageCode = "",
    };
    // Make the request
    ValidationResult response = await agentsClient.GetValidationResultAsync(request);
    

### ImportAgent(ImportAgentRequest, CallSettings)
    
    
    public virtual Operation<Empty, Struct> ImportAgent(ImportAgentRequest request, CallSettings callSettings = null)

Imports the specified agent from a ZIP file.

Uploads new intents and entity types without deleting the existing ones. Intents and entity types with the same name are replaced with the new versions from [ImportAgentRequest][google.cloud.dialogflow.v2.ImportAgentRequest]. After the import, the imported draft agent will be trained automatically (unless disabled in agent settings). However, once the import is done, training may not be completed yet. Please call [TrainAgent][google.cloud.dialogflow.v2.Agents.TrainAgent] and wait for the operation it returns in order to train explicitly.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
  * `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)



The operation only tracks when importing is complete, not when it is done training.

Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ImportAgentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = AgentsClient.Create();
    // Initialize request argument(s)
    ImportAgentRequest request = new ImportAgentRequest
    {
        ParentAsProjectName = ProjectName.FromProject("[PROJECT]"),
        AgentUri = "",
    };
    // Make the request
    Operation<Empty, Struct> response = agentsClient.ImportAgent(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, Struct> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, Struct> retrievedResponse = agentsClient.PollOnceImportAgent(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### ImportAgentAsync(ImportAgentRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, Struct>> ImportAgentAsync(ImportAgentRequest request, CallSettings callSettings = null)

Imports the specified agent from a ZIP file.

Uploads new intents and entity types without deleting the existing ones. Intents and entity types with the same name are replaced with the new versions from [ImportAgentRequest][google.cloud.dialogflow.v2.ImportAgentRequest]. After the import, the imported draft agent will be trained automatically (unless disabled in agent settings). However, once the import is done, training may not be completed yet. Please call [TrainAgent][google.cloud.dialogflow.v2.Agents.TrainAgent] and wait for the operation it returns in order to train explicitly.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
  * `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)



The operation only tracks when importing is complete, not when it is done training.

Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ImportAgentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    ImportAgentRequest request = new ImportAgentRequest
    {
        ParentAsProjectName = ProjectName.FromProject("[PROJECT]"),
        AgentUri = "",
    };
    // Make the request
    Operation<Empty, Struct> response = await agentsClient.ImportAgentAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, Struct> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, Struct> retrievedResponse = await agentsClient.PollOnceImportAgentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### ImportAgentAsync(ImportAgentRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, Struct>> ImportAgentAsync(ImportAgentRequest request, CancellationToken cancellationToken)

Imports the specified agent from a ZIP file.

Uploads new intents and entity types without deleting the existing ones. Intents and entity types with the same name are replaced with the new versions from [ImportAgentRequest][google.cloud.dialogflow.v2.ImportAgentRequest]. After the import, the imported draft agent will be trained automatically (unless disabled in agent settings). However, once the import is done, training may not be completed yet. Please call [TrainAgent][google.cloud.dialogflow.v2.Agents.TrainAgent] and wait for the operation it returns in order to train explicitly.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
  * `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)



The operation only tracks when importing is complete, not when it is done training.

Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ImportAgentRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    ImportAgentRequest request = new ImportAgentRequest
    {
        ParentAsProjectName = ProjectName.FromProject("[PROJECT]"),
        AgentUri = "",
    };
    // Make the request
    Operation<Empty, Struct> response = await agentsClient.ImportAgentAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, Struct> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, Struct> retrievedResponse = await agentsClient.PollOnceImportAgentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### PollOnceExportAgent(string, CallSettings)
    
    
    public virtual Operation<ExportAgentResponse, Struct> PollOnceExportAgent(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `ExportAgent`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportAgentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ExportAgentResponse)[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` | The result of polling the operation.  
  
### PollOnceExportAgentAsync(string, CallSettings)
    
    
    public virtual Task<Operation<ExportAgentResponse, Struct>> PollOnceExportAgentAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `ExportAgent`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportAgentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ExportAgentResponse)[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` | A task representing the result of polling the operation.  
  
### PollOnceImportAgent(string, CallSettings)
    
    
    public virtual Operation<Empty, Struct> PollOnceImportAgent(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `ImportAgent`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` | The result of polling the operation.  
  
### PollOnceImportAgentAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, Struct>> PollOnceImportAgentAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `ImportAgent`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` | A task representing the result of polling the operation.  
  
### PollOnceRestoreAgent(string, CallSettings)
    
    
    public virtual Operation<Empty, Struct> PollOnceRestoreAgent(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `RestoreAgent`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` | The result of polling the operation.  
  
### PollOnceRestoreAgentAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, Struct>> PollOnceRestoreAgentAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `RestoreAgent`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` | A task representing the result of polling the operation.  
  
### PollOnceTrainAgent(string, CallSettings)
    
    
    public virtual Operation<Empty, Struct> PollOnceTrainAgent(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `TrainAgent`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` | The result of polling the operation.  
  
### PollOnceTrainAgentAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, Struct>> PollOnceTrainAgentAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `TrainAgent`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` | A task representing the result of polling the operation.  
  
### RestoreAgent(RestoreAgentRequest, CallSettings)
    
    
    public virtual Operation<Empty, Struct> RestoreAgent(RestoreAgentRequest request, CallSettings callSettings = null)

Restores the specified agent from a ZIP file.

Replaces the current agent version with a new one. All the intents and entity types in the older version are deleted. After the restore, the restored draft agent will be trained automatically (unless disabled in agent settings). However, once the restore is done, training may not be completed yet. Please call [TrainAgent][google.cloud.dialogflow.v2.Agents.TrainAgent] and wait for the operation it returns in order to train explicitly.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
  * `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)



The operation only tracks when restoring is complete, not when it is done training.

Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RestoreAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.RestoreAgentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = AgentsClient.Create();
    // Initialize request argument(s)
    RestoreAgentRequest request = new RestoreAgentRequest
    {
        ParentAsProjectName = ProjectName.FromProject("[PROJECT]"),
        AgentUri = "",
    };
    // Make the request
    Operation<Empty, Struct> response = agentsClient.RestoreAgent(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, Struct> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, Struct> retrievedResponse = agentsClient.PollOnceRestoreAgent(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### RestoreAgentAsync(RestoreAgentRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, Struct>> RestoreAgentAsync(RestoreAgentRequest request, CallSettings callSettings = null)

Restores the specified agent from a ZIP file.

Replaces the current agent version with a new one. All the intents and entity types in the older version are deleted. After the restore, the restored draft agent will be trained automatically (unless disabled in agent settings). However, once the restore is done, training may not be completed yet. Please call [TrainAgent][google.cloud.dialogflow.v2.Agents.TrainAgent] and wait for the operation it returns in order to train explicitly.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
  * `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)



The operation only tracks when restoring is complete, not when it is done training.

Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RestoreAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.RestoreAgentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    RestoreAgentRequest request = new RestoreAgentRequest
    {
        ParentAsProjectName = ProjectName.FromProject("[PROJECT]"),
        AgentUri = "",
    };
    // Make the request
    Operation<Empty, Struct> response = await agentsClient.RestoreAgentAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, Struct> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, Struct> retrievedResponse = await agentsClient.PollOnceRestoreAgentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### RestoreAgentAsync(RestoreAgentRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, Struct>> RestoreAgentAsync(RestoreAgentRequest request, CancellationToken cancellationToken)

Restores the specified agent from a ZIP file.

Replaces the current agent version with a new one. All the intents and entity types in the older version are deleted. After the restore, the restored draft agent will be trained automatically (unless disabled in agent settings). However, once the restore is done, training may not be completed yet. Please call [TrainAgent][google.cloud.dialogflow.v2.Agents.TrainAgent] and wait for the operation it returns in order to train explicitly.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
  * `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)



The operation only tracks when restoring is complete, not when it is done training.

Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RestoreAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.RestoreAgentRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    RestoreAgentRequest request = new RestoreAgentRequest
    {
        ParentAsProjectName = ProjectName.FromProject("[PROJECT]"),
        AgentUri = "",
    };
    // Make the request
    Operation<Empty, Struct> response = await agentsClient.RestoreAgentAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, Struct> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, Struct> retrievedResponse = await agentsClient.PollOnceRestoreAgentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### SearchAgents(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<SearchAgentsResponse, Agent> SearchAgents(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Returns the list of agents.

Since there is at most one conversational agent per project, this method is useful primarily for listing all agents across projects the caller has access to. One can achieve that with a wildcard project collection id "-". Refer to [List Sub-Collections](https://cloud.google.com/apis/design/design_patterns#list_sub-collections).

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The project to list agents from. Format: `projects/<Project ID or '-'>`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[SearchAgentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.SearchAgentsResponse)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.Agent)` | A pageable sequence of [Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.Agent) resources.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = AgentsClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<SearchAgentsResponse, Agent> response = agentsClient.SearchAgents(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Agent item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (SearchAgentsResponse page in response.AsRawResponses())
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
    

### SearchAgents(ProjectName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<SearchAgentsResponse, Agent> SearchAgents(ProjectName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Returns the list of agents.

Since there is at most one conversational agent per project, this method is useful primarily for listing all agents across projects the caller has access to. One can achieve that with a wildcard project collection id "-". Refer to [List Sub-Collections](https://cloud.google.com/apis/design/design_patterns#list_sub-collections).

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)`  
Required. The project to list agents from. Format: `projects/<Project ID or '-'>`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[SearchAgentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.SearchAgentsResponse)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.Agent)` | A pageable sequence of [Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.Agent) resources.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = AgentsClient.Create();
    // Initialize request argument(s)
    ProjectName parent = ProjectName.FromProject("[PROJECT]");
    // Make the request
    PagedEnumerable<SearchAgentsResponse, Agent> response = agentsClient.SearchAgents(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Agent item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (SearchAgentsResponse page in response.AsRawResponses())
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
    

### SearchAgents(SearchAgentsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<SearchAgentsResponse, Agent> SearchAgents(SearchAgentsRequest request, CallSettings callSettings = null)

Returns the list of agents.

Since there is at most one conversational agent per project, this method is useful primarily for listing all agents across projects the caller has access to. One can achieve that with a wildcard project collection id "-". Refer to [List Sub-Collections](https://cloud.google.com/apis/design/design_patterns#list_sub-collections).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchAgentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.SearchAgentsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[SearchAgentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.SearchAgentsResponse)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.Agent)` | A pageable sequence of [Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.Agent) resources.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = AgentsClient.Create();
    // Initialize request argument(s)
    SearchAgentsRequest request = new SearchAgentsRequest
    {
        ParentAsProjectName = ProjectName.FromProject("[PROJECT]"),
    };
    // Make the request
    PagedEnumerable<SearchAgentsResponse, Agent> response = agentsClient.SearchAgents(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Agent item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (SearchAgentsResponse page in response.AsRawResponses())
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
    

### SearchAgents(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<SearchAgentsResponse, Agent> SearchAgents(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Returns the list of agents.

Since there is at most one conversational agent per project, this method is useful primarily for listing all agents across projects the caller has access to. One can achieve that with a wildcard project collection id "-". Refer to [List Sub-Collections](https://cloud.google.com/apis/design/design_patterns#list_sub-collections).

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The project to list agents from. Format: `projects/<Project ID or '-'>`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[SearchAgentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.SearchAgentsResponse)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.Agent)` | A pageable sequence of [Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.Agent) resources.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = AgentsClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]";
    // Make the request
    PagedEnumerable<SearchAgentsResponse, Agent> response = agentsClient.SearchAgents(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Agent item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (SearchAgentsResponse page in response.AsRawResponses())
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
    

### SearchAgentsAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<SearchAgentsResponse, Agent> SearchAgentsAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Returns the list of agents.

Since there is at most one conversational agent per project, this method is useful primarily for listing all agents across projects the caller has access to. One can achieve that with a wildcard project collection id "-". Refer to [List Sub-Collections](https://cloud.google.com/apis/design/design_patterns#list_sub-collections).

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The project to list agents from. Format: `projects/<Project ID or '-'>`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[SearchAgentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.SearchAgentsResponse)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.Agent)` | A pageable asynchronous sequence of [Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.Agent) resources.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<SearchAgentsResponse, Agent> response = agentsClient.SearchAgentsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Agent item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (SearchAgentsResponse page in response.AsRawResponses())
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
    

### SearchAgentsAsync(ProjectName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<SearchAgentsResponse, Agent> SearchAgentsAsync(ProjectName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Returns the list of agents.

Since there is at most one conversational agent per project, this method is useful primarily for listing all agents across projects the caller has access to. One can achieve that with a wildcard project collection id "-". Refer to [List Sub-Collections](https://cloud.google.com/apis/design/design_patterns#list_sub-collections).

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)`  
Required. The project to list agents from. Format: `projects/<Project ID or '-'>`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[SearchAgentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.SearchAgentsResponse)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.Agent)` | A pageable asynchronous sequence of [Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.Agent) resources.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    ProjectName parent = ProjectName.FromProject("[PROJECT]");
    // Make the request
    PagedAsyncEnumerable<SearchAgentsResponse, Agent> response = agentsClient.SearchAgentsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Agent item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (SearchAgentsResponse page in response.AsRawResponses())
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
    

### SearchAgentsAsync(SearchAgentsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<SearchAgentsResponse, Agent> SearchAgentsAsync(SearchAgentsRequest request, CallSettings callSettings = null)

Returns the list of agents.

Since there is at most one conversational agent per project, this method is useful primarily for listing all agents across projects the caller has access to. One can achieve that with a wildcard project collection id "-". Refer to [List Sub-Collections](https://cloud.google.com/apis/design/design_patterns#list_sub-collections).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchAgentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.SearchAgentsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[SearchAgentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.SearchAgentsResponse)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.Agent)` | A pageable asynchronous sequence of [Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.Agent) resources.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    SearchAgentsRequest request = new SearchAgentsRequest
    {
        ParentAsProjectName = ProjectName.FromProject("[PROJECT]"),
    };
    // Make the request
    PagedAsyncEnumerable<SearchAgentsResponse, Agent> response = agentsClient.SearchAgentsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Agent item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (SearchAgentsResponse page in response.AsRawResponses())
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
    

### SearchAgentsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<SearchAgentsResponse, Agent> SearchAgentsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Returns the list of agents.

Since there is at most one conversational agent per project, this method is useful primarily for listing all agents across projects the caller has access to. One can achieve that with a wildcard project collection id "-". Refer to [List Sub-Collections](https://cloud.google.com/apis/design/design_patterns#list_sub-collections).

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The project to list agents from. Format: `projects/<Project ID or '-'>`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[SearchAgentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.SearchAgentsResponse)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.Agent)` | A pageable asynchronous sequence of [Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.Agent) resources.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]";
    // Make the request
    PagedAsyncEnumerable<SearchAgentsResponse, Agent> response = agentsClient.SearchAgentsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Agent item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (SearchAgentsResponse page in response.AsRawResponses())
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
    

### SetAgent(Agent, CallSettings)
    
    
    public virtual Agent SetAgent(Agent agent, CallSettings callSettings = null)

Creates/updates the specified agent.

Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).

**Parameters**  
---  
**Name** | **Description**  
`agent` | `[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.Agent)`  
Required. The agent to update.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.Agent)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = AgentsClient.Create();
    // Initialize request argument(s)
    Agent agent = new Agent();
    // Make the request
    Agent response = agentsClient.SetAgent(agent);
    

### SetAgent(SetAgentRequest, CallSettings)
    
    
    public virtual Agent SetAgent(SetAgentRequest request, CallSettings callSettings = null)

Creates/updates the specified agent.

Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.SetAgentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.Agent)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = AgentsClient.Create();
    // Initialize request argument(s)
    SetAgentRequest request = new SetAgentRequest
    {
        Agent = new Agent(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Agent response = agentsClient.SetAgent(request);
    

### SetAgentAsync(Agent, CallSettings)
    
    
    public virtual Task<Agent> SetAgentAsync(Agent agent, CallSettings callSettings = null)

Creates/updates the specified agent.

Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).

**Parameters**  
---  
**Name** | **Description**  
`agent` | `[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.Agent)`  
Required. The agent to update.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.Agent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    Agent agent = new Agent();
    // Make the request
    Agent response = await agentsClient.SetAgentAsync(agent);
    

### SetAgentAsync(Agent, CancellationToken)
    
    
    public virtual Task<Agent> SetAgentAsync(Agent agent, CancellationToken cancellationToken)

Creates/updates the specified agent.

Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).

**Parameters**  
---  
**Name** | **Description**  
`agent` | `[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.Agent)`  
Required. The agent to update.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.Agent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    Agent agent = new Agent();
    // Make the request
    Agent response = await agentsClient.SetAgentAsync(agent);
    

### SetAgentAsync(SetAgentRequest, CallSettings)
    
    
    public virtual Task<Agent> SetAgentAsync(SetAgentRequest request, CallSettings callSettings = null)

Creates/updates the specified agent.

Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.SetAgentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.Agent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    SetAgentRequest request = new SetAgentRequest
    {
        Agent = new Agent(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Agent response = await agentsClient.SetAgentAsync(request);
    

### SetAgentAsync(SetAgentRequest, CancellationToken)
    
    
    public virtual Task<Agent> SetAgentAsync(SetAgentRequest request, CancellationToken cancellationToken)

Creates/updates the specified agent.

Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.SetAgentRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.Agent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    SetAgentRequest request = new SetAgentRequest
    {
        Agent = new Agent(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Agent response = await agentsClient.SetAgentAsync(request);
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentsClient#Google_Cloud_Dialogflow_V2_AgentsClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentsClient#Google_Cloud_Dialogflow_V2_AgentsClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentsClient#Google_Cloud_Dialogflow_V2_AgentsClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentsClient#Google_Cloud_Dialogflow_V2_AgentsClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### TrainAgent(LocationName, CallSettings)
    
    
    public virtual Operation<Empty, Struct> TrainAgent(LocationName parent, CallSettings callSettings = null)

Trains the specified agent.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
  * `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)



Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The project that the agent to train is associated with. Format: `projects/<Project ID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = AgentsClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    Operation<Empty, Struct> response = agentsClient.TrainAgent(parent);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, Struct> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, Struct> retrievedResponse = agentsClient.PollOnceTrainAgent(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### TrainAgent(ProjectName, CallSettings)
    
    
    public virtual Operation<Empty, Struct> TrainAgent(ProjectName parent, CallSettings callSettings = null)

Trains the specified agent.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
  * `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)



Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)`  
Required. The project that the agent to train is associated with. Format: `projects/<Project ID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = AgentsClient.Create();
    // Initialize request argument(s)
    ProjectName parent = ProjectName.FromProject("[PROJECT]");
    // Make the request
    Operation<Empty, Struct> response = agentsClient.TrainAgent(parent);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, Struct> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, Struct> retrievedResponse = agentsClient.PollOnceTrainAgent(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### TrainAgent(TrainAgentRequest, CallSettings)
    
    
    public virtual Operation<Empty, Struct> TrainAgent(TrainAgentRequest request, CallSettings callSettings = null)

Trains the specified agent.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
  * `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)



Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TrainAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.TrainAgentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = AgentsClient.Create();
    // Initialize request argument(s)
    TrainAgentRequest request = new TrainAgentRequest
    {
        ParentAsProjectName = ProjectName.FromProject("[PROJECT]"),
    };
    // Make the request
    Operation<Empty, Struct> response = agentsClient.TrainAgent(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, Struct> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, Struct> retrievedResponse = agentsClient.PollOnceTrainAgent(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### TrainAgent(string, CallSettings)
    
    
    public virtual Operation<Empty, Struct> TrainAgent(string parent, CallSettings callSettings = null)

Trains the specified agent.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
  * `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)



Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The project that the agent to train is associated with. Format: `projects/<Project ID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = AgentsClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]";
    // Make the request
    Operation<Empty, Struct> response = agentsClient.TrainAgent(parent);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, Struct> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, Struct> retrievedResponse = agentsClient.PollOnceTrainAgent(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### TrainAgentAsync(LocationName, CallSettings)
    
    
    public virtual Task<Operation<Empty, Struct>> TrainAgentAsync(LocationName parent, CallSettings callSettings = null)

Trains the specified agent.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
  * `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)



Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The project that the agent to train is associated with. Format: `projects/<Project ID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    Operation<Empty, Struct> response = await agentsClient.TrainAgentAsync(parent);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, Struct> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, Struct> retrievedResponse = await agentsClient.PollOnceTrainAgentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### TrainAgentAsync(LocationName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, Struct>> TrainAgentAsync(LocationName parent, CancellationToken cancellationToken)

Trains the specified agent.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
  * `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)



Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The project that the agent to train is associated with. Format: `projects/<Project ID>`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    Operation<Empty, Struct> response = await agentsClient.TrainAgentAsync(parent);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, Struct> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, Struct> retrievedResponse = await agentsClient.PollOnceTrainAgentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### TrainAgentAsync(ProjectName, CallSettings)
    
    
    public virtual Task<Operation<Empty, Struct>> TrainAgentAsync(ProjectName parent, CallSettings callSettings = null)

Trains the specified agent.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
  * `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)



Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)`  
Required. The project that the agent to train is associated with. Format: `projects/<Project ID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    ProjectName parent = ProjectName.FromProject("[PROJECT]");
    // Make the request
    Operation<Empty, Struct> response = await agentsClient.TrainAgentAsync(parent);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, Struct> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, Struct> retrievedResponse = await agentsClient.PollOnceTrainAgentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### TrainAgentAsync(ProjectName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, Struct>> TrainAgentAsync(ProjectName parent, CancellationToken cancellationToken)

Trains the specified agent.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
  * `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)



Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)`  
Required. The project that the agent to train is associated with. Format: `projects/<Project ID>`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    ProjectName parent = ProjectName.FromProject("[PROJECT]");
    // Make the request
    Operation<Empty, Struct> response = await agentsClient.TrainAgentAsync(parent);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, Struct> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, Struct> retrievedResponse = await agentsClient.PollOnceTrainAgentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### TrainAgentAsync(TrainAgentRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, Struct>> TrainAgentAsync(TrainAgentRequest request, CallSettings callSettings = null)

Trains the specified agent.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
  * `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)



Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TrainAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.TrainAgentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    TrainAgentRequest request = new TrainAgentRequest
    {
        ParentAsProjectName = ProjectName.FromProject("[PROJECT]"),
    };
    // Make the request
    Operation<Empty, Struct> response = await agentsClient.TrainAgentAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, Struct> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, Struct> retrievedResponse = await agentsClient.PollOnceTrainAgentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### TrainAgentAsync(TrainAgentRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, Struct>> TrainAgentAsync(TrainAgentRequest request, CancellationToken cancellationToken)

Trains the specified agent.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
  * `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)



Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TrainAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.TrainAgentRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    TrainAgentRequest request = new TrainAgentRequest
    {
        ParentAsProjectName = ProjectName.FromProject("[PROJECT]"),
    };
    // Make the request
    Operation<Empty, Struct> response = await agentsClient.TrainAgentAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, Struct> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, Struct> retrievedResponse = await agentsClient.PollOnceTrainAgentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### TrainAgentAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, Struct>> TrainAgentAsync(string parent, CallSettings callSettings = null)

Trains the specified agent.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
  * `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)



Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The project that the agent to train is associated with. Format: `projects/<Project ID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]";
    // Make the request
    Operation<Empty, Struct> response = await agentsClient.TrainAgentAsync(parent);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, Struct> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, Struct> retrievedResponse = await agentsClient.PollOnceTrainAgentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### TrainAgentAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, Struct>> TrainAgentAsync(string parent, CancellationToken cancellationToken)

Trains the specified agent.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
  * `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)



Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The project that the agent to train is associated with. Format: `projects/<Project ID>`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]";
    // Make the request
    Operation<Empty, Struct> response = await agentsClient.TrainAgentAsync(parent);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, Struct> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, Struct> retrievedResponse = await agentsClient.PollOnceTrainAgentAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
