---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageClient
title: Data Lineage v1 API - Class LineageClient (1.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:35.236460+00:00
---

# Data Lineage v1 API - Class LineageClient (1.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Data Lineage v1 API - Class LineageClient (1.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.6.0 (latest)  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public abstract class LineageClient

Reference documentation and code samples for the Data Lineage v1 API class LineageClient.

Lineage client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > LineageClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[LineageClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageClientImpl)

## Namespace

[Google.Cloud.DataCatalog.Lineage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1)

## Assembly

Google.Cloud.DataCatalog.Lineage.V1.dll

## Remarks

Lineage is used to track data flows between assets over time. You can create [LineageEvents][google.cloud.datacatalog.lineage.v1.LineageEvent] to record lineage between multiple sources and a single target, for example, when table data is based on data from multiple tables.

## Properties 

### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the Lineage service, which is a host of "datalineage.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default Lineage scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default Lineage scopes are:

  * <https://www.googleapis.com/auth/cloud-platform>



### DeleteProcessOperationsClient
    
    
    public virtual OperationsClient DeleteProcessOperationsClient { get; }

The long-running operations client for `DeleteProcess`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DeleteRunOperationsClient
    
    
    public virtual OperationsClient DeleteRunOperationsClient { get; }

The long-running operations client for `DeleteRun`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### GrpcClient
    
    
    public virtual Lineage.LineageClient GrpcClient { get; }

The underlying gRPC Lineage client

**Property Value**  
---  
**Type** | **Description**  
`[Lineage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Lineage)[LineageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Lineage.LineageClient)` |   
  
### ServiceMetadata
    
    
    public static ServiceMetadata ServiceMetadata { get; }

The service metadata associated with this client type.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceMetadata](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceMetadata.html)` |   
  
## Methods 

### BatchSearchLinkProcesses(BatchSearchLinkProcessesRequest, CallSettings)
    
    
    public virtual PagedEnumerable<BatchSearchLinkProcessesResponse, ProcessLinks> BatchSearchLinkProcesses(BatchSearchLinkProcessesRequest request, CallSettings callSettings = null)

Retrieve information about LineageProcesses associated with specific links. LineageProcesses are transformation pipelines that result in data flowing from **source** to **target** assets. Links between assets represent this operation.

If you have specific link names, you can use this method to verify which LineageProcesses contribute to creating those links. See the [SearchLinks][google.cloud.datacatalog.lineage.v1.Lineage.SearchLinks] method for more information on how to retrieve link name.

You can retrieve the LineageProcess information in every project where you have the `datalineage.events.get` permission. The project provided in the URL is used for Billing and Quota.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchSearchLinkProcessesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.BatchSearchLinkProcessesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[BatchSearchLinkProcessesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.BatchSearchLinkProcessesResponse)[ProcessLinks](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ProcessLinks)` | A pageable sequence of [ProcessLinks](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ProcessLinks) resources.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = LineageClient.Create();
    // Initialize request argument(s)
    BatchSearchLinkProcessesRequest request = new BatchSearchLinkProcessesRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Links = { "", },
    };
    // Make the request
    PagedEnumerable<BatchSearchLinkProcessesResponse, ProcessLinks> response = lineageClient.BatchSearchLinkProcesses(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (ProcessLinks item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (BatchSearchLinkProcessesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ProcessLinks item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ProcessLinks> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ProcessLinks item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### BatchSearchLinkProcessesAsync(BatchSearchLinkProcessesRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<BatchSearchLinkProcessesResponse, ProcessLinks> BatchSearchLinkProcessesAsync(BatchSearchLinkProcessesRequest request, CallSettings callSettings = null)

Retrieve information about LineageProcesses associated with specific links. LineageProcesses are transformation pipelines that result in data flowing from **source** to **target** assets. Links between assets represent this operation.

If you have specific link names, you can use this method to verify which LineageProcesses contribute to creating those links. See the [SearchLinks][google.cloud.datacatalog.lineage.v1.Lineage.SearchLinks] method for more information on how to retrieve link name.

You can retrieve the LineageProcess information in every project where you have the `datalineage.events.get` permission. The project provided in the URL is used for Billing and Quota.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchSearchLinkProcessesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.BatchSearchLinkProcessesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[BatchSearchLinkProcessesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.BatchSearchLinkProcessesResponse)[ProcessLinks](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ProcessLinks)` | A pageable asynchronous sequence of [ProcessLinks](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ProcessLinks) resources.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    BatchSearchLinkProcessesRequest request = new BatchSearchLinkProcessesRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Links = { "", },
    };
    // Make the request
    PagedAsyncEnumerable<BatchSearchLinkProcessesResponse, ProcessLinks> response = lineageClient.BatchSearchLinkProcessesAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (ProcessLinks item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (BatchSearchLinkProcessesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ProcessLinks item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ProcessLinks> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ProcessLinks item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### Create()
    
    
    public static LineageClient Create()

Synchronously creates a [LineageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [LineageClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[LineageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageClient)` | The created [LineageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<LineageClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [LineageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [LineageClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[LineageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageClient)` | The task representing the created [LineageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageClient).  
  
### CreateLineageEvent(CreateLineageEventRequest, CallSettings)
    
    
    public virtual LineageEvent CreateLineageEvent(CreateLineageEventRequest request, CallSettings callSettings = null)

Creates a new lineage event.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateLineageEventRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.CreateLineageEventRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[LineageEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageEvent)` | The RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = LineageClient.Create();
    // Initialize request argument(s)
    CreateLineageEventRequest request = new CreateLineageEventRequest
    {
        ParentAsRunName = RunName.FromProjectLocationProcessRun("[PROJECT]", "[LOCATION]", "[PROCESS]", "[RUN]"),
        LineageEvent = new LineageEvent(),
    };
    // Make the request
    LineageEvent response = lineageClient.CreateLineageEvent(request);
    

### CreateLineageEvent(RunName, LineageEvent, CallSettings)
    
    
    public virtual LineageEvent CreateLineageEvent(RunName parent, LineageEvent lineageEvent, CallSettings callSettings = null)

Creates a new lineage event.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[RunName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.RunName)`  
Required. The name of the run that should own the lineage event.  
`lineageEvent` | `[LineageEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageEvent)`  
Required. The lineage event to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[LineageEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageEvent)` | The RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = LineageClient.Create();
    // Initialize request argument(s)
    RunName parent = RunName.FromProjectLocationProcessRun("[PROJECT]", "[LOCATION]", "[PROCESS]", "[RUN]");
    LineageEvent lineageEvent = new LineageEvent();
    // Make the request
    LineageEvent response = lineageClient.CreateLineageEvent(parent, lineageEvent);
    

### CreateLineageEvent(string, LineageEvent, CallSettings)
    
    
    public virtual LineageEvent CreateLineageEvent(string parent, LineageEvent lineageEvent, CallSettings callSettings = null)

Creates a new lineage event.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the run that should own the lineage event.  
`lineageEvent` | `[LineageEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageEvent)`  
Required. The lineage event to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[LineageEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageEvent)` | The RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = LineageClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/processes/[PROCESS]/runs/[RUN]";
    LineageEvent lineageEvent = new LineageEvent();
    // Make the request
    LineageEvent response = lineageClient.CreateLineageEvent(parent, lineageEvent);
    

### CreateLineageEventAsync(CreateLineageEventRequest, CallSettings)
    
    
    public virtual Task<LineageEvent> CreateLineageEventAsync(CreateLineageEventRequest request, CallSettings callSettings = null)

Creates a new lineage event.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateLineageEventRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.CreateLineageEventRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[LineageEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageEvent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    CreateLineageEventRequest request = new CreateLineageEventRequest
    {
        ParentAsRunName = RunName.FromProjectLocationProcessRun("[PROJECT]", "[LOCATION]", "[PROCESS]", "[RUN]"),
        LineageEvent = new LineageEvent(),
    };
    // Make the request
    LineageEvent response = await lineageClient.CreateLineageEventAsync(request);
    

### CreateLineageEventAsync(CreateLineageEventRequest, CancellationToken)
    
    
    public virtual Task<LineageEvent> CreateLineageEventAsync(CreateLineageEventRequest request, CancellationToken cancellationToken)

Creates a new lineage event.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateLineageEventRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.CreateLineageEventRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[LineageEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageEvent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    CreateLineageEventRequest request = new CreateLineageEventRequest
    {
        ParentAsRunName = RunName.FromProjectLocationProcessRun("[PROJECT]", "[LOCATION]", "[PROCESS]", "[RUN]"),
        LineageEvent = new LineageEvent(),
    };
    // Make the request
    LineageEvent response = await lineageClient.CreateLineageEventAsync(request);
    

### CreateLineageEventAsync(RunName, LineageEvent, CallSettings)
    
    
    public virtual Task<LineageEvent> CreateLineageEventAsync(RunName parent, LineageEvent lineageEvent, CallSettings callSettings = null)

Creates a new lineage event.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[RunName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.RunName)`  
Required. The name of the run that should own the lineage event.  
`lineageEvent` | `[LineageEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageEvent)`  
Required. The lineage event to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[LineageEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageEvent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    RunName parent = RunName.FromProjectLocationProcessRun("[PROJECT]", "[LOCATION]", "[PROCESS]", "[RUN]");
    LineageEvent lineageEvent = new LineageEvent();
    // Make the request
    LineageEvent response = await lineageClient.CreateLineageEventAsync(parent, lineageEvent);
    

### CreateLineageEventAsync(RunName, LineageEvent, CancellationToken)
    
    
    public virtual Task<LineageEvent> CreateLineageEventAsync(RunName parent, LineageEvent lineageEvent, CancellationToken cancellationToken)

Creates a new lineage event.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[RunName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.RunName)`  
Required. The name of the run that should own the lineage event.  
`lineageEvent` | `[LineageEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageEvent)`  
Required. The lineage event to create.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[LineageEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageEvent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    RunName parent = RunName.FromProjectLocationProcessRun("[PROJECT]", "[LOCATION]", "[PROCESS]", "[RUN]");
    LineageEvent lineageEvent = new LineageEvent();
    // Make the request
    LineageEvent response = await lineageClient.CreateLineageEventAsync(parent, lineageEvent);
    

### CreateLineageEventAsync(string, LineageEvent, CallSettings)
    
    
    public virtual Task<LineageEvent> CreateLineageEventAsync(string parent, LineageEvent lineageEvent, CallSettings callSettings = null)

Creates a new lineage event.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the run that should own the lineage event.  
`lineageEvent` | `[LineageEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageEvent)`  
Required. The lineage event to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[LineageEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageEvent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/processes/[PROCESS]/runs/[RUN]";
    LineageEvent lineageEvent = new LineageEvent();
    // Make the request
    LineageEvent response = await lineageClient.CreateLineageEventAsync(parent, lineageEvent);
    

### CreateLineageEventAsync(string, LineageEvent, CancellationToken)
    
    
    public virtual Task<LineageEvent> CreateLineageEventAsync(string parent, LineageEvent lineageEvent, CancellationToken cancellationToken)

Creates a new lineage event.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the run that should own the lineage event.  
`lineageEvent` | `[LineageEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageEvent)`  
Required. The lineage event to create.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[LineageEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageEvent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/processes/[PROCESS]/runs/[RUN]";
    LineageEvent lineageEvent = new LineageEvent();
    // Make the request
    LineageEvent response = await lineageClient.CreateLineageEventAsync(parent, lineageEvent);
    

### CreateProcess(LocationName, Process, CallSettings)
    
    
    public virtual Process CreateProcess(LocationName parent, Process process, CallSettings callSettings = null)

Creates a new process.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The name of the project and its location that should own the process.  
`process` | `[Process](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Process)`  
Required. The process to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Process](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Process)` | The RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = LineageClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Process process = new Process();
    // Make the request
    Process response = lineageClient.CreateProcess(parent, process);
    

### CreateProcess(CreateProcessRequest, CallSettings)
    
    
    public virtual Process CreateProcess(CreateProcessRequest request, CallSettings callSettings = null)

Creates a new process.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateProcessRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.CreateProcessRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Process](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Process)` | The RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = LineageClient.Create();
    // Initialize request argument(s)
    CreateProcessRequest request = new CreateProcessRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Process = new Process(),
    };
    // Make the request
    Process response = lineageClient.CreateProcess(request);
    

### CreateProcess(string, Process, CallSettings)
    
    
    public virtual Process CreateProcess(string parent, Process process, CallSettings callSettings = null)

Creates a new process.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the project and its location that should own the process.  
`process` | `[Process](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Process)`  
Required. The process to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Process](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Process)` | The RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = LineageClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Process process = new Process();
    // Make the request
    Process response = lineageClient.CreateProcess(parent, process);
    

### CreateProcessAsync(LocationName, Process, CallSettings)
    
    
    public virtual Task<Process> CreateProcessAsync(LocationName parent, Process process, CallSettings callSettings = null)

Creates a new process.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The name of the project and its location that should own the process.  
`process` | `[Process](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Process)`  
Required. The process to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Process](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Process)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Process process = new Process();
    // Make the request
    Process response = await lineageClient.CreateProcessAsync(parent, process);
    

### CreateProcessAsync(LocationName, Process, CancellationToken)
    
    
    public virtual Task<Process> CreateProcessAsync(LocationName parent, Process process, CancellationToken cancellationToken)

Creates a new process.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The name of the project and its location that should own the process.  
`process` | `[Process](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Process)`  
Required. The process to create.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Process](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Process)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Process process = new Process();
    // Make the request
    Process response = await lineageClient.CreateProcessAsync(parent, process);
    

### CreateProcessAsync(CreateProcessRequest, CallSettings)
    
    
    public virtual Task<Process> CreateProcessAsync(CreateProcessRequest request, CallSettings callSettings = null)

Creates a new process.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateProcessRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.CreateProcessRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Process](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Process)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    CreateProcessRequest request = new CreateProcessRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Process = new Process(),
    };
    // Make the request
    Process response = await lineageClient.CreateProcessAsync(request);
    

### CreateProcessAsync(CreateProcessRequest, CancellationToken)
    
    
    public virtual Task<Process> CreateProcessAsync(CreateProcessRequest request, CancellationToken cancellationToken)

Creates a new process.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateProcessRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.CreateProcessRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Process](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Process)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    CreateProcessRequest request = new CreateProcessRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Process = new Process(),
    };
    // Make the request
    Process response = await lineageClient.CreateProcessAsync(request);
    

