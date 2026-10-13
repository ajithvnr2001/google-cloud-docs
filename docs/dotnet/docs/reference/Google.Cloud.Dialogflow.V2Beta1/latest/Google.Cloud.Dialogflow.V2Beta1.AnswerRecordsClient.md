---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.AnswerRecordsClient
title: Google Cloud Dialogflow v2beta1 API - Class AnswerRecordsClient (1.0.0-beta33) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:10:46.750444+00:00
---

# Google Cloud Dialogflow v2beta1 API - Class AnswerRecordsClient (1.0.0-beta33)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.AnswerRecordsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Dialogflow v2beta1 API - Class AnswerRecordsClient (1.0.0-beta33) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta33 (latest)  1.0.0-beta32 
    
    
    public abstract class AnswerRecordsClient

Reference documentation and code samples for the Google Cloud Dialogflow v2beta1 API class AnswerRecordsClient.

AnswerRecords client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AnswerRecordsClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[AnswerRecordsClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.AnswerRecordsClientImpl)

## Namespace

[Google.Cloud.Dialogflow.V2Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1)

## Assembly

Google.Cloud.Dialogflow.V2Beta1.dll

## Remarks

Service for managing [AnswerRecords][google.cloud.dialogflow.v2beta1.AnswerRecord].

## Properties 

### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the AnswerRecords service, which is a host of "dialogflow.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default AnswerRecords scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default AnswerRecords scopes are:

  * <https://www.googleapis.com/auth/cloud-platform>
  * <https://www.googleapis.com/auth/dialogflow>



### GrpcClient
    
    
    public virtual AnswerRecords.AnswerRecordsClient GrpcClient { get; }

The underlying gRPC AnswerRecords client

**Property Value**  
---  
**Type** | **Description**  
`[AnswerRecords](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.AnswerRecords)[AnswerRecordsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.AnswerRecords.AnswerRecordsClient)` |   
  
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
    
    
    public static AnswerRecordsClient Create()

