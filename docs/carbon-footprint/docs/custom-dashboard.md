---
url: https://docs.cloud.google.com/carbon-footprint/docs/custom-dashboard/
title: Create a custom dashboard or analysis for your Carbon Footprint data \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:24:57.255200+00:00
---

# Create a custom dashboard or analysis for your Carbon Footprint data  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/carbon-footprint/docs/custom-dashboard/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Carbon Footprint ](https://docs.cloud.google.com/carbon-footprint/docs/view-carbon-data)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a custom dashboard or analysis for your Carbon Footprint data

Beyond Carbon Footprint's default view and data export, you can create custom dashboards and analyses using the exported data. This flexibility allows for tailored data visualization and granularity, enabling deeper insights to optimize your carbon footprint management according to your specific requirements.

## Using Google Sheets

Follow these steps to create a custom dashboard for your Carbon Footprint data using [Google Sheets](https://www.google.com/sheets/about/).

  1. [Export your entire carbon footprint to a sheet](https://docs.cloud.google.com/carbon-footprint/docs/export#sheets)
  2. Use a [pivot table](https://support.google.com/docs/answer/1272900) to create custom reporting on your exported data.
  3. Create a [chart](https://support.google.com/docs/answer/63824) to visualize the results of the pivot table.



## Use Data Studio

Follow these steps to create a custom [Data Studio](https://lookerstudio.google.com/) report for your Carbon Footprint data.

  1. [Export your carbon footprint to BigQuery](https://docs.cloud.google.com/carbon-footprint/docs/export)
  2. [Create a new Data Studio report](https://support.google.com/looker-studio/answer/6292570)
  3. [Connect to BigQuery](https://support.google.com/looker-studio/answer/6370296) by selecting the dataset you previously chose when configuring the Carbon Footprint export.
  4. [Add charts to your report](https://support.google.com/looker-studio/answer/6293184) using the data source created in the previous step.



## Use Looker

Follow these steps to create a custom [Looker](https://looker.com/) dashboard for your Carbon Footprint data. This option is recommended if you are an existing Looker customer.

  1. [Export your carbon footprint to BigQuery](https://docs.cloud.google.com/carbon-footprint/docs/export)
  2. Install the [Carbon Footprint block](https://marketplace.looker.com/marketplace/detail/carbon)



## Estimate emissions data at different granularity by joining Carbon Footprint data with Cloud Billing data

You can combine your Carbon Footprint export data with your Cloud Billing export data to view your carbon You can combine your Carbon Footprint export data with your Cloud Billing export data to view your carbon emissions at different levels of granularity. This allows for analysis at customized label, tag, or resource levels, supporting the identification of areas for reducing your environmental impact. You can follow these steps to approximate either instance-level emissions data and tag or label level emissions data.

### Approximate instance-level emissions data

  1. **Export Data to BigQuery** : Export [Carbon Footprint data](https://docs.cloud.google.com/carbon-footprint/docs/export) and [Cloud Billing **detailed** usage cost data](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage) to BigQuery respectively.

  2. **Join Datasets** : First, aggregate the hourly Cloud Billing detailed usage cost data to the monthly level, grouped by billing account ID, project, product, resource, and region before joining. Then join exported Carbon Footprint data with [Cloud Billing **detailed** usage cost data](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage) using the common dimensions of billing account ID, project, product, region, and month.

  3. **Estimate Resource-Level Emissions** : Break down carbon emissions data (aggregated by billing account ID, project, product, region, and month) to the individual resource level. This estimation can be performed by proportionally distributing the emissions based on each resource's contribution to the cost at list within any given billing account ID, project, product, region, and month. Using cost_at_list avoids side effect of potential pricing discounts. Implement validation steps to identify and mitigate any potential double counting of emissions.




**Important Note** : Resource-level emissions estimated using this cost-based distribution are approximations, as both cost and emissions scale with usage. While not a precise measure of individual resource impact, this method helps prioritize high-usage resources for optimization.

### Approximate tag or label level emissions data

  1. **Export Data to BigQuery** : Export [Carbon Footprint data](https://docs.cloud.google.com/carbon-footprint/docs/export) and [Cloud Billing **standard** usage cost data](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage) to BigQuery respectively.

  2. **Join Datasets** : First, aggregate the hourly Cloud Billing standard usage cost data to the monthly level, grouped by billing account ID, project, product, **tag** or **labels** , and region before joining. Then join exported Carbon Footprint data with [Cloud Billing **standard** usage cost data](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage) using the common dimensions of billing account ID, project, product, region, and month.

  3. **Estimate Tag-Level or Label-level Emissions** : With the joined dataset, aggregate emissions data by **tag** or **labels** and other dimensions as needed.




**Important Note** : Tag-Level or label-level emissions aggregated using this approach are approximations and may not accurately reflect the actual energy consumption and emissions.

## What's next?

  * [Read about the data schema used in the export](https://docs.cloud.google.com/carbon-footprint/docs/data-schema).
  * [Understand the methodology behind Carbon Footprint](https://docs.cloud.google.com/carbon-footprint/docs/methodology)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
