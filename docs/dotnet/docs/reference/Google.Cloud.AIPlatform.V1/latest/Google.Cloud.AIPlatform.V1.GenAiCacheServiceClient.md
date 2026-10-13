---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GenAiCacheServiceClient
title: Vertex AI v1 API - Class GenAiCacheServiceClient (3.77.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:36:23.574200+00:00
---

# Vertex AI v1 API - Class GenAiCacheServiceClient (3.77.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GenAiCacheServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1 API - Class GenAiCacheServiceClient (3.77.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.77.0 (latest)  3.76.0  3.75.0  3.74.0  3.73.0  3.72.0  3.71.0  3.70.0  3.69.0  3.68.0  3.67.0  3.66.0  3.65.0  3.64.0  3.63.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.51.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.39.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.28.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public abstract class GenAiCacheServiceClient

Reference documentation and code samples for the Vertex AI v1 API class GenAiCacheServiceClient.

GenAiCacheService client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > GenAiCacheServiceClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[GenAiCacheServiceClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GenAiCacheServiceClientImpl)

## Namespace

[Google.Cloud.AIPlatform.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1)

## Assembly

Google.Cloud.AIPlatform.V1.dll

## Remarks

Service for managing Vertex AI's CachedContent resource.

## Properties 

### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the GenAiCacheService service, which is a host of "aiplatform.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default GenAiCacheService scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default GenAiCacheService scopes are:

  * <https://www.googleapis.com/auth/cloud-platform>



### GrpcClient
    
    
    public virtual GenAiCacheService.GenAiCacheServiceClient GrpcClient { get; }

The underlying gRPC GenAiCacheService client

**Property Value**  
---  
**Type** | **Description**  
`[GenAiCacheService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GenAiCacheService)[GenAiCacheServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GenAiCacheService.GenAiCacheServiceClient)` |   
  
### IAMPolicyClient
    
    
    public virtual IAMPolicyClient IAMPolicyClient { get; }

The [IAMPolicyClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.IAMPolicyClient.html) associated with this client.

**Property Value**  
---  
**Type** | **Description**  
`[IAMPolicyClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.IAMPolicyClient.html)` |   
  
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
    
    
    public static GenAiCacheServiceClient Create()

Synchronously creates a [GenAiCacheServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GenAiCacheServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [GenAiCacheServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GenAiCacheServiceClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[GenAiCacheServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GenAiCacheServiceClient)` | The created [GenAiCacheServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GenAiCacheServiceClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<GenAiCacheServiceClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [GenAiCacheServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GenAiCacheServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [GenAiCacheServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GenAiCacheServiceClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GenAiCacheServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GenAiCacheServiceClient)` | The task representing the created [GenAiCacheServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GenAiCacheServiceClient).  
  
### CreateCachedContent(LocationName, CachedContent, CallSettings)
    
    
    public virtual CachedContent CreateCachedContent(LocationName parent, CachedContent cachedContent, CallSettings callSettings = null)

Creates cached content, this call will initialize the cached content in the data storage, and users need to pay for the cache data storage.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent resource where the cached content will be created  
`cachedContent` | `[CachedContent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CachedContent)`  
Required. The cached content to create  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[CachedContent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CachedContent)` | The RPC response.  
**Example**
    
    
    // Create client
    GenAiCacheServiceClient genAiCacheServiceClient = GenAiCacheServiceClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    CachedContent cachedContent = new CachedContent();
    // Make the request
    CachedContent response = genAiCacheServiceClient.CreateCachedContent(parent, cachedContent);
    

### CreateCachedContent(CreateCachedContentRequest, CallSettings)
    
    
    public virtual CachedContent CreateCachedContent(CreateCachedContentRequest request, CallSettings callSettings = null)

Creates cached content, this call will initialize the cached content in the data storage, and users need to pay for the cache data storage.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateCachedContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CreateCachedContentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[CachedContent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CachedContent)` | The RPC response.  
**Example**
    
    
    // Create client
    GenAiCacheServiceClient genAiCacheServiceClient = GenAiCacheServiceClient.Create();
    // Initialize request argument(s)
    CreateCachedContentRequest request = new CreateCachedContentRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        CachedContent = new CachedContent(),
    };
    // Make the request
    CachedContent response = genAiCacheServiceClient.CreateCachedContent(request);
    

### CreateCachedContent(string, CachedContent, CallSettings)
    
    
    public virtual CachedContent CreateCachedContent(string parent, CachedContent cachedContent, CallSettings callSettings = null)

Creates cached content, this call will initialize the cached content in the data storage, and users need to pay for the cache data storage.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource where the cached content will be created  
`cachedContent` | `[CachedContent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CachedContent)`  
Required. The cached content to create  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[CachedContent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CachedContent)` | The RPC response.  
**Example**
    
    
    // Create client
    GenAiCacheServiceClient genAiCacheServiceClient = GenAiCacheServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    CachedContent cachedContent = new CachedContent();
    // Make the request
    CachedContent response = genAiCacheServiceClient.CreateCachedContent(parent, cachedContent);
    

### CreateCachedContentAsync(LocationName, CachedContent, CallSettings)
    
    
    public virtual Task<CachedContent> CreateCachedContentAsync(LocationName parent, CachedContent cachedContent, CallSettings callSettings = null)

Creates cached content, this call will initialize the cached content in the data storage, and users need to pay for the cache data storage.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent resource where the cached content will be created  
`cachedContent` | `[CachedContent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CachedContent)`  
Required. The cached content to create  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CachedContent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CachedContent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    GenAiCacheServiceClient genAiCacheServiceClient = await GenAiCacheServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    CachedContent cachedContent = new CachedContent();
    // Make the request
    CachedContent response = await genAiCacheServiceClient.CreateCachedContentAsync(parent, cachedContent);
    

### CreateCachedContentAsync(LocationName, CachedContent, CancellationToken)
    
    
    public virtual Task<CachedContent> CreateCachedContentAsync(LocationName parent, CachedContent cachedContent, CancellationToken cancellationToken)

Creates cached content, this call will initialize the cached content in the data storage, and users need to pay for the cache data storage.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent resource where the cached content will be created  
`cachedContent` | `[CachedContent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CachedContent)`  
Required. The cached content to create  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CachedContent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CachedContent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    GenAiCacheServiceClient genAiCacheServiceClient = await GenAiCacheServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    CachedContent cachedContent = new CachedContent();
    // Make the request
    CachedContent response = await genAiCacheServiceClient.CreateCachedContentAsync(parent, cachedContent);
    

### CreateCachedContentAsync(CreateCachedContentRequest, CallSettings)
    
    
    public virtual Task<CachedContent> CreateCachedContentAsync(CreateCachedContentRequest request, CallSettings callSettings = null)

Creates cached content, this call will initialize the cached content in the data storage, and users need to pay for the cache data storage.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateCachedContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CreateCachedContentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CachedContent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CachedContent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    GenAiCacheServiceClient genAiCacheServiceClient = await GenAiCacheServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateCachedContentRequest request = new CreateCachedContentRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        CachedContent = new CachedContent(),
    };
    // Make the request
    CachedContent response = await genAiCacheServiceClient.CreateCachedContentAsync(request);
    

### CreateCachedContentAsync(CreateCachedContentRequest, CancellationToken)
    
    
    public virtual Task<CachedContent> CreateCachedContentAsync(CreateCachedContentRequest request, CancellationToken cancellationToken)

Creates cached content, this call will initialize the cached content in the data storage, and users need to pay for the cache data storage.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateCachedContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CreateCachedContentRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CachedContent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CachedContent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    GenAiCacheServiceClient genAiCacheServiceClient = await GenAiCacheServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateCachedContentRequest request = new CreateCachedContentRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        CachedContent = new CachedContent(),
    };
    // Make the request
    CachedContent response = await genAiCacheServiceClient.CreateCachedContentAsync(request);
    

### CreateCachedContentAsync(string, CachedContent, CallSettings)
    
    
    public virtual Task<CachedContent> CreateCachedContentAsync(string parent, CachedContent cachedContent, CallSettings callSettings = null)

Creates cached content, this call will initialize the cached content in the data storage, and users need to pay for the cache data storage.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource where the cached content will be created  
`cachedContent` | `[CachedContent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CachedContent)`  
Required. The cached content to create  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CachedContent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CachedContent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    GenAiCacheServiceClient genAiCacheServiceClient = await GenAiCacheServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    CachedContent cachedContent = new CachedContent();
    // Make the request
    CachedContent response = await genAiCacheServiceClient.CreateCachedContentAsync(parent, cachedContent);
    

### CreateCachedContentAsync(string, CachedContent, CancellationToken)
    
    
    public virtual Task<CachedContent> CreateCachedContentAsync(string parent, CachedContent cachedContent, CancellationToken cancellationToken)

Creates cached content, this call will initialize the cached content in the data storage, and users need to pay for the cache data storage.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource where the cached content will be created  
`cachedContent` | `[CachedContent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CachedContent)`  
Required. The cached content to create  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CachedContent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CachedContent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    GenAiCacheServiceClient genAiCacheServiceClient = await GenAiCacheServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    CachedContent cachedContent = new CachedContent();
    // Make the request
    CachedContent response = await genAiCacheServiceClient.CreateCachedContentAsync(parent, cachedContent);
    

### DeleteCachedContent(CachedContentName, CallSettings)
    
    
    public virtual void DeleteCachedContent(CachedContentName name, CallSettings callSettings = null)

Deletes cached content

**Parameters**  
---  
**Name** | **Description**  
`name` | `[CachedContentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CachedContentName)`  
Required. The resource name referring to the cached content  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    GenAiCacheServiceClient genAiCacheServiceClient = GenAiCacheServiceClient.Create();
    // Initialize request argument(s)
    CachedContentName name = CachedContentName.FromProjectLocationCachedContent("[PROJECT]", "[LOCATION]", "[CACHED_CONTENT]");
    // Make the request
    genAiCacheServiceClient.DeleteCachedContent(name);
    

### DeleteCachedContent(DeleteCachedContentRequest, CallSettings)
    
    
    public virtual void DeleteCachedContent(DeleteCachedContentRequest request, CallSettings callSettings = null)

Deletes cached content

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteCachedContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeleteCachedContentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    GenAiCacheServiceClient genAiCacheServiceClient = GenAiCacheServiceClient.Create();
    // Initialize request argument(s)
    DeleteCachedContentRequest request = new DeleteCachedContentRequest
    {
        CachedContentName = CachedContentName.FromProjectLocationCachedContent("[PROJECT]", "[LOCATION]", "[CACHED_CONTENT]"),
    };
    // Make the request
    genAiCacheServiceClient.DeleteCachedContent(request);
    

### DeleteCachedContent(string, CallSettings)
    
    
    public virtual void DeleteCachedContent(string name, CallSettings callSettings = null)

Deletes cached content

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name referring to the cached content  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    GenAiCacheServiceClient genAiCacheServiceClient = GenAiCacheServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/cachedContents/[CACHED_CONTENT]";
    // Make the request
    genAiCacheServiceClient.DeleteCachedContent(name);
    

### DeleteCachedContentAsync(CachedContentName, CallSettings)
    
    
    public virtual Task DeleteCachedContentAsync(CachedContentName name, CallSettings callSettings = null)

Deletes cached content

**Parameters**  
---  
**Name** | **Description**  
`name` | `[CachedContentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CachedContentName)`  
Required. The resource name referring to the cached content  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    GenAiCacheServiceClient genAiCacheServiceClient = await GenAiCacheServiceClient.CreateAsync();
    // Initialize request argument(s)
    CachedContentName name = CachedContentName.FromProjectLocationCachedContent("[PROJECT]", "[LOCATION]", "[CACHED_CONTENT]");
    // Make the request
    await genAiCacheServiceClient.DeleteCachedContentAsync(name);
    

### DeleteCachedContentAsync(CachedContentName, CancellationToken)
    
    
    public virtual Task DeleteCachedContentAsync(CachedContentName name, CancellationToken cancellationToken)

Deletes cached content

**Parameters**  
---  
**Name** | **Description**  
`name` | `[CachedContentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CachedContentName)`  
Required. The resource name referring to the cached content  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    GenAiCacheServiceClient genAiCacheServiceClient = await GenAiCacheServiceClient.CreateAsync();
    // Initialize request argument(s)
    CachedContentName name = CachedContentName.FromProjectLocationCachedContent("[PROJECT]", "[LOCATION]", "[CACHED_CONTENT]");
    // Make the request
    await genAiCacheServiceClient.DeleteCachedContentAsync(name);
    

### DeleteCachedContentAsync(DeleteCachedContentRequest, CallSettings)
    
    
    public virtual Task DeleteCachedContentAsync(DeleteCachedContentRequest request, CallSettings callSettings = null)

Deletes cached content

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteCachedContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeleteCachedContentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    GenAiCacheServiceClient genAiCacheServiceClient = await GenAiCacheServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteCachedContentRequest request = new DeleteCachedContentRequest
    {
        CachedContentName = CachedContentName.FromProjectLocationCachedContent("[PROJECT]", "[LOCATION]", "[CACHED_CONTENT]"),
    };
    // Make the request
    await genAiCacheServiceClient.DeleteCachedContentAsync(request);
    

### DeleteCachedContentAsync(DeleteCachedContentRequest, CancellationToken)
    
    
    public virtual Task DeleteCachedContentAsync(DeleteCachedContentRequest request, CancellationToken cancellationToken)

Deletes cached content

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteCachedContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeleteCachedContentRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    GenAiCacheServiceClient genAiCacheServiceClient = await GenAiCacheServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteCachedContentRequest request = new DeleteCachedContentRequest
    {
        CachedContentName = CachedContentName.FromProjectLocationCachedContent("[PROJECT]", "[LOCATION]", "[CACHED_CONTENT]"),
    };
    // Make the request
    await genAiCacheServiceClient.DeleteCachedContentAsync(request);
    

### DeleteCachedContentAsync(string, CallSettings)
    
    
    public virtual Task DeleteCachedContentAsync(string name, CallSettings callSettings = null)

Deletes cached content

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name referring to the cached content  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    GenAiCacheServiceClient genAiCacheServiceClient = await GenAiCacheServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/cachedContents/[CACHED_CONTENT]";
    // Make the request
    await genAiCacheServiceClient.DeleteCachedContentAsync(name);
    

### DeleteCachedContentAsync(string, CancellationToken)
    
    
    public virtual Task DeleteCachedContentAsync(string name, CancellationToken cancellationToken)

Deletes cached content

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name referring to the cached content  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    GenAiCacheServiceClient genAiCacheServiceClient = await GenAiCacheServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/cachedContents/[CACHED_CONTENT]";
    // Make the request
    await genAiCacheServiceClient.DeleteCachedContentAsync(name);
    

### GetCachedContent(CachedContentName, CallSettings)
    
    
    public virtual CachedContent GetCachedContent(CachedContentName name, CallSettings callSettings = null)

Gets cached content configurations

**Parameters**  
---  
**Name** | **Description**  
`name` | `[CachedContentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CachedContentName)`  
Required. The resource name referring to the cached content  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[CachedContent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CachedContent)` | The RPC response.  
**Example**
    
    
    // Create client
    GenAiCacheServiceClient genAiCacheServiceClient = GenAiCacheServiceClient.Create();
    // Initialize request argument(s)
    CachedContentName name = CachedContentName.FromProjectLocationCachedContent("[PROJECT]", "[LOCATION]", "[CACHED_CONTENT]");
    // Make the request
    CachedContent response = genAiCacheServiceClient.GetCachedContent(name);
    

### GetCachedContent(GetCachedContentRequest, CallSettings)
    
    
    public virtual CachedContent GetCachedContent(GetCachedContentRequest request, CallSettings callSettings = null)

Gets cached content configurations

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCachedContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GetCachedContentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[CachedContent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CachedContent)` | The RPC response.  
**Example**
    
    
    // Create client
    GenAiCacheServiceClient genAiCacheServiceClient = GenAiCacheServiceClient.Create();
    // Initialize request argument(s)
    GetCachedContentRequest request = new GetCachedContentRequest
    {
        CachedContentName = CachedContentName.FromProjectLocationCachedContent("[PROJECT]", "[LOCATION]", "[CACHED_CONTENT]"),
    };
    // Make the request
    CachedContent response = genAiCacheServiceClient.GetCachedContent(request);
    

### GetCachedContent(string, CallSettings)
    
    
    public virtual CachedContent GetCachedContent(string name, CallSettings callSettings = null)

Gets cached content configurations

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name referring to the cached content  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[CachedContent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CachedContent)` | The RPC response.  
**Example**
    
    
    // Create client
    GenAiCacheServiceClient genAiCacheServiceClient = GenAiCacheServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/cachedContents/[CACHED_CONTENT]";
    // Make the request
    CachedContent response = genAiCacheServiceClient.GetCachedContent(name);
    

### GetCachedContentAsync(CachedContentName, CallSettings)
    
    
    public virtual Task<CachedContent> GetCachedContentAsync(CachedContentName name, CallSettings callSettings = null)

Gets cached content configurations

**Parameters**  
---  
**Name** | **Description**  
`name` | `[CachedContentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CachedContentName)`  
Required. The resource name referring to the cached content  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CachedContent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CachedContent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    GenAiCacheServiceClient genAiCacheServiceClient = await GenAiCacheServiceClient.CreateAsync();
    // Initialize request argument(s)
    CachedContentName name = CachedContentName.FromProjectLocationCachedContent("[PROJECT]", "[LOCATION]", "[CACHED_CONTENT]");
    // Make the request
    CachedContent response = await genAiCacheServiceClient.GetCachedContentAsync(name);
    

### GetCachedContentAsync(CachedContentName, CancellationToken)
    
    
    public virtual Task<CachedContent> GetCachedContentAsync(CachedContentName name, CancellationToken cancellationToken)

Gets cached content configurations

**Parameters**  
---  
**Name** | **Description**  
`name` | `[CachedContentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CachedContentName)`  
Required. The resource name referring to the cached content  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CachedContent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CachedContent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    GenAiCacheServiceClient genAiCacheServiceClient = await GenAiCacheServiceClient.CreateAsync();
    // Initialize request argument(s)
    CachedContentName name = CachedContentName.FromProjectLocationCachedContent("[PROJECT]", "[LOCATION]", "[CACHED_CONTENT]");
    // Make the request
    CachedContent response = await genAiCacheServiceClient.GetCachedContentAsync(name);
    

### GetCachedContentAsync(GetCachedContentRequest, CallSettings)
    
    
    public virtual Task<CachedContent> GetCachedContentAsync(GetCachedContentRequest request, CallSettings callSettings = null)

Gets cached content configurations

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCachedContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GetCachedContentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CachedContent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CachedContent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    GenAiCacheServiceClient genAiCacheServiceClient = await GenAiCacheServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetCachedContentRequest request = new GetCachedContentRequest
    {
        CachedContentName = CachedContentName.FromProjectLocationCachedContent("[PROJECT]", "[LOCATION]", "[CACHED_CONTENT]"),
    };
    // Make the request
    CachedContent response = await genAiCacheServiceClient.GetCachedContentAsync(request);
    

### GetCachedContentAsync(GetCachedContentRequest, CancellationToken)
    
    
    public virtual Task<CachedContent> GetCachedContentAsync(GetCachedContentRequest request, CancellationToken cancellationToken)

Gets cached content configurations

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCachedContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GetCachedContentRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CachedContent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CachedContent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    GenAiCacheServiceClient genAiCacheServiceClient = await GenAiCacheServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetCachedContentRequest request = new GetCachedContentRequest
    {
        CachedContentName = CachedContentName.FromProjectLocationCachedContent("[PROJECT]", "[LOCATION]", "[CACHED_CONTENT]"),
    };
    // Make the request
    CachedContent response = await genAiCacheServiceClient.GetCachedContentAsync(request);
    

### GetCachedContentAsync(string, CallSettings)
    
    
    public virtual Task<CachedContent> GetCachedContentAsync(string name, CallSettings callSettings = null)

Gets cached content configurations

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name referring to the cached content  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CachedContent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CachedContent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    GenAiCacheServiceClient genAiCacheServiceClient = await GenAiCacheServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/cachedContents/[CACHED_CONTENT]";
    // Make the request
    CachedContent response = await genAiCacheServiceClient.GetCachedContentAsync(name);
    

### GetCachedContentAsync(string, CancellationToken)
    
    
    public virtual Task<CachedContent> GetCachedContentAsync(string name, CancellationToken cancellationToken)

Gets cached content configurations

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name referring to the cached content  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CachedContent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CachedContent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    GenAiCacheServiceClient genAiCacheServiceClient = await GenAiCacheServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/cachedContents/[CACHED_CONTENT]";
    // Make the request
    CachedContent response = await genAiCacheServiceClient.GetCachedContentAsync(name);
    

### ListCachedContents(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListCachedContentsResponse, CachedContent> ListCachedContents(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists cached contents in a project

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent, which owns this collection of cached contents.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListCachedContentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ListCachedContentsResponse)[CachedContent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CachedContent)` | A pageable sequence of [CachedContent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CachedContent) resources.  
**Example**
    
    
    // Create client
    GenAiCacheServiceClient genAiCacheServiceClient = GenAiCacheServiceClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListCachedContentsResponse, CachedContent> response = genAiCacheServiceClient.ListCachedContents(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (CachedContent item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListCachedContentsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (CachedContent item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<CachedContent> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (CachedContent item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListCachedContents(ListCachedContentsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListCachedContentsResponse, CachedContent> ListCachedContents(ListCachedContentsRequest request, CallSettings callSettings = null)

Lists cached contents in a project

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListCachedContentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ListCachedContentsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListCachedContentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ListCachedContentsResponse)[CachedContent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CachedContent)` | A pageable sequence of [CachedContent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CachedContent) resources.  
**Example**
    
    
    // Create client
    GenAiCacheServiceClient genAiCacheServiceClient = GenAiCacheServiceClient.Create();
    // Initialize request argument(s)
    ListCachedContentsRequest request = new ListCachedContentsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    PagedEnumerable<ListCachedContentsResponse, CachedContent> response = genAiCacheServiceClient.ListCachedContents(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (CachedContent item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListCachedContentsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (CachedContent item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<CachedContent> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (CachedContent item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListCachedContents(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListCachedContentsResponse, CachedContent> ListCachedContents(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists cached contents in a project

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent, which owns this collection of cached contents.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListCachedContentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ListCachedContentsResponse)[CachedContent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CachedContent)` | A pageable sequence of [CachedContent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CachedContent) resources.  
**Example**
    
    
    // Create client
    GenAiCacheServiceClient genAiCacheServiceClient = GenAiCacheServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListCachedContentsResponse, CachedContent> response = genAiCacheServiceClient.ListCachedContents(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (CachedContent item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListCachedContentsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (CachedContent item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<CachedContent> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (CachedContent item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListCachedContentsAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListCachedContentsResponse, CachedContent> ListCachedContentsAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists cached contents in a project

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent, which owns this collection of cached contents.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListCachedContentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ListCachedContentsResponse)[CachedContent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CachedContent)` | A pageable asynchronous sequence of [CachedContent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CachedContent) resources.  
**Example**
    
    
    // Create client
    GenAiCacheServiceClient genAiCacheServiceClient = await GenAiCacheServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListCachedContentsResponse, CachedContent> response = genAiCacheServiceClient.ListCachedContentsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (CachedContent item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListCachedContentsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (CachedContent item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<CachedContent> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (CachedContent item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListCachedContentsAsync(ListCachedContentsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListCachedContentsResponse, CachedContent> ListCachedContentsAsync(ListCachedContentsRequest request, CallSettings callSettings = null)

Lists cached contents in a project

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListCachedContentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ListCachedContentsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListCachedContentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ListCachedContentsResponse)[CachedContent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CachedContent)` | A pageable asynchronous sequence of [CachedContent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CachedContent) resources.  
**Example**
    
    
    // Create client
    GenAiCacheServiceClient genAiCacheServiceClient = await GenAiCacheServiceClient.CreateAsync();
    // Initialize request argument(s)
    ListCachedContentsRequest request = new ListCachedContentsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    PagedAsyncEnumerable<ListCachedContentsResponse, CachedContent> response = genAiCacheServiceClient.ListCachedContentsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (CachedContent item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListCachedContentsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (CachedContent item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<CachedContent> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (CachedContent item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListCachedContentsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListCachedContentsResponse, CachedContent> ListCachedContentsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists cached contents in a project

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent, which owns this collection of cached contents.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListCachedContentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ListCachedContentsResponse)[CachedContent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CachedContent)` | A pageable asynchronous sequence of [CachedContent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CachedContent) resources.  
**Example**
    
    
    // Create client
    GenAiCacheServiceClient genAiCacheServiceClient = await GenAiCacheServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListCachedContentsResponse, CachedContent> response = genAiCacheServiceClient.ListCachedContentsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (CachedContent item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListCachedContentsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (CachedContent item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<CachedContent> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (CachedContent item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GenAiCacheServiceClient#Google_Cloud_AIPlatform_V1_GenAiCacheServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GenAiCacheServiceClient#Google_Cloud_AIPlatform_V1_GenAiCacheServiceClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GenAiCacheServiceClient#Google_Cloud_AIPlatform_V1_GenAiCacheServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GenAiCacheServiceClient#Google_Cloud_AIPlatform_V1_GenAiCacheServiceClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### UpdateCachedContent(CachedContent, FieldMask, CallSettings)
    
    
    public virtual CachedContent UpdateCachedContent(CachedContent cachedContent, FieldMask updateMask, CallSettings callSettings = null)

Updates cached content configurations

**Parameters**  
---  
**Name** | **Description**  
`cachedContent` | `[CachedContent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CachedContent)`  
Required. The cached content to update  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. The list of fields to update.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[CachedContent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CachedContent)` | The RPC response.  
**Example**
    
    
    // Create client
    GenAiCacheServiceClient genAiCacheServiceClient = GenAiCacheServiceClient.Create();
    // Initialize request argument(s)
    CachedContent cachedContent = new CachedContent();
    FieldMask updateMask = new FieldMask();
    // Make the request
    CachedContent response = genAiCacheServiceClient.UpdateCachedContent(cachedContent, updateMask);
    

### UpdateCachedContent(UpdateCachedContentRequest, CallSettings)
    
    
    public virtual CachedContent UpdateCachedContent(UpdateCachedContentRequest request, CallSettings callSettings = null)

Updates cached content configurations

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateCachedContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.UpdateCachedContentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[CachedContent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CachedContent)` | The RPC response.  
**Example**
    
    
    // Create client
    GenAiCacheServiceClient genAiCacheServiceClient = GenAiCacheServiceClient.Create();
    // Initialize request argument(s)
    UpdateCachedContentRequest request = new UpdateCachedContentRequest
    {
        CachedContent = new CachedContent(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    CachedContent response = genAiCacheServiceClient.UpdateCachedContent(request);
    

### UpdateCachedContentAsync(CachedContent, FieldMask, CallSettings)
    
    
    public virtual Task<CachedContent> UpdateCachedContentAsync(CachedContent cachedContent, FieldMask updateMask, CallSettings callSettings = null)

Updates cached content configurations

**Parameters**  
---  
**Name** | **Description**  
`cachedContent` | `[CachedContent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CachedContent)`  
Required. The cached content to update  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. The list of fields to update.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CachedContent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CachedContent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    GenAiCacheServiceClient genAiCacheServiceClient = await GenAiCacheServiceClient.CreateAsync();
    // Initialize request argument(s)
    CachedContent cachedContent = new CachedContent();
    FieldMask updateMask = new FieldMask();
    // Make the request
    CachedContent response = await genAiCacheServiceClient.UpdateCachedContentAsync(cachedContent, updateMask);
    

### UpdateCachedContentAsync(CachedContent, FieldMask, CancellationToken)
    
    
    public virtual Task<CachedContent> UpdateCachedContentAsync(CachedContent cachedContent, FieldMask updateMask, CancellationToken cancellationToken)

Updates cached content configurations

**Parameters**  
---  
**Name** | **Description**  
`cachedContent` | `[CachedContent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CachedContent)`  
Required. The cached content to update  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. The list of fields to update.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CachedContent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CachedContent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    GenAiCacheServiceClient genAiCacheServiceClient = await GenAiCacheServiceClient.CreateAsync();
    // Initialize request argument(s)
    CachedContent cachedContent = new CachedContent();
    FieldMask updateMask = new FieldMask();
    // Make the request
    CachedContent response = await genAiCacheServiceClient.UpdateCachedContentAsync(cachedContent, updateMask);
    

### UpdateCachedContentAsync(UpdateCachedContentRequest, CallSettings)
    
    
    public virtual Task<CachedContent> UpdateCachedContentAsync(UpdateCachedContentRequest request, CallSettings callSettings = null)

Updates cached content configurations

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateCachedContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.UpdateCachedContentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CachedContent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CachedContent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    GenAiCacheServiceClient genAiCacheServiceClient = await GenAiCacheServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateCachedContentRequest request = new UpdateCachedContentRequest
    {
        CachedContent = new CachedContent(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    CachedContent response = await genAiCacheServiceClient.UpdateCachedContentAsync(request);
    

### UpdateCachedContentAsync(UpdateCachedContentRequest, CancellationToken)
    
    
    public virtual Task<CachedContent> UpdateCachedContentAsync(UpdateCachedContentRequest request, CancellationToken cancellationToken)

Updates cached content configurations

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateCachedContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.UpdateCachedContentRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CachedContent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CachedContent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    GenAiCacheServiceClient genAiCacheServiceClient = await GenAiCacheServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateCachedContentRequest request = new UpdateCachedContentRequest
    {
        CachedContent = new CachedContent(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    CachedContent response = await genAiCacheServiceClient.UpdateCachedContentAsync(request);
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
