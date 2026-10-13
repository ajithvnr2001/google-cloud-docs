---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.MaintenanceClient
title: Maintenance v1 API - Class MaintenanceClient (1.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:54:14.648928+00:00
---

# Maintenance v1 API - Class MaintenanceClient (1.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.MaintenanceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Maintenance v1 API - Class MaintenanceClient (1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  1.0.0-beta01 
    
    
    public abstract class MaintenanceClient

Reference documentation and code samples for the Maintenance v1 API class MaintenanceClient.

Maintenance client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > MaintenanceClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[MaintenanceClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.MaintenanceClientImpl)

## Namespace

[Google.Cloud.Maintenance.Api.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1)

## Assembly

Google.Cloud.Maintenance.Api.V1.dll

## Remarks

Unified Maintenance service

## Properties 

### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the Maintenance service, which is a host of "maintenance.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default Maintenance scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default Maintenance scopes are:

  * <https://www.googleapis.com/auth/cloud-platform>



### GrpcClient
    
    
    public virtual Maintenance.MaintenanceClient GrpcClient { get; }

The underlying gRPC Maintenance client

**Property Value**  
---  
**Type** | **Description**  
`[Maintenance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.Maintenance)[MaintenanceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.Maintenance.MaintenanceClient)` |   
  
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
    
    
    public static MaintenanceClient Create()

Synchronously creates a [MaintenanceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.MaintenanceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [MaintenanceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.MaintenanceClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[MaintenanceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.MaintenanceClient)` | The created [MaintenanceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.MaintenanceClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<MaintenanceClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [MaintenanceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.MaintenanceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [MaintenanceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.MaintenanceClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[MaintenanceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.MaintenanceClient)` | The task representing the created [MaintenanceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.MaintenanceClient).  
  
### GetResourceMaintenance(GetResourceMaintenanceRequest, CallSettings)
    
    
    public virtual ResourceMaintenance GetResourceMaintenance(GetResourceMaintenanceRequest request, CallSettings callSettings = null)

Retrieve a single resource maintenance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetResourceMaintenanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.GetResourceMaintenanceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ResourceMaintenance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.ResourceMaintenance)` | The RPC response.  
**Example**
    
    
    // Create client
    MaintenanceClient maintenanceClient = MaintenanceClient.Create();
    // Initialize request argument(s)
    GetResourceMaintenanceRequest request = new GetResourceMaintenanceRequest
    {
        ResourceMaintenanceName = ResourceMaintenanceName.FromProjectLocationResourceMaintenance("[PROJECT]", "[LOCATION]", "[RESOURCE_MAINTENANCE]"),
    };
    // Make the request
    ResourceMaintenance response = maintenanceClient.GetResourceMaintenance(request);
    

### GetResourceMaintenance(ResourceMaintenanceName, CallSettings)
    
    
    public virtual ResourceMaintenance GetResourceMaintenance(ResourceMaintenanceName name, CallSettings callSettings = null)

Retrieve a single resource maintenance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ResourceMaintenanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.ResourceMaintenanceName)`  
Required. The resource name of the resource within a service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ResourceMaintenance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.ResourceMaintenance)` | The RPC response.  
**Example**
    
    
    // Create client
    MaintenanceClient maintenanceClient = MaintenanceClient.Create();
    // Initialize request argument(s)
    ResourceMaintenanceName name = ResourceMaintenanceName.FromProjectLocationResourceMaintenance("[PROJECT]", "[LOCATION]", "[RESOURCE_MAINTENANCE]");
    // Make the request
    ResourceMaintenance response = maintenanceClient.GetResourceMaintenance(name);
    

### GetResourceMaintenance(string, CallSettings)
    
    
    public virtual ResourceMaintenance GetResourceMaintenance(string name, CallSettings callSettings = null)

Retrieve a single resource maintenance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the resource within a service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ResourceMaintenance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.ResourceMaintenance)` | The RPC response.  
**Example**
    
    
    // Create client
    MaintenanceClient maintenanceClient = MaintenanceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/resourceMaintenances/[RESOURCE_MAINTENANCE]";
    // Make the request
    ResourceMaintenance response = maintenanceClient.GetResourceMaintenance(name);
    

### GetResourceMaintenanceAsync(GetResourceMaintenanceRequest, CallSettings)
    
    
    public virtual Task<ResourceMaintenance> GetResourceMaintenanceAsync(GetResourceMaintenanceRequest request, CallSettings callSettings = null)

Retrieve a single resource maintenance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetResourceMaintenanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.GetResourceMaintenanceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ResourceMaintenance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.ResourceMaintenance)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    MaintenanceClient maintenanceClient = await MaintenanceClient.CreateAsync();
    // Initialize request argument(s)
    GetResourceMaintenanceRequest request = new GetResourceMaintenanceRequest
    {
        ResourceMaintenanceName = ResourceMaintenanceName.FromProjectLocationResourceMaintenance("[PROJECT]", "[LOCATION]", "[RESOURCE_MAINTENANCE]"),
    };
    // Make the request
    ResourceMaintenance response = await maintenanceClient.GetResourceMaintenanceAsync(request);
    

