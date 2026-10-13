---
url: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1beta.CarrierRateOrBuilder
title: Interface CarrierRateOrBuilder (1.27.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:32:50.510918+00:00
---

# Interface CarrierRateOrBuilder (1.27.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1beta.CarrierRateOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface CarrierRateOrBuilder (1.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.27.0 (latest)  1.23.0  1.22.0  1.21.0  1.19.0  1.16.0  1.15.0  1.13.0  1.11.0  1.10.0  1.8.0  1.6.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.26.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface CarrierRateOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCarrier()
    
    
    public abstract String getCarrier()

Required. Carrier service, such as `"UPS"` or `"Fedex"`.

`optional string carrier = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The carrier.  
  
### getCarrierBytes()
    
    
    public abstract ByteString getCarrierBytes()

Required. Carrier service, such as `"UPS"` or `"Fedex"`.

`optional string carrier = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for carrier.  
  
### getCarrierService()
    
    
    public abstract String getCarrierService()

Required. Carrier service, such as `"ground"` or `"2 days"`.

`optional string carrier_service = 3 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The carrierService.  
  
### getCarrierServiceBytes()
    
    
    public abstract ByteString getCarrierServiceBytes()

Required. Carrier service, such as `"ground"` or `"2 days"`.

`optional string carrier_service = 3 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for carrierService.  
  
### getFlatAdjustment()
    
    
    public abstract Price getFlatAdjustment()

Optional. Additive shipping rate modifier. Can be negative. For example `{ "amount_micros": 1, "currency_code" : "USD" }` adds $1 to the rate, `{ "amount_micros": -3, "currency_code" : "USD" }` removes $3 from the rate.

` optional .google.shopping.type.Price flat_adjustment = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`com.google.shopping.type.Price` | The flatAdjustment.  
  
### getFlatAdjustmentOrBuilder()
    
    
    public abstract PriceOrBuilder getFlatAdjustmentOrBuilder()

Optional. Additive shipping rate modifier. Can be negative. For example `{ "amount_micros": 1, "currency_code" : "USD" }` adds $1 to the rate, `{ "amount_micros": -3, "currency_code" : "USD" }` removes $3 from the rate.

` optional .google.shopping.type.Price flat_adjustment = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`com.google.shopping.type.PriceOrBuilder` |   
  
### getName()
    
    
    public abstract String getName()

Required. Name of the carrier rate. Must be unique per rate group.

`optional string name = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Required. Name of the carrier rate. Must be unique per rate group.

`optional string name = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getOriginPostalCode()
    
    
    public abstract String getOriginPostalCode()

Required. Shipping origin for this carrier rate.

`optional string origin_postal_code = 4 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The originPostalCode.  
  
### getOriginPostalCodeBytes()
    
    
    public abstract ByteString getOriginPostalCodeBytes()

Required. Shipping origin for this carrier rate.

`optional string origin_postal_code = 4 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for originPostalCode.  
  
### getPercentageAdjustment()
    
    
    public abstract String getPercentageAdjustment()

Optional. Multiplicative shipping rate modifier as a number in decimal notation. Can be negative. For example `"5.4"` increases the rate by 5.4%, `"-3"` decreases the rate by 3%.

`optional string percentage_adjustment = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The percentageAdjustment.  
  
### getPercentageAdjustmentBytes()
    
    
    public abstract ByteString getPercentageAdjustmentBytes()

Optional. Multiplicative shipping rate modifier as a number in decimal notation. Can be negative. For example `"5.4"` increases the rate by 5.4%, `"-3"` decreases the rate by 3%.

`optional string percentage_adjustment = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for percentageAdjustment.  
  
### hasCarrier()
    
    
    public abstract boolean hasCarrier()

Required. Carrier service, such as `"UPS"` or `"Fedex"`.

`optional string carrier = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the carrier field is set.  
  
### hasCarrierService()
    
    
    public abstract boolean hasCarrierService()

Required. Carrier service, such as `"ground"` or `"2 days"`.

`optional string carrier_service = 3 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the carrierService field is set.  
  
### hasFlatAdjustment()
    
    
    public abstract boolean hasFlatAdjustment()

Optional. Additive shipping rate modifier. Can be negative. For example `{ "amount_micros": 1, "currency_code" : "USD" }` adds $1 to the rate, `{ "amount_micros": -3, "currency_code" : "USD" }` removes $3 from the rate.

` optional .google.shopping.type.Price flat_adjustment = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the flatAdjustment field is set.  
  
### hasName()
    
    
    public abstract boolean hasName()

Required. Name of the carrier rate. Must be unique per rate group.

`optional string name = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the name field is set.  
  
### hasOriginPostalCode()
    
    
    public abstract boolean hasOriginPostalCode()

Required. Shipping origin for this carrier rate.

`optional string origin_postal_code = 4 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the originPostalCode field is set.  
  
### hasPercentageAdjustment()
    
    
    public abstract boolean hasPercentageAdjustment()

Optional. Multiplicative shipping rate modifier as a number in decimal notation. Can be negative. For example `"5.4"` increases the rate by 5.4%, `"-3"` decreases the rate by 3%.

`optional string percentage_adjustment = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the percentageAdjustment field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
