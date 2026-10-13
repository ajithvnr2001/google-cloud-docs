---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationFinderClient
title: Cloud Location Finder v1 API - Class CloudLocationFinderClient (1.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:55.251686+00:00
---

# Cloud Location Finder v1 API - Class CloudLocationFinderClient (1.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationFinderClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Location Finder v1 API - Class CloudLocationFinderClient (1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  1.0.0-beta02 
    
    
    public abstract class CloudLocationFinderClient

Reference documentation and code samples for the Cloud Location Finder v1 API class CloudLocationFinderClient.

CloudLocationFinder client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CloudLocationFinderClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[CloudLocationFinderClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationFinderClientImpl)

## Namespace

[Google.Cloud.LocationFinder.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1)

## Assembly

Google.Cloud.LocationFinder.V1.dll

## Remarks

Service describing handlers for resources

## Properties 

### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the CloudLocationFinder service, which is a host of "cloudlocationfinder.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default CloudLocationFinder scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default CloudLocationFinder scopes are:

  * <https://www.googleapis.com/auth/cloud-platform>



### GrpcClient
    
    
    public virtual CloudLocationFinder.CloudLocationFinderClient GrpcClient { get; }

The underlying gRPC CloudLocationFinder client

**Property Value**  
---  
**Type** | **Description**  
`[CloudLocationFinder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationFinder)[CloudLocationFinderClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationFinder.CloudLocationFinderClient)` |   
  
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
    
    
    public static CloudLocationFinderClient Create()

Synchronously creates a [CloudLocationFinderClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationFinderClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [CloudLocationFinderClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationFinderClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[CloudLocationFinderClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationFinderClient)` | The created [CloudLocationFinderClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationFinderClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<CloudLocationFinderClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [CloudLocationFinderClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationFinderClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [CloudLocationFinderClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationFinderClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CloudLocationFinderClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationFinderClient)` | The task representing the created [CloudLocationFinderClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationFinderClient).  
  
### GetCloudLocation(CloudLocationName, CallSettings)
    
    
    public virtual CloudLocation GetCloudLocation(CloudLocationName name, CallSettings callSettings = null)

Retrieves a resource containing information about a cloud location.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[CloudLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationName)`  
Required. Name of the resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[CloudLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocation)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudLocationFinderClient cloudLocationFinderClient = CloudLocationFinderClient.Create();
    // Initialize request argument(s)
    CloudLocationName name = CloudLocationName.FromProjectLocationCloudLocation("[PROJECT]", "[LOCATION]", "[CLOUD_LOCATION]");
    // Make the request
    CloudLocation response = cloudLocationFinderClient.GetCloudLocation(name);
    

### GetCloudLocation(GetCloudLocationRequest, CallSettings)
    
    
    public virtual CloudLocation GetCloudLocation(GetCloudLocationRequest request, CallSettings callSettings = null)

Retrieves a resource containing information about a cloud location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCloudLocationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.GetCloudLocationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[CloudLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocation)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudLocationFinderClient cloudLocationFinderClient = CloudLocationFinderClient.Create();
    // Initialize request argument(s)
    GetCloudLocationRequest request = new GetCloudLocationRequest
    {
        CloudLocationName = CloudLocationName.FromProjectLocationCloudLocation("[PROJECT]", "[LOCATION]", "[CLOUD_LOCATION]"),
    };
    // Make the request
    CloudLocation response = cloudLocationFinderClient.GetCloudLocation(request);
    

### GetCloudLocation(string, CallSettings)
    
    
    public virtual CloudLocation GetCloudLocation(string name, CallSettings callSettings = null)

Retrieves a resource containing information about a cloud location.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[CloudLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocation)` | The RPC response.  
**Example**
    
    
    // Create client
    CloudLocationFinderClient cloudLocationFinderClient = CloudLocationFinderClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/cloudLocations/[CLOUD_LOCATION]";
    // Make the request
    CloudLocation response = cloudLocationFinderClient.GetCloudLocation(name);
    

### GetCloudLocationAsync(CloudLocationName, CallSettings)
    
    
    public virtual Task<CloudLocation> GetCloudLocationAsync(CloudLocationName name, CallSettings callSettings = null)

Retrieves a resource containing information about a cloud location.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[CloudLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationName)`  
Required. Name of the resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CloudLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudLocationFinderClient cloudLocationFinderClient = await CloudLocationFinderClient.CreateAsync();
    // Initialize request argument(s)
    CloudLocationName name = CloudLocationName.FromProjectLocationCloudLocation("[PROJECT]", "[LOCATION]", "[CLOUD_LOCATION]");
    // Make the request
    CloudLocation response = await cloudLocationFinderClient.GetCloudLocationAsync(name);
    

### GetCloudLocationAsync(CloudLocationName, CancellationToken)
    
    
    public virtual Task<CloudLocation> GetCloudLocationAsync(CloudLocationName name, CancellationToken cancellationToken)

Retrieves a resource containing information about a cloud location.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[CloudLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationName)`  
Required. Name of the resource.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CloudLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudLocationFinderClient cloudLocationFinderClient = await CloudLocationFinderClient.CreateAsync();
    // Initialize request argument(s)
    CloudLocationName name = CloudLocationName.FromProjectLocationCloudLocation("[PROJECT]", "[LOCATION]", "[CLOUD_LOCATION]");
    // Make the request
    CloudLocation response = await cloudLocationFinderClient.GetCloudLocationAsync(name);
    

### GetCloudLocationAsync(GetCloudLocationRequest, CallSettings)
    
    
    public virtual Task<CloudLocation> GetCloudLocationAsync(GetCloudLocationRequest request, CallSettings callSettings = null)

Retrieves a resource containing information about a cloud location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCloudLocationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.GetCloudLocationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CloudLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudLocationFinderClient cloudLocationFinderClient = await CloudLocationFinderClient.CreateAsync();
    // Initialize request argument(s)
    GetCloudLocationRequest request = new GetCloudLocationRequest
    {
        CloudLocationName = CloudLocationName.FromProjectLocationCloudLocation("[PROJECT]", "[LOCATION]", "[CLOUD_LOCATION]"),
    };
    // Make the request
    CloudLocation response = await cloudLocationFinderClient.GetCloudLocationAsync(request);
    

### GetCloudLocationAsync(GetCloudLocationRequest, CancellationToken)
    
    
    public virtual Task<CloudLocation> GetCloudLocationAsync(GetCloudLocationRequest request, CancellationToken cancellationToken)

Retrieves a resource containing information about a cloud location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCloudLocationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.GetCloudLocationRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CloudLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudLocationFinderClient cloudLocationFinderClient = await CloudLocationFinderClient.CreateAsync();
    // Initialize request argument(s)
    GetCloudLocationRequest request = new GetCloudLocationRequest
    {
        CloudLocationName = CloudLocationName.FromProjectLocationCloudLocation("[PROJECT]", "[LOCATION]", "[CLOUD_LOCATION]"),
    };
    // Make the request
    CloudLocation response = await cloudLocationFinderClient.GetCloudLocationAsync(request);
    

### GetCloudLocationAsync(string, CallSettings)
    
    
    public virtual Task<CloudLocation> GetCloudLocationAsync(string name, CallSettings callSettings = null)

Retrieves a resource containing information about a cloud location.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CloudLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudLocationFinderClient cloudLocationFinderClient = await CloudLocationFinderClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/cloudLocations/[CLOUD_LOCATION]";
    // Make the request
    CloudLocation response = await cloudLocationFinderClient.GetCloudLocationAsync(name);
    

### GetCloudLocationAsync(string, CancellationToken)
    
    
    public virtual Task<CloudLocation> GetCloudLocationAsync(string name, CancellationToken cancellationToken)

Retrieves a resource containing information about a cloud location.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the resource.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CloudLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    CloudLocationFinderClient cloudLocationFinderClient = await CloudLocationFinderClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/cloudLocations/[CLOUD_LOCATION]";
    // Make the request
    CloudLocation response = await cloudLocationFinderClient.GetCloudLocationAsync(name);
    

### ListCloudLocations(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListCloudLocationsResponse, CloudLocation> ListCloudLocations(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists cloud locations under a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent, which owns this collection of cloud locations. Format: projects/{project}/locations/{location}  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListCloudLocationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.ListCloudLocationsResponse)[CloudLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocation)` | A pageable sequence of [CloudLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocation) resources.  
**Example**
    
    
    // Create client
    CloudLocationFinderClient cloudLocationFinderClient = CloudLocationFinderClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListCloudLocationsResponse, CloudLocation> response = cloudLocationFinderClient.ListCloudLocations(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (CloudLocation item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListCloudLocationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (CloudLocation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<CloudLocation> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (CloudLocation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListCloudLocations(ListCloudLocationsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListCloudLocationsResponse, CloudLocation> ListCloudLocations(ListCloudLocationsRequest request, CallSettings callSettings = null)

Lists cloud locations under a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListCloudLocationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.ListCloudLocationsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListCloudLocationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.ListCloudLocationsResponse)[CloudLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocation)` | A pageable sequence of [CloudLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocation) resources.  
**Example**
    
    
    // Create client
    CloudLocationFinderClient cloudLocationFinderClient = CloudLocationFinderClient.Create();
    // Initialize request argument(s)
    ListCloudLocationsRequest request = new ListCloudLocationsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
    };
    // Make the request
    PagedEnumerable<ListCloudLocationsResponse, CloudLocation> response = cloudLocationFinderClient.ListCloudLocations(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (CloudLocation item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListCloudLocationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (CloudLocation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<CloudLocation> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (CloudLocation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListCloudLocations(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListCloudLocationsResponse, CloudLocation> ListCloudLocations(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists cloud locations under a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent, which owns this collection of cloud locations. Format: projects/{project}/locations/{location}  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListCloudLocationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.ListCloudLocationsResponse)[CloudLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocation)` | A pageable sequence of [CloudLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocation) resources.  
**Example**
    
    
    // Create client
    CloudLocationFinderClient cloudLocationFinderClient = CloudLocationFinderClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListCloudLocationsResponse, CloudLocation> response = cloudLocationFinderClient.ListCloudLocations(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (CloudLocation item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListCloudLocationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (CloudLocation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<CloudLocation> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (CloudLocation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListCloudLocationsAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListCloudLocationsResponse, CloudLocation> ListCloudLocationsAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists cloud locations under a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent, which owns this collection of cloud locations. Format: projects/{project}/locations/{location}  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListCloudLocationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.ListCloudLocationsResponse)[CloudLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocation)` | A pageable asynchronous sequence of [CloudLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocation) resources.  
**Example**
    
    
    // Create client
    CloudLocationFinderClient cloudLocationFinderClient = await CloudLocationFinderClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListCloudLocationsResponse, CloudLocation> response = cloudLocationFinderClient.ListCloudLocationsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (CloudLocation item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListCloudLocationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (CloudLocation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<CloudLocation> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (CloudLocation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListCloudLocationsAsync(ListCloudLocationsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListCloudLocationsResponse, CloudLocation> ListCloudLocationsAsync(ListCloudLocationsRequest request, CallSettings callSettings = null)

Lists cloud locations under a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListCloudLocationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.ListCloudLocationsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListCloudLocationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.ListCloudLocationsResponse)[CloudLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocation)` | A pageable asynchronous sequence of [CloudLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocation) resources.  
**Example**
    
    
    // Create client
    CloudLocationFinderClient cloudLocationFinderClient = await CloudLocationFinderClient.CreateAsync();
    // Initialize request argument(s)
    ListCloudLocationsRequest request = new ListCloudLocationsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListCloudLocationsResponse, CloudLocation> response = cloudLocationFinderClient.ListCloudLocationsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (CloudLocation item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListCloudLocationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (CloudLocation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<CloudLocation> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (CloudLocation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListCloudLocationsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListCloudLocationsResponse, CloudLocation> ListCloudLocationsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists cloud locations under a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent, which owns this collection of cloud locations. Format: projects/{project}/locations/{location}  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListCloudLocationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.ListCloudLocationsResponse)[CloudLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocation)` | A pageable asynchronous sequence of [CloudLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocation) resources.  
**Example**
    
    
    // Create client
    CloudLocationFinderClient cloudLocationFinderClient = await CloudLocationFinderClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListCloudLocationsResponse, CloudLocation> response = cloudLocationFinderClient.ListCloudLocationsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (CloudLocation item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListCloudLocationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (CloudLocation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<CloudLocation> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (CloudLocation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### SearchCloudLocations(LocationName, CloudLocationName, string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<SearchCloudLocationsResponse, CloudLocation> SearchCloudLocations(LocationName parent, CloudLocationName sourceCloudLocation, string query, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Searches for cloud locations from a given source location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent, which owns this collection of cloud locations. Format: projects/{project}/locations/{location}  
`sourceCloudLocation` | `[CloudLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationName)`  
Required. The source cloud location to search from. Example search can be searching nearby cloud locations from the source cloud location by latency.  
`query` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The query string in search query syntax. While filter is used to filter the search results by attributes, query is used to specify the search requirements.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[SearchCloudLocationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.SearchCloudLocationsResponse)[CloudLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocation)` | A pageable sequence of [CloudLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocation) resources.  
**Example**
    
    
    // Create client
    CloudLocationFinderClient cloudLocationFinderClient = CloudLocationFinderClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    CloudLocationName sourceCloudLocation = CloudLocationName.FromProjectLocationCloudLocation("[PROJECT]", "[LOCATION]", "[CLOUD_LOCATION]");
    string query = "";
    // Make the request
    PagedEnumerable<SearchCloudLocationsResponse, CloudLocation> response = cloudLocationFinderClient.SearchCloudLocations(parent, sourceCloudLocation, query);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (CloudLocation item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (SearchCloudLocationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (CloudLocation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<CloudLocation> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (CloudLocation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### SearchCloudLocations(SearchCloudLocationsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<SearchCloudLocationsResponse, CloudLocation> SearchCloudLocations(SearchCloudLocationsRequest request, CallSettings callSettings = null)

Searches for cloud locations from a given source location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchCloudLocationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.SearchCloudLocationsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[SearchCloudLocationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.SearchCloudLocationsResponse)[CloudLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocation)` | A pageable sequence of [CloudLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocation) resources.  
**Example**
    
    
    // Create client
    CloudLocationFinderClient cloudLocationFinderClient = CloudLocationFinderClient.Create();
    // Initialize request argument(s)
    SearchCloudLocationsRequest request = new SearchCloudLocationsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        SourceCloudLocationAsCloudLocationName = CloudLocationName.FromProjectLocationCloudLocation("[PROJECT]", "[LOCATION]", "[CLOUD_LOCATION]"),
        Query = "",
    };
    // Make the request
    PagedEnumerable<SearchCloudLocationsResponse, CloudLocation> response = cloudLocationFinderClient.SearchCloudLocations(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (CloudLocation item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (SearchCloudLocationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (CloudLocation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<CloudLocation> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (CloudLocation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### SearchCloudLocations(string, string, string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<SearchCloudLocationsResponse, CloudLocation> SearchCloudLocations(string parent, string sourceCloudLocation, string query, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Searches for cloud locations from a given source location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent, which owns this collection of cloud locations. Format: projects/{project}/locations/{location}  
`sourceCloudLocation` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The source cloud location to search from. Example search can be searching nearby cloud locations from the source cloud location by latency.  
`query` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The query string in search query syntax. While filter is used to filter the search results by attributes, query is used to specify the search requirements.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[SearchCloudLocationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.SearchCloudLocationsResponse)[CloudLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocation)` | A pageable sequence of [CloudLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocation) resources.  
**Example**
    
    
    // Create client
    CloudLocationFinderClient cloudLocationFinderClient = CloudLocationFinderClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    string sourceCloudLocation = "projects/[PROJECT]/locations/[LOCATION]/cloudLocations/[CLOUD_LOCATION]";
    string query = "";
    // Make the request
    PagedEnumerable<SearchCloudLocationsResponse, CloudLocation> response = cloudLocationFinderClient.SearchCloudLocations(parent, sourceCloudLocation, query);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (CloudLocation item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (SearchCloudLocationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (CloudLocation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<CloudLocation> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (CloudLocation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### SearchCloudLocationsAsync(LocationName, CloudLocationName, string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<SearchCloudLocationsResponse, CloudLocation> SearchCloudLocationsAsync(LocationName parent, CloudLocationName sourceCloudLocation, string query, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Searches for cloud locations from a given source location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent, which owns this collection of cloud locations. Format: projects/{project}/locations/{location}  
`sourceCloudLocation` | `[CloudLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationName)`  
Required. The source cloud location to search from. Example search can be searching nearby cloud locations from the source cloud location by latency.  
`query` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The query string in search query syntax. While filter is used to filter the search results by attributes, query is used to specify the search requirements.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[SearchCloudLocationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.SearchCloudLocationsResponse)[CloudLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocation)` | A pageable asynchronous sequence of [CloudLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocation) resources.  
**Example**
    
    
    // Create client
    CloudLocationFinderClient cloudLocationFinderClient = await CloudLocationFinderClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    CloudLocationName sourceCloudLocation = CloudLocationName.FromProjectLocationCloudLocation("[PROJECT]", "[LOCATION]", "[CLOUD_LOCATION]");
    string query = "";
    // Make the request
    PagedAsyncEnumerable<SearchCloudLocationsResponse, CloudLocation> response = cloudLocationFinderClient.SearchCloudLocationsAsync(parent, sourceCloudLocation, query);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (CloudLocation item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (SearchCloudLocationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (CloudLocation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<CloudLocation> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (CloudLocation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### SearchCloudLocationsAsync(SearchCloudLocationsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<SearchCloudLocationsResponse, CloudLocation> SearchCloudLocationsAsync(SearchCloudLocationsRequest request, CallSettings callSettings = null)

Searches for cloud locations from a given source location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchCloudLocationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.SearchCloudLocationsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[SearchCloudLocationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.SearchCloudLocationsResponse)[CloudLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocation)` | A pageable asynchronous sequence of [CloudLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocation) resources.  
**Example**
    
    
    // Create client
    CloudLocationFinderClient cloudLocationFinderClient = await CloudLocationFinderClient.CreateAsync();
    // Initialize request argument(s)
    SearchCloudLocationsRequest request = new SearchCloudLocationsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        SourceCloudLocationAsCloudLocationName = CloudLocationName.FromProjectLocationCloudLocation("[PROJECT]", "[LOCATION]", "[CLOUD_LOCATION]"),
        Query = "",
    };
    // Make the request
    PagedAsyncEnumerable<SearchCloudLocationsResponse, CloudLocation> response = cloudLocationFinderClient.SearchCloudLocationsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (CloudLocation item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (SearchCloudLocationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (CloudLocation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<CloudLocation> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (CloudLocation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### SearchCloudLocationsAsync(string, string, string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<SearchCloudLocationsResponse, CloudLocation> SearchCloudLocationsAsync(string parent, string sourceCloudLocation, string query, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Searches for cloud locations from a given source location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent, which owns this collection of cloud locations. Format: projects/{project}/locations/{location}  
`sourceCloudLocation` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The source cloud location to search from. Example search can be searching nearby cloud locations from the source cloud location by latency.  
`query` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The query string in search query syntax. While filter is used to filter the search results by attributes, query is used to specify the search requirements.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[SearchCloudLocationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.SearchCloudLocationsResponse)[CloudLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocation)` | A pageable asynchronous sequence of [CloudLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocation) resources.  
**Example**
    
    
    // Create client
    CloudLocationFinderClient cloudLocationFinderClient = await CloudLocationFinderClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    string sourceCloudLocation = "projects/[PROJECT]/locations/[LOCATION]/cloudLocations/[CLOUD_LOCATION]";
    string query = "";
    // Make the request
    PagedAsyncEnumerable<SearchCloudLocationsResponse, CloudLocation> response = cloudLocationFinderClient.SearchCloudLocationsAsync(parent, sourceCloudLocation, query);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (CloudLocation item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (SearchCloudLocationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (CloudLocation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<CloudLocation> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (CloudLocation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationFinderClient#Google_Cloud_LocationFinder_V1_CloudLocationFinderClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationFinderClient#Google_Cloud_LocationFinder_V1_CloudLocationFinderClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationFinderClient#Google_Cloud_LocationFinder_V1_CloudLocationFinderClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationFinderClient#Google_Cloud_LocationFinder_V1_CloudLocationFinderClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
