---
url: https://docs.cloud.google.com/cortex/docs/v6/deployment-step-five/
title: Step 5: Configure deployment \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:47.278195+00:00
---

# Step 5: Configure deployment  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/v6/deployment-step-five/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Version 6 Guides ](https://docs.cloud.google.com/cortex/docs/v6/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Step 5: Configure deployment

This page describes the fifth step to deploy Cortex Framework Data Foundation, the core of Cortex Framework. In this step, you modify the configuration file in the Cortex Framework Data Foundation repository to match your requirements.

**Note:** The steps outlined in this page are specifically designed for deploying Cortex Framework Data Foundation from the [official GitHub repository](https://github.com/GoogleCloudPlatform/cortex-data-foundation).

## Configuration file

The behavior of the deployment is controlled by the configuration file `config.json` in the [Cortex Framework Data Foundation](https://github.com/GoogleCloudPlatform/cortex-data-foundation). This file contains global configuration, specific configuration to each workload. Edit the `config.json` file according to your needs with the following steps:

  1. Open the file [`config.json`](https://github.com/GoogleCloudPlatform/cortex-data-foundation/blob/main/config/config.json) from Cloud Shell.
  2. Edit the `config.json` file according to the following parameters:

**Note:** See more parameters specifically for [Cortex for Meridan](https://docs.cloud.google.com/cortex/docs/v6/meridian) on [Additional deployment parameters for Meridian](https://docs.cloud.google.com/cortex/docs/v6/meridian#additional_deployment_parameters_for_merdian).**Parameter** **Meaning** **Default Value** **Description**  
`testData` Deploy Test Data `true` Project where the source dataset is and the build runs. **Note: Test data deployment will only execute if the raw dataset is empty and has no tables**.   
`deploySAP` Deploy SAP `true` Execute the deployment for SAP workload (ECC or S/4 HANA).   
`deploySFDC` Deploy Salesforce `true` Execute the deployment for Salesforce workload.   
`deployMarketing` Deploy Marketing `true` Execute the deployment for Marketing sources (Google Ads, CM360, and TikTok).   
`deployOracleEBS` Deploy Oracle EBS `true` Execute the deployment for Oracle EBS workload.   
`enableTaskDependencies` Task dependent DAGs `false` Enable task dependent DAGs so supported SQL tables will be executed based on dependency order, within single DAGs. For more information, see [Task dependent DAGs](https://docs.cloud.google.com/cortex/docs/v6/optional-step-task-dependent-dags).   
`turboMode` Deploy in [Turbo mode](https://docs.cloud.google.com/cortex/docs/v6/optional-step-turbo-mode). `true` Execute all views builds as a step in the same Cloud Build process, in parallel for a faster deployment. If set to `false`, each reporting view is generated in its own sequential build step. We recommend only setting it to `true` when using test data or after any mismatch between reporting columns and the source data have been resolved.   
`projectIdSource` Source Project ID \- Project where the source dataset is and the build runs.   
`projectIdTarget` Target Project ID \- Target project for user-facing datasets.   
`targetBucket` Target Bucket to storage generated DAG scripts \- Bucket [created previously](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-four#create_a_storage_bucket_for_storing_dag_related_files) where DAGs (and Dataflow temp files) are generated. Avoid using the actual Airflow bucket.   
`location` Location or Region `"US"` Location where the BigQuery dataset and Cloud Storage buckets are. 

See restrictions listed under [BigQuery dataset locations](https://docs.cloud.google.com/bigquery/docs/locations).   
  
`testDataProject` Source for test harness `kittycorn-public` Source of the test data for demo deployments. Applies when `testData` is `true`. 

Don't change this value, unless you have your own test harness.   
  
`k9.datasets.processing` K9 datasets - Processing `"K9_PROCESSING"` Execute cross-workload templates (for example, date dimension) as defined in the [K9 configuration file](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/k9/config/k9_settings.yaml). These templates are normally required by the downstream workloads.   
`k9.datasets.reporting` K9 datasets - Reporting `"K9_REPORTING"` Execute cross-workload templates and external data sources (for example: weather) as defined in the [K9 configuration file](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/k9/config/k9_settings.yaml). Commented out by default.   
  3. Configure your required workload(s) as needed. You don't need to configure them if the deployment parameter (for example, `deploySAP` or `deployMarketing`) for the workload is set to `False`. For more information, see [Step 3: Determine integration mechanism](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-three).


**Note:** When installing multiple Cortex Framework workloads, you need to increase the `Build and Operation Get requests per minute` and `Build and Operation Get requests per minute per user` quotas. For more information, see [Quotas and system limits](https://cloud.google.com/cortex/quotas).

For a better customization of your deployment, see the following **optional steps** :

  * [Telemetry Opt Out](https://docs.cloud.google.com/cortex/docs/v6/optional-step-telemetry).
  * [External datasets configuration for K9](https://docs.cloud.google.com/cortex/docs/v6/optional-step-external-datasets).
  * [Check for `CORTEX-CUSTOMER` tags](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-six#customize_and_prepare_for_upgrade).



## Performance optimization for reporting views

Reporting artifacts can be created as views or as tables refreshed regularly through DAGs. On one hand, views compute the data on each execution of a query, which keep the results always fresh. On the other hand, the table runs the computations once, and the results can be queried multiple times without incurring higher computing costs and achieving faster runtime. Each customer creates their own configuration according to their needs.

Materialized results are updated into a table. These tables can be further fine-tuned by adding Partitioning and Clustering to these tables.

The configuration files for each workload are located in the following paths within the Cortex Framework Data Foundation repository:

**Data Source** **Settings files**  
Operational - SAP [`src/SAP/SAP_REPORTING/reporting_settings_ecc.yaml`](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/SAP/SAP_REPORTING/reporting_settings_ecc.yaml)  
Operational - Salesforce Sales Cloud [`src/SFDC/config/reporting_settings.yaml`](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/SFDC/config/reporting_settings.yaml)  
Operational - Oracle EBS [`src/oracleEBS/config/reporting_settings.yaml`](https://github.com/GoogleCloudPlatform/cortex-data-foundation/blob/main/src/OracleEBS/config/reporting_settings.yaml)  
Marketing - Google Ads [`src/marketing/src/GoogleAds/config/reporting_settings.yaml`](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/marketing/src/GoogleAds/config/reporting_settings.yaml)  
Marketing - CM360 [`src/marketing/src/CM360/config/reporting_settings.yaml`](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/marketing/src/CM360/config/reporting_settings.yaml)  
Marketing - Meta [`src/marketing/src/Meta/config/reporting_settings.yaml`](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/marketing/src/Meta/config/reporting_settings.yaml)  
Marketing - Salesforce Marketing Cloud [`src/marketing/src/SFMC/config/reporting_settings.yaml`](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/marketing/src/SFMC/config/reporting_settings.yaml)  
Marketing - TikTok [`src/marketing/src/TikTok/config/reporting_settings.yaml`](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/marketing/src/TikTok/config/reporting_settings.yaml)  
Marketing - YouTube (with DV360) [`src/marketing/src/DV360/config/reporting_settings.yaml`](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/marketing/src/DV360/config/reporting_settings.yaml)  
Marketing - Google Analytics 4 [`src/marketing/src/GA4/config/reporting_settings.yaml`](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/marketing/src/GA4/config/reporting_settings.yaml)  
Marketing - Cross Media & Product Connected Insights [`src/marketing/src/CrossMedia/config/reporting_settings.yaml`](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/marketing/src/CrossMedia/config/reporting_settings.yaml)  
  
## Customizing reporting settings file

The `reporting_settings` files drives how the BigQuery objects (tables or views) are created for reporting datasets. Customize your file with the following parameters descriptions. Consider that this file contains two sections:

  1. `bq_independent_objects`: All BigQuery objects that can be created independently, without any other dependencies. When [`Turbo mode`](https://docs.cloud.google.com/cortex/docs/v6/optional-step-turbo-mode) is enabled, these BigQuery objects are created in parallel during the deployment time, speeding up the deployment process.
  2. `bq_dependent_objects`: All BigQuery objects that need to be created in a specific order due to dependencies on other BigQuery objects. [`Turbo mode`](https://docs.cloud.google.com/cortex/docs/v6/optional-step-turbo-mode) doesn´t apply to this section.



The deployer first creates all the BigQuery objects listed in `bq_independent_objects`, and then all the objects listed in `bq_dependent_objects`. Define The following properties for each object:

  1. `sql_file`: Name of the SQL file that creates a given object.
  2. `type`: Type of BigQuery object. Possible values: 
     * `view` : If you want the object to be a BigQuery view.
     * `table`: If you want the object to be a BigQuery table.
     * `script`: This is to create other types of objects (for example, BigQuery functions and stored processes).
  3. If `type` is set to `table`, the following optional properties can be defined: 
     * `load_frequency`: Frequency at which a Composer DAG is executed to refresh this table. See [Airflow documentation](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/cron.html) for details on possible values.
     * `partition_details`: How the table should be partitioned. This value is **optional**. For more information, see section Table partition.
     * `cluster_details`: How the table should be clustered. This value is **optional**. For more information, see section Cluster settings.

**Note:** If you enabled Task dependent DAGs by setting the `enableTaskDependencies` field to `True`, make sure to create a dedicated reporting settings file with the suffix `_task_dep.yaml` for each data source requiring task dependencies. For more information, see [Task dependent DAGs](https://docs.cloud.google.com/cortex/docs/v6/optional-step-task-dependent-dags)

### Table partition

Certain settings files let you configure materialized tables with custom clustering and partitioning options. This can significantly improve query performance for large datasets. This option applies only for `SAP cdc_settings.yaml` and all `reporting_settings.yaml` files.

Table Partitioning can be enabled by specifying the following`partition_details`:
    
    
    - base_table: vbap
      load_frequency: "@daily"
      partition_details: {
        column: "erdat", partition_type: "time", time_grain: "day" }
    

Use the following parameters to control partitioning details for a given table:

**Property** **Description** **Value**  
`column` Column by which the CDC table is partitioned. Column name.   
`partition_type` Type of partition. `"time"` for time based partition. For more information, see [Timestamp partitioned tables](https://docs.cloud.google.com/bigquery/docs/partitioned-tables#date_timestamp_partitioned_tables). `"integer_range"` for integer based partition. For more information, see [Integer range documentation](https://docs.cloud.google.com/bigquery/docs/partitioned-tables#integer_range).   
`time_grain` Time part to partition with Required when `partition_type = "time"`. `"hour"`, `"day"`, `"month"` or `"year"`.   
`integer_range_bucket` Bucket range Required when `partition_type = "integer_range"` `"start"` = Start value, `"end"` = End value, and `"interval`" = Interval of range.   
  
For more information about options and related limitations, see [BigQuery Table Partition](https://docs.cloud.google.com/bigquery/docs/partitioned-tables).

### Cluster settings

Table clustering can be enabled by specifying `cluster_details`:
    
    
      - base_table: vbak
        load_frequency: "@daily"
        cluster_details: {columns: ["vkorg"]}
    

Use the following parameters to control cluster details for a given table:

**Property** **Description** **Value**  
`columns` Columns by which a table is clustered. List of column names. For example, `"mjahr"` and `"matnr"`.   
  
For more information about options and related limitations, see [Table cluster documentation](https://docs.cloud.google.com/bigquery/docs/clustered-tables).

## Next steps

After you complete this step, move on to the following deployment step:

  1. [Establish workloads](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-one).
  2. [Clone repository](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-two).
  3. [Determine integration mechanism](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-three).
  4. [Set up components](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-four).
  5. [Configure deployment](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-five) (this page).
  6. [Execute deployment](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-six).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
