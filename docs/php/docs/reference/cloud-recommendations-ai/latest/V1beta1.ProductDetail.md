---
url: https://docs.cloud.google.com/php/docs/reference/cloud-recommendations-ai/latest/V1beta1.ProductDetail
title: Google Cloud Recommendation Engine V1beta1 Client - Class ProductDetail (0.10.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:11:07.946690+00:00
---

# Google Cloud Recommendation Engine V1beta1 Client - Class ProductDetail (0.10.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-recommendations-ai/latest/V1beta1.ProductDetail

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Recommendation Engine V1beta1 Client - Class ProductDetail (0.10.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.3 (latest)  0.9.3  0.8.2  0.7.7  0.6.4  0.5.0  0.4.12 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Recommendation Engine V1beta1 Client class ProductDetail.

Detailed product information associated with a user event.

Generated from protobuf message `google.cloud.recommendationengine.v1beta1.ProductDetail`

## Namespace

Google \ Cloud \ RecommendationEngine \ V1beta1

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ id` |  `string`   
Required. Catalog item ID. UTF-8 encoded string with a length limit of 128 characters.  
`↳ currency_code` |  `string`   
Optional. Currency code for price/costs. Use three-character ISO-4217 code. Required only if originalPrice or displayPrice is set.  
`↳ original_price` |  `float`   
Optional. Original price of the product. If provided, this will override the original price in Catalog for this product.  
`↳ display_price` |  `float`   
Optional. Display price of the product (e.g. discounted price). If provided, this will override the display price in Catalog for this product.  
`↳ stock_state` |  `int`   
Optional. Item stock state. If provided, this overrides the stock state in Catalog for items in this event.  
`↳ quantity` |  `int`   
Optional. Quantity of the product associated with the user event. For example, this field will be 2 if two products are added to the shopping cart for `add-to-cart` event. Required for `add-to-cart`, `add-to-list`, `remove-from-cart`, `checkout-start`, `purchase-complete`, `refund` event types.  
`↳ available_quantity` |  `int`   
Optional. Quantity of the products in stock when a user event happens. Optional. If provided, this overrides the available quantity in Catalog for this event. and can only be set if `stock_status` is set to `IN_STOCK`. Note that if an item is out of stock, you must set the `stock_state` field to be `OUT_OF_STOCK`. Leaving this field unspecified / as zero is not sufficient to mark the item out of stock.  
`↳ item_attributes` |  `[FeatureMap](https://docs.cloud.google.com/php/docs/reference/cloud-recommendations-ai/latest/V1beta1.FeatureMap)`   
Optional. Extra features associated with a product in the user event.  
  
### getId

Required. Catalog item ID. UTF-8 encoded string with a length limit of 128 characters.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setId

Required. Catalog item ID. UTF-8 encoded string with a length limit of 128 characters.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCurrencyCode

Optional. Currency code for price/costs. Use three-character ISO-4217 code. Required only if originalPrice or displayPrice is set.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setCurrencyCode

Optional. Currency code for price/costs. Use three-character ISO-4217 code. Required only if originalPrice or displayPrice is set.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getOriginalPrice

Optional. Original price of the product. If provided, this will override the original price in Catalog for this product.

**Returns**  
---  
**Type** | **Description**  
`float` |   
  
### setOriginalPrice

Optional. Original price of the product. If provided, this will override the original price in Catalog for this product.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `float`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDisplayPrice

Optional. Display price of the product (e.g. discounted price). If provided, this will override the display price in Catalog for this product.

**Returns**  
---  
**Type** | **Description**  
`float` |   
  
### setDisplayPrice

Optional. Display price of the product (e.g. discounted price). If provided, this will override the display price in Catalog for this product.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `float`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getStockState

Optional. Item stock state. If provided, this overrides the stock state in Catalog for items in this event.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [StockState](https://docs.cloud.google.com/php/docs/reference/cloud-recommendations-ai/latest/V1beta1.ProductCatalogItem.StockState).  
  
### setStockState

Optional. Item stock state. If provided, this overrides the stock state in Catalog for items in this event.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [StockState](https://docs.cloud.google.com/php/docs/reference/cloud-recommendations-ai/latest/V1beta1.ProductCatalogItem.StockState).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getQuantity

Optional. Quantity of the product associated with the user event. For example, this field will be 2 if two products are added to the shopping cart for `add-to-cart` event. Required for `add-to-cart`, `add-to-list`, `remove-from-cart`, `checkout-start`, `purchase-complete`, `refund` event types.

**Returns**  
---  
**Type** | **Description**  
`int` |   
  
### setQuantity

Optional. Quantity of the product associated with the user event. For example, this field will be 2 if two products are added to the shopping cart for `add-to-cart` event. Required for `add-to-cart`, `add-to-list`, `remove-from-cart`, `checkout-start`, `purchase-complete`, `refund` event types.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getAvailableQuantity

Optional. Quantity of the products in stock when a user event happens.

Optional. If provided, this overrides the available quantity in Catalog for this event. and can only be set if `stock_status` is set to `IN_STOCK`. Note that if an item is out of stock, you must set the `stock_state` field to be `OUT_OF_STOCK`. Leaving this field unspecified / as zero is not sufficient to mark the item out of stock.

**Returns**  
---  
**Type** | **Description**  
`int` |   
  
### setAvailableQuantity

Optional. Quantity of the products in stock when a user event happens.

Optional. If provided, this overrides the available quantity in Catalog for this event. and can only be set if `stock_status` is set to `IN_STOCK`. Note that if an item is out of stock, you must set the `stock_state` field to be `OUT_OF_STOCK`. Leaving this field unspecified / as zero is not sufficient to mark the item out of stock.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getItemAttributes

Optional. Extra features associated with a product in the user event.

**Returns**  
---  
**Type** | **Description**  
`[FeatureMap](https://docs.cloud.google.com/php/docs/reference/cloud-recommendations-ai/latest/V1beta1.FeatureMap)|null` |   
  
### hasItemAttributes

### clearItemAttributes

### setItemAttributes

Optional. Extra features associated with a product in the user event.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[FeatureMap](https://docs.cloud.google.com/php/docs/reference/cloud-recommendations-ai/latest/V1beta1.FeatureMap)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
