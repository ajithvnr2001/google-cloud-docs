---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.EntityServiceClient
title: Chronicle v1 API - Class EntityServiceClient (1.1.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:57:30.275367+00:00
---

# Chronicle v1 API - Class EntityServiceClient (1.1.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.EntityServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Chronicle v1 API - Class EntityServiceClient (1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0 
    
    
    public abstract class EntityServiceClient

Reference documentation and code samples for the Chronicle v1 API class EntityServiceClient.

EntityService client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > EntityServiceClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[EntityServiceClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.EntityServiceClientImpl)

## Namespace

[Google.Cloud.Chronicle.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1)

## Assembly

Google.Cloud.Chronicle.V1.dll

## Remarks

EntityService contains apis for finding entities.

## Properties 

### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the EntityService service, which is a host of "chronicle.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default EntityService scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default EntityService scopes are:

  * <https://www.googleapis.com/auth/cloud-platform>



### GrpcClient
    
    
    public virtual EntityService.EntityServiceClient GrpcClient { get; }

The underlying gRPC EntityService client

**Property Value**  
---  
**Type** | **Description**  
`[EntityService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.EntityService)[EntityServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.EntityService.EntityServiceClient)` |   
  
### ServiceMetadata
    
    
    public static ServiceMetadata ServiceMetadata { get; }

The service metadata associated with this client type.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceMetadata](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceMetadata.html)` |   
  
## Methods 

### Create()
    
    
    public static EntityServiceClient Create()

Synchronously creates a [EntityServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.EntityServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [EntityServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.EntityServiceClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[EntityServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.EntityServiceClient)` | The created [EntityServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.EntityServiceClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<EntityServiceClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [EntityServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.EntityServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [EntityServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.EntityServiceClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[EntityServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.EntityServiceClient)` | The task representing the created [EntityServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.EntityServiceClient).  
  
### CreateWatchlist(CreateWatchlistRequest, CallSettings)
    
    
    public virtual Watchlist CreateWatchlist(CreateWatchlistRequest request, CallSettings callSettings = null)

Creates a watchlist for the given instance. Note that there can be at most 200 watchlists per instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateWatchlistRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CreateWatchlistRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Watchlist](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.Watchlist)` | The RPC response.  
**Example**
    
    
    // Create client
    EntityServiceClient entityServiceClient = EntityServiceClient.Create();
    // Initialize request argument(s)
    CreateWatchlistRequest request = new CreateWatchlistRequest
    {
        ParentAsInstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
        WatchlistId = "",
        Watchlist = new Watchlist(),
    };
    // Make the request
    Watchlist response = entityServiceClient.CreateWatchlist(request);
    

### CreateWatchlist(InstanceName, Watchlist, string, CallSettings)
    
    
    public virtual Watchlist CreateWatchlist(InstanceName parent, Watchlist watchlist, string watchlistId, CallSettings callSettings = null)

Creates a watchlist for the given instance. Note that there can be at most 200 watchlists per instance.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.InstanceName)`  
Required. The parent resource where this watchlist will be created. Format: `projects/{project}/locations/{location}/instances/{instance}`  
`watchlist` | `[Watchlist](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.Watchlist)`  
Required. The watchlist to create.  
`watchlistId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the watchlist, which will become the final component of the watchlist's resource name. This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Watchlist](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.Watchlist)` | The RPC response.  
**Example**
    
    
    // Create client
    EntityServiceClient entityServiceClient = EntityServiceClient.Create();
    // Initialize request argument(s)
    InstanceName parent = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    Watchlist watchlist = new Watchlist();
    string watchlistId = "";
    // Make the request
    Watchlist response = entityServiceClient.CreateWatchlist(parent, watchlist, watchlistId);
    

### CreateWatchlist(string, Watchlist, string, CallSettings)
    
    
    public virtual Watchlist CreateWatchlist(string parent, Watchlist watchlist, string watchlistId, CallSettings callSettings = null)

Creates a watchlist for the given instance. Note that there can be at most 200 watchlists per instance.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource where this watchlist will be created. Format: `projects/{project}/locations/{location}/instances/{instance}`  
`watchlist` | `[Watchlist](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.Watchlist)`  
Required. The watchlist to create.  
`watchlistId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the watchlist, which will become the final component of the watchlist's resource name. This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Watchlist](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.Watchlist)` | The RPC response.  
**Example**
    
    
    // Create client
    EntityServiceClient entityServiceClient = EntityServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]";
    Watchlist watchlist = new Watchlist();
    string watchlistId = "";
    // Make the request
    Watchlist response = entityServiceClient.CreateWatchlist(parent, watchlist, watchlistId);
    

### CreateWatchlistAsync(CreateWatchlistRequest, CallSettings)
    
    
    public virtual Task<Watchlist> CreateWatchlistAsync(CreateWatchlistRequest request, CallSettings callSettings = null)

Creates a watchlist for the given instance. Note that there can be at most 200 watchlists per instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateWatchlistRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CreateWatchlistRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Watchlist](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.Watchlist)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EntityServiceClient entityServiceClient = await EntityServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateWatchlistRequest request = new CreateWatchlistRequest
    {
        ParentAsInstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
        WatchlistId = "",
        Watchlist = new Watchlist(),
    };
    // Make the request
    Watchlist response = await entityServiceClient.CreateWatchlistAsync(request);
    