### GetResourceMaintenanceAsync(GetResourceMaintenanceRequest, CancellationToken)
    
    
    public virtual Task<ResourceMaintenance> GetResourceMaintenanceAsync(GetResourceMaintenanceRequest request, CancellationToken cancellationToken)

Retrieve a single resource maintenance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetResourceMaintenanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.GetResourceMaintenanceRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ResourceMaintenance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.ResourceMaintenance)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    MaintenanceClient maintenanceClient = await MaintenanceClient.CreateAsync();
    // Initialize request argument(s)
    GetResourceMaintenanceRequest request = new GetResourceMaintenanceRequest
    {
        ResourceMaintenanceName = ResourceMaintenanceName.FromProjectLocationResourceMaintenance("[PROJECT]", "[LOCATION]", "[RESOURCE_MAINTENANCE]"),
    };
    // Make the request
    ResourceMaintenance response = await maintenanceClient.GetResourceMaintenanceAsync(request);
    

### GetResourceMaintenanceAsync(ResourceMaintenanceName, CallSettings)
    
    
    public virtual Task<ResourceMaintenance> GetResourceMaintenanceAsync(ResourceMaintenanceName name, CallSettings callSettings = null)

Retrieve a single resource maintenance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ResourceMaintenanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.ResourceMaintenanceName)`  
Required. The resource name of the resource within a service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ResourceMaintenance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.ResourceMaintenance)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    MaintenanceClient maintenanceClient = await MaintenanceClient.CreateAsync();
    // Initialize request argument(s)
    ResourceMaintenanceName name = ResourceMaintenanceName.FromProjectLocationResourceMaintenance("[PROJECT]", "[LOCATION]", "[RESOURCE_MAINTENANCE]");
    // Make the request
    ResourceMaintenance response = await maintenanceClient.GetResourceMaintenanceAsync(name);
    

### GetResourceMaintenanceAsync(ResourceMaintenanceName, CancellationToken)
    
    
    public virtual Task<ResourceMaintenance> GetResourceMaintenanceAsync(ResourceMaintenanceName name, CancellationToken cancellationToken)

Retrieve a single resource maintenance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ResourceMaintenanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.ResourceMaintenanceName)`  
Required. The resource name of the resource within a service.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ResourceMaintenance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.ResourceMaintenance)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    MaintenanceClient maintenanceClient = await MaintenanceClient.CreateAsync();
    // Initialize request argument(s)
    ResourceMaintenanceName name = ResourceMaintenanceName.FromProjectLocationResourceMaintenance("[PROJECT]", "[LOCATION]", "[RESOURCE_MAINTENANCE]");
    // Make the request
    ResourceMaintenance response = await maintenanceClient.GetResourceMaintenanceAsync(name);
    

### GetResourceMaintenanceAsync(string, CallSettings)
    
    
    public virtual Task<ResourceMaintenance> GetResourceMaintenanceAsync(string name, CallSettings callSettings = null)