Synchronously creates a [AnswerRecordsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.AnswerRecordsClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [AnswerRecordsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.AnswerRecordsClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[AnswerRecordsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.AnswerRecordsClient)` | The created [AnswerRecordsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.AnswerRecordsClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<AnswerRecordsClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [AnswerRecordsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.AnswerRecordsClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [AnswerRecordsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.AnswerRecordsClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AnswerRecordsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.AnswerRecordsClient)` | The task representing the created [AnswerRecordsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.AnswerRecordsClient).  
  
### GetAnswerRecord(GetAnswerRecordRequest, CallSettings)
    
    
    [Obsolete]
    public virtual AnswerRecord GetAnswerRecord(GetAnswerRecordRequest request, CallSettings callSettings = null)

Deprecated. Retrieves a specific answer record.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAnswerRecordRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GetAnswerRecordRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[AnswerRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.AnswerRecord)` | The RPC response.  
**Example**
    
    
                // Create client
                AnswerRecordsClient answerRecordsClient = AnswerRecordsClient.Create();
                // Initialize request argument(s)
                GetAnswerRecordRequest request = new GetAnswerRecordRequest { Name = "", };
                // Make the request
    #pragma warning disable CS0612
                AnswerRecord response = answerRecordsClient.GetAnswerRecord(request);
    #pragma warning restore CS0612
    

### GetAnswerRecordAsync(GetAnswerRecordRequest, CallSettings)
    
    
    [Obsolete]
    public virtual Task<AnswerRecord> GetAnswerRecordAsync(GetAnswerRecordRequest request, CallSettings callSettings = null)

Deprecated. Retrieves a specific answer record.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAnswerRecordRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GetAnswerRecordRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AnswerRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.AnswerRecord)` | A Task containing the RPC response.  
**Example**
    
    
                // Create client
                AnswerRecordsClient answerRecordsClient = await AnswerRecordsClient.CreateAsync();
                // Initialize request argument(s)
                GetAnswerRecordRequest request = new GetAnswerRecordRequest { Name = "", };
                // Make the request
    #pragma warning disable CS0612
                AnswerRecord response = await answerRecordsClient.GetAnswerRecordAsync(request);
    #pragma warning restore CS0612
    

### GetAnswerRecordAsync(GetAnswerRecordRequest, CancellationToken)
    
    
    [Obsolete]
    public virtual Task<AnswerRecord> GetAnswerRecordAsync(GetAnswerRecordRequest request, CancellationToken cancellationToken)

Deprecated. Retrieves a specific answer record.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAnswerRecordRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GetAnswerRecordRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AnswerRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.AnswerRecord)` | A Task containing the RPC response.  
**Example**
    
    
                // Create client
                AnswerRecordsClient answerRecordsClient = await AnswerRecordsClient.CreateAsync();
                // Initialize request argument(s)
                GetAnswerRecordRequest request = new GetAnswerRecordRequest { Name = "", };
                // Make the request
    #pragma warning disable CS0612
                AnswerRecord response = await answerRecordsClient.GetAnswerRecordAsync(request);
    #pragma warning restore CS0612
    

### ListAnswerRecords(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListAnswerRecordsResponse, AnswerRecord> ListAnswerRecords(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Returns the list of all answer records in the specified project in reverse chronological order.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The project to list all answer records for in reverse chronological order. Format: `projects/<Project ID>/locations/<Location ID>`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListAnswerRecordsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ListAnswerRecordsResponse)[AnswerRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.AnswerRecord)` | A pageable sequence of [AnswerRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.AnswerRecord) resources.  
**Example**
    
    
    // Create client
    AnswerRecordsClient answerRecordsClient = AnswerRecordsClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListAnswerRecordsResponse, AnswerRecord> response = answerRecordsClient.ListAnswerRecords(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (AnswerRecord item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListAnswerRecordsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (AnswerRecord item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<AnswerRecord> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (AnswerRecord item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAnswerRecords(ProjectName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListAnswerRecordsResponse, AnswerRecord> ListAnswerRecords(ProjectName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Returns the list of all answer records in the specified project in reverse chronological order.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)`  
Required. The project to list all answer records for in reverse chronological order. Format: `projects/<Project ID>/locations/<Location ID>`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListAnswerRecordsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ListAnswerRecordsResponse)[AnswerRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.AnswerRecord)` | A pageable sequence of [AnswerRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.AnswerRecord) resources.  
**Example**
    
    
    // Create client
    AnswerRecordsClient answerRecordsClient = AnswerRecordsClient.Create();
    // Initialize request argument(s)
    ProjectName parent = ProjectName.FromProject("[PROJECT]");
    // Make the request
    PagedEnumerable<ListAnswerRecordsResponse, AnswerRecord> response = answerRecordsClient.ListAnswerRecords(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (AnswerRecord item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListAnswerRecordsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (AnswerRecord item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<AnswerRecord> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (AnswerRecord item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAnswerRecords(ListAnswerRecordsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListAnswerRecordsResponse, AnswerRecord> ListAnswerRecords(ListAnswerRecordsRequest request, CallSettings callSettings = null)

Returns the list of all answer records in the specified project in reverse chronological order.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAnswerRecordsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ListAnswerRecordsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListAnswerRecordsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ListAnswerRecordsResponse)[AnswerRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.AnswerRecord)` | A pageable sequence of [AnswerRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.AnswerRecord) resources.  
**Example**
    
    
    // Create client
    AnswerRecordsClient answerRecordsClient = AnswerRecordsClient.Create();
    // Initialize request argument(s)
    ListAnswerRecordsRequest request = new ListAnswerRecordsRequest
    {
        ParentAsProjectName = ProjectName.FromProject("[PROJECT]"),
        Filter = "",
    };
    // Make the request
    PagedEnumerable<ListAnswerRecordsResponse, AnswerRecord> response = answerRecordsClient.ListAnswerRecords(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (AnswerRecord item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListAnswerRecordsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (AnswerRecord item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<AnswerRecord> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (AnswerRecord item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAnswerRecords(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListAnswerRecordsResponse, AnswerRecord> ListAnswerRecords(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Returns the list of all answer records in the specified project in reverse chronological order.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The project to list all answer records for in reverse chronological order. Format: `projects/<Project ID>/locations/<Location ID>`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListAnswerRecordsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ListAnswerRecordsResponse)[AnswerRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.AnswerRecord)` | A pageable sequence of [AnswerRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.AnswerRecord) resources.  
**Example**
    
    
    // Create client
    AnswerRecordsClient answerRecordsClient = AnswerRecordsClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]";
    // Make the request
    PagedEnumerable<ListAnswerRecordsResponse, AnswerRecord> response = answerRecordsClient.ListAnswerRecords(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (AnswerRecord item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListAnswerRecordsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (AnswerRecord item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<AnswerRecord> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (AnswerRecord item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAnswerRecordsAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListAnswerRecordsResponse, AnswerRecord> ListAnswerRecordsAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Returns the list of all answer records in the specified project in reverse chronological order.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The project to list all answer records for in reverse chronological order. Format: `projects/<Project ID>/locations/<Location ID>`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListAnswerRecordsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ListAnswerRecordsResponse)[AnswerRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.AnswerRecord)` | A pageable asynchronous sequence of [AnswerRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.AnswerRecord) resources.  
**Example**
    
    
    // Create client
    AnswerRecordsClient answerRecordsClient = await AnswerRecordsClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListAnswerRecordsResponse, AnswerRecord> response = answerRecordsClient.ListAnswerRecordsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (AnswerRecord item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListAnswerRecordsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (AnswerRecord item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<AnswerRecord> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (AnswerRecord item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAnswerRecordsAsync(ProjectName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListAnswerRecordsResponse, AnswerRecord> ListAnswerRecordsAsync(ProjectName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Returns the list of all answer records in the specified project in reverse chronological order.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)`  
Required. The project to list all answer records for in reverse chronological order. Format: `projects/<Project ID>/locations/<Location ID>`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListAnswerRecordsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ListAnswerRecordsResponse)[AnswerRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.AnswerRecord)` | A pageable asynchronous sequence of [AnswerRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.AnswerRecord) resources.  
**Example**
    
    
    // Create client
    AnswerRecordsClient answerRecordsClient = await AnswerRecordsClient.CreateAsync();
    // Initialize request argument(s)
    ProjectName parent = ProjectName.FromProject("[PROJECT]");
    // Make the request
    PagedAsyncEnumerable<ListAnswerRecordsResponse, AnswerRecord> response = answerRecordsClient.ListAnswerRecordsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (AnswerRecord item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListAnswerRecordsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (AnswerRecord item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<AnswerRecord> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (AnswerRecord item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAnswerRecordsAsync(ListAnswerRecordsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListAnswerRecordsResponse, AnswerRecord> ListAnswerRecordsAsync(ListAnswerRecordsRequest request, CallSettings callSettings = null)

Returns the list of all answer records in the specified project in reverse chronological order.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAnswerRecordsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ListAnswerRecordsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListAnswerRecordsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ListAnswerRecordsResponse)[AnswerRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.AnswerRecord)` | A pageable asynchronous sequence of [AnswerRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.AnswerRecord) resources.  
**Example**
    
    
    // Create client
    AnswerRecordsClient answerRecordsClient = await AnswerRecordsClient.CreateAsync();
    // Initialize request argument(s)
    ListAnswerRecordsRequest request = new ListAnswerRecordsRequest
    {
        ParentAsProjectName = ProjectName.FromProject("[PROJECT]"),
        Filter = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListAnswerRecordsResponse, AnswerRecord> response = answerRecordsClient.ListAnswerRecordsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (AnswerRecord item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListAnswerRecordsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (AnswerRecord item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<AnswerRecord> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (AnswerRecord item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAnswerRecordsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListAnswerRecordsResponse, AnswerRecord> ListAnswerRecordsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Returns the list of all answer records in the specified project in reverse chronological order.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The project to list all answer records for in reverse chronological order. Format: `projects/<Project ID>/locations/<Location ID>`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListAnswerRecordsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ListAnswerRecordsResponse)[AnswerRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.AnswerRecord)` | A pageable asynchronous sequence of [AnswerRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.AnswerRecord) resources.  
**Example**
    
    
    // Create client
    AnswerRecordsClient answerRecordsClient = await AnswerRecordsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]";
    // Make the request
    PagedAsyncEnumerable<ListAnswerRecordsResponse, AnswerRecord> response = answerRecordsClient.ListAnswerRecordsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (AnswerRecord item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListAnswerRecordsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (AnswerRecord item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<AnswerRecord> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (AnswerRecord item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.AnswerRecordsClient#Google_Cloud_Dialogflow_V2Beta1_AnswerRecordsClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.AnswerRecordsClient#Google_Cloud_Dialogflow_V2Beta1_AnswerRecordsClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.AnswerRecordsClient#Google_Cloud_Dialogflow_V2Beta1_AnswerRecordsClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.AnswerRecordsClient#Google_Cloud_Dialogflow_V2Beta1_AnswerRecordsClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### UpdateAnswerRecord(AnswerRecord, FieldMask, CallSettings)
    
    
    public virtual AnswerRecord UpdateAnswerRecord(AnswerRecord answerRecord, FieldMask updateMask, CallSettings callSettings = null)

Updates the specified answer record.

**Parameters**  
---  
**Name** | **Description**  
`answerRecord` | `[AnswerRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.AnswerRecord)`  
Required. Answer record to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. The mask to control which fields get updated.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[AnswerRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.AnswerRecord)` | The RPC response.  
**Example**
    
    
    // Create client
    AnswerRecordsClient answerRecordsClient = AnswerRecordsClient.Create();
    // Initialize request argument(s)
    AnswerRecord answerRecord = new AnswerRecord();
    FieldMask updateMask = new FieldMask();
    // Make the request
    AnswerRecord response = answerRecordsClient.UpdateAnswerRecord(answerRecord, updateMask);
    

### UpdateAnswerRecord(UpdateAnswerRecordRequest, CallSettings)
    
    
    public virtual AnswerRecord UpdateAnswerRecord(UpdateAnswerRecordRequest request, CallSettings callSettings = null)

Updates the specified answer record.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAnswerRecordRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.UpdateAnswerRecordRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[AnswerRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.AnswerRecord)` | The RPC response.  
**Example**
    
    
    // Create client
    AnswerRecordsClient answerRecordsClient = AnswerRecordsClient.Create();
    // Initialize request argument(s)
    UpdateAnswerRecordRequest request = new UpdateAnswerRecordRequest
    {
        AnswerRecord = new AnswerRecord(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    AnswerRecord response = answerRecordsClient.UpdateAnswerRecord(request);
    

### UpdateAnswerRecordAsync(AnswerRecord, FieldMask, CallSettings)
    
    
    public virtual Task<AnswerRecord> UpdateAnswerRecordAsync(AnswerRecord answerRecord, FieldMask updateMask, CallSettings callSettings = null)

Updates the specified answer record.

**Parameters**  
---  
**Name** | **Description**  
`answerRecord` | `[AnswerRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.AnswerRecord)`  
Required. Answer record to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. The mask to control which fields get updated.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AnswerRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.AnswerRecord)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AnswerRecordsClient answerRecordsClient = await AnswerRecordsClient.CreateAsync();
    // Initialize request argument(s)
    AnswerRecord answerRecord = new AnswerRecord();
    FieldMask updateMask = new FieldMask();
    // Make the request
    AnswerRecord response = await answerRecordsClient.UpdateAnswerRecordAsync(answerRecord, updateMask);
    

### UpdateAnswerRecordAsync(AnswerRecord, FieldMask, CancellationToken)
    
    
    public virtual Task<AnswerRecord> UpdateAnswerRecordAsync(AnswerRecord answerRecord, FieldMask updateMask, CancellationToken cancellationToken)

Updates the specified answer record.

**Parameters**  
---  
**Name** | **Description**  
`answerRecord` | `[AnswerRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.AnswerRecord)`  
Required. Answer record to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. The mask to control which fields get updated.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AnswerRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.AnswerRecord)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AnswerRecordsClient answerRecordsClient = await AnswerRecordsClient.CreateAsync();
    // Initialize request argument(s)
    AnswerRecord answerRecord = new AnswerRecord();
    FieldMask updateMask = new FieldMask();
    // Make the request
    AnswerRecord response = await answerRecordsClient.UpdateAnswerRecordAsync(answerRecord, updateMask);
    

### UpdateAnswerRecordAsync(UpdateAnswerRecordRequest, CallSettings)
    
    
    public virtual Task<AnswerRecord> UpdateAnswerRecordAsync(UpdateAnswerRecordRequest request, CallSettings callSettings = null)

Updates the specified answer record.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAnswerRecordRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.UpdateAnswerRecordRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AnswerRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.AnswerRecord)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AnswerRecordsClient answerRecordsClient = await AnswerRecordsClient.CreateAsync();
    // Initialize request argument(s)
    UpdateAnswerRecordRequest request = new UpdateAnswerRecordRequest
    {
        AnswerRecord = new AnswerRecord(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    AnswerRecord response = await answerRecordsClient.UpdateAnswerRecordAsync(request);
    

### UpdateAnswerRecordAsync(UpdateAnswerRecordRequest, CancellationToken)
    
    
    public virtual Task<AnswerRecord> UpdateAnswerRecordAsync(UpdateAnswerRecordRequest request, CancellationToken cancellationToken)

Updates the specified answer record.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAnswerRecordRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.UpdateAnswerRecordRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AnswerRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.AnswerRecord)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AnswerRecordsClient answerRecordsClient = await AnswerRecordsClient.CreateAsync();
    // Initialize request argument(s)
    UpdateAnswerRecordRequest request = new UpdateAnswerRecordRequest
    {
        AnswerRecord = new AnswerRecord(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    AnswerRecord response = await answerRecordsClient.UpdateAnswerRecordAsync(request);
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