### CreateProcessAsync(string, Process, CallSettings)
    
    
    public virtual Task<Process> CreateProcessAsync(string parent, Process process, CallSettings callSettings = null)

Creates a new process.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the project and its location that should own the process.  
`process` | `[Process](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Process)`  
Required. The process to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Process](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Process)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Process process = new Process();
    // Make the request
    Process response = await lineageClient.CreateProcessAsync(parent, process);
    

### CreateProcessAsync(string, Process, CancellationToken)
    
    
    public virtual Task<Process> CreateProcessAsync(string parent, Process process, CancellationToken cancellationToken)

Creates a new process.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the project and its location that should own the process.  
`process` | `[Process](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Process)`  
Required. The process to create.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Process](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Process)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Process process = new Process();
    // Make the request
    Process response = await lineageClient.CreateProcessAsync(parent, process);
    

### CreateRun(CreateRunRequest, CallSettings)
    
    
    public virtual Run CreateRun(CreateRunRequest request, CallSettings callSettings = null)

Creates a new run.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateRunRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.CreateRunRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Run](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Run)` | The RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = LineageClient.Create();
    // Initialize request argument(s)
    CreateRunRequest request = new CreateRunRequest
    {
        ParentAsProcessName = ProcessName.FromProjectLocationProcess("[PROJECT]", "[LOCATION]", "[PROCESS]"),
        Run = new Run(),
    };
    // Make the request
    Run response = lineageClient.CreateRun(request);
    

### CreateRun(ProcessName, Run, CallSettings)
    
    
    public virtual Run CreateRun(ProcessName parent, Run run, CallSettings callSettings = null)

Creates a new run.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ProcessName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ProcessName)`  
Required. The name of the process that should own the run.  
`run` | `[Run](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Run)`  
Required. The run to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Run](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Run)` | The RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = LineageClient.Create();
    // Initialize request argument(s)
    ProcessName parent = ProcessName.FromProjectLocationProcess("[PROJECT]", "[LOCATION]", "[PROCESS]");
    Run run = new Run();
    // Make the request
    Run response = lineageClient.CreateRun(parent, run);
    

### CreateRun(string, Run, CallSettings)
    
    
    public virtual Run CreateRun(string parent, Run run, CallSettings callSettings = null)

Creates a new run.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the process that should own the run.  
`run` | `[Run](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Run)`  
Required. The run to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Run](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Run)` | The RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = LineageClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/processes/[PROCESS]";
    Run run = new Run();
    // Make the request
    Run response = lineageClient.CreateRun(parent, run);
    

### CreateRunAsync(CreateRunRequest, CallSettings)
    
    
    public virtual Task<Run> CreateRunAsync(CreateRunRequest request, CallSettings callSettings = null)

Creates a new run.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateRunRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.CreateRunRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Run](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Run)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    CreateRunRequest request = new CreateRunRequest
    {
        ParentAsProcessName = ProcessName.FromProjectLocationProcess("[PROJECT]", "[LOCATION]", "[PROCESS]"),
        Run = new Run(),
    };
    // Make the request
    Run response = await lineageClient.CreateRunAsync(request);
    

### CreateRunAsync(CreateRunRequest, CancellationToken)
    
    
    public virtual Task<Run> CreateRunAsync(CreateRunRequest request, CancellationToken cancellationToken)

Creates a new run.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateRunRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.CreateRunRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Run](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Run)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    CreateRunRequest request = new CreateRunRequest
    {
        ParentAsProcessName = ProcessName.FromProjectLocationProcess("[PROJECT]", "[LOCATION]", "[PROCESS]"),
        Run = new Run(),
    };
    // Make the request
    Run response = await lineageClient.CreateRunAsync(request);
    

### CreateRunAsync(ProcessName, Run, CallSettings)
    
    
    public virtual Task<Run> CreateRunAsync(ProcessName parent, Run run, CallSettings callSettings = null)

Creates a new run.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ProcessName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ProcessName)`  
Required. The name of the process that should own the run.  
`run` | `[Run](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Run)`  
Required. The run to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Run](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Run)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    ProcessName parent = ProcessName.FromProjectLocationProcess("[PROJECT]", "[LOCATION]", "[PROCESS]");
    Run run = new Run();
    // Make the request
    Run response = await lineageClient.CreateRunAsync(parent, run);
    

### CreateRunAsync(ProcessName, Run, CancellationToken)
    
    
    public virtual Task<Run> CreateRunAsync(ProcessName parent, Run run, CancellationToken cancellationToken)

Creates a new run.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ProcessName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ProcessName)`  
Required. The name of the process that should own the run.  
`run` | `[Run](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Run)`  
Required. The run to create.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Run](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Run)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    ProcessName parent = ProcessName.FromProjectLocationProcess("[PROJECT]", "[LOCATION]", "[PROCESS]");
    Run run = new Run();
    // Make the request
    Run response = await lineageClient.CreateRunAsync(parent, run);
    

