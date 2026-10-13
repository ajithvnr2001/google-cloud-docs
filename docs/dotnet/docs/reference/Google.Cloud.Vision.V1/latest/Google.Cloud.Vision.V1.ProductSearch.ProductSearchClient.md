---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ProductSearch.ProductSearchClient
title: Google Cloud Vision v1 API - Class ProductSearch.ProductSearchClient (3.8.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:37:15.654443+00:00
---

# Google Cloud Vision v1 API - Class ProductSearch.ProductSearchClient (3.8.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ProductSearch.ProductSearchClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Vision v1 API - Class ProductSearch.ProductSearchClient (3.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.8.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ProductSearch.ProductSearchClient)
  * [ 3.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.7.0/Google.Cloud.Vision.V1.ProductSearch.ProductSearchClient)
  * [ 3.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.6.0/Google.Cloud.Vision.V1.ProductSearch.ProductSearchClient)
  * [ 3.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.5.0/Google.Cloud.Vision.V1.ProductSearch.ProductSearchClient)
  * [ 3.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.4.0/Google.Cloud.Vision.V1.ProductSearch.ProductSearchClient)
  * [ 3.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.3.0/Google.Cloud.Vision.V1.ProductSearch.ProductSearchClient)
  * [ 3.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.2.0/Google.Cloud.Vision.V1.ProductSearch.ProductSearchClient)
  * [ 3.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.1.0/Google.Cloud.Vision.V1.ProductSearch.ProductSearchClient)
  * [ 3.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.0.0/Google.Cloud.Vision.V1.ProductSearch.ProductSearchClient)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/2.5.0/Google.Cloud.Vision.V1.ProductSearch.ProductSearchClient)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/2.4.0/Google.Cloud.Vision.V1.ProductSearch.ProductSearchClient)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/2.3.0/Google.Cloud.Vision.V1.ProductSearch.ProductSearchClient)


    
    
    public class ProductSearch.ProductSearchClient : ClientBase<ProductSearch.ProductSearchClient>

Reference documentation and code samples for the Google Cloud Vision v1 API class ProductSearch.ProductSearchClient.

Client for ProductSearch

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html)[ProductSearch](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ProductSearch)[ProductSearchClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ProductSearch.ProductSearchClient) > ProductSearch.ProductSearchClient

## Inherited Members

[ClientBase<ProductSearch.ProductSearchClient>.WithHost(string)](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html#Grpc_Core_ClientBase_1_WithHost_System_String_)

[ClientBase.CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html#Grpc_Core_ClientBase_CallInvoker)

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Vision.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1)

## Assembly

Google.Cloud.Vision.V1.dll

## Constructors 

### ProductSearchClient()
    
    
    protected ProductSearchClient()

Protected parameterless constructor to allow creation of test doubles.

### ProductSearchClient(CallInvoker)
    
    
    public ProductSearchClient(CallInvoker callInvoker)

Creates a new client for ProductSearch that uses a custom `CallInvoker`.

**Parameter**  
---  
**Name** | **Description**  
`callInvoker` | `[CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallInvoker.html)`  
The callInvoker to use to make remote calls.  
  
### ProductSearchClient(ChannelBase)
    
    
    public ProductSearchClient(ChannelBase channel)

Creates a new client for ProductSearch

**Parameter**  
---  
**Name** | **Description**  
`channel` | `[ChannelBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ChannelBase.html)`  
The channel to use to make remote calls.  
  
### ProductSearchClient(ClientBaseConfiguration)
    
    
    protected ProductSearchClient(ClientBase.ClientBaseConfiguration configuration)

Protected constructor to allow creation of configured clients.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
The client configuration.  
  
## Methods 

### AddProductToProductSet(AddProductToProductSetRequest, CallOptions)
    
    
    public virtual Empty AddProductToProductSet(AddProductToProductSetRequest request, CallOptions options)

Adds a Product to the specified ProductSet. If the Product is already present, no change is made.

One Product can be added to at most 100 ProductSets.

Possible errors:

  * Returns NOT_FOUND if the Product or the ProductSet doesn't exist.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[AddProductToProductSetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.AddProductToProductSetRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response received from the server.  
  
### AddProductToProductSet(AddProductToProductSetRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Empty AddProductToProductSet(AddProductToProductSetRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Adds a Product to the specified ProductSet. If the Product is already present, no change is made.

One Product can be added to at most 100 ProductSets.

Possible errors:

  * Returns NOT_FOUND if the Product or the ProductSet doesn't exist.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[AddProductToProductSetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.AddProductToProductSetRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response received from the server.  
  
### AddProductToProductSetAsync(AddProductToProductSetRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Empty> AddProductToProductSetAsync(AddProductToProductSetRequest request, CallOptions options)

Adds a Product to the specified ProductSet. If the Product is already present, no change is made.

One Product can be added to at most 100 ProductSets.

Possible errors:

  * Returns NOT_FOUND if the Product or the ProductSet doesn't exist.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[AddProductToProductSetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.AddProductToProductSetRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The call object.  
  
### AddProductToProductSetAsync(AddProductToProductSetRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Empty> AddProductToProductSetAsync(AddProductToProductSetRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Adds a Product to the specified ProductSet. If the Product is already present, no change is made.

One Product can be added to at most 100 ProductSets.

Possible errors:

  * Returns NOT_FOUND if the Product or the ProductSet doesn't exist.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[AddProductToProductSetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.AddProductToProductSetRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The call object.  
  
### CreateOperationsClient()
    
    
    public virtual Operations.OperationsClient CreateOperationsClient()

Creates a new instance of [Operations.OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operations.OperationsClient.html) using the same call invoker as this client.

**Returns**  
---  
**Type** | **Description**  
`[Operations](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operations.html)[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operations.OperationsClient.html)` | A new Operations client for the same target as this client.  
  
### CreateProduct(CreateProductRequest, CallOptions)
    
    
    public virtual Product CreateProduct(CreateProductRequest request, CallOptions options)

Creates and returns a new product resource.

Possible errors:

  * Returns INVALID_ARGUMENT if display_name is missing or longer than 4096 characters.
  * Returns INVALID_ARGUMENT if description is longer than 4096 characters.
  * Returns INVALID_ARGUMENT if product_category is missing or invalid.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateProductRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.CreateProductRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Product](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.Product)` | The response received from the server.  
  
### CreateProduct(CreateProductRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Product CreateProduct(CreateProductRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates and returns a new product resource.

Possible errors:

  * Returns INVALID_ARGUMENT if display_name is missing or longer than 4096 characters.
  * Returns INVALID_ARGUMENT if description is longer than 4096 characters.
  * Returns INVALID_ARGUMENT if product_category is missing or invalid.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateProductRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.CreateProductRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Product](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.Product)` | The response received from the server.  
  
