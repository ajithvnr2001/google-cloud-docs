---
url: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1.RegionalInventoryServiceClient
title: Class RegionalInventoryServiceClient (1.27.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:18:06.225671+00:00
---

# Class RegionalInventoryServiceClient (1.27.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1.RegionalInventoryServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class RegionalInventoryServiceClient (1.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.27.0 (latest)  1.23.0  1.22.0  1.21.0  1.19.0  1.16.0  1.15.0  1.13.0  1.11.0  1.10.0  1.8.0  1.6.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.46.0  0.44.0  0.43.0  0.40.0  0.39.0  0.38.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-shopping-merchant-inventories/google-shopping-merchant-inventories/src/main/java/com/google/shopping/merchant/inventories/v1/RegionalInventoryServiceClient.java)| [Product Reference](https://developers.google.com/merchant/api)  
---|---  
  
Service Description: Service to manage regional inventory for products. There is also separate `regions` resource and API to manage regions definitions.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionalInventoryServiceClient regionalInventoryServiceClient =
         RegionalInventoryServiceClient.create()) {
       InsertRegionalInventoryRequest request =
           InsertRegionalInventoryRequest.newBuilder()
               .setParent(ProductName.of("[ACCOUNT]", "[PRODUCT]").toString())
               .setRegionalInventory(RegionalInventory.newBuilder().build())
               .build();
       RegionalInventory response = regionalInventoryServiceClient.insertRegionalInventory(request);
     }
     

