---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/inventory-updates/
title: Update inventory for AI Commerce Search \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:39:06.837771+00:00
---

# Update inventory for AI Commerce Search  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/inventory-updates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Update inventory for AI Commerce Search Stay organized with collections  Save and categorize content based on your preferences. 

This page outlines the methods for managing real-time price and quantity updates for the AI Commerce Search catalog using the AI Commerce Search API.

While the `Product` create, read, update, and delete (CRUD) methods are used to broadly modify a `Product`'s attributes, there is a set of `Product` methods that can be used for updating inventory-specific fields with varying levels of granularity.

## Understand inventory

In general terms, inventory usually refers to stock levels (quantity) and price for items on an ecommerce site. For the AI Commerce Search API, `inventory` refers to price, availability, available quantity, fulfillment information and local pricing and additional local attributes. These fields are defined in the Product schema with the following fields:

  * [`Product.availability`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.FIELDS.availability)
  * [`Product.availableQuantity`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.FIELDS.available_quantity)
  * [`Product.priceInfo`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.FIELDS.price_info)
  * [`Product.fulfillmentInfo`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.FIELDS.fulfillment_info)
  * [`Product.localInventories`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.FIELDS.local_inventories)



### Product-level inventory

For ecommerce site merchants with an online catalog only, `inventory` is usually represented as the products in the catalog only. Price, availability and all other data is set on each [Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product) entry in the catalog. The `fulfillmentInfo` and `localInventories` fields aren't used.

### Local inventory

For retailers that have multiple locations, products are still represented by the Product entries in the catalog, but local inventory (price, availability and fulfillment) can be added to locations (placeId) for a product with the [addLocalInventories](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products/addLocalInventories) method.

There are two separate Product fields used for local inventory: [Product.fulfillmentInfo](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.FIELDS.fulfillment_info) and [Product.localInventories](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.FIELDS.local_inventories). One or both can be used, depending on the requirements. Both `fulfillmentInfo` and `localInventories` are lists of locations with associated data.

`fulfillmentInfo` specifies how a product is fulfilled at a particular location, whereas `localInventories` specifies price and other custom attributes for each location.

To mark a product as out of stock or no longer available at a specific location, the [removeLocalInventories](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products/removeLocalInventories) method is used to remove `fulfillment` and `inventory` from a product for a particular `placeId`.

## Inventory update methods

Changes to a product's inventory information may occur much more frequently than changes to its catalog information. As such, a specialized set of methods are provided to handle large volumes of inventory-specific updates. These methods are asynchronous because of downstream optimizations that support hundreds of concurrent updates per product, without sacrificing performance.

### Incremental updates

Follow the [local inventory updates guide](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/local-inventory-updates) to issue incremental inventory updates. The newer API methods provide more fine-grained control for per-place inventory attributes.

`fulfillment_info` is often used to encode place-level fulfillment availability for a `Product`. In some cases, fulfillment availability for some specific places can change. You can decide to issue updates that describe this change, instead of using the [`UpdateProduct`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.UpdateProductRequest) method to respecify all the product's fulfillment information.

In such cases, the [`AddFulfillmentPlaces`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.AddFulfillmentPlacesRequest) and [`RemoveFulfillmentPlaces`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.RemoveFulfillmentPlacesRequest) methods can be used to incrementally update a product's fulfillment changes based on which place IDs are added or removed for a given fulfillment type.

### Java