### CreateProductAsync(CreateProductRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Product> CreateProductAsync(CreateProductRequest request, CallOptions options)

Creates and returns a new product resource.

Possible errors:

  * Returns INVALID_ARGUMENT if display_name is missing or longer than 4096 characters.
  * Returns INVALID_ARGUMENT if description is longer than 4096 characters.
  * Returns INVALID_ARGUMENT if product_category is missing or invalid.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateProductRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.CreateProductRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Product](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.Product)` | The call object.  
  
### CreateProductAsync(CreateProductRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Product> CreateProductAsync(CreateProductRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates and returns a new product resource.

Possible errors:

  * Returns INVALID_ARGUMENT if display_name is missing or longer than 4096 characters.
  * Returns INVALID_ARGUMENT if description is longer than 4096 characters.
  * Returns INVALID_ARGUMENT if product_category is missing or invalid.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateProductRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.CreateProductRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Product](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.Product)` | The call object.  
  
### CreateProductSet(CreateProductSetRequest, CallOptions)
    
    
    public virtual ProductSet CreateProductSet(CreateProductSetRequest request, CallOptions options)

Creates and returns a new ProductSet resource.

Possible errors:

  * Returns INVALID_ARGUMENT if display_name is missing, or is longer than 4096 characters.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateProductSetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.CreateProductSetRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ProductSet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ProductSet)` | The response received from the server.  
  
### CreateProductSet(CreateProductSetRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ProductSet CreateProductSet(CreateProductSetRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates and returns a new ProductSet resource.

Possible errors:

  * Returns INVALID_ARGUMENT if display_name is missing, or is longer than 4096 characters.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateProductSetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.CreateProductSetRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ProductSet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ProductSet)` | The response received from the server.  
  
### CreateProductSetAsync(CreateProductSetRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ProductSet> CreateProductSetAsync(CreateProductSetRequest request, CallOptions options)

Creates and returns a new ProductSet resource.

Possible errors:

  * Returns INVALID_ARGUMENT if display_name is missing, or is longer than 4096 characters.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateProductSetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.CreateProductSetRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ProductSet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ProductSet)` | The call object.  
  
### CreateProductSetAsync(CreateProductSetRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ProductSet> CreateProductSetAsync(CreateProductSetRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates and returns a new ProductSet resource.

Possible errors:

  * Returns INVALID_ARGUMENT if display_name is missing, or is longer than 4096 characters.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateProductSetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.CreateProductSetRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ProductSet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ProductSet)` | The call object.  
  
### CreateReferenceImage(CreateReferenceImageRequest, CallOptions)
    
    
    public virtual ReferenceImage CreateReferenceImage(CreateReferenceImageRequest request, CallOptions options)

Creates and returns a new ReferenceImage resource.

The `bounding_poly` field is optional. If `bounding_poly` is not specified, the system will try to detect regions of interest in the image that are compatible with the product_category on the parent product. If it is specified, detection is ALWAYS skipped. The system converts polygons into non-rotated rectangles.

Note that the pipeline will resize the image if the image resolution is too large to process (above 50MP).

Possible errors:

  * Returns INVALID_ARGUMENT if the image_uri is missing or longer than 4096 characters.
  * Returns INVALID_ARGUMENT if the product does not exist.
  * Returns INVALID_ARGUMENT if bounding_poly is not provided, and nothing compatible with the parent product's product_category is detected.
  * Returns INVALID_ARGUMENT if bounding_poly contains more than 10 polygons.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateReferenceImageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.CreateReferenceImageRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ReferenceImage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ReferenceImage)` | The response received from the server.  
  
### CreateReferenceImage(CreateReferenceImageRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ReferenceImage CreateReferenceImage(CreateReferenceImageRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates and returns a new ReferenceImage resource.

The `bounding_poly` field is optional. If `bounding_poly` is not specified, the system will try to detect regions of interest in the image that are compatible with the product_category on the parent product. If it is specified, detection is ALWAYS skipped. The system converts polygons into non-rotated rectangles.

Note that the pipeline will resize the image if the image resolution is too large to process (above 50MP).

Possible errors:

  * Returns INVALID_ARGUMENT if the image_uri is missing or longer than 4096 characters.
  * Returns INVALID_ARGUMENT if the product does not exist.
  * Returns INVALID_ARGUMENT if bounding_poly is not provided, and nothing compatible with the parent product's product_category is detected.
  * Returns INVALID_ARGUMENT if bounding_poly contains more than 10 polygons.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateReferenceImageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.CreateReferenceImageRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ReferenceImage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ReferenceImage)` | The response received from the server.  
  
