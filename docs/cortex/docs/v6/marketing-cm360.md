---
url: https://docs.cloud.google.com/cortex/docs/v6/marketing-cm360/
title: Integration with Campaign Manager 360 \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:04.955916+00:00
---

# Integration with Campaign Manager 360  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/v6/marketing-cm360/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Version 6 Guides ](https://docs.cloud.google.com/cortex/docs/v6/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integration with Campaign Manager 360

This page describes the required configurations to bring data from Campaign Manager 360 as a data source of the marketing workload of Cortex Framework Data Foundation.

Campaign Manager 360 (CM360) is a web-based advertising management platform offered by Google specifically designed for advertisers and agencies. It functions as a central hub to manage and optimize all your digital advertising campaigns across various channels. Cortex Framework provides the tools and platform to analyze CM360 data, combine it with data from other marketing channels, and use AI to gain deeper insights and optimize your overall marketing strategy.

The following diagram describes how CM360 data is available through the marketing workload of Cortex Framework Data Foundation:

![CM360 data source](https://docs.cloud.google.com/static/cortex/docs/v6/images/cm360-data-source.png)

**Figure 1**. CM360 data source.**Note:** For accessing configuration files, analytical views and models for the CM360 data source, see the [data source directory](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/marketing/src/CM360).

## Configuration file

The [`config.json`](https://github.com/GoogleCloudPlatform/cortex-data-foundation/blob/main/config/config.json) file configures the settings required to connect to data sources for transferring data from various workloads. This file contains the following parameters for CM360:
    
    
       "marketing": {
            "deployCM360": true,
            }
    
            "CM360": {
                "deployCDC": true,
                "dataTransferBucket": "",
                "datasets": {
                    "cdc": "",
                    "raw": "",
                    "reporting": "REPORTING_CM360"
                }
            }
    

The following table describes the value for each marketing parameter:

**Parameter** | **Meaning** | **Default Value** | **Description**  
---|---|---|---  
`marketing.deployCM360` | Deploy CM360  | `true` | Execute the deployment for CM360 data source.   
`marketing.CM360.deployCDC` | Deploy CDC scripts for CM360  | `true` | Generate CM360 CDC processing scripts to run as DAGs in Managed Service for Apache Airflow.   
`marketing.CM360.dataTransferBucket` | Bucket with Data Transfer Service results  | \-  | Bucket where DTv2 files are stored.   
`marketing.CM360.datasets.cdc` | CDC dataset for CM360  |  | CDC dataset for CM360.   
`marketing.CM360.datasets.raw` | Raw dataset for CM360  |  | Raw dataset for CM360.   
`marketing.CM360.datasets.reporting` | Reporting dataset for CM360  | `"REPORTING_CM360"` | Reporting dataset for CM360.   
  
## Data Model

This section describes the CM360 Data Model using the Entity Relationship Diagram (ERD).

[![Entity Relationship Diagram for CM360](https://docs.cloud.google.com/static/cortex/docs/v6/images/erd_cm360.png)](https://docs.cloud.google.com/static/cortex/docs/images/erd_cm360.png)

**Figure 2**. CM360: Entity Relationship Diagram.

### Base views

These are the blue objects in the ERD and are views on CDC tables with no transforms other than some column name aliases. See scripts in [`src/marketing/src/CM360/src/reporting/ddls`](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/marketing/src/CM360/src/reporting/ddls).

### Reporting views

These are the green objects in the ERD and are reporting views that contain aggregate metrics. See scripts in [`src/marketing/src/CM360/src/reporting/ddls`](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/marketing/src/CM360/src/reporting/ddls).

## DTv2 Files storage

DTv2 (Data Transfer Version 2) files are a specific format used by CM360 to deliver campaign performance data. Set up the data transfer process by following the [Data Transfer V2.0](https://developers.google.com/doubleclick-advertisers/dtv2/overview) documentation in order to use CM360 with Cortex Framework.

Create or add a Cloud Storage bucket for storing your DTv2 files from CM360. Ensure the files under the bucket are readable by the service account running DAGs in Managed Airflow. For more information, see [Create storage buckets](https://docs.cloud.google.com/storage/docs/creating-buckets).

## Data Freshness and Delay

As a general rule, data freshness for Cortex Framework data sources is limited by what upstream connection allows for, as well as the frequency of your DAG execution. Adjust your DAG execution frequency to align with upstream frequency, resource constraints, and your business needs.

With CM360 Data Transfer v2, Impressions and Clicks data are delivered 24 times a day (hourly). Process time can vary by file, so files may appear out of order. Activity files are delivered daily.

## Managed Airflow connections

Create the following connections in Managed Airflow. For more details, see the [Manage Airflow connections documentation](https://docs.cloud.google.com/composer/docs/how-to/managing/connections).

**Connection Name** | **Purpose**  
---|---  
`cm360_raw_dataflow` | For CM360 DTv2 files > BigQuery Raw Dataset   
`cm360_cdc_bq` | For Raw dataset > CDC dataset transfer   
`cm360_reporting_bq` | For CDC dataset > Reporting dataset transfer   
  
## Managed Service for Apache Airflow service account permissions

Grant Dataflow permissions to the service account used in Managed Airflow (as configured in the `cm360_raw_dataflow` connection). See instructions in [Dataflow documentation](https://docs.cloud.google.com/dataflow/docs/concepts/security-and-permissions#df-service-account).

## Ingestion settings

Control `Source to Raw` and `Raw to CDC` data pipelines through the settings in the file `[src/CM360/config/ingestion_settings.yaml](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/marketing/src/CM360/config/ingestion_settings.yaml)`. This section describes the parameters of each data pipeline.

### Source to raw tables

This section describes how entries that control which files from DTv2 are processed. Each entry corresponds with files associated with one entity. Based on this configuration, Cortex Framework creates Airflow DAGs that run Dataflow pipelines to process data from the DTv2 files.

The following parameters control the settings for `Source to Raw` for each entry:

**Parameter** | **Description**  
---|---  
`base_table` | Table in Raw dataset where the data for an entity is stored (for example, 'Clicks' data).   
`load_frequency` | How frequently a DAG for this entity runs to populate the CDC table. For more information about possible values, see [Airflow documentation](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/cron.html).   
`file_pattern` | Based filename patterns that correspond to an entity.   
`schema_file` | Schema file in `src/table_schema` directory that maps DTv2 fields to destination table's column names and data types.   
`partition_details` | **Optional:** If you want this table to be partitioned for performance considerations. For more information, see [Table Partition](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-five#table_partition).   
`cluster_details` | **Optional:** If you want this table to be clustered for performance considerations. For more information, see [Cluster Settings](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-five#cluster_settings).   
  
### Raw to CDC tables

This section has entries that control how data is moved from raw tables to CDC tables. Each entry corresponds with a raw table (which in turn corresponds with the DTv2 entity as mentioned above.)

The following parameters control the settings for `Raw to CDC` for each entry:

**Parameter** | **Description**  
---|---  
`base_table` | Table in CDC dataset where the raw data after CDC transformation is stored (for example, `customer`).   
`load_frequency` | How frequently a DAG for this entity runs to populate the CDC table. For more information about possible values, see [Airflow documentation](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/cron.html).   
`row_identifiers` | List of columns (separated by comma) that forms a unique record for this table.   
`partition_details` | **Optional:** If you want this table to be partitioned for performance considerations. For more information, see [Table Partition](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-five#table_partition).   
`cluster_details` | **Optional:** If you want this table to be clustered for performance considerations. For more information, see [Cluster Settings](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-five#cluster_settings).   
  
##### Reporting settings

You can configure and control how Cortex Framework generates data for the CM360 final reporting layer using the reporting settings file (`[src/CM360/config/reporting_settings.yaml](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/marketing/src/CM360/config/reporting_settings.yaml)`). This file controls how reporting layer BigQuery objects (tables, views, functions or stored procedures) are generated.

For more information, see [Customizing reporting settings file](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-five#customizing_reporting_settings_file).

## What's next?

  * For more information about other data sources and workloads, see [Data sources and workloads](https://docs.cloud.google.com/cortex/docs/v6/data-sources-and-workloads).
  * For more information about the steps for deployment in production environments, see [Cortex Framework Data Foundation deployment prerequisites](https://docs.cloud.google.com/cortex/docs/v6/deployment-prerequisites).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
