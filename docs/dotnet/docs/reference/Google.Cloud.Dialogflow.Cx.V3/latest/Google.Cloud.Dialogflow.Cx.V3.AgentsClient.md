---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentsClient
title: Dialogflow v3 API - Class AgentsClient (3.2.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:30:48.735413+00:00
---

# Dialogflow v3 API - Class AgentsClient (3.2.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Dialogflow v3 API - Class AgentsClient (3.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.2.0 (latest)  3.1.0  3.0.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public abstract class AgentsClient

Reference documentation and code samples for the Dialogflow v3 API class AgentsClient.

Agents client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AgentsClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[AgentsClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentsClientImpl)

## Namespace

[Google.Cloud.Dialogflow.Cx.V3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3)

## Assembly

Google.Cloud.Dialogflow.Cx.V3.dll

## Remarks

Service for managing [Agents][google.cloud.dialogflow.cx.v3.Agent].

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
`[Agents](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agents)[AgentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agents.AgentsClient)` |   
  
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
  
## Methods 

### Create()
    
    
    public static AgentsClient Create()

Synchronously creates a [AgentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentsClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [AgentsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentsClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[AgentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentsClient)` | The created [AgentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentsClient).  
  
### CreateAgent(LocationName, Agent, CallSettings)
    
    
    public virtual Agent CreateAgent(LocationName parent, Agent agent, CallSettings callSettings = null)

Creates an agent in the specified location.

Note: You should always train flows prior to sending them queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The location to create a agent for. Format: `projects/<ProjectID>/locations/<LocationID>`.  
`agent` | `[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent)`  
Required. The agent to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = AgentsClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Agent agent = new Agent();
    // Make the request
    Agent response = agentsClient.CreateAgent(parent, agent);
    

### CreateAgent(CreateAgentRequest, CallSettings)
    
    
    public virtual Agent CreateAgent(CreateAgentRequest request, CallSettings callSettings = null)

Creates an agent in the specified location.

Note: You should always train flows prior to sending them queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.CreateAgentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = AgentsClient.Create();
    // Initialize request argument(s)
    CreateAgentRequest request = new CreateAgentRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Agent = new Agent(),
    };
    // Make the request
    Agent response = agentsClient.CreateAgent(request);
    

### CreateAgent(string, Agent, CallSettings)
    
    
    public virtual Agent CreateAgent(string parent, Agent agent, CallSettings callSettings = null)

Creates an agent in the specified location.

Note: You should always train flows prior to sending them queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The location to create a agent for. Format: `projects/<ProjectID>/locations/<LocationID>`.  
`agent` | `[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent)`  
Required. The agent to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = AgentsClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Agent agent = new Agent();
    // Make the request
    Agent response = agentsClient.CreateAgent(parent, agent);
    

### CreateAgentAsync(LocationName, Agent, CallSettings)
    
    
    public virtual Task<Agent> CreateAgentAsync(LocationName parent, Agent agent, CallSettings callSettings = null)

Creates an agent in the specified location.

Note: You should always train flows prior to sending them queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The location to create a agent for. Format: `projects/<ProjectID>/locations/<LocationID>`.  
`agent` | `[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent)`  
Required. The agent to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Agent agent = new Agent();
    // Make the request
    Agent response = await agentsClient.CreateAgentAsync(parent, agent);
    

### CreateAgentAsync(LocationName, Agent, CancellationToken)
    
    
    public virtual Task<Agent> CreateAgentAsync(LocationName parent, Agent agent, CancellationToken cancellationToken)

Creates an agent in the specified location.

Note: You should always train flows prior to sending them queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The location to create a agent for. Format: `projects/<ProjectID>/locations/<LocationID>`.  
`agent` | `[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent)`  
Required. The agent to create.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Agent agent = new Agent();
    // Make the request
    Agent response = await agentsClient.CreateAgentAsync(parent, agent);
    

### CreateAgentAsync(CreateAgentRequest, CallSettings)
    
    
    public virtual Task<Agent> CreateAgentAsync(CreateAgentRequest request, CallSettings callSettings = null)

Creates an agent in the specified location.

Note: You should always train flows prior to sending them queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.CreateAgentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    CreateAgentRequest request = new CreateAgentRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Agent = new Agent(),
    };
    // Make the request
    Agent response = await agentsClient.CreateAgentAsync(request);
    

### CreateAgentAsync(CreateAgentRequest, CancellationToken)
    
    
    public virtual Task<Agent> CreateAgentAsync(CreateAgentRequest request, CancellationToken cancellationToken)

Creates an agent in the specified location.

Note: You should always train flows prior to sending them queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.CreateAgentRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    CreateAgentRequest request = new CreateAgentRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Agent = new Agent(),
    };
    // Make the request
    Agent response = await agentsClient.CreateAgentAsync(request);
    

### CreateAgentAsync(string, Agent, CallSettings)
    
    
    public virtual Task<Agent> CreateAgentAsync(string parent, Agent agent, CallSettings callSettings = null)

Creates an agent in the specified location.

Note: You should always train flows prior to sending them queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The location to create a agent for. Format: `projects/<ProjectID>/locations/<LocationID>`.  
`agent` | `[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent)`  
Required. The agent to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Agent agent = new Agent();
    // Make the request
    Agent response = await agentsClient.CreateAgentAsync(parent, agent);
    

### CreateAgentAsync(string, Agent, CancellationToken)
    
    
    public virtual Task<Agent> CreateAgentAsync(string parent, Agent agent, CancellationToken cancellationToken)

Creates an agent in the specified location.

Note: You should always train flows prior to sending them queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The location to create a agent for. Format: `projects/<ProjectID>/locations/<LocationID>`.  
`agent` | `[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent)`  
Required. The agent to create.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Agent agent = new Agent();
    // Make the request
    Agent response = await agentsClient.CreateAgentAsync(parent, agent);
    

### CreateAsync(CancellationToken)
    
    
    public static Task<AgentsClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [AgentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentsClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [AgentsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentsClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AgentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentsClient)` | The task representing the created [AgentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentsClient).  
  
### DeleteAgent(AgentName, CallSettings)
    
    
    public virtual void DeleteAgent(AgentName name, CallSettings callSettings = null)

Deletes the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AgentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentName)`  
Required. The name of the agent to delete. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = AgentsClient.Create();
    // Initialize request argument(s)
    AgentName name = AgentName.FromProjectLocationAgent("[PROJECT]", "[LOCATION]", "[AGENT]");
    // Make the request
    agentsClient.DeleteAgent(name);
    

### DeleteAgent(DeleteAgentRequest, CallSettings)
    
    
    public virtual void DeleteAgent(DeleteAgentRequest request, CallSettings callSettings = null)

Deletes the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DeleteAgentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = AgentsClient.Create();
    // Initialize request argument(s)
    DeleteAgentRequest request = new DeleteAgentRequest
    {
        AgentName = AgentName.FromProjectLocationAgent("[PROJECT]", "[LOCATION]", "[AGENT]"),
    };
    // Make the request
    agentsClient.DeleteAgent(request);
    

### DeleteAgent(string, CallSettings)
    
    
    public virtual void DeleteAgent(string name, CallSettings callSettings = null)

Deletes the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the agent to delete. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = AgentsClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/agents/[AGENT]";
    // Make the request
    agentsClient.DeleteAgent(name);
    

### DeleteAgentAsync(AgentName, CallSettings)
    
    
    public virtual Task DeleteAgentAsync(AgentName name, CallSettings callSettings = null)

Deletes the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AgentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentName)`  
Required. The name of the agent to delete. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
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
    AgentName name = AgentName.FromProjectLocationAgent("[PROJECT]", "[LOCATION]", "[AGENT]");
    // Make the request
    await agentsClient.DeleteAgentAsync(name);
    

### DeleteAgentAsync(AgentName, CancellationToken)
    
    
    public virtual Task DeleteAgentAsync(AgentName name, CancellationToken cancellationToken)

Deletes the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AgentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentName)`  
Required. The name of the agent to delete. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
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
    AgentName name = AgentName.FromProjectLocationAgent("[PROJECT]", "[LOCATION]", "[AGENT]");
    // Make the request
    await agentsClient.DeleteAgentAsync(name);
    

### DeleteAgentAsync(DeleteAgentRequest, CallSettings)
    
    
    public virtual Task DeleteAgentAsync(DeleteAgentRequest request, CallSettings callSettings = null)

Deletes the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DeleteAgentRequest)`  
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
        AgentName = AgentName.FromProjectLocationAgent("[PROJECT]", "[LOCATION]", "[AGENT]"),
    };
    // Make the request
    await agentsClient.DeleteAgentAsync(request);
    

