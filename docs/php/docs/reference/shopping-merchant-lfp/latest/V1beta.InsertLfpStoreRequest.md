---
url: https://docs.cloud.google.com/php/docs/reference/shopping-merchant-lfp/latest/V1beta.InsertLfpStoreRequest
title: Google Shopping Merchant Lfp V1beta Client - Class InsertLfpStoreRequest (1.2.6) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:09:04.207307+00:00
---

# Google Shopping Merchant Lfp V1beta Client - Class InsertLfpStoreRequest (1.2.6)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/shopping-merchant-lfp/latest/V1beta.InsertLfpStoreRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Shopping Merchant Lfp V1beta Client - Class InsertLfpStoreRequest (1.2.6) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.6 (latest)  1.2.1  1.1.3  1.0.0  0.4.0  0.3.2  0.2.0  0.1.3 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Shopping Merchant Lfp V1beta Client class InsertLfpStoreRequest.

Request message for the InsertLfpStore method.

Generated from protobuf message `google.shopping.merchant.lfp.v1beta.InsertLfpStoreRequest`

## Namespace

Google \ Shopping \ Merchant \ Lfp \ V1beta

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ parent` |  `string`   
Required. The LFP provider account Format: `accounts/{account}`  
`↳ lfp_store` |  `[LfpStore](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-lfp/latest/V1beta.LfpStore)`   
Required. The store to insert.  
  
### getParent

Required. The LFP provider account Format: `accounts/{account}`

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setParent

Required. The LFP provider account Format: `accounts/{account}`

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getLfpStore

Required. The store to insert.

**Returns**  
---  
**Type** | **Description**  
`[LfpStore](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-lfp/latest/V1beta.LfpStore)|null` |   
  
### hasLfpStore

### clearLfpStore

### setLfpStore

Required. The store to insert.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[LfpStore](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-lfp/latest/V1beta.LfpStore)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### static::build

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `string`   
Required. The LFP provider account Format: `accounts/{account}` Please see LfpStoreServiceClient::accountName() for help formatting this field.  
`lfpStore` |  `[LfpStore](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-lfp/latest/V1beta.LfpStore)`   
Required. The store to insert.  
**Returns**  
---  
**Type** | **Description**  
`[InsertLfpStoreRequest](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-lfp/latest/V1beta.InsertLfpStoreRequest)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
