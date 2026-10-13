---
url: https://docs.cloud.google.com/php/docs/reference/shopping-merchant-ordertracking/latest/V1beta.OrderTrackingSignal.LineItemDetails
title: Google Shopping Merchant Order Tracking V1beta Client - Class LineItemDetails (1.2.6) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:43:08.338042+00:00
---

# Google Shopping Merchant Order Tracking V1beta Client - Class LineItemDetails (1.2.6)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/shopping-merchant-ordertracking/latest/V1beta.OrderTrackingSignal.LineItemDetails

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Shopping Merchant Order Tracking V1beta Client - Class LineItemDetails (1.2.6) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.6 (latest)  1.2.1  1.1.3  1.0.0  0.2.0  0.1.1 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Shopping Merchant Order Tracking V1beta Client class LineItemDetails.

The line items of the order.

Generated from protobuf message `google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal.LineItemDetails`

## Namespace

Google \ Shopping \ Merchant \ OrderTracking \ V1beta \ OrderTrackingSignal

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ line_item_id` |  `string`   
Required. The ID for this line item.  
`↳ product_id` |  `string`   
Required. The Content API REST ID of the product, in the form channel:contentLanguage:targetCountry:offerId.  
`↳ gtin` |  `string`   
Optional. The Global Trade Item Number.  
`↳ mpn` |  `string`   
Optional. The manufacturer part number.  
`↳ product_title` |  `string`   
Optional. Plain text title of this product.  
`↳ brand` |  `string`   
Optional. Brand of the product.  
`↳ quantity` |  `int|string`   
Required. The quantity of the line item in the order.  
  
### getLineItemId

Required. The ID for this line item.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setLineItemId

Required. The ID for this line item.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getProductId

Required. The Content API REST ID of the product, in the form channel:contentLanguage:targetCountry:offerId.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setProductId

Required. The Content API REST ID of the product, in the form channel:contentLanguage:targetCountry:offerId.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getGtin

Optional. The Global Trade Item Number.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setGtin

Optional. The Global Trade Item Number.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getMpn

Optional. The manufacturer part number.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setMpn

Optional. The manufacturer part number.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getProductTitle

Optional. Plain text title of this product.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### hasProductTitle

### clearProductTitle

### setProductTitle

Optional. Plain text title of this product.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getBrand

Optional. Brand of the product.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### hasBrand

### clearBrand

### setBrand

Optional. Brand of the product.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getQuantity

Required. The quantity of the line item in the order.

**Returns**  
---  
**Type** | **Description**  
`int|string` |   
  
### setQuantity

Required. The quantity of the line item in the order.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int|string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