### DeleteAgentAsync(DeleteAgentRequest, CancellationToken)
    
    
    public virtual Task DeleteAgentAsync(DeleteAgentRequest request, CancellationToken cancellationToken)

Deletes the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DeleteAgentRequest)`  
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
        AgentName = AgentName.FromProjectLocationAgent("[PROJECT]", "[LOCATION]", "[AGENT]"),
    };
    // Make the request
    await agentsClient.DeleteAgentAsync(request);
    

### DeleteAgentAsync(string, CallSettings)
    
    
    public virtual Task DeleteAgentAsync(string name, CallSettings callSettings = null)

Deletes the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the agent to delete. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
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
    string name = "projects/[PROJECT]/locations/[LOCATION]/agents/[AGENT]";
    // Make the request
    await agentsClient.DeleteAgentAsync(name);
    

### DeleteAgentAsync(string, CancellationToken)
    
    
    public virtual Task DeleteAgentAsync(string name, CancellationToken cancellationToken)

Deletes the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the agent to delete. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
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
    string name = "projects/[PROJECT]/locations/[LOCATION]/agents/[AGENT]";
    // Make the request
    await agentsClient.DeleteAgentAsync(name);
    

### ExportAgent(ExportAgentRequest, CallSettings)
    
    
    public virtual Operation<ExportAgentResponse, Struct> ExportAgent(ExportAgentRequest request, CallSettings callSettings = null)

Exports the specified agent to a binary file.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
  * `response`: [ExportAgentResponse][google.cloud.dialogflow.cx.v3.ExportAgentResponse]



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportAgentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportAgentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportAgentResponse)[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = AgentsClient.Create();
    // Initialize request argument(s)
    ExportAgentRequest request = new ExportAgentRequest
    {
        AgentName = AgentName.FromProjectLocationAgent("[PROJECT]", "[LOCATION]", "[AGENT]"),
        AgentUri = "",
        DataFormat = ExportAgentRequest.Types.DataFormat.Unspecified,
        EnvironmentAsEnvironmentName = EnvironmentName.FromProjectLocationAgentEnvironment("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENVIRONMENT]"),
        GitDestination = new ExportAgentRequest.Types.GitDestination(),
        IncludeBigqueryExportSettings = false,
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
    

### ExportAgentAsync(ExportAgentRequest, CallSettings)
    
    
    public virtual Task<Operation<ExportAgentResponse, Struct>> ExportAgentAsync(ExportAgentRequest request, CallSettings callSettings = null)

Exports the specified agent to a binary file.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
  * `response`: [ExportAgentResponse][google.cloud.dialogflow.cx.v3.ExportAgentResponse]



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportAgentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportAgentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportAgentResponse)[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    ExportAgentRequest request = new ExportAgentRequest
    {
        AgentName = AgentName.FromProjectLocationAgent("[PROJECT]", "[LOCATION]", "[AGENT]"),
        AgentUri = "",
        DataFormat = ExportAgentRequest.Types.DataFormat.Unspecified,
        EnvironmentAsEnvironmentName = EnvironmentName.FromProjectLocationAgentEnvironment("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENVIRONMENT]"),
        GitDestination = new ExportAgentRequest.Types.GitDestination(),
        IncludeBigqueryExportSettings = false,
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

Exports the specified agent to a binary file.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
  * `response`: [ExportAgentResponse][google.cloud.dialogflow.cx.v3.ExportAgentResponse]



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportAgentRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportAgentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportAgentResponse)[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    ExportAgentRequest request = new ExportAgentRequest
    {
        AgentName = AgentName.FromProjectLocationAgent("[PROJECT]", "[LOCATION]", "[AGENT]"),
        AgentUri = "",
        DataFormat = ExportAgentRequest.Types.DataFormat.Unspecified,
        EnvironmentAsEnvironmentName = EnvironmentName.FromProjectLocationAgentEnvironment("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENVIRONMENT]"),
        GitDestination = new ExportAgentRequest.Types.GitDestination(),
        IncludeBigqueryExportSettings = false,
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
    

### GetAgent(AgentName, CallSettings)
    
    
    public virtual Agent GetAgent(AgentName name, CallSettings callSettings = null)

Retrieves the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AgentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentName)`  
Required. The name of the agent. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = AgentsClient.Create();
    // Initialize request argument(s)
    AgentName name = AgentName.FromProjectLocationAgent("[PROJECT]", "[LOCATION]", "[AGENT]");
    // Make the request
    Agent response = agentsClient.GetAgent(name);
    

