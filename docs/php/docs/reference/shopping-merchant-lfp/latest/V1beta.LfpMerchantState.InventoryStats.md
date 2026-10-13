---
url: https://docs.cloud.google.com/php/docs/reference/shopping-merchant-lfp/latest/V1beta.LfpMerchantState.InventoryStats
title: Google Shopping Merchant Lfp V1beta Client - Class InventoryStats (1.2.6) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:05:41.123592+00:00
---

# Google Shopping Merchant Lfp V1beta Client - Class InventoryStats (1.2.6)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/shopping-merchant-lfp/latest/V1beta.LfpMerchantState.InventoryStats

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Shopping Merchant Lfp V1beta Client - Class InventoryStats (1.2.6) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.6 (latest)  1.2.1  1.1.3  1.0.0  0.4.0  0.3.2  0.2.0  0.1.3 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Shopping Merchant Lfp V1beta Client class InventoryStats.

The inventory statistics for a merchant.

Generated from protobuf message `google.shopping.merchant.lfp.v1beta.LfpMerchantState.InventoryStats`

## Namespace

Google \ Shopping \ Merchant \ Lfp \ V1beta \ LfpMerchantState

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ submitted_entries` |  `int|string`   
Number of entries (understanding entry as a pair of product and store) that were built based on provided inventories/sales and submitted to Google.  
`↳ submitted_in_stock_entries` |  `int|string`   
Number of submitted in stock entries.  
`↳ unsubmitted_entries` |  `int|string`   
Number of entries that were built based on provided inventories/sales and couldn't be submitted to Google due to errors like missing product.  
`↳ submitted_products` |  `int|string`   
Number of products from provided inventories/sales that were created from matches to existing online products provided by the merchant or to the Google catalog.  
  
### getSubmittedEntries

Number of entries (understanding entry as a pair of product and store) that were built based on provided inventories/sales and submitted to Google.

**Returns**  
---  
**Type** | **Description**  
`int|string` |   
  
### setSubmittedEntries

Number of entries (understanding entry as a pair of product and store) that were built based on provided inventories/sales and submitted to Google.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int|string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getSubmittedInStockEntries

Number of submitted in stock entries.

**Returns**  
---  
**Type** | **Description**  
`int|string` |   
  
### setSubmittedInStockEntries

Number of submitted in stock entries.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int|string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getUnsubmittedEntries

Number of entries that were built based on provided inventories/sales and couldn't be submitted to Google due to errors like missing product.

**Returns**  
---  
**Type** | **Description**  
`int|string` |   
  
### setUnsubmittedEntries

Number of entries that were built based on provided inventories/sales and couldn't be submitted to Google due to errors like missing product.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int|string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getSubmittedProducts

Number of products from provided inventories/sales that were created from matches to existing online products provided by the merchant or to the Google catalog.

**Returns**  
---  
**Type** | **Description**  
`int|string` |   
  
### setSubmittedProducts

Number of products from provided inventories/sales that were created from matches to existing online products provided by the merchant or to the Google catalog.

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
