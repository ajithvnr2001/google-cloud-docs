---
url: https://docs.cloud.google.com/php/docs/reference/shopping-merchant-products/latest/V1beta.Installment
title: Google Shopping Merchant Products V1beta Client - Class Installment (1.8.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:18:37.648021+00:00
---

# Google Shopping Merchant Products V1beta Client - Class Installment (1.8.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/shopping-merchant-products/latest/V1beta.Installment

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Shopping Merchant Products V1beta Client - Class Installment (1.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.0 (latest)  1.7.5  1.6.0  1.5.0  1.4.1  1.3.1  1.2.0  1.1.0  1.0.0  0.7.0  0.6.1  0.5.0  0.4.0  0.3.0  0.2.1  0.1.1 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Shopping Merchant Products V1beta Client class Installment.

A message that represents installment.

Generated from protobuf message `google.shopping.merchant.products.v1beta.Installment`

## Namespace

Google \ Shopping \ Merchant \ Products \ V1beta

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ months` |  `int|string`   
The number of installments the buyer has to pay.  
`↳ amount` |  `[Google\Shopping\Type\Price](https://docs.cloud.google.com/php/docs/reference/shopping-common-protos/latest/Type.Price.html)`   
The amount the buyer has to pay per month.  
`↳ downpayment` |  `[Google\Shopping\Type\Price](https://docs.cloud.google.com/php/docs/reference/shopping-common-protos/latest/Type.Price.html)`   
The up-front down payment amount the buyer has to pay.  
`↳ credit_type` |  `string`   
Type of installment payments. Supported values are: * * "`finance`" * * "`lease`"  
  
### getMonths

The number of installments the buyer has to pay.

**Returns**  
---  
**Type** | **Description**  
`int|string` |   
  
### setMonths

The number of installments the buyer has to pay.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int|string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getAmount

The amount the buyer has to pay per month.

**Returns**  
---  
**Type** | **Description**  
`[Google\Shopping\Type\Price](https://docs.cloud.google.com/php/docs/reference/shopping-common-protos/latest/Type.Price.html)|null` |   
  
### hasAmount

### clearAmount

### setAmount

The amount the buyer has to pay per month.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Shopping\Type\Price](https://docs.cloud.google.com/php/docs/reference/shopping-common-protos/latest/Type.Price.html)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDownpayment

The up-front down payment amount the buyer has to pay.

**Returns**  
---  
**Type** | **Description**  
`[Google\Shopping\Type\Price](https://docs.cloud.google.com/php/docs/reference/shopping-common-protos/latest/Type.Price.html)|null` |   
  
### hasDownpayment

### clearDownpayment

### setDownpayment

The up-front down payment amount the buyer has to pay.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Shopping\Type\Price](https://docs.cloud.google.com/php/docs/reference/shopping-common-protos/latest/Type.Price.html)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCreditType

Type of installment payments.

Supported values are:

  * "`finance`"
  * "`lease`"



**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### hasCreditType

### clearCreditType

### setCreditType

Type of installment payments.

Supported values are:

  * "`finance`"
  * "`lease`"



**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