### GetAgent(GetAgentRequest, CallSettings)
    
    
    public virtual Agent GetAgent(GetAgentRequest request, CallSettings callSettings = null)

Retrieves the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GetAgentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = AgentsClient.Create();
    // Initialize request argument(s)
    GetAgentRequest request = new GetAgentRequest
    {
        AgentName = AgentName.FromProjectLocationAgent("[PROJECT]", "[LOCATION]", "[AGENT]"),
    };
    // Make the request
    Agent response = agentsClient.GetAgent(request);
    

### GetAgent(string, CallSettings)
    
    
    public virtual Agent GetAgent(string name, CallSettings callSettings = null)

Retrieves the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the agent. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = AgentsClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/agents/[AGENT]";
    // Make the request
    Agent response = agentsClient.GetAgent(name);
    

### GetAgentAsync(AgentName, CallSettings)
    
    
    public virtual Task<Agent> GetAgentAsync(AgentName name, CallSettings callSettings = null)

Retrieves the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AgentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentName)`  
Required. The name of the agent. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    AgentName name = AgentName.FromProjectLocationAgent("[PROJECT]", "[LOCATION]", "[AGENT]");
    // Make the request
    Agent response = await agentsClient.GetAgentAsync(name);
    

### GetAgentAsync(AgentName, CancellationToken)
    
    
    public virtual Task<Agent> GetAgentAsync(AgentName name, CancellationToken cancellationToken)

Retrieves the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AgentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentName)`  
Required. The name of the agent. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    AgentName name = AgentName.FromProjectLocationAgent("[PROJECT]", "[LOCATION]", "[AGENT]");
    // Make the request
    Agent response = await agentsClient.GetAgentAsync(name);
    

### GetAgentAsync(GetAgentRequest, CallSettings)
    
    
    public virtual Task<Agent> GetAgentAsync(GetAgentRequest request, CallSettings callSettings = null)

Retrieves the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GetAgentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    GetAgentRequest request = new GetAgentRequest
    {
        AgentName = AgentName.FromProjectLocationAgent("[PROJECT]", "[LOCATION]", "[AGENT]"),
    };
    // Make the request
    Agent response = await agentsClient.GetAgentAsync(request);
    

### GetAgentAsync(GetAgentRequest, CancellationToken)
    
    
    public virtual Task<Agent> GetAgentAsync(GetAgentRequest request, CancellationToken cancellationToken)

Retrieves the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GetAgentRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    GetAgentRequest request = new GetAgentRequest
    {
        AgentName = AgentName.FromProjectLocationAgent("[PROJECT]", "[LOCATION]", "[AGENT]"),
    };
    // Make the request
    Agent response = await agentsClient.GetAgentAsync(request);
    

### GetAgentAsync(string, CallSettings)
    
    
    public virtual Task<Agent> GetAgentAsync(string name, CallSettings callSettings = null)

Retrieves the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the agent. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/agents/[AGENT]";
    // Make the request
    Agent response = await agentsClient.GetAgentAsync(name);
    

### GetAgentAsync(string, CancellationToken)
    
    
    public virtual Task<Agent> GetAgentAsync(string name, CancellationToken cancellationToken)

Retrieves the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the agent. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/agents/[AGENT]";
    // Make the request
    Agent response = await agentsClient.GetAgentAsync(name);
    

