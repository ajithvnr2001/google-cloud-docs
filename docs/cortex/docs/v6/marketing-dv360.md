---
url: https://docs.cloud.google.com/cortex/docs/v6/marketing-dv360/
title: Integration with YouTube (DV360) \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:12:23.183990+00:00
---

# Integration with YouTube (DV360)  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/v6/marketing-dv360/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Version 6 Guides ](https://docs.cloud.google.com/cortex/docs/v6/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integration with YouTube (DV360)

This page describes the required configurations to bring data from YouTube with Display & Video 360 (DV360) as a data source of the marketing workload of Cortex Framework Data Foundation.

DV360 is an advertising platform by Google for managing YouTube advertising alongside other digital channels, offering advertisers greater control and efficiency in their marketing efforts.

The following diagram describes how DV360 data is available through the marketing workload of Cortex Framework Data Foundation:

![DV360 data source](https://docs.cloud.google.com/cortex/docs/images/dv360-data-source.png)

**Figure 1**. DV360 data source.**Note:** For accessing configuration files, analytical views and models for the DV360 data source, see the [data source directory](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/marketing/src/DV360).

## Configuration file

The [`config.json`](https://github.com/GoogleCloudPlatform/cortex-data-foundation/blob/main/config/config.json) file configures the settings required to connect to data sources for transferring data from various workloads. This file contains the following parameters for DV360:
    
    
       "marketing": {
            "deployDV360": true,
            "DV360": {
                "deployCDC": true,
                "datasets": {
                    "cdc": "",
                    "raw": "",
                    "reporting": "REPORTING_DV360"
                }
            }
       }
    

The following table describes the value for each marketing parameter:

**Parameter** | **Meaning** | **Default Value** | **Description**  
---|---|---|---  
`marketing.deployDV360` | Deploy DV360  | `true` | Execute the deployment for DV360 data source.   
`marketing.DV360.deployCDC` | Deploy CDC scripts for DV360  | `true` | Generate DV360 CDC processing scripts to run as DAGs in Managed Service for Apache Airflow.   
`marketing.DV360.datasets.cdc` | CDC dataset for DV360  |  \-  | CDC dataset for DV360.   
`marketing.DV360.datasets.raw` | Raw dataset for DV360  |  \-  | Raw dataset for DV360.   
`marketing.DV360.datasets.reporting` | Reporting dataset for DV360  | `REPORTING_DV360` | Reporting dataset for DV360.   
  
## Data Model

This section describes the Youtube (with DV360) Data Model using the Entity Relationship Diagram (ERD).

[![Entity Relationship Diagram for DV360](https://docs.cloud.google.com/cortex/docs/images/erd_dv360.png)](https://docs.cloud.google.com/cortex/docs/images/erd_dv360.png)

**Figure 2**. Youtube (with DV360): Entity Relationship Diagram.

### Reporting views

The blue objects in the ERD represent reporting views that contain aggregate metrics. See scripts in [`src/marketing/src/DV360/src/reporting/ddls`](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/marketing/src/DV360/src/reporting/ddls).

## Set up DV360 Raw data extraction

Cortex Framework integrates with DV360 using its Instant Reporting feature. [Instant Reporting](https://support.google.com/displayvideo/answer/7674615?hl) is reliable and low-cost out-of-the-box feature of DV360 which allows larger and more complex reports to be saved, scheduled and downloaded to files and different locations. Each report periodically creates export data tables in BigQuery with the same configured table name prefix, that contains data for the selected date range, at the selected frequency.

**Note:** Google is [migrating](https://support.google.com/displayvideo/answer/15141165?sjid=11873203811633756368-NC) all Offline Reporting reports to Instant Reporting starting on July 2024. The _Export to BigQuery_ feature works the same way between both reporting types. **You are responsible for managing all Instant Reporting reports**. Cortex Framework doesn't configure or control its behavior.

### Permissions

To successfully export raw data from DV360 using Instant Reporting, persons with the following permissions are required:

  * **DV360** : 
    * [Standard access](https://support.google.com/displayvideo/answer/2723011?hl) for the selected Partners or Advertisers.
  * **Google Cloud** : 
    * `BigQuery User` role assigned to the DV360 service account.
    * `BigQuery Data Editor` role assigned to the DV360 service account.



### Set up

Follow these steps to set up raw table export from DV360.

  1. Identify the service account required by the DV360 BigQuery Exporter by looking at the Link BigQuery Exporter Account, permission details section. See **Figure 2** for more reference. ![Identify the service account required by the DV360](https://docs.cloud.google.com/cortex/docs/images/dv360_example.png)**Figure 2**. Identifying the service account in the Link BigQuery Exporter Account
  2. Get Google Cloud permissions. A person with `BigQuery Administrator` role needs to grant `BigQuery User` and `BigQuery Data Editor` roles to the DV360 service account identified in the previous step.
  3. Link BigQuery to DV360, specifying the Raw dataset you intend to use in the process. Follow the instructions in **Offline reporting** > [**Enable BigQuery**](https://support.google.com/displayvideo/answer/6375151?hl#zippy=%2Cenable-bigquery-format) section.
  4. Go into [Instant Reporting](https://support.google.com/displayvideo/answer/7674615?hl) and create one report for each row in the following table, with the columns **exactly as shown**. For more information about detailed column schema definitions files under [`src/DV360/config/table_schema`](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/marketing/src/DV360/config/table_schema), see the Raw to CDC table schema section.

     1. Add at least one _Partner_ or _Advertiser_ filter. Ensure this aligns with the permissions of your BigQuery link in step 3.
**Note:** You may need to set up multiple reports or exports if you export multiple Partners or Advertisers.
     1. Select **Advertiser time zone** as the report's time zone setting. For more information, see the following section Additional considerations.
**Note:** If your account or BigQuery link only has _Advertiser access_ , you can't include a _Partner_ filter, otherwise the **Export to BigQuery** option will be disabled until the Partner filter is removed.**Table Prefix** | **Fields to include**  
---|---  
`lineitem_details` | 
     * Date
     * Line Item ID
     * Line Item
     * Campaign ID
     * Campaign
     * Line Item Type
     * Line Item Start Date
     * Line Item End Date
| 
     * Impressions  
`lineitem_insights` | 
     * Date
     * Line Item ID
     * Device Type
     * Browser
     * Environment
     * Country
     * Partner ID
     * Partner
     * Partner Currency
     * Advertiser ID
     * Advertiser
     * Advertiser Currency
     * Campaign ID
     * Campaign
     * Insertion Order ID
     * Insertion Order
     * Line Item
     * Line Item Type
     * Line Item Start Date
     * Line Item End Date
| 
     * Impressions
     * Clicks
     * Revenue (USD)
     * Engagements
     * Revenue (Partner Currency)
     * Revenue (Adv Currency)
     * TrueView: Views  
`adgroup_insights_by_age_gender` | 
     * Date
     * YouTube Ad Group ID
     * Age (YouTube)
     * Gender
     * Line Item ID
     * Partner ID
     * Partner
     * Partner Currency
     * AdvertiserID
     * Advertiser
     * Advertiser Currency
     * Insertion Order ID
     * Insertion Order
     * Line Item
     * YouTube AdGroup
| 
     * Revenue (USD)
     * Impressions
     * Clicks
     * Engagements (YouTube)
     * Revenue (Partner Currency)
     * Revenue (Adv Currency)
     * TrueView: Views  
`adgroup_insights_by_audience` | 
     * Date
     * YouTube Ad Group ID
     * Audience segment
     * Audience segment type
     * Line Item ID
     * Partner ID
     * Partner
     * PartnerCurrency
     * Advertiser ID
     * Advertiser
     * Advertiser Currency
     * Insertion Order ID
     * Insertion Order
     * Line Item
| 
     * Impressions
     * Clicks
     * YouTube Ad Group
     * Revenue (USD)
     * Engagements (YouTube)
     * Revenue (PartnerCurrency)
     * Revenue (Adv Currency)
     * TrueView: Views  
`adgroup_insights_by_adformat` | 
     * Date
     * YouTube Ad Group ID
     * YouTube Ad Format
     * Line Item ID
     * Partner ID
     * Partner
     * Partner Currency
     * Advertiser ID
     * Advertiser
     * Advertiser Currency
     * Insertion Order ID
     * Insertion Order
     * Line Item
| 
     * Impressions
     * Clicks
     * YouTube AdGroup
     * Revenue (USD)
     * Engagements (YouTube)
     * Revenue (Partner Currency)
     * Revenue (Adv Currency)
     * TrueView: Views  
`adgroup_insights_by_placement` | 
     * Date
     * YouTube Ad Group ID
     * Placement (All YouTube Channels)
     * Placement Name (All YouTube Channels)
     * Line Item ID
     * PartnerID
     * Partner
     * Partner Currency
     * Advertiser ID
     * Advertiser
     * Advertiser Currency
     * Insertion Order ID
     * Insertion Order
     * Line Item
| 
     * Impressions
     * YouTube Ad Group
     * Revenue (USD)
     * Engagements (YouTube)
     * Revenue (PartnerCurrency)
     * Revenue (Adv Currency)
     * TrueView: Views  
`adgroup_insights_by_adtype` | 
     * Date
     * YouTube Ad Group ID
     * YouTube Ad Type
     * Line Item ID
     * Partner ID
     * Partner
     * Partner Currency
     * Advertiser ID
     * Advertiser
     * Advertiser Currency
     * Insertion Order ID
     * Insertion Order
     * Line Item
| 
     * Impressions
     * Clicks
     * YouTube AdGroup
     * Revenue (USD)
     * Engagements (YouTube)
     * Revenue (Partner Currency)
     * Revenue (Adv Currency)
     * TrueView: Views  
`ad_insights` | 
     * Date
     * YouTube Ad ID
     * Line Item ID
     * Partner ID
     * Partner
     * Partner Currency
     * Advertiser ID
     * Advertiser
     * AdvertiserCurrency
     * Insertion Order ID
     * Insertion Order
     * Line Item
     * YouTube Ad Group ID
     * YouTube AdGroup
     * YouTube Ad
| 
     * Impressions
     * Clicks
     * Revenue (USD)
     * Engagements (YouTube)
     * Revenue (Partner Currency)
     * Revenue (AdvCurrency)
     * TrueView: Views  
  5. Set up the schedule and fill in historical data. Make sure you use the same BigQuery link as configured in the step 1, as well as the table prefix **exactly as shown** in the previous table. For more information, see the following section Additional considerations.

  6.      * Manually trigger a backfill run, or wait for the scheduled export to start. Either way, your data automatically lands in the Raw dataset configured for your BigQuery link.



### Additional considerations

Regarding time zone selection:

  * For some report types, you have the option to choose Advertiser time zone or UTC time zone for dates at the time of setting up the export. However, Youtube-related reports supports Advertiser time zone only. Therefore, make sure to select **Advertiser** time zone setting when setting up the exports.

  * As the report export is pre-aggregated to daily level, Cortex Framework uses the date provided directly without timezone conversions. You are responsible for interpreting the reported time zone information.




Regarding scheduling and backfilling historical data:

  * We recommend to select **last 7 days** as the export date range and **Daily** as export frequency. Selecting an export date range and an export frequency is necessary to strike a balance between data accuracy and storage cost, although any setting will work with our CDC process.

  * Instant Reporting supports exporting up to 14 days of data when exporting to BigQuery, although DV360 may occasionally make minor updates to data, up to 31 days after the report date. **If you set up export for multiple Advertisers, each advertiser's date will be in their own time zones**.

  * If historical data is required, as non-scheduled one-offs, Instant Reporting allows for exporting of up to 2 years worth of data into BigQuery tables directly. Make sure to do this at least once, manually from the DV360 UI.




## Data Freshness and Delay

As a general rule, data freshness for Cortex Framework data sources is limited by what upstream connection allows for, as well as the frequency of your DAG execution. Adjust your DAG execution frequency to align with upstream frequency, resource constraints, and your business needs.

With DV360 Instant Reporting, data freshness depends on the export frequency setting when BigQuery export is set up, which could be daily, weekly or monthly.

## Configurations

This section describes the configurations for the data process.

### Managed Service for Apache Airflow connections

Create the following connections in Managed Airflow. See more details in [Managed Airflow documentation](https://docs.cloud.google.com/composer/docs/how-to/managing/connections).

**Connection Name** | **Purpose**  
---|---  
`dv360_cdc_bq` | For Raw dataset > CDC dataset transfer.   
`dv360_reporting_bq` | For CDC dataset > Reporting dataset transfer.   
  
### Raw to CDC table schema

The directory [`src/DV360/config/table_schema`](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/marketing/src/DV360/config/table_schema) contains one schema file per set of tables (identified by the same prefix), that is exported from DV360. Each schema file contains two columns: `ColumnName` and `ColumnDataType`.

**Note:** If your use case included additional columns in the Instant Reporting export, make sure to include them in the corresponding schema files as well.

## Ingestion settings

The file [`src/DV360/config/ingestion_settings.yaml`](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/marketing/src/DV360/config/ingestion_settings.yaml) contains further settings that control **Source to CDC** data pipelines.

### Source to CDC tables

This section has entries that control how DV360 exported tables are ingested and relevant CDC process behavior. Each entry corresponds with one Instant Reporting report, identified by export prefix.

The following parameters control the settings for `Source to CDC` for each entry:

**Parameter** | **Description**  
---|---  
`base_table` | Table in CDC dataset where the raw data after CDC transformation is stored (for example, `customer`).   
`load_frequency` | How frequently a DAG for this entity runs to populate the CDC table. For more information about possible values, see [Airflow documentation](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/cron.html).   
`raw_table_prefix` | Prefix used by the corresponding Instant Reporting report to set up this BigQuery Export.   
`row_identifiers` | Columns (separated by comma) that form a unique record for this table.   
`partition_details` | **Optional:** If you want this table to be partitioned for performance considerations. For more information, see [Table Partition](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-five#table_partition).   
`cluster_details` | **Optional:** If you want this table to be clustered for performance considerations, see more information in [Cluster Settings](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-five#cluster_settings).   
  
## Reporting settings

You can configure and control how Cortex Framework generates data for the DV360 final reporting layer using the reporting settings file `[src/DV360/config/reporting_settings.yaml](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/marketing/src/DV360/config/reporting_settings.yaml)`. This file controls how reporting layer BigQuery objects (tables, views,functions or stored procedures) are generated.

For more information, see [Customizing reporting settings file](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-five#customizing_reporting_settings_file).

## What's next?

  * For more information about other data sources and workloads, see [Data sources and workloads](https://docs.cloud.google.com/cortex/docs/v6/data-sources-and-workloads).
  * For more information about the steps for deployment in production environments, see [Cortex Framework Data Foundation deployment prerequisites](https://docs.cloud.google.com/cortex/docs/v6/deployment-prerequisites).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
