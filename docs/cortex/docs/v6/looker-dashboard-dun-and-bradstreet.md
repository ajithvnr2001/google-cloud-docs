---
url: https://docs.cloud.google.com/cortex/docs/v6/looker-dashboard-dun-and-bradstreet/
title: Data Studio dashboard for Dun & Bradstreet \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:22.006829+00:00
---

# Data Studio dashboard for Dun & Bradstreet  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/v6/looker-dashboard-dun-and-bradstreet/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Version 6 Guides ](https://docs.cloud.google.com/cortex/docs/v6/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Data Studio dashboard for Dun & Bradstreet

This page describes the insights you can get from the Data Studio dashboard for Dun & Bradstreet data. By integrating Dun & Bradstreet's ESG (Environment, Society, and Governance) ranking data with SAP ERP supplier data, you can gain insights into ESG risks and opportunities in their supply chain. These insights can guide strategic decisions, monitor suppliers' ESG performance, assess vendors' capabilities in managing emissions, evaluate adherence to compliance and governance standards, and identify resilient suppliers.

You can also extend the insights beyond Sustainability with other data sources in [Cortex Framework](https://docs.cloud.google.com/cortex/docs/v6/data-sources-and-workloads).

## Available insights

The Data Studio dashboard for Dun & Bradstreet data from Cortex Framework offers the following insights.

### Vendor ESG performance overview

Overview of high-level vendor delivery and ESG performance including:

  * Number of active vendors in selected invoice date range
  * Average ESG ranking score across active vendors
  * Total spend with active vendors
  * Average GHG Emissions score across active vendors
  * _OnTimeInFull_ (OTIF) delivery percentage across active vendors



Insights into ESG risks and opportunities attached to total spend with vendors:

  * Total Spend by top vendors
  * Total Spend by ESG Ranking Score
  * Average ESG ranking score trend across active vendors
  * Number of active vendors by ESG ranking score



Distribution of active vendors into individual ESG ranking scores:

  * Number of vendors by environmental ranking score
  * Number of vendors by social ranking score
  * Number of vendors by governance ranking score



### Vendor environmental, social and governance insights

Detailed environmental, social and governance insights for active vendors:

  * Natural resource management scores
  * GHG emissions and climate scores
  * Environmental risk and opportunities scores
  * Human capital scores
  * Products quality management scores
  * Customer engagement scores
  * Community and supplier engagement and certifications scores
  * Corporate governance scores
  * Corporate behaviors scores
  * Business resiliency scores
  * Individual environmental, social and governance score trends



### Vendor ESG Performance Details

Top vendor comparison to their industry peers and holistic assessment using delivery and ESG performance insights:

  * Average peer ESG ranking score
  * ESG ranking score
  * Total spend to date
  * _OnTimeInFull_ delivery percentage



## Dashboard

To access the Cortex Data Studio dashboard for Dun & Bradstreet, see [Cortex Framework - Vendor ESG Performance](https://lookerstudio.google.com/c/reporting/cab436f2-ff83-4cfa-b7e4-e99b9fd9a8d0/page/p_wa5lq4dsfd). This dashboard contains predefined resources with a solid foundation for creating custom reports, visualizations, and dashboards tailored to your specific needs.

## Deployment

You can customize the Cortex Data Studio dashboard for Dun & Bradstreet by copying and connecting it to your own data with the following instructions:

  1. **Deploy Cortex Framework** : Ensure you have Cortex Framework set up and configured with your data sources. For more information, see [Cortex Framework prerequisites for deployment](https://docs.cloud.google.com/cortex/docs/v6/deployment-prerequisites).
  2. Copy the dashboard. 
     1. Go to the [Cortex Framework - Vendor ESG Performance](https://lookerstudio.google.com/c/reporting/cab436f2-ff83-4cfa-b7e4-e99b9fd9a8d0/page/p_wa5lq4dsfd) dashboard.
     2. On the top bar, select the three-dot **More options** button more_vert.
     3. Click **Make a copy** to copy the dashboard.
     4. A dialog would come up. Ignore the mapping of the new data source for now and click **Copy Report**.
     5. A copy is now created under your account.
  3. Enter the **Edit mode**.
  4. On the top bar, select **Resources** > **Manage added data sources**. You would see the two data sources that are powering this dashboard.
  5. Edit the _SustainableSourcing_ data source by clicking **Edit**. You would see that this dashboard uses a _CUSTOM QUERY_. 
     1. Choose the Billing Project in _CUSTOM QUERY_.
     2. Update the query accordingly to point to the location where your sustainability tables are deployed.
     3. Verify if you have access to the underlying source. You can copy and run the query directly in the BigQuery console which should complete successfully and return results.
     4. Click **RECONNECT**. The page should take about a minute to come back with any configuration changes.
     5. Click **Apply** and **Done** in the following page. This should bring you back to the Data Sources page.
  6. Edit the _SustainableVendorSourcing_ data source by clicking **Edit**. Repeat procedure from previous step.
  7. Close windows for **Manage added data sources**.
  8. Reload the your dashboard. You should be able to see the dashboard with your data.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