### GetAgentValidationResult(AgentValidationResultName, CallSettings)
    
    
    public virtual AgentValidationResult GetAgentValidationResult(AgentValidationResultName name, CallSettings callSettings = null)

Gets the latest agent validation result. Agent validation is performed when ValidateAgent is called.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AgentValidationResultName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentValidationResultName)`  
Required. The agent name. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/validationResult`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[AgentValidationResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentValidationResult)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = AgentsClient.Create();
    // Initialize request argument(s)
    AgentValidationResultName name = AgentValidationResultName.FromProjectLocationAgent("[PROJECT]", "[LOCATION]", "[AGENT]");
    // Make the request
    AgentValidationResult response = agentsClient.GetAgentValidationResult(name);
    

### GetAgentValidationResult(GetAgentValidationResultRequest, CallSettings)
    
    
    public virtual AgentValidationResult GetAgentValidationResult(GetAgentValidationResultRequest request, CallSettings callSettings = null)

Gets the latest agent validation result. Agent validation is performed when ValidateAgent is called.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAgentValidationResultRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GetAgentValidationResultRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[AgentValidationResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentValidationResult)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = AgentsClient.Create();
    // Initialize request argument(s)
    GetAgentValidationResultRequest request = new GetAgentValidationResultRequest
    {
        AgentValidationResultName = AgentValidationResultName.FromProjectLocationAgent("[PROJECT]", "[LOCATION]", "[AGENT]"),
        LanguageCode = "",
    };
    // Make the request
    AgentValidationResult response = agentsClient.GetAgentValidationResult(request);
    

### GetAgentValidationResult(string, CallSettings)
    
    
    public virtual AgentValidationResult GetAgentValidationResult(string name, CallSettings callSettings = null)

Gets the latest agent validation result. Agent validation is performed when ValidateAgent is called.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The agent name. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/validationResult`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[AgentValidationResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentValidationResult)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = AgentsClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/agents/[AGENT]/validationResult";
    // Make the request
    AgentValidationResult response = agentsClient.GetAgentValidationResult(name);
    

### GetAgentValidationResultAsync(AgentValidationResultName, CallSettings)
    
    
    public virtual Task<AgentValidationResult> GetAgentValidationResultAsync(AgentValidationResultName name, CallSettings callSettings = null)

Gets the latest agent validation result. Agent validation is performed when ValidateAgent is called.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AgentValidationResultName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentValidationResultName)`  
Required. The agent name. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/validationResult`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AgentValidationResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentValidationResult)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    AgentValidationResultName name = AgentValidationResultName.FromProjectLocationAgent("[PROJECT]", "[LOCATION]", "[AGENT]");
    // Make the request
    AgentValidationResult response = await agentsClient.GetAgentValidationResultAsync(name);
    

### GetAgentValidationResultAsync(AgentValidationResultName, CancellationToken)
    
    
    public virtual Task<AgentValidationResult> GetAgentValidationResultAsync(AgentValidationResultName name, CancellationToken cancellationToken)

Gets the latest agent validation result. Agent validation is performed when ValidateAgent is called.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AgentValidationResultName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentValidationResultName)`  
Required. The agent name. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/validationResult`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AgentValidationResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentValidationResult)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    AgentValidationResultName name = AgentValidationResultName.FromProjectLocationAgent("[PROJECT]", "[LOCATION]", "[AGENT]");
    // Make the request
    AgentValidationResult response = await agentsClient.GetAgentValidationResultAsync(name);
    

### GetAgentValidationResultAsync(GetAgentValidationResultRequest, CallSettings)
    
    
    public virtual Task<AgentValidationResult> GetAgentValidationResultAsync(GetAgentValidationResultRequest request, CallSettings callSettings = null)

Gets the latest agent validation result. Agent validation is performed when ValidateAgent is called.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAgentValidationResultRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GetAgentValidationResultRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AgentValidationResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentValidationResult)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    GetAgentValidationResultRequest request = new GetAgentValidationResultRequest
    {
        AgentValidationResultName = AgentValidationResultName.FromProjectLocationAgent("[PROJECT]", "[LOCATION]", "[AGENT]"),
        LanguageCode = "",
    };
    // Make the request
    AgentValidationResult response = await agentsClient.GetAgentValidationResultAsync(request);
    

### GetAgentValidationResultAsync(GetAgentValidationResultRequest, CancellationToken)
    
    
    public virtual Task<AgentValidationResult> GetAgentValidationResultAsync(GetAgentValidationResultRequest request, CancellationToken cancellationToken)

Gets the latest agent validation result. Agent validation is performed when ValidateAgent is called.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAgentValidationResultRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GetAgentValidationResultRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AgentValidationResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentValidationResult)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    GetAgentValidationResultRequest request = new GetAgentValidationResultRequest
    {
        AgentValidationResultName = AgentValidationResultName.FromProjectLocationAgent("[PROJECT]", "[LOCATION]", "[AGENT]"),
        LanguageCode = "",
    };
    // Make the request
    AgentValidationResult response = await agentsClient.GetAgentValidationResultAsync(request);
    

### GetAgentValidationResultAsync(string, CallSettings)
    
    
    public virtual Task<AgentValidationResult> GetAgentValidationResultAsync(string name, CallSettings callSettings = null)

Gets the latest agent validation result. Agent validation is performed when ValidateAgent is called.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The agent name. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/validationResult`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AgentValidationResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentValidationResult)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/agents/[AGENT]/validationResult";
    // Make the request
    AgentValidationResult response = await agentsClient.GetAgentValidationResultAsync(name);
    