### CreateWatchlistAsync(CreateWatchlistRequest, CancellationToken)
    
    
    public virtual Task<Watchlist> CreateWatchlistAsync(CreateWatchlistRequest request, CancellationToken cancellationToken)

Creates a watchlist for the given instance. Note that there can be at most 200 watchlists per instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateWatchlistRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CreateWatchlistRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Watchlist](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.Watchlist)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EntityServiceClient entityServiceClient = await EntityServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateWatchlistRequest request = new CreateWatchlistRequest
    {
        ParentAsInstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
        WatchlistId = "",
        Watchlist = new Watchlist(),
    };
    // Make the request
    Watchlist response = await entityServiceClient.CreateWatchlistAsync(request);
    

### CreateWatchlistAsync(InstanceName, Watchlist, string, CallSettings)
    
    
    public virtual Task<Watchlist> CreateWatchlistAsync(InstanceName parent, Watchlist watchlist, string watchlistId, CallSettings callSettings = null)

Creates a watchlist for the given instance. Note that there can be at most 200 watchlists per instance.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.InstanceName)`  
Required. The parent resource where this watchlist will be created. Format: `projects/{project}/locations/{location}/instances/{instance}`  
`watchlist` | `[Watchlist](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.Watchlist)`  
Required. The watchlist to create.  
`watchlistId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the watchlist, which will become the final component of the watchlist's resource name. This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Watchlist](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.Watchlist)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EntityServiceClient entityServiceClient = await EntityServiceClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName parent = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    Watchlist watchlist = new Watchlist();
    string watchlistId = "";
    // Make the request
    Watchlist response = await entityServiceClient.CreateWatchlistAsync(parent, watchlist, watchlistId);
    

### CreateWatchlistAsync(InstanceName, Watchlist, string, CancellationToken)
    
    
    public virtual Task<Watchlist> CreateWatchlistAsync(InstanceName parent, Watchlist watchlist, string watchlistId, CancellationToken cancellationToken)

Creates a watchlist for the given instance. Note that there can be at most 200 watchlists per instance.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.InstanceName)`  
Required. The parent resource where this watchlist will be created. Format: `projects/{project}/locations/{location}/instances/{instance}`  
`watchlist` | `[Watchlist](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.Watchlist)`  
Required. The watchlist to create.  
`watchlistId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the watchlist, which will become the final component of the watchlist's resource name. This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Watchlist](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.Watchlist)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EntityServiceClient entityServiceClient = await EntityServiceClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName parent = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    Watchlist watchlist = new Watchlist();
    string watchlistId = "";
    // Make the request
    Watchlist response = await entityServiceClient.CreateWatchlistAsync(parent, watchlist, watchlistId);
    

### CreateWatchlistAsync(string, Watchlist, string, CallSettings)
    
    
    public virtual Task<Watchlist> CreateWatchlistAsync(string parent, Watchlist watchlist, string watchlistId, CallSettings callSettings = null)

