---
url: https://docs.cloud.google.com/cortex/docs/v6/marketing-google-analytics/
title: Integration with Google Analytics 4 \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:18.446537+00:00
---

# Integration with Google Analytics 4  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/v6/marketing-google-analytics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Version 6 Guides ](https://docs.cloud.google.com/cortex/docs/v6/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integration with Google Analytics 4

This page describes the required configurations to bring data from Google Analytics 4 (GA4) as a data source of the marketing workload of Cortex Framework Data Foundation.

**GA4** is the latest version of Google Analytics. It provides a holistic view of user behavior, focusing on event-based tracking and machine learning to offer deeper insights. Cortex Framework lets you extract data from GA4 and integrate it into BigQuery for further analysis and reporting. You can gain valuable insights and drive better business outcomes.

The following diagram describes how GA4 data is available through the marketing workload of Cortex Framework Data Foundation:

![GA4 data source](https://docs.cloud.google.com/cortex/docs/images/ga4-data-source.png)

**Figure 1**. GA4 data source.**Note:** For accessing configuration files, analytical views and models for the GA4 data source, see the [data source directory](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/marketing/src/GA4).

## Configuration file

The [`config.json`](https://github.com/GoogleCloudPlatform/cortex-data-foundation/blob/main/config/config.json) file configures the settings required to connect to data sources for transferring data from various workloads. This file contains the following parameters for GA4:
    
    
       "marketing": {
            "deployGA4": true,
            "GA4": {
                "datasets": {
                    "cdc": [
                        {"property_id": 0, "name": ""}
                    ],
                    "reporting": "REPORTING_GA4"
                }
            }
        }
    

The following table describes the value for each marketing parameter:

**Parameter** | **Meaning** | **Default Value** | **Description**  
---|---|---|---  
`marketing.deployGA4` | Deploy GA4  | `true` | Execute the deployment for GA4 data source.   
`marketing.GA4.datasets.cdc` | BigQuery Export datasets for GA4  | `[{"property_id": 0, "name": ""}]` | Array of Google Analytics 4 BigQuery Export datasets. Each element specifies `Property ID` as `INT`, as well as its corresponding BigQuery Export dataset name.   
`marketing.GA4.datasets.reporting` | Reporting dataset for GA4  | `REPORTING_GA4` | Reporting dataset for GA4.   
  
## Data Model

This section describes the GA4 Data Model using the Entity Relationship Diagram (ERD).

[![Entity Relationship Diagram for GA4](https://docs.cloud.google.com/cortex/docs/images/erd_ga4.png)](https://docs.cloud.google.com/cortex/docs/images/erd_ga4.png)

**Figure 2**. GA4: Entity Relationship Diagram.

### Base views

These are the blue objects in the ERD and are views on CDC tables with minimal transformations to unpack complex data structures. See scripts in [`src/marketing/src/GA4/src/reporting/ddls`](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/marketing/src/GA4/src/reporting/ddls).

### Reporting views

These are the green objects in the ERD and are reporting views that contain aggregate metrics. See scripts in [`src/marketing/src/GA4/src/reporting/ddls`](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/marketing/src/GA4/src/reporting/ddls).

## Configure integration for GA4

Cortex Framework Data Foundation integrates with [GA4](https://support.google.com/analytics/answer/10089681?hl) by creating a **Reporting layer** on top of GA4's [BigQuery Export](https://support.google.com/analytics/answer/9823238?hl#zippy=%2Cin-this-article) datasets (treated as [CDC datasets](https://docs.cloud.google.com/cortex/docs/v6/cdc) in Cortex Framework architecture). This is accomplished by creating runtime views on top of CDC tables or running Managed Service for Apache Airflow DAGs for materialized data in BigQuery tables, depending on the [reporting settings configuration](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-five#customizing_reporting_settings_file).

### Set up GA4 BigQuery Export

Cortex Framework uses GA4's BigQuery Export feature to load data from the source system into BigQuery. Follow the instructions for setting up BigQuery Export or each GA4 property in this GA4 Help article: [GA4 - Set up BigQuery Export](https://support.google.com/analytics/answer/9823238?hl#zippy=%2Cin-this-article).

**Note:** If you are setting up export for multiple GA4 properties, ensure they all export to the same Google Cloud project. Export both **Event** and **User** data, for all properties.

### Known issues, limitations, and other considerations

Consider the following when setting up GA4 BigQuery Export:

  * **Backfilling** : GA4 BigQuery Export starts from the day it is set up and there is no backfilling.
  * **Difference between GA4 UI and Cortex Framework reported numbers** : Multiple factors, including but not limited to sampling, data collection delay, and high-cardinality reports, may cause minor discrepancy between Google Analytics UI and Cortex Framework. This is a known and innate limitation of Google Analytics. For more information, see [Bridge the gap between the Google Analytics UI and BigQuery export ](https://developers.google.com/analytics/blog/2023/bigquery-vs-ui).
  * **Event export volume restrictions** : Depending on your Google Analytics edition, you may face varying degree of BigQuery export volume restriction per day. For more information, see [GA4 - Set up BigQuery Export](https://support.google.com/analytics/answer/9823238?hl#limits).
  * **Time zone** : In BigQuery Export, `event_date` is set **in the property's reporting time zone** while `event_timestamp` is the **UTC** timestamp in microseconds. As a result, if `event_timestamp` is used, make sure to adjust for the correct reporting time zone when comparing with UI numbers.
  * **Daily versus Streaming (real-time) Event exports** : For _Event_ exports, Cortex Framework only supports the `events_YYYYMMDD` tables created by full daily export. For more information, see [GA4 - BigQuery Export](https://support.google.com/analytics/answer/9358801?hl#streaming).
  * **GA4 360 Service Level Agreement (SLA) for BigQuery Export** : While Cortex Framework doesn't support the `events_fresh_` tables created by [Fresh Daily exports](https://support.google.com/analytics/answer/14117050?hl) as separate source tables, you can follow the `##CORTEX-CUSTOMER` customization comments in the `Events` Reporting view to replace the source tables with these, to take advantage of the SLA provided by this feature. All Reporting views will continue to work after this substitution.



## Data Freshness and Delay

As a general rule, data freshness for Cortex Framework data sources is limited by what upstream connection allows for, as well as the frequency of your DAG execution. Adjust your DAG execution frequency to align with upstream frequency, resource constraints, and your business needs.

With Google Analytics 4, BigQuery export data may be delayed up to a day depending on your time zone, unless you are using [Fresh Daily Export](https://support.google.com/analytics/answer/15604391?sjid=7512611260796146949-NC).

## Configurations

This section describes the configurations for the data process.

### Managed Service for Apache Airflow connections

Create the following connections in Managed Airflow. See more details in the [Manage Airflow connections documentation](https://docs.cloud.google.com/composer/docs/how-to/managing/connections).

**Connection Name** | **Purpose**  
---|---  
`dv360_cdc_bq` | For Raw dataset > CDC dataset transfer.   
`dv360_reporting_bq` | For CDC dataset > Reporting dataset transfer.   
  
### Reporting settings

You can configure and control how Cortex Framework generates data for the GA4 final reporting layer using the reporting settings file `[src/GA4/config/reporting_settings.yaml](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/marketing/src/GA4/config/reporting_settings.yaml)`. This file controls how reporting layer BigQuery objects (tables, views,functions or stored procedures) are generated.

For more information, see [Customizing reporting settings file](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-five#customizing_reporting_settings_file).

## What's next?

  * For more information about other data sources and workloads, see [Data sources and workloads](https://docs.cloud.google.com/cortex/docs/v6/data-sources-and-workloads).
  * For more information about the steps for deployment in production environments, see [Cortex Framework Data Foundation deployment prerequisites](https://docs.cloud.google.com/cortex/docs/v6/deployment-prerequisites).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