### GetAgentValidationResultAsync(string, CancellationToken)
    
    
    public virtual Task<AgentValidationResult> GetAgentValidationResultAsync(string name, CancellationToken cancellationToken)

Gets the latest agent validation result. Agent validation is performed when ValidateAgent is called.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The agent name. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/validationResult`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AgentValidationResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentValidationResult)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/agents/[AGENT]/validationResult";
    // Make the request
    AgentValidationResult response = await agentsClient.GetAgentValidationResultAsync(name);
    

### GetGenerativeSettings(AgentGenerativeSettingsName, string, CallSettings)
    
    
    public virtual GenerativeSettings GetGenerativeSettings(AgentGenerativeSettingsName name, string languageCode, CallSettings callSettings = null)

Gets the generative settings for the agent.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AgentGenerativeSettingsName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentGenerativeSettingsName)`  
Required. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/generativeSettings`.  
`languageCode` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Language code of the generative settings.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[GenerativeSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GenerativeSettings)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = AgentsClient.Create();
    // Initialize request argument(s)
    AgentGenerativeSettingsName name = AgentGenerativeSettingsName.FromProjectLocationAgent("[PROJECT]", "[LOCATION]", "[AGENT]");
    string languageCode = "";
    // Make the request
    GenerativeSettings response = agentsClient.GetGenerativeSettings(name, languageCode);
    

### GetGenerativeSettings(GetGenerativeSettingsRequest, CallSettings)
    
    
    public virtual GenerativeSettings GetGenerativeSettings(GetGenerativeSettingsRequest request, CallSettings callSettings = null)

Gets the generative settings for the agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGenerativeSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GetGenerativeSettingsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[GenerativeSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GenerativeSettings)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = AgentsClient.Create();
    // Initialize request argument(s)
    GetGenerativeSettingsRequest request = new GetGenerativeSettingsRequest
    {
        AgentGenerativeSettingsName = AgentGenerativeSettingsName.FromProjectLocationAgent("[PROJECT]", "[LOCATION]", "[AGENT]"),
        LanguageCode = "",
    };
    // Make the request
    GenerativeSettings response = agentsClient.GetGenerativeSettings(request);
    

### GetGenerativeSettings(string, string, CallSettings)
    
    
    public virtual GenerativeSettings GetGenerativeSettings(string name, string languageCode, CallSettings callSettings = null)

Gets the generative settings for the agent.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/generativeSettings`.  
`languageCode` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Language code of the generative settings.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[GenerativeSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GenerativeSettings)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = AgentsClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/agents/[AGENT]/generativeSettings";
    string languageCode = "";
    // Make the request
    GenerativeSettings response = agentsClient.GetGenerativeSettings(name, languageCode);
    

### GetGenerativeSettingsAsync(AgentGenerativeSettingsName, string, CallSettings)
    
    
    public virtual Task<GenerativeSettings> GetGenerativeSettingsAsync(AgentGenerativeSettingsName name, string languageCode, CallSettings callSettings = null)

Gets the generative settings for the agent.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AgentGenerativeSettingsName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentGenerativeSettingsName)`  
Required. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/generativeSettings`.  
`languageCode` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Language code of the generative settings.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GenerativeSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GenerativeSettings)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    AgentGenerativeSettingsName name = AgentGenerativeSettingsName.FromProjectLocationAgent("[PROJECT]", "[LOCATION]", "[AGENT]");
    string languageCode = "";
    // Make the request
    GenerativeSettings response = await agentsClient.GetGenerativeSettingsAsync(name, languageCode);
    

### GetGenerativeSettingsAsync(AgentGenerativeSettingsName, string, CancellationToken)
    
    
    public virtual Task<GenerativeSettings> GetGenerativeSettingsAsync(AgentGenerativeSettingsName name, string languageCode, CancellationToken cancellationToken)

Gets the generative settings for the agent.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AgentGenerativeSettingsName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentGenerativeSettingsName)`  
Required. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/generativeSettings`.  
`languageCode` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Language code of the generative settings.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GenerativeSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GenerativeSettings)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    AgentGenerativeSettingsName name = AgentGenerativeSettingsName.FromProjectLocationAgent("[PROJECT]", "[LOCATION]", "[AGENT]");
    string languageCode = "";
    // Make the request
    GenerativeSettings response = await agentsClient.GetGenerativeSettingsAsync(name, languageCode);
    

### GetGenerativeSettingsAsync(GetGenerativeSettingsRequest, CallSettings)
    
    
    public virtual Task<GenerativeSettings> GetGenerativeSettingsAsync(GetGenerativeSettingsRequest request, CallSettings callSettings = null)

Gets the generative settings for the agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGenerativeSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GetGenerativeSettingsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GenerativeSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GenerativeSettings)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    GetGenerativeSettingsRequest request = new GetGenerativeSettingsRequest
    {
        AgentGenerativeSettingsName = AgentGenerativeSettingsName.FromProjectLocationAgent("[PROJECT]", "[LOCATION]", "[AGENT]"),
        LanguageCode = "",
    };
    // Make the request
    GenerativeSettings response = await agentsClient.GetGenerativeSettingsAsync(request);
    

### GetGenerativeSettingsAsync(GetGenerativeSettingsRequest, CancellationToken)
    
    
    public virtual Task<GenerativeSettings> GetGenerativeSettingsAsync(GetGenerativeSettingsRequest request, CancellationToken cancellationToken)

