---
url: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-order-tracking/latest/com.google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal.LineItemDetailsOrBuilder
title: Interface OrderTrackingSignal.LineItemDetailsOrBuilder (1.27.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:48:55.103923+00:00
---

# Interface OrderTrackingSignal.LineItemDetailsOrBuilder (1.27.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-order-tracking/latest/com.google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal.LineItemDetailsOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface OrderTrackingSignal.LineItemDetailsOrBuilder (1.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.27.0 (latest)  1.23.0  1.22.0  1.21.0  1.19.0  1.16.0  1.15.0  1.13.0  1.11.0  1.10.0  1.9.0  1.8.0  1.6.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.10.0  0.8.0  0.7.0  0.4.0  0.3.0  0.2.0 
    
    
    public static interface OrderTrackingSignal.LineItemDetailsOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getBrand()
    
    
    public abstract String getBrand()

Optional. Brand of the product.

`optional string brand = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The brand.  
  
### getBrandBytes()
    
    
    public abstract ByteString getBrandBytes()

Optional. Brand of the product.

`optional string brand = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for brand.  
  
### getGtin()
    
    
    public abstract String getGtin()

Optional. The Global Trade Item Number.

`string gtin = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The gtin.  
  
### getGtinBytes()
    
    
    public abstract ByteString getGtinBytes()

Optional. The Global Trade Item Number.

`string gtin = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for gtin.  
  
### getLineItemId()
    
    
    public abstract String getLineItemId()

Required. The ID for this line item.

`string line_item_id = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The lineItemId.  
  
### getLineItemIdBytes()
    
    
    public abstract ByteString getLineItemIdBytes()

Required. The ID for this line item.

`string line_item_id = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for lineItemId.  
  
### getMpn()
    
    
    public abstract String getMpn()

Optional. The manufacturer part number.

`string mpn = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The mpn.  
  
### getMpnBytes()
    
    
    public abstract ByteString getMpnBytes()

Optional. The manufacturer part number.

`string mpn = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for mpn.  
  
### getProductId()
    
    
    public abstract String getProductId()

Required. The Content API REST ID of the product, in the form channel:contentLanguage:targetCountry:offerId.

`string product_id = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The productId.  
  
### getProductIdBytes()
    
    
    public abstract ByteString getProductIdBytes()

Required. The Content API REST ID of the product, in the form channel:contentLanguage:targetCountry:offerId.

`string product_id = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for productId.  
  
### getProductTitle()
    
    
    public abstract String getProductTitle()

Optional. Plain text title of this product.

`optional string product_title = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The productTitle.  
  
### getProductTitleBytes()
    
    
    public abstract ByteString getProductTitleBytes()

Optional. Plain text title of this product.

`optional string product_title = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for productTitle.  
  
### getQuantity()
    
    
    public abstract long getQuantity()

Required. The quantity of the line item in the order.

`int64 quantity = 7 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The quantity.  
  
### hasBrand()
    
    
    public abstract boolean hasBrand()

Optional. Brand of the product.

`optional string brand = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the brand field is set.  
  
### hasProductTitle()
    
    
    public abstract boolean hasProductTitle()

Optional. Plain text title of this product.

`optional string product_title = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the productTitle field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
