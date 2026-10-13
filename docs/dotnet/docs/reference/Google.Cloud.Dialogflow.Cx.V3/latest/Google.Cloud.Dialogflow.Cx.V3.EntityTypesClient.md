---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityTypesClient
title: Dialogflow v3 API - Class EntityTypesClient (3.2.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:38:00.286878+00:00
---

# Dialogflow v3 API - Class EntityTypesClient (3.2.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityTypesClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Dialogflow v3 API - Class EntityTypesClient (3.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.2.0 (latest)  3.1.0  3.0.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public abstract class EntityTypesClient

Reference documentation and code samples for the Dialogflow v3 API class EntityTypesClient.

EntityTypes client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > EntityTypesClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[EntityTypesClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityTypesClientImpl)

## Namespace

[Google.Cloud.Dialogflow.Cx.V3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3)

## Assembly

Google.Cloud.Dialogflow.Cx.V3.dll

## Remarks

Service for managing [EntityTypes][google.cloud.dialogflow.cx.v3.EntityType].

## Properties 

### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the EntityTypes service, which is a host of "dialogflow.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default EntityTypes scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default EntityTypes scopes are:

  * <https://www.googleapis.com/auth/cloud-platform>
  * <https://www.googleapis.com/auth/dialogflow>



### ExportEntityTypesOperationsClient
    
    
    public virtual OperationsClient ExportEntityTypesOperationsClient { get; }

The long-running operations client for `ExportEntityTypes`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### GrpcClient
    
    
    public virtual EntityTypes.EntityTypesClient GrpcClient { get; }

The underlying gRPC EntityTypes client

**Property Value**  
---  
**Type** | **Description**  
`[EntityTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityTypes)[EntityTypesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityTypes.EntityTypesClient)` |   
  
### ImportEntityTypesOperationsClient
    
    
    public virtual OperationsClient ImportEntityTypesOperationsClient { get; }

The long-running operations client for `ImportEntityTypes`.

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
  
### ServiceMetadata
    
    
    public static ServiceMetadata ServiceMetadata { get; }

The service metadata associated with this client type.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceMetadata](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceMetadata.html)` |   
  
## Methods 

### Create()
    
    
    public static EntityTypesClient Create()

Synchronously creates a [EntityTypesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityTypesClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [EntityTypesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityTypesClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[EntityTypesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityTypesClient)` | The created [EntityTypesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityTypesClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<EntityTypesClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [EntityTypesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityTypesClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [EntityTypesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityTypesClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[EntityTypesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityTypesClient)` | The task representing the created [EntityTypesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityTypesClient).  
  
### CreateEntityType(AgentName, EntityType, CallSettings)
    
    
    public virtual EntityType CreateEntityType(AgentName parent, EntityType entityType, CallSettings callSettings = null)

Creates an entity type in the specified agent.

Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AgentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentName)`  
Required. The agent to create a entity type for. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
`entityType` | `[EntityType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityType)`  
Required. The entity type to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[EntityType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityType)` | The RPC response.  
**Example**
    
    
    // Create client
    EntityTypesClient entityTypesClient = EntityTypesClient.Create();
    // Initialize request argument(s)
    AgentName parent = AgentName.FromProjectLocationAgent("[PROJECT]", "[LOCATION]", "[AGENT]");
    EntityType entityType = new EntityType();
    // Make the request
    EntityType response = entityTypesClient.CreateEntityType(parent, entityType);
    

### CreateEntityType(CreateEntityTypeRequest, CallSettings)
    
    
    public virtual EntityType CreateEntityType(CreateEntityTypeRequest request, CallSettings callSettings = null)

Creates an entity type in the specified agent.

Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateEntityTypeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.CreateEntityTypeRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[EntityType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityType)` | The RPC response.  
**Example**
    
    
    // Create client
    EntityTypesClient entityTypesClient = EntityTypesClient.Create();
    // Initialize request argument(s)
    CreateEntityTypeRequest request = new CreateEntityTypeRequest
    {
        ParentAsAgentName = AgentName.FromProjectLocationAgent("[PROJECT]", "[LOCATION]", "[AGENT]"),
        EntityType = new EntityType(),
        LanguageCode = "",
    };
    // Make the request
    EntityType response = entityTypesClient.CreateEntityType(request);
    

### CreateEntityType(string, EntityType, CallSettings)
    
    
    public virtual EntityType CreateEntityType(string parent, EntityType entityType, CallSettings callSettings = null)

Creates an entity type in the specified agent.

Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The agent to create a entity type for. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
`entityType` | `[EntityType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityType)`  
Required. The entity type to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[EntityType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityType)` | The RPC response.  
**Example**
    
    
    // Create client
    EntityTypesClient entityTypesClient = EntityTypesClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/agents/[AGENT]";
    EntityType entityType = new EntityType();
    // Make the request
    EntityType response = entityTypesClient.CreateEntityType(parent, entityType);
    

### CreateEntityTypeAsync(AgentName, EntityType, CallSettings)
    
    
    public virtual Task<EntityType> CreateEntityTypeAsync(AgentName parent, EntityType entityType, CallSettings callSettings = null)

Creates an entity type in the specified agent.

Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AgentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentName)`  
Required. The agent to create a entity type for. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
`entityType` | `[EntityType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityType)`  
Required. The entity type to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[EntityType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityType)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EntityTypesClient entityTypesClient = await EntityTypesClient.CreateAsync();
    // Initialize request argument(s)
    AgentName parent = AgentName.FromProjectLocationAgent("[PROJECT]", "[LOCATION]", "[AGENT]");
    EntityType entityType = new EntityType();
    // Make the request
    EntityType response = await entityTypesClient.CreateEntityTypeAsync(parent, entityType);
    

### CreateEntityTypeAsync(AgentName, EntityType, CancellationToken)
    
    
    public virtual Task<EntityType> CreateEntityTypeAsync(AgentName parent, EntityType entityType, CancellationToken cancellationToken)

Creates an entity type in the specified agent.

Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AgentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentName)`  
Required. The agent to create a entity type for. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
`entityType` | `[EntityType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityType)`  
Required. The entity type to create.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[EntityType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityType)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EntityTypesClient entityTypesClient = await EntityTypesClient.CreateAsync();
    // Initialize request argument(s)
    AgentName parent = AgentName.FromProjectLocationAgent("[PROJECT]", "[LOCATION]", "[AGENT]");
    EntityType entityType = new EntityType();
    // Make the request
    EntityType response = await entityTypesClient.CreateEntityTypeAsync(parent, entityType);
    

### CreateEntityTypeAsync(CreateEntityTypeRequest, CallSettings)
    
    
    public virtual Task<EntityType> CreateEntityTypeAsync(CreateEntityTypeRequest request, CallSettings callSettings = null)

Creates an entity type in the specified agent.

Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateEntityTypeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.CreateEntityTypeRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[EntityType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityType)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EntityTypesClient entityTypesClient = await EntityTypesClient.CreateAsync();
    // Initialize request argument(s)
    CreateEntityTypeRequest request = new CreateEntityTypeRequest
    {
        ParentAsAgentName = AgentName.FromProjectLocationAgent("[PROJECT]", "[LOCATION]", "[AGENT]"),
        EntityType = new EntityType(),
        LanguageCode = "",
    };
    // Make the request
    EntityType response = await entityTypesClient.CreateEntityTypeAsync(request);
    

### CreateEntityTypeAsync(CreateEntityTypeRequest, CancellationToken)
    
    
    public virtual Task<EntityType> CreateEntityTypeAsync(CreateEntityTypeRequest request, CancellationToken cancellationToken)

Creates an entity type in the specified agent.

Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateEntityTypeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.CreateEntityTypeRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[EntityType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityType)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EntityTypesClient entityTypesClient = await EntityTypesClient.CreateAsync();
    // Initialize request argument(s)
    CreateEntityTypeRequest request = new CreateEntityTypeRequest
    {
        ParentAsAgentName = AgentName.FromProjectLocationAgent("[PROJECT]", "[LOCATION]", "[AGENT]"),
        EntityType = new EntityType(),
        LanguageCode = "",
    };
    // Make the request
    EntityType response = await entityTypesClient.CreateEntityTypeAsync(request);
    

### CreateEntityTypeAsync(string, EntityType, CallSettings)
    
    
    public virtual Task<EntityType> CreateEntityTypeAsync(string parent, EntityType entityType, CallSettings callSettings = null)

Creates an entity type in the specified agent.

Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The agent to create a entity type for. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
`entityType` | `[EntityType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityType)`  
Required. The entity type to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[EntityType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityType)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EntityTypesClient entityTypesClient = await EntityTypesClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/agents/[AGENT]";
    EntityType entityType = new EntityType();
    // Make the request
    EntityType response = await entityTypesClient.CreateEntityTypeAsync(parent, entityType);
    

### CreateEntityTypeAsync(string, EntityType, CancellationToken)
    
    
    public virtual Task<EntityType> CreateEntityTypeAsync(string parent, EntityType entityType, CancellationToken cancellationToken)

Creates an entity type in the specified agent.

Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The agent to create a entity type for. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
`entityType` | `[EntityType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityType)`  
Required. The entity type to create.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[EntityType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityType)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EntityTypesClient entityTypesClient = await EntityTypesClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/agents/[AGENT]";
    EntityType entityType = new EntityType();
    // Make the request
    EntityType response = await entityTypesClient.CreateEntityTypeAsync(parent, entityType);
    

### DeleteEntityType(DeleteEntityTypeRequest, CallSettings)
    
    
    public virtual void DeleteEntityType(DeleteEntityTypeRequest request, CallSettings callSettings = null)

Deletes the specified entity type.

Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteEntityTypeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DeleteEntityTypeRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    EntityTypesClient entityTypesClient = EntityTypesClient.Create();
    // Initialize request argument(s)
    DeleteEntityTypeRequest request = new DeleteEntityTypeRequest
    {
        EntityTypeName = EntityTypeName.FromProjectLocationAgentEntityType("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENTITY_TYPE]"),
        Force = false,
    };
    // Make the request
    entityTypesClient.DeleteEntityType(request);
    

### DeleteEntityType(EntityTypeName, CallSettings)
    
    
    public virtual void DeleteEntityType(EntityTypeName name, CallSettings callSettings = null)

Deletes the specified entity type.

Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

**Parameters**  
---  
**Name** | **Description**  
`name` | `[EntityTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityTypeName)`  
Required. The name of the entity type to delete. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/entityTypes/<EntityTypeID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    EntityTypesClient entityTypesClient = EntityTypesClient.Create();
    // Initialize request argument(s)
    EntityTypeName name = EntityTypeName.FromProjectLocationAgentEntityType("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENTITY_TYPE]");
    // Make the request
    entityTypesClient.DeleteEntityType(name);
    

### DeleteEntityType(string, CallSettings)
    
    
    public virtual void DeleteEntityType(string name, CallSettings callSettings = null)

Deletes the specified entity type.

Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the entity type to delete. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/entityTypes/<EntityTypeID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    EntityTypesClient entityTypesClient = EntityTypesClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/agents/[AGENT]/entityTypes/[ENTITY_TYPE]";
    // Make the request
    entityTypesClient.DeleteEntityType(name);
    

### DeleteEntityTypeAsync(DeleteEntityTypeRequest, CallSettings)
    
    
    public virtual Task DeleteEntityTypeAsync(DeleteEntityTypeRequest request, CallSettings callSettings = null)

Deletes the specified entity type.

Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteEntityTypeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DeleteEntityTypeRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EntityTypesClient entityTypesClient = await EntityTypesClient.CreateAsync();
    // Initialize request argument(s)
    DeleteEntityTypeRequest request = new DeleteEntityTypeRequest
    {
        EntityTypeName = EntityTypeName.FromProjectLocationAgentEntityType("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENTITY_TYPE]"),
        Force = false,
    };
    // Make the request
    await entityTypesClient.DeleteEntityTypeAsync(request);
    

### DeleteEntityTypeAsync(DeleteEntityTypeRequest, CancellationToken)
    
    
    public virtual Task DeleteEntityTypeAsync(DeleteEntityTypeRequest request, CancellationToken cancellationToken)

Deletes the specified entity type.

Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteEntityTypeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DeleteEntityTypeRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EntityTypesClient entityTypesClient = await EntityTypesClient.CreateAsync();
    // Initialize request argument(s)
    DeleteEntityTypeRequest request = new DeleteEntityTypeRequest
    {
        EntityTypeName = EntityTypeName.FromProjectLocationAgentEntityType("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENTITY_TYPE]"),
        Force = false,
    };
    // Make the request
    await entityTypesClient.DeleteEntityTypeAsync(request);
    

### DeleteEntityTypeAsync(EntityTypeName, CallSettings)
    
    
    public virtual Task DeleteEntityTypeAsync(EntityTypeName name, CallSettings callSettings = null)

Deletes the specified entity type.

Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

**Parameters**  
---  
**Name** | **Description**  
`name` | `[EntityTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityTypeName)`  
Required. The name of the entity type to delete. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/entityTypes/<EntityTypeID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EntityTypesClient entityTypesClient = await EntityTypesClient.CreateAsync();
    // Initialize request argument(s)
    EntityTypeName name = EntityTypeName.FromProjectLocationAgentEntityType("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENTITY_TYPE]");
    // Make the request
    await entityTypesClient.DeleteEntityTypeAsync(name);
    

### DeleteEntityTypeAsync(EntityTypeName, CancellationToken)
    
    
    public virtual Task DeleteEntityTypeAsync(EntityTypeName name, CancellationToken cancellationToken)

Deletes the specified entity type.

Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

**Parameters**  
---  
**Name** | **Description**  
`name` | `[EntityTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityTypeName)`  
Required. The name of the entity type to delete. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/entityTypes/<EntityTypeID>`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EntityTypesClient entityTypesClient = await EntityTypesClient.CreateAsync();
    // Initialize request argument(s)
    EntityTypeName name = EntityTypeName.FromProjectLocationAgentEntityType("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENTITY_TYPE]");
    // Make the request
    await entityTypesClient.DeleteEntityTypeAsync(name);
    

### DeleteEntityTypeAsync(string, CallSettings)
    
    
    public virtual Task DeleteEntityTypeAsync(string name, CallSettings callSettings = null)

Deletes the specified entity type.

Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the entity type to delete. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/entityTypes/<EntityTypeID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EntityTypesClient entityTypesClient = await EntityTypesClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/agents/[AGENT]/entityTypes/[ENTITY_TYPE]";
    // Make the request
    await entityTypesClient.DeleteEntityTypeAsync(name);
    

### DeleteEntityTypeAsync(string, CancellationToken)
    
    
    public virtual Task DeleteEntityTypeAsync(string name, CancellationToken cancellationToken)

Deletes the specified entity type.

Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the entity type to delete. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/entityTypes/<EntityTypeID>`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EntityTypesClient entityTypesClient = await EntityTypesClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/agents/[AGENT]/entityTypes/[ENTITY_TYPE]";
    // Make the request
    await entityTypesClient.DeleteEntityTypeAsync(name);
    

### ExportEntityTypes(ExportEntityTypesRequest, CallSettings)
    
    
    public virtual Operation<ExportEntityTypesResponse, ExportEntityTypesMetadata> ExportEntityTypes(ExportEntityTypesRequest request, CallSettings callSettings = null)

Exports the selected entity types.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportEntityTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportEntityTypesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportEntityTypesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportEntityTypesResponse)[ExportEntityTypesMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportEntityTypesMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    EntityTypesClient entityTypesClient = EntityTypesClient.Create();
    // Initialize request argument(s)
    ExportEntityTypesRequest request = new ExportEntityTypesRequest
    {
        ParentAsAgentName = AgentName.FromProjectLocationAgent("[PROJECT]", "[LOCATION]", "[AGENT]"),
        EntityTypes = { "", },
        EntityTypesUri = "",
        DataFormat = ExportEntityTypesRequest.Types.DataFormat.Unspecified,
        LanguageCode = "",
    };
    // Make the request
    Operation<ExportEntityTypesResponse, ExportEntityTypesMetadata> response = entityTypesClient.ExportEntityTypes(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ExportEntityTypesResponse, ExportEntityTypesMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    ExportEntityTypesResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ExportEntityTypesResponse, ExportEntityTypesMetadata> retrievedResponse = entityTypesClient.PollOnceExportEntityTypes(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ExportEntityTypesResponse retrievedResult = retrievedResponse.Result;
    }
    

### ExportEntityTypesAsync(ExportEntityTypesRequest, CallSettings)
    
    
    public virtual Task<Operation<ExportEntityTypesResponse, ExportEntityTypesMetadata>> ExportEntityTypesAsync(ExportEntityTypesRequest request, CallSettings callSettings = null)

Exports the selected entity types.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportEntityTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportEntityTypesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportEntityTypesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportEntityTypesResponse)[ExportEntityTypesMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportEntityTypesMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EntityTypesClient entityTypesClient = await EntityTypesClient.CreateAsync();
    // Initialize request argument(s)
    ExportEntityTypesRequest request = new ExportEntityTypesRequest
    {
        ParentAsAgentName = AgentName.FromProjectLocationAgent("[PROJECT]", "[LOCATION]", "[AGENT]"),
        EntityTypes = { "", },
        EntityTypesUri = "",
        DataFormat = ExportEntityTypesRequest.Types.DataFormat.Unspecified,
        LanguageCode = "",
    };
    // Make the request
    Operation<ExportEntityTypesResponse, ExportEntityTypesMetadata> response = await entityTypesClient.ExportEntityTypesAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ExportEntityTypesResponse, ExportEntityTypesMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ExportEntityTypesResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ExportEntityTypesResponse, ExportEntityTypesMetadata> retrievedResponse = await entityTypesClient.PollOnceExportEntityTypesAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ExportEntityTypesResponse retrievedResult = retrievedResponse.Result;
    }
    

### ExportEntityTypesAsync(ExportEntityTypesRequest, CancellationToken)
    
    
    public virtual Task<Operation<ExportEntityTypesResponse, ExportEntityTypesMetadata>> ExportEntityTypesAsync(ExportEntityTypesRequest request, CancellationToken cancellationToken)

Exports the selected entity types.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportEntityTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportEntityTypesRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportEntityTypesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportEntityTypesResponse)[ExportEntityTypesMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportEntityTypesMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EntityTypesClient entityTypesClient = await EntityTypesClient.CreateAsync();
    // Initialize request argument(s)
    ExportEntityTypesRequest request = new ExportEntityTypesRequest
    {
        ParentAsAgentName = AgentName.FromProjectLocationAgent("[PROJECT]", "[LOCATION]", "[AGENT]"),
        EntityTypes = { "", },
        EntityTypesUri = "",
        DataFormat = ExportEntityTypesRequest.Types.DataFormat.Unspecified,
        LanguageCode = "",
    };
    // Make the request
    Operation<ExportEntityTypesResponse, ExportEntityTypesMetadata> response = await entityTypesClient.ExportEntityTypesAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ExportEntityTypesResponse, ExportEntityTypesMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ExportEntityTypesResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ExportEntityTypesResponse, ExportEntityTypesMetadata> retrievedResponse = await entityTypesClient.PollOnceExportEntityTypesAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ExportEntityTypesResponse retrievedResult = retrievedResponse.Result;
    }
    

### GetEntityType(EntityTypeName, CallSettings)
    
    
    public virtual EntityType GetEntityType(EntityTypeName name, CallSettings callSettings = null)

Retrieves the specified entity type.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[EntityTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityTypeName)`  
Required. The name of the entity type. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/entityTypes/<EntityTypeID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[EntityType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityType)` | The RPC response.  
**Example**
    
    
    // Create client
    EntityTypesClient entityTypesClient = EntityTypesClient.Create();
    // Initialize request argument(s)
    EntityTypeName name = EntityTypeName.FromProjectLocationAgentEntityType("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENTITY_TYPE]");
    // Make the request
    EntityType response = entityTypesClient.GetEntityType(name);
    

### GetEntityType(GetEntityTypeRequest, CallSettings)
    
    
    public virtual EntityType GetEntityType(GetEntityTypeRequest request, CallSettings callSettings = null)

Retrieves the specified entity type.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetEntityTypeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GetEntityTypeRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[EntityType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityType)` | The RPC response.  
**Example**
    
    
    // Create client
    EntityTypesClient entityTypesClient = EntityTypesClient.Create();
    // Initialize request argument(s)
    GetEntityTypeRequest request = new GetEntityTypeRequest
    {
        EntityTypeName = EntityTypeName.FromProjectLocationAgentEntityType("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENTITY_TYPE]"),
        LanguageCode = "",
    };
    // Make the request
    EntityType response = entityTypesClient.GetEntityType(request);
    

### GetEntityType(string, CallSettings)
    
    
    public virtual EntityType GetEntityType(string name, CallSettings callSettings = null)

Retrieves the specified entity type.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the entity type. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/entityTypes/<EntityTypeID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[EntityType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityType)` | The RPC response.  
**Example**
    
    
    // Create client
    EntityTypesClient entityTypesClient = EntityTypesClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/agents/[AGENT]/entityTypes/[ENTITY_TYPE]";
    // Make the request
    EntityType response = entityTypesClient.GetEntityType(name);
    

### GetEntityTypeAsync(EntityTypeName, CallSettings)
    
    
    public virtual Task<EntityType> GetEntityTypeAsync(EntityTypeName name, CallSettings callSettings = null)

Retrieves the specified entity type.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[EntityTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityTypeName)`  
Required. The name of the entity type. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/entityTypes/<EntityTypeID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[EntityType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityType)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EntityTypesClient entityTypesClient = await EntityTypesClient.CreateAsync();
    // Initialize request argument(s)
    EntityTypeName name = EntityTypeName.FromProjectLocationAgentEntityType("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENTITY_TYPE]");
    // Make the request
    EntityType response = await entityTypesClient.GetEntityTypeAsync(name);
    

### GetEntityTypeAsync(EntityTypeName, CancellationToken)
    
    
    public virtual Task<EntityType> GetEntityTypeAsync(EntityTypeName name, CancellationToken cancellationToken)

Retrieves the specified entity type.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[EntityTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityTypeName)`  
Required. The name of the entity type. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/entityTypes/<EntityTypeID>`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[EntityType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityType)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EntityTypesClient entityTypesClient = await EntityTypesClient.CreateAsync();
    // Initialize request argument(s)
    EntityTypeName name = EntityTypeName.FromProjectLocationAgentEntityType("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENTITY_TYPE]");
    // Make the request
    EntityType response = await entityTypesClient.GetEntityTypeAsync(name);
    

### GetEntityTypeAsync(GetEntityTypeRequest, CallSettings)
    
    
    public virtual Task<EntityType> GetEntityTypeAsync(GetEntityTypeRequest request, CallSettings callSettings = null)

Retrieves the specified entity type.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetEntityTypeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GetEntityTypeRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[EntityType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityType)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EntityTypesClient entityTypesClient = await EntityTypesClient.CreateAsync();
    // Initialize request argument(s)
    GetEntityTypeRequest request = new GetEntityTypeRequest
    {
        EntityTypeName = EntityTypeName.FromProjectLocationAgentEntityType("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENTITY_TYPE]"),
        LanguageCode = "",
    };
    // Make the request
    EntityType response = await entityTypesClient.GetEntityTypeAsync(request);
    

### GetEntityTypeAsync(GetEntityTypeRequest, CancellationToken)
    
    
    public virtual Task<EntityType> GetEntityTypeAsync(GetEntityTypeRequest request, CancellationToken cancellationToken)

Retrieves the specified entity type.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetEntityTypeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GetEntityTypeRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[EntityType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityType)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EntityTypesClient entityTypesClient = await EntityTypesClient.CreateAsync();
    // Initialize request argument(s)
    GetEntityTypeRequest request = new GetEntityTypeRequest
    {
        EntityTypeName = EntityTypeName.FromProjectLocationAgentEntityType("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENTITY_TYPE]"),
        LanguageCode = "",
    };
    // Make the request
    EntityType response = await entityTypesClient.GetEntityTypeAsync(request);
    

### GetEntityTypeAsync(string, CallSettings)
    
    
    public virtual Task<EntityType> GetEntityTypeAsync(string name, CallSettings callSettings = null)

Retrieves the specified entity type.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the entity type. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/entityTypes/<EntityTypeID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[EntityType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityType)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EntityTypesClient entityTypesClient = await EntityTypesClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/agents/[AGENT]/entityTypes/[ENTITY_TYPE]";
    // Make the request
    EntityType response = await entityTypesClient.GetEntityTypeAsync(name);
    

### GetEntityTypeAsync(string, CancellationToken)
    
    
    public virtual Task<EntityType> GetEntityTypeAsync(string name, CancellationToken cancellationToken)

Retrieves the specified entity type.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the entity type. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/entityTypes/<EntityTypeID>`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[EntityType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityType)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EntityTypesClient entityTypesClient = await EntityTypesClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/agents/[AGENT]/entityTypes/[ENTITY_TYPE]";
    // Make the request
    EntityType response = await entityTypesClient.GetEntityTypeAsync(name);
    

### ImportEntityTypes(ImportEntityTypesRequest, CallSettings)
    
    
    public virtual Operation<ImportEntityTypesResponse, ImportEntityTypesMetadata> ImportEntityTypes(ImportEntityTypesRequest request, CallSettings callSettings = null)

Imports the specified entitytypes into the agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportEntityTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportEntityTypesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportEntityTypesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportEntityTypesResponse)[ImportEntityTypesMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportEntityTypesMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    EntityTypesClient entityTypesClient = EntityTypesClient.Create();
    // Initialize request argument(s)
    ImportEntityTypesRequest request = new ImportEntityTypesRequest
    {
        ParentAsAgentName = AgentName.FromProjectLocationAgent("[PROJECT]", "[LOCATION]", "[AGENT]"),
        EntityTypesUri = "",
        MergeOption = ImportEntityTypesRequest.Types.MergeOption.Unspecified,
        TargetEntityTypeAsEntityTypeName = EntityTypeName.FromProjectLocationAgentEntityType("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENTITY_TYPE]"),
    };
    // Make the request
    Operation<ImportEntityTypesResponse, ImportEntityTypesMetadata> response = entityTypesClient.ImportEntityTypes(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ImportEntityTypesResponse, ImportEntityTypesMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    ImportEntityTypesResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ImportEntityTypesResponse, ImportEntityTypesMetadata> retrievedResponse = entityTypesClient.PollOnceImportEntityTypes(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ImportEntityTypesResponse retrievedResult = retrievedResponse.Result;
    }
    

### ImportEntityTypesAsync(ImportEntityTypesRequest, CallSettings)
    
    
    public virtual Task<Operation<ImportEntityTypesResponse, ImportEntityTypesMetadata>> ImportEntityTypesAsync(ImportEntityTypesRequest request, CallSettings callSettings = null)

Imports the specified entitytypes into the agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportEntityTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportEntityTypesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportEntityTypesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportEntityTypesResponse)[ImportEntityTypesMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportEntityTypesMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EntityTypesClient entityTypesClient = await EntityTypesClient.CreateAsync();
    // Initialize request argument(s)
    ImportEntityTypesRequest request = new ImportEntityTypesRequest
    {
        ParentAsAgentName = AgentName.FromProjectLocationAgent("[PROJECT]", "[LOCATION]", "[AGENT]"),
        EntityTypesUri = "",
        MergeOption = ImportEntityTypesRequest.Types.MergeOption.Unspecified,
        TargetEntityTypeAsEntityTypeName = EntityTypeName.FromProjectLocationAgentEntityType("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENTITY_TYPE]"),
    };
    // Make the request
    Operation<ImportEntityTypesResponse, ImportEntityTypesMetadata> response = await entityTypesClient.ImportEntityTypesAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ImportEntityTypesResponse, ImportEntityTypesMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ImportEntityTypesResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ImportEntityTypesResponse, ImportEntityTypesMetadata> retrievedResponse = await entityTypesClient.PollOnceImportEntityTypesAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ImportEntityTypesResponse retrievedResult = retrievedResponse.Result;
    }
    

### ImportEntityTypesAsync(ImportEntityTypesRequest, CancellationToken)
    
    
    public virtual Task<Operation<ImportEntityTypesResponse, ImportEntityTypesMetadata>> ImportEntityTypesAsync(ImportEntityTypesRequest request, CancellationToken cancellationToken)

Imports the specified entitytypes into the agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportEntityTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportEntityTypesRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportEntityTypesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportEntityTypesResponse)[ImportEntityTypesMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportEntityTypesMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EntityTypesClient entityTypesClient = await EntityTypesClient.CreateAsync();
    // Initialize request argument(s)
    ImportEntityTypesRequest request = new ImportEntityTypesRequest
    {
        ParentAsAgentName = AgentName.FromProjectLocationAgent("[PROJECT]", "[LOCATION]", "[AGENT]"),
        EntityTypesUri = "",
        MergeOption = ImportEntityTypesRequest.Types.MergeOption.Unspecified,
        TargetEntityTypeAsEntityTypeName = EntityTypeName.FromProjectLocationAgentEntityType("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENTITY_TYPE]"),
    };
    // Make the request
    Operation<ImportEntityTypesResponse, ImportEntityTypesMetadata> response = await entityTypesClient.ImportEntityTypesAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ImportEntityTypesResponse, ImportEntityTypesMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ImportEntityTypesResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ImportEntityTypesResponse, ImportEntityTypesMetadata> retrievedResponse = await entityTypesClient.PollOnceImportEntityTypesAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ImportEntityTypesResponse retrievedResult = retrievedResponse.Result;
    }
    

### ListEntityTypes(AgentName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListEntityTypesResponse, EntityType> ListEntityTypes(AgentName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Returns the list of all entity types in the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AgentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentName)`  
Required. The agent to list all entity types for. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListEntityTypesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListEntityTypesResponse)[EntityType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityType)` | A pageable sequence of [EntityType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityType) resources.  
**Example**
    
    
    // Create client
    EntityTypesClient entityTypesClient = EntityTypesClient.Create();
    // Initialize request argument(s)
    AgentName parent = AgentName.FromProjectLocationAgent("[PROJECT]", "[LOCATION]", "[AGENT]");
    // Make the request
    PagedEnumerable<ListEntityTypesResponse, EntityType> response = entityTypesClient.ListEntityTypes(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (EntityType item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListEntityTypesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (EntityType item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<EntityType> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (EntityType item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListEntityTypes(ListEntityTypesRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListEntityTypesResponse, EntityType> ListEntityTypes(ListEntityTypesRequest request, CallSettings callSettings = null)

Returns the list of all entity types in the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListEntityTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListEntityTypesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListEntityTypesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListEntityTypesResponse)[EntityType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityType)` | A pageable sequence of [EntityType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityType) resources.  
**Example**
    
    
    // Create client
    EntityTypesClient entityTypesClient = EntityTypesClient.Create();
    // Initialize request argument(s)
    ListEntityTypesRequest request = new ListEntityTypesRequest
    {
        ParentAsAgentName = AgentName.FromProjectLocationAgent("[PROJECT]", "[LOCATION]", "[AGENT]"),
        LanguageCode = "",
    };
    // Make the request
    PagedEnumerable<ListEntityTypesResponse, EntityType> response = entityTypesClient.ListEntityTypes(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (EntityType item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListEntityTypesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (EntityType item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<EntityType> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (EntityType item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListEntityTypes(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListEntityTypesResponse, EntityType> ListEntityTypes(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Returns the list of all entity types in the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The agent to list all entity types for. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListEntityTypesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListEntityTypesResponse)[EntityType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityType)` | A pageable sequence of [EntityType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityType) resources.  
**Example**
    
    
    // Create client
    EntityTypesClient entityTypesClient = EntityTypesClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/agents/[AGENT]";
    // Make the request
    PagedEnumerable<ListEntityTypesResponse, EntityType> response = entityTypesClient.ListEntityTypes(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (EntityType item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListEntityTypesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (EntityType item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<EntityType> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (EntityType item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListEntityTypesAsync(AgentName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListEntityTypesResponse, EntityType> ListEntityTypesAsync(AgentName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Returns the list of all entity types in the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AgentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentName)`  
Required. The agent to list all entity types for. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListEntityTypesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListEntityTypesResponse)[EntityType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityType)` | A pageable asynchronous sequence of [EntityType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityType) resources.  
**Example**
    
    
    // Create client
    EntityTypesClient entityTypesClient = await EntityTypesClient.CreateAsync();
    // Initialize request argument(s)
    AgentName parent = AgentName.FromProjectLocationAgent("[PROJECT]", "[LOCATION]", "[AGENT]");
    // Make the request
    PagedAsyncEnumerable<ListEntityTypesResponse, EntityType> response = entityTypesClient.ListEntityTypesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (EntityType item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListEntityTypesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (EntityType item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<EntityType> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (EntityType item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListEntityTypesAsync(ListEntityTypesRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListEntityTypesResponse, EntityType> ListEntityTypesAsync(ListEntityTypesRequest request, CallSettings callSettings = null)

Returns the list of all entity types in the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListEntityTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListEntityTypesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListEntityTypesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListEntityTypesResponse)[EntityType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityType)` | A pageable asynchronous sequence of [EntityType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityType) resources.  
**Example**
    
    
    // Create client
    EntityTypesClient entityTypesClient = await EntityTypesClient.CreateAsync();
    // Initialize request argument(s)
    ListEntityTypesRequest request = new ListEntityTypesRequest
    {
        ParentAsAgentName = AgentName.FromProjectLocationAgent("[PROJECT]", "[LOCATION]", "[AGENT]"),
        LanguageCode = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListEntityTypesResponse, EntityType> response = entityTypesClient.ListEntityTypesAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (EntityType item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListEntityTypesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (EntityType item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<EntityType> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (EntityType item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListEntityTypesAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListEntityTypesResponse, EntityType> ListEntityTypesAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Returns the list of all entity types in the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The agent to list all entity types for. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListEntityTypesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListEntityTypesResponse)[EntityType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityType)` | A pageable asynchronous sequence of [EntityType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityType) resources.  
**Example**
    
    
    // Create client
    EntityTypesClient entityTypesClient = await EntityTypesClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/agents/[AGENT]";
    // Make the request
    PagedAsyncEnumerable<ListEntityTypesResponse, EntityType> response = entityTypesClient.ListEntityTypesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (EntityType item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListEntityTypesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (EntityType item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<EntityType> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (EntityType item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### PollOnceExportEntityTypes(string, CallSettings)
    
    
    public virtual Operation<ExportEntityTypesResponse, ExportEntityTypesMetadata> PollOnceExportEntityTypes(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `ExportEntityTypes` .

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportEntityTypesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportEntityTypesResponse)[ExportEntityTypesMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportEntityTypesMetadata)` | The result of polling the operation.  
  
### PollOnceExportEntityTypesAsync(string, CallSettings)
    
    
    public virtual Task<Operation<ExportEntityTypesResponse, ExportEntityTypesMetadata>> PollOnceExportEntityTypesAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `ExportEntityTypes`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ExportEntityTypesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportEntityTypesResponse)[ExportEntityTypesMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportEntityTypesMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceImportEntityTypes(string, CallSettings)
    
    
    public virtual Operation<ImportEntityTypesResponse, ImportEntityTypesMetadata> PollOnceImportEntityTypes(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `ImportEntityTypes` .

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportEntityTypesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportEntityTypesResponse)[ImportEntityTypesMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportEntityTypesMetadata)` | The result of polling the operation.  
  
### PollOnceImportEntityTypesAsync(string, CallSettings)
    
    
    public virtual Task<Operation<ImportEntityTypesResponse, ImportEntityTypesMetadata>> PollOnceImportEntityTypesAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `ImportEntityTypes`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportEntityTypesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportEntityTypesResponse)[ImportEntityTypesMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportEntityTypesMetadata)` | A task representing the result of polling the operation.  
  
### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityTypesClient#Google_Cloud_Dialogflow_Cx_V3_EntityTypesClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityTypesClient#Google_Cloud_Dialogflow_Cx_V3_EntityTypesClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityTypesClient#Google_Cloud_Dialogflow_Cx_V3_EntityTypesClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityTypesClient#Google_Cloud_Dialogflow_Cx_V3_EntityTypesClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### UpdateEntityType(EntityType, FieldMask, CallSettings)
    
    
    public virtual EntityType UpdateEntityType(EntityType entityType, FieldMask updateMask, CallSettings callSettings = null)

Updates the specified entity type.

Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

**Parameters**  
---  
**Name** | **Description**  
`entityType` | `[EntityType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityType)`  
Required. The entity type to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
The mask to control which fields get updated.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[EntityType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityType)` | The RPC response.  
**Example**
    
    
    // Create client
    EntityTypesClient entityTypesClient = EntityTypesClient.Create();
    // Initialize request argument(s)
    EntityType entityType = new EntityType();
    FieldMask updateMask = new FieldMask();
    // Make the request
    EntityType response = entityTypesClient.UpdateEntityType(entityType, updateMask);
    

### UpdateEntityType(UpdateEntityTypeRequest, CallSettings)
    
    
    public virtual EntityType UpdateEntityType(UpdateEntityTypeRequest request, CallSettings callSettings = null)

Updates the specified entity type.

Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateEntityTypeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.UpdateEntityTypeRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[EntityType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityType)` | The RPC response.  
**Example**
    
    
    // Create client
    EntityTypesClient entityTypesClient = EntityTypesClient.Create();
    // Initialize request argument(s)
    UpdateEntityTypeRequest request = new UpdateEntityTypeRequest
    {
        EntityType = new EntityType(),
        LanguageCode = "",
        UpdateMask = new FieldMask(),
    };
    // Make the request
    EntityType response = entityTypesClient.UpdateEntityType(request);
    

### UpdateEntityTypeAsync(EntityType, FieldMask, CallSettings)
    
    
    public virtual Task<EntityType> UpdateEntityTypeAsync(EntityType entityType, FieldMask updateMask, CallSettings callSettings = null)

Updates the specified entity type.

Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

**Parameters**  
---  
**Name** | **Description**  
`entityType` | `[EntityType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityType)`  
Required. The entity type to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
The mask to control which fields get updated.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[EntityType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityType)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EntityTypesClient entityTypesClient = await EntityTypesClient.CreateAsync();
    // Initialize request argument(s)
    EntityType entityType = new EntityType();
    FieldMask updateMask = new FieldMask();
    // Make the request
    EntityType response = await entityTypesClient.UpdateEntityTypeAsync(entityType, updateMask);
    

### UpdateEntityTypeAsync(EntityType, FieldMask, CancellationToken)
    
    
    public virtual Task<EntityType> UpdateEntityTypeAsync(EntityType entityType, FieldMask updateMask, CancellationToken cancellationToken)

Updates the specified entity type.

Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

**Parameters**  
---  
**Name** | **Description**  
`entityType` | `[EntityType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityType)`  
Required. The entity type to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
The mask to control which fields get updated.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[EntityType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityType)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EntityTypesClient entityTypesClient = await EntityTypesClient.CreateAsync();
    // Initialize request argument(s)
    EntityType entityType = new EntityType();
    FieldMask updateMask = new FieldMask();
    // Make the request
    EntityType response = await entityTypesClient.UpdateEntityTypeAsync(entityType, updateMask);
    

### UpdateEntityTypeAsync(UpdateEntityTypeRequest, CallSettings)
    
    
    public virtual Task<EntityType> UpdateEntityTypeAsync(UpdateEntityTypeRequest request, CallSettings callSettings = null)

Updates the specified entity type.

Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateEntityTypeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.UpdateEntityTypeRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[EntityType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityType)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EntityTypesClient entityTypesClient = await EntityTypesClient.CreateAsync();
    // Initialize request argument(s)
    UpdateEntityTypeRequest request = new UpdateEntityTypeRequest
    {
        EntityType = new EntityType(),
        LanguageCode = "",
        UpdateMask = new FieldMask(),
    };
    // Make the request
    EntityType response = await entityTypesClient.UpdateEntityTypeAsync(request);
    

### UpdateEntityTypeAsync(UpdateEntityTypeRequest, CancellationToken)
    
    
    public virtual Task<EntityType> UpdateEntityTypeAsync(UpdateEntityTypeRequest request, CancellationToken cancellationToken)

Updates the specified entity type.

Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateEntityTypeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.UpdateEntityTypeRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[EntityType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityType)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EntityTypesClient entityTypesClient = await EntityTypesClient.CreateAsync();
    // Initialize request argument(s)
    UpdateEntityTypeRequest request = new UpdateEntityTypeRequest
    {
        EntityType = new EntityType(),
        LanguageCode = "",
        UpdateMask = new FieldMask(),
    };
    // Make the request
    EntityType response = await entityTypesClient.UpdateEntityTypeAsync(request);
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