Gets the generative settings for the agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGenerativeSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GetGenerativeSettingsRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GenerativeSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GenerativeSettings)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    GetGenerativeSettingsRequest request = new GetGenerativeSettingsRequest
    {
        AgentGenerativeSettingsName = AgentGenerativeSettingsName.FromProjectLocationAgent("[PROJECT]", "[LOCATION]", "[AGENT]"),
        LanguageCode = "",
    };
    // Make the request
    GenerativeSettings response = await agentsClient.GetGenerativeSettingsAsync(request);
    

### GetGenerativeSettingsAsync(string, string, CallSettings)
    
    
    public virtual Task<GenerativeSettings> GetGenerativeSettingsAsync(string name, string languageCode, CallSettings callSettings = null)

Gets the generative settings for the agent.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/generativeSettings`.  
`languageCode` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Language code of the generative settings.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GenerativeSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GenerativeSettings)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/agents/[AGENT]/generativeSettings";
    string languageCode = "";
    // Make the request
    GenerativeSettings response = await agentsClient.GetGenerativeSettingsAsync(name, languageCode);
    

### GetGenerativeSettingsAsync(string, string, CancellationToken)
    
    
    public virtual Task<GenerativeSettings> GetGenerativeSettingsAsync(string name, string languageCode, CancellationToken cancellationToken)

Gets the generative settings for the agent.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/generativeSettings`.  
`languageCode` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Language code of the generative settings.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GenerativeSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GenerativeSettings)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/agents/[AGENT]/generativeSettings";
    string languageCode = "";
    // Make the request
    GenerativeSettings response = await agentsClient.GetGenerativeSettingsAsync(name, languageCode);
    

### ListAgents(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListAgentsResponse, Agent> ListAgents(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Returns the list of all agents in the specified location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The location to list all agents for. Format: `projects/<ProjectID>/locations/<LocationID>`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListAgentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListAgentsResponse)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent)` | A pageable sequence of [Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent) resources.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = AgentsClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListAgentsResponse, Agent> response = agentsClient.ListAgents(parent);
    
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

Returns the list of all agents in the specified location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAgentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListAgentsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListAgentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListAgentsResponse)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent)` | A pageable sequence of [Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent) resources.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = AgentsClient.Create();
    // Initialize request argument(s)
    ListAgentsRequest request = new ListAgentsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    PagedEnumerable<ListAgentsResponse, Agent> response = agentsClient.ListAgents(request);
    
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

Returns the list of all agents in the specified location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The location to list all agents for. Format: `projects/<ProjectID>/locations/<LocationID>`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListAgentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListAgentsResponse)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent)` | A pageable sequence of [Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent) resources.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = AgentsClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListAgentsResponse, Agent> response = agentsClient.ListAgents(parent);
    
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
    

### ListAgentsAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListAgentsResponse, Agent> ListAgentsAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Returns the list of all agents in the specified location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The location to list all agents for. Format: `projects/<ProjectID>/locations/<LocationID>`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListAgentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListAgentsResponse)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent)` | A pageable asynchronous sequence of [Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent) resources.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListAgentsResponse, Agent> response = agentsClient.ListAgentsAsync(parent);
    
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

Returns the list of all agents in the specified location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAgentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListAgentsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListAgentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListAgentsResponse)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent)` | A pageable asynchronous sequence of [Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent) resources.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    ListAgentsRequest request = new ListAgentsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    PagedAsyncEnumerable<ListAgentsResponse, Agent> response = agentsClient.ListAgentsAsync(request);
    
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

Returns the list of all agents in the specified location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The location to list all agents for. Format: `projects/<ProjectID>/locations/<LocationID>`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListAgentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListAgentsResponse)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent)` | A pageable asynchronous sequence of [Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent) resources.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListAgentsResponse, Agent> response = agentsClient.ListAgentsAsync(parent);
    
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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportAgentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportAgentResponse)[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` | The result of polling the operation.  
  
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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportAgentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportAgentResponse)[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` | A task representing the result of polling the operation.  
  
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
  
### RestoreAgent(RestoreAgentRequest, CallSettings)
    
    
    public virtual Operation<Empty, Struct> RestoreAgent(RestoreAgentRequest request, CallSettings callSettings = null)

Restores the specified agent from a binary file.

Replaces the current agent with a new one. Note that all existing resources in agent (e.g. intents, entity types, flows) will be removed.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
  * `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)



Note: You should always train flows prior to sending them queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RestoreAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.RestoreAgentRequest)`  
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
        AgentName = AgentName.FromProjectLocationAgent("[PROJECT]", "[LOCATION]", "[AGENT]"),
        AgentUri = "",
        RestoreOption = RestoreAgentRequest.Types.RestoreOption.Unspecified,
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

Restores the specified agent from a binary file.

Replaces the current agent with a new one. Note that all existing resources in agent (e.g. intents, entity types, flows) will be removed.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
  * `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)



Note: You should always train flows prior to sending them queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RestoreAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.RestoreAgentRequest)`  
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
        AgentName = AgentName.FromProjectLocationAgent("[PROJECT]", "[LOCATION]", "[AGENT]"),
        AgentUri = "",
        RestoreOption = RestoreAgentRequest.Types.RestoreOption.Unspecified,
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

Restores the specified agent from a binary file.

Replaces the current agent with a new one. Note that all existing resources in agent (e.g. intents, entity types, flows) will be removed.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

  * `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
  * `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)