### CreateReferenceImageAsync(CreateReferenceImageRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ReferenceImage> CreateReferenceImageAsync(CreateReferenceImageRequest request, CallOptions options)

Creates and returns a new ReferenceImage resource.

The `bounding_poly` field is optional. If `bounding_poly` is not specified, the system will try to detect regions of interest in the image that are compatible with the product_category on the parent product. If it is specified, detection is ALWAYS skipped. The system converts polygons into non-rotated rectangles.

Note that the pipeline will resize the image if the image resolution is too large to process (above 50MP).

Possible errors:

  * Returns INVALID_ARGUMENT if the image_uri is missing or longer than 4096 characters.
  * Returns INVALID_ARGUMENT if the product does not exist.
  * Returns INVALID_ARGUMENT if bounding_poly is not provided, and nothing compatible with the parent product's product_category is detected.
  * Returns INVALID_ARGUMENT if bounding_poly contains more than 10 polygons.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateReferenceImageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.CreateReferenceImageRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ReferenceImage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ReferenceImage)` | The call object.  
  
### CreateReferenceImageAsync(CreateReferenceImageRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ReferenceImage> CreateReferenceImageAsync(CreateReferenceImageRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates and returns a new ReferenceImage resource.

The `bounding_poly` field is optional. If `bounding_poly` is not specified, the system will try to detect regions of interest in the image that are compatible with the product_category on the parent product. If it is specified, detection is ALWAYS skipped. The system converts polygons into non-rotated rectangles.

Note that the pipeline will resize the image if the image resolution is too large to process (above 50MP).

Possible errors:

  * Returns INVALID_ARGUMENT if the image_uri is missing or longer than 4096 characters.
  * Returns INVALID_ARGUMENT if the product does not exist.
  * Returns INVALID_ARGUMENT if bounding_poly is not provided, and nothing compatible with the parent product's product_category is detected.
  * Returns INVALID_ARGUMENT if bounding_poly contains more than 10 polygons.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateReferenceImageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.CreateReferenceImageRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ReferenceImage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ReferenceImage)` | The call object.  
  
### DeleteProduct(DeleteProductRequest, CallOptions)
    
    
    public virtual Empty DeleteProduct(DeleteProductRequest request, CallOptions options)

Permanently deletes a product and its reference images.

Metadata of the product and all its images will be deleted right away, but search queries against ProductSets containing the product may still work until all related caches are refreshed.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteProductRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.DeleteProductRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response received from the server.  
  
### DeleteProduct(DeleteProductRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Empty DeleteProduct(DeleteProductRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Permanently deletes a product and its reference images.

Metadata of the product and all its images will be deleted right away, but search queries against ProductSets containing the product may still work until all related caches are refreshed.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteProductRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.DeleteProductRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response received from the server.  
  
### DeleteProductAsync(DeleteProductRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteProductAsync(DeleteProductRequest request, CallOptions options)

Permanently deletes a product and its reference images.

Metadata of the product and all its images will be deleted right away, but search queries against ProductSets containing the product may still work until all related caches are refreshed.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteProductRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.DeleteProductRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The call object.  
  
### DeleteProductAsync(DeleteProductRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteProductAsync(DeleteProductRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Permanently deletes a product and its reference images.

Metadata of the product and all its images will be deleted right away, but search queries against ProductSets containing the product may still work until all related caches are refreshed.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteProductRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.DeleteProductRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The call object.  
  
### DeleteProductSet(DeleteProductSetRequest, CallOptions)
    
    
    public virtual Empty DeleteProductSet(DeleteProductSetRequest request, CallOptions options)

Permanently deletes a ProductSet. Products and ReferenceImages in the ProductSet are not deleted.

The actual image files are not deleted from Google Cloud Storage.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteProductSetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.DeleteProductSetRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response received from the server.  
  
### DeleteProductSet(DeleteProductSetRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Empty DeleteProductSet(DeleteProductSetRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Permanently deletes a ProductSet. Products and ReferenceImages in the ProductSet are not deleted.

The actual image files are not deleted from Google Cloud Storage.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteProductSetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.DeleteProductSetRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response received from the server.  
  
### DeleteProductSetAsync(DeleteProductSetRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteProductSetAsync(DeleteProductSetRequest request, CallOptions options)

Permanently deletes a ProductSet. Products and ReferenceImages in the ProductSet are not deleted.

The actual image files are not deleted from Google Cloud Storage.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteProductSetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.DeleteProductSetRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The call object.  
  
### DeleteProductSetAsync(DeleteProductSetRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteProductSetAsync(DeleteProductSetRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Permanently deletes a ProductSet. Products and ReferenceImages in the ProductSet are not deleted.

The actual image files are not deleted from Google Cloud Storage.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteProductSetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.DeleteProductSetRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The call object.  
  
