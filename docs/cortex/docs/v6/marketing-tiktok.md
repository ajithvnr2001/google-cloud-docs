---
url: https://docs.cloud.google.com/cortex/docs/v6/marketing-tiktok/
title: Integration with TikTok \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:19:33.681317+00:00
---

# Integration with TikTok  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/v6/marketing-tiktok/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Version 6 Guides ](https://docs.cloud.google.com/cortex/docs/v6/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integration with TikTok

This page describes the required configurations to bring data from TikTok as a data source of the marketing workload of Cortex Framework Data Foundation.

TikTok is a popular social media app known for short-form videos that Cortex Framework can bring data to analyze an overall marketing performance. By combining data from TikTok and various sources, you can gain a more comprehensive understanding of your target audience and the effectiveness of your social media campaigns across different platforms.

The following diagram describes how TikTok data is available through the marketing workload of Cortex Framework Data Foundation:

![TikTok data source](https://docs.cloud.google.com/cortex/docs/images/tiktok-data-source.png)

**Figure 1**. TikTok data source.**Note:** For accessing configuration files, analytical views and models for the TikTok data source, see the [data source directory](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/marketing/src/TikTok).

## Configuration file

The [`config.json`](https://github.com/GoogleCloudPlatform/cortex-data-foundation/blob/main/config/config.json) file configures the settings required to connect to data sources for transferring data from various workloads. This file contains the following parameters for TikTok:
    
    
       "marketing": {
            "deployTikTok": true,
            },
            "TikTok": {
                "deployCDC": true,
                "datasets": {
                    "cdc": "",
                    "raw": "",
                    "reporting": "REPORTING_TikTok"
                }
            }
    

The following table describes the value for each marketing parameter:

**Parameter** | **Meaning** | **Default Value** | **Description**  
---|---|---|---  
`marketing.deployTikTok` | Deploy TikTok  | `true` | Execute the deployment for TikTok data source.   
`marketing.TikTok.deployCDC` | Deploy CDC scripts for TikTok  | `true` | Generate TikTok CDC processing scripts to run as DAGs in Managed Service for Apache Airflow.   
`marketing.TikTok.datasets.cdc` | CDC dataset for TikTok  |  | CDC dataset for TikTok.   
`marketing.TikTok.datasets.raw` | Raw dataset for TikTok  |  | Raw dataset for TikTok.   
`marketing.TikTok.datasets.reporting` | Reporting dataset for TikTok  | `"REPORTING_TikTok"` | Reporting dataset for TikTok.   
  
## Data Model

This section describes the TikTok Data Model using the Entity Relationship Diagram (ERD).

[![Entity Relationship Diagram for TikTok](https://docs.cloud.google.com/static/cortex/docs/v6/images/erd_tiktok.png)](https://docs.cloud.google.com/cortex/docs/images/erd_tiktok.png)

**Figure 2**. TikTok: Entity Relationship Diagram.

### Base views

These are the blue objects in the ERD and are views on CDC tables with no transforms other than some column name aliases. See scripts in [`src/marketing/src/TikTok/src/reporting/ddls`](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/marketing/src/TikTok/src/reporting/ddls).

### Reporting views

These are the green objects in the ERD and are reporting views that contain aggregate metrics. See scripts in [`src/marketing/src/TikTok/src/reporting/ddls`](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/marketing/src/TikTok/src/reporting/ddls).

## API connection

Cortex Framework uses TikTok Reporting APIs, version [v1.3](https://business-api.tiktok.com/portal/docs?id=1740579480076290), as the authoritative source for TikTok data. Cortex Framework uses the [synchronous](https://business-api.tiktok.com/portal/docs?id=1738864778664961) mode and calls [Basic Reporting](https://business-api.tiktok.com/portal/docs?id=1738864915188737) APIs to retrieve performance metrics for advertisements and ad groups. This ensures that Cortex Framework has access to up-to-date and accurate information from TikTok, enabling effective data analysis and reporting.

For more information about the API connection, see [TikTok Reporting APIs](https://business-api.tiktok.com/portal/docs?id=1751087777884161).

## Account authentication

To configure a TikTok account and account authentication, follow these steps:

  1. Set up a [TikTok Developer Account](https://business-api.tiktok.com/portal/docs?id=1738855176671234), if you don't have it already.
  2. Create an app for Cortex Framework integration. See [TikTok API for Business](https://business-api.tiktok.com/portal/docs?id=1738855242728450) for more information. Ensure you select the following two in the scopes for the app: 
     * `Ad Account Management/Ad Account Information`
     * `Reporting/All`
  3. Get **app ID** , **secret** and **long term access token** as described in the [TikTok guide](https://business-api.tiktok.com/portal/docs?id=1738373141733378), and store them respectively in [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/create-secret-quickstart) with the following names: 
     * **App ID** : `cortex_tiktok_app_id`
     * **Secret** : `cortex_tiktok_app_secret`
     * **Long term access token** : `cortex_tiktok_access_token`



## Data Freshness and Delay

As a general rule, data freshness for Cortex Framework data sources is limited by what upstream connection allows for, as well as the frequency of your DAG execution. Adjust your DAG execution frequency to align with upstream frequency, resource constraints, and your business needs.

With TikTok Marketing API, most data (excluding conversions) is available near real time.

## Managed Airflow connections

Create the following connections in Managed Airflow. For more details, see [Manage Airflow connections documentation](https://docs.cloud.google.com/composer/docs/how-to/managing/connections).

**Connection Name** | **Purpose**  
---|---  
`tiktok_raw_dataflow` | For TikTok API > BigQuery Raw Dataset   
`tiktok_cdc_bq` | For Raw dataset > CDC dataset transfer   
`tiktok_reporting_bq` | For CDC dataset > Reporting dataset transfer   
  
## Managed Service for Apache Airflow service account permissions

Grant Dataflow permissions to the service account used in Managed Airflow (as configured in the `tiktok_raw_dataflow` connection). See instructions in [Dataflow documentation](https://docs.cloud.google.com/dataflow/docs/concepts/security-and-permissions#df-service-account).

Also, the same service account should also have Secret Manager Accessor access.

## Ingestion settings

Control `Source to Raw` and `Raw to CDC` data pipelines through the settings in the file `[src/TikTok/config/ingestion_settings.yaml](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/marketing/src/TikTok/config/ingestion_settings.yaml)`. This section describes the parameters of each data pipeline.

### Source to raw tables

This section has entries that control how data from TikTok is fetched and where data end up in the raw dataset. Each entry corresponds with one raw table that has data fetched from TikTok API for that entity. Based on this configuration parameters, Cortex Framework creates Airflow DAGs that run Dataflow pipelines to process data from TikTok APIs.

The following parameters control the settings for `Source to Raw` for each entry:

**Parameter** | **Description**  
---|---  
`base_table` | Table in Raw dataset where the data for an entity is stored(for example, 'Ad' data).   
`load_frequency` | How often a DAG is run for this entity to process data. See [Airflow documentation](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/cron.html) for details on possible values.   
`schema_file` | Schema file in `src/table_schema` directory that maps API response fields to destination table's column names.   
`partition_details` | **Optional:** If you want this table to be partitioned for performance considerations. For more information, see [Table Partition](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-five#table_partition).   
`cluster_details` | **Optional:** If you want this table to be clustered for performance considerations. For more information, see [Cluster Settings](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-five#cluster_settings).   
  
### Raw to CDC tables

This section has entries that control how data moves from raw tables to CDC tables. Each entry corresponds with a CDC table (which in turn corresponds with an entity mentioned for the `Source to Raw table`.)

The following parameters control the settings for `Raw to CDC` for each entry:

**Parameter** | **Description**  
---|---  
`base_table` | Table in CDC dataset where the raw data after CDC transformation is stored (for example,`auction_ad_performance`)   
`load_frequency` | How frequently a DAG for this entity runs to populate the CDC table. For more information, see [Airflow documentation](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/cron.html) for details on possible values.   
`row_identifiers` | List of columns (separated by comma) that forms a unique record for this table.   
`partition_details` | **Optional:** If you want this table to be partitioned for performance considerations. For more information, see [Table Partition](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-five#table_partition).   
`cluster_details` | **Optional:** If you want this table to be clustered for performance considerations. For more information, see [Cluster Settings](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-five#cluster_settings).   
  
## Reporting settings

Configure and control how Cortex Framework generates data for the TikTok final reporting layer using the reporting settings file`[src/TikTok/config/reporting_settings.yaml](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/marketing/src/TikTok/config/reporting_settings.yaml)`. This file controls how reporting layer BigQuery objects (tables, views, functions or stored procedures) are generated.

For more information, see [Customizing reporting settings file](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-five#customizing_reporting_settings_file).

## What's next?

  * For more information about other data sources and workloads, see [Data sources and workloads](https://docs.cloud.google.com/cortex/docs/v6/data-sources-and-workloads).
  * For more information about the steps for deployment in production environments, see [Cortex Framework Data Foundation deployment prerequisites](https://docs.cloud.google.com/cortex/docs/v6/deployment-prerequisites).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