Creates a watchlist for the given instance. Note that there can be at most 200 watchlists per instance.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource where this watchlist will be created. Format: `projects/{project}/locations/{location}/instances/{instance}`  
`watchlist` | `[Watchlist](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.Watchlist)`  
Required. The watchlist to create.  
`watchlistId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the watchlist, which will become the final component of the watchlist's resource name. This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Watchlist](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.Watchlist)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EntityServiceClient entityServiceClient = await EntityServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]";
    Watchlist watchlist = new Watchlist();
    string watchlistId = "";
    // Make the request
    Watchlist response = await entityServiceClient.CreateWatchlistAsync(parent, watchlist, watchlistId);
    

### CreateWatchlistAsync(string, Watchlist, string, CancellationToken)
    
    
    public virtual Task<Watchlist> CreateWatchlistAsync(string parent, Watchlist watchlist, string watchlistId, CancellationToken cancellationToken)

Creates a watchlist for the given instance. Note that there can be at most 200 watchlists per instance.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource where this watchlist will be created. Format: `projects/{project}/locations/{location}/instances/{instance}`  
`watchlist` | `[Watchlist](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.Watchlist)`  
Required. The watchlist to create.  
`watchlistId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the watchlist, which will become the final component of the watchlist's resource name. This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Watchlist](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.Watchlist)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EntityServiceClient entityServiceClient = await EntityServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]";
    Watchlist watchlist = new Watchlist();
    string watchlistId = "";
    // Make the request
    Watchlist response = await entityServiceClient.CreateWatchlistAsync(parent, watchlist, watchlistId);
    

### DeleteWatchlist(DeleteWatchlistRequest, CallSettings)
    
    
    public virtual void DeleteWatchlist(DeleteWatchlistRequest request, CallSettings callSettings = null)

Deletes the watchlist for the given instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteWatchlistRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DeleteWatchlistRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    EntityServiceClient entityServiceClient = EntityServiceClient.Create();
    // Initialize request argument(s)
    DeleteWatchlistRequest request = new DeleteWatchlistRequest
    {
        WatchlistName = WatchlistName.FromProjectLocationInstanceWatchlist("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[WATCHLIST]"),
        Force = false,
    };
    // Make the request
    entityServiceClient.DeleteWatchlist(request);
    

### DeleteWatchlist(WatchlistName, bool, CallSettings)
    
    
    public virtual void DeleteWatchlist(WatchlistName name, bool force, CallSettings callSettings = null)

