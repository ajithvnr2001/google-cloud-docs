---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgentsClient
title: Google Cloud Dialogflow v2 API - Class CompanionAgentsClient (4.33.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:58:20.977242+00:00
---

# Google Cloud Dialogflow v2 API - Class CompanionAgentsClient (4.33.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgentsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Dialogflow v2 API - Class CompanionAgentsClient (4.33.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.33.0 (latest)  4.32.0  4.31.0  4.30.0  4.29.0  4.28.0  4.27.0  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.16.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.0  4.8.0  4.7.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0 
    
    
    public abstract class CompanionAgentsClient

Reference documentation and code samples for the Google Cloud Dialogflow v2 API class CompanionAgentsClient.

CompanionAgents client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CompanionAgentsClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[CompanionAgentsClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgentsClientImpl)

## Namespace

[Google.Cloud.Dialogflow.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2)

## Assembly

Google.Cloud.Dialogflow.V2.dll

## Remarks

Service for managing companion agents.

## Properties 

### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the CompanionAgents service, which is a host of "dialogflow.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default CompanionAgents scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default CompanionAgents scopes are:

  * <https://www.googleapis.com/auth/cloud-platform>
  * <https://www.googleapis.com/auth/dialogflow>



### GrpcClient
    
    
    public virtual CompanionAgents.CompanionAgentsClient GrpcClient { get; }

The underlying gRPC CompanionAgents client

**Property Value**  
---  
**Type** | **Description**  
`[CompanionAgents](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgents)[CompanionAgentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgents.CompanionAgentsClient)` |   
  
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

### Create()
    
    
    public static CompanionAgentsClient Create()

Synchronously creates a [CompanionAgentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgentsClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [CompanionAgentsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgentsClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[CompanionAgentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgentsClient)` | The created [CompanionAgentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgentsClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<CompanionAgentsClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [CompanionAgentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgentsClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [CompanionAgentsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgentsClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CompanionAgentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgentsClient)` | The task representing the created [CompanionAgentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgentsClient).  
  
### CreateCompanionAgent(LocationName, CompanionAgent, string, CallSettings)
    
    
    public virtual CompanionAgent CreateCompanionAgent(LocationName parent, CompanionAgent companionAgent, string companionAgentId, CallSettings callSettings = null)

Creates a companion agent.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Resource identifier of the project creating the companion agent. Format: `projects/{project}/locations/{location}`  
`companionAgent` | `[CompanionAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent)`  
Required. The companion agent to create.  
`companionAgentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The resource ID of the companion agent to create. If not provided, the server will auto-generate a resource ID.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[CompanionAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent)` | The RPC response.  
**Example**
    
    
    // Create client
    CompanionAgentsClient companionAgentsClient = CompanionAgentsClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    CompanionAgent companionAgent = new CompanionAgent();
    string companionAgentId = "";
    // Make the request
    CompanionAgent response = companionAgentsClient.CreateCompanionAgent(parent, companionAgent, companionAgentId);
    

### CreateCompanionAgent(CreateCompanionAgentRequest, CallSettings)
    
    
    public virtual CompanionAgent CreateCompanionAgent(CreateCompanionAgentRequest request, CallSettings callSettings = null)

Creates a companion agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateCompanionAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CreateCompanionAgentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[CompanionAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent)` | The RPC response.  
**Example**
    
    
    // Create client
    CompanionAgentsClient companionAgentsClient = CompanionAgentsClient.Create();
    // Initialize request argument(s)
    CreateCompanionAgentRequest request = new CreateCompanionAgentRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        CompanionAgent = new CompanionAgent(),
        CompanionAgentId = "",
    };
    // Make the request
    CompanionAgent response = companionAgentsClient.CreateCompanionAgent(request);
    

### CreateCompanionAgent(string, CompanionAgent, string, CallSettings)
    
    
    public virtual CompanionAgent CreateCompanionAgent(string parent, CompanionAgent companionAgent, string companionAgentId, CallSettings callSettings = null)

Creates a companion agent.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Resource identifier of the project creating the companion agent. Format: `projects/{project}/locations/{location}`  
`companionAgent` | `[CompanionAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent)`  
Required. The companion agent to create.  
`companionAgentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The resource ID of the companion agent to create. If not provided, the server will auto-generate a resource ID.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[CompanionAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent)` | The RPC response.  
**Example**
    
    
    // Create client
    CompanionAgentsClient companionAgentsClient = CompanionAgentsClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    CompanionAgent companionAgent = new CompanionAgent();
    string companionAgentId = "";
    // Make the request
    CompanionAgent response = companionAgentsClient.CreateCompanionAgent(parent, companionAgent, companionAgentId);
    

### CreateCompanionAgentAsync(LocationName, CompanionAgent, string, CallSettings)
    
    
    public virtual Task<CompanionAgent> CreateCompanionAgentAsync(LocationName parent, CompanionAgent companionAgent, string companionAgentId, CallSettings callSettings = null)

Creates a companion agent.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Resource identifier of the project creating the companion agent. Format: `projects/{project}/locations/{location}`  
`companionAgent` | `[CompanionAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent)`  
Required. The companion agent to create.  
`companionAgentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The resource ID of the companion agent to create. If not provided, the server will auto-generate a resource ID.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CompanionAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CompanionAgentsClient companionAgentsClient = await CompanionAgentsClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    CompanionAgent companionAgent = new CompanionAgent();
    string companionAgentId = "";
    // Make the request
    CompanionAgent response = await companionAgentsClient.CreateCompanionAgentAsync(parent, companionAgent, companionAgentId);
    

### CreateCompanionAgentAsync(LocationName, CompanionAgent, string, CancellationToken)
    
    
    public virtual Task<CompanionAgent> CreateCompanionAgentAsync(LocationName parent, CompanionAgent companionAgent, string companionAgentId, CancellationToken cancellationToken)

Creates a companion agent.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Resource identifier of the project creating the companion agent. Format: `projects/{project}/locations/{location}`  
`companionAgent` | `[CompanionAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent)`  
Required. The companion agent to create.  
`companionAgentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The resource ID of the companion agent to create. If not provided, the server will auto-generate a resource ID.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CompanionAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CompanionAgentsClient companionAgentsClient = await CompanionAgentsClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    CompanionAgent companionAgent = new CompanionAgent();
    string companionAgentId = "";
    // Make the request
    CompanionAgent response = await companionAgentsClient.CreateCompanionAgentAsync(parent, companionAgent, companionAgentId);
    

### CreateCompanionAgentAsync(CreateCompanionAgentRequest, CallSettings)
    
    
    public virtual Task<CompanionAgent> CreateCompanionAgentAsync(CreateCompanionAgentRequest request, CallSettings callSettings = null)

Creates a companion agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateCompanionAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CreateCompanionAgentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CompanionAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CompanionAgentsClient companionAgentsClient = await CompanionAgentsClient.CreateAsync();
    // Initialize request argument(s)
    CreateCompanionAgentRequest request = new CreateCompanionAgentRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        CompanionAgent = new CompanionAgent(),
        CompanionAgentId = "",
    };
    // Make the request
    CompanionAgent response = await companionAgentsClient.CreateCompanionAgentAsync(request);
    

### CreateCompanionAgentAsync(CreateCompanionAgentRequest, CancellationToken)
    
    
    public virtual Task<CompanionAgent> CreateCompanionAgentAsync(CreateCompanionAgentRequest request, CancellationToken cancellationToken)

Creates a companion agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateCompanionAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CreateCompanionAgentRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CompanionAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CompanionAgentsClient companionAgentsClient = await CompanionAgentsClient.CreateAsync();
    // Initialize request argument(s)
    CreateCompanionAgentRequest request = new CreateCompanionAgentRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        CompanionAgent = new CompanionAgent(),
        CompanionAgentId = "",
    };
    // Make the request
    CompanionAgent response = await companionAgentsClient.CreateCompanionAgentAsync(request);
    

### CreateCompanionAgentAsync(string, CompanionAgent, string, CallSettings)
    
    
    public virtual Task<CompanionAgent> CreateCompanionAgentAsync(string parent, CompanionAgent companionAgent, string companionAgentId, CallSettings callSettings = null)

Creates a companion agent.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Resource identifier of the project creating the companion agent. Format: `projects/{project}/locations/{location}`  
`companionAgent` | `[CompanionAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent)`  
Required. The companion agent to create.  
`companionAgentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The resource ID of the companion agent to create. If not provided, the server will auto-generate a resource ID.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CompanionAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CompanionAgentsClient companionAgentsClient = await CompanionAgentsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    CompanionAgent companionAgent = new CompanionAgent();
    string companionAgentId = "";
    // Make the request
    CompanionAgent response = await companionAgentsClient.CreateCompanionAgentAsync(parent, companionAgent, companionAgentId);
    

### CreateCompanionAgentAsync(string, CompanionAgent, string, CancellationToken)
    
    
    public virtual Task<CompanionAgent> CreateCompanionAgentAsync(string parent, CompanionAgent companionAgent, string companionAgentId, CancellationToken cancellationToken)

Creates a companion agent.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Resource identifier of the project creating the companion agent. Format: `projects/{project}/locations/{location}`  
`companionAgent` | `[CompanionAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent)`  
Required. The companion agent to create.  
`companionAgentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The resource ID of the companion agent to create. If not provided, the server will auto-generate a resource ID.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CompanionAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CompanionAgentsClient companionAgentsClient = await CompanionAgentsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    CompanionAgent companionAgent = new CompanionAgent();
    string companionAgentId = "";
    // Make the request
    CompanionAgent response = await companionAgentsClient.CreateCompanionAgentAsync(parent, companionAgent, companionAgentId);
    

### DeleteCompanionAgent(CompanionAgentName, CallSettings)
    
    
    public virtual void DeleteCompanionAgent(CompanionAgentName name, CallSettings callSettings = null)

Deletes a companion agent.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[CompanionAgentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgentName)`  
Required. The unique resource identifier of the CompanionAgent to delete. Format: `projects/{project}/locations/{location}/companionAgents/{companion_agent}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    CompanionAgentsClient companionAgentsClient = CompanionAgentsClient.Create();
    // Initialize request argument(s)
    CompanionAgentName name = CompanionAgentName.FromProjectLocationCompanionAgent("[PROJECT]", "[LOCATION]", "[COMPANION_AGENT]");
    // Make the request
    companionAgentsClient.DeleteCompanionAgent(name);
    

### DeleteCompanionAgent(DeleteCompanionAgentRequest, CallSettings)
    
    
    public virtual void DeleteCompanionAgent(DeleteCompanionAgentRequest request, CallSettings callSettings = null)

Deletes a companion agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteCompanionAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.DeleteCompanionAgentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    CompanionAgentsClient companionAgentsClient = CompanionAgentsClient.Create();
    // Initialize request argument(s)
    DeleteCompanionAgentRequest request = new DeleteCompanionAgentRequest
    {
        CompanionAgentName = CompanionAgentName.FromProjectLocationCompanionAgent("[PROJECT]", "[LOCATION]", "[COMPANION_AGENT]"),
    };
    // Make the request
    companionAgentsClient.DeleteCompanionAgent(request);
    

### DeleteCompanionAgent(string, CallSettings)
    
    
    public virtual void DeleteCompanionAgent(string name, CallSettings callSettings = null)

Deletes a companion agent.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The unique resource identifier of the CompanionAgent to delete. Format: `projects/{project}/locations/{location}/companionAgents/{companion_agent}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    CompanionAgentsClient companionAgentsClient = CompanionAgentsClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/companionAgents/[COMPANION_AGENT]";
    // Make the request
    companionAgentsClient.DeleteCompanionAgent(name);
    

### DeleteCompanionAgentAsync(CompanionAgentName, CallSettings)
    
    
    public virtual Task DeleteCompanionAgentAsync(CompanionAgentName name, CallSettings callSettings = null)

Deletes a companion agent.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[CompanionAgentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgentName)`  
Required. The unique resource identifier of the CompanionAgent to delete. Format: `projects/{project}/locations/{location}/companionAgents/{companion_agent}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CompanionAgentsClient companionAgentsClient = await CompanionAgentsClient.CreateAsync();
    // Initialize request argument(s)
    CompanionAgentName name = CompanionAgentName.FromProjectLocationCompanionAgent("[PROJECT]", "[LOCATION]", "[COMPANION_AGENT]");
    // Make the request
    await companionAgentsClient.DeleteCompanionAgentAsync(name);
    

### DeleteCompanionAgentAsync(CompanionAgentName, CancellationToken)
    
    
    public virtual Task DeleteCompanionAgentAsync(CompanionAgentName name, CancellationToken cancellationToken)

Deletes a companion agent.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[CompanionAgentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgentName)`  
Required. The unique resource identifier of the CompanionAgent to delete. Format: `projects/{project}/locations/{location}/companionAgents/{companion_agent}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CompanionAgentsClient companionAgentsClient = await CompanionAgentsClient.CreateAsync();
    // Initialize request argument(s)
    CompanionAgentName name = CompanionAgentName.FromProjectLocationCompanionAgent("[PROJECT]", "[LOCATION]", "[COMPANION_AGENT]");
    // Make the request
    await companionAgentsClient.DeleteCompanionAgentAsync(name);
    

### DeleteCompanionAgentAsync(DeleteCompanionAgentRequest, CallSettings)
    
    
    public virtual Task DeleteCompanionAgentAsync(DeleteCompanionAgentRequest request, CallSettings callSettings = null)

Deletes a companion agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteCompanionAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.DeleteCompanionAgentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CompanionAgentsClient companionAgentsClient = await CompanionAgentsClient.CreateAsync();
    // Initialize request argument(s)
    DeleteCompanionAgentRequest request = new DeleteCompanionAgentRequest
    {
        CompanionAgentName = CompanionAgentName.FromProjectLocationCompanionAgent("[PROJECT]", "[LOCATION]", "[COMPANION_AGENT]"),
    };
    // Make the request
    await companionAgentsClient.DeleteCompanionAgentAsync(request);
    

### DeleteCompanionAgentAsync(DeleteCompanionAgentRequest, CancellationToken)
    
    
    public virtual Task DeleteCompanionAgentAsync(DeleteCompanionAgentRequest request, CancellationToken cancellationToken)

Deletes a companion agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteCompanionAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.DeleteCompanionAgentRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CompanionAgentsClient companionAgentsClient = await CompanionAgentsClient.CreateAsync();
    // Initialize request argument(s)
    DeleteCompanionAgentRequest request = new DeleteCompanionAgentRequest
    {
        CompanionAgentName = CompanionAgentName.FromProjectLocationCompanionAgent("[PROJECT]", "[LOCATION]", "[COMPANION_AGENT]"),
    };
    // Make the request
    await companionAgentsClient.DeleteCompanionAgentAsync(request);
    

### DeleteCompanionAgentAsync(string, CallSettings)
    
    
    public virtual Task DeleteCompanionAgentAsync(string name, CallSettings callSettings = null)

Deletes a companion agent.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The unique resource identifier of the CompanionAgent to delete. Format: `projects/{project}/locations/{location}/companionAgents/{companion_agent}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CompanionAgentsClient companionAgentsClient = await CompanionAgentsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/companionAgents/[COMPANION_AGENT]";
    // Make the request
    await companionAgentsClient.DeleteCompanionAgentAsync(name);
    

### DeleteCompanionAgentAsync(string, CancellationToken)
    
    
    public virtual Task DeleteCompanionAgentAsync(string name, CancellationToken cancellationToken)

Deletes a companion agent.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The unique resource identifier of the CompanionAgent to delete. Format: `projects/{project}/locations/{location}/companionAgents/{companion_agent}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CompanionAgentsClient companionAgentsClient = await CompanionAgentsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/companionAgents/[COMPANION_AGENT]";
    // Make the request
    await companionAgentsClient.DeleteCompanionAgentAsync(name);
    

### GetCompanionAgent(CompanionAgentName, CallSettings)
    
    
    public virtual CompanionAgent GetCompanionAgent(CompanionAgentName name, CallSettings callSettings = null)

Gets a companion agent.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[CompanionAgentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgentName)`  
Required. The unique resource identifier of the CompanionAgent to get all information for. Format: `projects/{project}/locations/{location}/companionAgents/{companion_agent}`. Contains the information about the {project}, {location}, and {companion_agent}.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[CompanionAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent)` | The RPC response.  
**Example**
    
    
    // Create client
    CompanionAgentsClient companionAgentsClient = CompanionAgentsClient.Create();
    // Initialize request argument(s)
    CompanionAgentName name = CompanionAgentName.FromProjectLocationCompanionAgent("[PROJECT]", "[LOCATION]", "[COMPANION_AGENT]");
    // Make the request
    CompanionAgent response = companionAgentsClient.GetCompanionAgent(name);
    

### GetCompanionAgent(GetCompanionAgentRequest, CallSettings)
    
    
    public virtual CompanionAgent GetCompanionAgent(GetCompanionAgentRequest request, CallSettings callSettings = null)

Gets a companion agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCompanionAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.GetCompanionAgentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[CompanionAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent)` | The RPC response.  
**Example**
    
    
    // Create client
    CompanionAgentsClient companionAgentsClient = CompanionAgentsClient.Create();
    // Initialize request argument(s)
    GetCompanionAgentRequest request = new GetCompanionAgentRequest
    {
        CompanionAgentName = CompanionAgentName.FromProjectLocationCompanionAgent("[PROJECT]", "[LOCATION]", "[COMPANION_AGENT]"),
    };
    // Make the request
    CompanionAgent response = companionAgentsClient.GetCompanionAgent(request);
    

### GetCompanionAgent(string, CallSettings)
    
    
    public virtual CompanionAgent GetCompanionAgent(string name, CallSettings callSettings = null)

Gets a companion agent.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The unique resource identifier of the CompanionAgent to get all information for. Format: `projects/{project}/locations/{location}/companionAgents/{companion_agent}`. Contains the information about the {project}, {location}, and {companion_agent}.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[CompanionAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent)` | The RPC response.  
**Example**
    
    
    // Create client
    CompanionAgentsClient companionAgentsClient = CompanionAgentsClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/companionAgents/[COMPANION_AGENT]";
    // Make the request
    CompanionAgent response = companionAgentsClient.GetCompanionAgent(name);
    

### GetCompanionAgentAsync(CompanionAgentName, CallSettings)
    
    
    public virtual Task<CompanionAgent> GetCompanionAgentAsync(CompanionAgentName name, CallSettings callSettings = null)

Gets a companion agent.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[CompanionAgentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgentName)`  
Required. The unique resource identifier of the CompanionAgent to get all information for. Format: `projects/{project}/locations/{location}/companionAgents/{companion_agent}`. Contains the information about the {project}, {location}, and {companion_agent}.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CompanionAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CompanionAgentsClient companionAgentsClient = await CompanionAgentsClient.CreateAsync();
    // Initialize request argument(s)
    CompanionAgentName name = CompanionAgentName.FromProjectLocationCompanionAgent("[PROJECT]", "[LOCATION]", "[COMPANION_AGENT]");
    // Make the request
    CompanionAgent response = await companionAgentsClient.GetCompanionAgentAsync(name);
    

### GetCompanionAgentAsync(CompanionAgentName, CancellationToken)
    
    
    public virtual Task<CompanionAgent> GetCompanionAgentAsync(CompanionAgentName name, CancellationToken cancellationToken)

Gets a companion agent.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[CompanionAgentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgentName)`  
Required. The unique resource identifier of the CompanionAgent to get all information for. Format: `projects/{project}/locations/{location}/companionAgents/{companion_agent}`. Contains the information about the {project}, {location}, and {companion_agent}.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CompanionAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CompanionAgentsClient companionAgentsClient = await CompanionAgentsClient.CreateAsync();
    // Initialize request argument(s)
    CompanionAgentName name = CompanionAgentName.FromProjectLocationCompanionAgent("[PROJECT]", "[LOCATION]", "[COMPANION_AGENT]");
    // Make the request
    CompanionAgent response = await companionAgentsClient.GetCompanionAgentAsync(name);
    

### GetCompanionAgentAsync(GetCompanionAgentRequest, CallSettings)
    
    
    public virtual Task<CompanionAgent> GetCompanionAgentAsync(GetCompanionAgentRequest request, CallSettings callSettings = null)

Gets a companion agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCompanionAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.GetCompanionAgentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CompanionAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CompanionAgentsClient companionAgentsClient = await CompanionAgentsClient.CreateAsync();
    // Initialize request argument(s)
    GetCompanionAgentRequest request = new GetCompanionAgentRequest
    {
        CompanionAgentName = CompanionAgentName.FromProjectLocationCompanionAgent("[PROJECT]", "[LOCATION]", "[COMPANION_AGENT]"),
    };
    // Make the request
    CompanionAgent response = await companionAgentsClient.GetCompanionAgentAsync(request);
    

### GetCompanionAgentAsync(GetCompanionAgentRequest, CancellationToken)
    
    
    public virtual Task<CompanionAgent> GetCompanionAgentAsync(GetCompanionAgentRequest request, CancellationToken cancellationToken)

Gets a companion agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCompanionAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.GetCompanionAgentRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CompanionAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CompanionAgentsClient companionAgentsClient = await CompanionAgentsClient.CreateAsync();
    // Initialize request argument(s)
    GetCompanionAgentRequest request = new GetCompanionAgentRequest
    {
        CompanionAgentName = CompanionAgentName.FromProjectLocationCompanionAgent("[PROJECT]", "[LOCATION]", "[COMPANION_AGENT]"),
    };
    // Make the request
    CompanionAgent response = await companionAgentsClient.GetCompanionAgentAsync(request);
    

### GetCompanionAgentAsync(string, CallSettings)
    
    
    public virtual Task<CompanionAgent> GetCompanionAgentAsync(string name, CallSettings callSettings = null)

Gets a companion agent.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The unique resource identifier of the CompanionAgent to get all information for. Format: `projects/{project}/locations/{location}/companionAgents/{companion_agent}`. Contains the information about the {project}, {location}, and {companion_agent}.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CompanionAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CompanionAgentsClient companionAgentsClient = await CompanionAgentsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/companionAgents/[COMPANION_AGENT]";
    // Make the request
    CompanionAgent response = await companionAgentsClient.GetCompanionAgentAsync(name);
    

### GetCompanionAgentAsync(string, CancellationToken)
    
    
    public virtual Task<CompanionAgent> GetCompanionAgentAsync(string name, CancellationToken cancellationToken)

Gets a companion agent.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The unique resource identifier of the CompanionAgent to get all information for. Format: `projects/{project}/locations/{location}/companionAgents/{companion_agent}`. Contains the information about the {project}, {location}, and {companion_agent}.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CompanionAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CompanionAgentsClient companionAgentsClient = await CompanionAgentsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/companionAgents/[COMPANION_AGENT]";
    // Make the request
    CompanionAgent response = await companionAgentsClient.GetCompanionAgentAsync(name);
    

### ListCompanionAgents(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListCompanionAgentsResponse, CompanionAgent> ListCompanionAgents(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists companion agents.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent resource name to list the companion agents for. Format: `projects/{project}/locations/{location}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListCompanionAgentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ListCompanionAgentsResponse)[CompanionAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent)` | A pageable sequence of [CompanionAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent) resources.  
**Example**
    
    
    // Create client
    CompanionAgentsClient companionAgentsClient = CompanionAgentsClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListCompanionAgentsResponse, CompanionAgent> response = companionAgentsClient.ListCompanionAgents(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (CompanionAgent item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListCompanionAgentsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (CompanionAgent item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<CompanionAgent> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (CompanionAgent item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListCompanionAgents(ListCompanionAgentsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListCompanionAgentsResponse, CompanionAgent> ListCompanionAgents(ListCompanionAgentsRequest request, CallSettings callSettings = null)

Lists companion agents.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListCompanionAgentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ListCompanionAgentsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListCompanionAgentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ListCompanionAgentsResponse)[CompanionAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent)` | A pageable sequence of [CompanionAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent) resources.  
**Example**
    
    
    // Create client
    CompanionAgentsClient companionAgentsClient = CompanionAgentsClient.Create();
    // Initialize request argument(s)
    ListCompanionAgentsRequest request = new ListCompanionAgentsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    PagedEnumerable<ListCompanionAgentsResponse, CompanionAgent> response = companionAgentsClient.ListCompanionAgents(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (CompanionAgent item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListCompanionAgentsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (CompanionAgent item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<CompanionAgent> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (CompanionAgent item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListCompanionAgents(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListCompanionAgentsResponse, CompanionAgent> ListCompanionAgents(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists companion agents.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource name to list the companion agents for. Format: `projects/{project}/locations/{location}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListCompanionAgentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ListCompanionAgentsResponse)[CompanionAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent)` | A pageable sequence of [CompanionAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent) resources.  
**Example**
    
    
    // Create client
    CompanionAgentsClient companionAgentsClient = CompanionAgentsClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListCompanionAgentsResponse, CompanionAgent> response = companionAgentsClient.ListCompanionAgents(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (CompanionAgent item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListCompanionAgentsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (CompanionAgent item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<CompanionAgent> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (CompanionAgent item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListCompanionAgentsAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListCompanionAgentsResponse, CompanionAgent> ListCompanionAgentsAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists companion agents.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent resource name to list the companion agents for. Format: `projects/{project}/locations/{location}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListCompanionAgentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ListCompanionAgentsResponse)[CompanionAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent)` | A pageable asynchronous sequence of [CompanionAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent) resources.  
**Example**
    
    
    // Create client
    CompanionAgentsClient companionAgentsClient = await CompanionAgentsClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListCompanionAgentsResponse, CompanionAgent> response = companionAgentsClient.ListCompanionAgentsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (CompanionAgent item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListCompanionAgentsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (CompanionAgent item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<CompanionAgent> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (CompanionAgent item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListCompanionAgentsAsync(ListCompanionAgentsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListCompanionAgentsResponse, CompanionAgent> ListCompanionAgentsAsync(ListCompanionAgentsRequest request, CallSettings callSettings = null)

Lists companion agents.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListCompanionAgentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ListCompanionAgentsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListCompanionAgentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ListCompanionAgentsResponse)[CompanionAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent)` | A pageable asynchronous sequence of [CompanionAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent) resources.  
**Example**
    
    
    // Create client
    CompanionAgentsClient companionAgentsClient = await CompanionAgentsClient.CreateAsync();
    // Initialize request argument(s)
    ListCompanionAgentsRequest request = new ListCompanionAgentsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    PagedAsyncEnumerable<ListCompanionAgentsResponse, CompanionAgent> response = companionAgentsClient.ListCompanionAgentsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (CompanionAgent item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListCompanionAgentsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (CompanionAgent item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<CompanionAgent> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (CompanionAgent item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListCompanionAgentsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListCompanionAgentsResponse, CompanionAgent> ListCompanionAgentsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists companion agents.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource name to list the companion agents for. Format: `projects/{project}/locations/{location}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListCompanionAgentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ListCompanionAgentsResponse)[CompanionAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent)` | A pageable asynchronous sequence of [CompanionAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent) resources.  
**Example**
    
    
    // Create client
    CompanionAgentsClient companionAgentsClient = await CompanionAgentsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListCompanionAgentsResponse, CompanionAgent> response = companionAgentsClient.ListCompanionAgentsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (CompanionAgent item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListCompanionAgentsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (CompanionAgent item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<CompanionAgent> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (CompanionAgent item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgentsClient#Google_Cloud_Dialogflow_V2_CompanionAgentsClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgentsClient#Google_Cloud_Dialogflow_V2_CompanionAgentsClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgentsClient#Google_Cloud_Dialogflow_V2_CompanionAgentsClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgentsClient#Google_Cloud_Dialogflow_V2_CompanionAgentsClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### UpdateCompanionAgent(CompanionAgent, FieldMask, CallSettings)
    
    
    public virtual CompanionAgent UpdateCompanionAgent(CompanionAgent companionAgent, FieldMask updateMask, CallSettings callSettings = null)

Updates a companion agent.

**Parameters**  
---  
**Name** | **Description**  
`companionAgent` | `[CompanionAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent)`  
Required. The Companion Agent to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Update mask for Companion Agent.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[CompanionAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent)` | The RPC response.  
**Example**
    
    
    // Create client
    CompanionAgentsClient companionAgentsClient = CompanionAgentsClient.Create();
    // Initialize request argument(s)
    CompanionAgent companionAgent = new CompanionAgent();
    FieldMask updateMask = new FieldMask();
    // Make the request
    CompanionAgent response = companionAgentsClient.UpdateCompanionAgent(companionAgent, updateMask);
    

### UpdateCompanionAgent(UpdateCompanionAgentRequest, CallSettings)
    
    
    public virtual CompanionAgent UpdateCompanionAgent(UpdateCompanionAgentRequest request, CallSettings callSettings = null)

Updates a companion agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateCompanionAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.UpdateCompanionAgentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[CompanionAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent)` | The RPC response.  
**Example**
    
    
    // Create client
    CompanionAgentsClient companionAgentsClient = CompanionAgentsClient.Create();
    // Initialize request argument(s)
    UpdateCompanionAgentRequest request = new UpdateCompanionAgentRequest
    {
        CompanionAgent = new CompanionAgent(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    CompanionAgent response = companionAgentsClient.UpdateCompanionAgent(request);
    

### UpdateCompanionAgentAsync(CompanionAgent, FieldMask, CallSettings)
    
    
    public virtual Task<CompanionAgent> UpdateCompanionAgentAsync(CompanionAgent companionAgent, FieldMask updateMask, CallSettings callSettings = null)

Updates a companion agent.

**Parameters**  
---  
**Name** | **Description**  
`companionAgent` | `[CompanionAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent)`  
Required. The Companion Agent to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Update mask for Companion Agent.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CompanionAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CompanionAgentsClient companionAgentsClient = await CompanionAgentsClient.CreateAsync();
    // Initialize request argument(s)
    CompanionAgent companionAgent = new CompanionAgent();
    FieldMask updateMask = new FieldMask();
    // Make the request
    CompanionAgent response = await companionAgentsClient.UpdateCompanionAgentAsync(companionAgent, updateMask);
    

### UpdateCompanionAgentAsync(CompanionAgent, FieldMask, CancellationToken)
    
    
    public virtual Task<CompanionAgent> UpdateCompanionAgentAsync(CompanionAgent companionAgent, FieldMask updateMask, CancellationToken cancellationToken)

Updates a companion agent.

**Parameters**  
---  
**Name** | **Description**  
`companionAgent` | `[CompanionAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent)`  
Required. The Companion Agent to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Update mask for Companion Agent.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CompanionAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CompanionAgentsClient companionAgentsClient = await CompanionAgentsClient.CreateAsync();
    // Initialize request argument(s)
    CompanionAgent companionAgent = new CompanionAgent();
    FieldMask updateMask = new FieldMask();
    // Make the request
    CompanionAgent response = await companionAgentsClient.UpdateCompanionAgentAsync(companionAgent, updateMask);
    

### UpdateCompanionAgentAsync(UpdateCompanionAgentRequest, CallSettings)
    
    
    public virtual Task<CompanionAgent> UpdateCompanionAgentAsync(UpdateCompanionAgentRequest request, CallSettings callSettings = null)

Updates a companion agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateCompanionAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.UpdateCompanionAgentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CompanionAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CompanionAgentsClient companionAgentsClient = await CompanionAgentsClient.CreateAsync();
    // Initialize request argument(s)
    UpdateCompanionAgentRequest request = new UpdateCompanionAgentRequest
    {
        CompanionAgent = new CompanionAgent(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    CompanionAgent response = await companionAgentsClient.UpdateCompanionAgentAsync(request);
    

### UpdateCompanionAgentAsync(UpdateCompanionAgentRequest, CancellationToken)
    
    
    public virtual Task<CompanionAgent> UpdateCompanionAgentAsync(UpdateCompanionAgentRequest request, CancellationToken cancellationToken)

Updates a companion agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateCompanionAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.UpdateCompanionAgentRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CompanionAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CompanionAgentsClient companionAgentsClient = await CompanionAgentsClient.CreateAsync();
    // Initialize request argument(s)
    UpdateCompanionAgentRequest request = new UpdateCompanionAgentRequest
    {
        CompanionAgent = new CompanionAgent(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    CompanionAgent response = await companionAgentsClient.UpdateCompanionAgentAsync(request);
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
