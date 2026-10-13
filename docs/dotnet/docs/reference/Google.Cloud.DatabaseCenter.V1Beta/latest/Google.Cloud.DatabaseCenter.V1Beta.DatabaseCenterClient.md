---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenterClient
title: Database Center v1beta API - Class DatabaseCenterClient (1.0.0-beta08) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:34:53.406488+00:00
---

# Database Center v1beta API - Class DatabaseCenterClient (1.0.0-beta08)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenterClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Database Center v1beta API - Class DatabaseCenterClient (1.0.0-beta08) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta08 (latest)  1.0.0-beta07 
    
    
    public abstract class DatabaseCenterClient

Reference documentation and code samples for the Database Center v1beta API class DatabaseCenterClient.

DatabaseCenter client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DatabaseCenterClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[DatabaseCenterClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenterClientImpl)

## Namespace

[Google.Cloud.DatabaseCenter.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta)

## Assembly

Google.Cloud.DatabaseCenter.V1Beta.dll

## Remarks

DatabaseCenter contains methods to query fleet view for database resources.

## Properties 

### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the DatabaseCenter service, which is a host of "databasecenter.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default DatabaseCenter scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default DatabaseCenter scopes are:

  * <https://www.googleapis.com/auth/cloud-platform>



### GrpcClient
    
    
    public virtual DatabaseCenter.DatabaseCenterClient GrpcClient { get; }

The underlying gRPC DatabaseCenter client

**Property Value**  
---  
**Type** | **Description**  
`[DatabaseCenter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenter)[DatabaseCenterClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenter.DatabaseCenterClient)` |   
  
### ServiceMetadata
    
    
    public static ServiceMetadata ServiceMetadata { get; }