### DeleteReferenceImage(DeleteReferenceImageRequest, CallOptions)
    
    
    public virtual Empty DeleteReferenceImage(DeleteReferenceImageRequest request, CallOptions options)

Permanently deletes a reference image.

The image metadata will be deleted right away, but search queries against ProductSets containing the image may still work until all related caches are refreshed.

The actual image files are not deleted from Google Cloud Storage.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteReferenceImageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.DeleteReferenceImageRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response received from the server.  
  
### DeleteReferenceImage(DeleteReferenceImageRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Empty DeleteReferenceImage(DeleteReferenceImageRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Permanently deletes a reference image.

The image metadata will be deleted right away, but search queries against ProductSets containing the image may still work until all related caches are refreshed.

The actual image files are not deleted from Google Cloud Storage.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteReferenceImageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.DeleteReferenceImageRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response received from the server.  
  
### DeleteReferenceImageAsync(DeleteReferenceImageRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteReferenceImageAsync(DeleteReferenceImageRequest request, CallOptions options)

Permanently deletes a reference image.

The image metadata will be deleted right away, but search queries against ProductSets containing the image may still work until all related caches are refreshed.

The actual image files are not deleted from Google Cloud Storage.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteReferenceImageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.DeleteReferenceImageRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The call object.  
  
### DeleteReferenceImageAsync(DeleteReferenceImageRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteReferenceImageAsync(DeleteReferenceImageRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Permanently deletes a reference image.

The image metadata will be deleted right away, but search queries against ProductSets containing the image may still work until all related caches are refreshed.

The actual image files are not deleted from Google Cloud Storage.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteReferenceImageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.DeleteReferenceImageRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The call object.  
  
### GetProduct(GetProductRequest, CallOptions)
    
    
    public virtual Product GetProduct(GetProductRequest request, CallOptions options)

Gets information associated with a Product.

Possible errors:

  * Returns NOT_FOUND if the Product does not exist.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetProductRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.GetProductRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Product](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.Product)` | The response received from the server.  
  
### GetProduct(GetProductRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Product GetProduct(GetProductRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets information associated with a Product.

Possible errors:

  * Returns NOT_FOUND if the Product does not exist.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetProductRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.GetProductRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Product](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.Product)` | The response received from the server.  
  
### GetProductAsync(GetProductRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Product> GetProductAsync(GetProductRequest request, CallOptions options)

Gets information associated with a Product.

Possible errors:

  * Returns NOT_FOUND if the Product does not exist.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetProductRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.GetProductRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Product](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.Product)` | The call object.  
  
### GetProductAsync(GetProductRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Product> GetProductAsync(GetProductRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets information associated with a Product.

Possible errors:

  * Returns NOT_FOUND if the Product does not exist.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetProductRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.GetProductRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Product](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.Product)` | The call object.  
  
### GetProductSet(GetProductSetRequest, CallOptions)
    
    
    public virtual ProductSet GetProductSet(GetProductSetRequest request, CallOptions options)

Gets information associated with a ProductSet.

Possible errors:

  * Returns NOT_FOUND if the ProductSet does not exist.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetProductSetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.GetProductSetRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ProductSet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ProductSet)` | The response received from the server.  
  
### GetProductSet(GetProductSetRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ProductSet GetProductSet(GetProductSetRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets information associated with a ProductSet.

Possible errors:

  * Returns NOT_FOUND if the ProductSet does not exist.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetProductSetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.GetProductSetRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ProductSet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ProductSet)` | The response received from the server.  
  
### GetProductSetAsync(GetProductSetRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ProductSet> GetProductSetAsync(GetProductSetRequest request, CallOptions options)

Gets information associated with a ProductSet.

Possible errors:

  * Returns NOT_FOUND if the ProductSet does not exist.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetProductSetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.GetProductSetRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ProductSet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ProductSet)` | The call object.  
  
### GetProductSetAsync(GetProductSetRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ProductSet> GetProductSetAsync(GetProductSetRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets information associated with a ProductSet.

Possible errors:

  * Returns NOT_FOUND if the ProductSet does not exist.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetProductSetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.GetProductSetRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ProductSet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ProductSet)` | The call object.  
  
### GetReferenceImage(GetReferenceImageRequest, CallOptions)
    
    
    public virtual ReferenceImage GetReferenceImage(GetReferenceImageRequest request, CallOptions options)

Gets information associated with a ReferenceImage.

Possible errors:

  * Returns NOT_FOUND if the specified image does not exist.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetReferenceImageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.GetReferenceImageRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ReferenceImage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ReferenceImage)` | The response received from the server.  
  
### GetReferenceImage(GetReferenceImageRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ReferenceImage GetReferenceImage(GetReferenceImageRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets information associated with a ReferenceImage.

Possible errors:

  * Returns NOT_FOUND if the specified image does not exist.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetReferenceImageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.GetReferenceImageRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ReferenceImage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ReferenceImage)` | The response received from the server.  
  
### GetReferenceImageAsync(GetReferenceImageRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ReferenceImage> GetReferenceImageAsync(GetReferenceImageRequest request, CallOptions options)

Gets information associated with a ReferenceImage.

