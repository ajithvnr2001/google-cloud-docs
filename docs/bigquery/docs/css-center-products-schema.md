---
url: https://docs.cloud.google.com/bigquery/docs/css-center-products-schema/
title: Comparison Shopping Services Center table schema \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:44.073726+00:00
---

# Comparison Shopping Services Center table schema  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/css-center-products-schema/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Reference ](https://docs.cloud.google.com/bigquery/quotas)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Comparison Shopping Services Center table schema

When your Comparison Shopping Service (CSS) Center reporting data is transferred to BigQuery, the format of product and product issues data corresponds primarily to the format of the relevant fields of the Content API's [`ProductView`](https://developers.google.com/shopping-content/reference/rest/v2.1/reports/search#productview) and [`Productstatuses`](https://developers.google.com/shopping-content/v2/reference/v2.1/productstatuses) resources.

## CSS Center Products Schema

The following table lists the schema for the `Products_` table. Some fields are included as subsets of other fields. For example, the `Price` field contain both `Value` and `Currency` fields.

Field name | Type | Description  
---|---|---  
CSS ID | `INTEGER` | CSS ID  
Merchant ID | `INTEGER` | Merchant account ID who owns the offer  
Product ID | `STRING` | A unique identifier of the item  
Feed label | `STRING` | The feed label for the item, or "-" if not provided  
Language code | `STRING` | The two-letter ISO 639-1 language code for the item  
Channel | `STRING` | The item's channel, either `online` or `local`  
Title | `STRING` | Title of the item  
Brand | `STRING` | Brand of the item  
Category l{1-5} | `INTEGER` | Google Product Category of the item  
Product type l{1-5} | `STRING` | Product type of the item  
Price | `RECORD` | Full price of the item, prior to any discounts  
Value | `INTEGER` | Price value of the item  
Currency | `STRING` | The currency of the price  
Sale Price | `RECORD` | Sale price of the item, if applicable  
Value | `INTEGER` | Sale price value of the item  
Currency | `STRING` | The currency of the sale price  
Condition | `STRING` | Condition or state of the item  
Availability | `STRING` | Availability status of the item  
Shipping label | `STRING` | The shipping label specified in the feed  
Gtin | `STRING` | [Global Trade Item Number](https://support.google.com/merchants/answer/188494#gtin) (GTIN) of the item  
Item group ID | `STRING` | Shared identifier for all variants of the same product  
Creation time | `INTEGER` | The time this item was created by the provider as timestamp microseconds  
Expiration date | `DATE` | Date on which the item should expire, as specified upon insertion  
Aggregated reporting context status | `STRING` | The status of the product aggregated for all reporting contexts. The supported values are `ELIGIBLE`, `ELIGIBLE_LIMITED`, `PENDING`, `NOT_ELIGIBLE_OR_DISAPPROVED`, `AGGREGATED_STATUS_UNSPECIFIED`  
Reporting context statuses | `RECORD`, `REPEATED` | The status of the product in each reporting context and region  
Reporting context | `STRING` | Reporting context  
Region and status | `RECORD`, `REPEATED` | Status per region  
Region | `STRING` | Region code represented in ISO 3166 format  
Status | `STRING` | Status of the product in the region, can be `ELIGIBLE`, `PENDING`, or `DISAPPROVED`  
Item issues | `RECORD`, `REPEATED` | The list of item level issues associated with the product  
Type | `RECORD` | Issue type  
Code | `STRING` | The error code of the issue, equivalent to the [`code`](https://developers.google.com/shopping-content/guides/product-issues) of Product issues  
Canonical attribute | `STRING` | Canonical attribute name for attribute-specific issues  
Severity | `RECORD` | How this issue affects serving of the offer  
Severity per reporting context | `RECORD`, `REPEATED` | Issue severity per reporting context  
Reporting context | `STRING` | Reporting context the issue applies to  
Disapproved regions | `STRING`, `REPEATED` | List of disapproved regions in the reporting context, represented in ISO 3166 format  
Demoted regions | `STRING`, `REPEATED` | List of demoted regions in the reporting context, represented in ISO 3166 format  
Aggregated severity | `STRING` | Aggregated severity of the issue for all reporting contexts it affects. Its values can be `AGGREGATED_ISSUE_SEVERITY_UNSPECIFIED`, `DISAPPROVED`, `DEMOTED`, or `PENDING`  
Resolution | `STRING` | Whether the issue can be resolved by the merchant  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
