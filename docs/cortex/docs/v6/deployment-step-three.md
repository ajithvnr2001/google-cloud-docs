---
url: https://docs.cloud.google.com/cortex/docs/v6/deployment-step-three/
title: Step 3: Determine integration mechanism \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:34.052359+00:00
---

# Step 3: Determine integration mechanism  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/v6/deployment-step-three/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Version 6 Guides ](https://docs.cloud.google.com/cortex/docs/v6/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Step 3: Determine integration mechanism

This page describes the third step to deploy Cortex Framework Data Foundation, the core of Cortex Framework. In this step, you configure the integration with your chosen data source. **If you are using sample data, skip this step**.

**Note:** The steps outlined in this page are specifically designed for deploying Cortex Framework Data Foundation from the [official GitHub repository](https://github.com/GoogleCloudPlatform/cortex-data-foundation).

## Integration overview

Cortex Framework helps you centralize data from various sources, along with other platforms. This creates a single source of truth for your data. Cortex Data Foundation integrates with each data source in different ways, but most of them follow a similar procedure:

  * **Source to Raw layer:** Ingest data from data source to raw dataset using APIs. This is achieved by using Dataflow pipelines triggered through Managed Airflow DAGs.
  * **Raw layer to CDC layer** : Apply CDC processing on raw dataset and store the output in CDC dataset. This is accomplished by Managed Airflow DAGs running BigQuery SQLs.
  * **CDC layer to Reporting layer:** Creates final reporting tables from CDC tables in the Reporting dataset. This is accomplished by either creating runtime views on top of CDC tables or running Managed Airflow DAGs for materialized data in BigQuery tables - depending on how it's configured. For more information about configuration, see [Customizing reporting settings file](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-five#customizing_reporting_settings_file).



The [`config.json`](https://github.com/GoogleCloudPlatform/cortex-data-foundation/blob/main/config/config.json) file configures the settings required to connect to data sources for transferring data from various workloads. See the integration options for each data source in the following resources.

  * Operational: 
    * [SAP (SAP ECC or SAP S/4 HANA)](https://docs.cloud.google.com/cortex/docs/v6/operational-sap)
    * [Salesforce Sales Cloud](https://docs.cloud.google.com/cortex/docs/v6/operational-salesforce)
    * [Oracle EBS](https://docs.cloud.google.com/cortex/docs/v6/operational-oracle-ebs)
  * Marketing: 
    * [Google Ads ](https://docs.cloud.google.com/cortex/docs/v6/marketing-googleads)
    * [Campaign Manager 360 (CM360) ](https://docs.cloud.google.com/cortex/docs/v6/marketing-cm360)
    * [TikTok ](https://docs.cloud.google.com/cortex/docs/v6/marketing-tiktok)
    * [LiveRamp ](https://docs.cloud.google.com/cortex/docs/v6/marketing-liveramp)
    * [Meta (Facebook / Instagram)](https://docs.cloud.google.com/cortex/docs/v6/marketing-meta)
    * [Salesforce Marketing Cloud (SFMC) ](https://docs.cloud.google.com/cortex/docs/v6/marketing-salesforce)
    * [YouTube (with DV360)](https://docs.cloud.google.com/cortex/docs/v6/marketing-dv360)
    * [Google Analytics 4](https://docs.cloud.google.com/cortex/docs/v6/marketing-google-analytics)
    * [Cross Media & Product Connected Insights](https://docs.cloud.google.com/cortex/docs/v6/marketing-cross-media)
    * [Cortex for Meridian](https://docs.cloud.google.com/cortex/docs/v6/meridian)
  * Sustainability: 
    * [Dun & Bradstreet](https://docs.cloud.google.com/cortex/docs/v6/dun-and-bradstreet)



For more information about the **Entity-Relationship Diagrams** that each data source supports, see the [`docs`](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/docs) folder in the Cortex Framework Data Foundation repository.

## K9 deployment

The [K9 deployer](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/k9) simplifies the integration of diverse data sources. The K9 deployer is a predefined dataset within the BigQuery environment responsible for ingesting, processing, and modeling of components that are reusable across different data sources.

For example, the `time` dimension is reusable across all data sources where tables might need to take analytical results based on a Gregorian calendar. The K9 deployer combines external data like weather or Google Trends with other data sources (for example, SAP, Salesforce, Marketing). This enriched dataset enables deeper insights and more comprehensive analysis.

The following diagram shows the flow of data from different raw sources to various reporting layers:

![K9 datasets](https://docs.cloud.google.com/cortex/docs/images/k9_datasets.png)

**Figure 1**. K9 datasets.

In the diagram, the [source project](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-one#projects) contains the raw data from the chosen data sources (SAP, Salesforce, and Marketing). While the [target project](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-one#projects) contains processed data, derived from the Change Data Capture (CDC) process.

The pre-processing K9 step runs before all workloads start their deployment, so the reusable models are available during their deployment. This step transforms data from various sources to create a consistent and reusable dataset.

The post-processing K9 steps occurs after all workloads have deployed their reporting models to enable cross-workload reporting or augmenting models to find their necessary dependencies within each individual reporting dataset.

### Configure the K9 deployment

Configure the Directed Acyclic Graphs (DAGs) and models to be generated in the [K9 manifest file](https://github.com/GoogleCloudPlatform/cortex-data-foundation/blob/main/src/k9/src/manifest.yaml).

The K9 pre-processing step is important because it ensures that all workloads within the data pipeline have access to consistently prepared data. This reduces redundancy and ensures data consistency.

**Note:** If you are using a deployment framework like Dataform or [dbt](https://www.getdbt.com/), we recommended considering porting the K9 pre-processing DAG execution into your scheduler of choice, and ensure your reporting views use the pre-processed data generated by K9 (instead of the raw data sources). **The Cortex team can't provide support for external frameworks**.

For more information about how to configure external datasets for K9, see [Configure external datasets for K9](https://docs.cloud.google.com/cortex/docs/v6/optional-step-external-datasets).

## Next steps

After you complete this step, move on to the following deployment steps:

  1. [Establish workloads](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-one).
  2. [Clone repository](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-two).
  3. [Determine integration mechanism](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-three) (this page).
  4. [Set up components](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-four).
  5. [Configure deployment](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-five).
  6. [Execute deployment](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-six).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