To learn how to install and use the client library for AI Commerce Search, see [AI Commerce Search client libraries](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/libraries). For more information, see the [AI Commerce Search Java API reference documentation](https://github.com/googleapis/java-recommendations-ai/). 

To authenticate to AI Commerce Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    public static AddFulfillmentPlacesResponse addFulfillmentPlaces(
        Product productToUpdate, String fulfillmentInfoType, ImmutableList<String> placeIds)
        throws IOException, InterruptedException, ExecutionException {
      ProductServiceClient productClient = getProductServiceClient();
    
      AddFulfillmentPlacesRequest request = AddFulfillmentPlacesRequest.newBuilder()
          .setProduct(productToUpdate.getName())
          .setType(fulfillmentInfoType)
          .addAllPlaceIds(placeIds)
          .setAddTime(Timestamps.fromMillis(System.currentTimeMillis()))
          .build();
    
      AddFulfillmentPlacesResponse response = productClient
          .addFulfillmentPlacesAsync(request).get();
    
      productClient.shutdownNow();
      productClient.awaitTermination(2, TimeUnit.SECONDS);
    
      return response;
    }

### Proto
    
    
      {
        product: "projects/123/locations/global/catalogs/default_catalog/branches/default_branch/products/p123"
        type: "pickup-in-store"
        place_ids: "store0"
        place_ids: "store1"
        add_time: {
          seconds: 100
          nanos: 100
        }
        allow_missing: true
      }
      

This sample `AddFulfillmentPlacesRequest` adds fulfillment type `"pickup-in-store"` to place IDs `"store0"` and `"store1"` for the specified product. Because `AddFulfillmentPlacesRequest.allow_missing` is set to true, even if the product does not already exist, the updated inventory information will be stored for when the product is eventually created. The update is time stamped with `AddFulfillmentPlacesRequest.add_time` to prevent stale updates from overriding the fulfillment status of these place IDs. These features are discussed in greater detail in the following sections.

The behavior is identical for `RemoveFulfillmentPlacesRequest` and the schema is very similar.

When `fulfillment_types` is updated by [`AddLocalInventories`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/local-inventory-updates#add-local-inventories) and [`RemoveLocalInventories`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/local-inventory-updates#remove-local-inventories), it reflects a mapping from each place ID to a list of fulfillment types it supports. When `fulfillment_info` is updated by [`AddFulfillmentPlaces`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.AddFulfillmentPlacesRequest) and [`RemoveFulfillmentPlaces`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.RemoveFulfillmentPlacesRequest), it reflects a mapping from each specific fulfillment type to a list of place IDs that supports each type. Both API types are modifying the same underlying fulfillment information, and the effect of both types of APIs is reflected by `Product.fulfillment_info`.

### Non-incremental updates

The `price_info`, `availability`, and `available_quantity` methods can't be incrementally updated, because they represent product-level inventory, not place-level information. It can also be good to issue non-incremental updates to `fulfillment_info`. Instead of only incremental changes, [`SetInventory`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.SetInventoryRequest) is recommended.

The [`setInventory`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products/setInventory) method is the preferred way to update price, availability, and quantity at the product level when many, frequent updates required. The `setInventory` method is asynchronous, so the updates might not happen immediately. The default quota (300,000 requests per minute) supports much more requests than `UpdateProduct`.

Additionally, the [`setInventory`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products/setInventory) method is used for local fulfillment updates when [`fulfillmentInfo`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products/setInventory#body.request_body.FIELDS.fulfillment_info) is included in the request, but it can't update the `localInventories` fields. For those attributes, use the `addLocalInventories` and `removeLocalInventories` methods.

Local inventory is saved at the store-level, independent of the catalog. For customers with online and offline inventory, the main product catalog can be used for online or a specific `placeId` (`-1` or `online` for example) could be used to represent online inventory. However, use the main catalog for online inventory because the product inventory fields should be populated with valid `priceInfo` and `availability` values. If a separate inventory `placeId` is used for online, then the main catalog price and availability information should also be kept up to date. For more on local inventory updates, see [Update local inventory](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/local-inventory-updates).

### Java

To learn how to install and use the client library for AI Commerce Search, see [AI Commerce Search client libraries](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/libraries). For more information, see the [AI Commerce Search Java API reference documentation](https://github.com/googleapis/java-recommendations-ai/). 

To authenticate to AI Commerce Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    public static SetInventoryResponse setInventoryWithMask(Product productToUpdate,
        FieldMask updateMask)
        throws IOException, ExecutionException, InterruptedException {
      ProductServiceClient productClient = getProductServiceClient();
    
      SetInventoryRequest request = SetInventoryRequest.newBuilder()
          .setInventory(productToUpdate)
          .setSetMask(updateMask)
          .setSetTime(Timestamps.fromMillis(System.currentTimeMillis()))
          .setAllowMissing(true)
          .build();
    
      SetInventoryResponse response = productClient.setInventoryAsync(request).get();
    
      productClient.shutdownNow();
      productClient.awaitTermination(2, TimeUnit.SECONDS);
    
      return response;
    }

### Proto
    
    
      {
        product: {
          name: "projects/123/locations/global/catalogs/default_catalog/branches/default_branch/products/p123"
          availability: IN_STOCK
          fulfillment_info: {
            type: "pickup-in-store"
            place_ids: "store0"
            place_ids: "store1"
            place_ids: "store2"
            place_ids: "store3"
          }
          fulfillment_info: {
            type: "same-day-delivery"
          }
        }
        set_time: {
          seconds: 100
          nanos: 100
        }
        set_mask: {
          paths: "availability"
          paths: "fulfillment_info"
        }
        allow_missing: true
      }
      

In this particular request, the `SetInventoryRequest.product.fulfillment_info` fields are complete descriptions of each fulfillment type's eligible place IDs, as opposed to incremental specifications. The update to `"same-day-delivery"` indicates that no place IDs are eligible for this fulfillment type for this product. All other fulfillment types are not updated in this request. Thus, this method can be used to replace the place IDs for only a subset of fulfillment types while leaving the other types untouched.

By default,`SetInventory` will update all inventory fields if `SetInventory.set_mask` is unset or empty. If the mask is not empty or if an inventory field is not explicitly listed in `SetInventoryRequest.set_mask`, then any specified value for that inventory field will be ignored in the update request.

As with incremental updates, the `SetInventoryRequest.set_time` field can be used to set an update time that will be against the last recorded update time of all updated inventory fields.

### Timestamp protections for inventory updates

There are several different paths to update a product's inventory fields, and to protect against out-of-order updates, each inventory field is associated with a latest update time.

The latest update time is recorded for `price_info`, `availability`, `available_quantity`, and each pair of `(fulfillment_info.place_ids, fulfillment_info.type)`.

The [`AddFulfillmentPlaces`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.AddFulfillmentPlacesRequest), [`RemoveFulfillmentPlaces`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.RemoveFulfillmentPlacesRequest), and [`SetInventory`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.SetInventoryRequest) methods allow the caller to specify an update time for when the request is issued. This update time is compared against the latest update time recorded for the relevant inventory fields, and the update is committed if and only if the update time is strictly after the latest update time.

For example, suppose place ID `"store1"` has fulfillment type `"pickup-in- store"` enabled, with the last recorded update time set to time `T`. If `RemoveFulfillmentPlacesRequest.type = "pickup-in-store"` and `RemoveFulfillmentPlacesRequest.place_ids` contains `"store1"`, the request will clear `"pickup-in-store"` from `"store1"` if and only if the `RemoveFulfillmentPlacesRequest.remove_time` is later than time `T`. The same is true for `AddFulfillmentPlacesRequests`.

`SetInventory` operates in a similar way for updating `price_info`, `availability`, and `available_quantity`. When updating `fulfillment_info`, a `SetInventoryRequest` is implicitly asking to add all specified place IDs for a given fulfillment type and remove all unspecified existing place IDs.

When the `SetInventoryRequest` is processed, the `fulfillment_info` update is implicitly converted into an `AddFulfillmentPlacesRequest` and `RemoveFulfillmentPlacesRequest` for each specified fulfillment type. This means that if any existing place `"store1"` with fulfillment `"pickup-in-store"` has a last update time `T` that is more recent than `SetInventoryRequest.set_time`, then the implicit add or remove on `"store1"` and `"pickup-in-store"` won't be applied.

### Preload attributes

`setInventory` is asynchronous, meaning that no taxonomic or referencial controls are enforced when adding or modifying inventory fields. This method doesn't require the product referenced in the request to already exist.

This enables customers to implement preloading patterns, whereby the management of inventory fields can be decoupled from the main catalog or product import process. For example, users can import the availability or price context before the associated product is imported.

**Note:** If corresponding product entries are not created in two days, the unassociated inventory entries will be removed.

Each of the inventory update methods allows the caller to set `allow_missing` in the request. When `allow_missing` is set to true, an inventory update to a nonexistent `Product` will be processed as if the `Product` exists according to the method specification(s). The inventory information will be retained for a maximum of two days if the corresponding `Product` is not created using [`CreateProduct`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.CreateProductRequest) within this timeframe.

### Java
    
    
    public static SetInventoryResponse setInventory(Product productToUpdate)
        throws IOException, ExecutionException, InterruptedException {
      ProductServiceClient productClient = getProductServiceClient();
    
      SetInventoryRequest request = SetInventoryRequest.newBuilder()
          .setInventory(productToUpdate)
          .setSetTime(Timestamps.fromMillis(System.currentTimeMillis()))
          .setAllowMissing(true)
          .build();
    
      SetInventoryResponse response = productClient.setInventoryAsync(request).get();
    
      productClient.shutdownNow();
      productClient.awaitTermination(2, TimeUnit.SECONDS);
    
      return response;
    }

## When to use the `Product` methods

While it is possible to update inventory fields with the Product CRUD methods, the caller should be explicitly aware of the effects on existing or pre-existing inventory information.

These are synchronous methods, which means the downstream optimizations used for inventory methods don't apply, and it can become expensive to rely on these methods for frequent inventory updates. Wherever possible, prefer to use the aforementioned inventory update methods.

### `CreateProduct`

When [`CreateProduct`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.CreateProductRequest) is invoked with any inventory fields set, the provided values in the `CreateProductRequest.product` will override any preloaded values for those respective fields. If no inventory fields are set, then any pre-existing inventory information will be automatically used.

Furthermore, the latest update time for the overridden inventory fields will be reset to the time of the method call.

#### `CreateProduct` with preloaded inventory

### PROTO
    
    
    {
      parent: "projects/123/locations/global/catalogs/default_catalog/branches/default_branch"
      product_id: "p123"
      product: {
        name: "projects/123/locations/global/catalogs/default_catalog/branches/default_branch/products/p123"
        title: "some product"
        type: VARIANT
      }
    }

In this example, the created product does not have any inventory fields set, which means any preloaded inventory information will be automatically used if updated using the inventory update methods. This can be helpful when inventory updates are decoupled from catalog updates and you want to have a newly created `Product` synchronize with any pre-existing inventory information.

#### `CreateProduct` with explicit inventory

### PROTO
    
    
    {
      parent: "projects/123/locations/global/catalogs/default_catalog/branches/default_branch"
      product_id: "p123"
      product: {
        name: "projects/123/locations/global/catalogs/default_catalog/branches/default_branch/products/p123"
        title: "some product"
        type: VARIANT
        availability: OUT_OF_STOCK
        fulfillment_info: {
          type: "pickup-in-store"
        }
        fulfillment_info: {
          type: "same-day-delivery"
        }
      }
    }

In this example, a `Product` is created with explicitly set inventory fields. These fields will override any pre-existing values, ignoring the latest update time for the corresponding fields. Thus, the newly created `Product` will have availability set to `OUT_OF_STOCK`, and no place IDs will support fulfillment types `"pickup-in-store"` and `"same-day-delivery"`.

`CreateProduct` with inventory information can be helpful if you are not sure if all the preloaded inventory information is accurate, and prefer to explicitly set the inventory at creation time of `Product` to fully synchronize the catalog and inventory.

### `UpdateProduct`

The [`UpdateProduct`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products/patch) method can be used to update specific attributes on an existing catalog item. This can be done for single or multiple fields at the same time, and for individual products or using the import method multiple products. If you use the import method without the mask it does an overwrite.

`UpdateProduct` is often used for real time price & availability updates, but can be used to update any fields without having to submit all data for a product again. (in contrast to the `createMethod` or the `importProducts`.

The main benefit of using `UpdateProduct` is that it is a synchronous request. Updates to the index (and search or recommendations) is nearly instantaneous. However, `UpdateProduct` isn't intended to be used for very frequent updates. The default quota is 12,000 product write requests per minute. Usually, you'll want to use this method only when an item's price changes or if the stock state changes (not for each quantity decrease).

`UpdateProduct` can only modify the product-level attributes. It can't be used to modify any of the local inventory attributes for `localInventories` or `fulfillmentInfo`.

When making a call with `UpdateProduct` or `ImportProducts`, it is important to specify the [`updateMask`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products/patch#body.QUERY_PARAMETERS.update_mask) parameter. `updateMask` contains a list of the fields to update. Only fields specified in the updateMask will be updated, even if more fields are passed in the request body. _If no`updateMask` is present for an update or import request, all fields are updated to exactly what is submitted in the request body._

When [`UpdateProduct`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.UpdateProductRequest) is invoked and the field mask `UpdateProductRequest.update_mask` contains any inventory fields, the provided values in the `UpdateProductRequest.product` will override any preloaded values for those respective fields.

Furthermore, the latest update time for the overridden inventory fields will be reset to the time of the method call.

### PROTO
    
    
    {
      product: {
        name: "projects/123/locations/global/catalogs/default_catalog/branches/default_branch/products/p123"
        availability: IN_STOCK
        fulfillment_info: {
          type: "pickup-in-store"
          place_ids: "store0"
          place_ids: "store1"
          place_ids: "store2"
          place_ids: "store3"
        }
        fulfillment_info: {
          type: "same-day-delivery"
        }
      }
      update_mask: {
        paths: "availability"
        paths: "fulfillment_info"
      }
    }

This example is very similar to the `SetInventory` example, except the update applies, regardless of each inventory field's latest update time.

  * `UpdateProduct` for inventory can be helpful when a full sync on inventory information is needed while ignoring timestamp protections.

  * By setting `UpdateProductRequest.allow_missing` to `true` to perform a `Product` upsert, you can preload inventory information using `UpdateProduct`. The method requires setting specific catalog fields, like `UpdateProductRequest.product.title`. So use the inventory update methods for preloading use-cases.




### DeleteProduct

When [`DeleteProduct`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.DeleteProductRequest) is invoked, all existing inventory information for the product specified in `DeleteProductRequest.name` will be deleted, including all records of the latest update time for each inventory field.

## Considerations if you replace product-level attributes with inventory-level ones

Take note of the following considerations and limitations associated with each approach:

Feature | Product-level inventory | Store-level (local) inventory  
---|---|---  
**Search filter & boost controls** | Yes | Yes  
**Filter and facet key format specified in`facetSpec`** | Yes | No  
**Available for search facets** | Yes | No  
**Returned in search response** | Yes | Yes (using `variantRollupKeys`)  
**Recommendations AI v2 filters and boost controls** | Yes | No  
Feature | Product-level Inventory | Store-level (Local) Inventory  
---|---|---  
**Search filter and boost controls** |  |   
**Filter and facet key format specified in[`facetSpec`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/FacetSpec)** |  |   
**Available for search facets** |  |   
**Returned in search response** |  |  (using [`variantRollupKeys`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.placements/search#body.request_body.FIELDS.variant_rollup_keys))  
**Recommendations AI v2 filters and boost controls** |  |   
  
There is some overlap in the functionality of the different methods of updating product availability, fulfillment, and local price:

Feature | `UpdateProduct` | `setInventory` | `addLocalInventories`  
---|---|---|---  
**Realtime updates** |  |  |   
**Update any product fields** |  |  |   
**Update product price** |  |  |   
**Update product availability** |  |  |   
**Update`fulfillmentInfo`** |  |  |   
**Update`localInventories` (local prices)** |  |  |   
**Timestamp Sequencing** |  |  |   
  
## Examples

This section demonstrates how to update product inventory using the `UpdateProduct` and `setInventory` methods in curl commands.

  * `UpdateProduct` uses the REST API's HTTP PATCH method for synchronous, real-time updates of product-level fields like price and availability, and can also be used for batch updates by using the `import` method with an `updateMask`.

  * The asynchronous `setInventory` method is shown for updating product-level inventory fields (price, availability, quantity) and local fulfillment details using `fulfillmentInfo`, but it can't modify local prices or attributes stored in `localInventories`.




### Use `UpdateProduct` to update product price and availability

When using the REST API, `UpdateProduct` uses the HTTP `PATCH` method. The same endpoint URL as `CreateProduct`, `GetProduct`, `DeleteProduct` uses the HTTP `PUT`, `GET`, and `DELETE` methods, respectively. Expand the following links to view the respective curl samples.

#### Update availability only
    
    
    curl -X PATCH -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \                        
         -H "Content-Type: application/json; charset=utf-8"  \                                                              
         --data "{                                                                                                          
         'availability': 'OUT_OF_STOCK'                                                                                     
        }" \                                                                                                                "https://retail.googleapis.com/v2/projects/PROJECT/locations/global/catalogs/default_catalog/branches/default_branch/products/266309?updateMask=availability" 

#### Update price only
    
    
    curl -X PATCH -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8"  \
         --data "{
         'priceInfo' : { 
            'price': 5.99,
            'originalPrice': 5.99
            }
        }" \
    "https://retail.googleapis.com/v2/projects/PROJECT/locations/global/catalogs/default_catalog/branches/default_branch/products/266309?updateMask=priceInfo"

#### Update price and availability
    
    
    curl -X PATCH -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8"  \
         --data "{
         'availability': 'IN_STOCK',
         'priceInfo' : { 
            'price': 5.99,
            'originalPrice': 5.99
            }
        }" \
    "https://retail.googleapis.com/v2/projects/PROJECT/locations/global/catalogs/default_catalog/branches/default_branch/products/266309?updateMask=availability,priceInfo"

#### Use import with updateMask

Use `import` with `updateMask` to update price, availability and available quantity for multiple items.
    
    
    curl -X POST \
     -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
     -H "Content-Type: application/json; charset=utf-8" \
     --data @./inline-item.json \
    "https://retail.googleapis.com/v2/projects/PROJECT/locations/global/catalogs/default_catalog/branches/default_branch/products:import"
    inline-item.json file contents:
    {
        "updateMask": "availability,priceInfo,availableQuantity",
        "inputConfig": {
            "productInlineSource": {
                "products": [
                    {
                        "Id": "266309",
                        "availability": "IN_STOCK",
                        "availableQuantity": 10,
                        "priceInfo" : {
                            "price": 5.99,
                            "originalPrice": 5.99
                        }
                    },
                    {
                        "Id": "266310",
                        "availability": "IN_STOCK",
                        "availableQuantity": 10,
                        "priceInfo" : {
                            "price": 5.99,
                            "originalPrice": 5.99
                        }
                    }
                ]
            }
        }
    }

A similar update can be performed for large batches using Cloud Storage or BigQuery source.

### Use `setInventory` to update product price and availability

`setInventory` only supports the following fields:

  * `availability`
  * `availableQuantity`
  * `priceInfo`



Expand the following links to view the respective curl samples.

#### Update price and/or availability
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "x-goog-user-project: PROJECT" \
    -H "Content-Type: application/json" \
    --data '{
      "inventory": {
       "availability": "IN_STOCK", 
       "availableQuantity": "10",
        "priceInfo": {
          "price": 4.95
        }
      }
    }' \
    https://retail.googleapis.com/v2/projects/PROJECT/locations/global/catalogs/default_catalog/branches/default_branch/products/266309:setInventory

And for local inventory, `placeIds` and fulfillment types can be passed in `fulfillmentInfo`, as this curl sample demonstrates:

#### Local inventory
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "x-goog-user-project: PROJECT" \
    -H "Content-Type: application/json" \
    --data '{
      "inventory": {
        "availability": "IN_STOCK",
        "availableQuantity": 5,
        "priceInfo": {
          "price": 4.95
        },
        "fulfillmentInfo": [
          {
            "type": "pickup-in-store",
            "placeIds": [
              "store123","store456"
            ]
          },
          {                                                                                                                                                                                                                                                                                      
            "type": "same-day-delivery",
            "placeIds": [
              "store456"
            ]                                                                                                                                                                                                                                                                                 
          }
        ]
      }
    }' \
    https://retail.googleapis.com/v2/projects/PROJECT/locations/global/catalogs/default_catalog/branches/default_branch/products/266309:setInventory

**Note:** `setInventory` can't modify the localInventories fields which are local prices and attributes. More details about managing local inventory with `addLocalInventories` and `removeLocalInventories` can be found in [Update local inventory](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/local-inventory-updates).

## Tutorials

Use these tutorials to guide you through how to use `setInventory` or to add or remove fulfillments.

### Set inventory tutorial

This tutorial shows how to push inventory updates using the [`SetInventory`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.SetInventoryRequest) method instead of updating the entire product.

* * *

To follow step-by-step guidance for this task directly in the Cloud Shell Editor, click **Guide me** : 

[Guide me](https://shell.cloud.google.com/?walkthrough_tutorial_id=retail--retail_api_v2_set_inventory_select_language&show=ide&environment_deployment=ide)

* * *

### Add fulfillment tutorial

We recommend using the `AddLocalInventories` method instead of `AddFulfillmentPlaces`. `AddLocalInventories` achieves the same results but provides more fine-grained control over ingesting local inventory data. For more information, see the [`AddLocalInventories` documentation](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/local-inventory-updates#add-local-inventories).

This tutorial shows how to update product fulfillment information using the [`AddFulfillmentPlaces`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.AddFulfillmentPlacesRequest) method. In this way, search can show updates where products are available and orders can be fulfilled. For example, a shopper is looking for blue jeans in a shop but they're out of stock. The moment the jeans are in stock again at this shop or any other shop, the shopper sees the updates and can proceed with their order.

* * *

To follow step-by-step guidance for this task directly in the Cloud Shell Editor, click **Guide me** : 

[Guide me](https://shell.cloud.google.com/?walkthrough_tutorial_id=retail--retail_api_v2_add_fulfillment_places_select_language&show=ide&environment_deployment=ide)

* * *

### Remove fulfillment tutorial

We recommend using the `RemoveLocalInventories` method instead of `RemoveFulfillmentPlaces`. `RmoveLocalInventories` achieves the same results but provides more fine-grained control over ingesting local inventory data. For more information, see the [`RemoveLocalInventories` documentation](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/local-inventory-updates#remove-local-inventories).

This tutorial shows how to update product fulfillment information using the [`RemoveFulfillmentPlaces`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.RemoveFulfillmentPlacesRequest) method. In this way, AI Commerce Search can show updates where products aren't available and orders can't be fulfilled. In this way, search can show updates where products aren't available and orders can't be fulfilled. For example, a shopper is looking for blue jeans in a shop. If the jeans become out of stock in this shop, the shopper sees this and can't proceed with their order.

* * *

To follow step-by-step guidance for this task directly in the Cloud Shell Editor, click **Guide me** : 

[Guide me](https://shell.cloud.google.com/?walkthrough_tutorial_id=retail--retail_api_v2_remove_fulfillment_places_select_language&show=ide&environment_deployment=ide)

* * *

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
