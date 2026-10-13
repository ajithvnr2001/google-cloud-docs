---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AddressesClient
title: Compute Engine v1 API - Class AddressesClient (4.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:25:17.753485+00:00
---

# Compute Engine v1 API - Class AddressesClient (4.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AddressesClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Compute Engine v1 API - Class AddressesClient (4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public abstract class AddressesClient

Reference documentation and code samples for the Compute Engine v1 API class AddressesClient.

Addresses client wrapper, for convenient use. This client implements API version 2026-09-01.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AddressesClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[AddressesClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AddressesClientImpl)

## Namespace

[Google.Cloud.Compute.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1)

## Assembly

Google.Cloud.Compute.V1.dll

## Remarks

The Addresses API.

## Properties 

### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the Addresses service, which is a host of "compute.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default Addresses scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default Addresses scopes are:

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
    
    
    public virtual Addresses.AddressesClient GrpcClient { get; }

The underlying gRPC Addresses client

**Property Value**  
---  
**Type** | **Description**  
`[Addresses](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Addresses)[AddressesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Addresses.AddressesClient)` |   
  
### InsertOperationsClient
    
    
    public virtual OperationsClient InsertOperationsClient { get; }

The long-running operations client for `Insert`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### MoveOperationsClient
    
    
    public virtual OperationsClient MoveOperationsClient { get; }

The long-running operations client for `Move`.

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
  
### SetLabelsOperationsClient
    
    
    public virtual OperationsClient SetLabelsOperationsClient { get; }

The long-running operations client for `SetLabels`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
## Methods 

### AggregatedList(AggregatedListAddressesRequest, CallSettings)
    
    
    public virtual PagedEnumerable<AddressAggregatedList, KeyValuePair<string, AddressesScopedList>> AggregatedList(AggregatedListAddressesRequest request, CallSettings callSettings = null)

Retrieves an aggregated list of addresses.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AggregatedListAddressesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AggregatedListAddressesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[AddressAggregatedList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AddressAggregatedList)[KeyValuePair](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair-2)[string](https://learn.microsoft.com/dotnet/api/system.string)[AddressesScopedList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AddressesScopedList)` | A pageable sequence of [KeyValuePair<TKey, TValue>](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair-2) resources.  
**Example**
    
    
    // Create client
    AddressesClient addressesClient = AddressesClient.Create();
    // Initialize request argument(s)
    AggregatedListAddressesRequest request = new AggregatedListAddressesRequest
    {
        OrderBy = "",
        Project = "",
        ServiceProjectNumber = 0L,
        Filter = "",
        IncludeAllScopes = false,
    };
    // Make the request
    PagedEnumerable<AddressAggregatedList, KeyValuePair<string, AddressesScopedList>> response = addressesClient.AggregatedList(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (KeyValuePair<string, AddressesScopedList> item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (AddressAggregatedList page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (KeyValuePair<string, AddressesScopedList> item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<KeyValuePair<string, AddressesScopedList>> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (KeyValuePair<string, AddressesScopedList> item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### AggregatedList(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<AddressAggregatedList, KeyValuePair<string, AddressesScopedList>> AggregatedList(string project, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieves an aggregated list of addresses.

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
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[AddressAggregatedList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AddressAggregatedList)[KeyValuePair](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair-2)[string](https://learn.microsoft.com/dotnet/api/system.string)[AddressesScopedList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AddressesScopedList)` | A pageable sequence of [KeyValuePair<TKey, TValue>](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair-2) resources.  
**Example**
    
    
    // Create client
    AddressesClient addressesClient = AddressesClient.Create();
    // Initialize request argument(s)
    string project = "";
    // Make the request
    PagedEnumerable<AddressAggregatedList, KeyValuePair<string, AddressesScopedList>> response = addressesClient.AggregatedList(project);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (KeyValuePair<string, AddressesScopedList> item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (AddressAggregatedList page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (KeyValuePair<string, AddressesScopedList> item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<KeyValuePair<string, AddressesScopedList>> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (KeyValuePair<string, AddressesScopedList> item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### AggregatedListAsync(AggregatedListAddressesRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<AddressAggregatedList, KeyValuePair<string, AddressesScopedList>> AggregatedListAsync(AggregatedListAddressesRequest request, CallSettings callSettings = null)

Retrieves an aggregated list of addresses.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AggregatedListAddressesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AggregatedListAddressesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[AddressAggregatedList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AddressAggregatedList)[KeyValuePair](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair-2)[string](https://learn.microsoft.com/dotnet/api/system.string)[AddressesScopedList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AddressesScopedList)` | A pageable asynchronous sequence of [KeyValuePair<TKey, TValue>](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair-2) resources.  
**Example**
    
    
    // Create client
    AddressesClient addressesClient = await AddressesClient.CreateAsync();
    // Initialize request argument(s)
    AggregatedListAddressesRequest request = new AggregatedListAddressesRequest
    {
        OrderBy = "",
        Project = "",
        ServiceProjectNumber = 0L,
        Filter = "",
        IncludeAllScopes = false,
    };
    // Make the request
    PagedAsyncEnumerable<AddressAggregatedList, KeyValuePair<string, AddressesScopedList>> response = addressesClient.AggregatedListAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (KeyValuePair<string, AddressesScopedList> item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (AddressAggregatedList page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (KeyValuePair<string, AddressesScopedList> item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<KeyValuePair<string, AddressesScopedList>> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (KeyValuePair<string, AddressesScopedList> item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### AggregatedListAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<AddressAggregatedList, KeyValuePair<string, AddressesScopedList>> AggregatedListAsync(string project, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieves an aggregated list of addresses.

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
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[AddressAggregatedList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AddressAggregatedList)[KeyValuePair](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair-2)[string](https://learn.microsoft.com/dotnet/api/system.string)[AddressesScopedList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AddressesScopedList)` | A pageable asynchronous sequence of [KeyValuePair<TKey, TValue>](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair-2) resources.  
**Example**
    
    
    // Create client
    AddressesClient addressesClient = await AddressesClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    // Make the request
    PagedAsyncEnumerable<AddressAggregatedList, KeyValuePair<string, AddressesScopedList>> response = addressesClient.AggregatedListAsync(project);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (KeyValuePair<string, AddressesScopedList> item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (AddressAggregatedList page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (KeyValuePair<string, AddressesScopedList> item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<KeyValuePair<string, AddressesScopedList>> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (KeyValuePair<string, AddressesScopedList> item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### Create()
    
    
    public static AddressesClient Create()

Synchronously creates a [AddressesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AddressesClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [AddressesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AddressesClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[AddressesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AddressesClient)` | The created [AddressesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AddressesClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<AddressesClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [AddressesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AddressesClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [AddressesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AddressesClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AddressesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AddressesClient)` | The task representing the created [AddressesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AddressesClient).  
  
### Delete(DeleteAddressRequest, CallSettings)
    
    
    public virtual Operation<Operation, Operation> Delete(DeleteAddressRequest request, CallSettings callSettings = null)

Deletes the specified address resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAddressRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.DeleteAddressRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The RPC response.  
**Example**
    
    
    // Create client
    AddressesClient addressesClient = AddressesClient.Create();
    // Initialize request argument(s)
    DeleteAddressRequest request = new DeleteAddressRequest
    {
        RequestId = "",
        Region = "",
        Project = "",
        Address = "",
    };
    // Make the request
    lro::Operation<Operation, Operation> response = addressesClient.Delete(request);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = addressesClient.PollOnceDelete(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### Delete(string, string, string, CallSettings)
    
    
    public virtual Operation<Operation, Operation> Delete(string project, string region, string address, CallSettings callSettings = null)

Deletes the specified address resource.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the region for this request.  
`address` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the address resource to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The RPC response.  
**Example**
    
    
    // Create client
    AddressesClient addressesClient = AddressesClient.Create();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    string address = "";
    // Make the request
    lro::Operation<Operation, Operation> response = addressesClient.Delete(project, region, address);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = addressesClient.PollOnceDelete(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### DeleteAsync(DeleteAddressRequest, CallSettings)
    
    
    public virtual Task<Operation<Operation, Operation>> DeleteAsync(DeleteAddressRequest request, CallSettings callSettings = null)

Deletes the specified address resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAddressRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.DeleteAddressRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AddressesClient addressesClient = await AddressesClient.CreateAsync();
    // Initialize request argument(s)
    DeleteAddressRequest request = new DeleteAddressRequest
    {
        RequestId = "",
        Region = "",
        Project = "",
        Address = "",
    };
    // Make the request
    lro::Operation<Operation, Operation> response = await addressesClient.DeleteAsync(request);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = await addressesClient.PollOnceDeleteAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### DeleteAsync(DeleteAddressRequest, CancellationToken)
    
    
    public virtual Task<Operation<Operation, Operation>> DeleteAsync(DeleteAddressRequest request, CancellationToken cancellationToken)

Deletes the specified address resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAddressRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.DeleteAddressRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AddressesClient addressesClient = await AddressesClient.CreateAsync();
    // Initialize request argument(s)
    DeleteAddressRequest request = new DeleteAddressRequest
    {
        RequestId = "",
        Region = "",
        Project = "",
        Address = "",
    };
    // Make the request
    lro::Operation<Operation, Operation> response = await addressesClient.DeleteAsync(request);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = await addressesClient.PollOnceDeleteAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### DeleteAsync(string, string, string, CallSettings)
    
    
    public virtual Task<Operation<Operation, Operation>> DeleteAsync(string project, string region, string address, CallSettings callSettings = null)

Deletes the specified address resource.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the region for this request.  
`address` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the address resource to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AddressesClient addressesClient = await AddressesClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    string address = "";
    // Make the request
    lro::Operation<Operation, Operation> response = await addressesClient.DeleteAsync(project, region, address);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = await addressesClient.PollOnceDeleteAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### DeleteAsync(string, string, string, CancellationToken)
    
    
    public virtual Task<Operation<Operation, Operation>> DeleteAsync(string project, string region, string address, CancellationToken cancellationToken)

Deletes the specified address resource.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the region for this request.  
`address` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the address resource to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AddressesClient addressesClient = await AddressesClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    string address = "";
    // Make the request
    lro::Operation<Operation, Operation> response = await addressesClient.DeleteAsync(project, region, address);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = await addressesClient.PollOnceDeleteAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### Get(GetAddressRequest, CallSettings)
    
    
    public virtual Address Get(GetAddressRequest request, CallSettings callSettings = null)

Returns the specified address resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAddressRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetAddressRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Address](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Address)` | The RPC response.  
**Example**
    
    
    // Create client
    AddressesClient addressesClient = AddressesClient.Create();
    // Initialize request argument(s)
    GetAddressRequest request = new GetAddressRequest
    {
        Region = "",
        Project = "",
        Address = "",
    };
    // Make the request
    Address response = addressesClient.Get(request);
    

### Get(string, string, string, CallSettings)
    
    
    public virtual Address Get(string project, string region, string address, CallSettings callSettings = null)

Returns the specified address resource.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the region for this request.  
`address` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the address resource to return.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Address](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Address)` | The RPC response.  
**Example**
    
    
    // Create client
    AddressesClient addressesClient = AddressesClient.Create();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    string address = "";
    // Make the request
    Address response = addressesClient.Get(project, region, address);
    

### GetAsync(GetAddressRequest, CallSettings)
    
    
    public virtual Task<Address> GetAsync(GetAddressRequest request, CallSettings callSettings = null)

Returns the specified address resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAddressRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetAddressRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Address](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Address)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AddressesClient addressesClient = await AddressesClient.CreateAsync();
    // Initialize request argument(s)
    GetAddressRequest request = new GetAddressRequest
    {
        Region = "",
        Project = "",
        Address = "",
    };
    // Make the request
    Address response = await addressesClient.GetAsync(request);
    

### GetAsync(GetAddressRequest, CancellationToken)
    
    
    public virtual Task<Address> GetAsync(GetAddressRequest request, CancellationToken cancellationToken)

Returns the specified address resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAddressRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetAddressRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Address](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Address)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AddressesClient addressesClient = await AddressesClient.CreateAsync();
    // Initialize request argument(s)
    GetAddressRequest request = new GetAddressRequest
    {
        Region = "",
        Project = "",
        Address = "",
    };
    // Make the request
    Address response = await addressesClient.GetAsync(request);
    

### GetAsync(string, string, string, CallSettings)
    
    
    public virtual Task<Address> GetAsync(string project, string region, string address, CallSettings callSettings = null)

Returns the specified address resource.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the region for this request.  
`address` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the address resource to return.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Address](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Address)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AddressesClient addressesClient = await AddressesClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    string address = "";
    // Make the request
    Address response = await addressesClient.GetAsync(project, region, address);
    

### GetAsync(string, string, string, CancellationToken)
    
    
    public virtual Task<Address> GetAsync(string project, string region, string address, CancellationToken cancellationToken)

Returns the specified address resource.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the region for this request.  
`address` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the address resource to return.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Address](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Address)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AddressesClient addressesClient = await AddressesClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    string address = "";
    // Make the request
    Address response = await addressesClient.GetAsync(project, region, address);
    

### Insert(InsertAddressRequest, CallSettings)
    
    
    public virtual Operation<Operation, Operation> Insert(InsertAddressRequest request, CallSettings callSettings = null)

Creates an address resource in the specified project by using the data included in the request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[InsertAddressRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InsertAddressRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The RPC response.  
**Example**
    
    
    // Create client
    AddressesClient addressesClient = AddressesClient.Create();
    // Initialize request argument(s)
    InsertAddressRequest request = new InsertAddressRequest
    {
        RequestId = "",
        Region = "",
        Project = "",
        AddressResource = new Address(),
    };
    // Make the request
    lro::Operation<Operation, Operation> response = addressesClient.Insert(request);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = addressesClient.PollOnceInsert(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### Insert(string, string, Address, CallSettings)
    
    
    public virtual Operation<Operation, Operation> Insert(string project, string region, Address addressResource, CallSettings callSettings = null)

Creates an address resource in the specified project by using the data included in the request.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the region for this request.  
`addressResource` | `[Address](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Address)`  
The body resource for this request  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The RPC response.  
**Example**
    
    
    // Create client
    AddressesClient addressesClient = AddressesClient.Create();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    Address addressResource = new Address();
    // Make the request
    lro::Operation<Operation, Operation> response = addressesClient.Insert(project, region, addressResource);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = addressesClient.PollOnceInsert(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### InsertAsync(InsertAddressRequest, CallSettings)
    
    
    public virtual Task<Operation<Operation, Operation>> InsertAsync(InsertAddressRequest request, CallSettings callSettings = null)

Creates an address resource in the specified project by using the data included in the request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[InsertAddressRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InsertAddressRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AddressesClient addressesClient = await AddressesClient.CreateAsync();
    // Initialize request argument(s)
    InsertAddressRequest request = new InsertAddressRequest
    {
        RequestId = "",
        Region = "",
        Project = "",
        AddressResource = new Address(),
    };
    // Make the request
    lro::Operation<Operation, Operation> response = await addressesClient.InsertAsync(request);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = await addressesClient.PollOnceInsertAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### InsertAsync(InsertAddressRequest, CancellationToken)
    
    
    public virtual Task<Operation<Operation, Operation>> InsertAsync(InsertAddressRequest request, CancellationToken cancellationToken)

Creates an address resource in the specified project by using the data included in the request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[InsertAddressRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InsertAddressRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AddressesClient addressesClient = await AddressesClient.CreateAsync();
    // Initialize request argument(s)
    InsertAddressRequest request = new InsertAddressRequest
    {
        RequestId = "",
        Region = "",
        Project = "",
        AddressResource = new Address(),
    };
    // Make the request
    lro::Operation<Operation, Operation> response = await addressesClient.InsertAsync(request);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = await addressesClient.PollOnceInsertAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### InsertAsync(string, string, Address, CallSettings)
    
    
    public virtual Task<Operation<Operation, Operation>> InsertAsync(string project, string region, Address addressResource, CallSettings callSettings = null)

Creates an address resource in the specified project by using the data included in the request.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the region for this request.  
`addressResource` | `[Address](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Address)`  
The body resource for this request  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AddressesClient addressesClient = await AddressesClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    Address addressResource = new Address();
    // Make the request
    lro::Operation<Operation, Operation> response = await addressesClient.InsertAsync(project, region, addressResource);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = await addressesClient.PollOnceInsertAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### InsertAsync(string, string, Address, CancellationToken)
    
    
    public virtual Task<Operation<Operation, Operation>> InsertAsync(string project, string region, Address addressResource, CancellationToken cancellationToken)

Creates an address resource in the specified project by using the data included in the request.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the region for this request.  
`addressResource` | `[Address](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Address)`  
The body resource for this request  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AddressesClient addressesClient = await AddressesClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    Address addressResource = new Address();
    // Make the request
    lro::Operation<Operation, Operation> response = await addressesClient.InsertAsync(project, region, addressResource);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = await addressesClient.PollOnceInsertAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### List(ListAddressesRequest, CallSettings)
    
    
    public virtual PagedEnumerable<AddressList, Address> List(ListAddressesRequest request, CallSettings callSettings = null)

Retrieves a list of addresses contained within the specified region.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAddressesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ListAddressesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[AddressList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AddressList)[Address](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Address)` | A pageable sequence of [Address](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Address) resources.  
**Example**
    
    
    // Create client
    AddressesClient addressesClient = AddressesClient.Create();
    // Initialize request argument(s)
    ListAddressesRequest request = new ListAddressesRequest
    {
        Region = "",
        OrderBy = "",
        Project = "",
        Filter = "",
    };
    // Make the request
    PagedEnumerable<AddressList, Address> response = addressesClient.List(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Address item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (AddressList page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Address item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Address> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Address item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### List(string, string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<AddressList, Address> List(string project, string region, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieves a list of addresses contained within the specified region.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the region for this request.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[AddressList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AddressList)[Address](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Address)` | A pageable sequence of [Address](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Address) resources.  
**Example**
    
    
    // Create client
    AddressesClient addressesClient = AddressesClient.Create();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    // Make the request
    PagedEnumerable<AddressList, Address> response = addressesClient.List(project, region);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Address item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (AddressList page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Address item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Address> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Address item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAsync(ListAddressesRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<AddressList, Address> ListAsync(ListAddressesRequest request, CallSettings callSettings = null)

Retrieves a list of addresses contained within the specified region.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAddressesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ListAddressesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[AddressList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AddressList)[Address](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Address)` | A pageable asynchronous sequence of [Address](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Address) resources.  
**Example**
    
    
    // Create client
    AddressesClient addressesClient = await AddressesClient.CreateAsync();
    // Initialize request argument(s)
    ListAddressesRequest request = new ListAddressesRequest
    {
        Region = "",
        OrderBy = "",
        Project = "",
        Filter = "",
    };
    // Make the request
    PagedAsyncEnumerable<AddressList, Address> response = addressesClient.ListAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Address item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (AddressList page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Address item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Address> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Address item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAsync(string, string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<AddressList, Address> ListAsync(string project, string region, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Retrieves a list of addresses contained within the specified region.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the region for this request.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[AddressList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AddressList)[Address](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Address)` | A pageable asynchronous sequence of [Address](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Address) resources.  
**Example**
    
    
    // Create client
    AddressesClient addressesClient = await AddressesClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    // Make the request
    PagedAsyncEnumerable<AddressList, Address> response = addressesClient.ListAsync(project, region);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Address item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (AddressList page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Address item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Address> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Address item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### Move(MoveAddressRequest, CallSettings)
    
    
    public virtual Operation<Operation, Operation> Move(MoveAddressRequest request, CallSettings callSettings = null)

Moves the specified address resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MoveAddressRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.MoveAddressRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The RPC response.  
**Example**
    
    
    // Create client
    AddressesClient addressesClient = AddressesClient.Create();
    // Initialize request argument(s)
    MoveAddressRequest request = new MoveAddressRequest
    {
        RequestId = "",
        Region = "",
        Project = "",
        RegionAddressesMoveRequestResource = new RegionAddressesMoveRequest(),
        Address = "",
    };
    // Make the request
    lro::Operation<Operation, Operation> response = addressesClient.Move(request);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = addressesClient.PollOnceMove(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### Move(string, string, string, RegionAddressesMoveRequest, CallSettings)
    
    
    public virtual Operation<Operation, Operation> Move(string project, string region, string address, RegionAddressesMoveRequest regionAddressesMoveRequestResource, CallSettings callSettings = null)

Moves the specified address resource.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Source project ID which the Address is moved from.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the region for this request.  
`address` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the address resource to move.  
`regionAddressesMoveRequestResource` | `[RegionAddressesMoveRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionAddressesMoveRequest)`  
The body resource for this request  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The RPC response.  
**Example**
    
    
    // Create client
    AddressesClient addressesClient = AddressesClient.Create();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    string address = "";
    RegionAddressesMoveRequest regionAddressesMoveRequestResource = new RegionAddressesMoveRequest();
    // Make the request
    lro::Operation<Operation, Operation> response = addressesClient.Move(project, region, address, regionAddressesMoveRequestResource);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = addressesClient.PollOnceMove(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### MoveAsync(MoveAddressRequest, CallSettings)
    
    
    public virtual Task<Operation<Operation, Operation>> MoveAsync(MoveAddressRequest request, CallSettings callSettings = null)

Moves the specified address resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MoveAddressRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.MoveAddressRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AddressesClient addressesClient = await AddressesClient.CreateAsync();
    // Initialize request argument(s)
    MoveAddressRequest request = new MoveAddressRequest
    {
        RequestId = "",
        Region = "",
        Project = "",
        RegionAddressesMoveRequestResource = new RegionAddressesMoveRequest(),
        Address = "",
    };
    // Make the request
    lro::Operation<Operation, Operation> response = await addressesClient.MoveAsync(request);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = await addressesClient.PollOnceMoveAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### MoveAsync(MoveAddressRequest, CancellationToken)
    
    
    public virtual Task<Operation<Operation, Operation>> MoveAsync(MoveAddressRequest request, CancellationToken cancellationToken)

Moves the specified address resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MoveAddressRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.MoveAddressRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AddressesClient addressesClient = await AddressesClient.CreateAsync();
    // Initialize request argument(s)
    MoveAddressRequest request = new MoveAddressRequest
    {
        RequestId = "",
        Region = "",
        Project = "",
        RegionAddressesMoveRequestResource = new RegionAddressesMoveRequest(),
        Address = "",
    };
    // Make the request
    lro::Operation<Operation, Operation> response = await addressesClient.MoveAsync(request);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = await addressesClient.PollOnceMoveAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### MoveAsync(string, string, string, RegionAddressesMoveRequest, CallSettings)
    
    
    public virtual Task<Operation<Operation, Operation>> MoveAsync(string project, string region, string address, RegionAddressesMoveRequest regionAddressesMoveRequestResource, CallSettings callSettings = null)

Moves the specified address resource.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Source project ID which the Address is moved from.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the region for this request.  
`address` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the address resource to move.  
`regionAddressesMoveRequestResource` | `[RegionAddressesMoveRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionAddressesMoveRequest)`  
The body resource for this request  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AddressesClient addressesClient = await AddressesClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    string address = "";
    RegionAddressesMoveRequest regionAddressesMoveRequestResource = new RegionAddressesMoveRequest();
    // Make the request
    lro::Operation<Operation, Operation> response = await addressesClient.MoveAsync(project, region, address, regionAddressesMoveRequestResource);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = await addressesClient.PollOnceMoveAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### MoveAsync(string, string, string, RegionAddressesMoveRequest, CancellationToken)
    
    
    public virtual Task<Operation<Operation, Operation>> MoveAsync(string project, string region, string address, RegionAddressesMoveRequest regionAddressesMoveRequestResource, CancellationToken cancellationToken)

Moves the specified address resource.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Source project ID which the Address is moved from.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the region for this request.  
`address` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the address resource to move.  
`regionAddressesMoveRequestResource` | `[RegionAddressesMoveRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionAddressesMoveRequest)`  
The body resource for this request  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AddressesClient addressesClient = await AddressesClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    string address = "";
    RegionAddressesMoveRequest regionAddressesMoveRequestResource = new RegionAddressesMoveRequest();
    // Make the request
    lro::Operation<Operation, Operation> response = await addressesClient.MoveAsync(project, region, address, regionAddressesMoveRequestResource);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = await addressesClient.PollOnceMoveAsync(operationName);
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
  
### PollOnceMove(string, CallSettings)
    
    
    public virtual Operation<Operation, Operation> PollOnceMove(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `Move`.

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
  
### PollOnceMoveAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Operation, Operation>> PollOnceMoveAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `Move` .

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
  
### PollOnceSetLabels(string, CallSettings)
    
    
    public virtual Operation<Operation, Operation> PollOnceSetLabels(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `SetLabels`.

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
  
### PollOnceSetLabelsAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Operation, Operation>> PollOnceSetLabelsAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `SetLabels`.

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
  
### SetLabels(SetLabelsAddressRequest, CallSettings)
    
    
    public virtual Operation<Operation, Operation> SetLabels(SetLabelsAddressRequest request, CallSettings callSettings = null)

Sets the labels on an Address. To learn more about labels, read theLabeling Resources documentation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetLabelsAddressRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SetLabelsAddressRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The RPC response.  
**Example**
    
    
    // Create client
    AddressesClient addressesClient = AddressesClient.Create();
    // Initialize request argument(s)
    SetLabelsAddressRequest request = new SetLabelsAddressRequest
    {
        RequestId = "",
        Region = "",
        Resource = "",
        Project = "",
        RegionSetLabelsRequestResource = new RegionSetLabelsRequest(),
    };
    // Make the request
    lro::Operation<Operation, Operation> response = addressesClient.SetLabels(request);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = addressesClient.PollOnceSetLabels(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### SetLabels(string, string, string, RegionSetLabelsRequest, CallSettings)
    
    
    public virtual Operation<Operation, Operation> SetLabels(string project, string region, string resource, RegionSetLabelsRequest regionSetLabelsRequestResource, CallSettings callSettings = null)

Sets the labels on an Address. To learn more about labels, read theLabeling Resources documentation.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The region for this request.  
`resource` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name or id of the resource for this request.  
`regionSetLabelsRequestResource` | `[RegionSetLabelsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSetLabelsRequest)`  
The body resource for this request  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The RPC response.  
**Example**
    
    
    // Create client
    AddressesClient addressesClient = AddressesClient.Create();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    string resource = "";
    RegionSetLabelsRequest regionSetLabelsRequestResource = new RegionSetLabelsRequest();
    // Make the request
    lro::Operation<Operation, Operation> response = addressesClient.SetLabels(project, region, resource, regionSetLabelsRequestResource);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = addressesClient.PollOnceSetLabels(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### SetLabelsAsync(SetLabelsAddressRequest, CallSettings)
    
    
    public virtual Task<Operation<Operation, Operation>> SetLabelsAsync(SetLabelsAddressRequest request, CallSettings callSettings = null)

Sets the labels on an Address. To learn more about labels, read theLabeling Resources documentation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetLabelsAddressRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SetLabelsAddressRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AddressesClient addressesClient = await AddressesClient.CreateAsync();
    // Initialize request argument(s)
    SetLabelsAddressRequest request = new SetLabelsAddressRequest
    {
        RequestId = "",
        Region = "",
        Resource = "",
        Project = "",
        RegionSetLabelsRequestResource = new RegionSetLabelsRequest(),
    };
    // Make the request
    lro::Operation<Operation, Operation> response = await addressesClient.SetLabelsAsync(request);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = await addressesClient.PollOnceSetLabelsAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### SetLabelsAsync(SetLabelsAddressRequest, CancellationToken)
    
    
    public virtual Task<Operation<Operation, Operation>> SetLabelsAsync(SetLabelsAddressRequest request, CancellationToken cancellationToken)

Sets the labels on an Address. To learn more about labels, read theLabeling Resources documentation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetLabelsAddressRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SetLabelsAddressRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AddressesClient addressesClient = await AddressesClient.CreateAsync();
    // Initialize request argument(s)
    SetLabelsAddressRequest request = new SetLabelsAddressRequest
    {
        RequestId = "",
        Region = "",
        Resource = "",
        Project = "",
        RegionSetLabelsRequestResource = new RegionSetLabelsRequest(),
    };
    // Make the request
    lro::Operation<Operation, Operation> response = await addressesClient.SetLabelsAsync(request);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = await addressesClient.PollOnceSetLabelsAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### SetLabelsAsync(string, string, string, RegionSetLabelsRequest, CallSettings)
    
    
    public virtual Task<Operation<Operation, Operation>> SetLabelsAsync(string project, string region, string resource, RegionSetLabelsRequest regionSetLabelsRequestResource, CallSettings callSettings = null)

Sets the labels on an Address. To learn more about labels, read theLabeling Resources documentation.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The region for this request.  
`resource` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name or id of the resource for this request.  
`regionSetLabelsRequestResource` | `[RegionSetLabelsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSetLabelsRequest)`  
The body resource for this request  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AddressesClient addressesClient = await AddressesClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    string resource = "";
    RegionSetLabelsRequest regionSetLabelsRequestResource = new RegionSetLabelsRequest();
    // Make the request
    lro::Operation<Operation, Operation> response = await addressesClient.SetLabelsAsync(project, region, resource, regionSetLabelsRequestResource);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = await addressesClient.PollOnceSetLabelsAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### SetLabelsAsync(string, string, string, RegionSetLabelsRequest, CancellationToken)
    
    
    public virtual Task<Operation<Operation, Operation>> SetLabelsAsync(string project, string region, string resource, RegionSetLabelsRequest regionSetLabelsRequestResource, CancellationToken cancellationToken)

Sets the labels on an Address. To learn more about labels, read theLabeling Resources documentation.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The region for this request.  
`resource` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name or id of the resource for this request.  
`regionSetLabelsRequestResource` | `[RegionSetLabelsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSetLabelsRequest)`  
The body resource for this request  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AddressesClient addressesClient = await AddressesClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    string resource = "";
    RegionSetLabelsRequest regionSetLabelsRequestResource = new RegionSetLabelsRequest();
    // Make the request
    lro::Operation<Operation, Operation> response = await addressesClient.SetLabelsAsync(project, region, resource, regionSetLabelsRequestResource);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = await addressesClient.PollOnceSetLabelsAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AddressesClient#Google_Cloud_Compute_V1_AddressesClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AddressesClient#Google_Cloud_Compute_V1_AddressesClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AddressesClient#Google_Cloud_Compute_V1_AddressesClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AddressesClient#Google_Cloud_Compute_V1_AddressesClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### TestIamPermissions(TestIamPermissionsAddressRequest, CallSettings)
    
    
    public virtual TestPermissionsResponse TestIamPermissions(TestIamPermissionsAddressRequest request, CallSettings callSettings = null)

Returns permissions that a caller has on the specified resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsAddressRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TestIamPermissionsAddressRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[TestPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TestPermissionsResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    AddressesClient addressesClient = AddressesClient.Create();
    // Initialize request argument(s)
    TestIamPermissionsAddressRequest request = new TestIamPermissionsAddressRequest
    {
        Region = "",
        Resource = "",
        Project = "",
        TestPermissionsRequestResource = new TestPermissionsRequest(),
    };
    // Make the request
    TestPermissionsResponse response = addressesClient.TestIamPermissions(request);
    

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
    AddressesClient addressesClient = AddressesClient.Create();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    string resource = "";
    TestPermissionsRequest testPermissionsRequestResource = new TestPermissionsRequest();
    // Make the request
    TestPermissionsResponse response = addressesClient.TestIamPermissions(project, region, resource, testPermissionsRequestResource);
    

### TestIamPermissionsAsync(TestIamPermissionsAddressRequest, CallSettings)
    
    
    public virtual Task<TestPermissionsResponse> TestIamPermissionsAsync(TestIamPermissionsAddressRequest request, CallSettings callSettings = null)

Returns permissions that a caller has on the specified resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsAddressRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TestIamPermissionsAddressRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[TestPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TestPermissionsResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AddressesClient addressesClient = await AddressesClient.CreateAsync();
    // Initialize request argument(s)
    TestIamPermissionsAddressRequest request = new TestIamPermissionsAddressRequest
    {
        Region = "",
        Resource = "",
        Project = "",
        TestPermissionsRequestResource = new TestPermissionsRequest(),
    };
    // Make the request
    TestPermissionsResponse response = await addressesClient.TestIamPermissionsAsync(request);
    

### TestIamPermissionsAsync(TestIamPermissionsAddressRequest, CancellationToken)
    
    
    public virtual Task<TestPermissionsResponse> TestIamPermissionsAsync(TestIamPermissionsAddressRequest request, CancellationToken cancellationToken)

Returns permissions that a caller has on the specified resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsAddressRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TestIamPermissionsAddressRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[TestPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TestPermissionsResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AddressesClient addressesClient = await AddressesClient.CreateAsync();
    // Initialize request argument(s)
    TestIamPermissionsAddressRequest request = new TestIamPermissionsAddressRequest
    {
        Region = "",
        Resource = "",
        Project = "",
        TestPermissionsRequestResource = new TestPermissionsRequest(),
    };
    // Make the request
    TestPermissionsResponse response = await addressesClient.TestIamPermissionsAsync(request);
    

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
    AddressesClient addressesClient = await AddressesClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    string resource = "";
    TestPermissionsRequest testPermissionsRequestResource = new TestPermissionsRequest();
    // Make the request
    TestPermissionsResponse response = await addressesClient.TestIamPermissionsAsync(project, region, resource, testPermissionsRequestResource);
    

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
    AddressesClient addressesClient = await AddressesClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    string resource = "";
    TestPermissionsRequest testPermissionsRequestResource = new TestPermissionsRequest();
    // Make the request
    TestPermissionsResponse response = await addressesClient.TestIamPermissionsAsync(project, region, resource, testPermissionsRequestResource);
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