Possible errors:

  * Returns NOT_FOUND if the specified image does not exist.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetReferenceImageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.GetReferenceImageRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ReferenceImage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ReferenceImage)` | The call object.  
  
### GetReferenceImageAsync(GetReferenceImageRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ReferenceImage> GetReferenceImageAsync(GetReferenceImageRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets information associated with a ReferenceImage.

Possible errors:

  * Returns NOT_FOUND if the specified image does not exist.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetReferenceImageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.GetReferenceImageRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ReferenceImage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ReferenceImage)` | The call object.  
  
### ImportProductSets(ImportProductSetsRequest, CallOptions)
    
    
    public virtual Operation ImportProductSets(ImportProductSetsRequest request, CallOptions options)

Asynchronous API that imports a list of reference images to specified product sets based on a list of image information.

The [google.longrunning.Operation][google.longrunning.Operation] API can be used to keep track of the progress and results of the request. `Operation.metadata` contains `BatchOperationMetadata`. (progress) `Operation.response` contains `ImportProductSetsResponse`. (results)

The input source of this method is a csv file on Google Cloud Storage. For the format of the csv file please see [ImportProductSetsGcsSource.csv_file_uri][google.cloud.vision.v1.ImportProductSetsGcsSource.csv_file_uri].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportProductSetsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ImportProductSetsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### ImportProductSets(ImportProductSetsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation ImportProductSets(ImportProductSetsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Asynchronous API that imports a list of reference images to specified product sets based on a list of image information.

The [google.longrunning.Operation][google.longrunning.Operation] API can be used to keep track of the progress and results of the request. `Operation.metadata` contains `BatchOperationMetadata`. (progress) `Operation.response` contains `ImportProductSetsResponse`. (results)

The input source of this method is a csv file on Google Cloud Storage. For the format of the csv file please see [ImportProductSetsGcsSource.csv_file_uri][google.cloud.vision.v1.ImportProductSetsGcsSource.csv_file_uri].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportProductSetsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ImportProductSetsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### ImportProductSetsAsync(ImportProductSetsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> ImportProductSetsAsync(ImportProductSetsRequest request, CallOptions options)

Asynchronous API that imports a list of reference images to specified product sets based on a list of image information.

The [google.longrunning.Operation][google.longrunning.Operation] API can be used to keep track of the progress and results of the request. `Operation.metadata` contains `BatchOperationMetadata`. (progress) `Operation.response` contains `ImportProductSetsResponse`. (results)

The input source of this method is a csv file on Google Cloud Storage. For the format of the csv file please see [ImportProductSetsGcsSource.csv_file_uri][google.cloud.vision.v1.ImportProductSetsGcsSource.csv_file_uri].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportProductSetsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ImportProductSetsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### ImportProductSetsAsync(ImportProductSetsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> ImportProductSetsAsync(ImportProductSetsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Asynchronous API that imports a list of reference images to specified product sets based on a list of image information.

The [google.longrunning.Operation][google.longrunning.Operation] API can be used to keep track of the progress and results of the request. `Operation.metadata` contains `BatchOperationMetadata`. (progress) `Operation.response` contains `ImportProductSetsResponse`. (results)

The input source of this method is a csv file on Google Cloud Storage. For the format of the csv file please see [ImportProductSetsGcsSource.csv_file_uri][google.cloud.vision.v1.ImportProductSetsGcsSource.csv_file_uri].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportProductSetsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ImportProductSetsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### ListProductSets(ListProductSetsRequest, CallOptions)
    
    
    public virtual ListProductSetsResponse ListProductSets(ListProductSetsRequest request, CallOptions options)

Lists ProductSets in an unspecified order.

Possible errors:

  * Returns INVALID_ARGUMENT if page_size is greater than 100, or less than 1.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListProductSetsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ListProductSetsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListProductSetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ListProductSetsResponse)` | The response received from the server.  
  
### ListProductSets(ListProductSetsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListProductSetsResponse ListProductSets(ListProductSetsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists ProductSets in an unspecified order.

Possible errors:

  * Returns INVALID_ARGUMENT if page_size is greater than 100, or less than 1.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListProductSetsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ListProductSetsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListProductSetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ListProductSetsResponse)` | The response received from the server.  
  
### ListProductSetsAsync(ListProductSetsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListProductSetsResponse> ListProductSetsAsync(ListProductSetsRequest request, CallOptions options)

Lists ProductSets in an unspecified order.

Possible errors:

  * Returns INVALID_ARGUMENT if page_size is greater than 100, or less than 1.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListProductSetsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ListProductSetsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListProductSetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ListProductSetsResponse)` | The call object.  
  
### ListProductSetsAsync(ListProductSetsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListProductSetsResponse> ListProductSetsAsync(ListProductSetsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists ProductSets in an unspecified order.

Possible errors:

  * Returns INVALID_ARGUMENT if page_size is greater than 100, or less than 1.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListProductSetsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ListProductSetsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListProductSetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ListProductSetsResponse)` | The call object.  
  
### ListProducts(ListProductsRequest, CallOptions)
    
    
    public virtual ListProductsResponse ListProducts(ListProductsRequest request, CallOptions options)

Lists products in an unspecified order.

Possible errors:

  * Returns INVALID_ARGUMENT if page_size is greater than 100 or less than 1.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListProductsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ListProductsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListProductsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ListProductsResponse)` | The response received from the server.  
  
### ListProducts(ListProductsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListProductsResponse ListProducts(ListProductsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists products in an unspecified order.

Possible errors:

  * Returns INVALID_ARGUMENT if page_size is greater than 100 or less than 1.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListProductsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ListProductsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListProductsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ListProductsResponse)` | The response received from the server.  
  
