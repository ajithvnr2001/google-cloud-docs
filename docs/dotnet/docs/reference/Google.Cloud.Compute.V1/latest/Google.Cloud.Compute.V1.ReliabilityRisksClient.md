---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReliabilityRisksClient
title: Compute Engine v1 API - Class ReliabilityRisksClient (4.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:36:47.984334+00:00
---

# Compute Engine v1 API - Class ReliabilityRisksClient (4.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReliabilityRisksClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Compute Engine v1 API - Class ReliabilityRisksClient (4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public abstract class ReliabilityRisksClient

Reference documentation and code samples for the Compute Engine v1 API class ReliabilityRisksClient.

ReliabilityRisks client wrapper, for convenient use. This client implements API version 2026-09-01.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ReliabilityRisksClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[ReliabilityRisksClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReliabilityRisksClientImpl)

## Namespace

[Google.Cloud.Compute.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1)

## Assembly

Google.Cloud.Compute.V1.dll

## Remarks

The ReliabilityRisks API.

## Properties 

### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the ReliabilityRisks service, which is a host of "compute.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default ReliabilityRisks scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default ReliabilityRisks scopes are:

  * <https://www.googleapis.com/auth/compute.readonly>
  * <https://www.googleapis.com/auth/compute>
  * <https://www.googleapis.com/auth/cloud-platform>



### GrpcClient
    
    
    public virtual ReliabilityRisks.ReliabilityRisksClient GrpcClient { get; }

The underlying gRPC ReliabilityRisks client

**Property Value**  
---  
**Type** | **Description**  
`[ReliabilityRisks](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReliabilityRisks)[ReliabilityRisksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReliabilityRisks.ReliabilityRisksClient)` |   
  
### ServiceMetadata
    
    
    public static ServiceMetadata ServiceMetadata { get; }

The service metadata associated with this client type.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceMetadata](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceMetadata.html)` |   
  
## Methods 

### Create()
    
    
    public static ReliabilityRisksClient Create()

Synchronously creates a [ReliabilityRisksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReliabilityRisksClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [ReliabilityRisksClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReliabilityRisksClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[ReliabilityRisksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReliabilityRisksClient)` | The created [ReliabilityRisksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReliabilityRisksClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<ReliabilityRisksClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [ReliabilityRisksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReliabilityRisksClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [ReliabilityRisksClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReliabilityRisksClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ReliabilityRisksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReliabilityRisksClient)` | The task representing the created [ReliabilityRisksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReliabilityRisksClient).  
  
### Get(GetReliabilityRiskRequest, CallSettings)
    
    
    public virtual ReliabilityRisk Get(GetReliabilityRiskRequest request, CallSettings callSettings = null)

Returns the specified ReliabilityRisk resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetReliabilityRiskRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetReliabilityRiskRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ReliabilityRisk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReliabilityRisk)` | The RPC response.  
**Example**
    
    
    // Create client
    ReliabilityRisksClient reliabilityRisksClient = ReliabilityRisksClient.Create();
    // Initialize request argument(s)
    GetReliabilityRiskRequest request = new GetReliabilityRiskRequest
    {
        Project = "",
        ReliabilityRisk = "",
    };
    // Make the request
    ReliabilityRisk response = reliabilityRisksClient.Get(request);
    

### Get(string, string, CallSettings)
    
    
    public virtual ReliabilityRisk Get(string project, string reliabilityRisk, CallSettings callSettings = null)

Returns the specified ReliabilityRisk resource.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`reliabilityRisk` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the ReliabilityRisk resource to return.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ReliabilityRisk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReliabilityRisk)` | The RPC response.  
**Example**
    
    
    // Create client
    ReliabilityRisksClient reliabilityRisksClient = ReliabilityRisksClient.Create();
    // Initialize request argument(s)
    string project = "";
    string reliabilityRisk = "";
    // Make the request
    ReliabilityRisk response = reliabilityRisksClient.Get(project, reliabilityRisk);
    

### GetAsync(GetReliabilityRiskRequest, CallSettings)
    
    
    public virtual Task<ReliabilityRisk> GetAsync(GetReliabilityRiskRequest request, CallSettings callSettings = null)

Returns the specified ReliabilityRisk resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetReliabilityRiskRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetReliabilityRiskRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ReliabilityRisk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReliabilityRisk)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ReliabilityRisksClient reliabilityRisksClient = await ReliabilityRisksClient.CreateAsync();
    // Initialize request argument(s)
    GetReliabilityRiskRequest request = new GetReliabilityRiskRequest
    {
        Project = "",
        ReliabilityRisk = "",
    };
    // Make the request
    ReliabilityRisk response = await reliabilityRisksClient.GetAsync(request);
    

### GetAsync(GetReliabilityRiskRequest, CancellationToken)
    
    
    public virtual Task<ReliabilityRisk> GetAsync(GetReliabilityRiskRequest request, CancellationToken cancellationToken)

Returns the specified ReliabilityRisk resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetReliabilityRiskRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetReliabilityRiskRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ReliabilityRisk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReliabilityRisk)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ReliabilityRisksClient reliabilityRisksClient = await ReliabilityRisksClient.CreateAsync();
    // Initialize request argument(s)
    GetReliabilityRiskRequest request = new GetReliabilityRiskRequest
    {
        Project = "",
        ReliabilityRisk = "",
    };
    // Make the request
    ReliabilityRisk response = await reliabilityRisksClient.GetAsync(request);
    

### GetAsync(string, string, CallSettings)
    
    
    public virtual Task<ReliabilityRisk> GetAsync(string project, string reliabilityRisk, CallSettings callSettings = null)

Returns the specified ReliabilityRisk resource.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`reliabilityRisk` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the ReliabilityRisk resource to return.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ReliabilityRisk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReliabilityRisk)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ReliabilityRisksClient reliabilityRisksClient = await ReliabilityRisksClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string reliabilityRisk = "";
    // Make the request
    ReliabilityRisk response = await reliabilityRisksClient.GetAsync(project, reliabilityRisk);
    

### GetAsync(string, string, CancellationToken)
    
    
    public virtual Task<ReliabilityRisk> GetAsync(string project, string reliabilityRisk, CancellationToken cancellationToken)

Returns the specified ReliabilityRisk resource.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`reliabilityRisk` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the ReliabilityRisk resource to return.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ReliabilityRisk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReliabilityRisk)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ReliabilityRisksClient reliabilityRisksClient = await ReliabilityRisksClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string reliabilityRisk = "";
    // Make the request
    ReliabilityRisk response = await reliabilityRisksClient.GetAsync(project, reliabilityRisk);
    

### List(ListReliabilityRisksRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ReliabilityRisksListResponse, ReliabilityRisk> List(ListReliabilityRisksRequest request, CallSettings callSettings = null)

Retrieves the list of reliabilityRisks available in the specified project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListReliabilityRisksRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ListReliabilityRisksRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ReliabilityRisksListResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReliabilityRisksListResponse)[ReliabilityRisk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReliabilityRisk)` | A pageable sequence of [ReliabilityRisk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReliabilityRisk) resources.  
**Example**
    
    
    // Create client
    ReliabilityRisksClient reliabilityRisksClient = ReliabilityRisksClient.Create();
    // Initialize request argument(s)
    ListReliabilityRisksRequest request = new ListReliabilityRisksRequest
    {
        OrderBy = "",
        Project = "",
        Filter = "",
    };
    // Make the request
    PagedEnumerable<ReliabilityRisksListResponse, ReliabilityRisk> response = reliabilityRisksClient.List(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (ReliabilityRisk item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ReliabilityRisksListResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ReliabilityRisk item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ReliabilityRisk> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ReliabilityRisk item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### List(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ReliabilityRisksListResponse, ReliabilityRisk> List(string project, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieves the list of reliabilityRisks available in the specified project.

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
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ReliabilityRisksListResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReliabilityRisksListResponse)[ReliabilityRisk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReliabilityRisk)` | A pageable sequence of [ReliabilityRisk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReliabilityRisk) resources.  
**Example**
    
    
    // Create client
    ReliabilityRisksClient reliabilityRisksClient = ReliabilityRisksClient.Create();
    // Initialize request argument(s)
    string project = "";
    // Make the request
    PagedEnumerable<ReliabilityRisksListResponse, ReliabilityRisk> response = reliabilityRisksClient.List(project);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (ReliabilityRisk item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ReliabilityRisksListResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ReliabilityRisk item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ReliabilityRisk> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ReliabilityRisk item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAsync(ListReliabilityRisksRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ReliabilityRisksListResponse, ReliabilityRisk> ListAsync(ListReliabilityRisksRequest request, CallSettings callSettings = null)

Retrieves the list of reliabilityRisks available in the specified project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListReliabilityRisksRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ListReliabilityRisksRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ReliabilityRisksListResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReliabilityRisksListResponse)[ReliabilityRisk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReliabilityRisk)` | A pageable asynchronous sequence of [ReliabilityRisk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReliabilityRisk) resources.  
**Example**
    
    
    // Create client
    ReliabilityRisksClient reliabilityRisksClient = await ReliabilityRisksClient.CreateAsync();
    // Initialize request argument(s)
    ListReliabilityRisksRequest request = new ListReliabilityRisksRequest
    {
        OrderBy = "",
        Project = "",
        Filter = "",
    };
    // Make the request
    PagedAsyncEnumerable<ReliabilityRisksListResponse, ReliabilityRisk> response = reliabilityRisksClient.ListAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (ReliabilityRisk item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ReliabilityRisksListResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ReliabilityRisk item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ReliabilityRisk> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ReliabilityRisk item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ReliabilityRisksListResponse, ReliabilityRisk> ListAsync(string project, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieves the list of reliabilityRisks available in the specified project.

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
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ReliabilityRisksListResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReliabilityRisksListResponse)[ReliabilityRisk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReliabilityRisk)` | A pageable asynchronous sequence of [ReliabilityRisk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReliabilityRisk) resources.  
**Example**
    
    
    // Create client
    ReliabilityRisksClient reliabilityRisksClient = await ReliabilityRisksClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    // Make the request
    PagedAsyncEnumerable<ReliabilityRisksListResponse, ReliabilityRisk> response = reliabilityRisksClient.ListAsync(project);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (ReliabilityRisk item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ReliabilityRisksListResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ReliabilityRisk item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ReliabilityRisk> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ReliabilityRisk item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReliabilityRisksClient#Google_Cloud_Compute_V1_ReliabilityRisksClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReliabilityRisksClient#Google_Cloud_Compute_V1_ReliabilityRisksClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReliabilityRisksClient#Google_Cloud_Compute_V1_ReliabilityRisksClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReliabilityRisksClient#Google_Cloud_Compute_V1_ReliabilityRisksClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