The service metadata associated with this client type.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceMetadata](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceMetadata.html)` |   
  
## Methods 

### AggregateFleet(AggregateFleetRequest, CallSettings)
    
    
    public virtual PagedEnumerable<AggregateFleetResponse, AggregateFleetRow> AggregateFleet(AggregateFleetRequest request, CallSettings callSettings = null)

AggregateFleet provides statistics about the fleet grouped by various fields.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AggregateFleetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateFleetRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[AggregateFleetResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateFleetResponse)[AggregateFleetRow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateFleetRow)` | A pageable sequence of [AggregateFleetRow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateFleetRow) resources.  
**Example**
    
    
    // Create client
    DatabaseCenterClient databaseCenterClient = DatabaseCenterClient.Create();
    // Initialize request argument(s)
    AggregateFleetRequest request = new AggregateFleetRequest
    {
        Parent = "",
        Filter = "",
        GroupBy = "",
        OrderBy = "",
        BaselineDate = new Date(),
    };
    // Make the request
    PagedEnumerable<AggregateFleetResponse, AggregateFleetRow> response = databaseCenterClient.AggregateFleet(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (AggregateFleetRow item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (AggregateFleetResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (AggregateFleetRow item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<AggregateFleetRow> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (AggregateFleetRow item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### AggregateFleetAsync(AggregateFleetRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<AggregateFleetResponse, AggregateFleetRow> AggregateFleetAsync(AggregateFleetRequest request, CallSettings callSettings = null)

AggregateFleet provides statistics about the fleet grouped by various fields.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AggregateFleetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateFleetRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[AggregateFleetResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateFleetResponse)[AggregateFleetRow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateFleetRow)` | A pageable asynchronous sequence of [AggregateFleetRow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateFleetRow) resources.  
**Example**
    
    
    // Create client
    DatabaseCenterClient databaseCenterClient = await DatabaseCenterClient.CreateAsync();
    // Initialize request argument(s)
    AggregateFleetRequest request = new AggregateFleetRequest
    {
        Parent = "",
        Filter = "",
        GroupBy = "",
        OrderBy = "",
        BaselineDate = new Date(),
    };
    // Make the request
    PagedAsyncEnumerable<AggregateFleetResponse, AggregateFleetRow> response = databaseCenterClient.AggregateFleetAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (AggregateFleetRow item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (AggregateFleetResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (AggregateFleetRow item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<AggregateFleetRow> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (AggregateFleetRow item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### AggregateIssueStats(AggregateIssueStatsRequest, CallSettings)
    
    
    public virtual AggregateIssueStatsResponse AggregateIssueStats(AggregateIssueStatsRequest request, CallSettings callSettings = null)

AggregateIssueStats provides database resource issues statistics.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AggregateIssueStatsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateIssueStatsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[AggregateIssueStatsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateIssueStatsResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    DatabaseCenterClient databaseCenterClient = DatabaseCenterClient.Create();
    // Initialize request argument(s)
    AggregateIssueStatsRequest request = new AggregateIssueStatsRequest
    {
        Parent = "",
        Filter = "",
        SignalTypeGroups =
        {
            new SignalTypeGroup(),
        },
        BaselineDate = new Date(),
    };
    // Make the request
    AggregateIssueStatsResponse response = databaseCenterClient.AggregateIssueStats(request);
    

### AggregateIssueStatsAsync(AggregateIssueStatsRequest, CallSettings)
    
    
    public virtual Task<AggregateIssueStatsResponse> AggregateIssueStatsAsync(AggregateIssueStatsRequest request, CallSettings callSettings = null)

AggregateIssueStats provides database resource issues statistics.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AggregateIssueStatsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateIssueStatsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AggregateIssueStatsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateIssueStatsResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatabaseCenterClient databaseCenterClient = await DatabaseCenterClient.CreateAsync();
    // Initialize request argument(s)
    AggregateIssueStatsRequest request = new AggregateIssueStatsRequest
    {
        Parent = "",
        Filter = "",
        SignalTypeGroups =
        {
            new SignalTypeGroup(),
        },
        BaselineDate = new Date(),
    };
    // Make the request
    AggregateIssueStatsResponse response = await databaseCenterClient.AggregateIssueStatsAsync(request);
    

### AggregateIssueStatsAsync(AggregateIssueStatsRequest, CancellationToken)
    
    
    public virtual Task<AggregateIssueStatsResponse> AggregateIssueStatsAsync(AggregateIssueStatsRequest request, CancellationToken cancellationToken)

AggregateIssueStats provides database resource issues statistics.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AggregateIssueStatsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateIssueStatsRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AggregateIssueStatsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateIssueStatsResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DatabaseCenterClient databaseCenterClient = await DatabaseCenterClient.CreateAsync();
    // Initialize request argument(s)
    AggregateIssueStatsRequest request = new AggregateIssueStatsRequest
    {
        Parent = "",
        Filter = "",
        SignalTypeGroups =
        {
            new SignalTypeGroup(),
        },
        BaselineDate = new Date(),
    };
    // Make the request
    AggregateIssueStatsResponse response = await databaseCenterClient.AggregateIssueStatsAsync(request);
    

### AggregateQueryStats(AggregateQueryStatsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<AggregateQueryStatsResponse, QueryStatsInfo> AggregateQueryStats(AggregateQueryStatsRequest request, CallSettings callSettings = null)

AggregateQueryStats provides database resource query execution statistics.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AggregateQueryStatsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateQueryStatsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[AggregateQueryStatsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateQueryStatsResponse)[QueryStatsInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryStatsInfo)` | A pageable sequence of [QueryStatsInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryStatsInfo) resources.  
**Example**
    
    
    // Create client
    DatabaseCenterClient databaseCenterClient = DatabaseCenterClient.Create();
    // Initialize request argument(s)
    AggregateQueryStatsRequest request = new AggregateQueryStatsRequest
    {
        Parent = "",
        OrderBy = "",
        Filter = "",
    };
    // Make the request
    PagedEnumerable<AggregateQueryStatsResponse, QueryStatsInfo> response = databaseCenterClient.AggregateQueryStats(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (QueryStatsInfo item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (AggregateQueryStatsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (QueryStatsInfo item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<QueryStatsInfo> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (QueryStatsInfo item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### AggregateQueryStatsAsync(AggregateQueryStatsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<AggregateQueryStatsResponse, QueryStatsInfo> AggregateQueryStatsAsync(AggregateQueryStatsRequest request, CallSettings callSettings = null)

AggregateQueryStats provides database resource query execution statistics.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AggregateQueryStatsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateQueryStatsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[AggregateQueryStatsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateQueryStatsResponse)[QueryStatsInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryStatsInfo)` | A pageable asynchronous sequence of [QueryStatsInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryStatsInfo) resources.  
**Example**
    
    
    // Create client
    DatabaseCenterClient databaseCenterClient = await DatabaseCenterClient.CreateAsync();
    // Initialize request argument(s)
    AggregateQueryStatsRequest request = new AggregateQueryStatsRequest
    {
        Parent = "",
        OrderBy = "",
        Filter = "",
    };
    // Make the request
    PagedAsyncEnumerable<AggregateQueryStatsResponse, QueryStatsInfo> response = databaseCenterClient.AggregateQueryStatsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (QueryStatsInfo item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (AggregateQueryStatsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (QueryStatsInfo item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<QueryStatsInfo> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (QueryStatsInfo item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### Create()
    
    
    public static DatabaseCenterClient Create()

Synchronously creates a [DatabaseCenterClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenterClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [DatabaseCenterClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenterClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[DatabaseCenterClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenterClient)` | The created [DatabaseCenterClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenterClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<DatabaseCenterClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [DatabaseCenterClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenterClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [DatabaseCenterClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenterClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DatabaseCenterClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenterClient)` | The task representing the created [DatabaseCenterClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenterClient).  
  
### QueryDatabaseResourceGroups(QueryDatabaseResourceGroupsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<QueryDatabaseResourceGroupsResponse, DatabaseResourceGroup> QueryDatabaseResourceGroups(QueryDatabaseResourceGroupsRequest request, CallSettings callSettings = null)

QueryDatabaseResourceGroups returns paginated results of database groups.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryDatabaseResourceGroupsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryDatabaseResourceGroupsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[QueryDatabaseResourceGroupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryDatabaseResourceGroupsResponse)[DatabaseResourceGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseResourceGroup)` | A pageable sequence of [DatabaseResourceGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseResourceGroup) resources.  
**Example**
    
    
    // Create client
    DatabaseCenterClient databaseCenterClient = DatabaseCenterClient.Create();
    // Initialize request argument(s)
    QueryDatabaseResourceGroupsRequest request = new QueryDatabaseResourceGroupsRequest
    {
        Parent = "",
        Filter = "",
        SignalTypeGroups =
        {
            new SignalTypeGroup(),
        },
        SignalFilters = { new SignalFilter(), },
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<QueryDatabaseResourceGroupsResponse, DatabaseResourceGroup> response = databaseCenterClient.QueryDatabaseResourceGroups(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (DatabaseResourceGroup item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (QueryDatabaseResourceGroupsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (DatabaseResourceGroup item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<DatabaseResourceGroup> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (DatabaseResourceGroup item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### QueryDatabaseResourceGroupsAsync(QueryDatabaseResourceGroupsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<QueryDatabaseResourceGroupsResponse, DatabaseResourceGroup> QueryDatabaseResourceGroupsAsync(QueryDatabaseResourceGroupsRequest request, CallSettings callSettings = null)

QueryDatabaseResourceGroups returns paginated results of database groups.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryDatabaseResourceGroupsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryDatabaseResourceGroupsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[QueryDatabaseResourceGroupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryDatabaseResourceGroupsResponse)[DatabaseResourceGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseResourceGroup)` | A pageable asynchronous sequence of [DatabaseResourceGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseResourceGroup) resources.  
**Example**
    
    
    // Create client
    DatabaseCenterClient databaseCenterClient = await DatabaseCenterClient.CreateAsync();
    // Initialize request argument(s)
    QueryDatabaseResourceGroupsRequest request = new QueryDatabaseResourceGroupsRequest
    {
        Parent = "",
        Filter = "",
        SignalTypeGroups =
        {
            new SignalTypeGroup(),
        },
        SignalFilters = { new SignalFilter(), },
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<QueryDatabaseResourceGroupsResponse, DatabaseResourceGroup> response = databaseCenterClient.QueryDatabaseResourceGroupsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (DatabaseResourceGroup item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (QueryDatabaseResourceGroupsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (DatabaseResourceGroup item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<DatabaseResourceGroup> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (DatabaseResourceGroup item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### QueryIssues(QueryIssuesRequest, CallSettings)
    
    
    public virtual PagedEnumerable<QueryIssuesResponse, DatabaseResourceIssue> QueryIssues(QueryIssuesRequest request, CallSettings callSettings = null)

QueryIssues provides a list of issues and recommendations that a user has access to and that are within the requested scope.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryIssuesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryIssuesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[QueryIssuesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryIssuesResponse)[DatabaseResourceIssue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseResourceIssue)` | A pageable sequence of [DatabaseResourceIssue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseResourceIssue) resources.  
**Example**
    
    
    // Create client
    DatabaseCenterClient databaseCenterClient = DatabaseCenterClient.Create();
    // Initialize request argument(s)
    QueryIssuesRequest request = new QueryIssuesRequest
    {
        Parent = "",
        Filter = "",
        SignalProductsFilters =
        {
            new SignalProductsFilters(),
        },
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<QueryIssuesResponse, DatabaseResourceIssue> response = databaseCenterClient.QueryIssues(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (DatabaseResourceIssue item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (QueryIssuesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (DatabaseResourceIssue item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<DatabaseResourceIssue> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (DatabaseResourceIssue item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### QueryIssues(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<QueryIssuesResponse, DatabaseResourceIssue> QueryIssues(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

QueryIssues provides a list of issues and recommendations that a user has access to and that are within the requested scope.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Parent can be a project, a folder, or an organization. The list is limited to the one attached to resources within the `scope` that a user has access to. The allowed values are:

  * projects/{PROJECT_ID} (e.g., "projects/foo-bar")
  * projects/{PROJECT_NUMBER} (e.g., "projects/12345678")
  * folders/{FOLDER_NUMBER} (e.g., "folders/1234567")
  * organizations/{ORGANIZATION_NUMBER} (e.g., "organizations/123456")

  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[QueryIssuesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryIssuesResponse)[DatabaseResourceIssue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseResourceIssue)` | A pageable sequence of [DatabaseResourceIssue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseResourceIssue) resources.  
**Example**
    
    
    // Create client
    DatabaseCenterClient databaseCenterClient = DatabaseCenterClient.Create();
    // Initialize request argument(s)
    string parent = "";
    // Make the request
    PagedEnumerable<QueryIssuesResponse, DatabaseResourceIssue> response = databaseCenterClient.QueryIssues(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (DatabaseResourceIssue item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (QueryIssuesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (DatabaseResourceIssue item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<DatabaseResourceIssue> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (DatabaseResourceIssue item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### QueryIssuesAsync(QueryIssuesRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<QueryIssuesResponse, DatabaseResourceIssue> QueryIssuesAsync(QueryIssuesRequest request, CallSettings callSettings = null)

QueryIssues provides a list of issues and recommendations that a user has access to and that are within the requested scope.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryIssuesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryIssuesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[QueryIssuesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryIssuesResponse)[DatabaseResourceIssue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseResourceIssue)` | A pageable asynchronous sequence of [DatabaseResourceIssue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseResourceIssue) resources.  
**Example**
    
    
    // Create client
    DatabaseCenterClient databaseCenterClient = await DatabaseCenterClient.CreateAsync();
    // Initialize request argument(s)
    QueryIssuesRequest request = new QueryIssuesRequest
    {
        Parent = "",
        Filter = "",
        SignalProductsFilters =
        {
            new SignalProductsFilters(),
        },
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<QueryIssuesResponse, DatabaseResourceIssue> response = databaseCenterClient.QueryIssuesAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (DatabaseResourceIssue item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (QueryIssuesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (DatabaseResourceIssue item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<DatabaseResourceIssue> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (DatabaseResourceIssue item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### QueryIssuesAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<QueryIssuesResponse, DatabaseResourceIssue> QueryIssuesAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

QueryIssues provides a list of issues and recommendations that a user has access to and that are within the requested scope.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Parent can be a project, a folder, or an organization. The list is limited to the one attached to resources within the `scope` that a user has access to. The allowed values are:

  * projects/{PROJECT_ID} (e.g., "projects/foo-bar")
  * projects/{PROJECT_NUMBER} (e.g., "projects/12345678")
  * folders/{FOLDER_NUMBER} (e.g., "folders/1234567")
  * organizations/{ORGANIZATION_NUMBER} (e.g., "organizations/123456")

  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[QueryIssuesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryIssuesResponse)[DatabaseResourceIssue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseResourceIssue)` | A pageable asynchronous sequence of [DatabaseResourceIssue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseResourceIssue) resources.  
**Example**
    
    
    // Create client
    DatabaseCenterClient databaseCenterClient = await DatabaseCenterClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "";
    // Make the request
    PagedAsyncEnumerable<QueryIssuesResponse, DatabaseResourceIssue> response = databaseCenterClient.QueryIssuesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (DatabaseResourceIssue item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (QueryIssuesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (DatabaseResourceIssue item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<DatabaseResourceIssue> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (DatabaseResourceIssue item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### QueryProducts(QueryProductsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<QueryProductsResponse, Product> QueryProducts(QueryProductsRequest request, CallSettings callSettings = null)

QueryProducts provides a list of all possible products which can be used to filter database resources.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryProductsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryProductsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[QueryProductsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryProductsResponse)[Product](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.Product)` | A pageable sequence of [Product](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.Product) resources.  
**Example**
    
    
    // Create client
    DatabaseCenterClient databaseCenterClient = DatabaseCenterClient.Create();
    // Initialize request argument(s)
    QueryProductsRequest request = new QueryProductsRequest { Parent = "", };
    // Make the request
    PagedEnumerable<QueryProductsResponse, Product> response = databaseCenterClient.QueryProducts(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Product item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (QueryProductsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Product item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Product> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Product item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### QueryProductsAsync(QueryProductsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<QueryProductsResponse, Product> QueryProductsAsync(QueryProductsRequest request, CallSettings callSettings = null)

QueryProducts provides a list of all possible products which can be used to filter database resources.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryProductsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryProductsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[QueryProductsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryProductsResponse)[Product](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.Product)` | A pageable asynchronous sequence of [Product](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.Product) resources.  
**Example**
    
    
    // Create client
    DatabaseCenterClient databaseCenterClient = await DatabaseCenterClient.CreateAsync();
    // Initialize request argument(s)
    QueryProductsRequest request = new QueryProductsRequest { Parent = "", };
    // Make the request
    PagedAsyncEnumerable<QueryProductsResponse, Product> response = databaseCenterClient.QueryProductsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Product item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (QueryProductsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Product item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Product> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Product item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenterClient#Google_Cloud_DatabaseCenter_V1Beta_DatabaseCenterClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenterClient#Google_Cloud_DatabaseCenter_V1Beta_DatabaseCenterClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenterClient#Google_Cloud_DatabaseCenter_V1Beta_DatabaseCenterClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseCenterClient#Google_Cloud_DatabaseCenter_V1Beta_DatabaseCenterClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-30 UTC."],[],[]] 