Deletes the watchlist for the given instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[WatchlistName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.WatchlistName)`  
Required. The name of the watchlist to delete. Format: `projects/{project}/locations/{location}/instances/{instance}/watchlists/{watchlist}`  
`force` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
Optional. If set to true, any entities under this watchlist will also be deleted. (Otherwise, the request will only work if the watchlist has no entities.)  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    EntityServiceClient entityServiceClient = EntityServiceClient.Create();
    // Initialize request argument(s)
    WatchlistName name = WatchlistName.FromProjectLocationInstanceWatchlist("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[WATCHLIST]");
    bool force = false;
    // Make the request
    entityServiceClient.DeleteWatchlist(name, force);
    

### DeleteWatchlist(string, bool, CallSettings)
    
    
    public virtual void DeleteWatchlist(string name, bool force, CallSettings callSettings = null)

Deletes the watchlist for the given instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the watchlist to delete. Format: `projects/{project}/locations/{location}/instances/{instance}/watchlists/{watchlist}`  
`force` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
Optional. If set to true, any entities under this watchlist will also be deleted. (Otherwise, the request will only work if the watchlist has no entities.)  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    EntityServiceClient entityServiceClient = EntityServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]/watchlists/[WATCHLIST]";
    bool force = false;
    // Make the request
    entityServiceClient.DeleteWatchlist(name, force);
    

### DeleteWatchlistAsync(DeleteWatchlistRequest, CallSettings)
    
    
    public virtual Task DeleteWatchlistAsync(DeleteWatchlistRequest request, CallSettings callSettings = null)

Deletes the watchlist for the given instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteWatchlistRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DeleteWatchlistRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EntityServiceClient entityServiceClient = await EntityServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteWatchlistRequest request = new DeleteWatchlistRequest
    {
        WatchlistName = WatchlistName.FromProjectLocationInstanceWatchlist("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[WATCHLIST]"),
        Force = false,
    };
    // Make the request
    await entityServiceClient.DeleteWatchlistAsync(request);
    

### DeleteWatchlistAsync(DeleteWatchlistRequest, CancellationToken)
    
    
    public virtual Task DeleteWatchlistAsync(DeleteWatchlistRequest request, CancellationToken cancellationToken)

Deletes the watchlist for the given instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteWatchlistRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DeleteWatchlistRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EntityServiceClient entityServiceClient = await EntityServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteWatchlistRequest request = new DeleteWatchlistRequest
    {
        WatchlistName = WatchlistName.FromProjectLocationInstanceWatchlist("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[WATCHLIST]"),
        Force = false,
    };
    // Make the request
    await entityServiceClient.DeleteWatchlistAsync(request);
    

### DeleteWatchlistAsync(WatchlistName, bool, CallSettings)
    
    
    public virtual Task DeleteWatchlistAsync(WatchlistName name, bool force, CallSettings callSettings = null)

Deletes the watchlist for the given instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[WatchlistName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.WatchlistName)`  
Required. The name of the watchlist to delete. Format: `projects/{project}/locations/{location}/instances/{instance}/watchlists/{watchlist}`  
`force` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
Optional. If set to true, any entities under this watchlist will also be deleted. (Otherwise, the request will only work if the watchlist has no entities.)  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EntityServiceClient entityServiceClient = await EntityServiceClient.CreateAsync();
    // Initialize request argument(s)
    WatchlistName name = WatchlistName.FromProjectLocationInstanceWatchlist("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[WATCHLIST]");
    bool force = false;
    // Make the request
    await entityServiceClient.DeleteWatchlistAsync(name, force);
    

### DeleteWatchlistAsync(WatchlistName, bool, CancellationToken)
    
    
    public virtual Task DeleteWatchlistAsync(WatchlistName name, bool force, CancellationToken cancellationToken)

Deletes the watchlist for the given instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[WatchlistName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.WatchlistName)`  
Required. The name of the watchlist to delete. Format: `projects/{project}/locations/{location}/instances/{instance}/watchlists/{watchlist}`  
`force` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
Optional. If set to true, any entities under this watchlist will also be deleted. (Otherwise, the request will only work if the watchlist has no entities.)  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EntityServiceClient entityServiceClient = await EntityServiceClient.CreateAsync();
    // Initialize request argument(s)
    WatchlistName name = WatchlistName.FromProjectLocationInstanceWatchlist("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[WATCHLIST]");
    bool force = false;
    // Make the request
    await entityServiceClient.DeleteWatchlistAsync(name, force);
    

### DeleteWatchlistAsync(string, bool, CallSettings)
    
    
    public virtual Task DeleteWatchlistAsync(string name, bool force, CallSettings callSettings = null)

Deletes the watchlist for the given instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the watchlist to delete. Format: `projects/{project}/locations/{location}/instances/{instance}/watchlists/{watchlist}`  
`force` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
Optional. If set to true, any entities under this watchlist will also be deleted. (Otherwise, the request will only work if the watchlist has no entities.)  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EntityServiceClient entityServiceClient = await EntityServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]/watchlists/[WATCHLIST]";
    bool force = false;
    // Make the request
    await entityServiceClient.DeleteWatchlistAsync(name, force);
    

### DeleteWatchlistAsync(string, bool, CancellationToken)
    
    
    public virtual Task DeleteWatchlistAsync(string name, bool force, CancellationToken cancellationToken)

Deletes the watchlist for the given instance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the watchlist to delete. Format: `projects/{project}/locations/{location}/instances/{instance}/watchlists/{watchlist}`  
`force` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
Optional. If set to true, any entities under this watchlist will also be deleted. (Otherwise, the request will only work if the watchlist has no entities.)  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EntityServiceClient entityServiceClient = await EntityServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]/watchlists/[WATCHLIST]";
    bool force = false;
    // Make the request
    await entityServiceClient.DeleteWatchlistAsync(name, force);
    

### GetWatchlist(GetWatchlistRequest, CallSettings)
    
    
    public virtual Watchlist GetWatchlist(GetWatchlistRequest request, CallSettings callSettings = null)

Gets watchlist details for the given watchlist ID.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetWatchlistRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.GetWatchlistRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Watchlist](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.Watchlist)` | The RPC response.  
**Example**
    
    
    // Create client
    EntityServiceClient entityServiceClient = EntityServiceClient.Create();
    // Initialize request argument(s)
    GetWatchlistRequest request = new GetWatchlistRequest
    {
        WatchlistName = WatchlistName.FromProjectLocationInstanceWatchlist("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[WATCHLIST]"),
    };
    // Make the request
    Watchlist response = entityServiceClient.GetWatchlist(request);
    

