---
url: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-lfp/latest/com.google.shopping.merchant.lfp.v1.LfpInventoryOrBuilder
title: Interface LfpInventoryOrBuilder (1.27.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:11:24.937594+00:00
---

# Interface LfpInventoryOrBuilder (1.27.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-lfp/latest/com.google.shopping.merchant.lfp.v1.LfpInventoryOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface LfpInventoryOrBuilder (1.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.27.0 (latest)  1.23.0  1.22.0  1.21.0  1.19.0  1.16.0  1.15.0  1.13.0  1.11.0  1.10.0  1.8.0  1.6.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface LfpInventoryOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAvailability()
    
    
    public abstract String getAvailability()

Required. Availability of the product at this store. For accepted attribute values, see the [local product inventory data specification](https://support.google.com/merchants/answer/3061342)

`string availability = 9 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The availability.  
  
### getAvailabilityBytes()
    
    
    public abstract ByteString getAvailabilityBytes()

Required. Availability of the product at this store. For accepted attribute values, see the [local product inventory data specification](https://support.google.com/merchants/answer/3061342)

`string availability = 9 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for availability.  
  
### getCollectionTime()
    
    
    public abstract Timestamp getCollectionTime()

Optional. The time when the inventory is collected. If not set, it will be set to the time when the inventory is submitted.

` .google.protobuf.Timestamp collection_time = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The collectionTime.  
  
### getCollectionTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCollectionTimeOrBuilder()

Optional. The time when the inventory is collected. If not set, it will be set to the time when the inventory is submitted.

` .google.protobuf.Timestamp collection_time = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getContentLanguage()
    
    
    public abstract String getContentLanguage()

Required. The two-letter ISO 639-1 language code for the item.

`string content_language = 6 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The contentLanguage.  
  
### getContentLanguageBytes()
    
    
    public abstract ByteString getContentLanguageBytes()

Required. The two-letter ISO 639-1 language code for the item.

`string content_language = 6 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for contentLanguage.  
  
### getFeedLabel()
    
    
    public abstract String getFeedLabel()

Optional. The [feed label](https://developers.google.com/shopping-content/guides/products/feed-labels) for the product. If this is not set, it will default to `regionCode`.

`optional string feed_label = 14 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The feedLabel.  
  
### getFeedLabelBytes()
    
    
    public abstract ByteString getFeedLabelBytes()

Optional. The [feed label](https://developers.google.com/shopping-content/guides/products/feed-labels) for the product. If this is not set, it will default to `regionCode`.

`optional string feed_label = 14 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for feedLabel.  
  
### getGtin()
    
    
    public abstract String getGtin()

Optional. The Global Trade Item Number of the product.

`optional string gtin = 7 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The gtin.  
  
### getGtinBytes()
    
    
    public abstract ByteString getGtinBytes()

Optional. The Global Trade Item Number of the product.

`optional string gtin = 7 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for gtin.  
  
### getName()
    
    
    public abstract String getName()

Output only. Identifier. The name for the `LfpInventory` resource. Format: `accounts/{account}/lfpInventories/{target_merchant}~{store_code}~{offer}`

` string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.field_behavior) = IDENTIFIER]; `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Output only. Identifier. The name for the `LfpInventory` resource. Format: `accounts/{account}/lfpInventories/{target_merchant}~{store_code}~{offer}`

` string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.field_behavior) = IDENTIFIER]; `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getOfferId()
    
    
    public abstract String getOfferId()

Required. Immutable. A unique identifier for the product. If both inventories and sales are submitted for a merchant, this id should match for the same product.

**Note** : if the merchant sells the same product new and used, they should have different IDs.

` string offer_id = 4 [(.google.api.field_behavior) = REQUIRED, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The offerId.  
  
### getOfferIdBytes()
    
    
    public abstract ByteString getOfferIdBytes()

Required. Immutable. A unique identifier for the product. If both inventories and sales are submitted for a merchant, this id should match for the same product.

**Note** : if the merchant sells the same product new and used, they should have different IDs.

` string offer_id = 4 [(.google.api.field_behavior) = REQUIRED, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for offerId.  
  
### getPickupMethod()
    
    
    public abstract String getPickupMethod()

Optional. Supported pickup method for this offer. Unless the value is "not supported", this field must be submitted together with `pickupSla`. For accepted attribute values, see the [local product inventory data specification](https://support.google.com/merchants/answer/3061342).

`optional string pickup_method = 12 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The pickupMethod.  
  
### getPickupMethodBytes()
    
    
    public abstract ByteString getPickupMethodBytes()

Optional. Supported pickup method for this offer. Unless the value is "not supported", this field must be submitted together with `pickupSla`. For accepted attribute values, see the [local product inventory data specification](https://support.google.com/merchants/answer/3061342).

`optional string pickup_method = 12 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for pickupMethod.  
  
### getPickupSla()
    
    
    public abstract String getPickupSla()

Optional. Expected date that an order will be ready for pickup relative to the order date. Must be submitted together with `pickupMethod`. For accepted attribute values, see the [local product inventory data specification](https://support.google.com/merchants/answer/3061342).

`optional string pickup_sla = 13 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The pickupSla.  
  
### getPickupSlaBytes()
    
    
    public abstract ByteString getPickupSlaBytes()

Optional. Expected date that an order will be ready for pickup relative to the order date. Must be submitted together with `pickupMethod`. For accepted attribute values, see the [local product inventory data specification](https://support.google.com/merchants/answer/3061342).

`optional string pickup_sla = 13 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for pickupSla.  
  
### getPrice()
    
    
    public abstract Price getPrice()

Optional. The current price of the product.

`.google.shopping.type.Price price = 8 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`com.google.shopping.type.Price` | The price.  
  
### getPriceOrBuilder()
    
    
    public abstract PriceOrBuilder getPriceOrBuilder()

Optional. The current price of the product.

`.google.shopping.type.Price price = 8 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`com.google.shopping.type.PriceOrBuilder` |   
  
### getQuantity()
    
    
    public abstract long getQuantity()

Optional. Quantity of the product available at this store. Must be greater than or equal to zero.

`optional int64 quantity = 10 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The quantity.  
  
### getRegionCode()
    
    
    public abstract String getRegionCode()

Required. The [CLDR territory code](https://github.com/unicode-org/cldr/blob/latest/common/main/en.xml) for the country where the product is sold.

`string region_code = 5 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The regionCode.  
  
### getRegionCodeBytes()
    
    
    public abstract ByteString getRegionCodeBytes()

Required. The [CLDR territory code](https://github.com/unicode-org/cldr/blob/latest/common/main/en.xml) for the country where the product is sold.

`string region_code = 5 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for regionCode.  
  
### getStoreCode()
    
    
    public abstract String getStoreCode()

Required. The identifier of the merchant's store. Either the store code inserted through `InsertLfpStore` or the store code in the Business Profile.

`string store_code = 3 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The storeCode.  
  
### getStoreCodeBytes()
    
    
    public abstract ByteString getStoreCodeBytes()

Required. The identifier of the merchant's store. Either the store code inserted through `InsertLfpStore` or the store code in the Business Profile.

`string store_code = 3 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for storeCode.  
  
### getTargetAccount()
    
    
    public abstract long getTargetAccount()

Required. The Merchant Center ID of the merchant to submit the inventory for.

`int64 target_account = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The targetAccount.  
  
### hasCollectionTime()
    
    
    public abstract boolean hasCollectionTime()

Optional. The time when the inventory is collected. If not set, it will be set to the time when the inventory is submitted.

` .google.protobuf.Timestamp collection_time = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the collectionTime field is set.  
  
### hasFeedLabel()
    
    
    public abstract boolean hasFeedLabel()

Optional. The [feed label](https://developers.google.com/shopping-content/guides/products/feed-labels) for the product. If this is not set, it will default to `regionCode`.

`optional string feed_label = 14 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the feedLabel field is set.  
  
### hasGtin()
    
    
    public abstract boolean hasGtin()

Optional. The Global Trade Item Number of the product.

`optional string gtin = 7 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the gtin field is set.  
  
### hasPickupMethod()
    
    
    public abstract boolean hasPickupMethod()

Optional. Supported pickup method for this offer. Unless the value is "not supported", this field must be submitted together with `pickupSla`. For accepted attribute values, see the [local product inventory data specification](https://support.google.com/merchants/answer/3061342).

`optional string pickup_method = 12 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the pickupMethod field is set.  
  
### hasPickupSla()
    
    
    public abstract boolean hasPickupSla()

Optional. Expected date that an order will be ready for pickup relative to the order date. Must be submitted together with `pickupMethod`. For accepted attribute values, see the [local product inventory data specification](https://support.google.com/merchants/answer/3061342).

`optional string pickup_sla = 13 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the pickupSla field is set.  
  
### hasPrice()
    
    
    public abstract boolean hasPrice()

Optional. The current price of the product.

`.google.shopping.type.Price price = 8 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the price field is set.  
  
### hasQuantity()
    
    
    public abstract boolean hasQuantity()

Optional. Quantity of the product available at this store. Must be greater than or equal to zero.

`optional int64 quantity = 10 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the quantity field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
