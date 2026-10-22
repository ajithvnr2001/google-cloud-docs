---
url: https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/cud-export/
title: Structure of CUD metadata export \u00a0|\u00a0 Cloud Billing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:26:08.698339+00:00
---

# Structure of CUD metadata export  |  Cloud Billing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/cud-export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  Structure of CUD metadata export Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document provides reference information for the schema of Cloud Billing committed use discount (CUD) metadata that's exported daily to each table in BigQuery. This export provides a daily snapshot of your [_spend-based CUDs_](https://docs.cloud.google.com/docs/cuds-spend-based) commitment metadata to a BigQuery table, which you can join with other billing data exports for better CUD management and reporting.

## Ingress and egress rules

If you use [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) for BigQuery resources on your project or organization, you must create ingress and egress rules to properly enable data exports to BigQuery.

  1. Create an [ingress rule](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) that gives the individual access to create the export: 
         
         - ingressFrom:
               identities:
               - PRINCIPAL_IDENTIFIER_OF_USER_INITIATING_EXPORT
               sources:
               - accessLevel: "*"
           ingressTo:
               operations:
               - serviceName: bigquery.googleapis.com
                 methodSelectors:
                 - method: "*"
               resources:
               - projects/YOUR_PROJECT_ID_TO_HOST_EXPORT_DATA
           title: 'Ingress Rule Name'
           

See [Principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers) for more information about principal identifier formats.

  2. Create an [egress rule](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#definition-ingress-egress) to allow Google Cloud access to the BigQuery dataset through VPC Service Controls: 
         
         - egressTo:
                operations:
               - serviceName: bigquery.googleapis.com
                 methodSelectors:
                 - method: "*"
               resources:
               - projects/132468967293
           egressFrom:
               identityType: ANY_IDENTITY
               sources:
               - accessLevel: "*"
               sourceRestriction: RESTRICTION_STATUS
           title: 'Egress Rule Name'
           

**Note:** If you skip this step, you will receive the following error when you attempt to initiate the export: _You don't have permissions to enable the dataset_. 


## Schema of the CUD export data

In your BigQuery dataset, your Cloud Billing account CUD data is loaded into a data table named `cud_subscriptions_export`.

The following information describes the schema of the data that's exported to BigQuery.

Field | Type | Description | `billing_account_id` | String | The 18-character, alphanumeric billing account ID associated with the CUD data, for example, `010101-F0FFF0-10XX01`.  
---|---|---  
`cud_product.id` | String | The product definition ID, for example, `344fffc1-17f9-4e34-abf2-cfffff409fa2`.  
`cud_product.display_name` | String | The display name of the product associated with the commitment, for example, `Gemini Enterprise Flexible Savings Plans`.  
`cud_product.type` | String | The type of commitment, for example, `Spend-Based`.  
`consumption_model.id` | String | The ID of the [consumption model](https://docs.cloud.google.com/billing/docs/resources/multiprice-cuds) used by the commitment, for example, `5515-81A8-03A2`.  
`consumption_model.description` | String | The description of the [consumption model](https://docs.cloud.google.com/billing/docs/resources/multiprice-cuds) for the commitment, for example, `Gemini Enterprise Flexible Savings Plan - 1 Year`.  
`subscription.entitlement_scope` | String | The scope of the entitlement for the commitment, for example, `billingAccounts/010101-F0FFF0-10XX01`.  
`subscription.instance_id` | String | The subscription instance ID, which is a GUID, for example, `769c55ea-c50f-4258-bcf5-04b6688fa5fa`.  
`subscription.display_name` | String | The display name for the commitment, defined by you at the time of purchase.  
`subscription.entitlement_period` | String | The recurrence period of the commitment, either `Monthly` or `Hourly`.  
`subscription.payment_terms` | String | The payment terms for the commitment, for example, `Postpay`.  
`region` | String | The region associated with the commitment, for example, `us-central1`. If the commitment is global, this field is empty.  
`commitment_amount` | Repeated Record | The commitment amount details.  
`commitment_amount.unit` | String | The measurement unit of resource consumption for the commitment, for example, `$/mo` or `$/hr`.  
`commitment_amount.value` | Numeric | The commitment amount value.  
`commitment_fee` | Record | The commitment fee details.  
`commitment_fee.sku` | String | The SKU ID associated with the commitment fee.  
`commitment_fee.description` | String | The description of the fee SKU.  
`term` | String | The term length of the commitment in ISO 8601 duration format, where `P1Y` represents one year, and `P3Y` represents three years.  
`start_time` | Timestamp | The start timestamp for the commitment, for example, `2026-07-20 21:35:48 UTC`.  
`end_time` | Timestamp | The end timestamp for the commitment, for example, `2027-07-20 21:35:48 UTC`.  
`entitlement_schedule` | Repeated Record | The schedule details for the entitlement.  
`entitlement_schedule.start_time` | Datetime | The start of the schedule window in the America/Los_Angeles time zone.  
`entitlement_schedule.end_time` | Datetime | The end of the schedule window in the America/Los_Angeles time zone.  
`entitlement_schedule.commitment_amount` | Numeric | The commitment amount for this specific schedule window.  
`state` | String | The current status of the commitment, which can be `Pending`, `Active`, or `Expired`.  
  
## Related topics

For more information, see the following topics.

### Topics related to exported Cloud Billing data

  * [Set up Cloud Billing data export to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-setup)
  * [Example queries for Cloud Billing data export to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/bq-examples)



### Cost and pricing reports available in the Google Cloud console

  * [View your Cloud Billing reports and cost trends](https://docs.cloud.google.com/billing/docs/how-to/reports)
  * [View and download the cost details of your invoice or statement](https://docs.cloud.google.com/billing/docs/how-to/cost-table)
  * [View and download prices for Google's cloud services](https://docs.cloud.google.com/billing/docs/how-to/pricing-table)
  * [Understand your savings with cost breakdown reports](https://docs.cloud.google.com/billing/docs/how-to/cost-breakdown)
  * [Analyze the effectiveness of your committed use discounts](https://docs.cloud.google.com/billing/docs/how-to/cud-analysis)
  * [View your cost and payment history](https://docs.cloud.google.com/billing/docs/how-to/view-history)



[ Previous arrow_back  Structure of Pricing data export  ](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/pricing-data)

[ Next Example queries for Cloud Billing  arrow_forward  ](https://docs.cloud.google.com/billing/docs/how-to/bq-examples)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
