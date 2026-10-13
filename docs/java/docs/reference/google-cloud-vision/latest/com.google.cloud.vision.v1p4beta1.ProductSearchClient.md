---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ProductSearchClient
title: Class ProductSearchClient (3.97.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:44:29.303121+00:00
---

# Class ProductSearchClient (3.97.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ProductSearchClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ProductSearchClient (3.97.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.97.0 (latest)  3.93.0  3.92.0  3.91.0  3.89.0  3.86.0  3.85.0  3.83.0  3.81.0  3.80.0  3.78.0  3.76.0  3.74.0  3.73.0  3.72.0  3.71.0  3.70.0  3.68.0  3.66.0  3.65.0  3.62.0  3.61.0  3.60.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.51.0  3.50.0  3.49.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.39.0  3.38.0  3.37.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.3  2.1.4  2.0.29 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-vision/google-cloud-vision/src/main/java/com/google/cloud/vision/v1p4beta1/ProductSearchClient.java)| [Product Reference](https://cloud.google.com/vision/docs/)| [REST Documentation](https://cloud.google.com/vision/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/vision/docs/reference/rpc)  
---|---|---|---  
  
Service Description: Manages Products and ProductSets of reference images for use in product search. It uses the following resource model:

\- The API has a collection of ProductSet resources, named `projects/*/locations/*/productSets/*`, which acts as a way to put different products into groups to limit identification.

In parallel,

\- The API has a collection of Product resources, named `projects/*/locations/*/products/*`

\- Each Product has a collection of ReferenceImage resources, named `projects/*/locations/*/products/*/referenceImages/*`

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       ProductSet productSet = ProductSet.newBuilder().build();
       String productSetId = "productSetId1003042158";
       ProductSet response = productSearchClient.createProductSet(parent, productSet, productSetId);
     }
     

Note: close() needs to be called on the ProductSearchClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateProductSet |  Creates and returns a new ProductSet resource.  Possible errors: 

  * Returns INVALID_ARGUMENT if display_name is missing, or is longer than 4096 characters. 