### ListProductsAsync(ListProductsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListProductsResponse> ListProductsAsync(ListProductsRequest request, CallOptions options)

Lists products in an unspecified order.

Possible errors:

  * Returns INVALID_ARGUMENT if page_size is greater than 100 or less than 1.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListProductsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ListProductsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListProductsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ListProductsResponse)` | The call object.  
  
### ListProductsAsync(ListProductsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListProductsResponse> ListProductsAsync(ListProductsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists products in an unspecified order.

Possible errors:

  * Returns INVALID_ARGUMENT if page_size is greater than 100 or less than 1.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListProductsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ListProductsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListProductsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ListProductsResponse)` | The call object.  
  
### ListProductsInProductSet(ListProductsInProductSetRequest, CallOptions)
    
    
    public virtual ListProductsInProductSetResponse ListProductsInProductSet(ListProductsInProductSetRequest request, CallOptions options)

Lists the Products in a ProductSet, in an unspecified order. If the ProductSet does not exist, the products field of the response will be empty.

Possible errors:

  * Returns INVALID_ARGUMENT if page_size is greater than 100 or less than 1.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListProductsInProductSetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ListProductsInProductSetRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListProductsInProductSetResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ListProductsInProductSetResponse)` | The response received from the server.  
  
### ListProductsInProductSet(ListProductsInProductSetRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListProductsInProductSetResponse ListProductsInProductSet(ListProductsInProductSetRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists the Products in a ProductSet, in an unspecified order. If the ProductSet does not exist, the products field of the response will be empty.

Possible errors:

  * Returns INVALID_ARGUMENT if page_size is greater than 100 or less than 1.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListProductsInProductSetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ListProductsInProductSetRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListProductsInProductSetResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ListProductsInProductSetResponse)` | The response received from the server.  
  
### ListProductsInProductSetAsync(ListProductsInProductSetRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListProductsInProductSetResponse> ListProductsInProductSetAsync(ListProductsInProductSetRequest request, CallOptions options)

Lists the Products in a ProductSet, in an unspecified order. If the ProductSet does not exist, the products field of the response will be empty.

Possible errors:

  * Returns INVALID_ARGUMENT if page_size is greater than 100 or less than 1.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListProductsInProductSetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ListProductsInProductSetRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListProductsInProductSetResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ListProductsInProductSetResponse)` | The call object.  
  
### ListProductsInProductSetAsync(ListProductsInProductSetRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListProductsInProductSetResponse> ListProductsInProductSetAsync(ListProductsInProductSetRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists the Products in a ProductSet, in an unspecified order. If the ProductSet does not exist, the products field of the response will be empty.

Possible errors:

  * Returns INVALID_ARGUMENT if page_size is greater than 100 or less than 1.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListProductsInProductSetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ListProductsInProductSetRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListProductsInProductSetResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ListProductsInProductSetResponse)` | The call object.  
  
### ListReferenceImages(ListReferenceImagesRequest, CallOptions)
    
    
    public virtual ListReferenceImagesResponse ListReferenceImages(ListReferenceImagesRequest request, CallOptions options)

Lists reference images.

Possible errors:

  * Returns NOT_FOUND if the parent product does not exist.
  * Returns INVALID_ARGUMENT if the page_size is greater than 100, or less than 1.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListReferenceImagesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ListReferenceImagesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListReferenceImagesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ListReferenceImagesResponse)` | The response received from the server.  
  
### ListReferenceImages(ListReferenceImagesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListReferenceImagesResponse ListReferenceImages(ListReferenceImagesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists reference images.

Possible errors:

  * Returns NOT_FOUND if the parent product does not exist.
  * Returns INVALID_ARGUMENT if the page_size is greater than 100, or less than 1.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListReferenceImagesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ListReferenceImagesRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListReferenceImagesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ListReferenceImagesResponse)` | The response received from the server.  
  
### ListReferenceImagesAsync(ListReferenceImagesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListReferenceImagesResponse> ListReferenceImagesAsync(ListReferenceImagesRequest request, CallOptions options)

Lists reference images.

Possible errors:

  * Returns NOT_FOUND if the parent product does not exist.
  * Returns INVALID_ARGUMENT if the page_size is greater than 100, or less than 1.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListReferenceImagesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ListReferenceImagesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListReferenceImagesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ListReferenceImagesResponse)` | The call object.  
  
### ListReferenceImagesAsync(ListReferenceImagesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListReferenceImagesResponse> ListReferenceImagesAsync(ListReferenceImagesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists reference images.

Possible errors:

  * Returns NOT_FOUND if the parent product does not exist.
  * Returns INVALID_ARGUMENT if the page_size is greater than 100, or less than 1.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListReferenceImagesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ListReferenceImagesRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListReferenceImagesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ListReferenceImagesResponse)` | The call object.  
  
### NewInstance(ClientBaseConfiguration)
    
    
    protected override ProductSearch.ProductSearchClient NewInstance(ClientBase.ClientBaseConfiguration configuration)