Note: You should always train flows prior to sending them queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RestoreAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.RestoreAgentRequest)`  
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
        AgentName = AgentName.FromProjectLocationAgent("[PROJECT]", "[LOCATION]", "[AGENT]"),
        AgentUri = "",
        RestoreOption = RestoreAgentRequest.Types.RestoreOption.Unspecified,
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
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentsClient#Google_Cloud_Dialogflow_Cx_V3_AgentsClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentsClient#Google_Cloud_Dialogflow_Cx_V3_AgentsClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentsClient#Google_Cloud_Dialogflow_Cx_V3_AgentsClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentsClient#Google_Cloud_Dialogflow_Cx_V3_AgentsClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### UpdateAgent(Agent, FieldMask, CallSettings)
    
    
    public virtual Agent UpdateAgent(Agent agent, FieldMask updateMask, CallSettings callSettings = null)

Updates the specified agent.

Note: You should always train flows prior to sending them queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

**Parameters**  
---  
**Name** | **Description**  
`agent` | `[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent)`  
Required. The agent to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
The mask to control which fields get updated. If the mask is not present, all fields will be updated.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = AgentsClient.Create();
    // Initialize request argument(s)
    Agent agent = new Agent();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Agent response = agentsClient.UpdateAgent(agent, updateMask);
    

### UpdateAgent(UpdateAgentRequest, CallSettings)
    
    
    public virtual Agent UpdateAgent(UpdateAgentRequest request, CallSettings callSettings = null)

Updates the specified agent.

Note: You should always train flows prior to sending them queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.UpdateAgentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = AgentsClient.Create();
    // Initialize request argument(s)
    UpdateAgentRequest request = new UpdateAgentRequest
    {
        Agent = new Agent(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Agent response = agentsClient.UpdateAgent(request);
    

### UpdateAgentAsync(Agent, FieldMask, CallSettings)
    
    
    public virtual Task<Agent> UpdateAgentAsync(Agent agent, FieldMask updateMask, CallSettings callSettings = null)

Updates the specified agent.

Note: You should always train flows prior to sending them queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

**Parameters**  
---  
**Name** | **Description**  
`agent` | `[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent)`  
Required. The agent to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
The mask to control which fields get updated. If the mask is not present, all fields will be updated.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    Agent agent = new Agent();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Agent response = await agentsClient.UpdateAgentAsync(agent, updateMask);
    

### UpdateAgentAsync(Agent, FieldMask, CancellationToken)
    
    
    public virtual Task<Agent> UpdateAgentAsync(Agent agent, FieldMask updateMask, CancellationToken cancellationToken)

Updates the specified agent.

Note: You should always train flows prior to sending them queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

**Parameters**  
---  
**Name** | **Description**  
`agent` | `[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent)`  
Required. The agent to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
The mask to control which fields get updated. If the mask is not present, all fields will be updated.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    Agent agent = new Agent();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Agent response = await agentsClient.UpdateAgentAsync(agent, updateMask);
    

### UpdateAgentAsync(UpdateAgentRequest, CallSettings)
    
    
    public virtual Task<Agent> UpdateAgentAsync(UpdateAgentRequest request, CallSettings callSettings = null)

Updates the specified agent.

Note: You should always train flows prior to sending them queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.UpdateAgentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    UpdateAgentRequest request = new UpdateAgentRequest
    {
        Agent = new Agent(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Agent response = await agentsClient.UpdateAgentAsync(request);
    

### UpdateAgentAsync(UpdateAgentRequest, CancellationToken)
    
    
    public virtual Task<Agent> UpdateAgentAsync(UpdateAgentRequest request, CancellationToken cancellationToken)

Updates the specified agent.

Note: You should always train flows prior to sending them queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.UpdateAgentRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    UpdateAgentRequest request = new UpdateAgentRequest
    {
        Agent = new Agent(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Agent response = await agentsClient.UpdateAgentAsync(request);
    

### UpdateGenerativeSettings(GenerativeSettings, FieldMask, CallSettings)
    
    
    public virtual GenerativeSettings UpdateGenerativeSettings(GenerativeSettings generativeSettings, FieldMask updateMask, CallSettings callSettings = null)

Updates the generative settings for the agent.

**Parameters**  
---  
**Name** | **Description**  
`generativeSettings` | `[GenerativeSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GenerativeSettings)`  
Required. Generative settings to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. The mask to control which fields get updated. If the mask is not present, all fields will be updated.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[GenerativeSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GenerativeSettings)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = AgentsClient.Create();
    // Initialize request argument(s)
    GenerativeSettings generativeSettings = new GenerativeSettings();
    FieldMask updateMask = new FieldMask();
    // Make the request
    GenerativeSettings response = agentsClient.UpdateGenerativeSettings(generativeSettings, updateMask);
    

### UpdateGenerativeSettings(UpdateGenerativeSettingsRequest, CallSettings)
    
    
    public virtual GenerativeSettings UpdateGenerativeSettings(UpdateGenerativeSettingsRequest request, CallSettings callSettings = null)

Updates the generative settings for the agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateGenerativeSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.UpdateGenerativeSettingsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[GenerativeSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GenerativeSettings)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = AgentsClient.Create();
    // Initialize request argument(s)
    UpdateGenerativeSettingsRequest request = new UpdateGenerativeSettingsRequest
    {
        GenerativeSettings = new GenerativeSettings(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    GenerativeSettings response = agentsClient.UpdateGenerativeSettings(request);
    

### UpdateGenerativeSettingsAsync(GenerativeSettings, FieldMask, CallSettings)
    
    
    public virtual Task<GenerativeSettings> UpdateGenerativeSettingsAsync(GenerativeSettings generativeSettings, FieldMask updateMask, CallSettings callSettings = null)

Updates the generative settings for the agent.

**Parameters**  
---  
**Name** | **Description**  
`generativeSettings` | `[GenerativeSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GenerativeSettings)`  
Required. Generative settings to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. The mask to control which fields get updated. If the mask is not present, all fields will be updated.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GenerativeSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GenerativeSettings)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    GenerativeSettings generativeSettings = new GenerativeSettings();
    FieldMask updateMask = new FieldMask();
    // Make the request
    GenerativeSettings response = await agentsClient.UpdateGenerativeSettingsAsync(generativeSettings, updateMask);
    

### UpdateGenerativeSettingsAsync(GenerativeSettings, FieldMask, CancellationToken)
    
    
    public virtual Task<GenerativeSettings> UpdateGenerativeSettingsAsync(GenerativeSettings generativeSettings, FieldMask updateMask, CancellationToken cancellationToken)

Updates the generative settings for the agent.

**Parameters**  
---  
**Name** | **Description**  
`generativeSettings` | `[GenerativeSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GenerativeSettings)`  
Required. Generative settings to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. The mask to control which fields get updated. If the mask is not present, all fields will be updated.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GenerativeSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GenerativeSettings)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    GenerativeSettings generativeSettings = new GenerativeSettings();
    FieldMask updateMask = new FieldMask();
    // Make the request
    GenerativeSettings response = await agentsClient.UpdateGenerativeSettingsAsync(generativeSettings, updateMask);
    

### UpdateGenerativeSettingsAsync(UpdateGenerativeSettingsRequest, CallSettings)
    
    
    public virtual Task<GenerativeSettings> UpdateGenerativeSettingsAsync(UpdateGenerativeSettingsRequest request, CallSettings callSettings = null)

Updates the generative settings for the agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateGenerativeSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.UpdateGenerativeSettingsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GenerativeSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GenerativeSettings)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    UpdateGenerativeSettingsRequest request = new UpdateGenerativeSettingsRequest
    {
        GenerativeSettings = new GenerativeSettings(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    GenerativeSettings response = await agentsClient.UpdateGenerativeSettingsAsync(request);
    

### UpdateGenerativeSettingsAsync(UpdateGenerativeSettingsRequest, CancellationToken)
    
    
    public virtual Task<GenerativeSettings> UpdateGenerativeSettingsAsync(UpdateGenerativeSettingsRequest request, CancellationToken cancellationToken)

Updates the generative settings for the agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateGenerativeSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.UpdateGenerativeSettingsRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GenerativeSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GenerativeSettings)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    UpdateGenerativeSettingsRequest request = new UpdateGenerativeSettingsRequest
    {
        GenerativeSettings = new GenerativeSettings(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    GenerativeSettings response = await agentsClient.UpdateGenerativeSettingsAsync(request);
    

### ValidateAgent(ValidateAgentRequest, CallSettings)
    
    
    public virtual AgentValidationResult ValidateAgent(ValidateAgentRequest request, CallSettings callSettings = null)

Validates the specified agent and creates or updates validation results. The agent in draft version is validated. Please call this API after the training is completed to get the complete validation results.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ValidateAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ValidateAgentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[AgentValidationResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentValidationResult)` | The RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = AgentsClient.Create();
    // Initialize request argument(s)
    ValidateAgentRequest request = new ValidateAgentRequest
    {
        AgentName = AgentName.FromProjectLocationAgent("[PROJECT]", "[LOCATION]", "[AGENT]"),
        LanguageCode = "",
    };
    // Make the request
    AgentValidationResult response = agentsClient.ValidateAgent(request);
    

