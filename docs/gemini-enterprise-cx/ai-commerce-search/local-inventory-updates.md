---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/local-inventory-updates/
title: Update local inventory for AI Commerce Search \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:36:17.444660+00:00
---

# Update local inventory for AI Commerce Search  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/local-inventory-updates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Update local inventory for AI Commerce Search Stay organized with collections  Save and categorize content based on your preferences. 

`LocalInventory` is the inventory information associated with a certain place, identified by its `place_id`. For example, a `LocalInventory` could be created for a store or a region where a certain price is available. `LocalInventory` has the following fields:

  * `LocalInventory.price_info`
  * `LocalInventory.attributes`
  * `LocalInventory.fulfillment_types`



Existing `LocalInventory` entries are visible through `Product.local_inventories` (with the exception of `fulfillment_types` which, for backward compatibility, is available through `Product.fulfillment_info`). This field is output only. Setting `Product.local_inventories` for `Product` CRUD APIs or `SetInventory` has no effect.

Each `(LocalInventory.place_id, LocalInventory.fulfillment_types[...])` pair points to the same `(fulfillment_info.place_ids, fulfillment_info.type)` pair mentioned in the [Inventory update documentation](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/inventory-updates#inventory-update-methods). `fulfillment_types` updated by `AddLocalInventories` and `RemoveLocalInventories` reflects a mapping from each place ID to a list of fulfillment types it supports, while `fulfillment_info` updated by [`AddFulfillmentPlaces`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/inventory-updates#inventory-update-methods) and [`RemoveFulfillmentPlaces`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/inventory-updates#inventory-update-methods) reflects a mapping from each specific fulfillment type to a list of place IDs that supports such type. However, both types of the APIs are modifying the same underlying fulfillment information, and the effect of both types of APIs will be reflected onto `Product.fulfillment_info`.

## Local inventory update methods

Changes to a product's local inventory information can occur much more frequently than changes to its catalog information. A specialized set of methods are provided to handle large volumes of local inventory-specific updates. These methods are asynchronous because of downstream optimizations that support hundreds of concurrent updates per product, without sacrificing performance.

**Note:** There is no `availability` facet for `localInventory` objects. Instead, you can use custom `fulfillment_types`. For search queries, the filter or facet key can be changed to `"pickupInStore"`. See the [Filter and order](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/filter-and-order) and [Facets](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/facets-overview) pages for more information.

### `AddLocalInventories`

[`AddLocalInventories`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.AddLocalInventoriesRequest) can be used to create local inventories at new places (represented with new `place_id`s), or update existing fields on existing local inventories. Fields that are added or updated on the list of `LocalInventory` entries in the request body can be specified through `AddLocalInventoriesRequest.add_mask`. Valid `add_mask` values are:

  * `price_info`: overwrites `LocalInventory.price_info`.
  * `attributes`: overwrites all `LocalInventory.attributes`. Existing attributes that are not mentioned in the request body are removed.
  * `attributes.PLACEHOLDER_NAME`: overwrites only the specified custom attribute. If an existing attribute name is not provided in the request, the attribute is deleted. Multiple `attributes.PLACEHOLDER_NAME` can be specified, as long as each attribute name is different. However, `AddLocalInventoriesRequest.add_mask` can't include both the `attributes` value and `attributes.PLACEHOLDER_NAME` values in the same request.
  * `fulfillment_types`: overwrites all supported fulfillment types. Existing fulfillment types that are not mentioned in the request body are removed.



### Proto
    
    
    {
      product: "projects/123/locations/global/catalogs/default_catalog/branches/default_branch/products/p123"
      local_inventories: {
        place_id: "store1"
        price_info: {
          currency_code: "USD"
          price: 100
          original_price: 110
          cost: 95
        }
        fulfillment_types: "pickup-in-store"
        fulfillment_types: "ship-to-store"
      }
      local_inventories: {
        place_id: "store2"
        price_info: {
          currency_code: "USD"
          price: 200
          original_price: 210
          cost: 195
        }
        attributes: {
          key: "attr1",
          value: {
            text: "store2_value"
          }
        }
        fulfillment_types: "custom-type-1"
      }
      add_mask: {
        paths: "price_info"
        paths: "attributes.attr1"
        paths: "fulfillment_types"
      }
      add_time: {
        seconds: 100
        nanos: 100
      }
      allow_missing: true
    }
      

This sample `AddLocalInventoriesRequest` adds or updates two local inventories with place IDs `"store1"` and `"store2"` for the specified product. If `store1` exists, and `store2` does not exist before the request, the request will update fields of `store1`, and create `store2` with the given field values.

This `AddLocalInventoriesRequest.add_mask` specifies that `price_info`, a single custom attribute with the name `"attr1"`, and `fulfillment_types` should be updated using the values provided in the `AddLocalInventoriesRequest.local_inventories`.

`attributes` are attributes associated with a place with customizable name and values. Since `LocalInventory` of `store1` does not provide the value of `attr1` in the request, custom attribute `attr1` will be deleted from the existing `LocalInventory` of `store1` if it exists. `store2` will have its attribute `attr1`'s value set to a text value `store2_value`. Other existing custom attributes on `store1` and `store2` are untouched.

`fulfillment_types` represents a list of fulfillment availability for a `Product` at a single place. It is the same and accepts the same values as `fulfillment_info.type`. This `AddLocalInventoriesRequest` specifies that `store1` supports `pickup-in-store` and `ship-to-store` fulfillment types, while `store1` supports `custom-type-1`. Fulfillment types existing before this update that are not mentioned in the request will be deleted.

Since `AddLocalInventoriesRequest.allow_missing` is set to true, even if the product does not already exist, the updated local inventory information will be stored for when the product is eventually created. The update is timestamped with `AddLocalInventoriesRequest.add_time` to prevent stale updates from overriding the specified fields of these place IDs. For more about preventing stale updates and storing local inventory information before the product is created, see Timestamp protections for local inventory updates and Preloading inventory information.

### Proto
    
    
    {
      product: "projects/123/locations/global/catalogs/default_catalog/branches/default_branch/products/p123"
      local_inventories: {
        place_id: "store3"
        attributes: {
          key: "attr1",
          value: {
            text: "attr1_value"
          }
        }
        attributes: {
          key: "attr2",
          value: {
            numbers: 123
          }
        }
      }
      add_mask: {
        paths: "attributes"
      }
      add_time: {
        seconds: 100
        nanos: 100
      }
    }
      

This sample `AddLocalInventoriesRequest` adds or updates a single local inventory with place ID `"store3"` for the specified product. Since its `add_mask` contains `"attributes"`, all existing custom attributes of `store3` are deleted, and replaced with `attr1` and `attr2` as specified in the request. Note that since `allow_missing` is not set, it requires the specified product to exist. Otherwise, a `NOT_FOUND` error is thrown.

### `RemoveLocalInventories`

[`RemoveLocalInventories`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.RemoveLocalInventoriesRequest) can be used to remove existing local inventories at places with given place IDs.

### Proto
    
    
    {
      product: "projects/123/locations/global/catalogs/default_catalog/branches/default_branch/products/p123"
      place_ids: "store1"
      place_ids: "store2"
      remove_time: {
        seconds: 100
        nanos: 100
      }
      allow_missing: true
    }
      

This sample `RemoveLocalInventoriesRequest` removes local inventories for places with place IDs `"store1"` and `"store2"` for the specified product. The update is timestamped with `RemoveLocalInventoriesRequest.remove_time` to prevent stale updates from overriding the deletion of these place IDs. For specified place IDs without existing local inventories, the request also records their update time to `remove_time`. For more about update timestamps, see Timestamp protections for local inventory updates

### Timestamp protections for local inventory updates

To protect against out-of-order updates, each local inventory field is associated with a latest update time.

The latest update time is recorded for each `(place_id, price_info)`, `(place_id, attributes[...])`, and `(place_id, fulfillment_types[...])` pair.

The [`AddLocalInventories`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.AddLocalInventoriesRequest) and [`RemoveLocalInventories`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.RemoveLocalInventoriesRequest) methods allow the caller to specify an update time for when the request is issued. This update time is compared against the latest update time recorded for the relevant inventory fields, and the update is committed if and only if the update time is strictly after the latest update time.

For example, suppose place ID `"store1"` has `price_info` with the last recorded update time set to time `T`. If `RemoveLocalInventoriesRequest.place_ids` contains `"store1"`, the request will remove `price_info` from `"store1"` only if the `RemoveLocalInventoriesRequest.remove_time` is later than time `T`. The same is true for `RemoveLocalInventoriesRequest`s.

Under timestamp protection, it is possible that a `RemoveLocalInventoriesRequest` might remove only certain fields of a `LocalInventory` instead of all of it. Suppose a local inventory with place ID `"store1"` has `price_info` with last recorded update time set to time `T1`, and has its only existing custom attribute with name `"attr1"` with last recorded update time at `T2`. If a `RemoveLocalInventoriesRequest.place_ids` contains `"store1"`, and has `remove_time` set to `T3` (where `T1 < T3 < T2`), then `store_1`'s `price_info` will be removed, while its attribute `attr1` will be untouched.

### Preloading inventory information

Each of the local inventory update methods allows the caller to set `allow_missing` in the request. When `allow_missing` is set to true, a local inventory update to a nonexistent `Product` is processed as if the `Product` exists according to the method specification(s). The local inventory information will be retained for a maximum of two days if the corresponding `Product` is not created using [`CreateProduct`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#google.cloud.retail.v2.CreateProductRequest) within this timeframe.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