### GetWatchlist(WatchlistName, CallSettings)
    
    
    public virtual Watchlist GetWatchlist(WatchlistName name, CallSettings callSettings = null)

Gets watchlist details for the given watchlist ID.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[WatchlistName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.WatchlistName)`  
Required. The parent, which owns this collection of watchlists. The name of the watchlist to retrieve. Format: `projects/{project}/locations/{location}/instances/{instance}/watchlists/{watchlist}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Watchlist](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.Watchlist)` | The RPC response.  
**Example**
    
    
    // Create client
    EntityServiceClient entityServiceClient = EntityServiceClient.Create();
    // Initialize request argument(s)
    WatchlistName name = WatchlistName.FromProjectLocationInstanceWatchlist("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[WATCHLIST]");
    // Make the request
    Watchlist response = entityServiceClient.GetWatchlist(name);
    

### GetWatchlist(string, CallSettings)
    
    
    public virtual Watchlist GetWatchlist(string name, CallSettings callSettings = null)

Gets watchlist details for the given watchlist ID.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent, which owns this collection of watchlists. The name of the watchlist to retrieve. Format: `projects/{project}/locations/{location}/instances/{instance}/watchlists/{watchlist}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Watchlist](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.Watchlist)` | The RPC response.  
**Example**
    
    
    // Create client
    EntityServiceClient entityServiceClient = EntityServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]/watchlists/[WATCHLIST]";
    // Make the request
    Watchlist response = entityServiceClient.GetWatchlist(name);
    

### GetWatchlistAsync(GetWatchlistRequest, CallSettings)
    
    
    public virtual Task<Watchlist> GetWatchlistAsync(GetWatchlistRequest request, CallSettings callSettings = null)

Gets watchlist details for the given watchlist ID.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetWatchlistRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.GetWatchlistRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Watchlist](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.Watchlist)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EntityServiceClient entityServiceClient = await EntityServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetWatchlistRequest request = new GetWatchlistRequest
    {
        WatchlistName = WatchlistName.FromProjectLocationInstanceWatchlist("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[WATCHLIST]"),
    };
    // Make the request
    Watchlist response = await entityServiceClient.GetWatchlistAsync(request);
    

### GetWatchlistAsync(GetWatchlistRequest, CancellationToken)
    
    
    public virtual Task<Watchlist> GetWatchlistAsync(GetWatchlistRequest request, CancellationToken cancellationToken)

Gets watchlist details for the given watchlist ID.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetWatchlistRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.GetWatchlistRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Watchlist](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.Watchlist)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EntityServiceClient entityServiceClient = await EntityServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetWatchlistRequest request = new GetWatchlistRequest
    {
        WatchlistName = WatchlistName.FromProjectLocationInstanceWatchlist("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[WATCHLIST]"),
    };
    // Make the request
    Watchlist response = await entityServiceClient.GetWatchlistAsync(request);
    

### GetWatchlistAsync(WatchlistName, CallSettings)
    
    
    public virtual Task<Watchlist> GetWatchlistAsync(WatchlistName name, CallSettings callSettings = null)

Gets watchlist details for the given watchlist ID.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[WatchlistName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.WatchlistName)`  
Required. The parent, which owns this collection of watchlists. The name of the watchlist to retrieve. Format: `projects/{project}/locations/{location}/instances/{instance}/watchlists/{watchlist}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Watchlist](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.Watchlist)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EntityServiceClient entityServiceClient = await EntityServiceClient.CreateAsync();
    // Initialize request argument(s)
    WatchlistName name = WatchlistName.FromProjectLocationInstanceWatchlist("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[WATCHLIST]");
    // Make the request
    Watchlist response = await entityServiceClient.GetWatchlistAsync(name);
    

### GetWatchlistAsync(WatchlistName, CancellationToken)
    
    
    public virtual Task<Watchlist> GetWatchlistAsync(WatchlistName name, CancellationToken cancellationToken)

Gets watchlist details for the given watchlist ID.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[WatchlistName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.WatchlistName)`  
Required. The parent, which owns this collection of watchlists. The name of the watchlist to retrieve. Format: `projects/{project}/locations/{location}/instances/{instance}/watchlists/{watchlist}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Watchlist](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.Watchlist)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EntityServiceClient entityServiceClient = await EntityServiceClient.CreateAsync();
    // Initialize request argument(s)
    WatchlistName name = WatchlistName.FromProjectLocationInstanceWatchlist("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[WATCHLIST]");
    // Make the request
    Watchlist response = await entityServiceClient.GetWatchlistAsync(name);
    

### GetWatchlistAsync(string, CallSettings)
    
    
    public virtual Task<Watchlist> GetWatchlistAsync(string name, CallSettings callSettings = null)

Gets watchlist details for the given watchlist ID.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent, which owns this collection of watchlists. The name of the watchlist to retrieve. Format: `projects/{project}/locations/{location}/instances/{instance}/watchlists/{watchlist}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Watchlist](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.Watchlist)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EntityServiceClient entityServiceClient = await EntityServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]/watchlists/[WATCHLIST]";
    // Make the request
    Watchlist response = await entityServiceClient.GetWatchlistAsync(name);
    

