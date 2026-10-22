---
url: https://docs.cloud.google.com/compute/docs/deprecations/usage-export/
title: Compute Engine usage report deprecation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:35.390241+00:00
---

# Compute Engine usage report deprecation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/deprecations/usage-export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Resources ](https://docs.cloud.google.com/compute/docs/resources)



Send feedback 

#  Compute Engine usage report deprecation Stay organized with collections  Save and categorize content based on your preferences. 

The _usage export_ in Compute Engine was deprecated on January 20, 2026 and will be discontinued on March 30, 2026. To export Compute Engine usage, use [BigQuery Exports](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery).

## Generate usage reports with BigQuery

This section summarizes how to export Compute Engine usage reports to BigQuery. For more information, see [Export Cloud Billing data to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery).

To retrieve usage data with BigQuery, follow these steps:

  1. [Set up Cloud Billing data export to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-setup). This creates a dataset that you can query for usage information.
  2. Retrieve usage data with SQL queries. The following section describes how to run a query and provides some sample queries.



### Retrieve usage reports with SQL queries

Use the following SQL queries to retrieve usage reports. The query can be run in BigQuery following the instructions in [Run interactive queries](https://docs.cloud.google.com/bigquery/docs/running-queries).

Replace the following variables:

  * `PROJECT_ID`: The ID of the project that contains your BigQuery dataset.
  * `DATASET_NAME`: The name of the BigQuery dataset that contains your billing data.
  * `BILLING_ACCOUNT_ID`: Your Cloud Billing account ID, with hyphens (-) replaced by underscores (_). For example, `012345_567890_ABCDEF`.
  * `PROJECT_NUMBER`: Your project number.
  * `DAY`: The day of month to report on, in format `DD`.
  * `MONTH`: The month to report on, in format `MM`.
  * `YEAR`: The year to report on, in format `YYYY`.



Use the following query to produce daily usage data:
    
    
    SELECT
     DATE(usage_end_time) as report_date,
     sku.id as measurement_id,
     sum(usage.amount) as quantity,
     usage.unit as unit,
     REPLACE(REPLACE(REPLACE(resource.global_name, SPLIT(resource.global_name, "/")[ORDINAL(ARRAY_LENGTH(SPLIT(resource.global_name, "/")))], SPLIT(resource.name, "/")[ORDINAL(ARRAY_LENGTH(SPLIT(resource.name, "/")))]), "//compute.googleapis.com/", "https://www.googleapis.com/compute/v1/"), "/projects/PROJECT_NUMBER/","/projects/PROJECT_ID/") as resource_uri,
     SPLIT(resource.global_name, "/")[ORDINAL(ARRAY_LENGTH(SPLIT(resource.global_name, "/")))] as resource_id,
     location.region as location,
    FROM `PROJECT_ID.DATASET_NAME.gcp_billing_export_resource_v1_BILLING_ACCOUNT_ID`
    WHERE TRUE
     AND EXTRACT(DAY FROM usage_end_time) = DAY
     AND EXTRACT(MONTH FROM usage_end_time) = MONTH
     AND EXTRACT(YEAR FROM usage_end_time) = YEAR
     AND service.id = "6F81-5844-456A"
    GROUP BY 1,2,4,5,6,7
    

Use the following query to produce monthly usage data:
    
    
    SELECT
     DATE(usage_end_time) as report_date,
     sku.id as measurement_id,
     sum(usage.amount) as quantity,
     usage.unit as unit,
     REPLACE(REPLACE(REPLACE(resource.global_name, SPLIT(resource.global_name, "/")[ORDINAL(ARRAY_LENGTH(SPLIT(resource.global_name, "/")))], SPLIT(resource.name, "/")[ORDINAL(ARRAY_LENGTH(SPLIT(resource.name, "/")))]), "//compute.googleapis.com/", "https://www.googleapis.com/compute/v1/"), "/projects/PROJECT_NUMBER/","/projects/PROJECT_ID/") as resource_uri,
     SPLIT(resource.global_name, "/")[ORDINAL(ARRAY_LENGTH(SPLIT(resource.global_name, "/")))] as resource_id,
     location.region as location,
    FROM `PROJECT_ID.DATASET_NAME.gcp_billing_export_resource_v1_BILLING_ACCOUNT_ID`
    WHERE TRUE
     AND EXTRACT(MONTH FROM usage_end_time) = MONTH
     AND EXTRACT(YEAR FROM usage_end_time) = YEAR
     AND service.id = "6F81-5844-456A"
    GROUP BY 1,2,4,5,6,7
    

## Shutdown schedule

The following table lists the shutdown schedule for Compute Engine export.

Date | Event  
---|---  
**January 20, 2026** | Compute Engine usage export is deprecated.  
**March 30, 2026** | Compute Engine usage reports will no longer be exported.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