|  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createProductSet(CreateProductSetRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createProductSet(LocationName parent, ProductSet productSet, String productSetId) 
  * createProductSet(String parent, ProductSet productSet, String productSetId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createProductSetCallable() 

  
ListProductSets |  Lists ProductSets in an unspecified order.  Possible errors: 

  * Returns INVALID_ARGUMENT if page_size is greater than 100, or less than 1. 

|  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listProductSets(ListProductSetsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listProductSets(LocationName parent) 
  * listProductSets(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listProductSetsPagedCallable() 
  * listProductSetsCallable() 

  
GetProductSet |  Gets information associated with a ProductSet.  Possible errors: 

  * Returns NOT_FOUND if the ProductSet does not exist. 

|  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getProductSet(GetProductSetRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getProductSet(ProductSetName name) 
  * getProductSet(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getProductSetCallable() 

  
UpdateProductSet |  Makes changes to a ProductSet resource. Only display_name can be updated currently.  Possible errors: 

  * Returns NOT_FOUND if the ProductSet does not exist. 
  * Returns INVALID_ARGUMENT if display_name is present in update_mask but missing from the request or longer than 4096 characters. 

|  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateProductSet(UpdateProductSetRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateProductSet(ProductSet productSet, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateProductSetCallable() 

  
DeleteProductSet |  Permanently deletes a ProductSet. Products and ReferenceImages in the ProductSet are not deleted.  The actual image files are not deleted from Google Cloud Storage. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteProductSet(DeleteProductSetRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteProductSet(ProductSetName name) 
  * deleteProductSet(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteProductSetCallable() 

  
CreateProduct |  Creates and returns a new product resource.  Possible errors: 

  * Returns INVALID_ARGUMENT if display_name is missing or longer than 4096 characters. 
  * Returns INVALID_ARGUMENT if description is longer than 4096 characters. 
  * Returns INVALID_ARGUMENT if product_category is missing or invalid. 

|  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createProduct(CreateProductRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createProduct(LocationName parent, Product product, String productId) 
  * createProduct(String parent, Product product, String productId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createProductCallable() 

  
ListProducts |  Lists products in an unspecified order.  Possible errors: 

  * Returns INVALID_ARGUMENT if page_size is greater than 100 or less than 1. 

|  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listProducts(ListProductsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listProducts(LocationName parent) 
  * listProducts(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listProductsPagedCallable() 
  * listProductsCallable() 

  
GetProduct |  Gets information associated with a Product.  Possible errors: 

  * Returns NOT_FOUND if the Product does not exist. 

|  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getProduct(GetProductRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getProduct(ProductName name) 
  * getProduct(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getProductCallable() 

  
UpdateProduct |  Makes changes to a Product resource. Only the `display_name`, `description`, and `labels` fields can be updated right now.  If labels are updated, the change will not be reflected in queries until the next index time.  Possible errors: 

  * Returns NOT_FOUND if the Product does not exist. 
  * Returns INVALID_ARGUMENT if display_name is present in update_mask but is missing from the request or longer than 4096 characters. 
  * Returns INVALID_ARGUMENT if description is present in update_mask but is longer than 4096 characters. 
  * Returns INVALID_ARGUMENT if product_category is present in update_mask. 

|  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateProduct(UpdateProductRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateProduct(Product product, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateProductCallable() 

  
DeleteProduct |  Permanently deletes a product and its reference images.  Metadata of the product and all its images will be deleted right away, but search queries against ProductSets containing the product may still work until all related caches are refreshed. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteProduct(DeleteProductRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteProduct(ProductName name) 
  * deleteProduct(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteProductCallable() 

  
CreateReferenceImage |  Creates and returns a new ReferenceImage resource.  The `bounding_poly` field is optional. If `bounding_poly` is not specified, the system will try to detect regions of interest in the image that are compatible with the product_category on the parent product. If it is specified, detection is ALWAYS skipped. The system converts polygons into non-rotated rectangles.  Note that the pipeline will resize the image if the image resolution is too large to process (above 50MP).  Possible errors: 

  * Returns INVALID_ARGUMENT if the image_uri is missing or longer than 4096 characters. 
  * Returns INVALID_ARGUMENT if the product does not exist. 
  * Returns INVALID_ARGUMENT if bounding_poly is not provided, and nothing compatible with the parent product's product_category is detected. 
  * Returns INVALID_ARGUMENT if bounding_poly contains more than 10 polygons. 

|  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createReferenceImage(CreateReferenceImageRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createReferenceImage(ProductName parent, ReferenceImage referenceImage, String referenceImageId) 
  * createReferenceImage(String parent, ReferenceImage referenceImage, String referenceImageId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createReferenceImageCallable() 

  
DeleteReferenceImage |  Permanently deletes a reference image.  The image metadata will be deleted right away, but search queries against ProductSets containing the image may still work until all related caches are refreshed.  The actual image files are not deleted from Google Cloud Storage. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteReferenceImage(DeleteReferenceImageRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteReferenceImage(ReferenceImageName name) 
  * deleteReferenceImage(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteReferenceImageCallable() 

  
ListReferenceImages |  Lists reference images.  Possible errors: 

  * Returns NOT_FOUND if the parent product does not exist. 
  * Returns INVALID_ARGUMENT if the page_size is greater than 100, or less than 1. 

|  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listReferenceImages(ListReferenceImagesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listReferenceImages(ProductName parent) 
  * listReferenceImages(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listReferenceImagesPagedCallable() 
  * listReferenceImagesCallable() 

  
GetReferenceImage |  Gets information associated with a ReferenceImage.  Possible errors: 

  * Returns NOT_FOUND if the specified image does not exist. 

|  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getReferenceImage(GetReferenceImageRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getReferenceImage(ReferenceImageName name) 
  * getReferenceImage(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getReferenceImageCallable() 

  
AddProductToProductSet |  Adds a Product to the specified ProductSet. If the Product is already present, no change is made.  One Product can be added to at most 100 ProductSets.  Possible errors: 

  * Returns NOT_FOUND if the Product or the ProductSet doesn't exist. 

|  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * addProductToProductSet(AddProductToProductSetRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * addProductToProductSet(ProductSetName name, ProductName product) 
  * addProductToProductSet(ProductSetName name, String product) 
  * addProductToProductSet(String name, ProductName product) 
  * addProductToProductSet(String name, String product) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * addProductToProductSetCallable() 

  
RemoveProductFromProductSet |  Removes a Product from the specified ProductSet. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * removeProductFromProductSet(RemoveProductFromProductSetRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * removeProductFromProductSet(ProductSetName name, ProductName product) 
  * removeProductFromProductSet(ProductSetName name, String product) 
  * removeProductFromProductSet(String name, ProductName product) 
  * removeProductFromProductSet(String name, String product) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * removeProductFromProductSetCallable() 

  
ListProductsInProductSet |  Lists the Products in a ProductSet, in an unspecified order. If the ProductSet does not exist, the products field of the response will be empty.  Possible errors: 

  * Returns INVALID_ARGUMENT if page_size is greater than 100 or less than 1. 

|  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listProductsInProductSet(ListProductsInProductSetRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listProductsInProductSet(ProductSetName name) 
  * listProductsInProductSet(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listProductsInProductSetPagedCallable() 
  * listProductsInProductSetCallable() 

  
ImportProductSets |  Asynchronous API that imports a list of reference images to specified product sets based on a list of image information.  The google.longrunning.Operation API can be used to keep track of the progress and results of the request. `Operation.metadata` contains `BatchOperationMetadata`. (progress) `Operation.response` contains `ImportProductSetsResponse`. (results)  The input source of this method is a csv file on Google Cloud Storage. For the format of the csv file please see ImportProductSetsGcsSource.csv_file_uri. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * importProductSetsAsync(ImportProductSetsRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * importProductSetsAsync(LocationName parent, ImportProductSetsInputConfig inputConfig) 
  * importProductSetsAsync(String parent, ImportProductSetsInputConfig inputConfig) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * importProductSetsOperationCallable() 
  * importProductSetsCallable() 

  
PurgeProducts |  Asynchronous API to delete all Products in a ProductSet or all Products that are in no ProductSet.  If a Product is a member of the specified ProductSet in addition to other ProductSets, the Product will still be deleted.  It is recommended to not delete the specified ProductSet until after this operation has completed. It is also recommended to not add any of the Products involved in the batch delete to a new ProductSet while this operation is running because those Products may still end up deleted.  It's not possible to undo the PurgeProducts operation. Therefore, it is recommended to keep the csv files used in ImportProductSets (if that was how you originally built the Product Set) before starting PurgeProducts, in case you need to re-import the data after deletion.  If the plan is to purge all of the Products from a ProductSet and then re-use the empty ProductSet to re-import new Products into the empty ProductSet, you must wait until the PurgeProducts operation has finished for that ProductSet.  The google.longrunning.Operation API can be used to keep track of the progress and results of the request. `Operation.metadata` contains `BatchOperationMetadata`. (progress) |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * purgeProductsAsync(PurgeProductsRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * purgeProductsAsync(LocationName parent) 
  * purgeProductsAsync(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * purgeProductsOperationCallable() 
  * purgeProductsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of ProductSearchSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ProductSearchSettings productSearchSettings =
         ProductSearchSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     ProductSearchClient productSearchClient = ProductSearchClient.create(productSearchSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ProductSearchSettings productSearchSettings =
         ProductSearchSettings.newBuilder().setEndpoint(myEndpoint).build();
     ProductSearchClient productSearchClient = ProductSearchClient.create(productSearchSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ProductSearchSettings productSearchSettings =
         ProductSearchSettings.newHttpJsonBuilder().build();
     ProductSearchClient productSearchClient = ProductSearchClient.create(productSearchSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ProductSearchClient

## Static Methods 

### create()
    
    
    public static final ProductSearchClient create()

Constructs an instance of ProductSearchClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[ProductSearchClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ProductSearchClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ProductSearchSettings settings)
    
    
    public static final ProductSearchClient create(ProductSearchSettings settings)

Constructs an instance of ProductSearchClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ProductSearchSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ProductSearchSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductSearchClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ProductSearchClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ProductSearchStub stub)
    
    
    public static final ProductSearchClient create(ProductSearchStub stub)

Constructs an instance of ProductSearchClient, using the given stub for making calls. This is for advanced usage - prefer using create(ProductSearchSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ProductSearchStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.stub.ProductSearchStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductSearchClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ProductSearchClient)` |   
  
## Constructors 

### ProductSearchClient(ProductSearchSettings settings)
    
    
    protected ProductSearchClient(ProductSearchSettings settings)

Constructs an instance of ProductSearchClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ProductSearchSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ProductSearchSettings)`  
  
  
### ProductSearchClient(ProductSearchStub stub)
    
    
    protected ProductSearchClient(ProductSearchStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ProductSearchStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.stub.ProductSearchStub)`  
  
  
## Methods 

### addProductToProductSet(@Nullable ProductSetName name, @Nullable ProductName product)
    
    
    public final void addProductToProductSet(@Nullable ProductSetName name, @Nullable ProductName product)

Adds a Product to the specified ProductSet. If the Product is already present, no change is made.

One Product can be added to at most 100 ProductSets.

Possible errors:

  * Returns NOT_FOUND if the Product or the ProductSet doesn't exist. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       ProductSetName name = ProductSetName.of("[PROJECT]", "[LOCATION]", "[PRODUCT_SET]");
       ProductName product = ProductName.of("[PROJECT]", "[LOCATION]", "[PRODUCT]");
       productSearchClient.addProductToProductSet(name, product);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.vision.v1p4beta1.ProductSetName`  
Required. The resource name for the ProductSet to modify. Format is: `projects/PROJECT_ID/locations/LOC_ID/productSets/PRODUCT_SET_ID`  
`product` | `@org.jspecify.annotations.Nullable com.google.cloud.vision.v1p4beta1.ProductName`  
Required. The resource name for the Product to be added to this ProductSet. Format is: `projects/PROJECT_ID/locations/LOC_ID/products/PRODUCT_ID`  
  
### addProductToProductSet(@Nullable ProductSetName name, String product)
    
    
    public final void addProductToProductSet(@Nullable ProductSetName name, String product)

Adds a Product to the specified ProductSet. If the Product is already present, no change is made.

One Product can be added to at most 100 ProductSets.

Possible errors:

  * Returns NOT_FOUND if the Product or the ProductSet doesn't exist. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       ProductSetName name = ProductSetName.of("[PROJECT]", "[LOCATION]", "[PRODUCT_SET]");
       String product = ProductName.of("[PROJECT]", "[LOCATION]", "[PRODUCT]").toString();
       productSearchClient.addProductToProductSet(name, product);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.vision.v1p4beta1.ProductSetName`  
Required. The resource name for the ProductSet to modify. Format is: `projects/PROJECT_ID/locations/LOC_ID/productSets/PRODUCT_SET_ID`  
`product` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name for the Product to be added to this ProductSet. Format is: `projects/PROJECT_ID/locations/LOC_ID/products/PRODUCT_ID`  
  
### addProductToProductSet(AddProductToProductSetRequest request)
    
    
    public final void addProductToProductSet(AddProductToProductSetRequest request)

Adds a Product to the specified ProductSet. If the Product is already present, no change is made.

One Product can be added to at most 100 ProductSets.

Possible errors:

  * Returns NOT_FOUND if the Product or the ProductSet doesn't exist. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       AddProductToProductSetRequest request =
           AddProductToProductSetRequest.newBuilder()
               .setName(ProductSetName.of("[PROJECT]", "[LOCATION]", "[PRODUCT_SET]").toString())
               .setProduct(ProductName.of("[PROJECT]", "[LOCATION]", "[PRODUCT]").toString())
               .build();
       productSearchClient.addProductToProductSet(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AddProductToProductSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.AddProductToProductSetRequest)`  
The request object containing all of the parameters for the API call.  
  
### addProductToProductSet(String name, @Nullable ProductName product)
    
    
    public final void addProductToProductSet(String name, @Nullable ProductName product)

Adds a Product to the specified ProductSet. If the Product is already present, no change is made.

One Product can be added to at most 100 ProductSets.

Possible errors:

  * Returns NOT_FOUND if the Product or the ProductSet doesn't exist. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       String name = ProductSetName.of("[PROJECT]", "[LOCATION]", "[PRODUCT_SET]").toString();
       ProductName product = ProductName.of("[PROJECT]", "[LOCATION]", "[PRODUCT]");
       productSearchClient.addProductToProductSet(name, product);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name for the ProductSet to modify. Format is: `projects/PROJECT_ID/locations/LOC_ID/productSets/PRODUCT_SET_ID`  
`product` | `@org.jspecify.annotations.Nullable com.google.cloud.vision.v1p4beta1.ProductName`  
Required. The resource name for the Product to be added to this ProductSet. Format is: `projects/PROJECT_ID/locations/LOC_ID/products/PRODUCT_ID`  
  
### addProductToProductSet(String name, String product)
    
    
    public final void addProductToProductSet(String name, String product)

Adds a Product to the specified ProductSet. If the Product is already present, no change is made.

One Product can be added to at most 100 ProductSets.

Possible errors:

  * Returns NOT_FOUND if the Product or the ProductSet doesn't exist. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       String name = ProductSetName.of("[PROJECT]", "[LOCATION]", "[PRODUCT_SET]").toString();
       String product = ProductName.of("[PROJECT]", "[LOCATION]", "[PRODUCT]").toString();
       productSearchClient.addProductToProductSet(name, product);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name for the ProductSet to modify. Format is: `projects/PROJECT_ID/locations/LOC_ID/productSets/PRODUCT_SET_ID`  
`product` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name for the Product to be added to this ProductSet. Format is: `projects/PROJECT_ID/locations/LOC_ID/products/PRODUCT_ID`  
  
### addProductToProductSetCallable()
    
    
    public final UnaryCallable<AddProductToProductSetRequest,Empty> addProductToProductSetCallable()

Adds a Product to the specified ProductSet. If the Product is already present, no change is made.

One Product can be added to at most 100 ProductSets.

Possible errors:

  * Returns NOT_FOUND if the Product or the ProductSet doesn't exist. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       AddProductToProductSetRequest request =
           AddProductToProductSetRequest.newBuilder()
               .setName(ProductSetName.of("[PROJECT]", "[LOCATION]", "[PRODUCT_SET]").toString())
               .setProduct(ProductName.of("[PROJECT]", "[LOCATION]", "[PRODUCT]").toString())
               .build();
       ApiFuture<Empty> future =
           productSearchClient.addProductToProductSetCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AddProductToProductSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.AddProductToProductSetRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
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

### createProduct(@Nullable LocationName parent, Product product, String productId)
    
    
    public final Product createProduct(@Nullable LocationName parent, Product product, String productId)

Creates and returns a new product resource.

Possible errors:

  * Returns INVALID_ARGUMENT if display_name is missing or longer than 4096 characters. 
  * Returns INVALID_ARGUMENT if description is longer than 4096 characters. 
  * Returns INVALID_ARGUMENT if product_category is missing or invalid. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Product product = Product.newBuilder().build();
       String productId = "productId-1051830678";
       Product response = productSearchClient.createProduct(parent, product, productId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.vision.v1p4beta1.LocationName`  
Required. The project in which the Product should be created. Format is `projects/PROJECT_ID/locations/LOC_ID`.  
`product` | `[Product](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.Product)`  
Required. The product to create.  
`productId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
A user-supplied resource id for this Product. If set, the server will attempt to use this value as the resource id. If it is already in use, an error is returned with code ALREADY_EXISTS. Must be at most 128 characters long. It cannot contain the character `/`.  
**Returns**  
---  
**Type** | **Description**  
`[Product](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.Product)` |   
  
### createProduct(CreateProductRequest request)
    
    
    public final Product createProduct(CreateProductRequest request)

Creates and returns a new product resource.

Possible errors:

  * Returns INVALID_ARGUMENT if display_name is missing or longer than 4096 characters. 
  * Returns INVALID_ARGUMENT if description is longer than 4096 characters. 
  * Returns INVALID_ARGUMENT if product_category is missing or invalid. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       CreateProductRequest request =
           CreateProductRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setProduct(Product.newBuilder().build())
               .setProductId("productId-1051830678")
               .build();
       Product response = productSearchClient.createProduct(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateProductRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.CreateProductRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Product](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.Product)` |   
  
### createProduct(String parent, Product product, String productId)
    
    
    public final Product createProduct(String parent, Product product, String productId)

Creates and returns a new product resource.

Possible errors:

  * Returns INVALID_ARGUMENT if display_name is missing or longer than 4096 characters. 
  * Returns INVALID_ARGUMENT if description is longer than 4096 characters. 
  * Returns INVALID_ARGUMENT if product_category is missing or invalid. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Product product = Product.newBuilder().build();
       String productId = "productId-1051830678";
       Product response = productSearchClient.createProduct(parent, product, productId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project in which the Product should be created. Format is `projects/PROJECT_ID/locations/LOC_ID`.  
`product` | `[Product](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.Product)`  
Required. The product to create.  
`productId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
A user-supplied resource id for this Product. If set, the server will attempt to use this value as the resource id. If it is already in use, an error is returned with code ALREADY_EXISTS. Must be at most 128 characters long. It cannot contain the character `/`.  
**Returns**  
---  
**Type** | **Description**  
`[Product](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.Product)` |   
  
### createProductCallable()
    
    
    public final UnaryCallable<CreateProductRequest,Product> createProductCallable()

Creates and returns a new product resource.

Possible errors:

  * Returns INVALID_ARGUMENT if display_name is missing or longer than 4096 characters. 
  * Returns INVALID_ARGUMENT if description is longer than 4096 characters. 
  * Returns INVALID_ARGUMENT if product_category is missing or invalid. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       CreateProductRequest request =
           CreateProductRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setProduct(Product.newBuilder().build())
               .setProductId("productId-1051830678")
               .build();
       ApiFuture<Product> future = productSearchClient.createProductCallable().futureCall(request);
       // Do something.
       Product response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateProductRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.CreateProductRequest),[Product](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.Product)>` |   
  
### createProductSet(@Nullable LocationName parent, ProductSet productSet, String productSetId)
    
    
    public final ProductSet createProductSet(@Nullable LocationName parent, ProductSet productSet, String productSetId)

Creates and returns a new ProductSet resource.

Possible errors:

  * Returns INVALID_ARGUMENT if display_name is missing, or is longer than 4096 characters. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       ProductSet productSet = ProductSet.newBuilder().build();
       String productSetId = "productSetId1003042158";
       ProductSet response = productSearchClient.createProductSet(parent, productSet, productSetId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.vision.v1p4beta1.LocationName`  
Required. The project in which the ProductSet should be created. Format is `projects/PROJECT_ID/locations/LOC_ID`.  
`productSet` | `[ProductSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ProductSet)`  
Required. The ProductSet to create.  
`productSetId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
A user-supplied resource id for this ProductSet. If set, the server will attempt to use this value as the resource id. If it is already in use, an error is returned with code ALREADY_EXISTS. Must be at most 128 characters long. It cannot contain the character `/`.  
**Returns**  
---  
**Type** | **Description**  
`[ProductSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ProductSet)` |   
  
### createProductSet(CreateProductSetRequest request)
    
    
    public final ProductSet createProductSet(CreateProductSetRequest request)

Creates and returns a new ProductSet resource.

Possible errors:

  * Returns INVALID_ARGUMENT if display_name is missing, or is longer than 4096 characters. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       CreateProductSetRequest request =
           CreateProductSetRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setProductSet(ProductSet.newBuilder().build())
               .setProductSetId("productSetId1003042158")
               .build();
       ProductSet response = productSearchClient.createProductSet(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateProductSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.CreateProductSetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ProductSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ProductSet)` |   
  
### createProductSet(String parent, ProductSet productSet, String productSetId)
    
    
    public final ProductSet createProductSet(String parent, ProductSet productSet, String productSetId)

Creates and returns a new ProductSet resource.

Possible errors:

  * Returns INVALID_ARGUMENT if display_name is missing, or is longer than 4096 characters. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       ProductSet productSet = ProductSet.newBuilder().build();
       String productSetId = "productSetId1003042158";
       ProductSet response = productSearchClient.createProductSet(parent, productSet, productSetId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project in which the ProductSet should be created. Format is `projects/PROJECT_ID/locations/LOC_ID`.  
`productSet` | `[ProductSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ProductSet)`  
Required. The ProductSet to create.  
`productSetId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
A user-supplied resource id for this ProductSet. If set, the server will attempt to use this value as the resource id. If it is already in use, an error is returned with code ALREADY_EXISTS. Must be at most 128 characters long. It cannot contain the character `/`.  
**Returns**  
---  
**Type** | **Description**  
`[ProductSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ProductSet)` |   
  
### createProductSetCallable()
    
    
    public final UnaryCallable<CreateProductSetRequest,ProductSet> createProductSetCallable()

Creates and returns a new ProductSet resource.

Possible errors:

  * Returns INVALID_ARGUMENT if display_name is missing, or is longer than 4096 characters. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       CreateProductSetRequest request =
           CreateProductSetRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setProductSet(ProductSet.newBuilder().build())
               .setProductSetId("productSetId1003042158")
               .build();
       ApiFuture<ProductSet> future =
           productSearchClient.createProductSetCallable().futureCall(request);
       // Do something.
       ProductSet response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateProductSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.CreateProductSetRequest),[ProductSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ProductSet)>` |   
  
### createReferenceImage(@Nullable ProductName parent, ReferenceImage referenceImage, String referenceImageId)
    
    
    public final ReferenceImage createReferenceImage(@Nullable ProductName parent, ReferenceImage referenceImage, String referenceImageId)

Creates and returns a new ReferenceImage resource.

The `bounding_poly` field is optional. If `bounding_poly` is not specified, the system will try to detect regions of interest in the image that are compatible with the product_category on the parent product. If it is specified, detection is ALWAYS skipped. The system converts polygons into non-rotated rectangles.

Note that the pipeline will resize the image if the image resolution is too large to process (above 50MP).

Possible errors:

  * Returns INVALID_ARGUMENT if the image_uri is missing or longer than 4096 characters. 
  * Returns INVALID_ARGUMENT if the product does not exist. 
  * Returns INVALID_ARGUMENT if bounding_poly is not provided, and nothing compatible with the parent product's product_category is detected. 
  * Returns INVALID_ARGUMENT if bounding_poly contains more than 10 polygons. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       ProductName parent = ProductName.of("[PROJECT]", "[LOCATION]", "[PRODUCT]");
       ReferenceImage referenceImage = ReferenceImage.newBuilder().build();
       String referenceImageId = "referenceImageId1224107531";
       ReferenceImage response =
           productSearchClient.createReferenceImage(parent, referenceImage, referenceImageId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.vision.v1p4beta1.ProductName`  
Required. Resource name of the product in which to create the reference image. Format is `projects/PROJECT_ID/locations/LOC_ID/products/PRODUCT_ID`.  
`referenceImage` | `[ReferenceImage](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ReferenceImage)`  
Required. The reference image to create. If an image ID is specified, it is ignored.  
`referenceImageId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
A user-supplied resource id for the ReferenceImage to be added. If set, the server will attempt to use this value as the resource id. If it is already in use, an error is returned with code ALREADY_EXISTS. Must be at most 128 characters long. It cannot contain the character `/`.  
**Returns**  
---  
**Type** | **Description**  
`[ReferenceImage](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ReferenceImage)` |   
  
### createReferenceImage(CreateReferenceImageRequest request)
    
    
    public final ReferenceImage createReferenceImage(CreateReferenceImageRequest request)

Creates and returns a new ReferenceImage resource.

The `bounding_poly` field is optional. If `bounding_poly` is not specified, the system will try to detect regions of interest in the image that are compatible with the product_category on the parent product. If it is specified, detection is ALWAYS skipped. The system converts polygons into non-rotated rectangles.

Note that the pipeline will resize the image if the image resolution is too large to process (above 50MP).

Possible errors:

  * Returns INVALID_ARGUMENT if the image_uri is missing or longer than 4096 characters. 
  * Returns INVALID_ARGUMENT if the product does not exist. 
  * Returns INVALID_ARGUMENT if bounding_poly is not provided, and nothing compatible with the parent product's product_category is detected. 
  * Returns INVALID_ARGUMENT if bounding_poly contains more than 10 polygons. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       CreateReferenceImageRequest request =
           CreateReferenceImageRequest.newBuilder()
               .setParent(ProductName.of("[PROJECT]", "[LOCATION]", "[PRODUCT]").toString())
               .setReferenceImage(ReferenceImage.newBuilder().build())
               .setReferenceImageId("referenceImageId1224107531")
               .build();
       ReferenceImage response = productSearchClient.createReferenceImage(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateReferenceImageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.CreateReferenceImageRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ReferenceImage](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ReferenceImage)` |   
  
### createReferenceImage(String parent, ReferenceImage referenceImage, String referenceImageId)
    
    
    public final ReferenceImage createReferenceImage(String parent, ReferenceImage referenceImage, String referenceImageId)

Creates and returns a new ReferenceImage resource.

The `bounding_poly` field is optional. If `bounding_poly` is not specified, the system will try to detect regions of interest in the image that are compatible with the product_category on the parent product. If it is specified, detection is ALWAYS skipped. The system converts polygons into non-rotated rectangles.

Note that the pipeline will resize the image if the image resolution is too large to process (above 50MP).

Possible errors:

  * Returns INVALID_ARGUMENT if the image_uri is missing or longer than 4096 characters. 
  * Returns INVALID_ARGUMENT if the product does not exist. 
  * Returns INVALID_ARGUMENT if bounding_poly is not provided, and nothing compatible with the parent product's product_category is detected. 
  * Returns INVALID_ARGUMENT if bounding_poly contains more than 10 polygons. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       String parent = ProductName.of("[PROJECT]", "[LOCATION]", "[PRODUCT]").toString();
       ReferenceImage referenceImage = ReferenceImage.newBuilder().build();
       String referenceImageId = "referenceImageId1224107531";
       ReferenceImage response =
           productSearchClient.createReferenceImage(parent, referenceImage, referenceImageId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name of the product in which to create the reference image. Format is `projects/PROJECT_ID/locations/LOC_ID/products/PRODUCT_ID`.  
`referenceImage` | `[ReferenceImage](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ReferenceImage)`  
Required. The reference image to create. If an image ID is specified, it is ignored.  
`referenceImageId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
A user-supplied resource id for the ReferenceImage to be added. If set, the server will attempt to use this value as the resource id. If it is already in use, an error is returned with code ALREADY_EXISTS. Must be at most 128 characters long. It cannot contain the character `/`.  
**Returns**  
---  
**Type** | **Description**  
`[ReferenceImage](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ReferenceImage)` |   
  
### createReferenceImageCallable()
    
    
    public final UnaryCallable<CreateReferenceImageRequest,ReferenceImage> createReferenceImageCallable()

Creates and returns a new ReferenceImage resource.

The `bounding_poly` field is optional. If `bounding_poly` is not specified, the system will try to detect regions of interest in the image that are compatible with the product_category on the parent product. If it is specified, detection is ALWAYS skipped. The system converts polygons into non-rotated rectangles.

Note that the pipeline will resize the image if the image resolution is too large to process (above 50MP).

Possible errors:

  * Returns INVALID_ARGUMENT if the image_uri is missing or longer than 4096 characters. 
  * Returns INVALID_ARGUMENT if the product does not exist. 
  * Returns INVALID_ARGUMENT if bounding_poly is not provided, and nothing compatible with the parent product's product_category is detected. 
  * Returns INVALID_ARGUMENT if bounding_poly contains more than 10 polygons. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       CreateReferenceImageRequest request =
           CreateReferenceImageRequest.newBuilder()
               .setParent(ProductName.of("[PROJECT]", "[LOCATION]", "[PRODUCT]").toString())
               .setReferenceImage(ReferenceImage.newBuilder().build())
               .setReferenceImageId("referenceImageId1224107531")
               .build();
       ApiFuture<ReferenceImage> future =
           productSearchClient.createReferenceImageCallable().futureCall(request);
       // Do something.
       ReferenceImage response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateReferenceImageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.CreateReferenceImageRequest),[ReferenceImage](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ReferenceImage)>` |   
  
### deleteProduct(@Nullable ProductName name)
    
    
    public final void deleteProduct(@Nullable ProductName name)

Permanently deletes a product and its reference images.

Metadata of the product and all its images will be deleted right away, but search queries against ProductSets containing the product may still work until all related caches are refreshed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       ProductName name = ProductName.of("[PROJECT]", "[LOCATION]", "[PRODUCT]");
       productSearchClient.deleteProduct(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.vision.v1p4beta1.ProductName`  
Required. Resource name of product to delete. Format is: `projects/PROJECT_ID/locations/LOC_ID/products/PRODUCT_ID`  
  
### deleteProduct(DeleteProductRequest request)
    
    
    public final void deleteProduct(DeleteProductRequest request)

Permanently deletes a product and its reference images.

Metadata of the product and all its images will be deleted right away, but search queries against ProductSets containing the product may still work until all related caches are refreshed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       DeleteProductRequest request =
           DeleteProductRequest.newBuilder()
               .setName(ProductName.of("[PROJECT]", "[LOCATION]", "[PRODUCT]").toString())
               .build();
       productSearchClient.deleteProduct(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteProductRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.DeleteProductRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteProduct(String name)
    
    
    public final void deleteProduct(String name)

Permanently deletes a product and its reference images.

Metadata of the product and all its images will be deleted right away, but search queries against ProductSets containing the product may still work until all related caches are refreshed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       String name = ProductName.of("[PROJECT]", "[LOCATION]", "[PRODUCT]").toString();
       productSearchClient.deleteProduct(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name of product to delete. Format is: `projects/PROJECT_ID/locations/LOC_ID/products/PRODUCT_ID`  
  
### deleteProductCallable()
    
    
    public final UnaryCallable<DeleteProductRequest,Empty> deleteProductCallable()

Permanently deletes a product and its reference images.

Metadata of the product and all its images will be deleted right away, but search queries against ProductSets containing the product may still work until all related caches are refreshed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       DeleteProductRequest request =
           DeleteProductRequest.newBuilder()
               .setName(ProductName.of("[PROJECT]", "[LOCATION]", "[PRODUCT]").toString())
               .build();
       ApiFuture<Empty> future = productSearchClient.deleteProductCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteProductRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.DeleteProductRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteProductSet(@Nullable ProductSetName name)
    
    
    public final void deleteProductSet(@Nullable ProductSetName name)

Permanently deletes a ProductSet. Products and ReferenceImages in the ProductSet are not deleted.

The actual image files are not deleted from Google Cloud Storage.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       ProductSetName name = ProductSetName.of("[PROJECT]", "[LOCATION]", "[PRODUCT_SET]");
       productSearchClient.deleteProductSet(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.vision.v1p4beta1.ProductSetName`  
Required. Resource name of the ProductSet to delete. Format is: `projects/PROJECT_ID/locations/LOC_ID/productSets/PRODUCT_SET_ID`  
  
### deleteProductSet(DeleteProductSetRequest request)
    
    
    public final void deleteProductSet(DeleteProductSetRequest request)

Permanently deletes a ProductSet. Products and ReferenceImages in the ProductSet are not deleted.

The actual image files are not deleted from Google Cloud Storage.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       DeleteProductSetRequest request =
           DeleteProductSetRequest.newBuilder()
               .setName(ProductSetName.of("[PROJECT]", "[LOCATION]", "[PRODUCT_SET]").toString())
               .build();
       productSearchClient.deleteProductSet(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteProductSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.DeleteProductSetRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteProductSet(String name)
    
    
    public final void deleteProductSet(String name)

Permanently deletes a ProductSet. Products and ReferenceImages in the ProductSet are not deleted.

The actual image files are not deleted from Google Cloud Storage.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       String name = ProductSetName.of("[PROJECT]", "[LOCATION]", "[PRODUCT_SET]").toString();
       productSearchClient.deleteProductSet(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name of the ProductSet to delete. Format is: `projects/PROJECT_ID/locations/LOC_ID/productSets/PRODUCT_SET_ID`  
  
### deleteProductSetCallable()
    
    
    public final UnaryCallable<DeleteProductSetRequest,Empty> deleteProductSetCallable()

Permanently deletes a ProductSet. Products and ReferenceImages in the ProductSet are not deleted.

The actual image files are not deleted from Google Cloud Storage.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       DeleteProductSetRequest request =
           DeleteProductSetRequest.newBuilder()
               .setName(ProductSetName.of("[PROJECT]", "[LOCATION]", "[PRODUCT_SET]").toString())
               .build();
       ApiFuture<Empty> future = productSearchClient.deleteProductSetCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteProductSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.DeleteProductSetRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteReferenceImage(@Nullable ReferenceImageName name)
    
    
    public final void deleteReferenceImage(@Nullable ReferenceImageName name)

Permanently deletes a reference image.

The image metadata will be deleted right away, but search queries against ProductSets containing the image may still work until all related caches are refreshed.

The actual image files are not deleted from Google Cloud Storage.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       ReferenceImageName name =
           ReferenceImageName.of("[PROJECT]", "[LOCATION]", "[PRODUCT]", "[REFERENCE_IMAGE]");
       productSearchClient.deleteReferenceImage(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.vision.v1p4beta1.ReferenceImageName`  
Required. The resource name of the reference image to delete. Format is: `projects/PROJECT_ID/locations/LOC_ID/products/PRODUCT_ID/referenceImages/IMAGE_ID`  
  
### deleteReferenceImage(DeleteReferenceImageRequest request)
    
    
    public final void deleteReferenceImage(DeleteReferenceImageRequest request)

Permanently deletes a reference image.

The image metadata will be deleted right away, but search queries against ProductSets containing the image may still work until all related caches are refreshed.

The actual image files are not deleted from Google Cloud Storage.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       DeleteReferenceImageRequest request =
           DeleteReferenceImageRequest.newBuilder()
               .setName(
                   ReferenceImageName.of("[PROJECT]", "[LOCATION]", "[PRODUCT]", "[REFERENCE_IMAGE]")
                       .toString())
               .build();
       productSearchClient.deleteReferenceImage(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteReferenceImageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.DeleteReferenceImageRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteReferenceImage(String name)
    
    
    public final void deleteReferenceImage(String name)

Permanently deletes a reference image.

The image metadata will be deleted right away, but search queries against ProductSets containing the image may still work until all related caches are refreshed.

The actual image files are not deleted from Google Cloud Storage.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       String name =
           ReferenceImageName.of("[PROJECT]", "[LOCATION]", "[PRODUCT]", "[REFERENCE_IMAGE]")
               .toString();
       productSearchClient.deleteReferenceImage(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the reference image to delete. Format is: `projects/PROJECT_ID/locations/LOC_ID/products/PRODUCT_ID/referenceImages/IMAGE_ID`  
  
### deleteReferenceImageCallable()
    
    
    public final UnaryCallable<DeleteReferenceImageRequest,Empty> deleteReferenceImageCallable()

Permanently deletes a reference image.

The image metadata will be deleted right away, but search queries against ProductSets containing the image may still work until all related caches are refreshed.

The actual image files are not deleted from Google Cloud Storage.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       DeleteReferenceImageRequest request =
           DeleteReferenceImageRequest.newBuilder()
               .setName(
                   ReferenceImageName.of("[PROJECT]", "[LOCATION]", "[PRODUCT]", "[REFERENCE_IMAGE]")
                       .toString())
               .build();
       ApiFuture<Empty> future =
           productSearchClient.deleteReferenceImageCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteReferenceImageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.DeleteReferenceImageRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
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

Gets information associated with a Product.

Possible errors:

  * Returns NOT_FOUND if the Product does not exist. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       ProductName name = ProductName.of("[PROJECT]", "[LOCATION]", "[PRODUCT]");
       Product response = productSearchClient.getProduct(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.vision.v1p4beta1.ProductName`  
Required. Resource name of the Product to get. Format is: `projects/PROJECT_ID/locations/LOC_ID/products/PRODUCT_ID`  
**Returns**  
---  
**Type** | **Description**  
`[Product](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.Product)` |   
  
### getProduct(GetProductRequest request)
    
    
    public final Product getProduct(GetProductRequest request)

Gets information associated with a Product.

Possible errors:

  * Returns NOT_FOUND if the Product does not exist. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       GetProductRequest request =
           GetProductRequest.newBuilder()
               .setName(ProductName.of("[PROJECT]", "[LOCATION]", "[PRODUCT]").toString())
               .build();
       Product response = productSearchClient.getProduct(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetProductRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.GetProductRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Product](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.Product)` |   
  
### getProduct(String name)
    
    
    public final Product getProduct(String name)

Gets information associated with a Product.

Possible errors:

  * Returns NOT_FOUND if the Product does not exist. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       String name = ProductName.of("[PROJECT]", "[LOCATION]", "[PRODUCT]").toString();
       Product response = productSearchClient.getProduct(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name of the Product to get. Format is: `projects/PROJECT_ID/locations/LOC_ID/products/PRODUCT_ID`  
**Returns**  
---  
**Type** | **Description**  
`[Product](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.Product)` |   
  
### getProductCallable()
    
    
    public final UnaryCallable<GetProductRequest,Product> getProductCallable()

Gets information associated with a Product.

Possible errors:

  * Returns NOT_FOUND if the Product does not exist. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       GetProductRequest request =
           GetProductRequest.newBuilder()
               .setName(ProductName.of("[PROJECT]", "[LOCATION]", "[PRODUCT]").toString())
               .build();
       ApiFuture<Product> future = productSearchClient.getProductCallable().futureCall(request);
       // Do something.
       Product response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetProductRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.GetProductRequest),[Product](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.Product)>` |   
  
### getProductSet(@Nullable ProductSetName name)
    
    
    public final ProductSet getProductSet(@Nullable ProductSetName name)

Gets information associated with a ProductSet.

Possible errors:

  * Returns NOT_FOUND if the ProductSet does not exist. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       ProductSetName name = ProductSetName.of("[PROJECT]", "[LOCATION]", "[PRODUCT_SET]");
       ProductSet response = productSearchClient.getProductSet(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.vision.v1p4beta1.ProductSetName`  
Required. Resource name of the ProductSet to get. Format is: `projects/PROJECT_ID/locations/LOC_ID/productSets/PRODUCT_SET_ID`  
**Returns**  
---  
**Type** | **Description**  
`[ProductSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ProductSet)` |   
  
### getProductSet(GetProductSetRequest request)
    
    
    public final ProductSet getProductSet(GetProductSetRequest request)

Gets information associated with a ProductSet.

Possible errors:

  * Returns NOT_FOUND if the ProductSet does not exist. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       GetProductSetRequest request =
           GetProductSetRequest.newBuilder()
               .setName(ProductSetName.of("[PROJECT]", "[LOCATION]", "[PRODUCT_SET]").toString())
               .build();
       ProductSet response = productSearchClient.getProductSet(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetProductSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.GetProductSetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ProductSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ProductSet)` |   
  
### getProductSet(String name)
    
    
    public final ProductSet getProductSet(String name)

Gets information associated with a ProductSet.

Possible errors:

  * Returns NOT_FOUND if the ProductSet does not exist. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       String name = ProductSetName.of("[PROJECT]", "[LOCATION]", "[PRODUCT_SET]").toString();
       ProductSet response = productSearchClient.getProductSet(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name of the ProductSet to get. Format is: `projects/PROJECT_ID/locations/LOC_ID/productSets/PRODUCT_SET_ID`  
**Returns**  
---  
**Type** | **Description**  
`[ProductSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ProductSet)` |   
  
### getProductSetCallable()
    
    
    public final UnaryCallable<GetProductSetRequest,ProductSet> getProductSetCallable()

Gets information associated with a ProductSet.

Possible errors:

  * Returns NOT_FOUND if the ProductSet does not exist. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       GetProductSetRequest request =
           GetProductSetRequest.newBuilder()
               .setName(ProductSetName.of("[PROJECT]", "[LOCATION]", "[PRODUCT_SET]").toString())
               .build();
       ApiFuture<ProductSet> future =
           productSearchClient.getProductSetCallable().futureCall(request);
       // Do something.
       ProductSet response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetProductSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.GetProductSetRequest),[ProductSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ProductSet)>` |   
  
### getReferenceImage(@Nullable ReferenceImageName name)
    
    
    public final ReferenceImage getReferenceImage(@Nullable ReferenceImageName name)

Gets information associated with a ReferenceImage.

Possible errors:

  * Returns NOT_FOUND if the specified image does not exist. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       ReferenceImageName name =
           ReferenceImageName.of("[PROJECT]", "[LOCATION]", "[PRODUCT]", "[REFERENCE_IMAGE]");
       ReferenceImage response = productSearchClient.getReferenceImage(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.vision.v1p4beta1.ReferenceImageName`  
Required. The resource name of the ReferenceImage to get. Format is: `projects/PROJECT_ID/locations/LOC_ID/products/PRODUCT_ID/referenceImages/IMAGE_ID`.  
**Returns**  
---  
**Type** | **Description**  
`[ReferenceImage](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ReferenceImage)` |   
  
### getReferenceImage(GetReferenceImageRequest request)
    
    
    public final ReferenceImage getReferenceImage(GetReferenceImageRequest request)

Gets information associated with a ReferenceImage.

Possible errors:

  * Returns NOT_FOUND if the specified image does not exist. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       GetReferenceImageRequest request =
           GetReferenceImageRequest.newBuilder()
               .setName(
                   ReferenceImageName.of("[PROJECT]", "[LOCATION]", "[PRODUCT]", "[REFERENCE_IMAGE]")
                       .toString())
               .build();
       ReferenceImage response = productSearchClient.getReferenceImage(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetReferenceImageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.GetReferenceImageRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ReferenceImage](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ReferenceImage)` |   
  
### getReferenceImage(String name)
    
    
    public final ReferenceImage getReferenceImage(String name)

Gets information associated with a ReferenceImage.

Possible errors:

  * Returns NOT_FOUND if the specified image does not exist. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       String name =
           ReferenceImageName.of("[PROJECT]", "[LOCATION]", "[PRODUCT]", "[REFERENCE_IMAGE]")
               .toString();
       ReferenceImage response = productSearchClient.getReferenceImage(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the ReferenceImage to get. Format is: `projects/PROJECT_ID/locations/LOC_ID/products/PRODUCT_ID/referenceImages/IMAGE_ID`.  
**Returns**  
---  
**Type** | **Description**  
`[ReferenceImage](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ReferenceImage)` |   
  
### getReferenceImageCallable()
    
    
    public final UnaryCallable<GetReferenceImageRequest,ReferenceImage> getReferenceImageCallable()

Gets information associated with a ReferenceImage.

Possible errors:

  * Returns NOT_FOUND if the specified image does not exist. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       GetReferenceImageRequest request =
           GetReferenceImageRequest.newBuilder()
               .setName(
                   ReferenceImageName.of("[PROJECT]", "[LOCATION]", "[PRODUCT]", "[REFERENCE_IMAGE]")
                       .toString())
               .build();
       ApiFuture<ReferenceImage> future =
           productSearchClient.getReferenceImageCallable().futureCall(request);
       // Do something.
       ReferenceImage response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetReferenceImageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.GetReferenceImageRequest),[ReferenceImage](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ReferenceImage)>` |   
  
### getSettings()
    
    
    public final @Nullable ProductSearchSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.vision.v1p4beta1.ProductSearchSettings` |   
  
### getStub()
    
    
    public ProductSearchStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[ProductSearchStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.stub.ProductSearchStub)` |   
  
### importProductSetsAsync(@Nullable LocationName parent, ImportProductSetsInputConfig inputConfig)
    
    
    public final OperationFuture<ImportProductSetsResponse,BatchOperationMetadata> importProductSetsAsync(@Nullable LocationName parent, ImportProductSetsInputConfig inputConfig)

Asynchronous API that imports a list of reference images to specified product sets based on a list of image information.

The google.longrunning.Operation API can be used to keep track of the progress and results of the request. `Operation.metadata` contains `BatchOperationMetadata`. (progress) `Operation.response` contains `ImportProductSetsResponse`. (results)

The input source of this method is a csv file on Google Cloud Storage. For the format of the csv file please see ImportProductSetsGcsSource.csv_file_uri.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       ImportProductSetsInputConfig inputConfig = ImportProductSetsInputConfig.newBuilder().build();
       ImportProductSetsResponse response =
           productSearchClient.importProductSetsAsync(parent, inputConfig).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.vision.v1p4beta1.LocationName`  
Required. The project in which the ProductSets should be imported. Format is `projects/PROJECT_ID/locations/LOC_ID`.  
`inputConfig` | `[ImportProductSetsInputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ImportProductSetsInputConfig)`  
Required. The input content for the list of requests.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ImportProductSetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ImportProductSetsResponse),[BatchOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.BatchOperationMetadata)>` |   
  
### importProductSetsAsync(ImportProductSetsRequest request)
    
    
    public final OperationFuture<ImportProductSetsResponse,BatchOperationMetadata> importProductSetsAsync(ImportProductSetsRequest request)

Asynchronous API that imports a list of reference images to specified product sets based on a list of image information.

The google.longrunning.Operation API can be used to keep track of the progress and results of the request. `Operation.metadata` contains `BatchOperationMetadata`. (progress) `Operation.response` contains `ImportProductSetsResponse`. (results)

The input source of this method is a csv file on Google Cloud Storage. For the format of the csv file please see ImportProductSetsGcsSource.csv_file_uri.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       ImportProductSetsRequest request =
           ImportProductSetsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setInputConfig(ImportProductSetsInputConfig.newBuilder().build())
               .build();
       ImportProductSetsResponse response =
           productSearchClient.importProductSetsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ImportProductSetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ImportProductSetsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ImportProductSetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ImportProductSetsResponse),[BatchOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.BatchOperationMetadata)>` |   
  
### importProductSetsAsync(String parent, ImportProductSetsInputConfig inputConfig)
    
    
    public final OperationFuture<ImportProductSetsResponse,BatchOperationMetadata> importProductSetsAsync(String parent, ImportProductSetsInputConfig inputConfig)

Asynchronous API that imports a list of reference images to specified product sets based on a list of image information.

The google.longrunning.Operation API can be used to keep track of the progress and results of the request. `Operation.metadata` contains `BatchOperationMetadata`. (progress) `Operation.response` contains `ImportProductSetsResponse`. (results)

The input source of this method is a csv file on Google Cloud Storage. For the format of the csv file please see ImportProductSetsGcsSource.csv_file_uri.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       ImportProductSetsInputConfig inputConfig = ImportProductSetsInputConfig.newBuilder().build();
       ImportProductSetsResponse response =
           productSearchClient.importProductSetsAsync(parent, inputConfig).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project in which the ProductSets should be imported. Format is `projects/PROJECT_ID/locations/LOC_ID`.  
`inputConfig` | `[ImportProductSetsInputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ImportProductSetsInputConfig)`  
Required. The input content for the list of requests.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ImportProductSetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ImportProductSetsResponse),[BatchOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.BatchOperationMetadata)>` |   
  
### importProductSetsCallable()
    
    
    public final UnaryCallable<ImportProductSetsRequest,Operation> importProductSetsCallable()

Asynchronous API that imports a list of reference images to specified product sets based on a list of image information.

The google.longrunning.Operation API can be used to keep track of the progress and results of the request. `Operation.metadata` contains `BatchOperationMetadata`. (progress) `Operation.response` contains `ImportProductSetsResponse`. (results)

The input source of this method is a csv file on Google Cloud Storage. For the format of the csv file please see ImportProductSetsGcsSource.csv_file_uri.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       ImportProductSetsRequest request =
           ImportProductSetsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setInputConfig(ImportProductSetsInputConfig.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           productSearchClient.importProductSetsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ImportProductSetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ImportProductSetsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### importProductSetsOperationCallable()
    
    
    public final OperationCallable<ImportProductSetsRequest,ImportProductSetsResponse,BatchOperationMetadata> importProductSetsOperationCallable()

Asynchronous API that imports a list of reference images to specified product sets based on a list of image information.

The google.longrunning.Operation API can be used to keep track of the progress and results of the request. `Operation.metadata` contains `BatchOperationMetadata`. (progress) `Operation.response` contains `ImportProductSetsResponse`. (results)

The input source of this method is a csv file on Google Cloud Storage. For the format of the csv file please see ImportProductSetsGcsSource.csv_file_uri.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       ImportProductSetsRequest request =
           ImportProductSetsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setInputConfig(ImportProductSetsInputConfig.newBuilder().build())
               .build();
       OperationFuture<ImportProductSetsResponse, BatchOperationMetadata> future =
           productSearchClient.importProductSetsOperationCallable().futureCall(request);
       // Do something.
       ImportProductSetsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ImportProductSetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ImportProductSetsRequest),[ImportProductSetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ImportProductSetsResponse),[BatchOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.BatchOperationMetadata)>` |   
  
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
  
### listProductSets(@Nullable LocationName parent)
    
    
    public final ProductSearchClient.ListProductSetsPagedResponse listProductSets(@Nullable LocationName parent)

Lists ProductSets in an unspecified order.

Possible errors:

  * Returns INVALID_ARGUMENT if page_size is greater than 100, or less than 1. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (ProductSet element : productSearchClient.listProductSets(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.vision.v1p4beta1.LocationName`  
Required. The project from which ProductSets should be listed. Format is `projects/PROJECT_ID/locations/LOC_ID`.  
**Returns**  
---  
**Type** | **Description**  
`[ProductSearchClient.ListProductSetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ProductSearchClient.ListProductSetsPagedResponse)` |   
  
### listProductSets(ListProductSetsRequest request)
    
    
    public final ProductSearchClient.ListProductSetsPagedResponse listProductSets(ListProductSetsRequest request)

Lists ProductSets in an unspecified order.

Possible errors:

  * Returns INVALID_ARGUMENT if page_size is greater than 100, or less than 1. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       ListProductSetsRequest request =
           ListProductSetsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (ProductSet element : productSearchClient.listProductSets(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListProductSetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ListProductSetsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ProductSearchClient.ListProductSetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ProductSearchClient.ListProductSetsPagedResponse)` |   
  
### listProductSets(String parent)
    
    
    public final ProductSearchClient.ListProductSetsPagedResponse listProductSets(String parent)

Lists ProductSets in an unspecified order.

Possible errors:

  * Returns INVALID_ARGUMENT if page_size is greater than 100, or less than 1. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (ProductSet element : productSearchClient.listProductSets(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project from which ProductSets should be listed. Format is `projects/PROJECT_ID/locations/LOC_ID`.  
**Returns**  
---  
**Type** | **Description**  
`[ProductSearchClient.ListProductSetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ProductSearchClient.ListProductSetsPagedResponse)` |   
  
### listProductSetsCallable()
    
    
    public final UnaryCallable<ListProductSetsRequest,ListProductSetsResponse> listProductSetsCallable()

Lists ProductSets in an unspecified order.

Possible errors:

  * Returns INVALID_ARGUMENT if page_size is greater than 100, or less than 1. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       ListProductSetsRequest request =
           ListProductSetsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListProductSetsResponse response =
             productSearchClient.listProductSetsCallable().call(request);
         for (ProductSet element : response.getProductSetsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListProductSetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ListProductSetsRequest),[ListProductSetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ListProductSetsResponse)>` |   
  
### listProductSetsPagedCallable()
    
    
    public final UnaryCallable<ListProductSetsRequest,ProductSearchClient.ListProductSetsPagedResponse> listProductSetsPagedCallable()

Lists ProductSets in an unspecified order.

Possible errors:

  * Returns INVALID_ARGUMENT if page_size is greater than 100, or less than 1. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       ListProductSetsRequest request =
           ListProductSetsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<ProductSet> future =
           productSearchClient.listProductSetsPagedCallable().futureCall(request);
       // Do something.
       for (ProductSet element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListProductSetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ListProductSetsRequest),[ListProductSetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ProductSearchClient.ListProductSetsPagedResponse)>` |   
  
### listProducts(@Nullable LocationName parent)
    
    
    public final ProductSearchClient.ListProductsPagedResponse listProducts(@Nullable LocationName parent)

Lists products in an unspecified order.

Possible errors:

  * Returns INVALID_ARGUMENT if page_size is greater than 100 or less than 1. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Product element : productSearchClient.listProducts(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.vision.v1p4beta1.LocationName`  
Required. The project OR ProductSet from which Products should be listed. Format: `projects/PROJECT_ID/locations/LOC_ID`  
**Returns**  
---  
**Type** | **Description**  
`[ProductSearchClient.ListProductsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ProductSearchClient.ListProductsPagedResponse)` |   
  
### listProducts(ListProductsRequest request)
    
    
    public final ProductSearchClient.ListProductsPagedResponse listProducts(ListProductsRequest request)

Lists products in an unspecified order.

Possible errors:

  * Returns INVALID_ARGUMENT if page_size is greater than 100 or less than 1. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       ListProductsRequest request =
           ListProductsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Product element : productSearchClient.listProducts(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListProductsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ListProductsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ProductSearchClient.ListProductsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ProductSearchClient.ListProductsPagedResponse)` |   
  
### listProducts(String parent)
    
    
    public final ProductSearchClient.ListProductsPagedResponse listProducts(String parent)

Lists products in an unspecified order.

Possible errors:

  * Returns INVALID_ARGUMENT if page_size is greater than 100 or less than 1. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Product element : productSearchClient.listProducts(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project OR ProductSet from which Products should be listed. Format: `projects/PROJECT_ID/locations/LOC_ID`  
**Returns**  
---  
**Type** | **Description**  
`[ProductSearchClient.ListProductsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ProductSearchClient.ListProductsPagedResponse)` |   
  
### listProductsCallable()
    
    
    public final UnaryCallable<ListProductsRequest,ListProductsResponse> listProductsCallable()

Lists products in an unspecified order.

Possible errors:

  * Returns INVALID_ARGUMENT if page_size is greater than 100 or less than 1. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       ListProductsRequest request =
           ListProductsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListProductsResponse response = productSearchClient.listProductsCallable().call(request);
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListProductsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ListProductsRequest),[ListProductsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ListProductsResponse)>` |   
  
### listProductsInProductSet(@Nullable ProductSetName name)
    
    
    public final ProductSearchClient.ListProductsInProductSetPagedResponse listProductsInProductSet(@Nullable ProductSetName name)

Lists the Products in a ProductSet, in an unspecified order. If the ProductSet does not exist, the products field of the response will be empty.

Possible errors:

  * Returns INVALID_ARGUMENT if page_size is greater than 100 or less than 1. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       ProductSetName name = ProductSetName.of("[PROJECT]", "[LOCATION]", "[PRODUCT_SET]");
       for (Product element : productSearchClient.listProductsInProductSet(name).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.vision.v1p4beta1.ProductSetName`  
Required. The ProductSet resource for which to retrieve Products. Format is: `projects/PROJECT_ID/locations/LOC_ID/productSets/PRODUCT_SET_ID`  
**Returns**  
---  
**Type** | **Description**  
`[ProductSearchClient.ListProductsInProductSetPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ProductSearchClient.ListProductsInProductSetPagedResponse)` |   
  
### listProductsInProductSet(ListProductsInProductSetRequest request)
    
    
    public final ProductSearchClient.ListProductsInProductSetPagedResponse listProductsInProductSet(ListProductsInProductSetRequest request)

Lists the Products in a ProductSet, in an unspecified order. If the ProductSet does not exist, the products field of the response will be empty.

Possible errors:

  * Returns INVALID_ARGUMENT if page_size is greater than 100 or less than 1. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       ListProductsInProductSetRequest request =
           ListProductsInProductSetRequest.newBuilder()
               .setName(ProductSetName.of("[PROJECT]", "[LOCATION]", "[PRODUCT_SET]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Product element : productSearchClient.listProductsInProductSet(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListProductsInProductSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ListProductsInProductSetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ProductSearchClient.ListProductsInProductSetPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ProductSearchClient.ListProductsInProductSetPagedResponse)` |   
  
### listProductsInProductSet(String name)
    
    
    public final ProductSearchClient.ListProductsInProductSetPagedResponse listProductsInProductSet(String name)

Lists the Products in a ProductSet, in an unspecified order. If the ProductSet does not exist, the products field of the response will be empty.

Possible errors:

  * Returns INVALID_ARGUMENT if page_size is greater than 100 or less than 1. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       String name = ProductSetName.of("[PROJECT]", "[LOCATION]", "[PRODUCT_SET]").toString();
       for (Product element : productSearchClient.listProductsInProductSet(name).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ProductSet resource for which to retrieve Products. Format is: `projects/PROJECT_ID/locations/LOC_ID/productSets/PRODUCT_SET_ID`  
**Returns**  
---  
**Type** | **Description**  
`[ProductSearchClient.ListProductsInProductSetPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ProductSearchClient.ListProductsInProductSetPagedResponse)` |   
  
### listProductsInProductSetCallable()
    
    
    public final UnaryCallable<ListProductsInProductSetRequest,ListProductsInProductSetResponse> listProductsInProductSetCallable()

Lists the Products in a ProductSet, in an unspecified order. If the ProductSet does not exist, the products field of the response will be empty.

Possible errors:

  * Returns INVALID_ARGUMENT if page_size is greater than 100 or less than 1. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       ListProductsInProductSetRequest request =
           ListProductsInProductSetRequest.newBuilder()
               .setName(ProductSetName.of("[PROJECT]", "[LOCATION]", "[PRODUCT_SET]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListProductsInProductSetResponse response =
             productSearchClient.listProductsInProductSetCallable().call(request);
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListProductsInProductSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ListProductsInProductSetRequest),[ListProductsInProductSetResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ListProductsInProductSetResponse)>` |   
  
### listProductsInProductSetPagedCallable()
    
    
    public final UnaryCallable<ListProductsInProductSetRequest,ProductSearchClient.ListProductsInProductSetPagedResponse> listProductsInProductSetPagedCallable()

Lists the Products in a ProductSet, in an unspecified order. If the ProductSet does not exist, the products field of the response will be empty.

Possible errors:

  * Returns INVALID_ARGUMENT if page_size is greater than 100 or less than 1. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       ListProductsInProductSetRequest request =
           ListProductsInProductSetRequest.newBuilder()
               .setName(ProductSetName.of("[PROJECT]", "[LOCATION]", "[PRODUCT_SET]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Product> future =
           productSearchClient.listProductsInProductSetPagedCallable().futureCall(request);
       // Do something.
       for (Product element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListProductsInProductSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ListProductsInProductSetRequest),[ListProductsInProductSetPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ProductSearchClient.ListProductsInProductSetPagedResponse)>` |   
  
### listProductsPagedCallable()
    
    
    public final UnaryCallable<ListProductsRequest,ProductSearchClient.ListProductsPagedResponse> listProductsPagedCallable()

Lists products in an unspecified order.

Possible errors:

  * Returns INVALID_ARGUMENT if page_size is greater than 100 or less than 1. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       ListProductsRequest request =
           ListProductsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Product> future =
           productSearchClient.listProductsPagedCallable().futureCall(request);
       // Do something.
       for (Product element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListProductsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ListProductsRequest),[ListProductsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ProductSearchClient.ListProductsPagedResponse)>` |   
  
### listReferenceImages(@Nullable ProductName parent)
    
    
    public final ProductSearchClient.ListReferenceImagesPagedResponse listReferenceImages(@Nullable ProductName parent)

Lists reference images.

Possible errors:

  * Returns NOT_FOUND if the parent product does not exist. 
  * Returns INVALID_ARGUMENT if the page_size is greater than 100, or less than 1. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       ProductName parent = ProductName.of("[PROJECT]", "[LOCATION]", "[PRODUCT]");
       for (ReferenceImage element : productSearchClient.listReferenceImages(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.vision.v1p4beta1.ProductName`  
Required. Resource name of the product containing the reference images. Format is `projects/PROJECT_ID/locations/LOC_ID/products/PRODUCT_ID`.  
**Returns**  
---  
**Type** | **Description**  
`[ProductSearchClient.ListReferenceImagesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ProductSearchClient.ListReferenceImagesPagedResponse)` |   
  
### listReferenceImages(ListReferenceImagesRequest request)
    
    
    public final ProductSearchClient.ListReferenceImagesPagedResponse listReferenceImages(ListReferenceImagesRequest request)

Lists reference images.

Possible errors:

  * Returns NOT_FOUND if the parent product does not exist. 
  * Returns INVALID_ARGUMENT if the page_size is greater than 100, or less than 1. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       ListReferenceImagesRequest request =
           ListReferenceImagesRequest.newBuilder()
               .setParent(ProductName.of("[PROJECT]", "[LOCATION]", "[PRODUCT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (ReferenceImage element : productSearchClient.listReferenceImages(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListReferenceImagesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ListReferenceImagesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ProductSearchClient.ListReferenceImagesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ProductSearchClient.ListReferenceImagesPagedResponse)` |   
  
### listReferenceImages(String parent)
    
    
    public final ProductSearchClient.ListReferenceImagesPagedResponse listReferenceImages(String parent)

Lists reference images.

Possible errors:

  * Returns NOT_FOUND if the parent product does not exist. 
  * Returns INVALID_ARGUMENT if the page_size is greater than 100, or less than 1. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       String parent = ProductName.of("[PROJECT]", "[LOCATION]", "[PRODUCT]").toString();
       for (ReferenceImage element : productSearchClient.listReferenceImages(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name of the product containing the reference images. Format is `projects/PROJECT_ID/locations/LOC_ID/products/PRODUCT_ID`.  
**Returns**  
---  
**Type** | **Description**  
`[ProductSearchClient.ListReferenceImagesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ProductSearchClient.ListReferenceImagesPagedResponse)` |   
  
### listReferenceImagesCallable()
    
    
    public final UnaryCallable<ListReferenceImagesRequest,ListReferenceImagesResponse> listReferenceImagesCallable()

Lists reference images.

Possible errors:

  * Returns NOT_FOUND if the parent product does not exist. 
  * Returns INVALID_ARGUMENT if the page_size is greater than 100, or less than 1. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       ListReferenceImagesRequest request =
           ListReferenceImagesRequest.newBuilder()
               .setParent(ProductName.of("[PROJECT]", "[LOCATION]", "[PRODUCT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListReferenceImagesResponse response =
             productSearchClient.listReferenceImagesCallable().call(request);
         for (ReferenceImage element : response.getReferenceImagesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListReferenceImagesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ListReferenceImagesRequest),[ListReferenceImagesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ListReferenceImagesResponse)>` |   
  
### listReferenceImagesPagedCallable()
    
    
    public final UnaryCallable<ListReferenceImagesRequest,ProductSearchClient.ListReferenceImagesPagedResponse> listReferenceImagesPagedCallable()

Lists reference images.

Possible errors:

  * Returns NOT_FOUND if the parent product does not exist. 
  * Returns INVALID_ARGUMENT if the page_size is greater than 100, or less than 1. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       ListReferenceImagesRequest request =
           ListReferenceImagesRequest.newBuilder()
               .setParent(ProductName.of("[PROJECT]", "[LOCATION]", "[PRODUCT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<ReferenceImage> future =
           productSearchClient.listReferenceImagesPagedCallable().futureCall(request);
       // Do something.
       for (ReferenceImage element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListReferenceImagesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ListReferenceImagesRequest),[ListReferenceImagesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ProductSearchClient.ListReferenceImagesPagedResponse)>` |   
  
### purgeProductsAsync(@Nullable LocationName parent)
    
    
    public final OperationFuture<Empty,BatchOperationMetadata> purgeProductsAsync(@Nullable LocationName parent)

Asynchronous API to delete all Products in a ProductSet or all Products that are in no ProductSet.

If a Product is a member of the specified ProductSet in addition to other ProductSets, the Product will still be deleted.

It is recommended to not delete the specified ProductSet until after this operation has completed. It is also recommended to not add any of the Products involved in the batch delete to a new ProductSet while this operation is running because those Products may still end up deleted.

It's not possible to undo the PurgeProducts operation. Therefore, it is recommended to keep the csv files used in ImportProductSets (if that was how you originally built the Product Set) before starting PurgeProducts, in case you need to re-import the data after deletion.

If the plan is to purge all of the Products from a ProductSet and then re-use the empty ProductSet to re-import new Products into the empty ProductSet, you must wait until the PurgeProducts operation has finished for that ProductSet.

The google.longrunning.Operation API can be used to keep track of the progress and results of the request. `Operation.metadata` contains `BatchOperationMetadata`. (progress)

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       productSearchClient.purgeProductsAsync(parent).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.vision.v1p4beta1.LocationName`  
Required. The project and location in which the Products should be deleted. Format is `projects/PROJECT_ID/locations/LOC_ID`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[BatchOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.BatchOperationMetadata)>` |   
  
### purgeProductsAsync(PurgeProductsRequest request)
    
    
    public final OperationFuture<Empty,BatchOperationMetadata> purgeProductsAsync(PurgeProductsRequest request)

Asynchronous API to delete all Products in a ProductSet or all Products that are in no ProductSet.

If a Product is a member of the specified ProductSet in addition to other ProductSets, the Product will still be deleted.

It is recommended to not delete the specified ProductSet until after this operation has completed. It is also recommended to not add any of the Products involved in the batch delete to a new ProductSet while this operation is running because those Products may still end up deleted.

It's not possible to undo the PurgeProducts operation. Therefore, it is recommended to keep the csv files used in ImportProductSets (if that was how you originally built the Product Set) before starting PurgeProducts, in case you need to re-import the data after deletion.

If the plan is to purge all of the Products from a ProductSet and then re-use the empty ProductSet to re-import new Products into the empty ProductSet, you must wait until the PurgeProducts operation has finished for that ProductSet.

The google.longrunning.Operation API can be used to keep track of the progress and results of the request. `Operation.metadata` contains `BatchOperationMetadata`. (progress)

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       PurgeProductsRequest request =
           PurgeProductsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setForce(true)
               .build();
       productSearchClient.purgeProductsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PurgeProductsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.PurgeProductsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[BatchOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.BatchOperationMetadata)>` |   
  
### purgeProductsAsync(String parent)
    
    
    public final OperationFuture<Empty,BatchOperationMetadata> purgeProductsAsync(String parent)

Asynchronous API to delete all Products in a ProductSet or all Products that are in no ProductSet.

If a Product is a member of the specified ProductSet in addition to other ProductSets, the Product will still be deleted.

It is recommended to not delete the specified ProductSet until after this operation has completed. It is also recommended to not add any of the Products involved in the batch delete to a new ProductSet while this operation is running because those Products may still end up deleted.

It's not possible to undo the PurgeProducts operation. Therefore, it is recommended to keep the csv files used in ImportProductSets (if that was how you originally built the Product Set) before starting PurgeProducts, in case you need to re-import the data after deletion.

If the plan is to purge all of the Products from a ProductSet and then re-use the empty ProductSet to re-import new Products into the empty ProductSet, you must wait until the PurgeProducts operation has finished for that ProductSet.

The google.longrunning.Operation API can be used to keep track of the progress and results of the request. `Operation.metadata` contains `BatchOperationMetadata`. (progress)

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       productSearchClient.purgeProductsAsync(parent).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location in which the Products should be deleted. Format is `projects/PROJECT_ID/locations/LOC_ID`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[BatchOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.BatchOperationMetadata)>` |   
  
### purgeProductsCallable()
    
    
    public final UnaryCallable<PurgeProductsRequest,Operation> purgeProductsCallable()

Asynchronous API to delete all Products in a ProductSet or all Products that are in no ProductSet.

If a Product is a member of the specified ProductSet in addition to other ProductSets, the Product will still be deleted.

It is recommended to not delete the specified ProductSet until after this operation has completed. It is also recommended to not add any of the Products involved in the batch delete to a new ProductSet while this operation is running because those Products may still end up deleted.

It's not possible to undo the PurgeProducts operation. Therefore, it is recommended to keep the csv files used in ImportProductSets (if that was how you originally built the Product Set) before starting PurgeProducts, in case you need to re-import the data after deletion.

If the plan is to purge all of the Products from a ProductSet and then re-use the empty ProductSet to re-import new Products into the empty ProductSet, you must wait until the PurgeProducts operation has finished for that ProductSet.

The google.longrunning.Operation API can be used to keep track of the progress and results of the request. `Operation.metadata` contains `BatchOperationMetadata`. (progress)

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       PurgeProductsRequest request =
           PurgeProductsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setForce(true)
               .build();
       ApiFuture<Operation> future = productSearchClient.purgeProductsCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PurgeProductsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.PurgeProductsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### purgeProductsOperationCallable()
    
    
    public final OperationCallable<PurgeProductsRequest,Empty,BatchOperationMetadata> purgeProductsOperationCallable()

Asynchronous API to delete all Products in a ProductSet or all Products that are in no ProductSet.

If a Product is a member of the specified ProductSet in addition to other ProductSets, the Product will still be deleted.

It is recommended to not delete the specified ProductSet until after this operation has completed. It is also recommended to not add any of the Products involved in the batch delete to a new ProductSet while this operation is running because those Products may still end up deleted.

It's not possible to undo the PurgeProducts operation. Therefore, it is recommended to keep the csv files used in ImportProductSets (if that was how you originally built the Product Set) before starting PurgeProducts, in case you need to re-import the data after deletion.

If the plan is to purge all of the Products from a ProductSet and then re-use the empty ProductSet to re-import new Products into the empty ProductSet, you must wait until the PurgeProducts operation has finished for that ProductSet.

The google.longrunning.Operation API can be used to keep track of the progress and results of the request. `Operation.metadata` contains `BatchOperationMetadata`. (progress)

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       PurgeProductsRequest request =
           PurgeProductsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setForce(true)
               .build();
       OperationFuture<Empty, BatchOperationMetadata> future =
           productSearchClient.purgeProductsOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PurgeProductsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.PurgeProductsRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[BatchOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.BatchOperationMetadata)>` |   
  
### removeProductFromProductSet(@Nullable ProductSetName name, @Nullable ProductName product)
    
    
    public final void removeProductFromProductSet(@Nullable ProductSetName name, @Nullable ProductName product)

Removes a Product from the specified ProductSet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       ProductSetName name = ProductSetName.of("[PROJECT]", "[LOCATION]", "[PRODUCT_SET]");
       ProductName product = ProductName.of("[PROJECT]", "[LOCATION]", "[PRODUCT]");
       productSearchClient.removeProductFromProductSet(name, product);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.vision.v1p4beta1.ProductSetName`  
Required. The resource name for the ProductSet to modify. Format is: `projects/PROJECT_ID/locations/LOC_ID/productSets/PRODUCT_SET_ID`  
`product` | `@org.jspecify.annotations.Nullable com.google.cloud.vision.v1p4beta1.ProductName`  
Required. The resource name for the Product to be removed from this ProductSet. Format is: `projects/PROJECT_ID/locations/LOC_ID/products/PRODUCT_ID`  
  
### removeProductFromProductSet(@Nullable ProductSetName name, String product)
    
    
    public final void removeProductFromProductSet(@Nullable ProductSetName name, String product)

Removes a Product from the specified ProductSet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       ProductSetName name = ProductSetName.of("[PROJECT]", "[LOCATION]", "[PRODUCT_SET]");
       String product = ProductName.of("[PROJECT]", "[LOCATION]", "[PRODUCT]").toString();
       productSearchClient.removeProductFromProductSet(name, product);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.vision.v1p4beta1.ProductSetName`  
Required. The resource name for the ProductSet to modify. Format is: `projects/PROJECT_ID/locations/LOC_ID/productSets/PRODUCT_SET_ID`  
`product` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name for the Product to be removed from this ProductSet. Format is: `projects/PROJECT_ID/locations/LOC_ID/products/PRODUCT_ID`  
  
### removeProductFromProductSet(RemoveProductFromProductSetRequest request)
    
    
    public final void removeProductFromProductSet(RemoveProductFromProductSetRequest request)

Removes a Product from the specified ProductSet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       RemoveProductFromProductSetRequest request =
           RemoveProductFromProductSetRequest.newBuilder()
               .setName(ProductSetName.of("[PROJECT]", "[LOCATION]", "[PRODUCT_SET]").toString())
               .setProduct(ProductName.of("[PROJECT]", "[LOCATION]", "[PRODUCT]").toString())
               .build();
       productSearchClient.removeProductFromProductSet(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RemoveProductFromProductSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.RemoveProductFromProductSetRequest)`  
The request object containing all of the parameters for the API call.  
  
### removeProductFromProductSet(String name, @Nullable ProductName product)
    
    
    public final void removeProductFromProductSet(String name, @Nullable ProductName product)

Removes a Product from the specified ProductSet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       String name = ProductSetName.of("[PROJECT]", "[LOCATION]", "[PRODUCT_SET]").toString();
       ProductName product = ProductName.of("[PROJECT]", "[LOCATION]", "[PRODUCT]");
       productSearchClient.removeProductFromProductSet(name, product);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name for the ProductSet to modify. Format is: `projects/PROJECT_ID/locations/LOC_ID/productSets/PRODUCT_SET_ID`  
`product` | `@org.jspecify.annotations.Nullable com.google.cloud.vision.v1p4beta1.ProductName`  
Required. The resource name for the Product to be removed from this ProductSet. Format is: `projects/PROJECT_ID/locations/LOC_ID/products/PRODUCT_ID`  
  
### removeProductFromProductSet(String name, String product)
    
    
    public final void removeProductFromProductSet(String name, String product)

Removes a Product from the specified ProductSet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       String name = ProductSetName.of("[PROJECT]", "[LOCATION]", "[PRODUCT_SET]").toString();
       String product = ProductName.of("[PROJECT]", "[LOCATION]", "[PRODUCT]").toString();
       productSearchClient.removeProductFromProductSet(name, product);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name for the ProductSet to modify. Format is: `projects/PROJECT_ID/locations/LOC_ID/productSets/PRODUCT_SET_ID`  
`product` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name for the Product to be removed from this ProductSet. Format is: `projects/PROJECT_ID/locations/LOC_ID/products/PRODUCT_ID`  
  
### removeProductFromProductSetCallable()
    
    
    public final UnaryCallable<RemoveProductFromProductSetRequest,Empty> removeProductFromProductSetCallable()

Removes a Product from the specified ProductSet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       RemoveProductFromProductSetRequest request =
           RemoveProductFromProductSetRequest.newBuilder()
               .setName(ProductSetName.of("[PROJECT]", "[LOCATION]", "[PRODUCT_SET]").toString())
               .setProduct(ProductName.of("[PROJECT]", "[LOCATION]", "[PRODUCT]").toString())
               .build();
       ApiFuture<Empty> future =
           productSearchClient.removeProductFromProductSetCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RemoveProductFromProductSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.RemoveProductFromProductSetRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateProduct(Product product, FieldMask updateMask)
    
    
    public final Product updateProduct(Product product, FieldMask updateMask)

Makes changes to a Product resource. Only the `display_name`, `description`, and `labels` fields can be updated right now.

If labels are updated, the change will not be reflected in queries until the next index time.

Possible errors:

  * Returns NOT_FOUND if the Product does not exist. 
  * Returns INVALID_ARGUMENT if display_name is present in update_mask but is missing from the request or longer than 4096 characters. 
  * Returns INVALID_ARGUMENT if description is present in update_mask but is longer than 4096 characters. 
  * Returns INVALID_ARGUMENT if product_category is present in update_mask. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       Product product = Product.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Product response = productSearchClient.updateProduct(product, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`product` | `[Product](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.Product)`  
Required. The Product resource which replaces the one on the server. product.name is immutable.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
The FieldMask that specifies which fields to update. If update_mask isn't specified, all mutable fields are to be updated. Valid mask paths include `product_labels`, `display_name`, and `description`.  
**Returns**  
---  
**Type** | **Description**  
`[Product](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.Product)` |   
  
### updateProduct(UpdateProductRequest request)
    
    
    public final Product updateProduct(UpdateProductRequest request)

Makes changes to a Product resource. Only the `display_name`, `description`, and `labels` fields can be updated right now.

If labels are updated, the change will not be reflected in queries until the next index time.

Possible errors:

  * Returns NOT_FOUND if the Product does not exist. 
  * Returns INVALID_ARGUMENT if display_name is present in update_mask but is missing from the request or longer than 4096 characters. 
  * Returns INVALID_ARGUMENT if description is present in update_mask but is longer than 4096 characters. 
  * Returns INVALID_ARGUMENT if product_category is present in update_mask. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       UpdateProductRequest request =
           UpdateProductRequest.newBuilder()
               .setProduct(Product.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Product response = productSearchClient.updateProduct(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateProductRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.UpdateProductRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Product](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.Product)` |   
  
### updateProductCallable()
    
    
    public final UnaryCallable<UpdateProductRequest,Product> updateProductCallable()

Makes changes to a Product resource. Only the `display_name`, `description`, and `labels` fields can be updated right now.

If labels are updated, the change will not be reflected in queries until the next index time.

Possible errors:

  * Returns NOT_FOUND if the Product does not exist. 
  * Returns INVALID_ARGUMENT if display_name is present in update_mask but is missing from the request or longer than 4096 characters. 
  * Returns INVALID_ARGUMENT if description is present in update_mask but is longer than 4096 characters. 
  * Returns INVALID_ARGUMENT if product_category is present in update_mask. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       UpdateProductRequest request =
           UpdateProductRequest.newBuilder()
               .setProduct(Product.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Product> future = productSearchClient.updateProductCallable().futureCall(request);
       // Do something.
       Product response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateProductRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.UpdateProductRequest),[Product](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.Product)>` |   
  
### updateProductSet(ProductSet productSet, FieldMask updateMask)
    
    
    public final ProductSet updateProductSet(ProductSet productSet, FieldMask updateMask)

Makes changes to a ProductSet resource. Only display_name can be updated currently.

Possible errors:

  * Returns NOT_FOUND if the ProductSet does not exist. 
  * Returns INVALID_ARGUMENT if display_name is present in update_mask but missing from the request or longer than 4096 characters. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       ProductSet productSet = ProductSet.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       ProductSet response = productSearchClient.updateProductSet(productSet, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`productSet` | `[ProductSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ProductSet)`  
Required. The ProductSet resource which replaces the one on the server.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
The FieldMask that specifies which fields to update. If update_mask isn't specified, all mutable fields are to be updated. Valid mask path is `display_name`.  
**Returns**  
---  
**Type** | **Description**  
`[ProductSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ProductSet)` |   
  
### updateProductSet(UpdateProductSetRequest request)
    
    
    public final ProductSet updateProductSet(UpdateProductSetRequest request)

Makes changes to a ProductSet resource. Only display_name can be updated currently.

Possible errors:

  * Returns NOT_FOUND if the ProductSet does not exist. 
  * Returns INVALID_ARGUMENT if display_name is present in update_mask but missing from the request or longer than 4096 characters. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       UpdateProductSetRequest request =
           UpdateProductSetRequest.newBuilder()
               .setProductSet(ProductSet.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ProductSet response = productSearchClient.updateProductSet(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateProductSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.UpdateProductSetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ProductSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ProductSet)` |   
  
### updateProductSetCallable()
    
    
    public final UnaryCallable<UpdateProductSetRequest,ProductSet> updateProductSetCallable()

Makes changes to a ProductSet resource. Only display_name can be updated currently.

Possible errors:

  * Returns NOT_FOUND if the ProductSet does not exist. 
  * Returns INVALID_ARGUMENT if display_name is present in update_mask but missing from the request or longer than 4096 characters. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProductSearchClient productSearchClient = ProductSearchClient.create()) {
       UpdateProductSetRequest request =
           UpdateProductSetRequest.newBuilder()
               .setProductSet(ProductSet.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<ProductSet> future =
           productSearchClient.updateProductSetCallable().futureCall(request);
       // Do something.
       ProductSet response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateProductSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.UpdateProductSetRequest),[ProductSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p4beta1.ProductSet)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
