---
url: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1.OnlineReturnPolicy.RestockingFeeOrBuilder
title: Interface OnlineReturnPolicy.RestockingFeeOrBuilder (1.27.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:24:44.133443+00:00
---

# Interface OnlineReturnPolicy.RestockingFeeOrBuilder (1.27.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1.OnlineReturnPolicy.RestockingFeeOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface OnlineReturnPolicy.RestockingFeeOrBuilder (1.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.27.0 (latest)  1.23.0  1.22.0  1.21.0  1.19.0  1.16.0  1.15.0  1.13.0  1.11.0  1.10.0  1.8.0  1.6.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.26.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static interface OnlineReturnPolicy.RestockingFeeOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getFixedFee()
    
    
    public abstract Price getFixedFee()

Fixed restocking fee.

`.google.shopping.type.Price fixed_fee = 1;`

**Returns**  
---  
**Type** | **Description**  
`com.google.shopping.type.Price` | The fixedFee.  
  
### getFixedFeeOrBuilder()
    
    
    public abstract PriceOrBuilder getFixedFeeOrBuilder()

Fixed restocking fee.

`.google.shopping.type.Price fixed_fee = 1;`

**Returns**  
---  
**Type** | **Description**  
`com.google.shopping.type.PriceOrBuilder` |   
  
### getMicroPercent()
    
    
    public abstract int getMicroPercent()

Percent of total price in micros. 15,000,000 means 15% of the total price would be charged.

`int32 micro_percent = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The microPercent.  
  
### getTypeCase()
    
    
    public abstract OnlineReturnPolicy.RestockingFee.TypeCase getTypeCase()

**Returns**  
---  
**Type** | **Description**  
`[OnlineReturnPolicy.RestockingFee.TypeCase](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1.OnlineReturnPolicy.RestockingFee.TypeCase)` |   
  
### hasFixedFee()
    
    
    public abstract boolean hasFixedFee()

Fixed restocking fee.

`.google.shopping.type.Price fixed_fee = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the fixedFee field is set.  
  
### hasMicroPercent()
    
    
    public abstract boolean hasMicroPercent()

Percent of total price in micros. 15,000,000 means 15% of the total price would be charged.

`int32 micro_percent = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the microPercent field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
