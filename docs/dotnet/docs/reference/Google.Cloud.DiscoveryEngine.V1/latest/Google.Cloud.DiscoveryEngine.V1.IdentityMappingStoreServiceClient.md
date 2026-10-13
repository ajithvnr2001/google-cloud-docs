---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStoreServiceClient
title: Discovery Engine v1 API - Class IdentityMappingStoreServiceClient (1.16.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:10:04.663410+00:00
---

# Discovery Engine v1 API - Class IdentityMappingStoreServiceClient (1.16.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStoreServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Discovery Engine v1 API - Class IdentityMappingStoreServiceClient (1.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.16.0 (latest)  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0-beta06 
    
    
    public abstract class IdentityMappingStoreServiceClient

Reference documentation and code samples for the Discovery Engine v1 API class IdentityMappingStoreServiceClient.

IdentityMappingStoreService client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > IdentityMappingStoreServiceClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[IdentityMappingStoreServiceClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStoreServiceClientImpl)

## Namespace

[Google.Cloud.DiscoveryEngine.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1)

## Assembly

Google.Cloud.DiscoveryEngine.V1.dll

## Remarks

Service for managing Identity Mapping Stores.

## Properties 

### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the IdentityMappingStoreService service, which is a host of "discoveryengine.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default IdentityMappingStoreService scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default IdentityMappingStoreService scopes are:

  * <https://www.googleapis.com/auth/cloud-platform>



### DeleteIdentityMappingStoreOperationsClient
    
    
    public virtual OperationsClient DeleteIdentityMappingStoreOperationsClient { get; }

The long-running operations client for `DeleteIdentityMappingStore`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### GrpcClient
    
    
    public virtual IdentityMappingStoreService.IdentityMappingStoreServiceClient GrpcClient { get; }

The underlying gRPC IdentityMappingStoreService client

**Property Value**  
---  
**Type** | **Description**  
`[IdentityMappingStoreService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStoreService)[IdentityMappingStoreServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStoreService.IdentityMappingStoreServiceClient)` |   
  
### ImportIdentityMappingsOperationsClient
    
    
    public virtual OperationsClient ImportIdentityMappingsOperationsClient { get; }

The long-running operations client for `ImportIdentityMappings`.

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
  
### PurgeIdentityMappingsOperationsClient
    
    
    public virtual OperationsClient PurgeIdentityMappingsOperationsClient { get; }

The long-running operations client for `PurgeIdentityMappings`.

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
    
    
    public static IdentityMappingStoreServiceClient Create()

Synchronously creates a [IdentityMappingStoreServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStoreServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [IdentityMappingStoreServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStoreServiceClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[IdentityMappingStoreServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStoreServiceClient)` | The created [IdentityMappingStoreServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStoreServiceClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<IdentityMappingStoreServiceClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [IdentityMappingStoreServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStoreServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [IdentityMappingStoreServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStoreServiceClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IdentityMappingStoreServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStoreServiceClient)` | The task representing the created [IdentityMappingStoreServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStoreServiceClient).  
  
### CreateIdentityMappingStore(CreateIdentityMappingStoreRequest, CallSettings)
    
    
    public virtual IdentityMappingStore CreateIdentityMappingStore(CreateIdentityMappingStoreRequest request, CallSettings callSettings = null)

Creates a new Identity Mapping Store.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateIdentityMappingStoreRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.CreateIdentityMappingStoreRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[IdentityMappingStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStore)` | The RPC response.  
**Example**
    
    
    // Create client
    IdentityMappingStoreServiceClient identityMappingStoreServiceClient = IdentityMappingStoreServiceClient.Create();
    // Initialize request argument(s)
    CreateIdentityMappingStoreRequest request = new CreateIdentityMappingStoreRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        IdentityMappingStoreId = "",
        IdentityMappingStore = new IdentityMappingStore(),
        CmekConfigNameAsCmekConfigName = CmekConfigName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    IdentityMappingStore response = identityMappingStoreServiceClient.CreateIdentityMappingStore(request);
    

### CreateIdentityMappingStore(LocationName, IdentityMappingStore, string, CallSettings)
    
    
    public virtual IdentityMappingStore CreateIdentityMappingStore(LocationName parent, IdentityMappingStore identityMappingStore, string identityMappingStoreId, CallSettings callSettings = null)

Creates a new Identity Mapping Store.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.LocationName)`  
Required. The parent collection resource name, such as `projects/{project}/locations/{location}`.  
`identityMappingStore` | `[IdentityMappingStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStore)`  
Required. The Identity Mapping Store to create.  
`identityMappingStoreId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID of the Identity Mapping Store to create. The ID must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), and hyphens (-). The maximum length is 63 characters.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[IdentityMappingStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStore)` | The RPC response.  
**Example**
    
    
    // Create client
    IdentityMappingStoreServiceClient identityMappingStoreServiceClient = IdentityMappingStoreServiceClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    IdentityMappingStore identityMappingStore = new IdentityMappingStore();
    string identityMappingStoreId = "";
    // Make the request
    IdentityMappingStore response = identityMappingStoreServiceClient.CreateIdentityMappingStore(parent, identityMappingStore, identityMappingStoreId);
    

### CreateIdentityMappingStore(string, IdentityMappingStore, string, CallSettings)
    
    
    public virtual IdentityMappingStore CreateIdentityMappingStore(string parent, IdentityMappingStore identityMappingStore, string identityMappingStoreId, CallSettings callSettings = null)

Creates a new Identity Mapping Store.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent collection resource name, such as `projects/{project}/locations/{location}`.  
`identityMappingStore` | `[IdentityMappingStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStore)`  
Required. The Identity Mapping Store to create.  
`identityMappingStoreId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID of the Identity Mapping Store to create. The ID must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), and hyphens (-). The maximum length is 63 characters.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[IdentityMappingStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStore)` | The RPC response.  
**Example**
    
    
    // Create client
    IdentityMappingStoreServiceClient identityMappingStoreServiceClient = IdentityMappingStoreServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    IdentityMappingStore identityMappingStore = new IdentityMappingStore();
    string identityMappingStoreId = "";
    // Make the request
    IdentityMappingStore response = identityMappingStoreServiceClient.CreateIdentityMappingStore(parent, identityMappingStore, identityMappingStoreId);
    

### CreateIdentityMappingStoreAsync(CreateIdentityMappingStoreRequest, CallSettings)
    
    
    public virtual Task<IdentityMappingStore> CreateIdentityMappingStoreAsync(CreateIdentityMappingStoreRequest request, CallSettings callSettings = null)

Creates a new Identity Mapping Store.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateIdentityMappingStoreRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.CreateIdentityMappingStoreRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IdentityMappingStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStore)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    IdentityMappingStoreServiceClient identityMappingStoreServiceClient = await IdentityMappingStoreServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateIdentityMappingStoreRequest request = new CreateIdentityMappingStoreRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        IdentityMappingStoreId = "",
        IdentityMappingStore = new IdentityMappingStore(),
        CmekConfigNameAsCmekConfigName = CmekConfigName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    IdentityMappingStore response = await identityMappingStoreServiceClient.CreateIdentityMappingStoreAsync(request);
    

### CreateIdentityMappingStoreAsync(CreateIdentityMappingStoreRequest, CancellationToken)
    
    
    public virtual Task<IdentityMappingStore> CreateIdentityMappingStoreAsync(CreateIdentityMappingStoreRequest request, CancellationToken cancellationToken)

Creates a new Identity Mapping Store.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateIdentityMappingStoreRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.CreateIdentityMappingStoreRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IdentityMappingStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStore)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    IdentityMappingStoreServiceClient identityMappingStoreServiceClient = await IdentityMappingStoreServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateIdentityMappingStoreRequest request = new CreateIdentityMappingStoreRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        IdentityMappingStoreId = "",
        IdentityMappingStore = new IdentityMappingStore(),
        CmekConfigNameAsCmekConfigName = CmekConfigName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    IdentityMappingStore response = await identityMappingStoreServiceClient.CreateIdentityMappingStoreAsync(request);
    

### CreateIdentityMappingStoreAsync(LocationName, IdentityMappingStore, string, CallSettings)
    
    
    public virtual Task<IdentityMappingStore> CreateIdentityMappingStoreAsync(LocationName parent, IdentityMappingStore identityMappingStore, string identityMappingStoreId, CallSettings callSettings = null)

Creates a new Identity Mapping Store.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.LocationName)`  
Required. The parent collection resource name, such as `projects/{project}/locations/{location}`.  
`identityMappingStore` | `[IdentityMappingStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStore)`  
Required. The Identity Mapping Store to create.  
`identityMappingStoreId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID of the Identity Mapping Store to create. The ID must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), and hyphens (-). The maximum length is 63 characters.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IdentityMappingStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStore)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    IdentityMappingStoreServiceClient identityMappingStoreServiceClient = await IdentityMappingStoreServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    IdentityMappingStore identityMappingStore = new IdentityMappingStore();
    string identityMappingStoreId = "";
    // Make the request
    IdentityMappingStore response = await identityMappingStoreServiceClient.CreateIdentityMappingStoreAsync(parent, identityMappingStore, identityMappingStoreId);
    

