---
url: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.ProductReviewsServiceClient
title: Class ProductReviewsServiceClient (0.45.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:40:54.937588+00:00
---

# Class ProductReviewsServiceClient (0.45.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.ProductReviewsServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ProductReviewsServiceClient (0.45.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.45.0 (latest)  0.41.0  0.40.0  0.39.0  0.37.0  0.34.0  0.33.0  0.31.0  0.29.0  0.28.0  0.26.0  0.24.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.16.0  0.14.0  0.13.0  0.10.0  0.9.0  0.8.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-shopping-merchant-reviews/google-shopping-merchant-reviews/src/main/java/com/google/shopping/merchant/reviews/v1beta/ProductReviewsServiceClient.java)| [Product Reference](https://developers.google.com/merchant/api)  
---|---  
  
Service Description: Service to manage product reviews.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductReviewsServiceClient productReviewsServiceClient =
         ProductReviewsServiceClient.create()) {
       ProductReviewName name = ProductReviewName.of("[ACCOUNT]", "[PRODUCTREVIEW]");
       ProductReview response = productReviewsServiceClient.getProductReview(name);
     }
     

Note: close() needs to be called on the ProductReviewsServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetProductReview |  Gets a product review. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getProductReview(GetProductReviewRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getProductReview(ProductReviewName name) 
  * getProductReview(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getProductReviewCallable() 

  
ListProductReviews |  Lists product reviews. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listProductReviews(ListProductReviewsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listProductReviews(AccountName parent) 
  * listProductReviews(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listProductReviewsPagedCallable() 
  * listProductReviewsCallable() 

  
InsertProductReview |  Inserts a product review. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertProductReview(InsertProductReviewRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertProductReviewCallable() 

  
DeleteProductReview |  Deletes a product review. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteProductReview(DeleteProductReviewRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteProductReview(ProductReviewName name) 
  * deleteProductReview(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteProductReviewCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of ProductReviewsServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ProductReviewsServiceSettings productReviewsServiceSettings =
         ProductReviewsServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     ProductReviewsServiceClient productReviewsServiceClient =
         ProductReviewsServiceClient.create(productReviewsServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ProductReviewsServiceSettings productReviewsServiceSettings =
         ProductReviewsServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     ProductReviewsServiceClient productReviewsServiceClient =
         ProductReviewsServiceClient.create(productReviewsServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ProductReviewsServiceSettings productReviewsServiceSettings =
         ProductReviewsServiceSettings.newHttpJsonBuilder().build();
     ProductReviewsServiceClient productReviewsServiceClient =
         ProductReviewsServiceClient.create(productReviewsServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ProductReviewsServiceClient

## Static Methods 

### create()
    
    
    public static final ProductReviewsServiceClient create()

Constructs an instance of ProductReviewsServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[ProductReviewsServiceClient](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.ProductReviewsServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ProductReviewsServiceSettings settings)
    
    
    public static final ProductReviewsServiceClient create(ProductReviewsServiceSettings settings)

Constructs an instance of ProductReviewsServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ProductReviewsServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.ProductReviewsServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductReviewsServiceClient](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.ProductReviewsServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ProductReviewsServiceStub stub)
    
    
    public static final ProductReviewsServiceClient create(ProductReviewsServiceStub stub)

Constructs an instance of ProductReviewsServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(ProductReviewsServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ProductReviewsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.stub.ProductReviewsServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductReviewsServiceClient](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.ProductReviewsServiceClient)` |   
  
## Constructors 

### ProductReviewsServiceClient(ProductReviewsServiceSettings settings)
    
    
    protected ProductReviewsServiceClient(ProductReviewsServiceSettings settings)

Constructs an instance of ProductReviewsServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ProductReviewsServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.ProductReviewsServiceSettings)`  
  
  
### ProductReviewsServiceClient(ProductReviewsServiceStub stub)
    
    
    protected ProductReviewsServiceClient(ProductReviewsServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ProductReviewsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.stub.ProductReviewsServiceStub)`  
  
  
## Methods 

### awaitTermination(long duration, TimeUnit unit)
    
    
    public boolean awaitTermination(long duration, TimeUnit unit)

**Parameters**  
---  
**Name** | **Description**  
`duration` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`unit` | `[TimeUnit](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/TimeUnit.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InterruptedException](https://docs.oracle.com/javase/8/docs/api/java/lang/InterruptedException.html)` |   
  
### close()
    
    
    public final void close()

### deleteProductReview(@Nullable ProductReviewName name)
    
    
    public final void deleteProductReview(@Nullable ProductReviewName name)

Deletes a product review.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductReviewsServiceClient productReviewsServiceClient =
         ProductReviewsServiceClient.create()) {
       ProductReviewName name = ProductReviewName.of("[ACCOUNT]", "[PRODUCTREVIEW]");
       productReviewsServiceClient.deleteProductReview(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.shopping.merchant.reviews.v1beta.ProductReviewName`  
Required. The ID of the Product review. Format: accounts/{account}/productReviews/{productReview}  
  
### deleteProductReview(DeleteProductReviewRequest request)
    
    
    public final void deleteProductReview(DeleteProductReviewRequest request)

Deletes a product review.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductReviewsServiceClient productReviewsServiceClient =
         ProductReviewsServiceClient.create()) {
       DeleteProductReviewRequest request =
           DeleteProductReviewRequest.newBuilder()
               .setName(ProductReviewName.of("[ACCOUNT]", "[PRODUCTREVIEW]").toString())
               .build();
       productReviewsServiceClient.deleteProductReview(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteProductReviewRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.DeleteProductReviewRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteProductReview(String name)
    
    
    public final void deleteProductReview(String name)

Deletes a product review.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductReviewsServiceClient productReviewsServiceClient =
         ProductReviewsServiceClient.create()) {
       String name = ProductReviewName.of("[ACCOUNT]", "[PRODUCTREVIEW]").toString();
       productReviewsServiceClient.deleteProductReview(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID of the Product review. Format: accounts/{account}/productReviews/{productReview}  
  
### deleteProductReviewCallable()
    
    
    public final UnaryCallable<DeleteProductReviewRequest,Empty> deleteProductReviewCallable()

Deletes a product review.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductReviewsServiceClient productReviewsServiceClient =
         ProductReviewsServiceClient.create()) {
       DeleteProductReviewRequest request =
           DeleteProductReviewRequest.newBuilder()
               .setName(ProductReviewName.of("[ACCOUNT]", "[PRODUCTREVIEW]").toString())
               .build();
       ApiFuture<Empty> future =
           productReviewsServiceClient.deleteProductReviewCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteProductReviewRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.DeleteProductReviewRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getProductReview(@Nullable ProductReviewName name)
    
    
    public final ProductReview getProductReview(@Nullable ProductReviewName name)

Gets a product review.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductReviewsServiceClient productReviewsServiceClient =
         ProductReviewsServiceClient.create()) {
       ProductReviewName name = ProductReviewName.of("[ACCOUNT]", "[PRODUCTREVIEW]");
       ProductReview response = productReviewsServiceClient.getProductReview(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.shopping.merchant.reviews.v1beta.ProductReviewName`  
Required. The ID of the merchant review. Format: accounts/{account}/productReviews/{productReview}  
**Returns**  
---  
**Type** | **Description**  
`[ProductReview](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.ProductReview)` |   
  
### getProductReview(GetProductReviewRequest request)
    
    
    public final ProductReview getProductReview(GetProductReviewRequest request)

Gets a product review.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductReviewsServiceClient productReviewsServiceClient =
         ProductReviewsServiceClient.create()) {
       GetProductReviewRequest request =
           GetProductReviewRequest.newBuilder()
               .setName(ProductReviewName.of("[ACCOUNT]", "[PRODUCTREVIEW]").toString())
               .build();
       ProductReview response = productReviewsServiceClient.getProductReview(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetProductReviewRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.GetProductReviewRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ProductReview](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.ProductReview)` |   
  
### getProductReview(String name)
    
    
    public final ProductReview getProductReview(String name)

Gets a product review.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductReviewsServiceClient productReviewsServiceClient =
         ProductReviewsServiceClient.create()) {
       String name = ProductReviewName.of("[ACCOUNT]", "[PRODUCTREVIEW]").toString();
       ProductReview response = productReviewsServiceClient.getProductReview(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID of the merchant review. Format: accounts/{account}/productReviews/{productReview}  
**Returns**  
---  
**Type** | **Description**  
`[ProductReview](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.ProductReview)` |   
  
### getProductReviewCallable()
    
    
    public final UnaryCallable<GetProductReviewRequest,ProductReview> getProductReviewCallable()

Gets a product review.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductReviewsServiceClient productReviewsServiceClient =
         ProductReviewsServiceClient.create()) {
       GetProductReviewRequest request =
           GetProductReviewRequest.newBuilder()
               .setName(ProductReviewName.of("[ACCOUNT]", "[PRODUCTREVIEW]").toString())
               .build();
       ApiFuture<ProductReview> future =
           productReviewsServiceClient.getProductReviewCallable().futureCall(request);
       // Do something.
       ProductReview response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetProductReviewRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.GetProductReviewRequest),[ProductReview](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.ProductReview)>` |   
  
### getSettings()
    
    
    public final @Nullable ProductReviewsServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.shopping.merchant.reviews.v1beta.ProductReviewsServiceSettings` |   
  
### getStub()
    
    
    public ProductReviewsServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[ProductReviewsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.stub.ProductReviewsServiceStub)` |   
  
### insertProductReview(InsertProductReviewRequest request)
    
    
    public final ProductReview insertProductReview(InsertProductReviewRequest request)

Inserts a product review.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductReviewsServiceClient productReviewsServiceClient =
         ProductReviewsServiceClient.create()) {
       InsertProductReviewRequest request =
           InsertProductReviewRequest.newBuilder()
               .setParent("parent-995424086")
               .setProductReview(ProductReview.newBuilder().build())
               .setDataSource("dataSource1272470629")
               .build();
       ProductReview response = productReviewsServiceClient.insertProductReview(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertProductReviewRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.InsertProductReviewRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ProductReview](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.ProductReview)` |   
  
### insertProductReviewCallable()
    
    
    public final UnaryCallable<InsertProductReviewRequest,ProductReview> insertProductReviewCallable()

Inserts a product review.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductReviewsServiceClient productReviewsServiceClient =
         ProductReviewsServiceClient.create()) {
       InsertProductReviewRequest request =
           InsertProductReviewRequest.newBuilder()
               .setParent("parent-995424086")
               .setProductReview(ProductReview.newBuilder().build())
               .setDataSource("dataSource1272470629")
               .build();
       ApiFuture<ProductReview> future =
           productReviewsServiceClient.insertProductReviewCallable().futureCall(request);
       // Do something.
       ProductReview response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertProductReviewRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.InsertProductReviewRequest),[ProductReview](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.ProductReview)>` |   
  
### isShutdown()
    
    
    public boolean isShutdown()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### isTerminated()
    
    
    public boolean isTerminated()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### listProductReviews(@Nullable AccountName parent)
    
    
    public final ProductReviewsServiceClient.ListProductReviewsPagedResponse listProductReviews(@Nullable AccountName parent)

Lists product reviews.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductReviewsServiceClient productReviewsServiceClient =
         ProductReviewsServiceClient.create()) {
       AccountName parent = AccountName.of("[ACCOUNT]");
       for (ProductReview element :
           productReviewsServiceClient.listProductReviews(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.shopping.merchant.reviews.v1beta.AccountName`  
Required. The account to list product reviews for. Format: accounts/{account}  
**Returns**  
---  
**Type** | **Description**  
`[ProductReviewsServiceClient.ListProductReviewsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.ProductReviewsServiceClient.ListProductReviewsPagedResponse)` |   
  
### listProductReviews(ListProductReviewsRequest request)
    
    
    public final ProductReviewsServiceClient.ListProductReviewsPagedResponse listProductReviews(ListProductReviewsRequest request)

Lists product reviews.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductReviewsServiceClient productReviewsServiceClient =
         ProductReviewsServiceClient.create()) {
       ListProductReviewsRequest request =
           ListProductReviewsRequest.newBuilder()
               .setParent(AccountName.of("[ACCOUNT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (ProductReview element :
           productReviewsServiceClient.listProductReviews(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListProductReviewsRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.ListProductReviewsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ProductReviewsServiceClient.ListProductReviewsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.ProductReviewsServiceClient.ListProductReviewsPagedResponse)` |   
  
### listProductReviews(String parent)
    
    
    public final ProductReviewsServiceClient.ListProductReviewsPagedResponse listProductReviews(String parent)

Lists product reviews.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductReviewsServiceClient productReviewsServiceClient =
         ProductReviewsServiceClient.create()) {
       String parent = AccountName.of("[ACCOUNT]").toString();
       for (ProductReview element :
           productReviewsServiceClient.listProductReviews(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The account to list product reviews for. Format: accounts/{account}  
**Returns**  
---  
**Type** | **Description**  
`[ProductReviewsServiceClient.ListProductReviewsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.ProductReviewsServiceClient.ListProductReviewsPagedResponse)` |   
  
### listProductReviewsCallable()
    
    
    public final UnaryCallable<ListProductReviewsRequest,ListProductReviewsResponse> listProductReviewsCallable()

Lists product reviews.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductReviewsServiceClient productReviewsServiceClient =
         ProductReviewsServiceClient.create()) {
       ListProductReviewsRequest request =
           ListProductReviewsRequest.newBuilder()
               .setParent(AccountName.of("[ACCOUNT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListProductReviewsResponse response =
             productReviewsServiceClient.listProductReviewsCallable().call(request);
         for (ProductReview element : response.getProductReviewsList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListProductReviewsRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.ListProductReviewsRequest),[ListProductReviewsResponse](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.ListProductReviewsResponse)>` |   
  
### listProductReviewsPagedCallable()
    
    
    public final UnaryCallable<ListProductReviewsRequest,ProductReviewsServiceClient.ListProductReviewsPagedResponse> listProductReviewsPagedCallable()

Lists product reviews.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductReviewsServiceClient productReviewsServiceClient =
         ProductReviewsServiceClient.create()) {
       ListProductReviewsRequest request =
           ListProductReviewsRequest.newBuilder()
               .setParent(AccountName.of("[ACCOUNT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<ProductReview> future =
           productReviewsServiceClient.listProductReviewsPagedCallable().futureCall(request);
       // Do something.
       for (ProductReview element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListProductReviewsRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.ListProductReviewsRequest),[ListProductReviewsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.ProductReviewsServiceClient.ListProductReviewsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
