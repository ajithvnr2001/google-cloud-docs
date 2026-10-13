---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.ConnectionServiceClient
title: Apigee Connect v1 API - Class ConnectionServiceClient (2.5.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:14:46.563059+00:00
---

# Apigee Connect v1 API - Class ConnectionServiceClient (2.5.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.ConnectionServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Apigee Connect v1 API - Class ConnectionServiceClient (2.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.5.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.ConnectionServiceClient)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/2.4.0/Google.Cloud.ApigeeConnect.V1.ConnectionServiceClient)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/2.3.0/Google.Cloud.ApigeeConnect.V1.ConnectionServiceClient)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/2.2.0/Google.Cloud.ApigeeConnect.V1.ConnectionServiceClient)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/2.1.0/Google.Cloud.ApigeeConnect.V1.ConnectionServiceClient)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/2.0.0/Google.Cloud.ApigeeConnect.V1.ConnectionServiceClient)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/1.1.0/Google.Cloud.ApigeeConnect.V1.ConnectionServiceClient)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/1.0.0/Google.Cloud.ApigeeConnect.V1.ConnectionServiceClient)


    
    
    public abstract class ConnectionServiceClient

Reference documentation and code samples for the Apigee Connect v1 API class ConnectionServiceClient.

ConnectionService client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ConnectionServiceClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[ConnectionServiceClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.ConnectionServiceClientImpl)

## Namespace

[Google.Cloud.ApigeeConnect.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1)

## Assembly

Google.Cloud.ApigeeConnect.V1.dll

## Remarks

Service Interface for the Apigee Connect connection management APIs.

## Properties 

### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the ConnectionService service, which is a host of "apigeeconnect.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default ConnectionService scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default ConnectionService scopes are: 

  * <https://www.googleapis.com/auth/cloud-platform>



### GrpcClient
    
    
    public virtual ConnectionService.ConnectionServiceClient GrpcClient { get; }

The underlying gRPC ConnectionService client

**Property Value**  
---  
**Type** | **Description**  
`[ConnectionService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.ConnectionService)[ConnectionServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.ConnectionService.ConnectionServiceClient)` |   
  
### ServiceMetadata
    
    
    public static ServiceMetadata ServiceMetadata { get; }

The service metadata associated with this client type.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceMetadata](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceMetadata.html)` |   
  
## Methods 

### Create()
    
    
    public static ConnectionServiceClient Create()

Synchronously creates a [ConnectionServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.ConnectionServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [ConnectionServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.ConnectionServiceClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[ConnectionServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.ConnectionServiceClient)` | The created [ConnectionServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.ConnectionServiceClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<ConnectionServiceClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [ConnectionServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.ConnectionServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [ConnectionServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.ConnectionServiceClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ConnectionServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.ConnectionServiceClient)` | The task representing the created [ConnectionServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.ConnectionServiceClient).  
  
### ListConnections(EndpointName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListConnectionsResponse, Connection> ListConnections(EndpointName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists connections that are currently active for the given Apigee Connect endpoint.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[EndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.EndpointName)`  
Required. Parent name of the form: `projects/{project_number or project_id}/endpoints/{endpoint}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListConnectionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.ListConnectionsResponse)[Connection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.Connection)` | A pageable sequence of [Connection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.Connection) resources.  
**Example**
    
    
    // Create client
    ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.Create();
    // Initialize request argument(s)
    EndpointName parent = EndpointName.FromProjectEndpoint("[PROJECT]", "[ENDPOINT]");
    // Make the request
    PagedEnumerable<ListConnectionsResponse, Connection> response = connectionServiceClient.ListConnections(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Connection item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListConnectionsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Connection item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Connection> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Connection item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListConnections(ListConnectionsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListConnectionsResponse, Connection> ListConnections(ListConnectionsRequest request, CallSettings callSettings = null)

Lists connections that are currently active for the given Apigee Connect endpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListConnectionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.ListConnectionsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListConnectionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.ListConnectionsResponse)[Connection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.Connection)` | A pageable sequence of [Connection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.Connection) resources.  
**Example**
    
    
    // Create client
    ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.Create();
    // Initialize request argument(s)
    ListConnectionsRequest request = new ListConnectionsRequest
    {
        ParentAsEndpointName = EndpointName.FromProjectEndpoint("[PROJECT]", "[ENDPOINT]"),
    };
    // Make the request
    PagedEnumerable<ListConnectionsResponse, Connection> response = connectionServiceClient.ListConnections(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Connection item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListConnectionsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Connection item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Connection> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Connection item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListConnections(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListConnectionsResponse, Connection> ListConnections(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists connections that are currently active for the given Apigee Connect endpoint.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Parent name of the form: `projects/{project_number or project_id}/endpoints/{endpoint}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListConnectionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.ListConnectionsResponse)[Connection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.Connection)` | A pageable sequence of [Connection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.Connection) resources.  
**Example**
    
    
    // Create client
    ConnectionServiceClient connectionServiceClient = ConnectionServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/endpoints/[ENDPOINT]";
    // Make the request
    PagedEnumerable<ListConnectionsResponse, Connection> response = connectionServiceClient.ListConnections(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Connection item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListConnectionsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Connection item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Connection> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Connection item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListConnectionsAsync(EndpointName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListConnectionsResponse, Connection> ListConnectionsAsync(EndpointName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists connections that are currently active for the given Apigee Connect endpoint.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[EndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.EndpointName)`  
Required. Parent name of the form: `projects/{project_number or project_id}/endpoints/{endpoint}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListConnectionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.ListConnectionsResponse)[Connection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.Connection)` | A pageable asynchronous sequence of [Connection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.Connection) resources.  
**Example**
    
    
    // Create client
    ConnectionServiceClient connectionServiceClient = await ConnectionServiceClient.CreateAsync();
    // Initialize request argument(s)
    EndpointName parent = EndpointName.FromProjectEndpoint("[PROJECT]", "[ENDPOINT]");
    // Make the request
    PagedAsyncEnumerable<ListConnectionsResponse, Connection> response = connectionServiceClient.ListConnectionsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Connection item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListConnectionsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Connection item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Connection> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Connection item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListConnectionsAsync(ListConnectionsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListConnectionsResponse, Connection> ListConnectionsAsync(ListConnectionsRequest request, CallSettings callSettings = null)

Lists connections that are currently active for the given Apigee Connect endpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListConnectionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.ListConnectionsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListConnectionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.ListConnectionsResponse)[Connection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.Connection)` | A pageable asynchronous sequence of [Connection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.Connection) resources.  
**Example**
    
    
    // Create client
    ConnectionServiceClient connectionServiceClient = await ConnectionServiceClient.CreateAsync();
    // Initialize request argument(s)
    ListConnectionsRequest request = new ListConnectionsRequest
    {
        ParentAsEndpointName = EndpointName.FromProjectEndpoint("[PROJECT]", "[ENDPOINT]"),
    };
    // Make the request
    PagedAsyncEnumerable<ListConnectionsResponse, Connection> response = connectionServiceClient.ListConnectionsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Connection item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListConnectionsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Connection item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Connection> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Connection item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListConnectionsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListConnectionsResponse, Connection> ListConnectionsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists connections that are currently active for the given Apigee Connect endpoint.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Parent name of the form: `projects/{project_number or project_id}/endpoints/{endpoint}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListConnectionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.ListConnectionsResponse)[Connection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.Connection)` | A pageable asynchronous sequence of [Connection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.Connection) resources.  
**Example**
    
    
    // Create client
    ConnectionServiceClient connectionServiceClient = await ConnectionServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/endpoints/[ENDPOINT]";
    // Make the request
    PagedAsyncEnumerable<ListConnectionsResponse, Connection> response = connectionServiceClient.ListConnectionsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Connection item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListConnectionsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Connection item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Connection> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Connection item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.ConnectionServiceClient#Google_Cloud_ApigeeConnect_V1_ConnectionServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.ConnectionServiceClient#Google_Cloud_ApigeeConnect_V1_ConnectionServiceClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.ConnectionServiceClient#Google_Cloud_ApigeeConnect_V1_ConnectionServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.ConnectionServiceClient#Google_Cloud_ApigeeConnect_V1_ConnectionServiceClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