### CreateRunAsync(string, Run, CallSettings)
    
    
    public virtual Task<Run> CreateRunAsync(string parent, Run run, CallSettings callSettings = null)

Creates a new run.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the process that should own the run.  
`run` | `[Run](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Run)`  
Required. The run to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Run](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Run)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/processes/[PROCESS]";
    Run run = new Run();
    // Make the request
    Run response = await lineageClient.CreateRunAsync(parent, run);
    

### CreateRunAsync(string, Run, CancellationToken)
    
    
    public virtual Task<Run> CreateRunAsync(string parent, Run run, CancellationToken cancellationToken)

Creates a new run.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the process that should own the run.  
`run` | `[Run](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Run)`  
Required. The run to create.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Run](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Run)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/processes/[PROCESS]";
    Run run = new Run();
    // Make the request
    Run response = await lineageClient.CreateRunAsync(parent, run);
    

### DeleteLineageEvent(DeleteLineageEventRequest, CallSettings)
    
    
    public virtual void DeleteLineageEvent(DeleteLineageEventRequest request, CallSettings callSettings = null)

Deletes the lineage event with the specified name.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteLineageEventRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.DeleteLineageEventRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = LineageClient.Create();
    // Initialize request argument(s)
    DeleteLineageEventRequest request = new DeleteLineageEventRequest
    {
        LineageEventName = LineageEventName.FromProjectLocationProcessRunLineageEvent("[PROJECT]", "[LOCATION]", "[PROCESS]", "[RUN]", "[LINEAGE_EVENT]"),
        AllowMissing = false,
    };
    // Make the request
    lineageClient.DeleteLineageEvent(request);
    

### DeleteLineageEvent(LineageEventName, CallSettings)
    
    
    public virtual void DeleteLineageEvent(LineageEventName name, CallSettings callSettings = null)

Deletes the lineage event with the specified name.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[LineageEventName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageEventName)`  
Required. The name of the lineage event to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = LineageClient.Create();
    // Initialize request argument(s)
    LineageEventName name = LineageEventName.FromProjectLocationProcessRunLineageEvent("[PROJECT]", "[LOCATION]", "[PROCESS]", "[RUN]", "[LINEAGE_EVENT]");
    // Make the request
    lineageClient.DeleteLineageEvent(name);
    

### DeleteLineageEvent(string, CallSettings)
    
    
    public virtual void DeleteLineageEvent(string name, CallSettings callSettings = null)

Deletes the lineage event with the specified name.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the lineage event to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = LineageClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/processes/[PROCESS]/runs/[RUN]/lineageEvents/[LINEAGE_EVENT]";
    // Make the request
    lineageClient.DeleteLineageEvent(name);
    

### DeleteLineageEventAsync(DeleteLineageEventRequest, CallSettings)
    
    
    public virtual Task DeleteLineageEventAsync(DeleteLineageEventRequest request, CallSettings callSettings = null)

Deletes the lineage event with the specified name.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteLineageEventRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.DeleteLineageEventRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    DeleteLineageEventRequest request = new DeleteLineageEventRequest
    {
        LineageEventName = LineageEventName.FromProjectLocationProcessRunLineageEvent("[PROJECT]", "[LOCATION]", "[PROCESS]", "[RUN]", "[LINEAGE_EVENT]"),
        AllowMissing = false,
    };
    // Make the request
    await lineageClient.DeleteLineageEventAsync(request);
    

### DeleteLineageEventAsync(DeleteLineageEventRequest, CancellationToken)
    
    
    public virtual Task DeleteLineageEventAsync(DeleteLineageEventRequest request, CancellationToken cancellationToken)

Deletes the lineage event with the specified name.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteLineageEventRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.DeleteLineageEventRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    DeleteLineageEventRequest request = new DeleteLineageEventRequest
    {
        LineageEventName = LineageEventName.FromProjectLocationProcessRunLineageEvent("[PROJECT]", "[LOCATION]", "[PROCESS]", "[RUN]", "[LINEAGE_EVENT]"),
        AllowMissing = false,
    };
    // Make the request
    await lineageClient.DeleteLineageEventAsync(request);
    

### DeleteLineageEventAsync(LineageEventName, CallSettings)
    
    
    public virtual Task DeleteLineageEventAsync(LineageEventName name, CallSettings callSettings = null)

Deletes the lineage event with the specified name.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[LineageEventName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageEventName)`  
Required. The name of the lineage event to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    LineageEventName name = LineageEventName.FromProjectLocationProcessRunLineageEvent("[PROJECT]", "[LOCATION]", "[PROCESS]", "[RUN]", "[LINEAGE_EVENT]");
    // Make the request
    await lineageClient.DeleteLineageEventAsync(name);
    

### DeleteLineageEventAsync(LineageEventName, CancellationToken)
    
    
    public virtual Task DeleteLineageEventAsync(LineageEventName name, CancellationToken cancellationToken)