Retrieve a single resource maintenance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the resource within a service.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ResourceMaintenance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.ResourceMaintenance)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    MaintenanceClient maintenanceClient = await MaintenanceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/resourceMaintenances/[RESOURCE_MAINTENANCE]";
    // Make the request
    ResourceMaintenance response = await maintenanceClient.GetResourceMaintenanceAsync(name);
    

### GetResourceMaintenanceAsync(string, CancellationToken)
    
    
    public virtual Task<ResourceMaintenance> GetResourceMaintenanceAsync(string name, CancellationToken cancellationToken)

Retrieve a single resource maintenance.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the resource within a service.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ResourceMaintenance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.ResourceMaintenance)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    MaintenanceClient maintenanceClient = await MaintenanceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/resourceMaintenances/[RESOURCE_MAINTENANCE]";
    // Make the request
    ResourceMaintenance response = await maintenanceClient.GetResourceMaintenanceAsync(name);
    

### ListResourceMaintenances(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListResourceMaintenancesResponse, ResourceMaintenance> ListResourceMaintenances(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieve a collection of resource maintenances.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent of the resource maintenance.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListResourceMaintenancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.ListResourceMaintenancesResponse)[ResourceMaintenance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.ResourceMaintenance)` | A pageable sequence of [ResourceMaintenance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.ResourceMaintenance) resources.  
**Example**
    
    
    // Create client
    MaintenanceClient maintenanceClient = MaintenanceClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListResourceMaintenancesResponse, ResourceMaintenance> response = maintenanceClient.ListResourceMaintenances(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (ResourceMaintenance item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListResourceMaintenancesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ResourceMaintenance item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ResourceMaintenance> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ResourceMaintenance item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListResourceMaintenances(ListResourceMaintenancesRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListResourceMaintenancesResponse, ResourceMaintenance> ListResourceMaintenances(ListResourceMaintenancesRequest request, CallSettings callSettings = null)

Retrieve a collection of resource maintenances.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListResourceMaintenancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.ListResourceMaintenancesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListResourceMaintenancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.ListResourceMaintenancesResponse)[ResourceMaintenance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.ResourceMaintenance)` | A pageable sequence of [ResourceMaintenance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.ResourceMaintenance) resources.  
**Example**
    
    
    // Create client
    MaintenanceClient maintenanceClient = MaintenanceClient.Create();
    // Initialize request argument(s)
    ListResourceMaintenancesRequest request = new ListResourceMaintenancesRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListResourceMaintenancesResponse, ResourceMaintenance> response = maintenanceClient.ListResourceMaintenances(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (ResourceMaintenance item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListResourceMaintenancesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ResourceMaintenance item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ResourceMaintenance> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ResourceMaintenance item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListResourceMaintenances(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListResourceMaintenancesResponse, ResourceMaintenance> ListResourceMaintenances(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieve a collection of resource maintenances.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent of the resource maintenance.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListResourceMaintenancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.ListResourceMaintenancesResponse)[ResourceMaintenance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.ResourceMaintenance)` | A pageable sequence of [ResourceMaintenance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.ResourceMaintenance) resources.  
**Example**
    
    
    // Create client
    MaintenanceClient maintenanceClient = MaintenanceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListResourceMaintenancesResponse, ResourceMaintenance> response = maintenanceClient.ListResourceMaintenances(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (ResourceMaintenance item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListResourceMaintenancesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ResourceMaintenance item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ResourceMaintenance> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ResourceMaintenance item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListResourceMaintenancesAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListResourceMaintenancesResponse, ResourceMaintenance> ListResourceMaintenancesAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieve a collection of resource maintenances.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent of the resource maintenance.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListResourceMaintenancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.ListResourceMaintenancesResponse)[ResourceMaintenance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.ResourceMaintenance)` | A pageable asynchronous sequence of [ResourceMaintenance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.ResourceMaintenance) resources.  
**Example**
    
    
    // Create client
    MaintenanceClient maintenanceClient = await MaintenanceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListResourceMaintenancesResponse, ResourceMaintenance> response = maintenanceClient.ListResourceMaintenancesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (ResourceMaintenance item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListResourceMaintenancesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ResourceMaintenance item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ResourceMaintenance> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ResourceMaintenance item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListResourceMaintenancesAsync(ListResourceMaintenancesRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListResourceMaintenancesResponse, ResourceMaintenance> ListResourceMaintenancesAsync(ListResourceMaintenancesRequest request, CallSettings callSettings = null)

Retrieve a collection of resource maintenances.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListResourceMaintenancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.ListResourceMaintenancesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListResourceMaintenancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.ListResourceMaintenancesResponse)[ResourceMaintenance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.ResourceMaintenance)` | A pageable asynchronous sequence of [ResourceMaintenance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.ResourceMaintenance) resources.  
**Example**
    
    
    // Create client
    MaintenanceClient maintenanceClient = await MaintenanceClient.CreateAsync();
    // Initialize request argument(s)
    ListResourceMaintenancesRequest request = new ListResourceMaintenancesRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListResourceMaintenancesResponse, ResourceMaintenance> response = maintenanceClient.ListResourceMaintenancesAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (ResourceMaintenance item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListResourceMaintenancesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ResourceMaintenance item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ResourceMaintenance> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ResourceMaintenance item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListResourceMaintenancesAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListResourceMaintenancesResponse, ResourceMaintenance> ListResourceMaintenancesAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieve a collection of resource maintenances.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent of the resource maintenance.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListResourceMaintenancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.ListResourceMaintenancesResponse)[ResourceMaintenance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.ResourceMaintenance)` | A pageable asynchronous sequence of [ResourceMaintenance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.ResourceMaintenance) resources.  
**Example**
    
    
    // Create client
    MaintenanceClient maintenanceClient = await MaintenanceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListResourceMaintenancesResponse, ResourceMaintenance> response = maintenanceClient.ListResourceMaintenancesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (ResourceMaintenance item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListResourceMaintenancesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ResourceMaintenance item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ResourceMaintenance> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ResourceMaintenance item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.MaintenanceClient#Google_Cloud_Maintenance_Api_V1_MaintenanceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.MaintenanceClient#Google_Cloud_Maintenance_Api_V1_MaintenanceClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.MaintenanceClient#Google_Cloud_Maintenance_Api_V1_MaintenanceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.MaintenanceClient#Google_Cloud_Maintenance_Api_V1_MaintenanceClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### SummarizeMaintenances(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<SummarizeMaintenancesResponse, MaintenanceSummary> SummarizeMaintenances(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieves the statistics of a specific maintenance.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent of the resource maintenance. eg. `projects/123/locations/*`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[SummarizeMaintenancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.SummarizeMaintenancesResponse)[MaintenanceSummary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.MaintenanceSummary)` | A pageable sequence of [MaintenanceSummary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.MaintenanceSummary) resources.  
**Example**
    
    
    // Create client
    MaintenanceClient maintenanceClient = MaintenanceClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<SummarizeMaintenancesResponse, MaintenanceSummary> response = maintenanceClient.SummarizeMaintenances(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (MaintenanceSummary item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (SummarizeMaintenancesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (MaintenanceSummary item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<MaintenanceSummary> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (MaintenanceSummary item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### SummarizeMaintenances(SummarizeMaintenancesRequest, CallSettings)
    
    
    public virtual PagedEnumerable<SummarizeMaintenancesResponse, MaintenanceSummary> SummarizeMaintenances(SummarizeMaintenancesRequest request, CallSettings callSettings = null)

Retrieves the statistics of a specific maintenance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SummarizeMaintenancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.SummarizeMaintenancesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[SummarizeMaintenancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.SummarizeMaintenancesResponse)[MaintenanceSummary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.MaintenanceSummary)` | A pageable sequence of [MaintenanceSummary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.MaintenanceSummary) resources.  
**Example**
    
    
    // Create client
    MaintenanceClient maintenanceClient = MaintenanceClient.Create();
    // Initialize request argument(s)
    SummarizeMaintenancesRequest request = new SummarizeMaintenancesRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<SummarizeMaintenancesResponse, MaintenanceSummary> response = maintenanceClient.SummarizeMaintenances(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (MaintenanceSummary item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (SummarizeMaintenancesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (MaintenanceSummary item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<MaintenanceSummary> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (MaintenanceSummary item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### SummarizeMaintenances(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<SummarizeMaintenancesResponse, MaintenanceSummary> SummarizeMaintenances(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieves the statistics of a specific maintenance.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent of the resource maintenance. eg. `projects/123/locations/*`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[SummarizeMaintenancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.SummarizeMaintenancesResponse)[MaintenanceSummary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.MaintenanceSummary)` | A pageable sequence of [MaintenanceSummary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.MaintenanceSummary) resources.  
**Example**
    
    
    // Create client
    MaintenanceClient maintenanceClient = MaintenanceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<SummarizeMaintenancesResponse, MaintenanceSummary> response = maintenanceClient.SummarizeMaintenances(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (MaintenanceSummary item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (SummarizeMaintenancesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (MaintenanceSummary item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<MaintenanceSummary> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (MaintenanceSummary item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### SummarizeMaintenancesAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<SummarizeMaintenancesResponse, MaintenanceSummary> SummarizeMaintenancesAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieves the statistics of a specific maintenance.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent of the resource maintenance. eg. `projects/123/locations/*`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[SummarizeMaintenancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.SummarizeMaintenancesResponse)[MaintenanceSummary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.MaintenanceSummary)` | A pageable asynchronous sequence of [MaintenanceSummary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.MaintenanceSummary) resources.  
**Example**
    
    
    // Create client
    MaintenanceClient maintenanceClient = await MaintenanceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<SummarizeMaintenancesResponse, MaintenanceSummary> response = maintenanceClient.SummarizeMaintenancesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (MaintenanceSummary item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (SummarizeMaintenancesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (MaintenanceSummary item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<MaintenanceSummary> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (MaintenanceSummary item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### SummarizeMaintenancesAsync(SummarizeMaintenancesRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<SummarizeMaintenancesResponse, MaintenanceSummary> SummarizeMaintenancesAsync(SummarizeMaintenancesRequest request, CallSettings callSettings = null)

Retrieves the statistics of a specific maintenance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SummarizeMaintenancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.SummarizeMaintenancesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[SummarizeMaintenancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.SummarizeMaintenancesResponse)[MaintenanceSummary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.MaintenanceSummary)` | A pageable asynchronous sequence of [MaintenanceSummary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.MaintenanceSummary) resources.  
**Example**
    
    
    // Create client
    MaintenanceClient maintenanceClient = await MaintenanceClient.CreateAsync();
    // Initialize request argument(s)
    SummarizeMaintenancesRequest request = new SummarizeMaintenancesRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<SummarizeMaintenancesResponse, MaintenanceSummary> response = maintenanceClient.SummarizeMaintenancesAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (MaintenanceSummary item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (SummarizeMaintenancesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (MaintenanceSummary item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<MaintenanceSummary> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (MaintenanceSummary item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### SummarizeMaintenancesAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<SummarizeMaintenancesResponse, MaintenanceSummary> SummarizeMaintenancesAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieves the statistics of a specific maintenance.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent of the resource maintenance. eg. `projects/123/locations/*`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[SummarizeMaintenancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.SummarizeMaintenancesResponse)[MaintenanceSummary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.MaintenanceSummary)` | A pageable asynchronous sequence of [MaintenanceSummary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.MaintenanceSummary) resources.  
**Example**
    
    
    // Create client
    MaintenanceClient maintenanceClient = await MaintenanceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<SummarizeMaintenancesResponse, MaintenanceSummary> response = maintenanceClient.SummarizeMaintenancesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (MaintenanceSummary item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (SummarizeMaintenancesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (MaintenanceSummary item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<MaintenanceSummary> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (MaintenanceSummary item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
