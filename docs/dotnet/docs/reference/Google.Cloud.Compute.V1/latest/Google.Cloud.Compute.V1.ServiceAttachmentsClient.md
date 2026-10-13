---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachmentsClient
title: Compute Engine v1 API - Class ServiceAttachmentsClient (4.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:25:57.229808+00:00
---

# Compute Engine v1 API - Class ServiceAttachmentsClient (4.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachmentsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Compute Engine v1 API - Class ServiceAttachmentsClient (4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public abstract class ServiceAttachmentsClient

Reference documentation and code samples for the Compute Engine v1 API class ServiceAttachmentsClient.

ServiceAttachments client wrapper, for convenient use. This client implements API version 2026-09-01.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ServiceAttachmentsClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[ServiceAttachmentsClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachmentsClientImpl)

## Namespace

[Google.Cloud.Compute.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1)

## Assembly

Google.Cloud.Compute.V1.dll

## Remarks

The ServiceAttachments API.

## Properties 

### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the ServiceAttachments service, which is a host of "compute.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default ServiceAttachments scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default ServiceAttachments scopes are:

  * <https://www.googleapis.com/auth/compute>
  * <https://www.googleapis.com/auth/cloud-platform>



### DeleteOperationsClient
    
    
    public virtual OperationsClient DeleteOperationsClient { get; }

The long-running operations client for `Delete`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### GrpcClient
    
    
    public virtual ServiceAttachments.ServiceAttachmentsClient GrpcClient { get; }

The underlying gRPC ServiceAttachments client

**Property Value**  
---  
**Type** | **Description**  
`[ServiceAttachments](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachments)[ServiceAttachmentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachments.ServiceAttachmentsClient)` |   
  
### InsertOperationsClient
    
    
    public virtual OperationsClient InsertOperationsClient { get; }

The long-running operations client for `Insert`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### PatchOperationsClient
    
    
    public virtual OperationsClient PatchOperationsClient { get; }

The long-running operations client for `Patch`.

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

### AggregatedList(AggregatedListServiceAttachmentsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ServiceAttachmentAggregatedList, KeyValuePair<string, ServiceAttachmentsScopedList>> AggregatedList(AggregatedListServiceAttachmentsRequest request, CallSettings callSettings = null)

Retrieves the list of all ServiceAttachment resources, regional and global, available to the specified project.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AggregatedListServiceAttachmentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AggregatedListServiceAttachmentsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ServiceAttachmentAggregatedList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachmentAggregatedList)[KeyValuePair](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair-2)[string](https://learn.microsoft.com/dotnet/api/system.string)[ServiceAttachmentsScopedList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachmentsScopedList)` | A pageable sequence of [KeyValuePair<TKey, TValue>](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair-2) resources.  
**Example**
    
    
    // Create client
    ServiceAttachmentsClient serviceAttachmentsClient = ServiceAttachmentsClient.Create();
    // Initialize request argument(s)
    AggregatedListServiceAttachmentsRequest request = new AggregatedListServiceAttachmentsRequest
    {
        OrderBy = "",
        Project = "",
        ServiceProjectNumber = 0L,
        Filter = "",
        IncludeAllScopes = false,
    };
    // Make the request
    PagedEnumerable<ServiceAttachmentAggregatedList, KeyValuePair<string, ServiceAttachmentsScopedList>> response = serviceAttachmentsClient.AggregatedList(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (KeyValuePair<string, ServiceAttachmentsScopedList> item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ServiceAttachmentAggregatedList page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (KeyValuePair<string, ServiceAttachmentsScopedList> item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<KeyValuePair<string, ServiceAttachmentsScopedList>> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (KeyValuePair<string, ServiceAttachmentsScopedList> item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### AggregatedList(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ServiceAttachmentAggregatedList, KeyValuePair<string, ServiceAttachmentsScopedList>> AggregatedList(string project, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieves the list of all ServiceAttachment resources, regional and global, available to the specified project.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the project scoping this request.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ServiceAttachmentAggregatedList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachmentAggregatedList)[KeyValuePair](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair-2)[string](https://learn.microsoft.com/dotnet/api/system.string)[ServiceAttachmentsScopedList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachmentsScopedList)` | A pageable sequence of [KeyValuePair<TKey, TValue>](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair-2) resources.  
**Example**
    
    
    // Create client
    ServiceAttachmentsClient serviceAttachmentsClient = ServiceAttachmentsClient.Create();
    // Initialize request argument(s)
    string project = "";
    // Make the request
    PagedEnumerable<ServiceAttachmentAggregatedList, KeyValuePair<string, ServiceAttachmentsScopedList>> response = serviceAttachmentsClient.AggregatedList(project);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (KeyValuePair<string, ServiceAttachmentsScopedList> item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ServiceAttachmentAggregatedList page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (KeyValuePair<string, ServiceAttachmentsScopedList> item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<KeyValuePair<string, ServiceAttachmentsScopedList>> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (KeyValuePair<string, ServiceAttachmentsScopedList> item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### AggregatedListAsync(AggregatedListServiceAttachmentsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ServiceAttachmentAggregatedList, KeyValuePair<string, ServiceAttachmentsScopedList>> AggregatedListAsync(AggregatedListServiceAttachmentsRequest request, CallSettings callSettings = null)

Retrieves the list of all ServiceAttachment resources, regional and global, available to the specified project.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AggregatedListServiceAttachmentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AggregatedListServiceAttachmentsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ServiceAttachmentAggregatedList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachmentAggregatedList)[KeyValuePair](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair-2)[string](https://learn.microsoft.com/dotnet/api/system.string)[ServiceAttachmentsScopedList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachmentsScopedList)` | A pageable asynchronous sequence of [KeyValuePair<TKey, TValue>](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair-2) resources.  
**Example**
    
    
    // Create client
    ServiceAttachmentsClient serviceAttachmentsClient = await ServiceAttachmentsClient.CreateAsync();
    // Initialize request argument(s)
    AggregatedListServiceAttachmentsRequest request = new AggregatedListServiceAttachmentsRequest
    {
        OrderBy = "",
        Project = "",
        ServiceProjectNumber = 0L,
        Filter = "",
        IncludeAllScopes = false,
    };
    // Make the request
    PagedAsyncEnumerable<ServiceAttachmentAggregatedList, KeyValuePair<string, ServiceAttachmentsScopedList>> response = serviceAttachmentsClient.AggregatedListAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (KeyValuePair<string, ServiceAttachmentsScopedList> item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ServiceAttachmentAggregatedList page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (KeyValuePair<string, ServiceAttachmentsScopedList> item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<KeyValuePair<string, ServiceAttachmentsScopedList>> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (KeyValuePair<string, ServiceAttachmentsScopedList> item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### AggregatedListAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ServiceAttachmentAggregatedList, KeyValuePair<string, ServiceAttachmentsScopedList>> AggregatedListAsync(string project, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieves the list of all ServiceAttachment resources, regional and global, available to the specified project.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the project scoping this request.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ServiceAttachmentAggregatedList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachmentAggregatedList)[KeyValuePair](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair-2)[string](https://learn.microsoft.com/dotnet/api/system.string)[ServiceAttachmentsScopedList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachmentsScopedList)` | A pageable asynchronous sequence of [KeyValuePair<TKey, TValue>](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair-2) resources.  
**Example**
    
    
    // Create client
    ServiceAttachmentsClient serviceAttachmentsClient = await ServiceAttachmentsClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    // Make the request
    PagedAsyncEnumerable<ServiceAttachmentAggregatedList, KeyValuePair<string, ServiceAttachmentsScopedList>> response = serviceAttachmentsClient.AggregatedListAsync(project);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (KeyValuePair<string, ServiceAttachmentsScopedList> item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ServiceAttachmentAggregatedList page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (KeyValuePair<string, ServiceAttachmentsScopedList> item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<KeyValuePair<string, ServiceAttachmentsScopedList>> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (KeyValuePair<string, ServiceAttachmentsScopedList> item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### Create()
    
    
    public static ServiceAttachmentsClient Create()

Synchronously creates a [ServiceAttachmentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachmentsClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [ServiceAttachmentsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachmentsClientBuilder) .

**Returns**  
---  
**Type** | **Description**  
`[ServiceAttachmentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachmentsClient)` | The created [ServiceAttachmentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachmentsClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<ServiceAttachmentsClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [ServiceAttachmentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachmentsClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [ServiceAttachmentsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachmentsClientBuilder) .

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ServiceAttachmentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachmentsClient)` | The task representing the created [ServiceAttachmentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachmentsClient).  
  
### Delete(DeleteServiceAttachmentRequest, CallSettings)
    
    
    public virtual Operation<Operation, Operation> Delete(DeleteServiceAttachmentRequest request, CallSettings callSettings = null)

Deletes the specified ServiceAttachment in the given scope

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteServiceAttachmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.DeleteServiceAttachmentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The RPC response.  
**Example**
    
    
    // Create client
    ServiceAttachmentsClient serviceAttachmentsClient = ServiceAttachmentsClient.Create();
    // Initialize request argument(s)
    DeleteServiceAttachmentRequest request = new DeleteServiceAttachmentRequest
    {
        RequestId = "",
        Region = "",
        Project = "",
        ServiceAttachment = "",
    };
    // Make the request
    lro::Operation<Operation, Operation> response = serviceAttachmentsClient.Delete(request);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = serviceAttachmentsClient.PollOnceDelete(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### Delete(string, string, string, CallSettings)
    
    
    public virtual Operation<Operation, Operation> Delete(string project, string region, string serviceAttachment, CallSettings callSettings = null)

Deletes the specified ServiceAttachment in the given scope

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the region of this request.  
`serviceAttachment` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the ServiceAttachment resource to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The RPC response.  
**Example**
    
    
    // Create client
    ServiceAttachmentsClient serviceAttachmentsClient = ServiceAttachmentsClient.Create();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    string serviceAttachment = "";
    // Make the request
    lro::Operation<Operation, Operation> response = serviceAttachmentsClient.Delete(project, region, serviceAttachment);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = serviceAttachmentsClient.PollOnceDelete(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### DeleteAsync(DeleteServiceAttachmentRequest, CallSettings)
    
    
    public virtual Task<Operation<Operation, Operation>> DeleteAsync(DeleteServiceAttachmentRequest request, CallSettings callSettings = null)

Deletes the specified ServiceAttachment in the given scope

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteServiceAttachmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.DeleteServiceAttachmentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ServiceAttachmentsClient serviceAttachmentsClient = await ServiceAttachmentsClient.CreateAsync();
    // Initialize request argument(s)
    DeleteServiceAttachmentRequest request = new DeleteServiceAttachmentRequest
    {
        RequestId = "",
        Region = "",
        Project = "",
        ServiceAttachment = "",
    };
    // Make the request
    lro::Operation<Operation, Operation> response = await serviceAttachmentsClient.DeleteAsync(request);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = await serviceAttachmentsClient.PollOnceDeleteAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### DeleteAsync(DeleteServiceAttachmentRequest, CancellationToken)
    
    
    public virtual Task<Operation<Operation, Operation>> DeleteAsync(DeleteServiceAttachmentRequest request, CancellationToken cancellationToken)

Deletes the specified ServiceAttachment in the given scope

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteServiceAttachmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.DeleteServiceAttachmentRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ServiceAttachmentsClient serviceAttachmentsClient = await ServiceAttachmentsClient.CreateAsync();
    // Initialize request argument(s)
    DeleteServiceAttachmentRequest request = new DeleteServiceAttachmentRequest
    {
        RequestId = "",
        Region = "",
        Project = "",
        ServiceAttachment = "",
    };
    // Make the request
    lro::Operation<Operation, Operation> response = await serviceAttachmentsClient.DeleteAsync(request);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = await serviceAttachmentsClient.PollOnceDeleteAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### DeleteAsync(string, string, string, CallSettings)
    
    
    public virtual Task<Operation<Operation, Operation>> DeleteAsync(string project, string region, string serviceAttachment, CallSettings callSettings = null)

Deletes the specified ServiceAttachment in the given scope

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the region of this request.  
`serviceAttachment` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the ServiceAttachment resource to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ServiceAttachmentsClient serviceAttachmentsClient = await ServiceAttachmentsClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    string serviceAttachment = "";
    // Make the request
    lro::Operation<Operation, Operation> response = await serviceAttachmentsClient.DeleteAsync(project, region, serviceAttachment);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = await serviceAttachmentsClient.PollOnceDeleteAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### DeleteAsync(string, string, string, CancellationToken)
    
    
    public virtual Task<Operation<Operation, Operation>> DeleteAsync(string project, string region, string serviceAttachment, CancellationToken cancellationToken)

Deletes the specified ServiceAttachment in the given scope

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the region of this request.  
`serviceAttachment` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the ServiceAttachment resource to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ServiceAttachmentsClient serviceAttachmentsClient = await ServiceAttachmentsClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    string serviceAttachment = "";
    // Make the request
    lro::Operation<Operation, Operation> response = await serviceAttachmentsClient.DeleteAsync(project, region, serviceAttachment);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = await serviceAttachmentsClient.PollOnceDeleteAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### Get(GetServiceAttachmentRequest, CallSettings)
    
    
    public virtual ServiceAttachment Get(GetServiceAttachmentRequest request, CallSettings callSettings = null)

Returns the specified ServiceAttachment resource in the given scope.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetServiceAttachmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetServiceAttachmentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ServiceAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachment)` | The RPC response.  
**Example**
    
    
    // Create client
    ServiceAttachmentsClient serviceAttachmentsClient = ServiceAttachmentsClient.Create();
    // Initialize request argument(s)
    GetServiceAttachmentRequest request = new GetServiceAttachmentRequest
    {
        Region = "",
        Project = "",
        ServiceAttachment = "",
        ShowNatIps = false,
    };
    // Make the request
    ServiceAttachment response = serviceAttachmentsClient.Get(request);
    

### Get(string, string, string, CallSettings)
    
    
    public virtual ServiceAttachment Get(string project, string region, string serviceAttachment, CallSettings callSettings = null)

Returns the specified ServiceAttachment resource in the given scope.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the region of this request.  
`serviceAttachment` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the ServiceAttachment resource to return.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ServiceAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachment)` | The RPC response.  
**Example**
    
    
    // Create client
    ServiceAttachmentsClient serviceAttachmentsClient = ServiceAttachmentsClient.Create();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    string serviceAttachment = "";
    // Make the request
    ServiceAttachment response = serviceAttachmentsClient.Get(project, region, serviceAttachment);
    

### GetAsync(GetServiceAttachmentRequest, CallSettings)
    
    
    public virtual Task<ServiceAttachment> GetAsync(GetServiceAttachmentRequest request, CallSettings callSettings = null)

Returns the specified ServiceAttachment resource in the given scope.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetServiceAttachmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetServiceAttachmentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ServiceAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachment)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ServiceAttachmentsClient serviceAttachmentsClient = await ServiceAttachmentsClient.CreateAsync();
    // Initialize request argument(s)
    GetServiceAttachmentRequest request = new GetServiceAttachmentRequest
    {
        Region = "",
        Project = "",
        ServiceAttachment = "",
        ShowNatIps = false,
    };
    // Make the request
    ServiceAttachment response = await serviceAttachmentsClient.GetAsync(request);
    

### GetAsync(GetServiceAttachmentRequest, CancellationToken)
    
    
    public virtual Task<ServiceAttachment> GetAsync(GetServiceAttachmentRequest request, CancellationToken cancellationToken)

Returns the specified ServiceAttachment resource in the given scope.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetServiceAttachmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetServiceAttachmentRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ServiceAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachment)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ServiceAttachmentsClient serviceAttachmentsClient = await ServiceAttachmentsClient.CreateAsync();
    // Initialize request argument(s)
    GetServiceAttachmentRequest request = new GetServiceAttachmentRequest
    {
        Region = "",
        Project = "",
        ServiceAttachment = "",
        ShowNatIps = false,
    };
    // Make the request
    ServiceAttachment response = await serviceAttachmentsClient.GetAsync(request);
    

### GetAsync(string, string, string, CallSettings)
    
    
    public virtual Task<ServiceAttachment> GetAsync(string project, string region, string serviceAttachment, CallSettings callSettings = null)

Returns the specified ServiceAttachment resource in the given scope.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the region of this request.  
`serviceAttachment` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the ServiceAttachment resource to return.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ServiceAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachment)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ServiceAttachmentsClient serviceAttachmentsClient = await ServiceAttachmentsClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    string serviceAttachment = "";
    // Make the request
    ServiceAttachment response = await serviceAttachmentsClient.GetAsync(project, region, serviceAttachment);
    

### GetAsync(string, string, string, CancellationToken)
    
    
    public virtual Task<ServiceAttachment> GetAsync(string project, string region, string serviceAttachment, CancellationToken cancellationToken)

Returns the specified ServiceAttachment resource in the given scope.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the region of this request.  
`serviceAttachment` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the ServiceAttachment resource to return.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ServiceAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachment)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ServiceAttachmentsClient serviceAttachmentsClient = await ServiceAttachmentsClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    string serviceAttachment = "";
    // Make the request
    ServiceAttachment response = await serviceAttachmentsClient.GetAsync(project, region, serviceAttachment);
    

### GetIamPolicy(GetIamPolicyServiceAttachmentRequest, CallSettings)
    
    
    public virtual Policy GetIamPolicy(GetIamPolicyServiceAttachmentRequest request, CallSettings callSettings = null)

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetIamPolicyServiceAttachmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetIamPolicyServiceAttachmentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Policy)` | The RPC response.  
**Example**
    
    
    // Create client
    ServiceAttachmentsClient serviceAttachmentsClient = ServiceAttachmentsClient.Create();
    // Initialize request argument(s)
    GetIamPolicyServiceAttachmentRequest request = new GetIamPolicyServiceAttachmentRequest
    {
        Region = "",
        Resource = "",
        Project = "",
        OptionsRequestedPolicyVersion = 0,
    };
    // Make the request
    Policy response = serviceAttachmentsClient.GetIamPolicy(request);
    

### GetIamPolicy(string, string, string, CallSettings)
    
    
    public virtual Policy GetIamPolicy(string project, string region, string resource, CallSettings callSettings = null)

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the region for this request.  
`resource` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name or id of the resource for this request.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Policy)` | The RPC response.  
**Example**
    
    
    // Create client
    ServiceAttachmentsClient serviceAttachmentsClient = ServiceAttachmentsClient.Create();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    string resource = "";
    // Make the request
    Policy response = serviceAttachmentsClient.GetIamPolicy(project, region, resource);
    

### GetIamPolicyAsync(GetIamPolicyServiceAttachmentRequest, CallSettings)
    
    
    public virtual Task<Policy> GetIamPolicyAsync(GetIamPolicyServiceAttachmentRequest request, CallSettings callSettings = null)

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetIamPolicyServiceAttachmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetIamPolicyServiceAttachmentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Policy)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ServiceAttachmentsClient serviceAttachmentsClient = await ServiceAttachmentsClient.CreateAsync();
    // Initialize request argument(s)
    GetIamPolicyServiceAttachmentRequest request = new GetIamPolicyServiceAttachmentRequest
    {
        Region = "",
        Resource = "",
        Project = "",
        OptionsRequestedPolicyVersion = 0,
    };
    // Make the request
    Policy response = await serviceAttachmentsClient.GetIamPolicyAsync(request);
    

### GetIamPolicyAsync(GetIamPolicyServiceAttachmentRequest, CancellationToken)
    
    
    public virtual Task<Policy> GetIamPolicyAsync(GetIamPolicyServiceAttachmentRequest request, CancellationToken cancellationToken)

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetIamPolicyServiceAttachmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetIamPolicyServiceAttachmentRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Policy)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ServiceAttachmentsClient serviceAttachmentsClient = await ServiceAttachmentsClient.CreateAsync();
    // Initialize request argument(s)
    GetIamPolicyServiceAttachmentRequest request = new GetIamPolicyServiceAttachmentRequest
    {
        Region = "",
        Resource = "",
        Project = "",
        OptionsRequestedPolicyVersion = 0,
    };
    // Make the request
    Policy response = await serviceAttachmentsClient.GetIamPolicyAsync(request);
    

### GetIamPolicyAsync(string, string, string, CallSettings)
    
    
    public virtual Task<Policy> GetIamPolicyAsync(string project, string region, string resource, CallSettings callSettings = null)

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the region for this request.  
`resource` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name or id of the resource for this request.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Policy)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ServiceAttachmentsClient serviceAttachmentsClient = await ServiceAttachmentsClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    string resource = "";
    // Make the request
    Policy response = await serviceAttachmentsClient.GetIamPolicyAsync(project, region, resource);
    

### GetIamPolicyAsync(string, string, string, CancellationToken)
    
    
    public virtual Task<Policy> GetIamPolicyAsync(string project, string region, string resource, CancellationToken cancellationToken)

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the region for this request.  
`resource` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name or id of the resource for this request.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Policy)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ServiceAttachmentsClient serviceAttachmentsClient = await ServiceAttachmentsClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    string resource = "";
    // Make the request
    Policy response = await serviceAttachmentsClient.GetIamPolicyAsync(project, region, resource);
    

### Insert(InsertServiceAttachmentRequest, CallSettings)
    
    
    public virtual Operation<Operation, Operation> Insert(InsertServiceAttachmentRequest request, CallSettings callSettings = null)

Creates a ServiceAttachment in the specified project in the given scope using the parameters that are included in the request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[InsertServiceAttachmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InsertServiceAttachmentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The RPC response.  
**Example**
    
    
    // Create client
    ServiceAttachmentsClient serviceAttachmentsClient = ServiceAttachmentsClient.Create();
    // Initialize request argument(s)
    InsertServiceAttachmentRequest request = new InsertServiceAttachmentRequest
    {
        RequestId = "",
        Region = "",
        Project = "",
        ServiceAttachmentResource = new ServiceAttachment(),
    };
    // Make the request
    lro::Operation<Operation, Operation> response = serviceAttachmentsClient.Insert(request);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = serviceAttachmentsClient.PollOnceInsert(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### Insert(string, string, ServiceAttachment, CallSettings)
    
    
    public virtual Operation<Operation, Operation> Insert(string project, string region, ServiceAttachment serviceAttachmentResource, CallSettings callSettings = null)

Creates a ServiceAttachment in the specified project in the given scope using the parameters that are included in the request.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the region of this request.  
`serviceAttachmentResource` | `[ServiceAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachment)`  
The body resource for this request  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The RPC response.  
**Example**
    
    
    // Create client
    ServiceAttachmentsClient serviceAttachmentsClient = ServiceAttachmentsClient.Create();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    ServiceAttachment serviceAttachmentResource = new ServiceAttachment();
    // Make the request
    lro::Operation<Operation, Operation> response = serviceAttachmentsClient.Insert(project, region, serviceAttachmentResource);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = serviceAttachmentsClient.PollOnceInsert(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### InsertAsync(InsertServiceAttachmentRequest, CallSettings)
    
    
    public virtual Task<Operation<Operation, Operation>> InsertAsync(InsertServiceAttachmentRequest request, CallSettings callSettings = null)

Creates a ServiceAttachment in the specified project in the given scope using the parameters that are included in the request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[InsertServiceAttachmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InsertServiceAttachmentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ServiceAttachmentsClient serviceAttachmentsClient = await ServiceAttachmentsClient.CreateAsync();
    // Initialize request argument(s)
    InsertServiceAttachmentRequest request = new InsertServiceAttachmentRequest
    {
        RequestId = "",
        Region = "",
        Project = "",
        ServiceAttachmentResource = new ServiceAttachment(),
    };
    // Make the request
    lro::Operation<Operation, Operation> response = await serviceAttachmentsClient.InsertAsync(request);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = await serviceAttachmentsClient.PollOnceInsertAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### InsertAsync(InsertServiceAttachmentRequest, CancellationToken)
    
    
    public virtual Task<Operation<Operation, Operation>> InsertAsync(InsertServiceAttachmentRequest request, CancellationToken cancellationToken)

Creates a ServiceAttachment in the specified project in the given scope using the parameters that are included in the request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[InsertServiceAttachmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InsertServiceAttachmentRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ServiceAttachmentsClient serviceAttachmentsClient = await ServiceAttachmentsClient.CreateAsync();
    // Initialize request argument(s)
    InsertServiceAttachmentRequest request = new InsertServiceAttachmentRequest
    {
        RequestId = "",
        Region = "",
        Project = "",
        ServiceAttachmentResource = new ServiceAttachment(),
    };
    // Make the request
    lro::Operation<Operation, Operation> response = await serviceAttachmentsClient.InsertAsync(request);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = await serviceAttachmentsClient.PollOnceInsertAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### InsertAsync(string, string, ServiceAttachment, CallSettings)
    
    
    public virtual Task<Operation<Operation, Operation>> InsertAsync(string project, string region, ServiceAttachment serviceAttachmentResource, CallSettings callSettings = null)

Creates a ServiceAttachment in the specified project in the given scope using the parameters that are included in the request.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the region of this request.  
`serviceAttachmentResource` | `[ServiceAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachment)`  
The body resource for this request  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ServiceAttachmentsClient serviceAttachmentsClient = await ServiceAttachmentsClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    ServiceAttachment serviceAttachmentResource = new ServiceAttachment();
    // Make the request
    lro::Operation<Operation, Operation> response = await serviceAttachmentsClient.InsertAsync(project, region, serviceAttachmentResource);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = await serviceAttachmentsClient.PollOnceInsertAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### InsertAsync(string, string, ServiceAttachment, CancellationToken)
    
    
    public virtual Task<Operation<Operation, Operation>> InsertAsync(string project, string region, ServiceAttachment serviceAttachmentResource, CancellationToken cancellationToken)

Creates a ServiceAttachment in the specified project in the given scope using the parameters that are included in the request.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the region of this request.  
`serviceAttachmentResource` | `[ServiceAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachment)`  
The body resource for this request  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ServiceAttachmentsClient serviceAttachmentsClient = await ServiceAttachmentsClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    ServiceAttachment serviceAttachmentResource = new ServiceAttachment();
    // Make the request
    lro::Operation<Operation, Operation> response = await serviceAttachmentsClient.InsertAsync(project, region, serviceAttachmentResource);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = await serviceAttachmentsClient.PollOnceInsertAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### List(ListServiceAttachmentsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ServiceAttachmentList, ServiceAttachment> List(ListServiceAttachmentsRequest request, CallSettings callSettings = null)

Lists the ServiceAttachments for a project in the given scope.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListServiceAttachmentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ListServiceAttachmentsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ServiceAttachmentList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachmentList)[ServiceAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachment)` | A pageable sequence of [ServiceAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachment) resources.  
**Example**
    
    
    // Create client
    ServiceAttachmentsClient serviceAttachmentsClient = ServiceAttachmentsClient.Create();
    // Initialize request argument(s)
    ListServiceAttachmentsRequest request = new ListServiceAttachmentsRequest
    {
        Region = "",
        OrderBy = "",
        Project = "",
        Filter = "",
    };
    // Make the request
    PagedEnumerable<ServiceAttachmentList, ServiceAttachment> response = serviceAttachmentsClient.List(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (ServiceAttachment item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ServiceAttachmentList page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ServiceAttachment item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ServiceAttachment> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ServiceAttachment item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### List(string, string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ServiceAttachmentList, ServiceAttachment> List(string project, string region, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the ServiceAttachments for a project in the given scope.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the region of this request.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ServiceAttachmentList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachmentList)[ServiceAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachment)` | A pageable sequence of [ServiceAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachment) resources.  
**Example**
    
    
    // Create client
    ServiceAttachmentsClient serviceAttachmentsClient = ServiceAttachmentsClient.Create();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    // Make the request
    PagedEnumerable<ServiceAttachmentList, ServiceAttachment> response = serviceAttachmentsClient.List(project, region);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (ServiceAttachment item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ServiceAttachmentList page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ServiceAttachment item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ServiceAttachment> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ServiceAttachment item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAsync(ListServiceAttachmentsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ServiceAttachmentList, ServiceAttachment> ListAsync(ListServiceAttachmentsRequest request, CallSettings callSettings = null)

Lists the ServiceAttachments for a project in the given scope.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListServiceAttachmentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ListServiceAttachmentsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ServiceAttachmentList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachmentList)[ServiceAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachment)` | A pageable asynchronous sequence of [ServiceAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachment) resources.  
**Example**
    
    
    // Create client
    ServiceAttachmentsClient serviceAttachmentsClient = await ServiceAttachmentsClient.CreateAsync();
    // Initialize request argument(s)
    ListServiceAttachmentsRequest request = new ListServiceAttachmentsRequest
    {
        Region = "",
        OrderBy = "",
        Project = "",
        Filter = "",
    };
    // Make the request
    PagedAsyncEnumerable<ServiceAttachmentList, ServiceAttachment> response = serviceAttachmentsClient.ListAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (ServiceAttachment item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ServiceAttachmentList page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ServiceAttachment item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ServiceAttachment> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ServiceAttachment item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAsync(string, string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ServiceAttachmentList, ServiceAttachment> ListAsync(string project, string region, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the ServiceAttachments for a project in the given scope.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the region of this request.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ServiceAttachmentList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachmentList)[ServiceAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachment)` | A pageable asynchronous sequence of [ServiceAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachment) resources.  
**Example**
    
    
    // Create client
    ServiceAttachmentsClient serviceAttachmentsClient = await ServiceAttachmentsClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    // Make the request
    PagedAsyncEnumerable<ServiceAttachmentList, ServiceAttachment> response = serviceAttachmentsClient.ListAsync(project, region);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (ServiceAttachment item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ServiceAttachmentList page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ServiceAttachment item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ServiceAttachment> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ServiceAttachment item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### Patch(PatchServiceAttachmentRequest, CallSettings)
    
    
    public virtual Operation<Operation, Operation> Patch(PatchServiceAttachmentRequest request, CallSettings callSettings = null)

Patches the specified ServiceAttachment resource with the data included in the request. This method supports PATCH semantics and usesJSON merge patch format and processing rules.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PatchServiceAttachmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.PatchServiceAttachmentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The RPC response.  
**Example**
    
    
    // Create client
    ServiceAttachmentsClient serviceAttachmentsClient = ServiceAttachmentsClient.Create();
    // Initialize request argument(s)
    PatchServiceAttachmentRequest request = new PatchServiceAttachmentRequest
    {
        RequestId = "",
        Region = "",
        Project = "",
        ServiceAttachment = "",
        ServiceAttachmentResource = new ServiceAttachment(),
    };
    // Make the request
    lro::Operation<Operation, Operation> response = serviceAttachmentsClient.Patch(request);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = serviceAttachmentsClient.PollOncePatch(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### Patch(string, string, string, ServiceAttachment, CallSettings)
    
    
    public virtual Operation<Operation, Operation> Patch(string project, string region, string serviceAttachment, ServiceAttachment serviceAttachmentResource, CallSettings callSettings = null)

Patches the specified ServiceAttachment resource with the data included in the request. This method supports PATCH semantics and usesJSON merge patch format and processing rules.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The region scoping this request and should conform to RFC1035.  
`serviceAttachment` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource id of the ServiceAttachment to patch. It should conform to RFC1035 resource name or be a string form on an unsigned long number.  
`serviceAttachmentResource` | `[ServiceAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachment)`  
The body resource for this request  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The RPC response.  
**Example**
    
    
    // Create client
    ServiceAttachmentsClient serviceAttachmentsClient = ServiceAttachmentsClient.Create();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    string serviceAttachment = "";
    ServiceAttachment serviceAttachmentResource = new ServiceAttachment();
    // Make the request
    lro::Operation<Operation, Operation> response = serviceAttachmentsClient.Patch(project, region, serviceAttachment, serviceAttachmentResource);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = serviceAttachmentsClient.PollOncePatch(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### PatchAsync(PatchServiceAttachmentRequest, CallSettings)
    
    
    public virtual Task<Operation<Operation, Operation>> PatchAsync(PatchServiceAttachmentRequest request, CallSettings callSettings = null)

Patches the specified ServiceAttachment resource with the data included in the request. This method supports PATCH semantics and usesJSON merge patch format and processing rules.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PatchServiceAttachmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.PatchServiceAttachmentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ServiceAttachmentsClient serviceAttachmentsClient = await ServiceAttachmentsClient.CreateAsync();
    // Initialize request argument(s)
    PatchServiceAttachmentRequest request = new PatchServiceAttachmentRequest
    {
        RequestId = "",
        Region = "",
        Project = "",
        ServiceAttachment = "",
        ServiceAttachmentResource = new ServiceAttachment(),
    };
    // Make the request
    lro::Operation<Operation, Operation> response = await serviceAttachmentsClient.PatchAsync(request);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = await serviceAttachmentsClient.PollOncePatchAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### PatchAsync(PatchServiceAttachmentRequest, CancellationToken)
    
    
    public virtual Task<Operation<Operation, Operation>> PatchAsync(PatchServiceAttachmentRequest request, CancellationToken cancellationToken)

Patches the specified ServiceAttachment resource with the data included in the request. This method supports PATCH semantics and usesJSON merge patch format and processing rules.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PatchServiceAttachmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.PatchServiceAttachmentRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ServiceAttachmentsClient serviceAttachmentsClient = await ServiceAttachmentsClient.CreateAsync();
    // Initialize request argument(s)
    PatchServiceAttachmentRequest request = new PatchServiceAttachmentRequest
    {
        RequestId = "",
        Region = "",
        Project = "",
        ServiceAttachment = "",
        ServiceAttachmentResource = new ServiceAttachment(),
    };
    // Make the request
    lro::Operation<Operation, Operation> response = await serviceAttachmentsClient.PatchAsync(request);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = await serviceAttachmentsClient.PollOncePatchAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### PatchAsync(string, string, string, ServiceAttachment, CallSettings)
    
    
    public virtual Task<Operation<Operation, Operation>> PatchAsync(string project, string region, string serviceAttachment, ServiceAttachment serviceAttachmentResource, CallSettings callSettings = null)

Patches the specified ServiceAttachment resource with the data included in the request. This method supports PATCH semantics and usesJSON merge patch format and processing rules.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The region scoping this request and should conform to RFC1035.  
`serviceAttachment` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource id of the ServiceAttachment to patch. It should conform to RFC1035 resource name or be a string form on an unsigned long number.  
`serviceAttachmentResource` | `[ServiceAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachment)`  
The body resource for this request  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ServiceAttachmentsClient serviceAttachmentsClient = await ServiceAttachmentsClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    string serviceAttachment = "";
    ServiceAttachment serviceAttachmentResource = new ServiceAttachment();
    // Make the request
    lro::Operation<Operation, Operation> response = await serviceAttachmentsClient.PatchAsync(project, region, serviceAttachment, serviceAttachmentResource);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = await serviceAttachmentsClient.PollOncePatchAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### PatchAsync(string, string, string, ServiceAttachment, CancellationToken)
    
    
    public virtual Task<Operation<Operation, Operation>> PatchAsync(string project, string region, string serviceAttachment, ServiceAttachment serviceAttachmentResource, CancellationToken cancellationToken)

Patches the specified ServiceAttachment resource with the data included in the request. This method supports PATCH semantics and usesJSON merge patch format and processing rules.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The region scoping this request and should conform to RFC1035.  
`serviceAttachment` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource id of the ServiceAttachment to patch. It should conform to RFC1035 resource name or be a string form on an unsigned long number.  
`serviceAttachmentResource` | `[ServiceAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachment)`  
The body resource for this request  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ServiceAttachmentsClient serviceAttachmentsClient = await ServiceAttachmentsClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    string serviceAttachment = "";
    ServiceAttachment serviceAttachmentResource = new ServiceAttachment();
    // Make the request
    lro::Operation<Operation, Operation> response = await serviceAttachmentsClient.PatchAsync(project, region, serviceAttachment, serviceAttachmentResource);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = await serviceAttachmentsClient.PollOncePatchAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### PollOnceDelete(string, CallSettings)
    
    
    public virtual Operation<Operation, Operation> PollOnceDelete(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `Delete`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The result of polling the operation.  
  
### PollOnceDeleteAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Operation, Operation>> PollOnceDeleteAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `Delete` .

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A task representing the result of polling the operation.  
  
### PollOnceInsert(string, CallSettings)
    
    
    public virtual Operation<Operation, Operation> PollOnceInsert(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `Insert`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The result of polling the operation.  
  
### PollOnceInsertAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Operation, Operation>> PollOnceInsertAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `Insert` .

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A task representing the result of polling the operation.  
  
### PollOncePatch(string, CallSettings)
    
    
    public virtual Operation<Operation, Operation> PollOncePatch(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `Patch`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The result of polling the operation.  
  
### PollOncePatchAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Operation, Operation>> PollOncePatchAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `Patch` .

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A task representing the result of polling the operation.  
  
### SetIamPolicy(SetIamPolicyServiceAttachmentRequest, CallSettings)
    
    
    public virtual Policy SetIamPolicy(SetIamPolicyServiceAttachmentRequest request, CallSettings callSettings = null)

Sets the access control policy on the specified resource. Replaces any existing policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetIamPolicyServiceAttachmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SetIamPolicyServiceAttachmentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Policy)` | The RPC response.  
**Example**
    
    
    // Create client
    ServiceAttachmentsClient serviceAttachmentsClient = ServiceAttachmentsClient.Create();
    // Initialize request argument(s)
    SetIamPolicyServiceAttachmentRequest request = new SetIamPolicyServiceAttachmentRequest
    {
        Region = "",
        Resource = "",
        Project = "",
        RegionSetPolicyRequestResource = new RegionSetPolicyRequest(),
    };
    // Make the request
    Policy response = serviceAttachmentsClient.SetIamPolicy(request);
    

### SetIamPolicy(string, string, string, RegionSetPolicyRequest, CallSettings)
    
    
    public virtual Policy SetIamPolicy(string project, string region, string resource, RegionSetPolicyRequest regionSetPolicyRequestResource, CallSettings callSettings = null)

Sets the access control policy on the specified resource. Replaces any existing policy.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the region for this request.  
`resource` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name or id of the resource for this request.  
`regionSetPolicyRequestResource` | `[RegionSetPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSetPolicyRequest)`  
The body resource for this request  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Policy)` | The RPC response.  
**Example**
    
    
    // Create client
    ServiceAttachmentsClient serviceAttachmentsClient = ServiceAttachmentsClient.Create();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    string resource = "";
    RegionSetPolicyRequest regionSetPolicyRequestResource = new RegionSetPolicyRequest();
    // Make the request
    Policy response = serviceAttachmentsClient.SetIamPolicy(project, region, resource, regionSetPolicyRequestResource);
    

### SetIamPolicyAsync(SetIamPolicyServiceAttachmentRequest, CallSettings)
    
    
    public virtual Task<Policy> SetIamPolicyAsync(SetIamPolicyServiceAttachmentRequest request, CallSettings callSettings = null)

Sets the access control policy on the specified resource. Replaces any existing policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetIamPolicyServiceAttachmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SetIamPolicyServiceAttachmentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Policy)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ServiceAttachmentsClient serviceAttachmentsClient = await ServiceAttachmentsClient.CreateAsync();
    // Initialize request argument(s)
    SetIamPolicyServiceAttachmentRequest request = new SetIamPolicyServiceAttachmentRequest
    {
        Region = "",
        Resource = "",
        Project = "",
        RegionSetPolicyRequestResource = new RegionSetPolicyRequest(),
    };
    // Make the request
    Policy response = await serviceAttachmentsClient.SetIamPolicyAsync(request);
    

### SetIamPolicyAsync(SetIamPolicyServiceAttachmentRequest, CancellationToken)
    
    
    public virtual Task<Policy> SetIamPolicyAsync(SetIamPolicyServiceAttachmentRequest request, CancellationToken cancellationToken)

Sets the access control policy on the specified resource. Replaces any existing policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetIamPolicyServiceAttachmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SetIamPolicyServiceAttachmentRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Policy)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ServiceAttachmentsClient serviceAttachmentsClient = await ServiceAttachmentsClient.CreateAsync();
    // Initialize request argument(s)
    SetIamPolicyServiceAttachmentRequest request = new SetIamPolicyServiceAttachmentRequest
    {
        Region = "",
        Resource = "",
        Project = "",
        RegionSetPolicyRequestResource = new RegionSetPolicyRequest(),
    };
    // Make the request
    Policy response = await serviceAttachmentsClient.SetIamPolicyAsync(request);
    

### SetIamPolicyAsync(string, string, string, RegionSetPolicyRequest, CallSettings)
    
    
    public virtual Task<Policy> SetIamPolicyAsync(string project, string region, string resource, RegionSetPolicyRequest regionSetPolicyRequestResource, CallSettings callSettings = null)

Sets the access control policy on the specified resource. Replaces any existing policy.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the region for this request.  
`resource` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name or id of the resource for this request.  
`regionSetPolicyRequestResource` | `[RegionSetPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSetPolicyRequest)`  
The body resource for this request  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Policy)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ServiceAttachmentsClient serviceAttachmentsClient = await ServiceAttachmentsClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    string resource = "";
    RegionSetPolicyRequest regionSetPolicyRequestResource = new RegionSetPolicyRequest();
    // Make the request
    Policy response = await serviceAttachmentsClient.SetIamPolicyAsync(project, region, resource, regionSetPolicyRequestResource);
    

### SetIamPolicyAsync(string, string, string, RegionSetPolicyRequest, CancellationToken)
    
    
    public virtual Task<Policy> SetIamPolicyAsync(string project, string region, string resource, RegionSetPolicyRequest regionSetPolicyRequestResource, CancellationToken cancellationToken)

Sets the access control policy on the specified resource. Replaces any existing policy.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the region for this request.  
`resource` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name or id of the resource for this request.  
`regionSetPolicyRequestResource` | `[RegionSetPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSetPolicyRequest)`  
The body resource for this request  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Policy)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ServiceAttachmentsClient serviceAttachmentsClient = await ServiceAttachmentsClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    string resource = "";
    RegionSetPolicyRequest regionSetPolicyRequestResource = new RegionSetPolicyRequest();
    // Make the request
    Policy response = await serviceAttachmentsClient.SetIamPolicyAsync(project, region, resource, regionSetPolicyRequestResource);
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachmentsClient#Google_Cloud_Compute_V1_ServiceAttachmentsClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachmentsClient#Google_Cloud_Compute_V1_ServiceAttachmentsClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachmentsClient#Google_Cloud_Compute_V1_ServiceAttachmentsClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachmentsClient#Google_Cloud_Compute_V1_ServiceAttachmentsClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### TestIamPermissions(TestIamPermissionsServiceAttachmentRequest, CallSettings)
    
    
    public virtual TestPermissionsResponse TestIamPermissions(TestIamPermissionsServiceAttachmentRequest request, CallSettings callSettings = null)

Returns permissions that a caller has on the specified resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsServiceAttachmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TestIamPermissionsServiceAttachmentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[TestPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TestPermissionsResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    ServiceAttachmentsClient serviceAttachmentsClient = ServiceAttachmentsClient.Create();
    // Initialize request argument(s)
    TestIamPermissionsServiceAttachmentRequest request = new TestIamPermissionsServiceAttachmentRequest
    {
        Region = "",
        Resource = "",
        Project = "",
        TestPermissionsRequestResource = new TestPermissionsRequest(),
    };
    // Make the request
    TestPermissionsResponse response = serviceAttachmentsClient.TestIamPermissions(request);
    

### TestIamPermissions(string, string, string, TestPermissionsRequest, CallSettings)
    
    
    public virtual TestPermissionsResponse TestIamPermissions(string project, string region, string resource, TestPermissionsRequest testPermissionsRequestResource, CallSettings callSettings = null)

Returns permissions that a caller has on the specified resource.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the region for this request.  
`resource` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name or id of the resource for this request.  
`testPermissionsRequestResource` | `[TestPermissionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TestPermissionsRequest)`  
The body resource for this request  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[TestPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TestPermissionsResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    ServiceAttachmentsClient serviceAttachmentsClient = ServiceAttachmentsClient.Create();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    string resource = "";
    TestPermissionsRequest testPermissionsRequestResource = new TestPermissionsRequest();
    // Make the request
    TestPermissionsResponse response = serviceAttachmentsClient.TestIamPermissions(project, region, resource, testPermissionsRequestResource);
    

### TestIamPermissionsAsync(TestIamPermissionsServiceAttachmentRequest, CallSettings)
    
    
    public virtual Task<TestPermissionsResponse> TestIamPermissionsAsync(TestIamPermissionsServiceAttachmentRequest request, CallSettings callSettings = null)

Returns permissions that a caller has on the specified resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsServiceAttachmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TestIamPermissionsServiceAttachmentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[TestPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TestPermissionsResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ServiceAttachmentsClient serviceAttachmentsClient = await ServiceAttachmentsClient.CreateAsync();
    // Initialize request argument(s)
    TestIamPermissionsServiceAttachmentRequest request = new TestIamPermissionsServiceAttachmentRequest
    {
        Region = "",
        Resource = "",
        Project = "",
        TestPermissionsRequestResource = new TestPermissionsRequest(),
    };
    // Make the request
    TestPermissionsResponse response = await serviceAttachmentsClient.TestIamPermissionsAsync(request);
    

### TestIamPermissionsAsync(TestIamPermissionsServiceAttachmentRequest, CancellationToken)
    
    
    public virtual Task<TestPermissionsResponse> TestIamPermissionsAsync(TestIamPermissionsServiceAttachmentRequest request, CancellationToken cancellationToken)

Returns permissions that a caller has on the specified resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsServiceAttachmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TestIamPermissionsServiceAttachmentRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[TestPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TestPermissionsResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ServiceAttachmentsClient serviceAttachmentsClient = await ServiceAttachmentsClient.CreateAsync();
    // Initialize request argument(s)
    TestIamPermissionsServiceAttachmentRequest request = new TestIamPermissionsServiceAttachmentRequest
    {
        Region = "",
        Resource = "",
        Project = "",
        TestPermissionsRequestResource = new TestPermissionsRequest(),
    };
    // Make the request
    TestPermissionsResponse response = await serviceAttachmentsClient.TestIamPermissionsAsync(request);
    

### TestIamPermissionsAsync(string, string, string, TestPermissionsRequest, CallSettings)
    
    
    public virtual Task<TestPermissionsResponse> TestIamPermissionsAsync(string project, string region, string resource, TestPermissionsRequest testPermissionsRequestResource, CallSettings callSettings = null)

Returns permissions that a caller has on the specified resource.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the region for this request.  
`resource` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name or id of the resource for this request.  
`testPermissionsRequestResource` | `[TestPermissionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TestPermissionsRequest)`  
The body resource for this request  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[TestPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TestPermissionsResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ServiceAttachmentsClient serviceAttachmentsClient = await ServiceAttachmentsClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    string resource = "";
    TestPermissionsRequest testPermissionsRequestResource = new TestPermissionsRequest();
    // Make the request
    TestPermissionsResponse response = await serviceAttachmentsClient.TestIamPermissionsAsync(project, region, resource, testPermissionsRequestResource);
    

### TestIamPermissionsAsync(string, string, string, TestPermissionsRequest, CancellationToken)
    
    
    public virtual Task<TestPermissionsResponse> TestIamPermissionsAsync(string project, string region, string resource, TestPermissionsRequest testPermissionsRequestResource, CancellationToken cancellationToken)

Returns permissions that a caller has on the specified resource.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the region for this request.  
`resource` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name or id of the resource for this request.  
`testPermissionsRequestResource` | `[TestPermissionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TestPermissionsRequest)`  
The body resource for this request  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[TestPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TestPermissionsResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ServiceAttachmentsClient serviceAttachmentsClient = await ServiceAttachmentsClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    string resource = "";
    TestPermissionsRequest testPermissionsRequestResource = new TestPermissionsRequest();
    // Make the request
    TestPermissionsResponse response = await serviceAttachmentsClient.TestIamPermissionsAsync(project, region, resource, testPermissionsRequestResource);
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