Deletes the lineage event with the specified name.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[LineageEventName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageEventName)`  
Required. The name of the lineage event to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    LineageEventName name = LineageEventName.FromProjectLocationProcessRunLineageEvent("[PROJECT]", "[LOCATION]", "[PROCESS]", "[RUN]", "[LINEAGE_EVENT]");
    // Make the request
    await lineageClient.DeleteLineageEventAsync(name);
    

### DeleteLineageEventAsync(string, CallSettings)
    
    
    public virtual Task DeleteLineageEventAsync(string name, CallSettings callSettings = null)

Deletes the lineage event with the specified name.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the lineage event to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/processes/[PROCESS]/runs/[RUN]/lineageEvents/[LINEAGE_EVENT]";
    // Make the request
    await lineageClient.DeleteLineageEventAsync(name);
    

### DeleteLineageEventAsync(string, CancellationToken)
    
    
    public virtual Task DeleteLineageEventAsync(string name, CancellationToken cancellationToken)

Deletes the lineage event with the specified name.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the lineage event to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/processes/[PROCESS]/runs/[RUN]/lineageEvents/[LINEAGE_EVENT]";
    // Make the request
    await lineageClient.DeleteLineageEventAsync(name);
    

### DeleteProcess(DeleteProcessRequest, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteProcess(DeleteProcessRequest request, CallSettings callSettings = null)

Deletes the process with the specified name.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteProcessRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.DeleteProcessRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = LineageClient.Create();
    // Initialize request argument(s)
    DeleteProcessRequest request = new DeleteProcessRequest
    {
        ProcessName = ProcessName.FromProjectLocationProcess("[PROJECT]", "[LOCATION]", "[PROCESS]"),
        AllowMissing = false,
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = lineageClient.DeleteProcess(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = lineageClient.PollOnceDeleteProcess(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteProcess(ProcessName, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteProcess(ProcessName name, CallSettings callSettings = null)

Deletes the process with the specified name.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ProcessName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ProcessName)`  
Required. The name of the process to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = LineageClient.Create();
    // Initialize request argument(s)
    ProcessName name = ProcessName.FromProjectLocationProcess("[PROJECT]", "[LOCATION]", "[PROCESS]");
    // Make the request
    Operation<Empty, OperationMetadata> response = lineageClient.DeleteProcess(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = lineageClient.PollOnceDeleteProcess(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteProcess(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteProcess(string name, CallSettings callSettings = null)

Deletes the process with the specified name.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the process to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = LineageClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/processes/[PROCESS]";
    // Make the request
    Operation<Empty, OperationMetadata> response = lineageClient.DeleteProcess(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = lineageClient.PollOnceDeleteProcess(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteProcessAsync(DeleteProcessRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteProcessAsync(DeleteProcessRequest request, CallSettings callSettings = null)

Deletes the process with the specified name.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteProcessRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.DeleteProcessRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    DeleteProcessRequest request = new DeleteProcessRequest
    {
        ProcessName = ProcessName.FromProjectLocationProcess("[PROJECT]", "[LOCATION]", "[PROCESS]"),
        AllowMissing = false,
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await lineageClient.DeleteProcessAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await lineageClient.PollOnceDeleteProcessAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteProcessAsync(DeleteProcessRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteProcessAsync(DeleteProcessRequest request, CancellationToken cancellationToken)

Deletes the process with the specified name.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteProcessRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.DeleteProcessRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    DeleteProcessRequest request = new DeleteProcessRequest
    {
        ProcessName = ProcessName.FromProjectLocationProcess("[PROJECT]", "[LOCATION]", "[PROCESS]"),
        AllowMissing = false,
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await lineageClient.DeleteProcessAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await lineageClient.PollOnceDeleteProcessAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteProcessAsync(ProcessName, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteProcessAsync(ProcessName name, CallSettings callSettings = null)

Deletes the process with the specified name.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ProcessName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ProcessName)`  
Required. The name of the process to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    ProcessName name = ProcessName.FromProjectLocationProcess("[PROJECT]", "[LOCATION]", "[PROCESS]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await lineageClient.DeleteProcessAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await lineageClient.PollOnceDeleteProcessAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteProcessAsync(ProcessName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteProcessAsync(ProcessName name, CancellationToken cancellationToken)

Deletes the process with the specified name.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ProcessName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ProcessName)`  
Required. The name of the process to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    ProcessName name = ProcessName.FromProjectLocationProcess("[PROJECT]", "[LOCATION]", "[PROCESS]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await lineageClient.DeleteProcessAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await lineageClient.PollOnceDeleteProcessAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteProcessAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteProcessAsync(string name, CallSettings callSettings = null)

Deletes the process with the specified name.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the process to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/processes/[PROCESS]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await lineageClient.DeleteProcessAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await lineageClient.PollOnceDeleteProcessAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteProcessAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteProcessAsync(string name, CancellationToken cancellationToken)

Deletes the process with the specified name.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the process to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/processes/[PROCESS]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await lineageClient.DeleteProcessAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await lineageClient.PollOnceDeleteProcessAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteRun(DeleteRunRequest, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteRun(DeleteRunRequest request, CallSettings callSettings = null)

Deletes the run with the specified name.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteRunRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.DeleteRunRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = LineageClient.Create();
    // Initialize request argument(s)
    DeleteRunRequest request = new DeleteRunRequest
    {
        RunName = RunName.FromProjectLocationProcessRun("[PROJECT]", "[LOCATION]", "[PROCESS]", "[RUN]"),
        AllowMissing = false,
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = lineageClient.DeleteRun(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = lineageClient.PollOnceDeleteRun(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteRun(RunName, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteRun(RunName name, CallSettings callSettings = null)

Deletes the run with the specified name.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[RunName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.RunName)`  
Required. The name of the run to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = LineageClient.Create();
    // Initialize request argument(s)
    RunName name = RunName.FromProjectLocationProcessRun("[PROJECT]", "[LOCATION]", "[PROCESS]", "[RUN]");
    // Make the request
    Operation<Empty, OperationMetadata> response = lineageClient.DeleteRun(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = lineageClient.PollOnceDeleteRun(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteRun(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteRun(string name, CallSettings callSettings = null)

Deletes the run with the specified name.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the run to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = LineageClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/processes/[PROCESS]/runs/[RUN]";
    // Make the request
    Operation<Empty, OperationMetadata> response = lineageClient.DeleteRun(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = lineageClient.PollOnceDeleteRun(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteRunAsync(DeleteRunRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteRunAsync(DeleteRunRequest request, CallSettings callSettings = null)

Deletes the run with the specified name.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteRunRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.DeleteRunRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    DeleteRunRequest request = new DeleteRunRequest
    {
        RunName = RunName.FromProjectLocationProcessRun("[PROJECT]", "[LOCATION]", "[PROCESS]", "[RUN]"),
        AllowMissing = false,
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await lineageClient.DeleteRunAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await lineageClient.PollOnceDeleteRunAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteRunAsync(DeleteRunRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteRunAsync(DeleteRunRequest request, CancellationToken cancellationToken)

Deletes the run with the specified name.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteRunRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.DeleteRunRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    DeleteRunRequest request = new DeleteRunRequest
    {
        RunName = RunName.FromProjectLocationProcessRun("[PROJECT]", "[LOCATION]", "[PROCESS]", "[RUN]"),
        AllowMissing = false,
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await lineageClient.DeleteRunAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await lineageClient.PollOnceDeleteRunAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteRunAsync(RunName, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteRunAsync(RunName name, CallSettings callSettings = null)

Deletes the run with the specified name.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[RunName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.RunName)`  
Required. The name of the run to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    RunName name = RunName.FromProjectLocationProcessRun("[PROJECT]", "[LOCATION]", "[PROCESS]", "[RUN]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await lineageClient.DeleteRunAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await lineageClient.PollOnceDeleteRunAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteRunAsync(RunName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteRunAsync(RunName name, CancellationToken cancellationToken)

Deletes the run with the specified name.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[RunName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.RunName)`  
Required. The name of the run to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    RunName name = RunName.FromProjectLocationProcessRun("[PROJECT]", "[LOCATION]", "[PROCESS]", "[RUN]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await lineageClient.DeleteRunAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await lineageClient.PollOnceDeleteRunAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteRunAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteRunAsync(string name, CallSettings callSettings = null)

Deletes the run with the specified name.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the run to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/processes/[PROCESS]/runs/[RUN]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await lineageClient.DeleteRunAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await lineageClient.PollOnceDeleteRunAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteRunAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteRunAsync(string name, CancellationToken cancellationToken)

Deletes the run with the specified name.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the run to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/processes/[PROCESS]/runs/[RUN]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await lineageClient.DeleteRunAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await lineageClient.PollOnceDeleteRunAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### GetLineageEvent(GetLineageEventRequest, CallSettings)
    
    
    public virtual LineageEvent GetLineageEvent(GetLineageEventRequest request, CallSettings callSettings = null)

Gets details of a specified lineage event.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetLineageEventRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.GetLineageEventRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[LineageEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageEvent)` | The RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = LineageClient.Create();
    // Initialize request argument(s)
    GetLineageEventRequest request = new GetLineageEventRequest
    {
        LineageEventName = LineageEventName.FromProjectLocationProcessRunLineageEvent("[PROJECT]", "[LOCATION]", "[PROCESS]", "[RUN]", "[LINEAGE_EVENT]"),
    };
    // Make the request
    LineageEvent response = lineageClient.GetLineageEvent(request);
    

### GetLineageEvent(LineageEventName, CallSettings)
    
    
    public virtual LineageEvent GetLineageEvent(LineageEventName name, CallSettings callSettings = null)

Gets details of a specified lineage event.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[LineageEventName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageEventName)`  
Required. The name of the lineage event to get.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[LineageEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageEvent)` | The RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = LineageClient.Create();
    // Initialize request argument(s)
    LineageEventName name = LineageEventName.FromProjectLocationProcessRunLineageEvent("[PROJECT]", "[LOCATION]", "[PROCESS]", "[RUN]", "[LINEAGE_EVENT]");
    // Make the request
    LineageEvent response = lineageClient.GetLineageEvent(name);
    

### GetLineageEvent(string, CallSettings)
    
    
    public virtual LineageEvent GetLineageEvent(string name, CallSettings callSettings = null)

Gets details of a specified lineage event.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the lineage event to get.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[LineageEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageEvent)` | The RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = LineageClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/processes/[PROCESS]/runs/[RUN]/lineageEvents/[LINEAGE_EVENT]";
    // Make the request
    LineageEvent response = lineageClient.GetLineageEvent(name);
    

### GetLineageEventAsync(GetLineageEventRequest, CallSettings)
    
    
    public virtual Task<LineageEvent> GetLineageEventAsync(GetLineageEventRequest request, CallSettings callSettings = null)

Gets details of a specified lineage event.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetLineageEventRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.GetLineageEventRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[LineageEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageEvent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    GetLineageEventRequest request = new GetLineageEventRequest
    {
        LineageEventName = LineageEventName.FromProjectLocationProcessRunLineageEvent("[PROJECT]", "[LOCATION]", "[PROCESS]", "[RUN]", "[LINEAGE_EVENT]"),
    };
    // Make the request
    LineageEvent response = await lineageClient.GetLineageEventAsync(request);
    

### GetLineageEventAsync(GetLineageEventRequest, CancellationToken)
    
    
    public virtual Task<LineageEvent> GetLineageEventAsync(GetLineageEventRequest request, CancellationToken cancellationToken)

Gets details of a specified lineage event.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetLineageEventRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.GetLineageEventRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[LineageEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageEvent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    GetLineageEventRequest request = new GetLineageEventRequest
    {
        LineageEventName = LineageEventName.FromProjectLocationProcessRunLineageEvent("[PROJECT]", "[LOCATION]", "[PROCESS]", "[RUN]", "[LINEAGE_EVENT]"),
    };
    // Make the request
    LineageEvent response = await lineageClient.GetLineageEventAsync(request);
    

### GetLineageEventAsync(LineageEventName, CallSettings)
    
    
    public virtual Task<LineageEvent> GetLineageEventAsync(LineageEventName name, CallSettings callSettings = null)

Gets details of a specified lineage event.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[LineageEventName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageEventName)`  
Required. The name of the lineage event to get.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[LineageEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageEvent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    LineageEventName name = LineageEventName.FromProjectLocationProcessRunLineageEvent("[PROJECT]", "[LOCATION]", "[PROCESS]", "[RUN]", "[LINEAGE_EVENT]");
    // Make the request
    LineageEvent response = await lineageClient.GetLineageEventAsync(name);
    

### GetLineageEventAsync(LineageEventName, CancellationToken)
    
    
    public virtual Task<LineageEvent> GetLineageEventAsync(LineageEventName name, CancellationToken cancellationToken)

Gets details of a specified lineage event.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[LineageEventName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageEventName)`  
Required. The name of the lineage event to get.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[LineageEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageEvent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    LineageEventName name = LineageEventName.FromProjectLocationProcessRunLineageEvent("[PROJECT]", "[LOCATION]", "[PROCESS]", "[RUN]", "[LINEAGE_EVENT]");
    // Make the request
    LineageEvent response = await lineageClient.GetLineageEventAsync(name);
    

### GetLineageEventAsync(string, CallSettings)
    
    
    public virtual Task<LineageEvent> GetLineageEventAsync(string name, CallSettings callSettings = null)

Gets details of a specified lineage event.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the lineage event to get.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[LineageEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageEvent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/processes/[PROCESS]/runs/[RUN]/lineageEvents/[LINEAGE_EVENT]";
    // Make the request
    LineageEvent response = await lineageClient.GetLineageEventAsync(name);
    

### GetLineageEventAsync(string, CancellationToken)
    
    
    public virtual Task<LineageEvent> GetLineageEventAsync(string name, CancellationToken cancellationToken)

Gets details of a specified lineage event.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the lineage event to get.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[LineageEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageEvent)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/processes/[PROCESS]/runs/[RUN]/lineageEvents/[LINEAGE_EVENT]";
    // Make the request
    LineageEvent response = await lineageClient.GetLineageEventAsync(name);
    

### GetProcess(GetProcessRequest, CallSettings)
    
    
    public virtual Process GetProcess(GetProcessRequest request, CallSettings callSettings = null)

Gets the details of the specified process.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetProcessRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.GetProcessRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Process](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Process)` | The RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = LineageClient.Create();
    // Initialize request argument(s)
    GetProcessRequest request = new GetProcessRequest
    {
        ProcessName = ProcessName.FromProjectLocationProcess("[PROJECT]", "[LOCATION]", "[PROCESS]"),
    };
    // Make the request
    Process response = lineageClient.GetProcess(request);
    

### GetProcess(ProcessName, CallSettings)
    
    
    public virtual Process GetProcess(ProcessName name, CallSettings callSettings = null)

Gets the details of the specified process.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ProcessName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ProcessName)`  
Required. The name of the process to get.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Process](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Process)` | The RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = LineageClient.Create();
    // Initialize request argument(s)
    ProcessName name = ProcessName.FromProjectLocationProcess("[PROJECT]", "[LOCATION]", "[PROCESS]");
    // Make the request
    Process response = lineageClient.GetProcess(name);
    

### GetProcess(string, CallSettings)
    
    
    public virtual Process GetProcess(string name, CallSettings callSettings = null)

Gets the details of the specified process.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the process to get.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Process](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Process)` | The RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = LineageClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/processes/[PROCESS]";
    // Make the request
    Process response = lineageClient.GetProcess(name);
    

### GetProcessAsync(GetProcessRequest, CallSettings)
    
    
    public virtual Task<Process> GetProcessAsync(GetProcessRequest request, CallSettings callSettings = null)

Gets the details of the specified process.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetProcessRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.GetProcessRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Process](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Process)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    GetProcessRequest request = new GetProcessRequest
    {
        ProcessName = ProcessName.FromProjectLocationProcess("[PROJECT]", "[LOCATION]", "[PROCESS]"),
    };
    // Make the request
    Process response = await lineageClient.GetProcessAsync(request);
    

### GetProcessAsync(GetProcessRequest, CancellationToken)
    
    
    public virtual Task<Process> GetProcessAsync(GetProcessRequest request, CancellationToken cancellationToken)

Gets the details of the specified process.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetProcessRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.GetProcessRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Process](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Process)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    GetProcessRequest request = new GetProcessRequest
    {
        ProcessName = ProcessName.FromProjectLocationProcess("[PROJECT]", "[LOCATION]", "[PROCESS]"),
    };
    // Make the request
    Process response = await lineageClient.GetProcessAsync(request);
    

### GetProcessAsync(ProcessName, CallSettings)
    
    
    public virtual Task<Process> GetProcessAsync(ProcessName name, CallSettings callSettings = null)

Gets the details of the specified process.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ProcessName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ProcessName)`  
Required. The name of the process to get.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Process](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Process)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    ProcessName name = ProcessName.FromProjectLocationProcess("[PROJECT]", "[LOCATION]", "[PROCESS]");
    // Make the request
    Process response = await lineageClient.GetProcessAsync(name);
    

### GetProcessAsync(ProcessName, CancellationToken)
    
    
    public virtual Task<Process> GetProcessAsync(ProcessName name, CancellationToken cancellationToken)

Gets the details of the specified process.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ProcessName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ProcessName)`  
Required. The name of the process to get.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Process](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Process)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    ProcessName name = ProcessName.FromProjectLocationProcess("[PROJECT]", "[LOCATION]", "[PROCESS]");
    // Make the request
    Process response = await lineageClient.GetProcessAsync(name);
    

### GetProcessAsync(string, CallSettings)
    
    
    public virtual Task<Process> GetProcessAsync(string name, CallSettings callSettings = null)

Gets the details of the specified process.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the process to get.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Process](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Process)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/processes/[PROCESS]";
    // Make the request
    Process response = await lineageClient.GetProcessAsync(name);
    

### GetProcessAsync(string, CancellationToken)
    
    
    public virtual Task<Process> GetProcessAsync(string name, CancellationToken cancellationToken)

Gets the details of the specified process.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the process to get.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Process](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Process)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/processes/[PROCESS]";
    // Make the request
    Process response = await lineageClient.GetProcessAsync(name);
    

### GetRun(GetRunRequest, CallSettings)
    
    
    public virtual Run GetRun(GetRunRequest request, CallSettings callSettings = null)

Gets the details of the specified run.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRunRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.GetRunRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Run](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Run)` | The RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = LineageClient.Create();
    // Initialize request argument(s)
    GetRunRequest request = new GetRunRequest
    {
        RunName = RunName.FromProjectLocationProcessRun("[PROJECT]", "[LOCATION]", "[PROCESS]", "[RUN]"),
    };
    // Make the request
    Run response = lineageClient.GetRun(request);
    

### GetRun(RunName, CallSettings)
    
    
    public virtual Run GetRun(RunName name, CallSettings callSettings = null)

Gets the details of the specified run.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[RunName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.RunName)`  
Required. The name of the run to get.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Run](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Run)` | The RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = LineageClient.Create();
    // Initialize request argument(s)
    RunName name = RunName.FromProjectLocationProcessRun("[PROJECT]", "[LOCATION]", "[PROCESS]", "[RUN]");
    // Make the request
    Run response = lineageClient.GetRun(name);
    

### GetRun(string, CallSettings)
    
    
    public virtual Run GetRun(string name, CallSettings callSettings = null)

Gets the details of the specified run.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the run to get.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Run](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Run)` | The RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = LineageClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/processes/[PROCESS]/runs/[RUN]";
    // Make the request
    Run response = lineageClient.GetRun(name);
    

### GetRunAsync(GetRunRequest, CallSettings)
    
    
    public virtual Task<Run> GetRunAsync(GetRunRequest request, CallSettings callSettings = null)

Gets the details of the specified run.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRunRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.GetRunRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Run](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Run)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    GetRunRequest request = new GetRunRequest
    {
        RunName = RunName.FromProjectLocationProcessRun("[PROJECT]", "[LOCATION]", "[PROCESS]", "[RUN]"),
    };
    // Make the request
    Run response = await lineageClient.GetRunAsync(request);
    

### GetRunAsync(GetRunRequest, CancellationToken)
    
    
    public virtual Task<Run> GetRunAsync(GetRunRequest request, CancellationToken cancellationToken)

Gets the details of the specified run.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRunRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.GetRunRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Run](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Run)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    GetRunRequest request = new GetRunRequest
    {
        RunName = RunName.FromProjectLocationProcessRun("[PROJECT]", "[LOCATION]", "[PROCESS]", "[RUN]"),
    };
    // Make the request
    Run response = await lineageClient.GetRunAsync(request);
    

### GetRunAsync(RunName, CallSettings)
    
    
    public virtual Task<Run> GetRunAsync(RunName name, CallSettings callSettings = null)

Gets the details of the specified run.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[RunName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.RunName)`  
Required. The name of the run to get.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Run](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Run)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    RunName name = RunName.FromProjectLocationProcessRun("[PROJECT]", "[LOCATION]", "[PROCESS]", "[RUN]");
    // Make the request
    Run response = await lineageClient.GetRunAsync(name);
    

### GetRunAsync(RunName, CancellationToken)
    
    
    public virtual Task<Run> GetRunAsync(RunName name, CancellationToken cancellationToken)

Gets the details of the specified run.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[RunName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.RunName)`  
Required. The name of the run to get.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Run](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Run)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    RunName name = RunName.FromProjectLocationProcessRun("[PROJECT]", "[LOCATION]", "[PROCESS]", "[RUN]");
    // Make the request
    Run response = await lineageClient.GetRunAsync(name);
    

### GetRunAsync(string, CallSettings)
    
    
    public virtual Task<Run> GetRunAsync(string name, CallSettings callSettings = null)

Gets the details of the specified run.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the run to get.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Run](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Run)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/processes/[PROCESS]/runs/[RUN]";
    // Make the request
    Run response = await lineageClient.GetRunAsync(name);
    

### GetRunAsync(string, CancellationToken)
    
    
    public virtual Task<Run> GetRunAsync(string name, CancellationToken cancellationToken)

Gets the details of the specified run.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the run to get.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Run](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Run)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/processes/[PROCESS]/runs/[RUN]";
    // Make the request
    Run response = await lineageClient.GetRunAsync(name);
    

### ListLineageEvents(ListLineageEventsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListLineageEventsResponse, LineageEvent> ListLineageEvents(ListLineageEventsRequest request, CallSettings callSettings = null)

Lists lineage events in the given project and location. The list order is not defined.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListLineageEventsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ListLineageEventsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListLineageEventsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ListLineageEventsResponse)[LineageEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageEvent)` | A pageable sequence of [LineageEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageEvent) resources.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = LineageClient.Create();
    // Initialize request argument(s)
    ListLineageEventsRequest request = new ListLineageEventsRequest
    {
        ParentAsRunName = RunName.FromProjectLocationProcessRun("[PROJECT]", "[LOCATION]", "[PROCESS]", "[RUN]"),
    };
    // Make the request
    PagedEnumerable<ListLineageEventsResponse, LineageEvent> response = lineageClient.ListLineageEvents(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (LineageEvent item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListLineageEventsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (LineageEvent item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<LineageEvent> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (LineageEvent item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListLineageEvents(RunName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListLineageEventsResponse, LineageEvent> ListLineageEvents(RunName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists lineage events in the given project and location. The list order is not defined.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[RunName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.RunName)`  
Required. The name of the run that owns the collection of lineage events to get.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListLineageEventsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ListLineageEventsResponse)[LineageEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageEvent)` | A pageable sequence of [LineageEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageEvent) resources.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = LineageClient.Create();
    // Initialize request argument(s)
    RunName parent = RunName.FromProjectLocationProcessRun("[PROJECT]", "[LOCATION]", "[PROCESS]", "[RUN]");
    // Make the request
    PagedEnumerable<ListLineageEventsResponse, LineageEvent> response = lineageClient.ListLineageEvents(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (LineageEvent item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListLineageEventsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (LineageEvent item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<LineageEvent> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (LineageEvent item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListLineageEvents(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListLineageEventsResponse, LineageEvent> ListLineageEvents(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists lineage events in the given project and location. The list order is not defined.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the run that owns the collection of lineage events to get.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListLineageEventsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ListLineageEventsResponse)[LineageEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageEvent)` | A pageable sequence of [LineageEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageEvent) resources.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = LineageClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/processes/[PROCESS]/runs/[RUN]";
    // Make the request
    PagedEnumerable<ListLineageEventsResponse, LineageEvent> response = lineageClient.ListLineageEvents(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (LineageEvent item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListLineageEventsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (LineageEvent item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<LineageEvent> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (LineageEvent item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListLineageEventsAsync(ListLineageEventsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListLineageEventsResponse, LineageEvent> ListLineageEventsAsync(ListLineageEventsRequest request, CallSettings callSettings = null)

Lists lineage events in the given project and location. The list order is not defined.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListLineageEventsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ListLineageEventsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListLineageEventsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ListLineageEventsResponse)[LineageEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageEvent)` | A pageable asynchronous sequence of [LineageEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageEvent) resources.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    ListLineageEventsRequest request = new ListLineageEventsRequest
    {
        ParentAsRunName = RunName.FromProjectLocationProcessRun("[PROJECT]", "[LOCATION]", "[PROCESS]", "[RUN]"),
    };
    // Make the request
    PagedAsyncEnumerable<ListLineageEventsResponse, LineageEvent> response = lineageClient.ListLineageEventsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (LineageEvent item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListLineageEventsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (LineageEvent item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<LineageEvent> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (LineageEvent item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListLineageEventsAsync(RunName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListLineageEventsResponse, LineageEvent> ListLineageEventsAsync(RunName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists lineage events in the given project and location. The list order is not defined.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[RunName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.RunName)`  
Required. The name of the run that owns the collection of lineage events to get.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListLineageEventsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ListLineageEventsResponse)[LineageEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageEvent)` | A pageable asynchronous sequence of [LineageEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageEvent) resources.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    RunName parent = RunName.FromProjectLocationProcessRun("[PROJECT]", "[LOCATION]", "[PROCESS]", "[RUN]");
    // Make the request
    PagedAsyncEnumerable<ListLineageEventsResponse, LineageEvent> response = lineageClient.ListLineageEventsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (LineageEvent item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListLineageEventsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (LineageEvent item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<LineageEvent> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (LineageEvent item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListLineageEventsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListLineageEventsResponse, LineageEvent> ListLineageEventsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists lineage events in the given project and location. The list order is not defined.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the run that owns the collection of lineage events to get.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListLineageEventsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ListLineageEventsResponse)[LineageEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageEvent)` | A pageable asynchronous sequence of [LineageEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageEvent) resources.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/processes/[PROCESS]/runs/[RUN]";
    // Make the request
    PagedAsyncEnumerable<ListLineageEventsResponse, LineageEvent> response = lineageClient.ListLineageEventsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (LineageEvent item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListLineageEventsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (LineageEvent item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<LineageEvent> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (LineageEvent item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListProcesses(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListProcessesResponse, Process> ListProcesses(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

List processes in the given project and location. List order is descending by insertion time.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The name of the project and its location that owns this collection of processes.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListProcessesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ListProcessesResponse)[Process](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Process)` | A pageable sequence of [Process](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Process) resources.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = LineageClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListProcessesResponse, Process> response = lineageClient.ListProcesses(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Process item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListProcessesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Process item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Process> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Process item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListProcesses(ListProcessesRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListProcessesResponse, Process> ListProcesses(ListProcessesRequest request, CallSettings callSettings = null)

List processes in the given project and location. List order is descending by insertion time.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListProcessesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ListProcessesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListProcessesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ListProcessesResponse)[Process](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Process)` | A pageable sequence of [Process](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Process) resources.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = LineageClient.Create();
    // Initialize request argument(s)
    ListProcessesRequest request = new ListProcessesRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    PagedEnumerable<ListProcessesResponse, Process> response = lineageClient.ListProcesses(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Process item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListProcessesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Process item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Process> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Process item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListProcesses(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListProcessesResponse, Process> ListProcesses(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

List processes in the given project and location. List order is descending by insertion time.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the project and its location that owns this collection of processes.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListProcessesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ListProcessesResponse)[Process](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Process)` | A pageable sequence of [Process](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Process) resources.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = LineageClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListProcessesResponse, Process> response = lineageClient.ListProcesses(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Process item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListProcessesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Process item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Process> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Process item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListProcessesAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListProcessesResponse, Process> ListProcessesAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

List processes in the given project and location. List order is descending by insertion time.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The name of the project and its location that owns this collection of processes.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListProcessesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ListProcessesResponse)[Process](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Process)` | A pageable asynchronous sequence of [Process](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Process) resources.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListProcessesResponse, Process> response = lineageClient.ListProcessesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Process item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListProcessesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Process item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Process> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Process item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListProcessesAsync(ListProcessesRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListProcessesResponse, Process> ListProcessesAsync(ListProcessesRequest request, CallSettings callSettings = null)

List processes in the given project and location. List order is descending by insertion time.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListProcessesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ListProcessesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListProcessesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ListProcessesResponse)[Process](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Process)` | A pageable asynchronous sequence of [Process](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Process) resources.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    ListProcessesRequest request = new ListProcessesRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    PagedAsyncEnumerable<ListProcessesResponse, Process> response = lineageClient.ListProcessesAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Process item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListProcessesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Process item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Process> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Process item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListProcessesAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListProcessesResponse, Process> ListProcessesAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

List processes in the given project and location. List order is descending by insertion time.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the project and its location that owns this collection of processes.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListProcessesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ListProcessesResponse)[Process](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Process)` | A pageable asynchronous sequence of [Process](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Process) resources.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListProcessesResponse, Process> response = lineageClient.ListProcessesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Process item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListProcessesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Process item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Process> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Process item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListRuns(ListRunsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListRunsResponse, Run> ListRuns(ListRunsRequest request, CallSettings callSettings = null)

Lists runs in the given project and location. List order is descending by `start_time`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRunsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ListRunsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListRunsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ListRunsResponse)[Run](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Run)` | A pageable sequence of [Run](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Run) resources.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = LineageClient.Create();
    // Initialize request argument(s)
    ListRunsRequest request = new ListRunsRequest
    {
        ParentAsProcessName = ProcessName.FromProjectLocationProcess("[PROJECT]", "[LOCATION]", "[PROCESS]"),
    };
    // Make the request
    PagedEnumerable<ListRunsResponse, Run> response = lineageClient.ListRuns(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Run item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListRunsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Run item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Run> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Run item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListRuns(ProcessName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListRunsResponse, Run> ListRuns(ProcessName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists runs in the given project and location. List order is descending by `start_time`.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ProcessName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ProcessName)`  
Required. The name of process that owns this collection of runs.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListRunsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ListRunsResponse)[Run](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Run)` | A pageable sequence of [Run](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Run) resources.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = LineageClient.Create();
    // Initialize request argument(s)
    ProcessName parent = ProcessName.FromProjectLocationProcess("[PROJECT]", "[LOCATION]", "[PROCESS]");
    // Make the request
    PagedEnumerable<ListRunsResponse, Run> response = lineageClient.ListRuns(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Run item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListRunsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Run item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Run> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Run item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListRuns(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListRunsResponse, Run> ListRuns(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists runs in the given project and location. List order is descending by `start_time`.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of process that owns this collection of runs.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListRunsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ListRunsResponse)[Run](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Run)` | A pageable sequence of [Run](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Run) resources.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = LineageClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/processes/[PROCESS]";
    // Make the request
    PagedEnumerable<ListRunsResponse, Run> response = lineageClient.ListRuns(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Run item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListRunsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Run item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Run> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Run item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListRunsAsync(ListRunsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListRunsResponse, Run> ListRunsAsync(ListRunsRequest request, CallSettings callSettings = null)

Lists runs in the given project and location. List order is descending by `start_time`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRunsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ListRunsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListRunsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ListRunsResponse)[Run](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Run)` | A pageable asynchronous sequence of [Run](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Run) resources.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    ListRunsRequest request = new ListRunsRequest
    {
        ParentAsProcessName = ProcessName.FromProjectLocationProcess("[PROJECT]", "[LOCATION]", "[PROCESS]"),
    };
    // Make the request
    PagedAsyncEnumerable<ListRunsResponse, Run> response = lineageClient.ListRunsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Run item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListRunsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Run item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Run> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Run item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListRunsAsync(ProcessName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListRunsResponse, Run> ListRunsAsync(ProcessName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists runs in the given project and location. List order is descending by `start_time`.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ProcessName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ProcessName)`  
Required. The name of process that owns this collection of runs.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListRunsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ListRunsResponse)[Run](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Run)` | A pageable asynchronous sequence of [Run](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Run) resources.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    ProcessName parent = ProcessName.FromProjectLocationProcess("[PROJECT]", "[LOCATION]", "[PROCESS]");
    // Make the request
    PagedAsyncEnumerable<ListRunsResponse, Run> response = lineageClient.ListRunsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Run item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListRunsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Run item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Run> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Run item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListRunsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListRunsResponse, Run> ListRunsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists runs in the given project and location. List order is descending by `start_time`.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of process that owns this collection of runs.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListRunsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ListRunsResponse)[Run](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Run)` | A pageable asynchronous sequence of [Run](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Run) resources.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/processes/[PROCESS]";
    // Make the request
    PagedAsyncEnumerable<ListRunsResponse, Run> response = lineageClient.ListRunsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Run item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListRunsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Run item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Run> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Run item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### PollOnceDeleteProcess(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> PollOnceDeleteProcess(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteProcess`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteProcessAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> PollOnceDeleteProcessAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteProcess`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteRun(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> PollOnceDeleteRun(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteRun`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteRunAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> PollOnceDeleteRunAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteRun`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### ProcessOpenLineageRunEvent(ProcessOpenLineageRunEventRequest, CallSettings)
    
    
    public virtual ProcessOpenLineageRunEventResponse ProcessOpenLineageRunEvent(ProcessOpenLineageRunEventRequest request, CallSettings callSettings = null)

Creates new lineage events together with their parents: process and run. Updates the process and run if they already exist. Mapped from Open Lineage specification: <https://github.com/OpenLineage/OpenLineage/blob/main/spec/OpenLineage.json>.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ProcessOpenLineageRunEventRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ProcessOpenLineageRunEventRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ProcessOpenLineageRunEventResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ProcessOpenLineageRunEventResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = LineageClient.Create();
    // Initialize request argument(s)
    ProcessOpenLineageRunEventRequest request = new ProcessOpenLineageRunEventRequest
    {
        Parent = "",
        OpenLineage = new Struct(),
    };
    // Make the request
    ProcessOpenLineageRunEventResponse response = lineageClient.ProcessOpenLineageRunEvent(request);
    

### ProcessOpenLineageRunEvent(string, Struct, CallSettings)
    
    
    public virtual ProcessOpenLineageRunEventResponse ProcessOpenLineageRunEvent(string parent, Struct openLineage, CallSettings callSettings = null)

Creates new lineage events together with their parents: process and run. Updates the process and run if they already exist. Mapped from Open Lineage specification: <https://github.com/OpenLineage/OpenLineage/blob/main/spec/OpenLineage.json>.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the project and its location that should own the process, run, and lineage event.  
`openLineage` | `[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)`  
Required. OpenLineage message following OpenLineage format: <https://github.com/OpenLineage/OpenLineage/blob/main/spec/OpenLineage.json>  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ProcessOpenLineageRunEventResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ProcessOpenLineageRunEventResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = LineageClient.Create();
    // Initialize request argument(s)
    string parent = "";
    Struct openLineage = new Struct();
    // Make the request
    ProcessOpenLineageRunEventResponse response = lineageClient.ProcessOpenLineageRunEvent(parent, openLineage);
    

### ProcessOpenLineageRunEventAsync(ProcessOpenLineageRunEventRequest, CallSettings)
    
    
    public virtual Task<ProcessOpenLineageRunEventResponse> ProcessOpenLineageRunEventAsync(ProcessOpenLineageRunEventRequest request, CallSettings callSettings = null)

Creates new lineage events together with their parents: process and run. Updates the process and run if they already exist. Mapped from Open Lineage specification: <https://github.com/OpenLineage/OpenLineage/blob/main/spec/OpenLineage.json>.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ProcessOpenLineageRunEventRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ProcessOpenLineageRunEventRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ProcessOpenLineageRunEventResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ProcessOpenLineageRunEventResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    ProcessOpenLineageRunEventRequest request = new ProcessOpenLineageRunEventRequest
    {
        Parent = "",
        OpenLineage = new Struct(),
    };
    // Make the request
    ProcessOpenLineageRunEventResponse response = await lineageClient.ProcessOpenLineageRunEventAsync(request);
    

### ProcessOpenLineageRunEventAsync(ProcessOpenLineageRunEventRequest, CancellationToken)
    
    
    public virtual Task<ProcessOpenLineageRunEventResponse> ProcessOpenLineageRunEventAsync(ProcessOpenLineageRunEventRequest request, CancellationToken cancellationToken)

Creates new lineage events together with their parents: process and run. Updates the process and run if they already exist. Mapped from Open Lineage specification: <https://github.com/OpenLineage/OpenLineage/blob/main/spec/OpenLineage.json>.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ProcessOpenLineageRunEventRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ProcessOpenLineageRunEventRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ProcessOpenLineageRunEventResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ProcessOpenLineageRunEventResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    ProcessOpenLineageRunEventRequest request = new ProcessOpenLineageRunEventRequest
    {
        Parent = "",
        OpenLineage = new Struct(),
    };
    // Make the request
    ProcessOpenLineageRunEventResponse response = await lineageClient.ProcessOpenLineageRunEventAsync(request);
    

### ProcessOpenLineageRunEventAsync(string, Struct, CallSettings)
    
    
    public virtual Task<ProcessOpenLineageRunEventResponse> ProcessOpenLineageRunEventAsync(string parent, Struct openLineage, CallSettings callSettings = null)

Creates new lineage events together with their parents: process and run. Updates the process and run if they already exist. Mapped from Open Lineage specification: <https://github.com/OpenLineage/OpenLineage/blob/main/spec/OpenLineage.json>.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the project and its location that should own the process, run, and lineage event.  
`openLineage` | `[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)`  
Required. OpenLineage message following OpenLineage format: <https://github.com/OpenLineage/OpenLineage/blob/main/spec/OpenLineage.json>  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ProcessOpenLineageRunEventResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ProcessOpenLineageRunEventResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "";
    Struct openLineage = new Struct();
    // Make the request
    ProcessOpenLineageRunEventResponse response = await lineageClient.ProcessOpenLineageRunEventAsync(parent, openLineage);
    

### ProcessOpenLineageRunEventAsync(string, Struct, CancellationToken)
    
    
    public virtual Task<ProcessOpenLineageRunEventResponse> ProcessOpenLineageRunEventAsync(string parent, Struct openLineage, CancellationToken cancellationToken)

Creates new lineage events together with their parents: process and run. Updates the process and run if they already exist. Mapped from Open Lineage specification: <https://github.com/OpenLineage/OpenLineage/blob/main/spec/OpenLineage.json>.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the project and its location that should own the process, run, and lineage event.  
`openLineage` | `[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)`  
Required. OpenLineage message following OpenLineage format: <https://github.com/OpenLineage/OpenLineage/blob/main/spec/OpenLineage.json>  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ProcessOpenLineageRunEventResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.ProcessOpenLineageRunEventResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "";
    Struct openLineage = new Struct();
    // Make the request
    ProcessOpenLineageRunEventResponse response = await lineageClient.ProcessOpenLineageRunEventAsync(parent, openLineage);
    

### SearchLineageStreaming(SearchLineageStreamingRequest, CallSettings)
    
    
    public virtual LineageClient.SearchLineageStreamingStream SearchLineageStreaming(SearchLineageStreamingRequest request, CallSettings callSettings = null)

Retrieves a streaming response of lineage links connected to the requested assets by performing a breadth-first search in the given direction. Links represent the data flow between **source** (upstream) and **target** (downstream) assets in transformation pipelines. Links are stored in the same project as the Lineage Events that create them. This method retrieves links from all valid locations provided in the request. This method supports Column-Level Lineage (CLL) along with wildcard support to retrieve all CLL for an Entity FQN.

Following permissions are required to retrieve links:

  * `datalineage.events.get` permission for the project where the link is stored for entity-level lineage.
  * `datalineage.events.getFields` permission for the project where the link is stored for column-level lineage.



This method also returns processes that created the links if explicitly requested by setting [max_process_per_link](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/google.cloud.datacatalog.lineage.v1.SearchLineageStreamingRequest.limits.max_process_per_link) is non-zero and full process details are requested via `links.processes.process` in the [FieldMask](https://developers.google.com/workspace/docs/api/how-tos/field-masks#read_with_a_field_mask).

Permission required to retrieve processes:

  * `datalineage.processes.get` permission for the project where the process is stored.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchLineageStreamingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLineageStreamingRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[LineageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageClient)[SearchLineageStreamingStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageClient.SearchLineageStreamingStream)` | The server stream.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = LineageClient.Create();
    // Initialize request argument(s)
    SearchLineageStreamingRequest request = new SearchLineageStreamingRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Locations = { "", },
        RootCriteria = new SearchLineageStreamingRequest.Types.RootCriteria(),
        Direction = SearchLineageStreamingRequest.Types.SearchDirection.Unspecified,
        Filters = new SearchLineageStreamingRequest.Types.SearchFilters(),
        Limits = new SearchLineageStreamingRequest.Types.SearchLimits(),
    };
    // Make the request, returning a streaming response
    using LineageClient.SearchLineageStreamingStream response = lineageClient.SearchLineageStreaming(request);
    
    // Read streaming responses from server until complete
    // Note that C# 8 code can use await foreach
    AsyncResponseStream<SearchLineageStreamingResponse> responseStream = response.GetResponseStream();
    while (await responseStream.MoveNextAsync())
    {
        SearchLineageStreamingResponse responseItem = responseStream.Current;
        // Do something with streamed response
    }
    // The response stream has completed
    

### SearchLinks(SearchLinksRequest, CallSettings)
    
    
    public virtual PagedEnumerable<SearchLinksResponse, Link> SearchLinks(SearchLinksRequest request, CallSettings callSettings = null)

Retrieve a list of links connected to a specific asset. Links represent the data flow between **source** (upstream) and **target** (downstream) assets in transformation pipelines. Links are stored in the same project as the Lineage Events that create them.

You can retrieve links in every project where you have the `datalineage.events.get` permission. The project provided in the URL is used for Billing and Quota.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchLinksRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLinksRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[SearchLinksResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLinksResponse)[Link](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Link)` | A pageable sequence of [Link](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Link) resources.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = LineageClient.Create();
    // Initialize request argument(s)
    SearchLinksRequest request = new SearchLinksRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Source = new EntityReference(),
    };
    // Make the request
    PagedEnumerable<SearchLinksResponse, Link> response = lineageClient.SearchLinks(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Link item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (SearchLinksResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Link item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Link> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Link item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### SearchLinksAsync(SearchLinksRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<SearchLinksResponse, Link> SearchLinksAsync(SearchLinksRequest request, CallSettings callSettings = null)

Retrieve a list of links connected to a specific asset. Links represent the data flow between **source** (upstream) and **target** (downstream) assets in transformation pipelines. Links are stored in the same project as the Lineage Events that create them.

You can retrieve links in every project where you have the `datalineage.events.get` permission. The project provided in the URL is used for Billing and Quota.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchLinksRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLinksRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[SearchLinksResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLinksResponse)[Link](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Link)` | A pageable asynchronous sequence of [Link](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Link) resources.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    SearchLinksRequest request = new SearchLinksRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Source = new EntityReference(),
    };
    // Make the request
    PagedAsyncEnumerable<SearchLinksResponse, Link> response = lineageClient.SearchLinksAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Link item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (SearchLinksResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Link item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Link> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Link item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageClient#Google_Cloud_DataCatalog_Lineage_V1_LineageClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageClient#Google_Cloud_DataCatalog_Lineage_V1_LineageClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageClient#Google_Cloud_DataCatalog_Lineage_V1_LineageClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.LineageClient#Google_Cloud_DataCatalog_Lineage_V1_LineageClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### UpdateProcess(Process, FieldMask, CallSettings)
    
    
    public virtual Process UpdateProcess(Process process, FieldMask updateMask, CallSettings callSettings = null)

Updates a process.

**Parameters**  
---  
**Name** | **Description**  
`process` | `[Process](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Process)`  
Required. The lineage process to update. The process's `name` field is used to identify the process to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. The list of fields to update. Currently not used. The whole message is updated.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Process](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Process)` | The RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = LineageClient.Create();
    // Initialize request argument(s)
    Process process = new Process();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Process response = lineageClient.UpdateProcess(process, updateMask);
    

### UpdateProcess(UpdateProcessRequest, CallSettings)
    
    
    public virtual Process UpdateProcess(UpdateProcessRequest request, CallSettings callSettings = null)

Updates a process.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateProcessRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.UpdateProcessRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Process](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Process)` | The RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = LineageClient.Create();
    // Initialize request argument(s)
    UpdateProcessRequest request = new UpdateProcessRequest
    {
        Process = new Process(),
        UpdateMask = new FieldMask(),
        AllowMissing = false,
    };
    // Make the request
    Process response = lineageClient.UpdateProcess(request);
    

### UpdateProcessAsync(Process, FieldMask, CallSettings)
    
    
    public virtual Task<Process> UpdateProcessAsync(Process process, FieldMask updateMask, CallSettings callSettings = null)

Updates a process.

**Parameters**  
---  
**Name** | **Description**  
`process` | `[Process](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Process)`  
Required. The lineage process to update. The process's `name` field is used to identify the process to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. The list of fields to update. Currently not used. The whole message is updated.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Process](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Process)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    Process process = new Process();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Process response = await lineageClient.UpdateProcessAsync(process, updateMask);
    

### UpdateProcessAsync(Process, FieldMask, CancellationToken)
    
    
    public virtual Task<Process> UpdateProcessAsync(Process process, FieldMask updateMask, CancellationToken cancellationToken)

Updates a process.

**Parameters**  
---  
**Name** | **Description**  
`process` | `[Process](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Process)`  
Required. The lineage process to update. The process's `name` field is used to identify the process to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. The list of fields to update. Currently not used. The whole message is updated.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Process](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Process)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    Process process = new Process();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Process response = await lineageClient.UpdateProcessAsync(process, updateMask);
    

### UpdateProcessAsync(UpdateProcessRequest, CallSettings)
    
    
    public virtual Task<Process> UpdateProcessAsync(UpdateProcessRequest request, CallSettings callSettings = null)

Updates a process.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateProcessRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.UpdateProcessRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Process](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Process)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    UpdateProcessRequest request = new UpdateProcessRequest
    {
        Process = new Process(),
        UpdateMask = new FieldMask(),
        AllowMissing = false,
    };
    // Make the request
    Process response = await lineageClient.UpdateProcessAsync(request);
    

### UpdateProcessAsync(UpdateProcessRequest, CancellationToken)
    
    
    public virtual Task<Process> UpdateProcessAsync(UpdateProcessRequest request, CancellationToken cancellationToken)

Updates a process.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateProcessRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.UpdateProcessRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Process](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Process)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    UpdateProcessRequest request = new UpdateProcessRequest
    {
        Process = new Process(),
        UpdateMask = new FieldMask(),
        AllowMissing = false,
    };
    // Make the request
    Process response = await lineageClient.UpdateProcessAsync(request);
    

### UpdateRun(Run, FieldMask, CallSettings)
    
    
    public virtual Run UpdateRun(Run run, FieldMask updateMask, CallSettings callSettings = null)

Updates a run.

**Parameters**  
---  
**Name** | **Description**  
`run` | `[Run](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Run)`  
Required. The lineage run to update. The run's `name` field is used to identify the run to update. Format: `projects/{project}/locations/{location}/processes/{process}/runs/{run}`.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. The list of fields to update. Currently not used. The whole message is updated.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Run](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Run)` | The RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = LineageClient.Create();
    // Initialize request argument(s)
    Run run = new Run();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Run response = lineageClient.UpdateRun(run, updateMask);
    

### UpdateRun(UpdateRunRequest, CallSettings)
    
    
    public virtual Run UpdateRun(UpdateRunRequest request, CallSettings callSettings = null)

Updates a run.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateRunRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.UpdateRunRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Run](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Run)` | The RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = LineageClient.Create();
    // Initialize request argument(s)
    UpdateRunRequest request = new UpdateRunRequest
    {
        Run = new Run(),
        UpdateMask = new FieldMask(),
        AllowMissing = false,
    };
    // Make the request
    Run response = lineageClient.UpdateRun(request);
    

### UpdateRunAsync(Run, FieldMask, CallSettings)
    
    
    public virtual Task<Run> UpdateRunAsync(Run run, FieldMask updateMask, CallSettings callSettings = null)

Updates a run.

**Parameters**  
---  
**Name** | **Description**  
`run` | `[Run](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Run)`  
Required. The lineage run to update. The run's `name` field is used to identify the run to update. Format: `projects/{project}/locations/{location}/processes/{process}/runs/{run}`.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. The list of fields to update. Currently not used. The whole message is updated.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Run](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Run)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    Run run = new Run();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Run response = await lineageClient.UpdateRunAsync(run, updateMask);
    

### UpdateRunAsync(Run, FieldMask, CancellationToken)
    
    
    public virtual Task<Run> UpdateRunAsync(Run run, FieldMask updateMask, CancellationToken cancellationToken)

Updates a run.

**Parameters**  
---  
**Name** | **Description**  
`run` | `[Run](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Run)`  
Required. The lineage run to update. The run's `name` field is used to identify the run to update. Format: `projects/{project}/locations/{location}/processes/{process}/runs/{run}`.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. The list of fields to update. Currently not used. The whole message is updated.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Run](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Run)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    Run run = new Run();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Run response = await lineageClient.UpdateRunAsync(run, updateMask);
    

### UpdateRunAsync(UpdateRunRequest, CallSettings)
    
    
    public virtual Task<Run> UpdateRunAsync(UpdateRunRequest request, CallSettings callSettings = null)

Updates a run.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateRunRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.UpdateRunRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Run](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Run)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    UpdateRunRequest request = new UpdateRunRequest
    {
        Run = new Run(),
        UpdateMask = new FieldMask(),
        AllowMissing = false,
    };
    // Make the request
    Run response = await lineageClient.UpdateRunAsync(request);
    

### UpdateRunAsync(UpdateRunRequest, CancellationToken)
    
    
    public virtual Task<Run> UpdateRunAsync(UpdateRunRequest request, CancellationToken cancellationToken)

Updates a run.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateRunRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.UpdateRunRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Run](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.Run)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    LineageClient lineageClient = await LineageClient.CreateAsync();
    // Initialize request argument(s)
    UpdateRunRequest request = new UpdateRunRequest
    {
        Run = new Run(),
        UpdateMask = new FieldMask(),
        AllowMissing = false,
    };
    // Make the request
    Run response = await lineageClient.UpdateRunAsync(request);
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-11 UTC."],[],[]] 
