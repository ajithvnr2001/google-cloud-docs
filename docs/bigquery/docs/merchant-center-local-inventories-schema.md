---
url: https://docs.cloud.google.com/bigquery/docs/merchant-center-local-inventories-schema/
title: Google Merchant Center local inventories table \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:36:03.643167+00:00
---

# Google Merchant Center local inventories table  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/merchant-center-local-inventories-schema/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Reference ](https://docs.cloud.google.com/bigquery/quotas)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Google Merchant Center local inventories table

## Overview

Local inventories data allows merchants to export their local offers of their products to BigQuery. This data includes pricing, availability, and quantity of the product along with the information about pick-up and product in-store location.

The format of local inventories data corresponds primarily to the format of the relevant fields of the Content API's [`localinventory`](https://developers.google.com/shopping-content/reference/rest/v2.1/localinventory) resource.

Depending on the type of Merchant account that you use, the data is written to one of the following tables:

  * If you are using an individual Merchant ID, then the data is written to the `LocalInventories_MERCHANT_ID` table.
  * If you are using an MCA account, then the data is written to the `LocalInventories_AGGREGATOR_ID` table.



## Schema

The `LocalInventories_` tables have the following schema:

**Column** | **BigQuery data type** | **Description** | **Example data**  
---|---|---|---  
`**product_id**` | `STRING` | Content API's REST ID of the product in the form: `channel:content_language:feed_label:offer_id`. This field is a primary key. | online:en:AU:666840730  
`**merchant_id**` | `INTEGER` | Merchant account ID. This field is a primary key. |   
`aggregator_id` | `INTEGER` | ID of the [Multi Client Account (MCA)](https://support.google.com/merchants/answer/188487). |   
`store_code` | `STRING` | Store code of this local inventory resource. |   
`price` | `RECORD` | Local price of the item. |   
`price.value` | `NUMERIC` | Local price of the item. | 99  
`price.currency` | `STRING` | Currency of the local price of the item. | CHF  
`sale_price` | `RECORD` | Local sale price of the item. |   
`sale_price.value` | `NUMERIC` | Local sale price of the item. | 49  
`sale_price.currency` | `STRING` | Currency of the local sale price of the item. | CHF  
`sale_price_effective_start_date` | `TIMESTAMP` | Start date and time when the item is on sale. | 2021-03-30 00:00:00 UTC  
`sale_price_effective_end_date` | `TIMESTAMP` | End date and time when the item is on sale. | 2021-04-14 00:00:00 UTC  
`availability` | `STRING` | Local availability status of the item. | out of stock  
`quantity` | `INTEGER` | Quantity of the item. | 500  
`pickup_method` | `STRING` | Supported pick-up method of the item. | ship to store  
`pickup_sla` | `STRING` | Expected elapsed time between the order date and the date that the item is ready for pickup. | three days  
`instore_product_location` | `STRING` | In-store location of the item. |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