Creates a new instance of client from given `ClientBaseConfiguration`.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductSearch](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ProductSearch)[ProductSearchClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ProductSearch.ProductSearchClient)` |   
**Overrides**

Grpc.Core.ClientBase<Google.Cloud.Vision.V1.ProductSearch.ProductSearchClient>.NewInstance(Grpc.Core.ClientBase.ClientBaseConfiguration)

### PurgeProducts(PurgeProductsRequest, CallOptions)
    
    
    public virtual Operation PurgeProducts(PurgeProductsRequest request, CallOptions options)

Asynchronous API to delete all Products in a ProductSet or all Products that are in no ProductSet.

If a Product is a member of the specified ProductSet in addition to other ProductSets, the Product will still be deleted.

It is recommended to not delete the specified ProductSet until after this operation has completed. It is also recommended to not add any of the Products involved in the batch delete to a new ProductSet while this operation is running because those Products may still end up deleted.

It's not possible to undo the PurgeProducts operation. Therefore, it is recommended to keep the csv files used in ImportProductSets (if that was how you originally built the Product Set) before starting PurgeProducts, in case you need to re-import the data after deletion.

If the plan is to purge all of the Products from a ProductSet and then re-use the empty ProductSet to re-import new Products into the empty ProductSet, you must wait until the PurgeProducts operation has finished for that ProductSet.

The [google.longrunning.Operation][google.longrunning.Operation] API can be used to keep track of the progress and results of the request. `Operation.metadata` contains `BatchOperationMetadata`. (progress)

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PurgeProductsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.PurgeProductsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### PurgeProducts(PurgeProductsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation PurgeProducts(PurgeProductsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Asynchronous API to delete all Products in a ProductSet or all Products that are in no ProductSet.

If a Product is a member of the specified ProductSet in addition to other ProductSets, the Product will still be deleted.

It is recommended to not delete the specified ProductSet until after this operation has completed. It is also recommended to not add any of the Products involved in the batch delete to a new ProductSet while this operation is running because those Products may still end up deleted.

It's not possible to undo the PurgeProducts operation. Therefore, it is recommended to keep the csv files used in ImportProductSets (if that was how you originally built the Product Set) before starting PurgeProducts, in case you need to re-import the data after deletion.

If the plan is to purge all of the Products from a ProductSet and then re-use the empty ProductSet to re-import new Products into the empty ProductSet, you must wait until the PurgeProducts operation has finished for that ProductSet.

The [google.longrunning.Operation][google.longrunning.Operation] API can be used to keep track of the progress and results of the request. `Operation.metadata` contains `BatchOperationMetadata`. (progress)

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PurgeProductsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.PurgeProductsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### PurgeProductsAsync(PurgeProductsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> PurgeProductsAsync(PurgeProductsRequest request, CallOptions options)

Asynchronous API to delete all Products in a ProductSet or all Products that are in no ProductSet.

If a Product is a member of the specified ProductSet in addition to other ProductSets, the Product will still be deleted.

It is recommended to not delete the specified ProductSet until after this operation has completed. It is also recommended to not add any of the Products involved in the batch delete to a new ProductSet while this operation is running because those Products may still end up deleted.

It's not possible to undo the PurgeProducts operation. Therefore, it is recommended to keep the csv files used in ImportProductSets (if that was how you originally built the Product Set) before starting PurgeProducts, in case you need to re-import the data after deletion.

If the plan is to purge all of the Products from a ProductSet and then re-use the empty ProductSet to re-import new Products into the empty ProductSet, you must wait until the PurgeProducts operation has finished for that ProductSet.

The [google.longrunning.Operation][google.longrunning.Operation] API can be used to keep track of the progress and results of the request. `Operation.metadata` contains `BatchOperationMetadata`. (progress)

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PurgeProductsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.PurgeProductsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### PurgeProductsAsync(PurgeProductsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> PurgeProductsAsync(PurgeProductsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Asynchronous API to delete all Products in a ProductSet or all Products that are in no ProductSet.

If a Product is a member of the specified ProductSet in addition to other ProductSets, the Product will still be deleted.

It is recommended to not delete the specified ProductSet until after this operation has completed. It is also recommended to not add any of the Products involved in the batch delete to a new ProductSet while this operation is running because those Products may still end up deleted.

It's not possible to undo the PurgeProducts operation. Therefore, it is recommended to keep the csv files used in ImportProductSets (if that was how you originally built the Product Set) before starting PurgeProducts, in case you need to re-import the data after deletion.

If the plan is to purge all of the Products from a ProductSet and then re-use the empty ProductSet to re-import new Products into the empty ProductSet, you must wait until the PurgeProducts operation has finished for that ProductSet.

The [google.longrunning.Operation][google.longrunning.Operation] API can be used to keep track of the progress and results of the request. `Operation.metadata` contains `BatchOperationMetadata`. (progress)

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PurgeProductsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.PurgeProductsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### RemoveProductFromProductSet(RemoveProductFromProductSetRequest, CallOptions)
    
    
    public virtual Empty RemoveProductFromProductSet(RemoveProductFromProductSetRequest request, CallOptions options)

Removes a Product from the specified ProductSet.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemoveProductFromProductSetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.RemoveProductFromProductSetRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response received from the server.  
  
### RemoveProductFromProductSet(RemoveProductFromProductSetRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Empty RemoveProductFromProductSet(RemoveProductFromProductSetRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Removes a Product from the specified ProductSet.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemoveProductFromProductSetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.RemoveProductFromProductSetRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response received from the server.  
  
### RemoveProductFromProductSetAsync(RemoveProductFromProductSetRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Empty> RemoveProductFromProductSetAsync(RemoveProductFromProductSetRequest request, CallOptions options)

Removes a Product from the specified ProductSet.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemoveProductFromProductSetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.RemoveProductFromProductSetRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The call object.  
  
### RemoveProductFromProductSetAsync(RemoveProductFromProductSetRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Empty> RemoveProductFromProductSetAsync(RemoveProductFromProductSetRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Removes a Product from the specified ProductSet.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemoveProductFromProductSetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.RemoveProductFromProductSetRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The call object.  
  
### UpdateProduct(UpdateProductRequest, CallOptions)
    
    
    public virtual Product UpdateProduct(UpdateProductRequest request, CallOptions options)

Makes changes to a Product resource. Only the `display_name`, `description`, and `labels` fields can be updated right now.

If labels are updated, the change will not be reflected in queries until the next index time.

Possible errors:

  * Returns NOT_FOUND if the Product does not exist.
  * Returns INVALID_ARGUMENT if display_name is present in update_mask but is missing from the request or longer than 4096 characters.
  * Returns INVALID_ARGUMENT if description is present in update_mask but is longer than 4096 characters.
  * Returns INVALID_ARGUMENT if product_category is present in update_mask.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateProductRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.UpdateProductRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Product](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.Product)` | The response received from the server.  
  
