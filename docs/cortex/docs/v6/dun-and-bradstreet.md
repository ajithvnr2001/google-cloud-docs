---
url: https://docs.cloud.google.com/cortex/docs/v6/dun-and-bradstreet/
title: Integration with Dun & Bradstreet \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:12:22.819796+00:00
---

# Integration with Dun & Bradstreet  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/v6/dun-and-bradstreet/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Version 6 Guides ](https://docs.cloud.google.com/cortex/docs/v6/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integration with Dun & Bradstreet

This page explains how to integrate Dun & Bradstreet (D&B) Environmental, Social, and Governance (ESG) data with your existing SAP supplier performance data within the Cortex Framework Data Foundation. Cortex Framework integrates data from data sources with Dataflow pipelines through to BigQuery, while Managed Service for Apache Airflow schedules and monitors these Dataflow pipelines for getting insights from your SAP operational data.

There's a growing need for businesses to understand the ESG performance of their suppliers. This integration helps you gain insights into your suppliers' environmental impact, social responsibility, and governance practices.

By connecting D&B ESG data with Cortex Framework you can answer compare your raw material suppliers' ESG performance against industry peers, measure and manage greenhouse gas emissions and demonstrate a commitment to environmental compliance and good corporate governance.

**Note:** Before configuring the integration for a workload, follow the steps for [Cortex Framework Data Foundation deployment](https://docs.cloud.google.com/cortex/docs/v6/deployment-prerequisites).

## Data model

This section describes the Dun and Bradstreet (D&B) Data Model using the Entity Relationship Diagram (ERD).

[![Entity Relationship Diagram for D&B ](https://docs.cloud.google.com/cortex/docs/images/erd_sustainability.png)](https://docs.cloud.google.com/cortex/docs/images/erd_sustainability.png)

**Figure 2**. Dun and Bradstreet (D&B): Entity Relationship Diagram.

### Reporting views

Two BigQuery views are provided for this module, in the `K9 Reporting` dataset (purple objects):

  * `SustainableSourcing` provides ESG Insights for each vendor.
  * `SustainableVendorSourcing` provides vendor performance insights alongside ESG Insights.



You can adjust the [reporting settings file](https://github.com/GoogleCloudPlatform/cortex-data-foundation/blob/main/src/k9/src/sustainability/reporting/sustainability_reporting.yaml) as described in the [Customizing reporting settings section](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-five#performance_optimization_for_reporting_views).

## Prerequisites

The following is required for this module to function:

  * See Cortex Framework Data Foundation [prerequisites](https://docs.cloud.google.com/cortex/docs/v6/deployment-prerequisites) and its [deployment steps](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-one).
  * Data should be loaded into a specific BigQuery table named `dun_bradstreet_esg` within the `K9 Processing` dataset. For more information, see [K9 deployment](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-three#configure_k9_deployment).



## Acquiring data

This procedure outlines two ways to acquire D&B ESG data for use with Cortex Framework Data Foundation.

### BigQuery sharing (formerly Analytics Hub)

  1. Navigate to the [Analytics Hub](https://cloud.google.com/analytics-hub).
  2. Search for `ESG ranking`.
  3. Choose an option between the four datasets: 
     * `US Full File`
     * `UK Full File`
     * `Global Full File`
     * `Global Financial Services`
  4. Select `Request Access` to get in touch with D&B for further instructions.



### Google Cloud Marketplace

  1. Navigate to the Google Cloud Marketplace, which offers various cloud applications and services.
  2. Search for D&B ESG Intelligence. Look for the offering named `Dun & Bradstreet ESG Intelligence`.
  3. Explore and Subscribe. The marketplace listing should provide details about the D&B ESG Intelligence offering. You can explore the offering details and potentially subscribe to the service if it meets your requirements.

**Note:** Both methods don't provide the actual data directly. Whichever method you choose, you need to interact with D&B to obtain access credentials or establish a subscription plan to access the ESG data.

## Loading data

This section references the documentation to load [D&B ESG data](https://www.dnb.co.uk/content/dam/english/dnb-solutions/ESG%20Methodology%20Whitepaper.pdf) into your Cortex Framework Data Foundation environment. It should be loaded through a CSV file provided by D&B. For more information, see to the [data dictionary](https://github.com/GoogleCloudPlatform/cortex-data-foundation/blob/main/src/k9/src/sustainability/data/dnb_esg_data_dict.csv) and [sample data](https://github.com/GoogleCloudPlatform/cortex-data-foundation/blob/main/src/k9/src/sustainability/data/dnb_esg_sample_record.csv).

## Data Studio Dashboard

See how Data Studio can be used to showcase insights in [Data Studio Dashboard for Dun & Bradstreet](https://docs.cloud.google.com/cortex/docs/v6/looker-dashboard-dun-and-bradstreet).

## What's next?

  * For more information about other data sources and workloads, see [Data sources and workloads](https://docs.cloud.google.com/cortex/docs/v6/data-sources-and-workloads).
  * For more information about the steps for deployment in production environments, see [Cortex Framework Data Foundation deployment prerequisites](https://docs.cloud.google.com/cortex/docs/v6/deployment-prerequisites).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