### GetWatchlistAsync(string, CancellationToken)
    
    
    public virtual Task<Watchlist> GetWatchlistAsync(string name, CancellationToken cancellationToken)

Gets watchlist details for the given watchlist ID.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent, which owns this collection of watchlists. The name of the watchlist to retrieve. Format: `projects/{project}/locations/{location}/instances/{instance}/watchlists/{watchlist}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Watchlist](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.Watchlist)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EntityServiceClient entityServiceClient = await EntityServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]/watchlists/[WATCHLIST]";
    // Make the request
    Watchlist response = await entityServiceClient.GetWatchlistAsync(name);
    

### ListWatchlists(InstanceName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListWatchlistsResponse, Watchlist> ListWatchlists(InstanceName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists all watchlists for the given instance.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.InstanceName)`  
Required. The parent, which owns this collection of watchlists. Format: `projects/{project}/locations/{location}/instances/{instance}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListWatchlistsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.ListWatchlistsResponse)[Watchlist](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.Watchlist)` | A pageable sequence of [Watchlist](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.Watchlist) resources.  
**Example**
    
    
    // Create client
    EntityServiceClient entityServiceClient = EntityServiceClient.Create();
    // Initialize request argument(s)
    InstanceName parent = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    // Make the request
    PagedEnumerable<ListWatchlistsResponse, Watchlist> response = entityServiceClient.ListWatchlists(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Watchlist item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListWatchlistsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Watchlist item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Watchlist> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Watchlist item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListWatchlists(ListWatchlistsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListWatchlistsResponse, Watchlist> ListWatchlists(ListWatchlistsRequest request, CallSettings callSettings = null)

Lists all watchlists for the given instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListWatchlistsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.ListWatchlistsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListWatchlistsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.ListWatchlistsResponse)[Watchlist](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.Watchlist)` | A pageable sequence of [Watchlist](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.Watchlist) resources.  
**Example**
    
    
    // Create client
    EntityServiceClient entityServiceClient = EntityServiceClient.Create();
    // Initialize request argument(s)
    ListWatchlistsRequest request = new ListWatchlistsRequest
    {
        ParentAsInstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
        Filter = "",
    };
    // Make the request
    PagedEnumerable<ListWatchlistsResponse, Watchlist> response = entityServiceClient.ListWatchlists(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Watchlist item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListWatchlistsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Watchlist item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Watchlist> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Watchlist item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListWatchlists(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListWatchlistsResponse, Watchlist> ListWatchlists(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists all watchlists for the given instance.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent, which owns this collection of watchlists. Format: `projects/{project}/locations/{location}/instances/{instance}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListWatchlistsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.ListWatchlistsResponse)[Watchlist](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.Watchlist)` | A pageable sequence of [Watchlist](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.Watchlist) resources.  
**Example**
    
    
    // Create client
    EntityServiceClient entityServiceClient = EntityServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]";
    // Make the request
    PagedEnumerable<ListWatchlistsResponse, Watchlist> response = entityServiceClient.ListWatchlists(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Watchlist item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListWatchlistsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Watchlist item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Watchlist> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Watchlist item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListWatchlistsAsync(InstanceName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListWatchlistsResponse, Watchlist> ListWatchlistsAsync(InstanceName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists all watchlists for the given instance.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.InstanceName)`  