### CreateIdentityMappingStoreAsync(LocationName, IdentityMappingStore, string, CancellationToken)
    
    
    public virtual Task<IdentityMappingStore> CreateIdentityMappingStoreAsync(LocationName parent, IdentityMappingStore identityMappingStore, string identityMappingStoreId, CancellationToken cancellationToken)

Creates a new Identity Mapping Store.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.LocationName)`  
Required. The parent collection resource name, such as `projects/{project}/locations/{location}`.  
`identityMappingStore` | `[IdentityMappingStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStore)`  
Required. The Identity Mapping Store to create.  
`identityMappingStoreId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID of the Identity Mapping Store to create. The ID must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), and hyphens (-). The maximum length is 63 characters.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IdentityMappingStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStore)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    IdentityMappingStoreServiceClient identityMappingStoreServiceClient = await IdentityMappingStoreServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    IdentityMappingStore identityMappingStore = new IdentityMappingStore();
    string identityMappingStoreId = "";
    // Make the request
    IdentityMappingStore response = await identityMappingStoreServiceClient.CreateIdentityMappingStoreAsync(parent, identityMappingStore, identityMappingStoreId);
    

### CreateIdentityMappingStoreAsync(string, IdentityMappingStore, string, CallSettings)
    
    
    public virtual Task<IdentityMappingStore> CreateIdentityMappingStoreAsync(string parent, IdentityMappingStore identityMappingStore, string identityMappingStoreId, CallSettings callSettings = null)

Creates a new Identity Mapping Store.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent collection resource name, such as `projects/{project}/locations/{location}`.  
`identityMappingStore` | `[IdentityMappingStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStore)`  
Required. The Identity Mapping Store to create.  
`identityMappingStoreId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID of the Identity Mapping Store to create. The ID must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), and hyphens (-). The maximum length is 63 characters.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IdentityMappingStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStore)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    IdentityMappingStoreServiceClient identityMappingStoreServiceClient = await IdentityMappingStoreServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    IdentityMappingStore identityMappingStore = new IdentityMappingStore();
    string identityMappingStoreId = "";
    // Make the request
    IdentityMappingStore response = await identityMappingStoreServiceClient.CreateIdentityMappingStoreAsync(parent, identityMappingStore, identityMappingStoreId);
    

### CreateIdentityMappingStoreAsync(string, IdentityMappingStore, string, CancellationToken)
    
    
    public virtual Task<IdentityMappingStore> CreateIdentityMappingStoreAsync(string parent, IdentityMappingStore identityMappingStore, string identityMappingStoreId, CancellationToken cancellationToken)

Creates a new Identity Mapping Store.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent collection resource name, such as `projects/{project}/locations/{location}`.  
`identityMappingStore` | `[IdentityMappingStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStore)`  
Required. The Identity Mapping Store to create.  
`identityMappingStoreId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID of the Identity Mapping Store to create. The ID must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), and hyphens (-). The maximum length is 63 characters.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IdentityMappingStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStore)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    IdentityMappingStoreServiceClient identityMappingStoreServiceClient = await IdentityMappingStoreServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    IdentityMappingStore identityMappingStore = new IdentityMappingStore();
    string identityMappingStoreId = "";
    // Make the request
    IdentityMappingStore response = await identityMappingStoreServiceClient.CreateIdentityMappingStoreAsync(parent, identityMappingStore, identityMappingStoreId);
    

### DeleteIdentityMappingStore(DeleteIdentityMappingStoreRequest, CallSettings)
    
    
    public virtual Operation<Empty, DeleteIdentityMappingStoreMetadata> DeleteIdentityMappingStore(DeleteIdentityMappingStoreRequest request, CallSettings callSettings = null)

