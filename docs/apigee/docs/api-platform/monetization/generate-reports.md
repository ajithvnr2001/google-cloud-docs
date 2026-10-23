---
url: https://docs.cloud.google.com/apigee/docs/api-platform/monetization/generate-reports/
title: Generating monetization reports \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:16:53.271426+00:00
---

# Generating monetization reports  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/monetization/generate-reports/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Generating monetization reports Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Note: Generating Custom Reports is not supported in Apigee hybrid. [Known issue: 355714868](https://docs.cloud.google.com/apigee/docs/release/known-issues#355714868)

By using Apigee's [Custom Reports](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/create-custom-reports) feature, you can generate reports to view monetization information of your APIs. To generate the reports, you can use the Apigee UI, the stats API, or the queries API as described in the following sections:

  * [Adding a custom report using the Apigee UI](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/create-custom-reports#add)
  * [Stats API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.stats/get)
  * [Queries API (Asynchronous custom reports API)](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/asynch-reports-api)



## Monetization metrics and dimensions

Apigee provides the following monetization metrics and dimensions:

  * Metrics and dimensions for transactions using an API proxy
  * Metrics and dimensions for fee-based transactions



### Metrics and dimensions for transactions using an API proxy

The following tables list the `x_apigee_mintng_*` metrics and dimensions available for transactions using an API proxy:

  * **Metrics** Name in UI | Name in API | Description | API price multiplier | x_apigee_mintng_price_multiplier | The factor (multiplier) by which the per-transaction cost is multiplied.  
---|---|---  
Developer share of revenue | x_apigee_mintng_dev_share | App developer's or AppGroup's share in a transaction's revenue.  
Monetization price | x_apigee_mintng_price | Total revenue of a transaction.  
Monetization rates | x_apigee_mintng_rate | Rate charged for a transaction.  
  * **Dimensions** Name in UI | Name in API | Description | Rate Plan ID | x_apigee_mintng_rate_plan_id |  The monetization rate plan for the app developer.  
---|---|---  
Revenue Currency | x_apigee_mintng_currency | Currency of the transaction revenue.  
Transaction Success | x_apigee_mintng_tx_success | Monetization status of the transaction.  

**Note:**

  * For the transactions using an API proxy, you can also use [other metrics and dimensions](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-reference) along with the `x_apigee_mintng_*` metrics and dimensions. 
  * The interpretation of a dimension value depends on the metric. For example, if you select the `API Product` dimension, for a fee-based transaction, the value will be the name of the API product corresponding to the rate plan for which setup fee or recurring fee should be applied. However, if you select the `API Product` dimension for a non-fee-based transaction, the value will be the name of the API product containing the API proxies being called.



### Metrics and dimensions for fee-based transactions

The following tables list the metrics and dimensions available only for fee-based transactions:

  * **Metrics** Name in UI | Name in API | Description | Fees | fees | Fee amount.  
---|---|---  
  * **Dimensions** Name in UI | Name in API | Description | App Group Name | app_group_name | Name of the AppGroup the fees apply to, if applicable. For app developers, this field is blank.  
---|---|---  
Fee Type | fees_type | Type of fee: setup fee, recurring fee, prepaid topup, or refund. This dimension will be `null` when used with any metric other than `fees`.  
Fee Time Created | created |  Unix Timestamp when the fee was added for the app developer and API product. This dimension is `null` when used with any metric other than `fees`.  
Revenue Currency | x_apigee_mintng_currency | Currency of the fee.  
Developer Email | developer_email | App developer or AppGroup to be charged with the setup fee, recurring fees, or prepaid topup.  
Developer ID / AppGroup ID | developer |  ID of the Apigee-registered app developer or AppGroup the fees apply to. This value can be used for billing calculations.   
API Product | api_product | API product corresponding to the rate plan for which the fee applies. The value is empty for some fee types, such as prepaid topup.  
Rate Plan ID | x_apigee_mintng_rate_plan_id |  The monetization rate plan for the app developer. The value is empty for some fee types, such as prepaid topup.  
Period Start | period_start |  Start of the period for which recurring fees are charged. For example, for a monthly fee this is the first day of the month. This dimension is `null` when used with any metric other than `fees`.  
Period End | period_end |  End of the period for which recurring fees are charged. For example, for a monthly fee this is the last day of the month. This dimension is `null` when used with any metric other than `fees`.  



For detailed descriptions of these metrics and dimensions, see [Analytics metrics, dimensions, and filters reference](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-reference). 

The following sample custom report displays the **sum of Monetization rates** across all the developer apps: 

![Results of custom report showing sum of monetization rates](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/analytics-monetization-rate-plan.png)

For each developer app, the sample, shows the total cost of all the transactions from `1-Apr-2021 to 15-Apr-2021`. The cost is calculated based on the consumption-based pricing as configured in your rate plan. Notice that in this example, the metric (`x_apigee_mintng_rate`) is a monetization field but the dimension (`developer_app`) is a non-monetization field. So, based on your requirements, you can generate reports with a combination of both monetization and non-monetization fields.

You can also limit your results based on metric characteristics by using [filters](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-reference#filters).

To see recurring fees on generated reports, include in the selected date range the day after the last day of the month or the day after the subscription expiration date, as this is when they are charged.

## Exporting monetization analytics data

In Apigee you do not need to perform any additional steps to export your monetization analytics data. If you are [exporting analytics data](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/export-data), Apigee exports the following monetization fields along with regular analytics data. When fee-based transactions and transactions using an API proxy are exported together, each record exports with the common metrics and dimensions, with other (non-related) metrics and dimensions set to NULL. Note: See the exporting page linked in the previous sentence for additional information on these values.**Important:** Apigee periodically adds new fields, and recommends against writing dependent code that would break for new fields. 

  * `client_received_start_timestamp`
  * `period_end`
  * `period_start`
  * `x_apigee_mintng_currency`
  * `x_apigee_mintng_dev_share`
  * `x_apigee_mintng_price`
  * `x_apigee_mintng_price_multiplier`
  * `x_apigee_mintng_rate`
  * `x_apigee_mintng_rate_plan_id`
  * `x_apigee_mintng_tx_success`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