### ValidateAgentAsync(ValidateAgentRequest, CallSettings)
    
    
    public virtual Task<AgentValidationResult> ValidateAgentAsync(ValidateAgentRequest request, CallSettings callSettings = null)

Validates the specified agent and creates or updates validation results. The agent in draft version is validated. Please call this API after the training is completed to get the complete validation results.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ValidateAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ValidateAgentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AgentValidationResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentValidationResult)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    ValidateAgentRequest request = new ValidateAgentRequest
    {
        AgentName = AgentName.FromProjectLocationAgent("[PROJECT]", "[LOCATION]", "[AGENT]"),
        LanguageCode = "",
    };
    // Make the request
    AgentValidationResult response = await agentsClient.ValidateAgentAsync(request);
    

### ValidateAgentAsync(ValidateAgentRequest, CancellationToken)
    
    
    public virtual Task<AgentValidationResult> ValidateAgentAsync(ValidateAgentRequest request, CancellationToken cancellationToken)

Validates the specified agent and creates or updates validation results. The agent in draft version is validated. Please call this API after the training is completed to get the complete validation results.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ValidateAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ValidateAgentRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AgentValidationResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentValidationResult)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AgentsClient agentsClient = await AgentsClient.CreateAsync();
    // Initialize request argument(s)
    ValidateAgentRequest request = new ValidateAgentRequest
    {
        AgentName = AgentName.FromProjectLocationAgent("[PROJECT]", "[LOCATION]", "[AGENT]"),
        LanguageCode = "",
    };
    // Make the request
    AgentValidationResult response = await agentsClient.ValidateAgentAsync(request);
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