Deletes the Identity Mapping Store.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteIdentityMappingStoreRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DeleteIdentityMappingStoreRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteIdentityMappingStoreMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DeleteIdentityMappingStoreMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    IdentityMappingStoreServiceClient identityMappingStoreServiceClient = IdentityMappingStoreServiceClient.Create();
    // Initialize request argument(s)
    DeleteIdentityMappingStoreRequest request = new DeleteIdentityMappingStoreRequest
    {
        IdentityMappingStoreName = IdentityMappingStoreName.FromProjectLocationIdentityMappingStore("[PROJECT]", "[LOCATION]", "[IDENTITY_MAPPING_STORE]"),
    };
    // Make the request
    Operation<Empty, DeleteIdentityMappingStoreMetadata> response = identityMappingStoreServiceClient.DeleteIdentityMappingStore(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteIdentityMappingStoreMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteIdentityMappingStoreMetadata> retrievedResponse = identityMappingStoreServiceClient.PollOnceDeleteIdentityMappingStore(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteIdentityMappingStore(IdentityMappingStoreName, CallSettings)
    
    
    public virtual Operation<Empty, DeleteIdentityMappingStoreMetadata> DeleteIdentityMappingStore(IdentityMappingStoreName name, CallSettings callSettings = null)

Deletes the Identity Mapping Store.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[IdentityMappingStoreName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStoreName)`  
Required. The name of the Identity Mapping Store to delete. Format: `projects/{project}/locations/{location}/identityMappingStores/{identityMappingStore}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteIdentityMappingStoreMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DeleteIdentityMappingStoreMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    IdentityMappingStoreServiceClient identityMappingStoreServiceClient = IdentityMappingStoreServiceClient.Create();
    // Initialize request argument(s)
    IdentityMappingStoreName name = IdentityMappingStoreName.FromProjectLocationIdentityMappingStore("[PROJECT]", "[LOCATION]", "[IDENTITY_MAPPING_STORE]");
    // Make the request
    Operation<Empty, DeleteIdentityMappingStoreMetadata> response = identityMappingStoreServiceClient.DeleteIdentityMappingStore(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteIdentityMappingStoreMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteIdentityMappingStoreMetadata> retrievedResponse = identityMappingStoreServiceClient.PollOnceDeleteIdentityMappingStore(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteIdentityMappingStore(string, CallSettings)
    
    
    public virtual Operation<Empty, DeleteIdentityMappingStoreMetadata> DeleteIdentityMappingStore(string name, CallSettings callSettings = null)

Deletes the Identity Mapping Store.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Identity Mapping Store to delete. Format: `projects/{project}/locations/{location}/identityMappingStores/{identityMappingStore}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteIdentityMappingStoreMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DeleteIdentityMappingStoreMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    IdentityMappingStoreServiceClient identityMappingStoreServiceClient = IdentityMappingStoreServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/identityMappingStores/[IDENTITY_MAPPING_STORE]";
    // Make the request
    Operation<Empty, DeleteIdentityMappingStoreMetadata> response = identityMappingStoreServiceClient.DeleteIdentityMappingStore(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteIdentityMappingStoreMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteIdentityMappingStoreMetadata> retrievedResponse = identityMappingStoreServiceClient.PollOnceDeleteIdentityMappingStore(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteIdentityMappingStoreAsync(DeleteIdentityMappingStoreRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteIdentityMappingStoreMetadata>> DeleteIdentityMappingStoreAsync(DeleteIdentityMappingStoreRequest request, CallSettings callSettings = null)

Deletes the Identity Mapping Store.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteIdentityMappingStoreRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DeleteIdentityMappingStoreRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteIdentityMappingStoreMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DeleteIdentityMappingStoreMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    IdentityMappingStoreServiceClient identityMappingStoreServiceClient = await IdentityMappingStoreServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteIdentityMappingStoreRequest request = new DeleteIdentityMappingStoreRequest
    {
        IdentityMappingStoreName = IdentityMappingStoreName.FromProjectLocationIdentityMappingStore("[PROJECT]", "[LOCATION]", "[IDENTITY_MAPPING_STORE]"),
    };
    // Make the request
    Operation<Empty, DeleteIdentityMappingStoreMetadata> response = await identityMappingStoreServiceClient.DeleteIdentityMappingStoreAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteIdentityMappingStoreMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteIdentityMappingStoreMetadata> retrievedResponse = await identityMappingStoreServiceClient.PollOnceDeleteIdentityMappingStoreAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteIdentityMappingStoreAsync(DeleteIdentityMappingStoreRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, DeleteIdentityMappingStoreMetadata>> DeleteIdentityMappingStoreAsync(DeleteIdentityMappingStoreRequest request, CancellationToken cancellationToken)

Deletes the Identity Mapping Store.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteIdentityMappingStoreRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DeleteIdentityMappingStoreRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteIdentityMappingStoreMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DeleteIdentityMappingStoreMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    IdentityMappingStoreServiceClient identityMappingStoreServiceClient = await IdentityMappingStoreServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteIdentityMappingStoreRequest request = new DeleteIdentityMappingStoreRequest
    {
        IdentityMappingStoreName = IdentityMappingStoreName.FromProjectLocationIdentityMappingStore("[PROJECT]", "[LOCATION]", "[IDENTITY_MAPPING_STORE]"),
    };
    // Make the request
    Operation<Empty, DeleteIdentityMappingStoreMetadata> response = await identityMappingStoreServiceClient.DeleteIdentityMappingStoreAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteIdentityMappingStoreMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteIdentityMappingStoreMetadata> retrievedResponse = await identityMappingStoreServiceClient.PollOnceDeleteIdentityMappingStoreAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteIdentityMappingStoreAsync(IdentityMappingStoreName, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteIdentityMappingStoreMetadata>> DeleteIdentityMappingStoreAsync(IdentityMappingStoreName name, CallSettings callSettings = null)

Deletes the Identity Mapping Store.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[IdentityMappingStoreName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStoreName)`  
Required. The name of the Identity Mapping Store to delete. Format: `projects/{project}/locations/{location}/identityMappingStores/{identityMappingStore}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteIdentityMappingStoreMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DeleteIdentityMappingStoreMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    IdentityMappingStoreServiceClient identityMappingStoreServiceClient = await IdentityMappingStoreServiceClient.CreateAsync();
    // Initialize request argument(s)
    IdentityMappingStoreName name = IdentityMappingStoreName.FromProjectLocationIdentityMappingStore("[PROJECT]", "[LOCATION]", "[IDENTITY_MAPPING_STORE]");
    // Make the request
    Operation<Empty, DeleteIdentityMappingStoreMetadata> response = await identityMappingStoreServiceClient.DeleteIdentityMappingStoreAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteIdentityMappingStoreMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteIdentityMappingStoreMetadata> retrievedResponse = await identityMappingStoreServiceClient.PollOnceDeleteIdentityMappingStoreAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteIdentityMappingStoreAsync(IdentityMappingStoreName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, DeleteIdentityMappingStoreMetadata>> DeleteIdentityMappingStoreAsync(IdentityMappingStoreName name, CancellationToken cancellationToken)

Deletes the Identity Mapping Store.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[IdentityMappingStoreName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStoreName)`  
Required. The name of the Identity Mapping Store to delete. Format: `projects/{project}/locations/{location}/identityMappingStores/{identityMappingStore}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteIdentityMappingStoreMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DeleteIdentityMappingStoreMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    IdentityMappingStoreServiceClient identityMappingStoreServiceClient = await IdentityMappingStoreServiceClient.CreateAsync();
    // Initialize request argument(s)
    IdentityMappingStoreName name = IdentityMappingStoreName.FromProjectLocationIdentityMappingStore("[PROJECT]", "[LOCATION]", "[IDENTITY_MAPPING_STORE]");
    // Make the request
    Operation<Empty, DeleteIdentityMappingStoreMetadata> response = await identityMappingStoreServiceClient.DeleteIdentityMappingStoreAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteIdentityMappingStoreMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteIdentityMappingStoreMetadata> retrievedResponse = await identityMappingStoreServiceClient.PollOnceDeleteIdentityMappingStoreAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteIdentityMappingStoreAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteIdentityMappingStoreMetadata>> DeleteIdentityMappingStoreAsync(string name, CallSettings callSettings = null)

Deletes the Identity Mapping Store.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Identity Mapping Store to delete. Format: `projects/{project}/locations/{location}/identityMappingStores/{identityMappingStore}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteIdentityMappingStoreMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DeleteIdentityMappingStoreMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    IdentityMappingStoreServiceClient identityMappingStoreServiceClient = await IdentityMappingStoreServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/identityMappingStores/[IDENTITY_MAPPING_STORE]";
    // Make the request
    Operation<Empty, DeleteIdentityMappingStoreMetadata> response = await identityMappingStoreServiceClient.DeleteIdentityMappingStoreAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteIdentityMappingStoreMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteIdentityMappingStoreMetadata> retrievedResponse = await identityMappingStoreServiceClient.PollOnceDeleteIdentityMappingStoreAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteIdentityMappingStoreAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, DeleteIdentityMappingStoreMetadata>> DeleteIdentityMappingStoreAsync(string name, CancellationToken cancellationToken)

Deletes the Identity Mapping Store.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Identity Mapping Store to delete. Format: `projects/{project}/locations/{location}/identityMappingStores/{identityMappingStore}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteIdentityMappingStoreMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DeleteIdentityMappingStoreMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    IdentityMappingStoreServiceClient identityMappingStoreServiceClient = await IdentityMappingStoreServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/identityMappingStores/[IDENTITY_MAPPING_STORE]";
    // Make the request
    Operation<Empty, DeleteIdentityMappingStoreMetadata> response = await identityMappingStoreServiceClient.DeleteIdentityMappingStoreAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteIdentityMappingStoreMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteIdentityMappingStoreMetadata> retrievedResponse = await identityMappingStoreServiceClient.PollOnceDeleteIdentityMappingStoreAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### GetIdentityMappingStore(GetIdentityMappingStoreRequest, CallSettings)
    
    
    public virtual IdentityMappingStore GetIdentityMappingStore(GetIdentityMappingStoreRequest request, CallSettings callSettings = null)

Gets the Identity Mapping Store.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetIdentityMappingStoreRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.GetIdentityMappingStoreRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[IdentityMappingStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStore)` | The RPC response.  
**Example**
    
    
    // Create client
    IdentityMappingStoreServiceClient identityMappingStoreServiceClient = IdentityMappingStoreServiceClient.Create();
    // Initialize request argument(s)
    GetIdentityMappingStoreRequest request = new GetIdentityMappingStoreRequest
    {
        IdentityMappingStoreName = IdentityMappingStoreName.FromProjectLocationIdentityMappingStore("[PROJECT]", "[LOCATION]", "[IDENTITY_MAPPING_STORE]"),
    };
    // Make the request
    IdentityMappingStore response = identityMappingStoreServiceClient.GetIdentityMappingStore(request);
    

### GetIdentityMappingStore(IdentityMappingStoreName, CallSettings)
    
    
    public virtual IdentityMappingStore GetIdentityMappingStore(IdentityMappingStoreName name, CallSettings callSettings = null)

Gets the Identity Mapping Store.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[IdentityMappingStoreName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStoreName)`  
Required. The name of the Identity Mapping Store to get. Format: `projects/{project}/locations/{location}/identityMappingStores/{identityMappingStore}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[IdentityMappingStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStore)` | The RPC response.  
**Example**
    
    
    // Create client
    IdentityMappingStoreServiceClient identityMappingStoreServiceClient = IdentityMappingStoreServiceClient.Create();
    // Initialize request argument(s)
    IdentityMappingStoreName name = IdentityMappingStoreName.FromProjectLocationIdentityMappingStore("[PROJECT]", "[LOCATION]", "[IDENTITY_MAPPING_STORE]");
    // Make the request
    IdentityMappingStore response = identityMappingStoreServiceClient.GetIdentityMappingStore(name);
    

### GetIdentityMappingStore(string, CallSettings)
    
    
    public virtual IdentityMappingStore GetIdentityMappingStore(string name, CallSettings callSettings = null)

Gets the Identity Mapping Store.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Identity Mapping Store to get. Format: `projects/{project}/locations/{location}/identityMappingStores/{identityMappingStore}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[IdentityMappingStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStore)` | The RPC response.  
**Example**
    
    
    // Create client
    IdentityMappingStoreServiceClient identityMappingStoreServiceClient = IdentityMappingStoreServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/identityMappingStores/[IDENTITY_MAPPING_STORE]";
    // Make the request
    IdentityMappingStore response = identityMappingStoreServiceClient.GetIdentityMappingStore(name);
    

### GetIdentityMappingStoreAsync(GetIdentityMappingStoreRequest, CallSettings)
    
    
    public virtual Task<IdentityMappingStore> GetIdentityMappingStoreAsync(GetIdentityMappingStoreRequest request, CallSettings callSettings = null)

Gets the Identity Mapping Store.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetIdentityMappingStoreRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.GetIdentityMappingStoreRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IdentityMappingStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStore)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    IdentityMappingStoreServiceClient identityMappingStoreServiceClient = await IdentityMappingStoreServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetIdentityMappingStoreRequest request = new GetIdentityMappingStoreRequest
    {
        IdentityMappingStoreName = IdentityMappingStoreName.FromProjectLocationIdentityMappingStore("[PROJECT]", "[LOCATION]", "[IDENTITY_MAPPING_STORE]"),
    };
    // Make the request
    IdentityMappingStore response = await identityMappingStoreServiceClient.GetIdentityMappingStoreAsync(request);
    

### GetIdentityMappingStoreAsync(GetIdentityMappingStoreRequest, CancellationToken)
    
    
    public virtual Task<IdentityMappingStore> GetIdentityMappingStoreAsync(GetIdentityMappingStoreRequest request, CancellationToken cancellationToken)

Gets the Identity Mapping Store.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetIdentityMappingStoreRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.GetIdentityMappingStoreRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IdentityMappingStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStore)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    IdentityMappingStoreServiceClient identityMappingStoreServiceClient = await IdentityMappingStoreServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetIdentityMappingStoreRequest request = new GetIdentityMappingStoreRequest
    {
        IdentityMappingStoreName = IdentityMappingStoreName.FromProjectLocationIdentityMappingStore("[PROJECT]", "[LOCATION]", "[IDENTITY_MAPPING_STORE]"),
    };
    // Make the request
    IdentityMappingStore response = await identityMappingStoreServiceClient.GetIdentityMappingStoreAsync(request);
    

### GetIdentityMappingStoreAsync(IdentityMappingStoreName, CallSettings)
    
    
    public virtual Task<IdentityMappingStore> GetIdentityMappingStoreAsync(IdentityMappingStoreName name, CallSettings callSettings = null)

Gets the Identity Mapping Store.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[IdentityMappingStoreName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStoreName)`  
Required. The name of the Identity Mapping Store to get. Format: `projects/{project}/locations/{location}/identityMappingStores/{identityMappingStore}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IdentityMappingStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStore)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    IdentityMappingStoreServiceClient identityMappingStoreServiceClient = await IdentityMappingStoreServiceClient.CreateAsync();
    // Initialize request argument(s)
    IdentityMappingStoreName name = IdentityMappingStoreName.FromProjectLocationIdentityMappingStore("[PROJECT]", "[LOCATION]", "[IDENTITY_MAPPING_STORE]");
    // Make the request
    IdentityMappingStore response = await identityMappingStoreServiceClient.GetIdentityMappingStoreAsync(name);
    

### GetIdentityMappingStoreAsync(IdentityMappingStoreName, CancellationToken)
    
    
    public virtual Task<IdentityMappingStore> GetIdentityMappingStoreAsync(IdentityMappingStoreName name, CancellationToken cancellationToken)

Gets the Identity Mapping Store.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[IdentityMappingStoreName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStoreName)`  
Required. The name of the Identity Mapping Store to get. Format: `projects/{project}/locations/{location}/identityMappingStores/{identityMappingStore}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IdentityMappingStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStore)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    IdentityMappingStoreServiceClient identityMappingStoreServiceClient = await IdentityMappingStoreServiceClient.CreateAsync();
    // Initialize request argument(s)
    IdentityMappingStoreName name = IdentityMappingStoreName.FromProjectLocationIdentityMappingStore("[PROJECT]", "[LOCATION]", "[IDENTITY_MAPPING_STORE]");
    // Make the request
    IdentityMappingStore response = await identityMappingStoreServiceClient.GetIdentityMappingStoreAsync(name);
    

### GetIdentityMappingStoreAsync(string, CallSettings)
    
    
    public virtual Task<IdentityMappingStore> GetIdentityMappingStoreAsync(string name, CallSettings callSettings = null)

Gets the Identity Mapping Store.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Identity Mapping Store to get. Format: `projects/{project}/locations/{location}/identityMappingStores/{identityMappingStore}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IdentityMappingStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStore)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    IdentityMappingStoreServiceClient identityMappingStoreServiceClient = await IdentityMappingStoreServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/identityMappingStores/[IDENTITY_MAPPING_STORE]";
    // Make the request
    IdentityMappingStore response = await identityMappingStoreServiceClient.GetIdentityMappingStoreAsync(name);
    

### GetIdentityMappingStoreAsync(string, CancellationToken)
    
    
    public virtual Task<IdentityMappingStore> GetIdentityMappingStoreAsync(string name, CancellationToken cancellationToken)

Gets the Identity Mapping Store.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Identity Mapping Store to get. Format: `projects/{project}/locations/{location}/identityMappingStores/{identityMappingStore}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IdentityMappingStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStore)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    IdentityMappingStoreServiceClient identityMappingStoreServiceClient = await IdentityMappingStoreServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/identityMappingStores/[IDENTITY_MAPPING_STORE]";
    // Make the request
    IdentityMappingStore response = await identityMappingStoreServiceClient.GetIdentityMappingStoreAsync(name);
    

### ImportIdentityMappings(ImportIdentityMappingsRequest, CallSettings)
    
    
    public virtual Operation<ImportIdentityMappingsResponse, IdentityMappingEntryOperationMetadata> ImportIdentityMappings(ImportIdentityMappingsRequest request, CallSettings callSettings = null)

Imports a list of Identity Mapping Entries to an Identity Mapping Store.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportIdentityMappingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.ImportIdentityMappingsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportIdentityMappingsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.ImportIdentityMappingsResponse)[IdentityMappingEntryOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingEntryOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    IdentityMappingStoreServiceClient identityMappingStoreServiceClient = IdentityMappingStoreServiceClient.Create();
    // Initialize request argument(s)
    ImportIdentityMappingsRequest request = new ImportIdentityMappingsRequest
    {
        IdentityMappingStoreAsIdentityMappingStoreName = IdentityMappingStoreName.FromProjectLocationIdentityMappingStore("[PROJECT]", "[LOCATION]", "[IDENTITY_MAPPING_STORE]"),
        InlineSource = new ImportIdentityMappingsRequest.Types.InlineSource(),
    };
    // Make the request
    Operation<ImportIdentityMappingsResponse, IdentityMappingEntryOperationMetadata> response = identityMappingStoreServiceClient.ImportIdentityMappings(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ImportIdentityMappingsResponse, IdentityMappingEntryOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    ImportIdentityMappingsResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ImportIdentityMappingsResponse, IdentityMappingEntryOperationMetadata> retrievedResponse = identityMappingStoreServiceClient.PollOnceImportIdentityMappings(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ImportIdentityMappingsResponse retrievedResult = retrievedResponse.Result;
    }
    

### ImportIdentityMappingsAsync(ImportIdentityMappingsRequest, CallSettings)
    
    
    public virtual Task<Operation<ImportIdentityMappingsResponse, IdentityMappingEntryOperationMetadata>> ImportIdentityMappingsAsync(ImportIdentityMappingsRequest request, CallSettings callSettings = null)

Imports a list of Identity Mapping Entries to an Identity Mapping Store.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportIdentityMappingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.ImportIdentityMappingsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportIdentityMappingsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.ImportIdentityMappingsResponse)[IdentityMappingEntryOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingEntryOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    IdentityMappingStoreServiceClient identityMappingStoreServiceClient = await IdentityMappingStoreServiceClient.CreateAsync();
    // Initialize request argument(s)
    ImportIdentityMappingsRequest request = new ImportIdentityMappingsRequest
    {
        IdentityMappingStoreAsIdentityMappingStoreName = IdentityMappingStoreName.FromProjectLocationIdentityMappingStore("[PROJECT]", "[LOCATION]", "[IDENTITY_MAPPING_STORE]"),
        InlineSource = new ImportIdentityMappingsRequest.Types.InlineSource(),
    };
    // Make the request
    Operation<ImportIdentityMappingsResponse, IdentityMappingEntryOperationMetadata> response = await identityMappingStoreServiceClient.ImportIdentityMappingsAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ImportIdentityMappingsResponse, IdentityMappingEntryOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ImportIdentityMappingsResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ImportIdentityMappingsResponse, IdentityMappingEntryOperationMetadata> retrievedResponse = await identityMappingStoreServiceClient.PollOnceImportIdentityMappingsAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ImportIdentityMappingsResponse retrievedResult = retrievedResponse.Result;
    }
    

### ImportIdentityMappingsAsync(ImportIdentityMappingsRequest, CancellationToken)
    
    
    public virtual Task<Operation<ImportIdentityMappingsResponse, IdentityMappingEntryOperationMetadata>> ImportIdentityMappingsAsync(ImportIdentityMappingsRequest request, CancellationToken cancellationToken)

Imports a list of Identity Mapping Entries to an Identity Mapping Store.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportIdentityMappingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.ImportIdentityMappingsRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportIdentityMappingsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.ImportIdentityMappingsResponse)[IdentityMappingEntryOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingEntryOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    IdentityMappingStoreServiceClient identityMappingStoreServiceClient = await IdentityMappingStoreServiceClient.CreateAsync();
    // Initialize request argument(s)
    ImportIdentityMappingsRequest request = new ImportIdentityMappingsRequest
    {
        IdentityMappingStoreAsIdentityMappingStoreName = IdentityMappingStoreName.FromProjectLocationIdentityMappingStore("[PROJECT]", "[LOCATION]", "[IDENTITY_MAPPING_STORE]"),
        InlineSource = new ImportIdentityMappingsRequest.Types.InlineSource(),
    };
    // Make the request
    Operation<ImportIdentityMappingsResponse, IdentityMappingEntryOperationMetadata> response = await identityMappingStoreServiceClient.ImportIdentityMappingsAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ImportIdentityMappingsResponse, IdentityMappingEntryOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ImportIdentityMappingsResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ImportIdentityMappingsResponse, IdentityMappingEntryOperationMetadata> retrievedResponse = await identityMappingStoreServiceClient.PollOnceImportIdentityMappingsAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ImportIdentityMappingsResponse retrievedResult = retrievedResponse.Result;
    }
    

### ListIdentityMappingStores(ListIdentityMappingStoresRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListIdentityMappingStoresResponse, IdentityMappingStore> ListIdentityMappingStores(ListIdentityMappingStoresRequest request, CallSettings callSettings = null)

Lists all Identity Mapping Stores.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListIdentityMappingStoresRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.ListIdentityMappingStoresRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListIdentityMappingStoresResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.ListIdentityMappingStoresResponse)[IdentityMappingStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStore)` | A pageable sequence of [IdentityMappingStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStore) resources.  
**Example**
    
    
    // Create client
    IdentityMappingStoreServiceClient identityMappingStoreServiceClient = IdentityMappingStoreServiceClient.Create();
    // Initialize request argument(s)
    ListIdentityMappingStoresRequest request = new ListIdentityMappingStoresRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    PagedEnumerable<ListIdentityMappingStoresResponse, IdentityMappingStore> response = identityMappingStoreServiceClient.ListIdentityMappingStores(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (IdentityMappingStore item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListIdentityMappingStoresResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (IdentityMappingStore item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<IdentityMappingStore> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (IdentityMappingStore item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListIdentityMappingStores(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListIdentityMappingStoresResponse, IdentityMappingStore> ListIdentityMappingStores(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists all Identity Mapping Stores.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.LocationName)`  
Required. The parent of the Identity Mapping Stores to list. Format: `projects/{project}/locations/{location}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListIdentityMappingStoresResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.ListIdentityMappingStoresResponse)[IdentityMappingStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStore)` | A pageable sequence of [IdentityMappingStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStore) resources.  
**Example**
    
    
    // Create client
    IdentityMappingStoreServiceClient identityMappingStoreServiceClient = IdentityMappingStoreServiceClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListIdentityMappingStoresResponse, IdentityMappingStore> response = identityMappingStoreServiceClient.ListIdentityMappingStores(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (IdentityMappingStore item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListIdentityMappingStoresResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (IdentityMappingStore item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<IdentityMappingStore> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (IdentityMappingStore item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListIdentityMappingStores(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListIdentityMappingStoresResponse, IdentityMappingStore> ListIdentityMappingStores(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists all Identity Mapping Stores.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent of the Identity Mapping Stores to list. Format: `projects/{project}/locations/{location}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListIdentityMappingStoresResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.ListIdentityMappingStoresResponse)[IdentityMappingStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStore)` | A pageable sequence of [IdentityMappingStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStore) resources.  
**Example**
    
    
    // Create client
    IdentityMappingStoreServiceClient identityMappingStoreServiceClient = IdentityMappingStoreServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListIdentityMappingStoresResponse, IdentityMappingStore> response = identityMappingStoreServiceClient.ListIdentityMappingStores(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (IdentityMappingStore item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListIdentityMappingStoresResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (IdentityMappingStore item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<IdentityMappingStore> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (IdentityMappingStore item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListIdentityMappingStoresAsync(ListIdentityMappingStoresRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListIdentityMappingStoresResponse, IdentityMappingStore> ListIdentityMappingStoresAsync(ListIdentityMappingStoresRequest request, CallSettings callSettings = null)

Lists all Identity Mapping Stores.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListIdentityMappingStoresRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.ListIdentityMappingStoresRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListIdentityMappingStoresResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.ListIdentityMappingStoresResponse)[IdentityMappingStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStore)` | A pageable asynchronous sequence of [IdentityMappingStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStore) resources.  
**Example**
    
    
    // Create client
    IdentityMappingStoreServiceClient identityMappingStoreServiceClient = await IdentityMappingStoreServiceClient.CreateAsync();
    // Initialize request argument(s)
    ListIdentityMappingStoresRequest request = new ListIdentityMappingStoresRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    PagedAsyncEnumerable<ListIdentityMappingStoresResponse, IdentityMappingStore> response = identityMappingStoreServiceClient.ListIdentityMappingStoresAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (IdentityMappingStore item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListIdentityMappingStoresResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (IdentityMappingStore item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<IdentityMappingStore> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (IdentityMappingStore item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListIdentityMappingStoresAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListIdentityMappingStoresResponse, IdentityMappingStore> ListIdentityMappingStoresAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists all Identity Mapping Stores.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.LocationName)`  
Required. The parent of the Identity Mapping Stores to list. Format: `projects/{project}/locations/{location}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListIdentityMappingStoresResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.ListIdentityMappingStoresResponse)[IdentityMappingStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStore)` | A pageable asynchronous sequence of [IdentityMappingStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStore) resources.  
**Example**
    
    
    // Create client
    IdentityMappingStoreServiceClient identityMappingStoreServiceClient = await IdentityMappingStoreServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListIdentityMappingStoresResponse, IdentityMappingStore> response = identityMappingStoreServiceClient.ListIdentityMappingStoresAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (IdentityMappingStore item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListIdentityMappingStoresResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (IdentityMappingStore item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<IdentityMappingStore> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (IdentityMappingStore item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListIdentityMappingStoresAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListIdentityMappingStoresResponse, IdentityMappingStore> ListIdentityMappingStoresAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists all Identity Mapping Stores.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent of the Identity Mapping Stores to list. Format: `projects/{project}/locations/{location}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListIdentityMappingStoresResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.ListIdentityMappingStoresResponse)[IdentityMappingStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStore)` | A pageable asynchronous sequence of [IdentityMappingStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStore) resources.  
**Example**
    
    
    // Create client
    IdentityMappingStoreServiceClient identityMappingStoreServiceClient = await IdentityMappingStoreServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListIdentityMappingStoresResponse, IdentityMappingStore> response = identityMappingStoreServiceClient.ListIdentityMappingStoresAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (IdentityMappingStore item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListIdentityMappingStoresResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (IdentityMappingStore item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<IdentityMappingStore> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (IdentityMappingStore item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListIdentityMappings(ListIdentityMappingsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListIdentityMappingsResponse, IdentityMappingEntry> ListIdentityMappings(ListIdentityMappingsRequest request, CallSettings callSettings = null)

Lists Identity Mappings in an Identity Mapping Store.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListIdentityMappingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.ListIdentityMappingsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListIdentityMappingsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.ListIdentityMappingsResponse)[IdentityMappingEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingEntry)` | A pageable sequence of [IdentityMappingEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingEntry) resources.  
**Example**
    
    
    // Create client
    IdentityMappingStoreServiceClient identityMappingStoreServiceClient = IdentityMappingStoreServiceClient.Create();
    // Initialize request argument(s)
    ListIdentityMappingsRequest request = new ListIdentityMappingsRequest
    {
        IdentityMappingStoreAsIdentityMappingStoreName = IdentityMappingStoreName.FromProjectLocationIdentityMappingStore("[PROJECT]", "[LOCATION]", "[IDENTITY_MAPPING_STORE]"),
    };
    // Make the request
    PagedEnumerable<ListIdentityMappingsResponse, IdentityMappingEntry> response = identityMappingStoreServiceClient.ListIdentityMappings(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (IdentityMappingEntry item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListIdentityMappingsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (IdentityMappingEntry item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<IdentityMappingEntry> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (IdentityMappingEntry item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListIdentityMappingsAsync(ListIdentityMappingsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListIdentityMappingsResponse, IdentityMappingEntry> ListIdentityMappingsAsync(ListIdentityMappingsRequest request, CallSettings callSettings = null)

Lists Identity Mappings in an Identity Mapping Store.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListIdentityMappingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.ListIdentityMappingsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListIdentityMappingsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.ListIdentityMappingsResponse)[IdentityMappingEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingEntry)` | A pageable asynchronous sequence of [IdentityMappingEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingEntry) resources.  
**Example**
    
    
    // Create client
    IdentityMappingStoreServiceClient identityMappingStoreServiceClient = await IdentityMappingStoreServiceClient.CreateAsync();
    // Initialize request argument(s)
    ListIdentityMappingsRequest request = new ListIdentityMappingsRequest
    {
        IdentityMappingStoreAsIdentityMappingStoreName = IdentityMappingStoreName.FromProjectLocationIdentityMappingStore("[PROJECT]", "[LOCATION]", "[IDENTITY_MAPPING_STORE]"),
    };
    // Make the request
    PagedAsyncEnumerable<ListIdentityMappingsResponse, IdentityMappingEntry> response = identityMappingStoreServiceClient.ListIdentityMappingsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (IdentityMappingEntry item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListIdentityMappingsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (IdentityMappingEntry item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<IdentityMappingEntry> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (IdentityMappingEntry item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### PollOnceDeleteIdentityMappingStore(string, CallSettings)
    
    
    public virtual Operation<Empty, DeleteIdentityMappingStoreMetadata> PollOnceDeleteIdentityMappingStore(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteIdentityMappingStore`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteIdentityMappingStoreMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DeleteIdentityMappingStoreMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteIdentityMappingStoreAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteIdentityMappingStoreMetadata>> PollOnceDeleteIdentityMappingStoreAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteIdentityMappingStore`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteIdentityMappingStoreMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DeleteIdentityMappingStoreMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceImportIdentityMappings(string, CallSettings)
    
    
    public virtual Operation<ImportIdentityMappingsResponse, IdentityMappingEntryOperationMetadata> PollOnceImportIdentityMappings(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `ImportIdentityMappings`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportIdentityMappingsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.ImportIdentityMappingsResponse)[IdentityMappingEntryOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingEntryOperationMetadata)` | The result of polling the operation.  
  
### PollOnceImportIdentityMappingsAsync(string, CallSettings)
    
    
    public virtual Task<Operation<ImportIdentityMappingsResponse, IdentityMappingEntryOperationMetadata>> PollOnceImportIdentityMappingsAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `ImportIdentityMappings`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportIdentityMappingsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.ImportIdentityMappingsResponse)[IdentityMappingEntryOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingEntryOperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOncePurgeIdentityMappings(string, CallSettings)
    
    
    public virtual Operation<Empty, IdentityMappingEntryOperationMetadata> PollOncePurgeIdentityMappings(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `PurgeIdentityMappings` .

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[IdentityMappingEntryOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingEntryOperationMetadata)` | The result of polling the operation.  
  
### PollOncePurgeIdentityMappingsAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, IdentityMappingEntryOperationMetadata>> PollOncePurgeIdentityMappingsAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `PurgeIdentityMappings`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[IdentityMappingEntryOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingEntryOperationMetadata)` | A task representing the result of polling the operation.  
  
### PurgeIdentityMappings(PurgeIdentityMappingsRequest, CallSettings)
    
    
    public virtual Operation<Empty, IdentityMappingEntryOperationMetadata> PurgeIdentityMappings(PurgeIdentityMappingsRequest request, CallSettings callSettings = null)

Purges specified or all Identity Mapping Entries from an Identity Mapping Store.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PurgeIdentityMappingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.PurgeIdentityMappingsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[IdentityMappingEntryOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingEntryOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    IdentityMappingStoreServiceClient identityMappingStoreServiceClient = IdentityMappingStoreServiceClient.Create();
    // Initialize request argument(s)
    PurgeIdentityMappingsRequest request = new PurgeIdentityMappingsRequest
    {
        IdentityMappingStoreAsIdentityMappingStoreName = IdentityMappingStoreName.FromProjectLocationIdentityMappingStore("[PROJECT]", "[LOCATION]", "[IDENTITY_MAPPING_STORE]"),
        InlineSource = new PurgeIdentityMappingsRequest.Types.InlineSource(),
        Filter = "",
        Force = false,
    };
    // Make the request
    Operation<Empty, IdentityMappingEntryOperationMetadata> response = identityMappingStoreServiceClient.PurgeIdentityMappings(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, IdentityMappingEntryOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, IdentityMappingEntryOperationMetadata> retrievedResponse = identityMappingStoreServiceClient.PollOncePurgeIdentityMappings(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### PurgeIdentityMappingsAsync(PurgeIdentityMappingsRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, IdentityMappingEntryOperationMetadata>> PurgeIdentityMappingsAsync(PurgeIdentityMappingsRequest request, CallSettings callSettings = null)

Purges specified or all Identity Mapping Entries from an Identity Mapping Store.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PurgeIdentityMappingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.PurgeIdentityMappingsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[IdentityMappingEntryOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingEntryOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    IdentityMappingStoreServiceClient identityMappingStoreServiceClient = await IdentityMappingStoreServiceClient.CreateAsync();
    // Initialize request argument(s)
    PurgeIdentityMappingsRequest request = new PurgeIdentityMappingsRequest
    {
        IdentityMappingStoreAsIdentityMappingStoreName = IdentityMappingStoreName.FromProjectLocationIdentityMappingStore("[PROJECT]", "[LOCATION]", "[IDENTITY_MAPPING_STORE]"),
        InlineSource = new PurgeIdentityMappingsRequest.Types.InlineSource(),
        Filter = "",
        Force = false,
    };
    // Make the request
    Operation<Empty, IdentityMappingEntryOperationMetadata> response = await identityMappingStoreServiceClient.PurgeIdentityMappingsAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, IdentityMappingEntryOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, IdentityMappingEntryOperationMetadata> retrievedResponse = await identityMappingStoreServiceClient.PollOncePurgeIdentityMappingsAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### PurgeIdentityMappingsAsync(PurgeIdentityMappingsRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, IdentityMappingEntryOperationMetadata>> PurgeIdentityMappingsAsync(PurgeIdentityMappingsRequest request, CancellationToken cancellationToken)

Purges specified or all Identity Mapping Entries from an Identity Mapping Store.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PurgeIdentityMappingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.PurgeIdentityMappingsRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[IdentityMappingEntryOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingEntryOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    IdentityMappingStoreServiceClient identityMappingStoreServiceClient = await IdentityMappingStoreServiceClient.CreateAsync();
    // Initialize request argument(s)
    PurgeIdentityMappingsRequest request = new PurgeIdentityMappingsRequest
    {
        IdentityMappingStoreAsIdentityMappingStoreName = IdentityMappingStoreName.FromProjectLocationIdentityMappingStore("[PROJECT]", "[LOCATION]", "[IDENTITY_MAPPING_STORE]"),
        InlineSource = new PurgeIdentityMappingsRequest.Types.InlineSource(),
        Filter = "",
        Force = false,
    };
    // Make the request
    Operation<Empty, IdentityMappingEntryOperationMetadata> response = await identityMappingStoreServiceClient.PurgeIdentityMappingsAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, IdentityMappingEntryOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, IdentityMappingEntryOperationMetadata> retrievedResponse = await identityMappingStoreServiceClient.PollOncePurgeIdentityMappingsAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStoreServiceClient#Google_Cloud_DiscoveryEngine_V1_IdentityMappingStoreServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStoreServiceClient#Google_Cloud_DiscoveryEngine_V1_IdentityMappingStoreServiceClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStoreServiceClient#Google_Cloud_DiscoveryEngine_V1_IdentityMappingStoreServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.IdentityMappingStoreServiceClient#Google_Cloud_DiscoveryEngine_V1_IdentityMappingStoreServiceClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-17 UTC."],[],[]] 