### UpdateProduct(UpdateProductRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Product UpdateProduct(UpdateProductRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Makes changes to a Product resource. Only the `display_name`, `description`, and `labels` fields can be updated right now.

If labels are updated, the change will not be reflected in queries until the next index time.

Possible errors:

  * Returns NOT_FOUND if the Product does not exist.
  * Returns INVALID_ARGUMENT if display_name is present in update_mask but is missing from the request or longer than 4096 characters.
  * Returns INVALID_ARGUMENT if description is present in update_mask but is longer than 4096 characters.
  * Returns INVALID_ARGUMENT if product_category is present in update_mask.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateProductRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.UpdateProductRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Product](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.Product)` | The response received from the server.  
  
### UpdateProductAsync(UpdateProductRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Product> UpdateProductAsync(UpdateProductRequest request, CallOptions options)

Makes changes to a Product resource. Only the `display_name`, `description`, and `labels` fields can be updated right now.

If labels are updated, the change will not be reflected in queries until the next index time.

Possible errors:

  * Returns NOT_FOUND if the Product does not exist.
  * Returns INVALID_ARGUMENT if display_name is present in update_mask but is missing from the request or longer than 4096 characters.
  * Returns INVALID_ARGUMENT if description is present in update_mask but is longer than 4096 characters.
  * Returns INVALID_ARGUMENT if product_category is present in update_mask.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateProductRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.UpdateProductRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Product](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.Product)` | The call object.  
  
### UpdateProductAsync(UpdateProductRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Product> UpdateProductAsync(UpdateProductRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Makes changes to a Product resource. Only the `display_name`, `description`, and `labels` fields can be updated right now.

If labels are updated, the change will not be reflected in queries until the next index time.

Possible errors:

  * Returns NOT_FOUND if the Product does not exist.
  * Returns INVALID_ARGUMENT if display_name is present in update_mask but is missing from the request or longer than 4096 characters.
  * Returns INVALID_ARGUMENT if description is present in update_mask but is longer than 4096 characters.
  * Returns INVALID_ARGUMENT if product_category is present in update_mask.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateProductRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.UpdateProductRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Product](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.Product)` | The call object.  
  
### UpdateProductSet(UpdateProductSetRequest, CallOptions)
    
    
    public virtual ProductSet UpdateProductSet(UpdateProductSetRequest request, CallOptions options)

Makes changes to a ProductSet resource. Only display_name can be updated currently.

Possible errors:

  * Returns NOT_FOUND if the ProductSet does not exist.
  * Returns INVALID_ARGUMENT if display_name is present in update_mask but missing from the request or longer than 4096 characters.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateProductSetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.UpdateProductSetRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ProductSet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ProductSet)` | The response received from the server.  
  
### UpdateProductSet(UpdateProductSetRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ProductSet UpdateProductSet(UpdateProductSetRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Makes changes to a ProductSet resource. Only display_name can be updated currently.

Possible errors:

  * Returns NOT_FOUND if the ProductSet does not exist.
  * Returns INVALID_ARGUMENT if display_name is present in update_mask but missing from the request or longer than 4096 characters.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateProductSetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.UpdateProductSetRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ProductSet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ProductSet)` | The response received from the server.  
  
### UpdateProductSetAsync(UpdateProductSetRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ProductSet> UpdateProductSetAsync(UpdateProductSetRequest request, CallOptions options)

Makes changes to a ProductSet resource. Only display_name can be updated currently.

Possible errors:

  * Returns NOT_FOUND if the ProductSet does not exist.
  * Returns INVALID_ARGUMENT if display_name is present in update_mask but missing from the request or longer than 4096 characters.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateProductSetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.UpdateProductSetRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ProductSet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ProductSet)` | The call object.  
  
### UpdateProductSetAsync(UpdateProductSetRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ProductSet> UpdateProductSetAsync(UpdateProductSetRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Makes changes to a ProductSet resource. Only display_name can be updated currently.

Possible errors:

  * Returns NOT_FOUND if the ProductSet does not exist.
  * Returns INVALID_ARGUMENT if display_name is present in update_mask but missing from the request or longer than 4096 characters.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateProductSetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.UpdateProductSetRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ProductSet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ProductSet)` | The call object.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
