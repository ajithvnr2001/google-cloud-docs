---
url: https://docs.cloud.google.com/cortex/docs/v6/marketing-salesforce/
title: Integration with Salesforce Marketing Cloud \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:04.248269+00:00
---

# Integration with Salesforce Marketing Cloud  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/v6/marketing-salesforce/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Version 6 Guides ](https://docs.cloud.google.com/cortex/docs/v6/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integration with Salesforce Marketing Cloud

This page describes the required configurations to bring data from Salesforce Marketing Cloud (SFMC) as a data source of the marketing workload of Cortex Framework Data Foundation.

SFMC is a digital marketing automation platform offered by Salesforce. It provides businesses with a comprehensive suite of tools to manage and automate various marketing activities across multiple channels. Cortex Framework acts as the data analysis and AI engine that helps you understand the results, identify areas for improvement, and optimize your marketing strategy for better outcomes.

The following diagram describes how SFMC data is available through the marketing workload of Cortex Framework Data Foundation:

![SFMC data source](https://docs.cloud.google.com/cortex/docs/images/sfmc-data-source.png)

**Figure 1**. SFMC data source.**Note:** For accessing configuration files, analytical views and models for the Salesforce Marketing Cloud data source, see the [data source directory](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/marketing/src/SFMC).

## Configuration file

The [`config.json`](https://github.com/GoogleCloudPlatform/cortex-data-foundation/blob/main/config/config.json) file configures the settings required to connect to data sources for transferring data from various workloads. This file contains the following parameters for SFMC:
    
    
       "marketing": {
            "deploySFMC": true,
            "SFMC": {
                "deployCDC": true,
                "fileTransferBucket": "",
                "datasets": {
                    "cdc": "",
                    "raw": "",
                    "reporting": "REPORTING_SFMC"
                }
            }
        }
    

The following table describes the value for each marketing parameter:

**Parameter** | **Meaning** | **Default Value** | **Description**  
---|---|---|---  
`marketing.deploySFMC` | Deploy SFMC  | `true` | Execute the deployment for SFMC data source.   
`marketing.SFMC.deployCDC` | Deploy CDC scripts for SFMC  | `true` | Generate Salesforce Marketing Cloud (SFMC) CDC processing scripts to run as DAGs in Managed Airflow.   
`marketing.SFMC.fileTransferBucket` | Bucket with Data Extract files  | \-  | Bucket where Salesforce Marketing Cloud (SFMC) Automation Studio Data Extract files are stored.   
`marketing.SFMC.datasets.cdc` | CDC dataset for SFMC  |  | CDC dataset for Salesforce Marketing Cloud (SFMC).   
`marketing.SFMC.datasets.raw` | Raw dataset for SFMC  |  | Raw dataset for Salesforce Marketing Cloud (SFMC).   
`marketing.SFMC.datasets.reporting` | Reporting dataset for SFMC  | `"REPORTING_SFMC"` | Reporting dataset for Salesforce Marketing Cloud (SFMC).   
  
## Data Model

This section describes the Salesforce Marketing Cloud (SFMC) Data Model using the Entity Relationship Diagram (ERD).

[![Entity Relationship Diagram for SFMC](https://docs.cloud.google.com/cortex/docs/images/erd_sfmc.png)](https://docs.cloud.google.com/cortex/docs/images/erd_sfmc.png)

**Figure 2**. Salesforce Marketing Cloud (SFMC): Entity Relationship Diagram.

### Base views

These are the blue objects in the ERD and are views on CDC tables with no transforms other than some column name aliases. See scripts in [`src/marketing/src/SFMC/src/reporting/ddls`](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/marketing/src/SFMC/src/reporting/ddls).

### Reporting views

These are the green objects in the ERD and are reporting views that contain aggregate metrics. See scripts in [`src/marketing/src/SFMC/src/reporting/ddls`](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/marketing/src/SFMC/src/reporting/ddls).

## Data Extraction using Automation Studio

[SFMC Automation Studio](https://help.salesforce.com/s/articleView?id=sf.mc_as_automation_studio.htm) allows consumers of SFMC to export their SFMC data to various storage systems. Cortex Framework Data Foundation looks for a set of files created with Automation Studio in a Cloud Storage bucket. You also need to use [SFMC Email Studio](https://help.salesforce.com/s/articleView?id=sf.mc_es_email_studio.htm&type=5) in this process.

**Note:** base version of SFMC doesn't offer Automation Studio, but it is available for all the other versions.

To set up the data extract and export processes, follow these steps:

  1. **Set up a Cloud Storage bucket.** This bucket stores files exported from SFMC. Name the bucket `marketing.SFMC.fileTransferBucket` config parameter. See the instructions in the [Salesforce documentation](https://help.salesforce.com/s/articleView?id=sf.mc_overview_set_up_google_cloud_location.htm).
  2. **Create data extensions.** For each entity you want to extract data for, create a [Data Extension in Email Studio](https://help.salesforce.com/s/articleView?id=sf.mc_es_create_data_extension.htm&type=5). This is needed to identify the data sources from the SFMC internal database.

     * List all the fields that are defined in `src/SFMC/config/table_schema` for the entity. If you need to customize this to extract more or less fields, make sure the list of fields are aligned in these steps as well as in the table schema files. For example:
    
    Entity: unsubscribe
      Fields:
      AccountID
      OYBAccountID
      JobID
      ListID
      BatchID
      SubscriberID
      SubscriberKey
      EventDate
      IsUnique
      Domain
    

  3. **Create SQL query activities.** For each entity, create a [SQL Query Activity](https://help.salesforce.com/s/articleView?id=sf.mc_as_use_the_sql_query_activity.htm&type=5). This activity is connected to its corresponding data extension created earlier. See [Salesforce documentation ](https://help.salesforce.com/s/articleView?id=sf.mc_as_use_the_sql_query_activity.htm&type=5) for this step:

     1. Define SQL query with all the relevant fields. The query needs to select all the fields relevant to the entity that is defined in the data extension in the previous step.
     2. Select the correct data extension as target.
     3. Select **Overwrite** as Data Action.
     4. See the following example query:
    
    SELECT
        AccountID,
        OYBAccountID,
        JobID,
        ListID,
        BatchID,
        SubscriberID,
        SubscriberKey,
        EventDate,
        IsUnique,
        Domain
      FROM
        _Unsubscribe
    

  4. **Create data extract activities.** See Salesforce documentation for creating a [Data Extract Activity ](https://help.salesforce.com/s/articleView?id=sf.mc_as_use_a_data_extract_activity.htm&language=en_us&type=5) for each entity. This activity gets the data from the Salesforce Data Extension and extracts it to a csv file. For this step:

     1. Use the correct naming pattern. It should match the pattern defined in the settings. For example, for `Unsubscribe` entity, the filename can be something like `unsubscribe_%%Year%%_%%Month%%_%%Day%% %%Hour%%.csv`.
     2. Set **Extract Type** to `Data Extension Extract`.
     3. Select **Has column Headers** and **Text Qualified** options.
  5. **Create file conversion activities to convert format from UTF-16 to UTF-8**. By default Salesforce exports CSV files in UTF-16. In this step you convert it to UTF-8 format. For each entity, create another [Data Extract Activity](https://help.salesforce.com/s/articleView?id=sf.mc_as_use_a_data_extract_activity.htm&language=en_us&type=5), for file conversion. For this step:

     * Use the same filename pattern that was used in the previous step of Data Extraction Activity.
     * Set **Extract Type** to `File Convert`
     * Select `UTF8` form the drop-down at `Convert To`.
  6. **Create file transfer activities.** Create a [File Transfer Activity](https://help.salesforce.com/s/articleView?id=sf.mc_as_using_the_file_transfer_activity.htm&type=5) for each entity. These activities move the extracted csv files from the Salesforce Safehouse to Cloud Storage buckets. For this step:

     * Use the same filename pattern used in prior steps.
     * Select a Cloud Storage bucket that was setted up earlier in the process as destination.
  7. **Schedule the execution.** After all the activities are complete, set up [automated schedules](https://help.salesforce.com/s/articleView?id=sf.mc_as_schedule_an_automation.htm&type=5) to run them.




## Data Freshness and Delay

As a general rule, data freshness for Cortex Framework data sources is limited by what upstream connection allows for, as well as the frequency of your DAG execution. Adjust your DAG execution frequency to align with upstream frequency, resource constraints, and your business needs.

With SFMC Automation Studio, the data freshness delay depends on the scheduling delay when data export is set up.

## Managed Service for Apache Airflow connections permissions

Create the following connections in Managed Airflow. See more details in the [Manage Airflow connections documentation](https://docs.cloud.google.com/composer/docs/how-to/managing/connections).

**Connection Name** | **Purpose**  
---|---  
`sfmc_raw_dataflow` | For SFMC Extracted files > BigQueryRaw dataset.   
`sfmc_cdc_bq` | For Raw dataset > CDC dataset transfer.   
`sfmc_reporting_bq` | For CDC dataset > Reporting dataset transfer.   
  
## Managed Airflow service account permissions

The service account used in Managed Airflow (as configured in the `sfmc_raw_dataflow` connection) needs Dataflow related permissions. See instructions in [Dataflow documentation](https://docs.cloud.google.com/dataflow/docs/concepts/security-and-permissions#df-service-account)

## Ingestion settings

Control `Source to Raw` and `Raw to CDC` data pipelines through the settings in the file `[src/SFMC/config/ingestion_settings.yaml ](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/marketing/src/SFMC/config/ingestion_settings.yaml)`. This section describes the parameters of each data pipeline.

### Source to raw tables

This section has entries that control how files extracted from Automation Studio are used. Each entry corresponds with one SFMC entity. Based on this config, Cortex Framework creates Airflow DAGs that run Dataflow pipelines to load data from exported files into BigQuery tables in raw dataset.

Directory `src/SFMC/config/table_schema` contains a schema file for each entity that is extracted from SFMC. Each file explains how to read the csv files extracted from Automaton Studio in order to successfully load them into BigQueryraw dataset.

Each schema file contains three columns:

  * `SourceField`: Field name of the csv file.
  * `TargetField`: Column name in the raw table for this entity.
  * `DataType`: Data type of each raw table field.



The following parameters control the settings for `Source to Raw` for each entry:

**Parameter** | **Description**  
---|---  
`base_table` | Raw table name in which an SFMC entity extracted data is loaded.   
`load_frequency` | How frequently a DAG for this entity runs to load data from extracted files. For more information about possible values, see [Airflow documentation](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/cron.html).   
`file_pattern` | Pattern for file for this table that's exported from Automation Studio into Cloud Storage bucket. Change this only if you chose a different name than the ones suggested for extracted files.   
`partition_details` | How the raw table is partitioned for performance considerations. For more information, see [Table Partition](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-five#table_partition).   
`cluster_details` | **Optional:** If you want the raw table to be clustered for performance considerations. For more information, see [Cluster Settings](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-five#cluster_settings).   
  
### Raw to CDC tables

This section describes which entries control how data is moved from raw tables to CDC tables. Each entry corresponds with a raw table.

The following parameters control the settings for `Raw to CDC` for each entry:

**Parameter** | **Description**  
---|---  
`base_table` | Table in CDC dataset where the raw data after CDC transformation is stored.   
`load_frequency` | How frequently a DAG for this entity runs to populate the CDC table. For more information about possible values, see [Airflow documentation](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/cron.html).   
`raw_table` | Source table from raw dataset.   
`row_identifiers` | Columns (separated by comma) that form a unique record for this table.   
`partition_details` | How the CDC table is partitioned for performance considerations. For more information, see [Table Partition](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-five#table_partition).   
`cluster_details` | **Optional:** If you want this table to be clustered for performance considerations. For more information, see [Cluster Settings](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-five#cluster_settings).   
  
## Reporting settings

You can configure and control how Cortex Framework generates data for the SFMC final reporting layer using the reporting settings file (`[src/SFMC/config/reporting_settings.yaml](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/marketing/src/SFMC/config/reporting_settings.yaml)`). This file controls how reporting layer BigQuery objects (tables, views,functions or stored procedures) are generated. For more information, see [Customizing reporting settings file](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-five#customizing_reporting_settings_file).

## What's next?

  * For more information about other data sources and workloads, see [Data sources and workloads](https://docs.cloud.google.com/cortex/docs/v6/data-sources-and-workloads).
  * For more information about the steps for deployment in production environments, see [Cortex Framework Data Foundation deployment prerequisites](https://docs.cloud.google.com/cortex/docs/deployment-prerequisites).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
