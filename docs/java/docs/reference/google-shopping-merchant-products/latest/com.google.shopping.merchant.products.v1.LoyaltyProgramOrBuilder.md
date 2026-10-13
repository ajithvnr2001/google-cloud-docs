---
url: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.LoyaltyProgramOrBuilder
title: Interface LoyaltyProgramOrBuilder (1.27.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:34:34.056977+00:00
---

# Interface LoyaltyProgramOrBuilder (1.27.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.LoyaltyProgramOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface LoyaltyProgramOrBuilder (1.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.27.0 (latest)  1.23.0  1.22.0  1.21.0  1.19.0  1.16.0  1.15.0  1.13.0  1.11.0  1.10.0  1.8.0  1.6.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.26.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface LoyaltyProgramOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCashbackForFutureUse()
    
    
    public abstract Price getCashbackForFutureUse()

The cashback that can be used for future purchases.

`optional .google.shopping.type.Price cashback_for_future_use = 4;`

**Returns**  
---  
**Type** | **Description**  
`com.google.shopping.type.Price` | The cashbackForFutureUse.  
  
### getCashbackForFutureUseOrBuilder()
    
    
    public abstract PriceOrBuilder getCashbackForFutureUseOrBuilder()

The cashback that can be used for future purchases.

`optional .google.shopping.type.Price cashback_for_future_use = 4;`

**Returns**  
---  
**Type** | **Description**  
`com.google.shopping.type.PriceOrBuilder` |   
  
### getLoyaltyPoints()
    
    
    public abstract long getLoyaltyPoints()

The amount of loyalty points earned on a purchase.

`optional int64 loyalty_points = 5;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The loyaltyPoints.  
  
### getMemberPriceEffectiveDate()
    
    
    public abstract Interval getMemberPriceEffectiveDate()

A date range during which the item is eligible for member price. If not specified, the member price is always applicable. The date range is represented by a pair of ISO 8601 dates separated by a space, comma, or slash.

`optional .google.type.Interval member_price_effective_date = 6;`

**Returns**  
---  
**Type** | **Description**  
`com.google.type.Interval` | The memberPriceEffectiveDate.  
  
### getMemberPriceEffectiveDateOrBuilder()
    
    
    public abstract IntervalOrBuilder getMemberPriceEffectiveDateOrBuilder()

A date range during which the item is eligible for member price. If not specified, the member price is always applicable. The date range is represented by a pair of ISO 8601 dates separated by a space, comma, or slash.

`optional .google.type.Interval member_price_effective_date = 6;`

**Returns**  
---  
**Type** | **Description**  
`com.google.type.IntervalOrBuilder` |   
  
### getPrice()
    
    
    public abstract Price getPrice()

The price for members of the given tier, that is, the instant discount price. Must be smaller or equal to the regular price.

`optional .google.shopping.type.Price price = 3;`

**Returns**  
---  
**Type** | **Description**  
`com.google.shopping.type.Price` | The price.  
  
### getPriceOrBuilder()
    
    
    public abstract PriceOrBuilder getPriceOrBuilder()

The price for members of the given tier, that is, the instant discount price. Must be smaller or equal to the regular price.

`optional .google.shopping.type.Price price = 3;`

**Returns**  
---  
**Type** | **Description**  
`com.google.shopping.type.PriceOrBuilder` |   
  
### getProgramLabel()
    
    
    public abstract String getProgramLabel()

The label of the loyalty program. This is an internal label that uniquely identifies the relationship between a business entity and a loyalty program entity. The label must be provided so that the system can associate the assets below (for example, price and points) with a business. The corresponding program must be linked to the Merchant Center account.

`optional string program_label = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The programLabel.  
  
### getProgramLabelBytes()
    
    
    public abstract ByteString getProgramLabelBytes()

The label of the loyalty program. This is an internal label that uniquely identifies the relationship between a business entity and a loyalty program entity. The label must be provided so that the system can associate the assets below (for example, price and points) with a business. The corresponding program must be linked to the Merchant Center account.

`optional string program_label = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for programLabel.  
  
### getShippingLabel()
    
    
    public abstract String getShippingLabel()

The label of the shipping benefit. If the field has value, this offer has loyalty shipping benefit. If the field value isn't provided, the item is not eligible for loyalty shipping for the given loyalty tier.

`optional string shipping_label = 7;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The shippingLabel.  
  
### getShippingLabelBytes()
    
    
    public abstract ByteString getShippingLabelBytes()

The label of the shipping benefit. If the field has value, this offer has loyalty shipping benefit. If the field value isn't provided, the item is not eligible for loyalty shipping for the given loyalty tier.

`optional string shipping_label = 7;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for shippingLabel.  
  
### getTierLabel()
    
    
    public abstract String getTierLabel()

The label of the tier within the loyalty program. Must match one of the labels within the program.

`optional string tier_label = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The tierLabel.  
  
### getTierLabelBytes()
    
    
    public abstract ByteString getTierLabelBytes()

The label of the tier within the loyalty program. Must match one of the labels within the program.

`optional string tier_label = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for tierLabel.  
  
### hasCashbackForFutureUse()
    
    
    public abstract boolean hasCashbackForFutureUse()

The cashback that can be used for future purchases.

`optional .google.shopping.type.Price cashback_for_future_use = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the cashbackForFutureUse field is set.  
  
### hasLoyaltyPoints()
    
    
    public abstract boolean hasLoyaltyPoints()

The amount of loyalty points earned on a purchase.

`optional int64 loyalty_points = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the loyaltyPoints field is set.  
  
### hasMemberPriceEffectiveDate()
    
    
    public abstract boolean hasMemberPriceEffectiveDate()

A date range during which the item is eligible for member price. If not specified, the member price is always applicable. The date range is represented by a pair of ISO 8601 dates separated by a space, comma, or slash.

`optional .google.type.Interval member_price_effective_date = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the memberPriceEffectiveDate field is set.  
  
### hasPrice()
    
    
    public abstract boolean hasPrice()

The price for members of the given tier, that is, the instant discount price. Must be smaller or equal to the regular price.

`optional .google.shopping.type.Price price = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the price field is set.  
  
### hasProgramLabel()
    
    
    public abstract boolean hasProgramLabel()

The label of the loyalty program. This is an internal label that uniquely identifies the relationship between a business entity and a loyalty program entity. The label must be provided so that the system can associate the assets below (for example, price and points) with a business. The corresponding program must be linked to the Merchant Center account.

`optional string program_label = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the programLabel field is set.  
  
### hasShippingLabel()
    
    
    public abstract boolean hasShippingLabel()

The label of the shipping benefit. If the field has value, this offer has loyalty shipping benefit. If the field value isn't provided, the item is not eligible for loyalty shipping for the given loyalty tier.

`optional string shipping_label = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the shippingLabel field is set.  
  
### hasTierLabel()
    
    
    public abstract boolean hasTierLabel()

The label of the tier within the loyalty program. Must match one of the labels within the program.

`optional string tier_label = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the tierLabel field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
