---
url: https://docs.cloud.google.com/bigquery/docs/merchant-center-product-targeting-schema/
title: Google Merchant Center product targeting table \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:44:48.365290+00:00
---

# Google Merchant Center product targeting table  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/merchant-center-product-targeting-schema/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Reference ](https://docs.cloud.google.com/bigquery/quotas)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Google Merchant Center product targeting table

## Overview

Product targeting data helps merchants understand which products are targeted by the Shopping and Performance Max campaigns in each linked advertiser account that they can access.

  * All campaign targeting parameters are considered, such as [listing groups](https://support.google.com/google-ads/answer/11596074), [product groups](https://support.google.com/google-ads/answer/6275317), and [feed labels](https://support.google.com/merchants/answer/14994087).
  * Only active campaigns with active ad groups or asset groups are considered.
  * To compute the `targeting_status`, we only consider advertiser accounts that are accessible to the user who owns the BigQuery export. For more information, see [Manage access to your Google Ads account](https://support.google.com/google-ads/answer/6372672).



## Table name

If you choose the **Product Targeting** report option when you [set up a Google Merchant Center transfer](https://docs.cloud.google.com/bigquery/docs/merchant-center-transfer-schedule-transfers#set_up_a_google_merchant_center_transfer), BigQuery creates a table for the data during the transfer. The table name starts with the `ProductTargeting_` prefix:

  * If you configured the transfer with an individual merchant ID, the table name is `ProductTargeting_MERCHANT_ID`.
  * If you configured the transfer with an MCA account, the table name is `ProductTargeting_AGGREGATOR_ID`.



## Schema

The product targeting table has the following schema:

Name | Type | Description | Example data  
---|---|---|---  
`product_id` | `STRING` | The Content API REST ID for the product is in the format: `channel:content_language:feed_label:offer_id`. This field is a primary key. | online:en:AU:666840730  
`**advertiser_id**` | `INTEGER` | Advertiser ID of the campaign. This field is a primary key. | 4321  
`targeting_status` | `STRING` | Whether the product is targeted by Ads campaigns.  
**Note:** Products targeted by Ads campaigns might not be eligible to serve. To check if your products are eligible, use the `destinations.status` field of the [ products report](https://docs.cloud.google.com/bigquery/docs/merchant-center-products-schema).  | TARGETED, NOT_TARGETED  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
