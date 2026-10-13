---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ProductServiceClient
title: Class ProductServiceClient (2.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:52:22.523746+00:00
---

# Class ProductServiceClient (2.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ProductServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ProductServiceClient (2.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.101.0 (latest)  2.97.0  2.96.0  2.95.0  2.93.0  2.90.0  2.89.0  2.87.0  2.85.0  2.84.0  2.82.0  2.80.0  2.78.0  2.77.0  2.76.0  2.75.0  2.74.0  2.72.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.1  2.4.0  2.3.0  2.2.3  2.1.0  2.0.19 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-retail/google-cloud-retail/src/main/java/com/google/cloud/retail/v2/ProductServiceClient.java)| [Product Reference](https://cloud.google.com/solutions/retail)  
---|---  
  
Service Description: Service for ingesting Product information of the customer's website.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductServiceClient productServiceClient = ProductServiceClient.create()) {
       BranchName parent = BranchName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]");
       Product product = Product.newBuilder().build();
       String productId = "productId-1051830678";
       Product response = productServiceClient.createProduct(parent, product, productId);
     }
     

Note: close() needs to be called on the ProductServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateProduct |  Creates a Product. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createProduct(CreateProductRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createProduct(BranchName parent, Product product, String productId) 
  * createProduct(String parent, Product product, String productId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createProductCallable() 

  
GetProduct |  Gets a Product. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getProduct(GetProductRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getProduct(ProductName name) 
  * getProduct(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getProductCallable() 

  
ListProducts |  Gets a list of Products. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listProducts(ListProductsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listProducts(BranchName parent) 
  * listProducts(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listProductsPagedCallable() 
  * listProductsCallable() 

  
UpdateProduct |  Updates a Product. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateProduct(UpdateProductRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateProduct(Product product, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateProductCallable() 

  
DeleteProduct |  Deletes a Product. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteProduct(DeleteProductRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteProduct(ProductName name) 
  * deleteProduct(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteProductCallable() 

  
PurgeProducts |  Permanently deletes all selected Products under a branch.  This process is asynchronous. If the request is valid, the removal will be enqueued and processed offline. Depending on the number of Products, this operation could take hours to complete. Before the operation completes, some Products may still be returned by ProductService.GetProduct or ProductService.ListProducts.  Depending on the number of Products, this operation could take hours to complete. To get a sample of Products that would be deleted, set PurgeProductsRequest.force to false. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * purgeProductsAsync(PurgeProductsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * purgeProductsOperationCallable() 
  * purgeProductsCallable() 

  
ImportProducts |  Bulk import of multiple Products.  Request processing may be synchronous. Non-existing items are created.  Note that it is possible for a subset of the Products to be successfully updated. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * importProductsAsync(ImportProductsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * importProductsOperationCallable() 
  * importProductsCallable() 

  
SetInventory |  Updates inventory information for a Product while respecting the last update timestamps of each inventory field.  This process is asynchronous and does not require the Product to exist before updating fulfillment information. If the request is valid, the update is enqueued and processed downstream. As a consequence, when a response is returned, updates are not immediately manifested in the Product queried by ProductService.GetProduct or ProductService.ListProducts.  When inventory is updated with ProductService.CreateProduct and ProductService.UpdateProduct, the specified inventory field value(s) overwrite any existing value(s) while ignoring the last update time for this field. Furthermore, the last update times for the specified inventory fields are overwritten by the times of the ProductService.CreateProduct or ProductService.UpdateProduct request.  If no inventory fields are set in CreateProductRequest.product, then any pre-existing inventory information for this product is used.  If no inventory fields are set in SetInventoryRequest.set_mask, then any existing inventory information is preserved.  Pre-existing inventory information can only be updated with ProductService.SetInventory, ProductService.AddFulfillmentPlaces, and ProductService.RemoveFulfillmentPlaces.  The returned Operations is obsolete after one day, and the GetOperation API returns `NOT_FOUND` afterwards.  If conflicting updates are issued, the Operations associated with the stale updates are not marked as done until they are obsolete. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setInventoryAsync(SetInventoryRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setInventoryAsync(Product inventory, FieldMask setMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setInventoryOperationCallable() 
  * setInventoryCallable() 

  
AddFulfillmentPlaces |  We recommend that you use the ProductService.AddLocalInventories method instead of the ProductService.AddFulfillmentPlaces method. ProductService.AddLocalInventories achieves the same results but provides more fine-grained control over ingesting local inventory data.  Incrementally adds place IDs to Product.fulfillment_info.place_ids.  This process is asynchronous and does not require the Product to exist before updating fulfillment information. If the request is valid, the update will be enqueued and processed downstream. As a consequence, when a response is returned, the added place IDs are not immediately manifested in the Product queried by ProductService.GetProduct or ProductService.ListProducts.  The returned Operations will be obsolete after 1 day, and GetOperation API will return NOT_FOUND afterwards.  If conflicting updates are issued, the Operations associated with the stale updates will not be marked as done until being obsolete. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * addFulfillmentPlacesAsync(AddFulfillmentPlacesRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * addFulfillmentPlacesAsync(ProductName product) 
  * addFulfillmentPlacesAsync(String product) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * addFulfillmentPlacesOperationCallable() 
  * addFulfillmentPlacesCallable() 

  
RemoveFulfillmentPlaces |  We recommend that you use the ProductService.RemoveLocalInventories method instead of the ProductService.RemoveFulfillmentPlaces method. ProductService.RemoveLocalInventories achieves the same results but provides more fine-grained control over ingesting local inventory data.  Incrementally removes place IDs from a Product.fulfillment_info.place_ids.  This process is asynchronous and does not require the Product to exist before updating fulfillment information. If the request is valid, the update will be enqueued and processed downstream. As a consequence, when a response is returned, the removed place IDs are not immediately manifested in the Product queried by ProductService.GetProduct or ProductService.ListProducts.  The returned Operations will be obsolete after 1 day, and GetOperation API will return NOT_FOUND afterwards.  If conflicting updates are issued, the Operations associated with the stale updates will not be marked as done until being obsolete. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * removeFulfillmentPlacesAsync(RemoveFulfillmentPlacesRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * removeFulfillmentPlacesAsync(ProductName product) 
  * removeFulfillmentPlacesAsync(String product) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * removeFulfillmentPlacesOperationCallable() 
  * removeFulfillmentPlacesCallable() 

  
AddLocalInventories |  Updates local inventory information for a Product at a list of places, while respecting the last update timestamps of each inventory field.  This process is asynchronous and does not require the Product to exist before updating inventory information. If the request is valid, the update will be enqueued and processed downstream. As a consequence, when a response is returned, updates are not immediately manifested in the Product queried by ProductService.GetProduct or ProductService.ListProducts.  Local inventory information can only be modified using this method. ProductService.CreateProduct and ProductService.UpdateProduct has no effect on local inventories.  The returned Operations will be obsolete after 1 day, and GetOperation API will return NOT_FOUND afterwards.  If conflicting updates are issued, the Operations associated with the stale updates will not be marked as done until being obsolete. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * addLocalInventoriesAsync(AddLocalInventoriesRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * addLocalInventoriesAsync(ProductName product) 
  * addLocalInventoriesAsync(String product) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * addLocalInventoriesOperationCallable() 
  * addLocalInventoriesCallable() 

  
RemoveLocalInventories |  Remove local inventory information for a Product at a list of places at a removal timestamp.  This process is asynchronous. If the request is valid, the removal will be enqueued and processed downstream. As a consequence, when a response is returned, removals are not immediately manifested in the Product queried by ProductService.GetProduct or ProductService.ListProducts.  Local inventory information can only be removed using this method. ProductService.CreateProduct and ProductService.UpdateProduct has no effect on local inventories.  The returned Operations will be obsolete after 1 day, and GetOperation API will return NOT_FOUND afterwards.  If conflicting updates are issued, the Operations associated with the stale updates will not be marked as done until being obsolete. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * removeLocalInventoriesAsync(RemoveLocalInventoriesRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * removeLocalInventoriesAsync(ProductName product) 
  * removeLocalInventoriesAsync(String product) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * removeLocalInventoriesOperationCallable() 
  * removeLocalInventoriesCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of ProductServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ProductServiceSettings productServiceSettings =
         ProductServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     ProductServiceClient productServiceClient = ProductServiceClient.create(productServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ProductServiceSettings productServiceSettings =
         ProductServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     ProductServiceClient productServiceClient = ProductServiceClient.create(productServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ProductServiceSettings productServiceSettings =
         ProductServiceSettings.newHttpJsonBuilder().build();
     ProductServiceClient productServiceClient = ProductServiceClient.create(productServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ProductServiceClient

## Static Methods 

### create()
    
    
    public static final ProductServiceClient create()

Constructs an instance of ProductServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[ProductServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ProductServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ProductServiceSettings settings)
    
    
    public static final ProductServiceClient create(ProductServiceSettings settings)

Constructs an instance of ProductServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ProductServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ProductServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ProductServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ProductServiceStub stub)
    
    
    public static final ProductServiceClient create(ProductServiceStub stub)

Constructs an instance of ProductServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(ProductServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ProductServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.stub.ProductServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ProductServiceClient)` |   
  
## Constructors 

### ProductServiceClient(ProductServiceSettings settings)
    
    
    protected ProductServiceClient(ProductServiceSettings settings)

Constructs an instance of ProductServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ProductServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ProductServiceSettings)`  
  
  
### ProductServiceClient(ProductServiceStub stub)
    
    
    protected ProductServiceClient(ProductServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ProductServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.stub.ProductServiceStub)`  
  
  
## Methods 

### addFulfillmentPlacesAsync(@Nullable ProductName product)
    
    
    public final OperationFuture<AddFulfillmentPlacesResponse,AddFulfillmentPlacesMetadata> addFulfillmentPlacesAsync(@Nullable ProductName product)

We recommend that you use the ProductService.AddLocalInventories method instead of the ProductService.AddFulfillmentPlaces method. ProductService.AddLocalInventories achieves the same results but provides more fine-grained control over ingesting local inventory data.

Incrementally adds place IDs to Product.fulfillment_info.place_ids.

This process is asynchronous and does not require the Product to exist before updating fulfillment information. If the request is valid, the update will be enqueued and processed downstream. As a consequence, when a response is returned, the added place IDs are not immediately manifested in the Product queried by ProductService.GetProduct or ProductService.ListProducts.

The returned Operations will be obsolete after 1 day, and GetOperation API will return NOT_FOUND afterwards.

If conflicting updates are issued, the Operations associated with the stale updates will not be marked as done until being obsolete.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductServiceClient productServiceClient = ProductServiceClient.create()) {
       ProductName product =
           ProductName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]", "[PRODUCT]");
       AddFulfillmentPlacesResponse response =
           productServiceClient.addFulfillmentPlacesAsync(product).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`product` | `@org.jspecify.annotations.Nullable com.google.cloud.retail.v2.ProductName`  
Required. Full resource name of Product, such as `projects/*/locations/global/catalogs/default_catalog/branches/default_branch/products/some_product_id`. If the caller does not have permission to access the Product, regardless of whether or not it exists, a PERMISSION_DENIED error is returned.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AddFulfillmentPlacesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.AddFulfillmentPlacesResponse),[AddFulfillmentPlacesMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.AddFulfillmentPlacesMetadata)>` |   
  
### addFulfillmentPlacesAsync(AddFulfillmentPlacesRequest request)
    
    
    public final OperationFuture<AddFulfillmentPlacesResponse,AddFulfillmentPlacesMetadata> addFulfillmentPlacesAsync(AddFulfillmentPlacesRequest request)

We recommend that you use the ProductService.AddLocalInventories method instead of the ProductService.AddFulfillmentPlaces method. ProductService.AddLocalInventories achieves the same results but provides more fine-grained control over ingesting local inventory data.

Incrementally adds place IDs to Product.fulfillment_info.place_ids.

This process is asynchronous and does not require the Product to exist before updating fulfillment information. If the request is valid, the update will be enqueued and processed downstream. As a consequence, when a response is returned, the added place IDs are not immediately manifested in the Product queried by ProductService.GetProduct or ProductService.ListProducts.

The returned Operations will be obsolete after 1 day, and GetOperation API will return NOT_FOUND afterwards.

If conflicting updates are issued, the Operations associated with the stale updates will not be marked as done until being obsolete.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductServiceClient productServiceClient = ProductServiceClient.create()) {
       AddFulfillmentPlacesRequest request =
           AddFulfillmentPlacesRequest.newBuilder()
               .setProduct(
                   ProductName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]", "[PRODUCT]")
                       .toString())
               .setType("type3575610")
               .addAllPlaceIds(new ArrayList<String>())
               .setAddTime(Timestamp.newBuilder().build())
               .setAllowMissing(true)
               .build();
       AddFulfillmentPlacesResponse response =
           productServiceClient.addFulfillmentPlacesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AddFulfillmentPlacesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.AddFulfillmentPlacesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AddFulfillmentPlacesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.AddFulfillmentPlacesResponse),[AddFulfillmentPlacesMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.AddFulfillmentPlacesMetadata)>` |   
  
### addFulfillmentPlacesAsync(String product)
    
    
    public final OperationFuture<AddFulfillmentPlacesResponse,AddFulfillmentPlacesMetadata> addFulfillmentPlacesAsync(String product)

We recommend that you use the ProductService.AddLocalInventories method instead of the ProductService.AddFulfillmentPlaces method. ProductService.AddLocalInventories achieves the same results but provides more fine-grained control over ingesting local inventory data.

Incrementally adds place IDs to Product.fulfillment_info.place_ids.

This process is asynchronous and does not require the Product to exist before updating fulfillment information. If the request is valid, the update will be enqueued and processed downstream. As a consequence, when a response is returned, the added place IDs are not immediately manifested in the Product queried by ProductService.GetProduct or ProductService.ListProducts.

The returned Operations will be obsolete after 1 day, and GetOperation API will return NOT_FOUND afterwards.

If conflicting updates are issued, the Operations associated with the stale updates will not be marked as done until being obsolete.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductServiceClient productServiceClient = ProductServiceClient.create()) {
       String product =
           ProductName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]", "[PRODUCT]")
               .toString();
       AddFulfillmentPlacesResponse response =
           productServiceClient.addFulfillmentPlacesAsync(product).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`product` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Full resource name of Product, such as `projects/*/locations/global/catalogs/default_catalog/branches/default_branch/products/some_product_id`. If the caller does not have permission to access the Product, regardless of whether or not it exists, a PERMISSION_DENIED error is returned.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AddFulfillmentPlacesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.AddFulfillmentPlacesResponse),[AddFulfillmentPlacesMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.AddFulfillmentPlacesMetadata)>` |   
  
### addFulfillmentPlacesCallable()
    
    
    public final UnaryCallable<AddFulfillmentPlacesRequest,Operation> addFulfillmentPlacesCallable()

We recommend that you use the ProductService.AddLocalInventories method instead of the ProductService.AddFulfillmentPlaces method. ProductService.AddLocalInventories achieves the same results but provides more fine-grained control over ingesting local inventory data.

Incrementally adds place IDs to Product.fulfillment_info.place_ids.

This process is asynchronous and does not require the Product to exist before updating fulfillment information. If the request is valid, the update will be enqueued and processed downstream. As a consequence, when a response is returned, the added place IDs are not immediately manifested in the Product queried by ProductService.GetProduct or ProductService.ListProducts.

The returned Operations will be obsolete after 1 day, and GetOperation API will return NOT_FOUND afterwards.

If conflicting updates are issued, the Operations associated with the stale updates will not be marked as done until being obsolete.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductServiceClient productServiceClient = ProductServiceClient.create()) {
       AddFulfillmentPlacesRequest request =
           AddFulfillmentPlacesRequest.newBuilder()
               .setProduct(
                   ProductName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]", "[PRODUCT]")
                       .toString())
               .setType("type3575610")
               .addAllPlaceIds(new ArrayList<String>())
               .setAddTime(Timestamp.newBuilder().build())
               .setAllowMissing(true)
               .build();
       ApiFuture<Operation> future =
           productServiceClient.addFulfillmentPlacesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AddFulfillmentPlacesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.AddFulfillmentPlacesRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### addFulfillmentPlacesOperationCallable()
    
    
    public final OperationCallable<AddFulfillmentPlacesRequest,AddFulfillmentPlacesResponse,AddFulfillmentPlacesMetadata> addFulfillmentPlacesOperationCallable()

We recommend that you use the ProductService.AddLocalInventories method instead of the ProductService.AddFulfillmentPlaces method. ProductService.AddLocalInventories achieves the same results but provides more fine-grained control over ingesting local inventory data.

Incrementally adds place IDs to Product.fulfillment_info.place_ids.

This process is asynchronous and does not require the Product to exist before updating fulfillment information. If the request is valid, the update will be enqueued and processed downstream. As a consequence, when a response is returned, the added place IDs are not immediately manifested in the Product queried by ProductService.GetProduct or ProductService.ListProducts.

The returned Operations will be obsolete after 1 day, and GetOperation API will return NOT_FOUND afterwards.

If conflicting updates are issued, the Operations associated with the stale updates will not be marked as done until being obsolete.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductServiceClient productServiceClient = ProductServiceClient.create()) {
       AddFulfillmentPlacesRequest request =
           AddFulfillmentPlacesRequest.newBuilder()
               .setProduct(
                   ProductName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]", "[PRODUCT]")
                       .toString())
               .setType("type3575610")
               .addAllPlaceIds(new ArrayList<String>())
               .setAddTime(Timestamp.newBuilder().build())
               .setAllowMissing(true)
               .build();
       OperationFuture<AddFulfillmentPlacesResponse, AddFulfillmentPlacesMetadata> future =
           productServiceClient.addFulfillmentPlacesOperationCallable().futureCall(request);
       // Do something.
       AddFulfillmentPlacesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[AddFulfillmentPlacesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.AddFulfillmentPlacesRequest),[AddFulfillmentPlacesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.AddFulfillmentPlacesResponse),[AddFulfillmentPlacesMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.AddFulfillmentPlacesMetadata)>` |   
  
### addLocalInventoriesAsync(@Nullable ProductName product)
    
    
    public final OperationFuture<AddLocalInventoriesResponse,AddLocalInventoriesMetadata> addLocalInventoriesAsync(@Nullable ProductName product)

Updates local inventory information for a Product at a list of places, while respecting the last update timestamps of each inventory field.

This process is asynchronous and does not require the Product to exist before updating inventory information. If the request is valid, the update will be enqueued and processed downstream. As a consequence, when a response is returned, updates are not immediately manifested in the Product queried by ProductService.GetProduct or ProductService.ListProducts.

Local inventory information can only be modified using this method. ProductService.CreateProduct and ProductService.UpdateProduct has no effect on local inventories.

The returned Operations will be obsolete after 1 day, and GetOperation API will return NOT_FOUND afterwards.

If conflicting updates are issued, the Operations associated with the stale updates will not be marked as done until being obsolete.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductServiceClient productServiceClient = ProductServiceClient.create()) {
       ProductName product =
           ProductName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]", "[PRODUCT]");
       AddLocalInventoriesResponse response =
           productServiceClient.addLocalInventoriesAsync(product).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`product` | `@org.jspecify.annotations.Nullable com.google.cloud.retail.v2.ProductName`  
Required. Full resource name of Product, such as `projects/*/locations/global/catalogs/default_catalog/branches/default_branch/products/some_product_id`. If the caller does not have permission to access the Product, regardless of whether or not it exists, a PERMISSION_DENIED error is returned.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AddLocalInventoriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.AddLocalInventoriesResponse),[AddLocalInventoriesMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.AddLocalInventoriesMetadata)>` |   
  
### addLocalInventoriesAsync(AddLocalInventoriesRequest request)
    
    
    public final OperationFuture<AddLocalInventoriesResponse,AddLocalInventoriesMetadata> addLocalInventoriesAsync(AddLocalInventoriesRequest request)

Updates local inventory information for a Product at a list of places, while respecting the last update timestamps of each inventory field.

This process is asynchronous and does not require the Product to exist before updating inventory information. If the request is valid, the update will be enqueued and processed downstream. As a consequence, when a response is returned, updates are not immediately manifested in the Product queried by ProductService.GetProduct or ProductService.ListProducts.

Local inventory information can only be modified using this method. ProductService.CreateProduct and ProductService.UpdateProduct has no effect on local inventories.

The returned Operations will be obsolete after 1 day, and GetOperation API will return NOT_FOUND afterwards.

If conflicting updates are issued, the Operations associated with the stale updates will not be marked as done until being obsolete.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductServiceClient productServiceClient = ProductServiceClient.create()) {
       AddLocalInventoriesRequest request =
           AddLocalInventoriesRequest.newBuilder()
               .setProduct(
                   ProductName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]", "[PRODUCT]")
                       .toString())
               .addAllLocalInventories(new ArrayList<LocalInventory>())
               .setAddMask(FieldMask.newBuilder().build())
               .setAddTime(Timestamp.newBuilder().build())
               .setAllowMissing(true)
               .build();
       AddLocalInventoriesResponse response =
           productServiceClient.addLocalInventoriesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AddLocalInventoriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.AddLocalInventoriesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AddLocalInventoriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.AddLocalInventoriesResponse),[AddLocalInventoriesMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.AddLocalInventoriesMetadata)>` |   
  
### addLocalInventoriesAsync(String product)
    
    
    public final OperationFuture<AddLocalInventoriesResponse,AddLocalInventoriesMetadata> addLocalInventoriesAsync(String product)

Updates local inventory information for a Product at a list of places, while respecting the last update timestamps of each inventory field.

This process is asynchronous and does not require the Product to exist before updating inventory information. If the request is valid, the update will be enqueued and processed downstream. As a consequence, when a response is returned, updates are not immediately manifested in the Product queried by ProductService.GetProduct or ProductService.ListProducts.

Local inventory information can only be modified using this method. ProductService.CreateProduct and ProductService.UpdateProduct has no effect on local inventories.

The returned Operations will be obsolete after 1 day, and GetOperation API will return NOT_FOUND afterwards.

If conflicting updates are issued, the Operations associated with the stale updates will not be marked as done until being obsolete.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductServiceClient productServiceClient = ProductServiceClient.create()) {
       String product =
           ProductName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]", "[PRODUCT]")
               .toString();
       AddLocalInventoriesResponse response =
           productServiceClient.addLocalInventoriesAsync(product).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`product` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Full resource name of Product, such as `projects/*/locations/global/catalogs/default_catalog/branches/default_branch/products/some_product_id`. If the caller does not have permission to access the Product, regardless of whether or not it exists, a PERMISSION_DENIED error is returned.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AddLocalInventoriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.AddLocalInventoriesResponse),[AddLocalInventoriesMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.AddLocalInventoriesMetadata)>` |   
  
### addLocalInventoriesCallable()
    
    
    public final UnaryCallable<AddLocalInventoriesRequest,Operation> addLocalInventoriesCallable()

Updates local inventory information for a Product at a list of places, while respecting the last update timestamps of each inventory field.

This process is asynchronous and does not require the Product to exist before updating inventory information. If the request is valid, the update will be enqueued and processed downstream. As a consequence, when a response is returned, updates are not immediately manifested in the Product queried by ProductService.GetProduct or ProductService.ListProducts.

Local inventory information can only be modified using this method. ProductService.CreateProduct and ProductService.UpdateProduct has no effect on local inventories.

The returned Operations will be obsolete after 1 day, and GetOperation API will return NOT_FOUND afterwards.

If conflicting updates are issued, the Operations associated with the stale updates will not be marked as done until being obsolete.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductServiceClient productServiceClient = ProductServiceClient.create()) {
       AddLocalInventoriesRequest request =
           AddLocalInventoriesRequest.newBuilder()
               .setProduct(
                   ProductName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]", "[PRODUCT]")
                       .toString())
               .addAllLocalInventories(new ArrayList<LocalInventory>())
               .setAddMask(FieldMask.newBuilder().build())
               .setAddTime(Timestamp.newBuilder().build())
               .setAllowMissing(true)
               .build();
       ApiFuture<Operation> future =
           productServiceClient.addLocalInventoriesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AddLocalInventoriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.AddLocalInventoriesRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### addLocalInventoriesOperationCallable()
    
    
    public final OperationCallable<AddLocalInventoriesRequest,AddLocalInventoriesResponse,AddLocalInventoriesMetadata> addLocalInventoriesOperationCallable()

Updates local inventory information for a Product at a list of places, while respecting the last update timestamps of each inventory field.

This process is asynchronous and does not require the Product to exist before updating inventory information. If the request is valid, the update will be enqueued and processed downstream. As a consequence, when a response is returned, updates are not immediately manifested in the Product queried by ProductService.GetProduct or ProductService.ListProducts.

Local inventory information can only be modified using this method. ProductService.CreateProduct and ProductService.UpdateProduct has no effect on local inventories.

The returned Operations will be obsolete after 1 day, and GetOperation API will return NOT_FOUND afterwards.

If conflicting updates are issued, the Operations associated with the stale updates will not be marked as done until being obsolete.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductServiceClient productServiceClient = ProductServiceClient.create()) {
       AddLocalInventoriesRequest request =
           AddLocalInventoriesRequest.newBuilder()
               .setProduct(
                   ProductName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]", "[PRODUCT]")
                       .toString())
               .addAllLocalInventories(new ArrayList<LocalInventory>())
               .setAddMask(FieldMask.newBuilder().build())
               .setAddTime(Timestamp.newBuilder().build())
               .setAllowMissing(true)
               .build();
       OperationFuture<AddLocalInventoriesResponse, AddLocalInventoriesMetadata> future =
           productServiceClient.addLocalInventoriesOperationCallable().futureCall(request);
       // Do something.
       AddLocalInventoriesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[AddLocalInventoriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.AddLocalInventoriesRequest),[AddLocalInventoriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.AddLocalInventoriesResponse),[AddLocalInventoriesMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.AddLocalInventoriesMetadata)>` |   
  
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

### createProduct(@Nullable BranchName parent, Product product, String productId)
    
    
    public final Product createProduct(@Nullable BranchName parent, Product product, String productId)

Creates a Product.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductServiceClient productServiceClient = ProductServiceClient.create()) {
       BranchName parent = BranchName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]");
       Product product = Product.newBuilder().build();
       String productId = "productId-1051830678";
       Product response = productServiceClient.createProduct(parent, product, productId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.retail.v2.BranchName`  
Required. The parent catalog resource name, such as `projects/*/locations/global/catalogs/default_catalog/branches/default_branch`.  
`product` | `[Product](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Product)`  
Required. The Product to create.  
`productId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the Product, which will become the final component of the Product.name. If the caller does not have permission to create the Product, regardless of whether or not it exists, a PERMISSION_DENIED error is returned. This field must be unique among all Products with the same parent. Otherwise, an ALREADY_EXISTS error is returned. This field must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an INVALID_ARGUMENT error is returned.  
**Returns**  
---  
**Type** | **Description**  
`[Product](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Product)` |   
  
### createProduct(CreateProductRequest request)
    
    
    public final Product createProduct(CreateProductRequest request)

Creates a Product.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductServiceClient productServiceClient = ProductServiceClient.create()) {
       CreateProductRequest request =
           CreateProductRequest.newBuilder()
               .setParent(
                   BranchName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]").toString())
               .setProduct(Product.newBuilder().build())
               .setProductId("productId-1051830678")
               .build();
       Product response = productServiceClient.createProduct(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateProductRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.CreateProductRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Product](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Product)` |   
  
### createProduct(String parent, Product product, String productId)
    
    
    public final Product createProduct(String parent, Product product, String productId)

Creates a Product.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductServiceClient productServiceClient = ProductServiceClient.create()) {
       String parent = BranchName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]").toString();
       Product product = Product.newBuilder().build();
       String productId = "productId-1051830678";
       Product response = productServiceClient.createProduct(parent, product, productId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent catalog resource name, such as `projects/*/locations/global/catalogs/default_catalog/branches/default_branch`.  
`product` | `[Product](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Product)`  
Required. The Product to create.  
`productId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the Product, which will become the final component of the Product.name. If the caller does not have permission to create the Product, regardless of whether or not it exists, a PERMISSION_DENIED error is returned. This field must be unique among all Products with the same parent. Otherwise, an ALREADY_EXISTS error is returned. This field must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an INVALID_ARGUMENT error is returned.  
**Returns**  
---  
**Type** | **Description**  
`[Product](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Product)` |   
  
### createProductCallable()
    
    
    public final UnaryCallable<CreateProductRequest,Product> createProductCallable()

Creates a Product.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductServiceClient productServiceClient = ProductServiceClient.create()) {
       CreateProductRequest request =
           CreateProductRequest.newBuilder()
               .setParent(
                   BranchName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]").toString())
               .setProduct(Product.newBuilder().build())
               .setProductId("productId-1051830678")
               .build();
       ApiFuture<Product> future = productServiceClient.createProductCallable().futureCall(request);
       // Do something.
       Product response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateProductRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.CreateProductRequest),[Product](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Product)>` |   
  
### deleteProduct(@Nullable ProductName name)
    
    
    public final void deleteProduct(@Nullable ProductName name)

Deletes a Product.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductServiceClient productServiceClient = ProductServiceClient.create()) {
       ProductName name =
           ProductName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]", "[PRODUCT]");
       productServiceClient.deleteProduct(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.retail.v2.ProductName`  
Required. Full resource name of Product, such as `projects/*/locations/global/catalogs/default_catalog/branches/default_branch/products/some_product_id`. If the caller does not have permission to delete the Product, regardless of whether or not it exists, a PERMISSION_DENIED error is returned. If the Product to delete does not exist, a NOT_FOUND error is returned. The Product to delete can neither be a Product.Type.COLLECTION Product member nor a Product.Type.PRIMARY Product with more than one variants. Otherwise, an INVALID_ARGUMENT error is returned. All inventory information for the named Product will be deleted.  
  
### deleteProduct(DeleteProductRequest request)
    
    
    public final void deleteProduct(DeleteProductRequest request)

Deletes a Product.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductServiceClient productServiceClient = ProductServiceClient.create()) {
       DeleteProductRequest request =
           DeleteProductRequest.newBuilder()
               .setName(
                   ProductName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]", "[PRODUCT]")
                       .toString())
               .build();
       productServiceClient.deleteProduct(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteProductRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.DeleteProductRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteProduct(String name)
    
    
    public final void deleteProduct(String name)

Deletes a Product.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductServiceClient productServiceClient = ProductServiceClient.create()) {
       String name =
           ProductName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]", "[PRODUCT]")
               .toString();
       productServiceClient.deleteProduct(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Full resource name of Product, such as `projects/*/locations/global/catalogs/default_catalog/branches/default_branch/products/some_product_id`. If the caller does not have permission to delete the Product, regardless of whether or not it exists, a PERMISSION_DENIED error is returned. If the Product to delete does not exist, a NOT_FOUND error is returned. The Product to delete can neither be a Product.Type.COLLECTION Product member nor a Product.Type.PRIMARY Product with more than one variants. Otherwise, an INVALID_ARGUMENT error is returned. All inventory information for the named Product will be deleted.  
  
### deleteProductCallable()
    
    
    public final UnaryCallable<DeleteProductRequest,Empty> deleteProductCallable()

Deletes a Product.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductServiceClient productServiceClient = ProductServiceClient.create()) {
       DeleteProductRequest request =
           DeleteProductRequest.newBuilder()
               .setName(
                   ProductName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]", "[PRODUCT]")
                       .toString())
               .build();
       ApiFuture<Empty> future = productServiceClient.deleteProductCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteProductRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.DeleteProductRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getHttpJsonOperationsClient()
    
    
    public final OperationsClient getHttpJsonOperationsClient()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.OperationsClient.html)` |   
  
### getOperationsClient()
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getProduct(@Nullable ProductName name)
    
    
    public final Product getProduct(@Nullable ProductName name)

Gets a Product.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductServiceClient productServiceClient = ProductServiceClient.create()) {
       ProductName name =
           ProductName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]", "[PRODUCT]");
       Product response = productServiceClient.getProduct(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.retail.v2.ProductName`  
Required. Full resource name of Product, such as `projects/*/locations/global/catalogs/default_catalog/branches/default_branch/products/some_product_id`. If the caller does not have permission to access the Product, regardless of whether or not it exists, a PERMISSION_DENIED error is returned. If the requested Product does not exist, a NOT_FOUND error is returned.  
**Returns**  
---  
**Type** | **Description**  
`[Product](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Product)` |   
  
### getProduct(GetProductRequest request)
    
    
    public final Product getProduct(GetProductRequest request)

Gets a Product.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductServiceClient productServiceClient = ProductServiceClient.create()) {
       GetProductRequest request =
           GetProductRequest.newBuilder()
               .setName(
                   ProductName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]", "[PRODUCT]")
                       .toString())
               .build();
       Product response = productServiceClient.getProduct(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetProductRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.GetProductRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Product](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Product)` |   
  
### getProduct(String name)
    
    
    public final Product getProduct(String name)

Gets a Product.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductServiceClient productServiceClient = ProductServiceClient.create()) {
       String name =
           ProductName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]", "[PRODUCT]")
               .toString();
       Product response = productServiceClient.getProduct(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Full resource name of Product, such as `projects/*/locations/global/catalogs/default_catalog/branches/default_branch/products/some_product_id`. If the caller does not have permission to access the Product, regardless of whether or not it exists, a PERMISSION_DENIED error is returned. If the requested Product does not exist, a NOT_FOUND error is returned.  
**Returns**  
---  
**Type** | **Description**  
`[Product](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Product)` |   
  
### getProductCallable()
    
    
    public final UnaryCallable<GetProductRequest,Product> getProductCallable()

Gets a Product.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductServiceClient productServiceClient = ProductServiceClient.create()) {
       GetProductRequest request =
           GetProductRequest.newBuilder()
               .setName(
                   ProductName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]", "[PRODUCT]")
                       .toString())
               .build();
       ApiFuture<Product> future = productServiceClient.getProductCallable().futureCall(request);
       // Do something.
       Product response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetProductRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.GetProductRequest),[Product](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Product)>` |   
  
### getSettings()
    
    
    public final @Nullable ProductServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.retail.v2.ProductServiceSettings` |   
  
### getStub()
    
    
    public ProductServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[ProductServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.stub.ProductServiceStub)` |   
  
### importProductsAsync(ImportProductsRequest request)
    
    
    public final OperationFuture<ImportProductsResponse,ImportMetadata> importProductsAsync(ImportProductsRequest request)

Bulk import of multiple Products.

Request processing may be synchronous. Non-existing items are created.

Note that it is possible for a subset of the Products to be successfully updated.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductServiceClient productServiceClient = ProductServiceClient.create()) {
       ImportProductsRequest request =
           ImportProductsRequest.newBuilder()
               .setParent(
                   BranchName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]").toString())
               .setRequestId("requestId693933066")
               .setInputConfig(ProductInputConfig.newBuilder().build())
               .setErrorsConfig(ImportErrorsConfig.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setNotificationPubsubTopic("notificationPubsubTopic-1361224991")
               .build();
       ImportProductsResponse response = productServiceClient.importProductsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ImportProductsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ImportProductsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ImportProductsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ImportProductsResponse),[ImportMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ImportMetadata)>` |   
  
### importProductsCallable()
    
    
    public final UnaryCallable<ImportProductsRequest,Operation> importProductsCallable()

Bulk import of multiple Products.

Request processing may be synchronous. Non-existing items are created.

Note that it is possible for a subset of the Products to be successfully updated.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductServiceClient productServiceClient = ProductServiceClient.create()) {
       ImportProductsRequest request =
           ImportProductsRequest.newBuilder()
               .setParent(
                   BranchName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]").toString())
               .setRequestId("requestId693933066")
               .setInputConfig(ProductInputConfig.newBuilder().build())
               .setErrorsConfig(ImportErrorsConfig.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setNotificationPubsubTopic("notificationPubsubTopic-1361224991")
               .build();
       ApiFuture<Operation> future =
           productServiceClient.importProductsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ImportProductsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ImportProductsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### importProductsOperationCallable()
    
    
    public final OperationCallable<ImportProductsRequest,ImportProductsResponse,ImportMetadata> importProductsOperationCallable()

Bulk import of multiple Products.

Request processing may be synchronous. Non-existing items are created.

Note that it is possible for a subset of the Products to be successfully updated.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductServiceClient productServiceClient = ProductServiceClient.create()) {
       ImportProductsRequest request =
           ImportProductsRequest.newBuilder()
               .setParent(
                   BranchName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]").toString())
               .setRequestId("requestId693933066")
               .setInputConfig(ProductInputConfig.newBuilder().build())
               .setErrorsConfig(ImportErrorsConfig.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setNotificationPubsubTopic("notificationPubsubTopic-1361224991")
               .build();
       OperationFuture<ImportProductsResponse, ImportMetadata> future =
           productServiceClient.importProductsOperationCallable().futureCall(request);
       // Do something.
       ImportProductsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ImportProductsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ImportProductsRequest),[ImportProductsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ImportProductsResponse),[ImportMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ImportMetadata)>` |   
  
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
  
### listProducts(@Nullable BranchName parent)
    
    
    public final ProductServiceClient.ListProductsPagedResponse listProducts(@Nullable BranchName parent)

Gets a list of Products.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductServiceClient productServiceClient = ProductServiceClient.create()) {
       BranchName parent = BranchName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]");
       for (Product element : productServiceClient.listProducts(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.retail.v2.BranchName`  
Required. The parent branch resource name, such as `projects/*/locations/global/catalogs/default_catalog/branches/0`. Use `default_branch` as the branch ID, to list products under the default branch. If the caller does not have permission to list Products under this branch, regardless of whether or not this branch exists, a PERMISSION_DENIED error is returned.  
**Returns**  
---  
**Type** | **Description**  
`[ProductServiceClient.ListProductsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ProductServiceClient.ListProductsPagedResponse)` |   
  
### listProducts(ListProductsRequest request)
    
    
    public final ProductServiceClient.ListProductsPagedResponse listProducts(ListProductsRequest request)

Gets a list of Products.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductServiceClient productServiceClient = ProductServiceClient.create()) {
       ListProductsRequest request =
           ListProductsRequest.newBuilder()
               .setParent(
                   BranchName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       for (Product element : productServiceClient.listProducts(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListProductsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ListProductsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ProductServiceClient.ListProductsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ProductServiceClient.ListProductsPagedResponse)` |   
  
### listProducts(String parent)
    
    
    public final ProductServiceClient.ListProductsPagedResponse listProducts(String parent)

Gets a list of Products.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductServiceClient productServiceClient = ProductServiceClient.create()) {
       String parent = BranchName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]").toString();
       for (Product element : productServiceClient.listProducts(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent branch resource name, such as `projects/*/locations/global/catalogs/default_catalog/branches/0`. Use `default_branch` as the branch ID, to list products under the default branch. If the caller does not have permission to list Products under this branch, regardless of whether or not this branch exists, a PERMISSION_DENIED error is returned.  
**Returns**  
---  
**Type** | **Description**  
`[ProductServiceClient.ListProductsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ProductServiceClient.ListProductsPagedResponse)` |   
  
### listProductsCallable()
    
    
    public final UnaryCallable<ListProductsRequest,ListProductsResponse> listProductsCallable()

Gets a list of Products.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductServiceClient productServiceClient = ProductServiceClient.create()) {
       ListProductsRequest request =
           ListProductsRequest.newBuilder()
               .setParent(
                   BranchName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       while (true) {
         ListProductsResponse response = productServiceClient.listProductsCallable().call(request);
         for (Product element : response.getProductsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListProductsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ListProductsRequest),[ListProductsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ListProductsResponse)>` |   
  
### listProductsPagedCallable()
    
    
    public final UnaryCallable<ListProductsRequest,ProductServiceClient.ListProductsPagedResponse> listProductsPagedCallable()

Gets a list of Products.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductServiceClient productServiceClient = ProductServiceClient.create()) {
       ListProductsRequest request =
           ListProductsRequest.newBuilder()
               .setParent(
                   BranchName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Product> future =
           productServiceClient.listProductsPagedCallable().futureCall(request);
       // Do something.
       for (Product element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListProductsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ListProductsRequest),[ListProductsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ProductServiceClient.ListProductsPagedResponse)>` |   
  
### purgeProductsAsync(PurgeProductsRequest request)
    
    
    public final OperationFuture<PurgeProductsResponse,PurgeProductsMetadata> purgeProductsAsync(PurgeProductsRequest request)

Permanently deletes all selected Products under a branch.

This process is asynchronous. If the request is valid, the removal will be enqueued and processed offline. Depending on the number of Products, this operation could take hours to complete. Before the operation completes, some Products may still be returned by ProductService.GetProduct or ProductService.ListProducts.

Depending on the number of Products, this operation could take hours to complete. To get a sample of Products that would be deleted, set PurgeProductsRequest.force to false.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductServiceClient productServiceClient = ProductServiceClient.create()) {
       PurgeProductsRequest request =
           PurgeProductsRequest.newBuilder()
               .setParent(
                   BranchName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]").toString())
               .setFilter("filter-1274492040")
               .setForce(true)
               .build();
       PurgeProductsResponse response = productServiceClient.purgeProductsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PurgeProductsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.PurgeProductsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PurgeProductsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.PurgeProductsResponse),[PurgeProductsMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.PurgeProductsMetadata)>` |   
  
### purgeProductsCallable()
    
    
    public final UnaryCallable<PurgeProductsRequest,Operation> purgeProductsCallable()

Permanently deletes all selected Products under a branch.

This process is asynchronous. If the request is valid, the removal will be enqueued and processed offline. Depending on the number of Products, this operation could take hours to complete. Before the operation completes, some Products may still be returned by ProductService.GetProduct or ProductService.ListProducts.

Depending on the number of Products, this operation could take hours to complete. To get a sample of Products that would be deleted, set PurgeProductsRequest.force to false.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductServiceClient productServiceClient = ProductServiceClient.create()) {
       PurgeProductsRequest request =
           PurgeProductsRequest.newBuilder()
               .setParent(
                   BranchName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]").toString())
               .setFilter("filter-1274492040")
               .setForce(true)
               .build();
       ApiFuture<Operation> future =
           productServiceClient.purgeProductsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PurgeProductsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.PurgeProductsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### purgeProductsOperationCallable()
    
    
    public final OperationCallable<PurgeProductsRequest,PurgeProductsResponse,PurgeProductsMetadata> purgeProductsOperationCallable()

Permanently deletes all selected Products under a branch.

This process is asynchronous. If the request is valid, the removal will be enqueued and processed offline. Depending on the number of Products, this operation could take hours to complete. Before the operation completes, some Products may still be returned by ProductService.GetProduct or ProductService.ListProducts.

Depending on the number of Products, this operation could take hours to complete. To get a sample of Products that would be deleted, set PurgeProductsRequest.force to false.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductServiceClient productServiceClient = ProductServiceClient.create()) {
       PurgeProductsRequest request =
           PurgeProductsRequest.newBuilder()
               .setParent(
                   BranchName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]").toString())
               .setFilter("filter-1274492040")
               .setForce(true)
               .build();
       OperationFuture<PurgeProductsResponse, PurgeProductsMetadata> future =
           productServiceClient.purgeProductsOperationCallable().futureCall(request);
       // Do something.
       PurgeProductsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PurgeProductsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.PurgeProductsRequest),[PurgeProductsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.PurgeProductsResponse),[PurgeProductsMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.PurgeProductsMetadata)>` |   
  
### removeFulfillmentPlacesAsync(@Nullable ProductName product)
    
    
    public final OperationFuture<RemoveFulfillmentPlacesResponse,RemoveFulfillmentPlacesMetadata> removeFulfillmentPlacesAsync(@Nullable ProductName product)

We recommend that you use the ProductService.RemoveLocalInventories method instead of the ProductService.RemoveFulfillmentPlaces method. ProductService.RemoveLocalInventories achieves the same results but provides more fine-grained control over ingesting local inventory data.

Incrementally removes place IDs from a Product.fulfillment_info.place_ids.

This process is asynchronous and does not require the Product to exist before updating fulfillment information. If the request is valid, the update will be enqueued and processed downstream. As a consequence, when a response is returned, the removed place IDs are not immediately manifested in the Product queried by ProductService.GetProduct or ProductService.ListProducts.

The returned Operations will be obsolete after 1 day, and GetOperation API will return NOT_FOUND afterwards.

If conflicting updates are issued, the Operations associated with the stale updates will not be marked as done until being obsolete.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductServiceClient productServiceClient = ProductServiceClient.create()) {
       ProductName product =
           ProductName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]", "[PRODUCT]");
       RemoveFulfillmentPlacesResponse response =
           productServiceClient.removeFulfillmentPlacesAsync(product).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`product` | `@org.jspecify.annotations.Nullable com.google.cloud.retail.v2.ProductName`  
Required. Full resource name of Product, such as `projects/*/locations/global/catalogs/default_catalog/branches/default_branch/products/some_product_id`. If the caller does not have permission to access the Product, regardless of whether or not it exists, a PERMISSION_DENIED error is returned.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[RemoveFulfillmentPlacesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.RemoveFulfillmentPlacesResponse),[RemoveFulfillmentPlacesMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.RemoveFulfillmentPlacesMetadata)>` |   
  
### removeFulfillmentPlacesAsync(RemoveFulfillmentPlacesRequest request)
    
    
    public final OperationFuture<RemoveFulfillmentPlacesResponse,RemoveFulfillmentPlacesMetadata> removeFulfillmentPlacesAsync(RemoveFulfillmentPlacesRequest request)

We recommend that you use the ProductService.RemoveLocalInventories method instead of the ProductService.RemoveFulfillmentPlaces method. ProductService.RemoveLocalInventories achieves the same results but provides more fine-grained control over ingesting local inventory data.

Incrementally removes place IDs from a Product.fulfillment_info.place_ids.

This process is asynchronous and does not require the Product to exist before updating fulfillment information. If the request is valid, the update will be enqueued and processed downstream. As a consequence, when a response is returned, the removed place IDs are not immediately manifested in the Product queried by ProductService.GetProduct or ProductService.ListProducts.

The returned Operations will be obsolete after 1 day, and GetOperation API will return NOT_FOUND afterwards.

If conflicting updates are issued, the Operations associated with the stale updates will not be marked as done until being obsolete.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductServiceClient productServiceClient = ProductServiceClient.create()) {
       RemoveFulfillmentPlacesRequest request =
           RemoveFulfillmentPlacesRequest.newBuilder()
               .setProduct(
                   ProductName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]", "[PRODUCT]")
                       .toString())
               .setType("type3575610")
               .addAllPlaceIds(new ArrayList<String>())
               .setRemoveTime(Timestamp.newBuilder().build())
               .setAllowMissing(true)
               .build();
       RemoveFulfillmentPlacesResponse response =
           productServiceClient.removeFulfillmentPlacesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RemoveFulfillmentPlacesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.RemoveFulfillmentPlacesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[RemoveFulfillmentPlacesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.RemoveFulfillmentPlacesResponse),[RemoveFulfillmentPlacesMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.RemoveFulfillmentPlacesMetadata)>` |   
  
### removeFulfillmentPlacesAsync(String product)
    
    
    public final OperationFuture<RemoveFulfillmentPlacesResponse,RemoveFulfillmentPlacesMetadata> removeFulfillmentPlacesAsync(String product)

We recommend that you use the ProductService.RemoveLocalInventories method instead of the ProductService.RemoveFulfillmentPlaces method. ProductService.RemoveLocalInventories achieves the same results but provides more fine-grained control over ingesting local inventory data.

Incrementally removes place IDs from a Product.fulfillment_info.place_ids.

This process is asynchronous and does not require the Product to exist before updating fulfillment information. If the request is valid, the update will be enqueued and processed downstream. As a consequence, when a response is returned, the removed place IDs are not immediately manifested in the Product queried by ProductService.GetProduct or ProductService.ListProducts.

The returned Operations will be obsolete after 1 day, and GetOperation API will return NOT_FOUND afterwards.

If conflicting updates are issued, the Operations associated with the stale updates will not be marked as done until being obsolete.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductServiceClient productServiceClient = ProductServiceClient.create()) {
       String product =
           ProductName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]", "[PRODUCT]")
               .toString();
       RemoveFulfillmentPlacesResponse response =
           productServiceClient.removeFulfillmentPlacesAsync(product).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`product` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Full resource name of Product, such as `projects/*/locations/global/catalogs/default_catalog/branches/default_branch/products/some_product_id`. If the caller does not have permission to access the Product, regardless of whether or not it exists, a PERMISSION_DENIED error is returned.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[RemoveFulfillmentPlacesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.RemoveFulfillmentPlacesResponse),[RemoveFulfillmentPlacesMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.RemoveFulfillmentPlacesMetadata)>` |   
  
### removeFulfillmentPlacesCallable()
    
    
    public final UnaryCallable<RemoveFulfillmentPlacesRequest,Operation> removeFulfillmentPlacesCallable()

We recommend that you use the ProductService.RemoveLocalInventories method instead of the ProductService.RemoveFulfillmentPlaces method. ProductService.RemoveLocalInventories achieves the same results but provides more fine-grained control over ingesting local inventory data.

Incrementally removes place IDs from a Product.fulfillment_info.place_ids.

This process is asynchronous and does not require the Product to exist before updating fulfillment information. If the request is valid, the update will be enqueued and processed downstream. As a consequence, when a response is returned, the removed place IDs are not immediately manifested in the Product queried by ProductService.GetProduct or ProductService.ListProducts.

The returned Operations will be obsolete after 1 day, and GetOperation API will return NOT_FOUND afterwards.

If conflicting updates are issued, the Operations associated with the stale updates will not be marked as done until being obsolete.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductServiceClient productServiceClient = ProductServiceClient.create()) {
       RemoveFulfillmentPlacesRequest request =
           RemoveFulfillmentPlacesRequest.newBuilder()
               .setProduct(
                   ProductName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]", "[PRODUCT]")
                       .toString())
               .setType("type3575610")
               .addAllPlaceIds(new ArrayList<String>())
               .setRemoveTime(Timestamp.newBuilder().build())
               .setAllowMissing(true)
               .build();
       ApiFuture<Operation> future =
           productServiceClient.removeFulfillmentPlacesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RemoveFulfillmentPlacesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.RemoveFulfillmentPlacesRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### removeFulfillmentPlacesOperationCallable()
    
    
    public final OperationCallable<RemoveFulfillmentPlacesRequest,RemoveFulfillmentPlacesResponse,RemoveFulfillmentPlacesMetadata> removeFulfillmentPlacesOperationCallable()

We recommend that you use the ProductService.RemoveLocalInventories method instead of the ProductService.RemoveFulfillmentPlaces method. ProductService.RemoveLocalInventories achieves the same results but provides more fine-grained control over ingesting local inventory data.

Incrementally removes place IDs from a Product.fulfillment_info.place_ids.

This process is asynchronous and does not require the Product to exist before updating fulfillment information. If the request is valid, the update will be enqueued and processed downstream. As a consequence, when a response is returned, the removed place IDs are not immediately manifested in the Product queried by ProductService.GetProduct or ProductService.ListProducts.

The returned Operations will be obsolete after 1 day, and GetOperation API will return NOT_FOUND afterwards.

If conflicting updates are issued, the Operations associated with the stale updates will not be marked as done until being obsolete.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductServiceClient productServiceClient = ProductServiceClient.create()) {
       RemoveFulfillmentPlacesRequest request =
           RemoveFulfillmentPlacesRequest.newBuilder()
               .setProduct(
                   ProductName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]", "[PRODUCT]")
                       .toString())
               .setType("type3575610")
               .addAllPlaceIds(new ArrayList<String>())
               .setRemoveTime(Timestamp.newBuilder().build())
               .setAllowMissing(true)
               .build();
       OperationFuture<RemoveFulfillmentPlacesResponse, RemoveFulfillmentPlacesMetadata> future =
           productServiceClient.removeFulfillmentPlacesOperationCallable().futureCall(request);
       // Do something.
       RemoveFulfillmentPlacesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RemoveFulfillmentPlacesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.RemoveFulfillmentPlacesRequest),[RemoveFulfillmentPlacesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.RemoveFulfillmentPlacesResponse),[RemoveFulfillmentPlacesMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.RemoveFulfillmentPlacesMetadata)>` |   
  
### removeLocalInventoriesAsync(@Nullable ProductName product)
    
    
    public final OperationFuture<RemoveLocalInventoriesResponse,RemoveLocalInventoriesMetadata> removeLocalInventoriesAsync(@Nullable ProductName product)

Remove local inventory information for a Product at a list of places at a removal timestamp.

This process is asynchronous. If the request is valid, the removal will be enqueued and processed downstream. As a consequence, when a response is returned, removals are not immediately manifested in the Product queried by ProductService.GetProduct or ProductService.ListProducts.

Local inventory information can only be removed using this method. ProductService.CreateProduct and ProductService.UpdateProduct has no effect on local inventories.

The returned Operations will be obsolete after 1 day, and GetOperation API will return NOT_FOUND afterwards.

If conflicting updates are issued, the Operations associated with the stale updates will not be marked as done until being obsolete.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductServiceClient productServiceClient = ProductServiceClient.create()) {
       ProductName product =
           ProductName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]", "[PRODUCT]");
       RemoveLocalInventoriesResponse response =
           productServiceClient.removeLocalInventoriesAsync(product).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`product` | `@org.jspecify.annotations.Nullable com.google.cloud.retail.v2.ProductName`  
Required. Full resource name of Product, such as `projects/*/locations/global/catalogs/default_catalog/branches/default_branch/products/some_product_id`. If the caller does not have permission to access the Product, regardless of whether or not it exists, a PERMISSION_DENIED error is returned.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[RemoveLocalInventoriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.RemoveLocalInventoriesResponse),[RemoveLocalInventoriesMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.RemoveLocalInventoriesMetadata)>` |   
  
### removeLocalInventoriesAsync(RemoveLocalInventoriesRequest request)
    
    
    public final OperationFuture<RemoveLocalInventoriesResponse,RemoveLocalInventoriesMetadata> removeLocalInventoriesAsync(RemoveLocalInventoriesRequest request)

Remove local inventory information for a Product at a list of places at a removal timestamp.

This process is asynchronous. If the request is valid, the removal will be enqueued and processed downstream. As a consequence, when a response is returned, removals are not immediately manifested in the Product queried by ProductService.GetProduct or ProductService.ListProducts.

Local inventory information can only be removed using this method. ProductService.CreateProduct and ProductService.UpdateProduct has no effect on local inventories.

The returned Operations will be obsolete after 1 day, and GetOperation API will return NOT_FOUND afterwards.

If conflicting updates are issued, the Operations associated with the stale updates will not be marked as done until being obsolete.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductServiceClient productServiceClient = ProductServiceClient.create()) {
       RemoveLocalInventoriesRequest request =
           RemoveLocalInventoriesRequest.newBuilder()
               .setProduct(
                   ProductName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]", "[PRODUCT]")
                       .toString())
               .addAllPlaceIds(new ArrayList<String>())
               .setRemoveTime(Timestamp.newBuilder().build())
               .setAllowMissing(true)
               .build();
       RemoveLocalInventoriesResponse response =
           productServiceClient.removeLocalInventoriesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RemoveLocalInventoriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.RemoveLocalInventoriesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[RemoveLocalInventoriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.RemoveLocalInventoriesResponse),[RemoveLocalInventoriesMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.RemoveLocalInventoriesMetadata)>` |   
  
### removeLocalInventoriesAsync(String product)
    
    
    public final OperationFuture<RemoveLocalInventoriesResponse,RemoveLocalInventoriesMetadata> removeLocalInventoriesAsync(String product)

Remove local inventory information for a Product at a list of places at a removal timestamp.

This process is asynchronous. If the request is valid, the removal will be enqueued and processed downstream. As a consequence, when a response is returned, removals are not immediately manifested in the Product queried by ProductService.GetProduct or ProductService.ListProducts.

Local inventory information can only be removed using this method. ProductService.CreateProduct and ProductService.UpdateProduct has no effect on local inventories.

The returned Operations will be obsolete after 1 day, and GetOperation API will return NOT_FOUND afterwards.

If conflicting updates are issued, the Operations associated with the stale updates will not be marked as done until being obsolete.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductServiceClient productServiceClient = ProductServiceClient.create()) {
       String product =
           ProductName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]", "[PRODUCT]")
               .toString();
       RemoveLocalInventoriesResponse response =
           productServiceClient.removeLocalInventoriesAsync(product).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`product` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Full resource name of Product, such as `projects/*/locations/global/catalogs/default_catalog/branches/default_branch/products/some_product_id`. If the caller does not have permission to access the Product, regardless of whether or not it exists, a PERMISSION_DENIED error is returned.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[RemoveLocalInventoriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.RemoveLocalInventoriesResponse),[RemoveLocalInventoriesMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.RemoveLocalInventoriesMetadata)>` |   
  
### removeLocalInventoriesCallable()
    
    
    public final UnaryCallable<RemoveLocalInventoriesRequest,Operation> removeLocalInventoriesCallable()

Remove local inventory information for a Product at a list of places at a removal timestamp.

This process is asynchronous. If the request is valid, the removal will be enqueued and processed downstream. As a consequence, when a response is returned, removals are not immediately manifested in the Product queried by ProductService.GetProduct or ProductService.ListProducts.

Local inventory information can only be removed using this method. ProductService.CreateProduct and ProductService.UpdateProduct has no effect on local inventories.

The returned Operations will be obsolete after 1 day, and GetOperation API will return NOT_FOUND afterwards.

If conflicting updates are issued, the Operations associated with the stale updates will not be marked as done until being obsolete.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductServiceClient productServiceClient = ProductServiceClient.create()) {
       RemoveLocalInventoriesRequest request =
           RemoveLocalInventoriesRequest.newBuilder()
               .setProduct(
                   ProductName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]", "[PRODUCT]")
                       .toString())
               .addAllPlaceIds(new ArrayList<String>())
               .setRemoveTime(Timestamp.newBuilder().build())
               .setAllowMissing(true)
               .build();
       ApiFuture<Operation> future =
           productServiceClient.removeLocalInventoriesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RemoveLocalInventoriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.RemoveLocalInventoriesRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### removeLocalInventoriesOperationCallable()
    
    
    public final OperationCallable<RemoveLocalInventoriesRequest,RemoveLocalInventoriesResponse,RemoveLocalInventoriesMetadata> removeLocalInventoriesOperationCallable()

Remove local inventory information for a Product at a list of places at a removal timestamp.

This process is asynchronous. If the request is valid, the removal will be enqueued and processed downstream. As a consequence, when a response is returned, removals are not immediately manifested in the Product queried by ProductService.GetProduct or ProductService.ListProducts.

Local inventory information can only be removed using this method. ProductService.CreateProduct and ProductService.UpdateProduct has no effect on local inventories.

The returned Operations will be obsolete after 1 day, and GetOperation API will return NOT_FOUND afterwards.

If conflicting updates are issued, the Operations associated with the stale updates will not be marked as done until being obsolete.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductServiceClient productServiceClient = ProductServiceClient.create()) {
       RemoveLocalInventoriesRequest request =
           RemoveLocalInventoriesRequest.newBuilder()
               .setProduct(
                   ProductName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]", "[PRODUCT]")
                       .toString())
               .addAllPlaceIds(new ArrayList<String>())
               .setRemoveTime(Timestamp.newBuilder().build())
               .setAllowMissing(true)
               .build();
       OperationFuture<RemoveLocalInventoriesResponse, RemoveLocalInventoriesMetadata> future =
           productServiceClient.removeLocalInventoriesOperationCallable().futureCall(request);
       // Do something.
       RemoveLocalInventoriesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RemoveLocalInventoriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.RemoveLocalInventoriesRequest),[RemoveLocalInventoriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.RemoveLocalInventoriesResponse),[RemoveLocalInventoriesMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.RemoveLocalInventoriesMetadata)>` |   
  
### setInventoryAsync(Product inventory, FieldMask setMask)
    
    
    public final OperationFuture<SetInventoryResponse,SetInventoryMetadata> setInventoryAsync(Product inventory, FieldMask setMask)

Updates inventory information for a Product while respecting the last update timestamps of each inventory field.

This process is asynchronous and does not require the Product to exist before updating fulfillment information. If the request is valid, the update is enqueued and processed downstream. As a consequence, when a response is returned, updates are not immediately manifested in the Product queried by ProductService.GetProduct or ProductService.ListProducts.

When inventory is updated with ProductService.CreateProduct and ProductService.UpdateProduct, the specified inventory field value(s) overwrite any existing value(s) while ignoring the last update time for this field. Furthermore, the last update times for the specified inventory fields are overwritten by the times of the ProductService.CreateProduct or ProductService.UpdateProduct request.

If no inventory fields are set in CreateProductRequest.product, then any pre-existing inventory information for this product is used.

If no inventory fields are set in SetInventoryRequest.set_mask, then any existing inventory information is preserved.

Pre-existing inventory information can only be updated with ProductService.SetInventory, ProductService.AddFulfillmentPlaces, and ProductService.RemoveFulfillmentPlaces.

The returned Operations is obsolete after one day, and the GetOperation API returns `NOT_FOUND` afterwards.

If conflicting updates are issued, the Operations associated with the stale updates are not marked as done until they are obsolete.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductServiceClient productServiceClient = ProductServiceClient.create()) {
       Product inventory = Product.newBuilder().build();
       FieldMask setMask = FieldMask.newBuilder().build();
       SetInventoryResponse response =
           productServiceClient.setInventoryAsync(inventory, setMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`inventory` | `[Product](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Product)`  
Required. The inventory information to update. The allowable fields to update are: 

  * Product.price_info
  * Product.availability
  * Product.available_quantity
  * Product.fulfillment_info The updated inventory fields must be specified in SetInventoryRequest.set_mask. 

If SetInventoryRequest.inventory.name is empty or invalid, an INVALID_ARGUMENT error is returned. If the caller does not have permission to update the Product named in Product.name, regardless of whether or not it exists, a PERMISSION_DENIED error is returned. If the Product to update does not have existing inventory information, the provided inventory information will be inserted. If the Product to update has existing inventory information, the provided inventory information will be merged while respecting the last update time for each inventory field, using the provided or default value for SetInventoryRequest.set_time. The caller can replace place IDs for a subset of fulfillment types in the following ways: 

  * Adds "fulfillment_info" in SetInventoryRequest.set_mask
  * Specifies only the desired fulfillment types and corresponding place IDs to update in SetInventoryRequest.inventory.fulfillment_info

The caller can clear all place IDs from a subset of fulfillment types in the following ways: 

  * Adds "fulfillment_info" in SetInventoryRequest.set_mask
  * Specifies only the desired fulfillment types to clear in SetInventoryRequest.inventory.fulfillment_info
  * Checks that only the desired fulfillment info types have empty SetInventoryRequest.inventory.fulfillment_info.place_ids

The last update time is recorded for the following inventory fields: 

  * Product.price_info
  * Product.availability
  * Product.available_quantity
  * Product.fulfillment_info

If a full overwrite of inventory information while ignoring timestamps is needed, ProductService.UpdateProduct should be invoked instead.  
`setMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Indicates which inventory fields in the provided Product to update. At least one field must be provided. If an unsupported or unknown field is provided, an INVALID_ARGUMENT error is returned and the entire update will be ignored.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[SetInventoryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SetInventoryResponse),[SetInventoryMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SetInventoryMetadata)>` |   
  
### setInventoryAsync(SetInventoryRequest request)
    
    
    public final OperationFuture<SetInventoryResponse,SetInventoryMetadata> setInventoryAsync(SetInventoryRequest request)

Updates inventory information for a Product while respecting the last update timestamps of each inventory field.

This process is asynchronous and does not require the Product to exist before updating fulfillment information. If the request is valid, the update is enqueued and processed downstream. As a consequence, when a response is returned, updates are not immediately manifested in the Product queried by ProductService.GetProduct or ProductService.ListProducts.

When inventory is updated with ProductService.CreateProduct and ProductService.UpdateProduct, the specified inventory field value(s) overwrite any existing value(s) while ignoring the last update time for this field. Furthermore, the last update times for the specified inventory fields are overwritten by the times of the ProductService.CreateProduct or ProductService.UpdateProduct request.

If no inventory fields are set in CreateProductRequest.product, then any pre-existing inventory information for this product is used.

If no inventory fields are set in SetInventoryRequest.set_mask, then any existing inventory information is preserved.

Pre-existing inventory information can only be updated with ProductService.SetInventory, ProductService.AddFulfillmentPlaces, and ProductService.RemoveFulfillmentPlaces.

The returned Operations is obsolete after one day, and the GetOperation API returns `NOT_FOUND` afterwards.

If conflicting updates are issued, the Operations associated with the stale updates are not marked as done until they are obsolete.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductServiceClient productServiceClient = ProductServiceClient.create()) {
       SetInventoryRequest request =
           SetInventoryRequest.newBuilder()
               .setInventory(Product.newBuilder().build())
               .setSetMask(FieldMask.newBuilder().build())
               .setSetTime(Timestamp.newBuilder().build())
               .setAllowMissing(true)
               .build();
       SetInventoryResponse response = productServiceClient.setInventoryAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetInventoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SetInventoryRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[SetInventoryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SetInventoryResponse),[SetInventoryMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SetInventoryMetadata)>` |   
  
### setInventoryCallable()
    
    
    public final UnaryCallable<SetInventoryRequest,Operation> setInventoryCallable()

Updates inventory information for a Product while respecting the last update timestamps of each inventory field.

This process is asynchronous and does not require the Product to exist before updating fulfillment information. If the request is valid, the update is enqueued and processed downstream. As a consequence, when a response is returned, updates are not immediately manifested in the Product queried by ProductService.GetProduct or ProductService.ListProducts.

When inventory is updated with ProductService.CreateProduct and ProductService.UpdateProduct, the specified inventory field value(s) overwrite any existing value(s) while ignoring the last update time for this field. Furthermore, the last update times for the specified inventory fields are overwritten by the times of the ProductService.CreateProduct or ProductService.UpdateProduct request.

If no inventory fields are set in CreateProductRequest.product, then any pre-existing inventory information for this product is used.

If no inventory fields are set in SetInventoryRequest.set_mask, then any existing inventory information is preserved.

Pre-existing inventory information can only be updated with ProductService.SetInventory, ProductService.AddFulfillmentPlaces, and ProductService.RemoveFulfillmentPlaces.

The returned Operations is obsolete after one day, and the GetOperation API returns `NOT_FOUND` afterwards.

If conflicting updates are issued, the Operations associated with the stale updates are not marked as done until they are obsolete.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductServiceClient productServiceClient = ProductServiceClient.create()) {
       SetInventoryRequest request =
           SetInventoryRequest.newBuilder()
               .setInventory(Product.newBuilder().build())
               .setSetMask(FieldMask.newBuilder().build())
               .setSetTime(Timestamp.newBuilder().build())
               .setAllowMissing(true)
               .build();
       ApiFuture<Operation> future = productServiceClient.setInventoryCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetInventoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SetInventoryRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### setInventoryOperationCallable()
    
    
    public final OperationCallable<SetInventoryRequest,SetInventoryResponse,SetInventoryMetadata> setInventoryOperationCallable()

Updates inventory information for a Product while respecting the last update timestamps of each inventory field.

This process is asynchronous and does not require the Product to exist before updating fulfillment information. If the request is valid, the update is enqueued and processed downstream. As a consequence, when a response is returned, updates are not immediately manifested in the Product queried by ProductService.GetProduct or ProductService.ListProducts.

When inventory is updated with ProductService.CreateProduct and ProductService.UpdateProduct, the specified inventory field value(s) overwrite any existing value(s) while ignoring the last update time for this field. Furthermore, the last update times for the specified inventory fields are overwritten by the times of the ProductService.CreateProduct or ProductService.UpdateProduct request.

If no inventory fields are set in CreateProductRequest.product, then any pre-existing inventory information for this product is used.

If no inventory fields are set in SetInventoryRequest.set_mask, then any existing inventory information is preserved.

Pre-existing inventory information can only be updated with ProductService.SetInventory, ProductService.AddFulfillmentPlaces, and ProductService.RemoveFulfillmentPlaces.

The returned Operations is obsolete after one day, and the GetOperation API returns `NOT_FOUND` afterwards.

If conflicting updates are issued, the Operations associated with the stale updates are not marked as done until they are obsolete.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductServiceClient productServiceClient = ProductServiceClient.create()) {
       SetInventoryRequest request =
           SetInventoryRequest.newBuilder()
               .setInventory(Product.newBuilder().build())
               .setSetMask(FieldMask.newBuilder().build())
               .setSetTime(Timestamp.newBuilder().build())
               .setAllowMissing(true)
               .build();
       OperationFuture<SetInventoryResponse, SetInventoryMetadata> future =
           productServiceClient.setInventoryOperationCallable().futureCall(request);
       // Do something.
       SetInventoryResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetInventoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SetInventoryRequest),[SetInventoryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SetInventoryResponse),[SetInventoryMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SetInventoryMetadata)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateProduct(Product product, FieldMask updateMask)
    
    
    public final Product updateProduct(Product product, FieldMask updateMask)

Updates a Product.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductServiceClient productServiceClient = ProductServiceClient.create()) {
       Product product = Product.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Product response = productServiceClient.updateProduct(product, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`product` | `[Product](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Product)`  
Required. The product to update/create. If the caller does not have permission to update the Product, regardless of whether or not it exists, a PERMISSION_DENIED error is returned. If the Product to update does not exist and allow_missing is not set, a NOT_FOUND error is returned.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Indicates which fields in the provided Product to update. The immutable and output only fields are NOT supported. If not set, all supported fields (the fields that are neither immutable nor output only) are updated. If an unsupported or unknown field is provided, an INVALID_ARGUMENT error is returned. The attribute key can be updated by setting the mask path as "attributes.${key_name}". If a key name is present in the mask but not in the patching product from the request, this key will be deleted after the update.  
**Returns**  
---  
**Type** | **Description**  
`[Product](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Product)` |   
  
### updateProduct(UpdateProductRequest request)
    
    
    public final Product updateProduct(UpdateProductRequest request)

Updates a Product.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductServiceClient productServiceClient = ProductServiceClient.create()) {
       UpdateProductRequest request =
           UpdateProductRequest.newBuilder()
               .setProduct(Product.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setAllowMissing(true)
               .build();
       Product response = productServiceClient.updateProduct(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateProductRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.UpdateProductRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Product](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Product)` |   
  
### updateProductCallable()
    
    
    public final UnaryCallable<UpdateProductRequest,Product> updateProductCallable()

Updates a Product.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductServiceClient productServiceClient = ProductServiceClient.create()) {
       UpdateProductRequest request =
           UpdateProductRequest.newBuilder()
               .setProduct(Product.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setAllowMissing(true)
               .build();
       ApiFuture<Product> future = productServiceClient.updateProductCallable().futureCall(request);
       // Do something.
       Product response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateProductRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.UpdateProductRequest),[Product](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Product)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
