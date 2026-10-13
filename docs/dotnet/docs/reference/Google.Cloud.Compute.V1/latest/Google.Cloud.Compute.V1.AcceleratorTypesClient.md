---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorTypesClient
title: Compute Engine v1 API - Class AcceleratorTypesClient (4.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:24:46.791341+00:00
---

# Compute Engine v1 API - Class AcceleratorTypesClient (4.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorTypesClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Compute Engine v1 API - Class AcceleratorTypesClient (4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public abstract class AcceleratorTypesClient

Reference documentation and code samples for the Compute Engine v1 API class AcceleratorTypesClient.

AcceleratorTypes client wrapper, for convenient use. This client implements API version 2026-09-01.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AcceleratorTypesClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[AcceleratorTypesClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorTypesClientImpl)

## Namespace

[Google.Cloud.Compute.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1)

## Assembly

Google.Cloud.Compute.V1.dll

## Remarks

Services

The AcceleratorTypes API.

## Properties 

### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the AcceleratorTypes service, which is a host of "compute.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default AcceleratorTypes scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default AcceleratorTypes scopes are:

  * <https://www.googleapis.com/auth/compute.readonly>
  * <https://www.googleapis.com/auth/compute>
  * <https://www.googleapis.com/auth/cloud-platform>



### GrpcClient
    
    
    public virtual AcceleratorTypes.AcceleratorTypesClient GrpcClient { get; }

The underlying gRPC AcceleratorTypes client

**Property Value**  
---  
**Type** | **Description**  
`[AcceleratorTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorTypes)[AcceleratorTypesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorTypes.AcceleratorTypesClient)` |   
  
### ServiceMetadata
    
    
    public static ServiceMetadata ServiceMetadata { get; }

The service metadata associated with this client type.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceMetadata](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceMetadata.html)` |   
  
## Methods 

### AggregatedList(AggregatedListAcceleratorTypesRequest, CallSettings)
    
    
    public virtual PagedEnumerable<AcceleratorTypeAggregatedList, KeyValuePair<string, AcceleratorTypesScopedList>> AggregatedList(AggregatedListAcceleratorTypesRequest request, CallSettings callSettings = null)

Retrieves an aggregated list of accelerator types.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AggregatedListAcceleratorTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AggregatedListAcceleratorTypesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[AcceleratorTypeAggregatedList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorTypeAggregatedList)[KeyValuePair](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair-2)[string](https://learn.microsoft.com/dotnet/api/system.string)[AcceleratorTypesScopedList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorTypesScopedList)` | A pageable sequence of [KeyValuePair<TKey, TValue>](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair-2) resources.  
**Example**
    
    
    // Create client
    AcceleratorTypesClient acceleratorTypesClient = AcceleratorTypesClient.Create();
    // Initialize request argument(s)
    AggregatedListAcceleratorTypesRequest request = new AggregatedListAcceleratorTypesRequest
    {
        OrderBy = "",
        Project = "",
        ServiceProjectNumber = 0L,
        Filter = "",
        IncludeAllScopes = false,
    };
    // Make the request
    PagedEnumerable<AcceleratorTypeAggregatedList, KeyValuePair<string, AcceleratorTypesScopedList>> response = acceleratorTypesClient.AggregatedList(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (KeyValuePair<string, AcceleratorTypesScopedList> item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (AcceleratorTypeAggregatedList page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (KeyValuePair<string, AcceleratorTypesScopedList> item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<KeyValuePair<string, AcceleratorTypesScopedList>> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (KeyValuePair<string, AcceleratorTypesScopedList> item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### AggregatedList(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<AcceleratorTypeAggregatedList, KeyValuePair<string, AcceleratorTypesScopedList>> AggregatedList(string project, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieves an aggregated list of accelerator types.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[AcceleratorTypeAggregatedList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorTypeAggregatedList)[KeyValuePair](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair-2)[string](https://learn.microsoft.com/dotnet/api/system.string)[AcceleratorTypesScopedList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorTypesScopedList)` | A pageable sequence of [KeyValuePair<TKey, TValue>](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair-2) resources.  
**Example**
    
    
    // Create client
    AcceleratorTypesClient acceleratorTypesClient = AcceleratorTypesClient.Create();
    // Initialize request argument(s)
    string project = "";
    // Make the request
    PagedEnumerable<AcceleratorTypeAggregatedList, KeyValuePair<string, AcceleratorTypesScopedList>> response = acceleratorTypesClient.AggregatedList(project);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (KeyValuePair<string, AcceleratorTypesScopedList> item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (AcceleratorTypeAggregatedList page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (KeyValuePair<string, AcceleratorTypesScopedList> item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<KeyValuePair<string, AcceleratorTypesScopedList>> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (KeyValuePair<string, AcceleratorTypesScopedList> item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### AggregatedListAsync(AggregatedListAcceleratorTypesRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<AcceleratorTypeAggregatedList, KeyValuePair<string, AcceleratorTypesScopedList>> AggregatedListAsync(AggregatedListAcceleratorTypesRequest request, CallSettings callSettings = null)

Retrieves an aggregated list of accelerator types.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AggregatedListAcceleratorTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AggregatedListAcceleratorTypesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[AcceleratorTypeAggregatedList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorTypeAggregatedList)[KeyValuePair](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair-2)[string](https://learn.microsoft.com/dotnet/api/system.string)[AcceleratorTypesScopedList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorTypesScopedList)` | A pageable asynchronous sequence of [KeyValuePair<TKey, TValue>](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair-2) resources.  
**Example**
    
    
    // Create client
    AcceleratorTypesClient acceleratorTypesClient = await AcceleratorTypesClient.CreateAsync();
    // Initialize request argument(s)
    AggregatedListAcceleratorTypesRequest request = new AggregatedListAcceleratorTypesRequest
    {
        OrderBy = "",
        Project = "",
        ServiceProjectNumber = 0L,
        Filter = "",
        IncludeAllScopes = false,
    };
    // Make the request
    PagedAsyncEnumerable<AcceleratorTypeAggregatedList, KeyValuePair<string, AcceleratorTypesScopedList>> response = acceleratorTypesClient.AggregatedListAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (KeyValuePair<string, AcceleratorTypesScopedList> item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (AcceleratorTypeAggregatedList page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (KeyValuePair<string, AcceleratorTypesScopedList> item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<KeyValuePair<string, AcceleratorTypesScopedList>> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (KeyValuePair<string, AcceleratorTypesScopedList> item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### AggregatedListAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<AcceleratorTypeAggregatedList, KeyValuePair<string, AcceleratorTypesScopedList>> AggregatedListAsync(string project, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieves an aggregated list of accelerator types.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[AcceleratorTypeAggregatedList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorTypeAggregatedList)[KeyValuePair](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair-2)[string](https://learn.microsoft.com/dotnet/api/system.string)[AcceleratorTypesScopedList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorTypesScopedList)` | A pageable asynchronous sequence of [KeyValuePair<TKey, TValue>](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair-2) resources.  
**Example**
    
    
    // Create client
    AcceleratorTypesClient acceleratorTypesClient = await AcceleratorTypesClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    // Make the request
    PagedAsyncEnumerable<AcceleratorTypeAggregatedList, KeyValuePair<string, AcceleratorTypesScopedList>> response = acceleratorTypesClient.AggregatedListAsync(project);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (KeyValuePair<string, AcceleratorTypesScopedList> item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (AcceleratorTypeAggregatedList page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (KeyValuePair<string, AcceleratorTypesScopedList> item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<KeyValuePair<string, AcceleratorTypesScopedList>> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (KeyValuePair<string, AcceleratorTypesScopedList> item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### Create()
    
    
    public static AcceleratorTypesClient Create()

Synchronously creates a [AcceleratorTypesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorTypesClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [AcceleratorTypesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorTypesClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[AcceleratorTypesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorTypesClient)` | The created [AcceleratorTypesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorTypesClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<AcceleratorTypesClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [AcceleratorTypesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorTypesClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [AcceleratorTypesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorTypesClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AcceleratorTypesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorTypesClient)` | The task representing the created [AcceleratorTypesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorTypesClient).  
  
### Get(GetAcceleratorTypeRequest, CallSettings)
    
    
    public virtual AcceleratorType Get(GetAcceleratorTypeRequest request, CallSettings callSettings = null)

Returns the specified accelerator type.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAcceleratorTypeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetAcceleratorTypeRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[AcceleratorType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorType)` | The RPC response.  
**Example**
    
    
    // Create client
    AcceleratorTypesClient acceleratorTypesClient = AcceleratorTypesClient.Create();
    // Initialize request argument(s)
    GetAcceleratorTypeRequest request = new GetAcceleratorTypeRequest
    {
        Zone = "",
        AcceleratorType = "",
        Project = "",
    };
    // Make the request
    AcceleratorType response = acceleratorTypesClient.Get(request);
    

### Get(string, string, string, CallSettings)
    
    
    public virtual AcceleratorType Get(string project, string zone, string acceleratorType, CallSettings callSettings = null)

Returns the specified accelerator type.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`zone` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the zone for this request.  
`acceleratorType` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the accelerator type to return.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[AcceleratorType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorType)` | The RPC response.  
**Example**
    
    
    // Create client
    AcceleratorTypesClient acceleratorTypesClient = AcceleratorTypesClient.Create();
    // Initialize request argument(s)
    string project = "";
    string zone = "";
    string acceleratorType = "";
    // Make the request
    AcceleratorType response = acceleratorTypesClient.Get(project, zone, acceleratorType);
    

### GetAsync(GetAcceleratorTypeRequest, CallSettings)
    
    
    public virtual Task<AcceleratorType> GetAsync(GetAcceleratorTypeRequest request, CallSettings callSettings = null)

Returns the specified accelerator type.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAcceleratorTypeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetAcceleratorTypeRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AcceleratorType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorType)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AcceleratorTypesClient acceleratorTypesClient = await AcceleratorTypesClient.CreateAsync();
    // Initialize request argument(s)
    GetAcceleratorTypeRequest request = new GetAcceleratorTypeRequest
    {
        Zone = "",
        AcceleratorType = "",
        Project = "",
    };
    // Make the request
    AcceleratorType response = await acceleratorTypesClient.GetAsync(request);
    

### GetAsync(GetAcceleratorTypeRequest, CancellationToken)
    
    
    public virtual Task<AcceleratorType> GetAsync(GetAcceleratorTypeRequest request, CancellationToken cancellationToken)

Returns the specified accelerator type.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAcceleratorTypeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetAcceleratorTypeRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AcceleratorType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorType)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AcceleratorTypesClient acceleratorTypesClient = await AcceleratorTypesClient.CreateAsync();
    // Initialize request argument(s)
    GetAcceleratorTypeRequest request = new GetAcceleratorTypeRequest
    {
        Zone = "",
        AcceleratorType = "",
        Project = "",
    };
    // Make the request
    AcceleratorType response = await acceleratorTypesClient.GetAsync(request);
    

### GetAsync(string, string, string, CallSettings)
    
    
    public virtual Task<AcceleratorType> GetAsync(string project, string zone, string acceleratorType, CallSettings callSettings = null)

Returns the specified accelerator type.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`zone` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the zone for this request.  
`acceleratorType` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the accelerator type to return.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AcceleratorType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorType)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AcceleratorTypesClient acceleratorTypesClient = await AcceleratorTypesClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string zone = "";
    string acceleratorType = "";
    // Make the request
    AcceleratorType response = await acceleratorTypesClient.GetAsync(project, zone, acceleratorType);
    

### GetAsync(string, string, string, CancellationToken)
    
    
    public virtual Task<AcceleratorType> GetAsync(string project, string zone, string acceleratorType, CancellationToken cancellationToken)

Returns the specified accelerator type.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`zone` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the zone for this request.  
`acceleratorType` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the accelerator type to return.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AcceleratorType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorType)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AcceleratorTypesClient acceleratorTypesClient = await AcceleratorTypesClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string zone = "";
    string acceleratorType = "";
    // Make the request
    AcceleratorType response = await acceleratorTypesClient.GetAsync(project, zone, acceleratorType);
    

### List(ListAcceleratorTypesRequest, CallSettings)
    
    
    public virtual PagedEnumerable<AcceleratorTypeList, AcceleratorType> List(ListAcceleratorTypesRequest request, CallSettings callSettings = null)

Retrieves a list of accelerator types that are available to the specified project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAcceleratorTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ListAcceleratorTypesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[AcceleratorTypeList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorTypeList)[AcceleratorType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorType)` | A pageable sequence of [AcceleratorType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorType) resources.  
**Example**
    
    
    // Create client
    AcceleratorTypesClient acceleratorTypesClient = AcceleratorTypesClient.Create();
    // Initialize request argument(s)
    ListAcceleratorTypesRequest request = new ListAcceleratorTypesRequest
    {
        Zone = "",
        OrderBy = "",
        Project = "",
        Filter = "",
    };
    // Make the request
    PagedEnumerable<AcceleratorTypeList, AcceleratorType> response = acceleratorTypesClient.List(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (AcceleratorType item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (AcceleratorTypeList page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (AcceleratorType item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<AcceleratorType> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (AcceleratorType item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### List(string, string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<AcceleratorTypeList, AcceleratorType> List(string project, string zone, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieves a list of accelerator types that are available to the specified project.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`zone` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the zone for this request.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[AcceleratorTypeList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorTypeList)[AcceleratorType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorType)` | A pageable sequence of [AcceleratorType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorType) resources.  
**Example**
    
    
    // Create client
    AcceleratorTypesClient acceleratorTypesClient = AcceleratorTypesClient.Create();
    // Initialize request argument(s)
    string project = "";
    string zone = "";
    // Make the request
    PagedEnumerable<AcceleratorTypeList, AcceleratorType> response = acceleratorTypesClient.List(project, zone);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (AcceleratorType item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (AcceleratorTypeList page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (AcceleratorType item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<AcceleratorType> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (AcceleratorType item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAsync(ListAcceleratorTypesRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<AcceleratorTypeList, AcceleratorType> ListAsync(ListAcceleratorTypesRequest request, CallSettings callSettings = null)

Retrieves a list of accelerator types that are available to the specified project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAcceleratorTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ListAcceleratorTypesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[AcceleratorTypeList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorTypeList)[AcceleratorType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorType)` | A pageable asynchronous sequence of [AcceleratorType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorType) resources.  
**Example**
    
    
    // Create client
    AcceleratorTypesClient acceleratorTypesClient = await AcceleratorTypesClient.CreateAsync();
    // Initialize request argument(s)
    ListAcceleratorTypesRequest request = new ListAcceleratorTypesRequest
    {
        Zone = "",
        OrderBy = "",
        Project = "",
        Filter = "",
    };
    // Make the request
    PagedAsyncEnumerable<AcceleratorTypeList, AcceleratorType> response = acceleratorTypesClient.ListAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (AcceleratorType item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (AcceleratorTypeList page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (AcceleratorType item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<AcceleratorType> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (AcceleratorType item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAsync(string, string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<AcceleratorTypeList, AcceleratorType> ListAsync(string project, string zone, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieves a list of accelerator types that are available to the specified project.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`zone` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the zone for this request.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[AcceleratorTypeList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorTypeList)[AcceleratorType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorType)` | A pageable asynchronous sequence of [AcceleratorType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorType) resources.  
**Example**
    
    
    // Create client
    AcceleratorTypesClient acceleratorTypesClient = await AcceleratorTypesClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string zone = "";
    // Make the request
    PagedAsyncEnumerable<AcceleratorTypeList, AcceleratorType> response = acceleratorTypesClient.ListAsync(project, zone);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (AcceleratorType item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (AcceleratorTypeList page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (AcceleratorType item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<AcceleratorType> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (AcceleratorType item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorTypesClient#Google_Cloud_Compute_V1_AcceleratorTypesClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorTypesClient#Google_Cloud_Compute_V1_AcceleratorTypesClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorTypesClient#Google_Cloud_Compute_V1_AcceleratorTypesClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorTypesClient#Google_Cloud_Compute_V1_AcceleratorTypesClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