Note: close() needs to be called on the RegionalInventoryServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListRegionalInventories |  Lists the `RegionalInventory` resources for the given product in your merchant account. The response might contain fewer items than specified by `pageSize`. If `pageToken` was returned in previous request, it can be used to obtain additional results.  `RegionalInventory` resources are listed per product for a given account. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listRegionalInventories(ListRegionalInventoriesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listRegionalInventories(ProductName parent) 
  * listRegionalInventories(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listRegionalInventoriesPagedCallable() 
  * listRegionalInventoriesCallable() 

  
InsertRegionalInventory |  Inserts a `RegionalInventory` to a given product in your merchant account.  Replaces the full `RegionalInventory` resource if an entry with the same `region` already exists for the product.  It might take up to 30 minutes for the new or updated `RegionalInventory` resource to appear in products. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertRegionalInventory(InsertRegionalInventoryRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertRegionalInventoryCallable() 

  
DeleteRegionalInventory |  Deletes the specified `RegionalInventory` resource from the given product in your merchant account. It might take up to an hour for the `RegionalInventory` to be deleted from the specific product. Once you have received a successful delete response, wait for that period before attempting a delete again. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteRegionalInventory(DeleteRegionalInventoryRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteRegionalInventory(RegionalInventoryName name) 
  * deleteRegionalInventory(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteRegionalInventoryCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of RegionalInventoryServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RegionalInventoryServiceSettings regionalInventoryServiceSettings =
         RegionalInventoryServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     RegionalInventoryServiceClient regionalInventoryServiceClient =
         RegionalInventoryServiceClient.create(regionalInventoryServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RegionalInventoryServiceSettings regionalInventoryServiceSettings =
         RegionalInventoryServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     RegionalInventoryServiceClient regionalInventoryServiceClient =
         RegionalInventoryServiceClient.create(regionalInventoryServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RegionalInventoryServiceSettings regionalInventoryServiceSettings =
         RegionalInventoryServiceSettings.newHttpJsonBuilder().build();
     RegionalInventoryServiceClient regionalInventoryServiceClient =
         RegionalInventoryServiceClient.create(regionalInventoryServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > RegionalInventoryServiceClient

## Static Methods 

### create()
    
    
    public static final RegionalInventoryServiceClient create()

Constructs an instance of RegionalInventoryServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[RegionalInventoryServiceClient](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1.RegionalInventoryServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(RegionalInventoryServiceSettings settings)
    
    
    public static final RegionalInventoryServiceClient create(RegionalInventoryServiceSettings settings)

Constructs an instance of RegionalInventoryServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[RegionalInventoryServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1.RegionalInventoryServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RegionalInventoryServiceClient](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1.RegionalInventoryServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(RegionalInventoryServiceStub stub)
    
    
    public static final RegionalInventoryServiceClient create(RegionalInventoryServiceStub stub)

Constructs an instance of RegionalInventoryServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(RegionalInventoryServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[RegionalInventoryServiceStub](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1.stub.RegionalInventoryServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RegionalInventoryServiceClient](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1.RegionalInventoryServiceClient)` |   
  
## Constructors 

### RegionalInventoryServiceClient(RegionalInventoryServiceSettings settings)
    
    
    protected RegionalInventoryServiceClient(RegionalInventoryServiceSettings settings)

Constructs an instance of RegionalInventoryServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[RegionalInventoryServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1.RegionalInventoryServiceSettings)`  
  
  
### RegionalInventoryServiceClient(RegionalInventoryServiceStub stub)
    
    
    protected RegionalInventoryServiceClient(RegionalInventoryServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[RegionalInventoryServiceStub](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1.stub.RegionalInventoryServiceStub)`  
  
  
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

### deleteRegionalInventory(@Nullable RegionalInventoryName name)
    
    
    public final void deleteRegionalInventory(@Nullable RegionalInventoryName name)

Deletes the specified `RegionalInventory` resource from the given product in your merchant account. It might take up to an hour for the `RegionalInventory` to be deleted from the specific product. Once you have received a successful delete response, wait for that period before attempting a delete again.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionalInventoryServiceClient regionalInventoryServiceClient =
         RegionalInventoryServiceClient.create()) {
       RegionalInventoryName name = RegionalInventoryName.of("[ACCOUNT]", "[PRODUCT]", "[REGION]");
       regionalInventoryServiceClient.deleteRegionalInventory(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.shopping.merchant.inventories.v1.RegionalInventoryName`  
Required. The name of the `RegionalInventory` resource to delete. Format: `accounts/{account}/products/{product}/regionalInventories/{region}` The `{product}` segment is a unique identifier for the product. This identifier must be unique within a merchant account and generally follows the structure: `content_language~feed_label~offer_id`. Example: `en~US~sku123` For legacy local products, the structure is: `local~content_language~feed_label~offer_id`. Example: `local~en~US~sku123` The format of the `{product}` segment in the URL is automatically detected by the server, supporting two options: 1\. **Encoded Format**: The `{product}` segment is an **unpadded base64url** encoded string (RFC 4648 Section 5). The decoded string must result in the `content_language~feed_label~offer_id` structure. This encoding MUST be used if any part of the product identifier (like `offer_id`) contains characters such as `/`, `%`, or `~`. * Example: To represent the product ID `en~US~sku/123` for `region` "region123", the `{product}` segment must be the unpadded base64url encoding of this string, which is `ZW5-VVN-c2t1LzEyMw`. The full resource name for the regional inventory would be `accounts/123/products/ZW5-VVN-c2t1LzEyMw/regionalInventories/region123`. 2\. **Plain Format**: The `{product}` segment is the tilde-separated string `content_language~feed_label~offer_id`. This format is suitable only when `content_language`, `feed_label`, and `offer_id` do not contain URL-problematic characters like `/`, `%`, or `~`. We recommend using the **Encoded Format** for all product IDs to ensure correct parsing, especially those containing special characters. The presence of tilde (`~`) characters in the `{product}` segment is used to differentiate between the two formats.  
  
### deleteRegionalInventory(DeleteRegionalInventoryRequest request)
    
    
    public final void deleteRegionalInventory(DeleteRegionalInventoryRequest request)

Deletes the specified `RegionalInventory` resource from the given product in your merchant account. It might take up to an hour for the `RegionalInventory` to be deleted from the specific product. Once you have received a successful delete response, wait for that period before attempting a delete again.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionalInventoryServiceClient regionalInventoryServiceClient =
         RegionalInventoryServiceClient.create()) {
       DeleteRegionalInventoryRequest request =
           DeleteRegionalInventoryRequest.newBuilder()
               .setName(RegionalInventoryName.of("[ACCOUNT]", "[PRODUCT]", "[REGION]").toString())
               .build();
       regionalInventoryServiceClient.deleteRegionalInventory(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteRegionalInventoryRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1.DeleteRegionalInventoryRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteRegionalInventory(String name)
    
    
    public final void deleteRegionalInventory(String name)

Deletes the specified `RegionalInventory` resource from the given product in your merchant account. It might take up to an hour for the `RegionalInventory` to be deleted from the specific product. Once you have received a successful delete response, wait for that period before attempting a delete again.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionalInventoryServiceClient regionalInventoryServiceClient =
         RegionalInventoryServiceClient.create()) {
       String name = RegionalInventoryName.of("[ACCOUNT]", "[PRODUCT]", "[REGION]").toString();
       regionalInventoryServiceClient.deleteRegionalInventory(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the `RegionalInventory` resource to delete. Format: `accounts/{account}/products/{product}/regionalInventories/{region}` The `{product}` segment is a unique identifier for the product. This identifier must be unique within a merchant account and generally follows the structure: `content_language~feed_label~offer_id`. Example: `en~US~sku123` For legacy local products, the structure is: `local~content_language~feed_label~offer_id`. Example: `local~en~US~sku123` The format of the `{product}` segment in the URL is automatically detected by the server, supporting two options: 1\. **Encoded Format**: The `{product}` segment is an **unpadded base64url** encoded string (RFC 4648 Section 5). The decoded string must result in the `content_language~feed_label~offer_id` structure. This encoding MUST be used if any part of the product identifier (like `offer_id`) contains characters such as `/`, `%`, or `~`. * Example: To represent the product ID `en~US~sku/123` for `region` "region123", the `{product}` segment must be the unpadded base64url encoding of this string, which is `ZW5-VVN-c2t1LzEyMw`. The full resource name for the regional inventory would be `accounts/123/products/ZW5-VVN-c2t1LzEyMw/regionalInventories/region123`. 2\. **Plain Format**: The `{product}` segment is the tilde-separated string `content_language~feed_label~offer_id`. This format is suitable only when `content_language`, `feed_label`, and `offer_id` do not contain URL-problematic characters like `/`, `%`, or `~`. We recommend using the **Encoded Format** for all product IDs to ensure correct parsing, especially those containing special characters. The presence of tilde (`~`) characters in the `{product}` segment is used to differentiate between the two formats.  
  
### deleteRegionalInventoryCallable()
    
    
    public final UnaryCallable<DeleteRegionalInventoryRequest,Empty> deleteRegionalInventoryCallable()

Deletes the specified `RegionalInventory` resource from the given product in your merchant account. It might take up to an hour for the `RegionalInventory` to be deleted from the specific product. Once you have received a successful delete response, wait for that period before attempting a delete again.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionalInventoryServiceClient regionalInventoryServiceClient =
         RegionalInventoryServiceClient.create()) {
       DeleteRegionalInventoryRequest request =
           DeleteRegionalInventoryRequest.newBuilder()
               .setName(RegionalInventoryName.of("[ACCOUNT]", "[PRODUCT]", "[REGION]").toString())
               .build();
       ApiFuture<Empty> future =
           regionalInventoryServiceClient.deleteRegionalInventoryCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteRegionalInventoryRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1.DeleteRegionalInventoryRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getSettings()
    
    
    public final @Nullable RegionalInventoryServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.shopping.merchant.inventories.v1.RegionalInventoryServiceSettings` |   
  
### getStub()
    
    
    public RegionalInventoryServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[RegionalInventoryServiceStub](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1.stub.RegionalInventoryServiceStub)` |   
  
### insertRegionalInventory(InsertRegionalInventoryRequest request)
    
    
    public final RegionalInventory insertRegionalInventory(InsertRegionalInventoryRequest request)

Inserts a `RegionalInventory` to a given product in your merchant account.

Replaces the full `RegionalInventory` resource if an entry with the same `region` already exists for the product.

It might take up to 30 minutes for the new or updated `RegionalInventory` resource to appear in products.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionalInventoryServiceClient regionalInventoryServiceClient =
         RegionalInventoryServiceClient.create()) {
       InsertRegionalInventoryRequest request =
           InsertRegionalInventoryRequest.newBuilder()
               .setParent(ProductName.of("[ACCOUNT]", "[PRODUCT]").toString())
               .setRegionalInventory(RegionalInventory.newBuilder().build())
               .build();
       RegionalInventory response = regionalInventoryServiceClient.insertRegionalInventory(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertRegionalInventoryRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1.InsertRegionalInventoryRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RegionalInventory](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1.RegionalInventory)` |   
  
### insertRegionalInventoryCallable()
    
    
    public final UnaryCallable<InsertRegionalInventoryRequest,RegionalInventory> insertRegionalInventoryCallable()

Inserts a `RegionalInventory` to a given product in your merchant account.

Replaces the full `RegionalInventory` resource if an entry with the same `region` already exists for the product.

It might take up to 30 minutes for the new or updated `RegionalInventory` resource to appear in products.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionalInventoryServiceClient regionalInventoryServiceClient =
         RegionalInventoryServiceClient.create()) {
       InsertRegionalInventoryRequest request =
           InsertRegionalInventoryRequest.newBuilder()
               .setParent(ProductName.of("[ACCOUNT]", "[PRODUCT]").toString())
               .setRegionalInventory(RegionalInventory.newBuilder().build())
               .build();
       ApiFuture<RegionalInventory> future =
           regionalInventoryServiceClient.insertRegionalInventoryCallable().futureCall(request);
       // Do something.
       RegionalInventory response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertRegionalInventoryRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1.InsertRegionalInventoryRequest),[RegionalInventory](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1.RegionalInventory)>` |   
  
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
  
### listRegionalInventories(@Nullable ProductName parent)
    
    
    public final RegionalInventoryServiceClient.ListRegionalInventoriesPagedResponse listRegionalInventories(@Nullable ProductName parent)

Lists the `RegionalInventory` resources for the given product in your merchant account. The response might contain fewer items than specified by `pageSize`. If `pageToken` was returned in previous request, it can be used to obtain additional results.

`RegionalInventory` resources are listed per product for a given account.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionalInventoryServiceClient regionalInventoryServiceClient =
         RegionalInventoryServiceClient.create()) {
       ProductName parent = ProductName.of("[ACCOUNT]", "[PRODUCT]");
       for (RegionalInventory element :
           regionalInventoryServiceClient.listRegionalInventories(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.shopping.merchant.inventories.v1.ProductName`  
Required. The `name` of the parent product to list `RegionalInventory` resources for. Format: `accounts/{account}/products/{product}` The `{product}` segment is a unique identifier for the product. This identifier must be unique within a merchant account and generally follows the structure: `content_language~feed_label~offer_id`. Example: `en~US~sku123` For legacy local products, the structure is: `local~content_language~feed_label~offer_id`. Example: `local~en~US~sku123` The format of the `{product}` segment in the URL is automatically detected by the server, supporting two options: 1\. **Encoded Format**: The `{product}` segment is an **unpadded base64url** encoded string (RFC 4648 Section 5). The decoded string must result in the `content_language~feed_label~offer_id` structure. This encoding MUST be used if any part of the product identifier (like `offer_id`) contains characters such as `/`, `%`, or `~`. * Example: To represent the product ID `en~US~sku/123`, the `{product}` segment must be the unpadded base64url encoding of this string, which is `ZW5-VVN-c2t1LzEyMw`. The full resource name for the product would be `accounts/123/products/ZW5-VVN-c2t1LzEyMw`. 2\. **Plain Format**: The `{product}` segment is the tilde-separated string `content_language~feed_label~offer_id`. This format is suitable only when `content_language`, `feed_label`, and `offer_id` do not contain URL-problematic characters like `/`, `%`, or `~`. We recommend using the **Encoded Format** for all product IDs to ensure correct parsing, especially those containing special characters. The presence of tilde (`~`) characters in the `{product}` segment is used to differentiate between the two formats.  
**Returns**  
---  
**Type** | **Description**  
`[RegionalInventoryServiceClient.ListRegionalInventoriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1.RegionalInventoryServiceClient.ListRegionalInventoriesPagedResponse)` |   
  
### listRegionalInventories(ListRegionalInventoriesRequest request)
    
    
    public final RegionalInventoryServiceClient.ListRegionalInventoriesPagedResponse listRegionalInventories(ListRegionalInventoriesRequest request)

Lists the `RegionalInventory` resources for the given product in your merchant account. The response might contain fewer items than specified by `pageSize`. If `pageToken` was returned in previous request, it can be used to obtain additional results.

`RegionalInventory` resources are listed per product for a given account.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionalInventoryServiceClient regionalInventoryServiceClient =
         RegionalInventoryServiceClient.create()) {
       ListRegionalInventoriesRequest request =
           ListRegionalInventoriesRequest.newBuilder()
               .setParent(ProductName.of("[ACCOUNT]", "[PRODUCT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (RegionalInventory element :
           regionalInventoryServiceClient.listRegionalInventories(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListRegionalInventoriesRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1.ListRegionalInventoriesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RegionalInventoryServiceClient.ListRegionalInventoriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1.RegionalInventoryServiceClient.ListRegionalInventoriesPagedResponse)` |   
  
### listRegionalInventories(String parent)
    
    
    public final RegionalInventoryServiceClient.ListRegionalInventoriesPagedResponse listRegionalInventories(String parent)

Lists the `RegionalInventory` resources for the given product in your merchant account. The response might contain fewer items than specified by `pageSize`. If `pageToken` was returned in previous request, it can be used to obtain additional results.

`RegionalInventory` resources are listed per product for a given account.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionalInventoryServiceClient regionalInventoryServiceClient =
         RegionalInventoryServiceClient.create()) {
       String parent = ProductName.of("[ACCOUNT]", "[PRODUCT]").toString();
       for (RegionalInventory element :
           regionalInventoryServiceClient.listRegionalInventories(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The `name` of the parent product to list `RegionalInventory` resources for. Format: `accounts/{account}/products/{product}` The `{product}` segment is a unique identifier for the product. This identifier must be unique within a merchant account and generally follows the structure: `content_language~feed_label~offer_id`. Example: `en~US~sku123` For legacy local products, the structure is: `local~content_language~feed_label~offer_id`. Example: `local~en~US~sku123` The format of the `{product}` segment in the URL is automatically detected by the server, supporting two options: 1\. **Encoded Format**: The `{product}` segment is an **unpadded base64url** encoded string (RFC 4648 Section 5). The decoded string must result in the `content_language~feed_label~offer_id` structure. This encoding MUST be used if any part of the product identifier (like `offer_id`) contains characters such as `/`, `%`, or `~`. * Example: To represent the product ID `en~US~sku/123`, the `{product}` segment must be the unpadded base64url encoding of this string, which is `ZW5-VVN-c2t1LzEyMw`. The full resource name for the product would be `accounts/123/products/ZW5-VVN-c2t1LzEyMw`. 2\. **Plain Format**: The `{product}` segment is the tilde-separated string `content_language~feed_label~offer_id`. This format is suitable only when `content_language`, `feed_label`, and `offer_id` do not contain URL-problematic characters like `/`, `%`, or `~`. We recommend using the **Encoded Format** for all product IDs to ensure correct parsing, especially those containing special characters. The presence of tilde (`~`) characters in the `{product}` segment is used to differentiate between the two formats.  
**Returns**  
---  
**Type** | **Description**  
`[RegionalInventoryServiceClient.ListRegionalInventoriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1.RegionalInventoryServiceClient.ListRegionalInventoriesPagedResponse)` |   
  
### listRegionalInventoriesCallable()
    
    
    public final UnaryCallable<ListRegionalInventoriesRequest,ListRegionalInventoriesResponse> listRegionalInventoriesCallable()

Lists the `RegionalInventory` resources for the given product in your merchant account. The response might contain fewer items than specified by `pageSize`. If `pageToken` was returned in previous request, it can be used to obtain additional results.

`RegionalInventory` resources are listed per product for a given account.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionalInventoryServiceClient regionalInventoryServiceClient =
         RegionalInventoryServiceClient.create()) {
       ListRegionalInventoriesRequest request =
           ListRegionalInventoriesRequest.newBuilder()
               .setParent(ProductName.of("[ACCOUNT]", "[PRODUCT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListRegionalInventoriesResponse response =
             regionalInventoryServiceClient.listRegionalInventoriesCallable().call(request);
         for (RegionalInventory element : response.getRegionalInventoriesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRegionalInventoriesRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1.ListRegionalInventoriesRequest),[ListRegionalInventoriesResponse](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1.ListRegionalInventoriesResponse)>` |   
  
### listRegionalInventoriesPagedCallable()
    
    
    public final UnaryCallable<ListRegionalInventoriesRequest,RegionalInventoryServiceClient.ListRegionalInventoriesPagedResponse> listRegionalInventoriesPagedCallable()

Lists the `RegionalInventory` resources for the given product in your merchant account. The response might contain fewer items than specified by `pageSize`. If `pageToken` was returned in previous request, it can be used to obtain additional results.

`RegionalInventory` resources are listed per product for a given account.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionalInventoryServiceClient regionalInventoryServiceClient =
         RegionalInventoryServiceClient.create()) {
       ListRegionalInventoriesRequest request =
           ListRegionalInventoriesRequest.newBuilder()
               .setParent(ProductName.of("[ACCOUNT]", "[PRODUCT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<RegionalInventory> future =
           regionalInventoryServiceClient.listRegionalInventoriesPagedCallable().futureCall(request);
       // Do something.
       for (RegionalInventory element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRegionalInventoriesRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1.ListRegionalInventoriesRequest),[ListRegionalInventoriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-inventories/latest/com.google.shopping.merchant.inventories.v1.RegionalInventoryServiceClient.ListRegionalInventoriesPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