Required. The parent, which owns this collection of watchlists. Format: `projects/{project}/locations/{location}/instances/{instance}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListWatchlistsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.ListWatchlistsResponse)[Watchlist](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.Watchlist)` | A pageable asynchronous sequence of [Watchlist](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.Watchlist) resources.  
**Example**
    
    
    // Create client
    EntityServiceClient entityServiceClient = await EntityServiceClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName parent = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]");
    // Make the request
    PagedAsyncEnumerable<ListWatchlistsResponse, Watchlist> response = entityServiceClient.ListWatchlistsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Watchlist item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListWatchlistsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Watchlist item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Watchlist> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Watchlist item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListWatchlistsAsync(ListWatchlistsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListWatchlistsResponse, Watchlist> ListWatchlistsAsync(ListWatchlistsRequest request, CallSettings callSettings = null)

Lists all watchlists for the given instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListWatchlistsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.ListWatchlistsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListWatchlistsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.ListWatchlistsResponse)[Watchlist](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.Watchlist)` | A pageable asynchronous sequence of [Watchlist](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.Watchlist) resources.  
**Example**
    
    
    // Create client
    EntityServiceClient entityServiceClient = await EntityServiceClient.CreateAsync();
    // Initialize request argument(s)
    ListWatchlistsRequest request = new ListWatchlistsRequest
    {
        ParentAsInstanceName = InstanceName.FromProjectLocationInstance("[PROJECT]", "[LOCATION]", "[INSTANCE]"),
        Filter = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListWatchlistsResponse, Watchlist> response = entityServiceClient.ListWatchlistsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Watchlist item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListWatchlistsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Watchlist item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Watchlist> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Watchlist item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListWatchlistsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListWatchlistsResponse, Watchlist> ListWatchlistsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists all watchlists for the given instance.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent, which owns this collection of watchlists. Format: `projects/{project}/locations/{location}/instances/{instance}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListWatchlistsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.ListWatchlistsResponse)[Watchlist](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.Watchlist)` | A pageable asynchronous sequence of [Watchlist](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.Watchlist) resources.  
**Example**
    
    
    // Create client
    EntityServiceClient entityServiceClient = await EntityServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/instances/[INSTANCE]";
    // Make the request
    PagedAsyncEnumerable<ListWatchlistsResponse, Watchlist> response = entityServiceClient.ListWatchlistsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Watchlist item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListWatchlistsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Watchlist item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Watchlist> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Watchlist item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.EntityServiceClient#Google_Cloud_Chronicle_V1_EntityServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.EntityServiceClient#Google_Cloud_Chronicle_V1_EntityServiceClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.EntityServiceClient#Google_Cloud_Chronicle_V1_EntityServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.EntityServiceClient#Google_Cloud_Chronicle_V1_EntityServiceClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### UpdateWatchlist(UpdateWatchlistRequest, CallSettings)
    
    
    public virtual Watchlist UpdateWatchlist(UpdateWatchlistRequest request, CallSettings callSettings = null)

Updates the watchlist for the given instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateWatchlistRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.UpdateWatchlistRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Watchlist](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.Watchlist)` | The RPC response.  
**Example**
    
    
    // Create client
    EntityServiceClient entityServiceClient = EntityServiceClient.Create();
    // Initialize request argument(s)
    UpdateWatchlistRequest request = new UpdateWatchlistRequest
    {
        Watchlist = new Watchlist(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Watchlist response = entityServiceClient.UpdateWatchlist(request);
    

### UpdateWatchlist(Watchlist, FieldMask, CallSettings)
    
    
    public virtual Watchlist UpdateWatchlist(Watchlist watchlist, FieldMask updateMask, CallSettings callSettings = null)

Updates the watchlist for the given instance.

**Parameters**  
---  
**Name** | **Description**  
`watchlist` | `[Watchlist](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.Watchlist)`  
Required. The watchlist to update. The watchlist's `name` field is used to identify the watchlist to update. Format: `projects/{project}/locations/{location}/instances/{instance}/watchlists/{watchlist}`  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. The list of fields to update.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Watchlist](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.Watchlist)` | The RPC response.  
**Example**
    
    
    // Create client
    EntityServiceClient entityServiceClient = EntityServiceClient.Create();
    // Initialize request argument(s)
    Watchlist watchlist = new Watchlist();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Watchlist response = entityServiceClient.UpdateWatchlist(watchlist, updateMask);
    

### UpdateWatchlistAsync(UpdateWatchlistRequest, CallSettings)
    
    
    public virtual Task<Watchlist> UpdateWatchlistAsync(UpdateWatchlistRequest request, CallSettings callSettings = null)

Updates the watchlist for the given instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateWatchlistRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.UpdateWatchlistRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Watchlist](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.Watchlist)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EntityServiceClient entityServiceClient = await EntityServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateWatchlistRequest request = new UpdateWatchlistRequest
    {
        Watchlist = new Watchlist(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Watchlist response = await entityServiceClient.UpdateWatchlistAsync(request);
    

### UpdateWatchlistAsync(UpdateWatchlistRequest, CancellationToken)
    
    
    public virtual Task<Watchlist> UpdateWatchlistAsync(UpdateWatchlistRequest request, CancellationToken cancellationToken)

Updates the watchlist for the given instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateWatchlistRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.UpdateWatchlistRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Watchlist](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.Watchlist)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EntityServiceClient entityServiceClient = await EntityServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateWatchlistRequest request = new UpdateWatchlistRequest
    {
        Watchlist = new Watchlist(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Watchlist response = await entityServiceClient.UpdateWatchlistAsync(request);
    

### UpdateWatchlistAsync(Watchlist, FieldMask, CallSettings)
    
    
    public virtual Task<Watchlist> UpdateWatchlistAsync(Watchlist watchlist, FieldMask updateMask, CallSettings callSettings = null)

Updates the watchlist for the given instance.

**Parameters**  
---  
**Name** | **Description**  
`watchlist` | `[Watchlist](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.Watchlist)`  
Required. The watchlist to update. The watchlist's `name` field is used to identify the watchlist to update. Format: `projects/{project}/locations/{location}/instances/{instance}/watchlists/{watchlist}`  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. The list of fields to update.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Watchlist](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.Watchlist)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EntityServiceClient entityServiceClient = await EntityServiceClient.CreateAsync();
    // Initialize request argument(s)
    Watchlist watchlist = new Watchlist();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Watchlist response = await entityServiceClient.UpdateWatchlistAsync(watchlist, updateMask);
    

### UpdateWatchlistAsync(Watchlist, FieldMask, CancellationToken)
    
    
    public virtual Task<Watchlist> UpdateWatchlistAsync(Watchlist watchlist, FieldMask updateMask, CancellationToken cancellationToken)

Updates the watchlist for the given instance.

**Parameters**  
---  
**Name** | **Description**  
`watchlist` | `[Watchlist](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.Watchlist)`  
Required. The watchlist to update. The watchlist's `name` field is used to identify the watchlist to update. Format: `projects/{project}/locations/{location}/instances/{instance}/watchlists/{watchlist}`  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. The list of fields to update.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Watchlist](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.Watchlist)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    EntityServiceClient entityServiceClient = await EntityServiceClient.CreateAsync();
    // Initialize request argument(s)
    Watchlist watchlist = new Watchlist();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Watchlist response = await entityServiceClient.UpdateWatchlistAsync(watchlist, updateMask);
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
