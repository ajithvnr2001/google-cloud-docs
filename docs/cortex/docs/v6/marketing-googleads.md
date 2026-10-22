---
url: https://docs.cloud.google.com/cortex/docs/v6/marketing-googleads/
title: Integration with Google Ads \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:47.496157+00:00
---

# Integration with Google Ads  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/v6/marketing-googleads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Version 6 Guides ](https://docs.cloud.google.com/cortex/docs/v6/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integration with Google Ads

This page describes the required configurations to bring data from Google Ads as a data source of the marketing workload of Cortex Framework Data Foundation.

[Google Ads](https://ads.google.com/) is an online advertising platform that allows businesses to advertise their products or services across various Google properties. Cortex Framework brings your Google Ads data together with other marketing channels, analyzes it comprehensively, and uses AI to improve your campaign results.

The following diagram describes how Google Ads data is available through the marketing workload of Cortex Framework Data Foundation:

![Google Ads data source](https://docs.cloud.google.com/cortex/docs/images/google-ads-data-source.png)

**Figure 1**. Google Ads data source.**Note:** For accessing configuration files, analytical views and models for the Google Ads data source, see the [data source directory](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/marketing/src/GoogleAds).

## Configuration file

The [`config.json`](https://github.com/GoogleCloudPlatform/cortex-data-foundation/blob/main/config/config.json) file configures the settings required to transfer data from any data source, including Google Ads. This file contains the following parameters for Google Ads:
    
    
      "marketing": {
              "deployGoogleAds": true,
              "GoogleAds": {
                  "deployCDC": true,
                  "lookbackDays": 180,
                  "datasets": {
                      "cdc": "",
                      "raw": "",
                      "reporting": "REPORTING_GoogleAds"
                        }
                      }
                     }
    

The following table describes the value for each Google Ads marketing parameter:

**Parameter** | **Meaning** | **Default Value** | **Description**  
---|---|---|---  
`marketing.deployGoogleAds` | Deploy Google Ads  | `true` | Execute the deployment for Google Ads data source.   
`marketing.GoogleAds.deployCDC` | Deploy CDC for Google Ads  | `true` | Generate Google Ads CDC processing scripts to run as DAGs in Managed Airflow.   
`marketing.GoogleAds.lookbackDays` | Lookback days for Google Ads  | `180` | Number of days to start fetching data from Google Ads API.   
`marketing.GoogleAds.datasets.cdc` | CDC dataset for Google Ads  |  | CDC dataset for Google Ads.   
`marketing.GoogleAds.datasets.raw` | Raw dataset for Google Ads  |  | Raw dataset for Google Ads.   
`marketing.GoogleAds.datasets.reporting` | Reporting dataset for Google Ads  | `"REPORTING_GoogleAds"` | Reporting dataset for Google Ads.   
  
## Data Model

This section describes the Google Ads Data Model using the Entity Relationship Diagram (ERD).

[![Entity Relationship Diagram for Google Ads](https://docs.cloud.google.com/cortex/docs/images/erd_gads.png)](https://docs.cloud.google.com/cortex/docs/images/erd_gads.png)

**Figure 2**. Google Ads: Entity Relationship Diagram.

### Base views

These are the blue objects in the ERD and are views on CDC tables with no transforms other than some column name aliases. See scripts in [`src/marketing/src/GoogleAds/src/reporting/ddls`](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/marketing/src/GoogleAds/src/reporting/ddls).

### Reporting views

These are the green objects in the ERD and are reporting views that contain aggregate metrics. See scripts in [`src/marketing/src/GoogleAds/src/reporting/ddls`](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/marketing/src/GoogleAds/src/reporting/ddls).

## API connection

Cortex Framework ingestion templates use the [Google Ads API](https://developers.google.com/google-ads/api/docs/start) to retrieve reporting attributes and metrics from Google Ads. The current Cortex Framework templates use Google Ads API [version 17.1](https://developers.google.com/google-ads/api/fields/v17/overview). Consider the Google Ads API limitations:

  * **Basic access operations per day** : 15000 (paginated requests containing valid `next_page_token` are not counted).
  * **Max page size:** 10000 rows per page.
  * **Recommended default parameters:** Page size equals to 10000 rows per page.



For more information about the API connection, see [Google Ads API documentation.](https://developers.google.com/google-ads/api/docs/start).

## Account authentication

Follow these steps to set up account authentication:

  1. In the [Google Cloud console](https://console.cloud.google.com/), click **Navigation menu** > **API & Services** > **Credentials** > **Create credentials**.
  2. Create a **OAuth Client ID** credential with the following characteristics. For more information, see [Using OAuth 2.0 to Access Google APIs](https://developers.google.com/identity/protocols/oauth2/).
         
         Application type: "Web Application"
         Name: CHOSEN_NAME #(For example,"Cortex Authentication Client").
         Authorized redirect URIs: http://127.0.0.1
         

Replace `CHOSEN_NAME` with the chosen name for OAuth Client ID credential account.

  3. Save the `Client ID` and `Client secret` after the credential is configured. You need it later.

  4. Generate a fresh token using [OAuth 2.0 Access Google APIs](https://developers.google.com/identity/protocols/oauth2#5.-refresh-the-access-token,-if-necessary). Cortex Data Foundation automatically detects and ingest data from all customers (accounts) that are accessible to the credentials used to generate the token.

  5. Create a _secret_ using Secret Manager:

     * In the [Google Cloud console](https://console.cloud.google.com/), click **Secret Manager.**
     * Create a secret called `cortex-framework-google-ads-yaml` using the following format and changing the values according with your settings:
    
    {"developer_token": "DEVELOPER_TOKEN_VALUE", "refresh_token": "REFRESH_TOKEN_VALUE", "client_id": "CLIENT_ID_VALUE", "client_secret": "CLIENT_SECRET_VALUE", "use_proto_plus": False}
    




Replace the following:

  * `DEVELOPER_TOKEN_VALUE` with the developer token value available in Google Ads account.
  * `REFRESH_TOKEN_VALUE` with the refresh token value obtained in step 4.
  * `CLIENT_ID_VALUE` with the client ID value obtained in the OAuth setup in step 2.
  * `CLIENT_SECRET_VALUE` with the client secret value obtained from the OAuth setup in step 2.



## Data Freshness and Delay

As a general rule, data freshness for Cortex Framework data sources is limited by what upstream connection allows for, as well as the frequency of your DAG execution. Adjust your DAG execution frequency to align with upstream frequency, resource constraints, and your business needs.

Data retrieved using Google Ads API is generally available with 3+ hour latency. They may be adjusted afterwards due to conversions and invalid traffic detection. For more information, see the following [About data freshness](https://support.google.com/google-ads/answer/2544985) article in the Google Ads Help Center.

## Managed Service for Apache Airflow connections permissions

Create the following connections in Managed Airflow. See more details in the [Manage Airflow connections documentation](https://docs.cloud.google.com/composer/docs/how-to/managing/connections).

**Connection Name** | **Purpose**  
---|---  
`googleads_raw_dataflow` | For Google Ads API > BigQuery Raw Dataset.   
`googleads_cdc_bq` | For Raw dataset > CDC dataset transfer.   
`googleads_reporting_bq` | For CDC dataset > Reporting dataset transfer.   
  
## Managed Airflow service account permissions

Grant Dataflow permissions to the service account used in Managed Airflow (as configured in the `googleads_raw_dataflow` connection). See instructions in [Dataflow documentation](https://docs.cloud.google.com/dataflow/docs/concepts/security-and-permissions#df-service-account).

## Ingestion settings

Control `Source to Raw` and `Raw to CDC` data pipelines through the settings in the file `[src/GoogleAds/config/ingestion_settings.yaml](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/marketing/src/GoogleAds/config/ingestion_settings.yaml)`. This section describes the parameters of each data pipeline.

### Source to raw tables

This section describes which entities are fetched by APIs and how. Each entry corresponds with one Google Ads entity. Based on this config, Cortex creates Airflow DAGs that run Dataflow pipelines to fetch data using Google Ads APIs.

The following parameters control the settings for `Source to Raw` for each entry:

**Parameter** | **Description**  
---|---  
`load_frequency` | How frequently a DAG for this entity runs to fetch data from Google Ads. For more information about possible values, see [Airflow documentation](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/cron.html).   
`api_name` | API Resource Name (for example, `[customer](https://developers.google.com/google-ads/api/fields/v15/customer)`).   
`table_name` | Table in Raw dataset where the fetched data is stored (for example, `customer`).   
`schema_file` | Schema file in `src/table_schema` directory that maps API response fields to destination table's column names.   
`key` | Columns (separated by comma) that form a unique record for this table.   
`is_metrics_table` | Indicates if a given entry is for a metric entity (in Google Ads API). System treats such tables a bit differently due to the aggregated nature of such tables.   
`partition_details` | **Optional:** If you want this table to be partitioned for performance considerations. For more information, see [Table Partition](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-five#table_partition).   
`cluster_details` | **Optional:** If you want this table to be clustered for performance considerations. For more information, see [Cluster Settings](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-five#cluster_settings).   
  
### Raw to CDC tables

This section describes which entries control how data is moved from raw tables to CDC tables. Each entry corresponds with a raw table (which in turn corresponds with Google Ads API entity as mentioned).

The following parameters control the settings for `Raw to CDC` for each entry:

**Parameter** | **Description**  
---|---  
`table_name` | Table in CDC dataset where the raw data after CDC transformation is stored (for example, `customer`).   
`raw_table` | Table on which raw data has been replicated.   
`key` | Columns (separated by comma) that form a unique record for this table.   
`load_frequency` | How frequently a DAG for this entity runs to populate the CDC table. For more information about possible values, see [Airflow documentation](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/cron.html).   
`schema_file` | Schema file in `src/table_schema` directory that maps raw columns to CDC columns and data type of the CDC column. This is the same schema file that's referred to in the previous section.   
`partition_details` | **Optional:** If you want this table to be partitioned for performance considerations. For more information, see [Table Partition](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-five#table_partition).   
`cluster_details` | **Optional:** If you want this table to be clustered for performance considerations. For more information, see [Cluster Settings](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-five#cluster_settings).   
  
## Reporting settings

You can configure and control how Cortex Framework generates data for the Google Ads final reporting layer using the reporting settings file `[src/GoogleAds/config/reporting_settings.yaml](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/marketing/src/GoogleAds/config/reporting_settings.yaml)`. This file controls how reporting layer BigQuery objects (tables, views,functions or stored procedures) are generated.

For more information, see [Customizing reporting settings file](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-five#customizing_reporting_settings_file).

## What's next?

  * For more information about other data sources and workloads, see [Data sources and workloads](https://docs.cloud.google.com/cortex/docs/v6/data-sources-and-workloads).
  * For more information about the steps for deployment in production environments, see [Cortex Framework Data Foundation deployment prerequisites](https://docs.cloud.google.com/cortex/docs/v6/deployment-prerequisites).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
