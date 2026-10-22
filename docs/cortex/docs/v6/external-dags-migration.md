---
url: https://docs.cloud.google.com/cortex/docs/v6/external-dags-migration/
title: External DAGs migration from v4.2 to v5.0 \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:20.692958+00:00
---

# External DAGs migration from v4.2 to v5.0  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/v6/external-dags-migration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Version 6 Guides ](https://docs.cloud.google.com/cortex/docs/v6/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# External DAGs migration from v4.2 to v5.0 

**Warning:** This page contains specific information to update only Google Cloud Cortex Framework versions 4.2 to 5.0. The content might not apply to other versions.

This guide outlines the steps necessary to relocate output tables from external Directed Acyclic Graphs (DAGs) to their new locations within the Cortex Data Foundation v5.0 architecture. For example, Weather and Trends. This guide is specifically designed for users who have implemented External DAGs in previous Cortex Framework Data Foundation versions (4.2 to 5.0) and are now upgrading. If you haven't used External DAGs or haven't deployed SAP, this guide is not applicable.

## Context

Cortex Framework Data Foundation versions prior to 4.2 used a `_GEN_EXT` flag to manage the deployment of external data sources, with some sources tied to specific workloads (like currency conversion for SAP). However, with version 5.0, this flag has been removed. Now, there's a new module dedicated to managing DAGs that can serve multiple workloads. This guide outlines steps to adjust your existing data pipelines to work with this new structure.

### Cross-workload reusable DAGs

Cortex Framework Data Foundation v5.0 introduces K9, a new component responsible for ingesting, processing, and modeling reusable data elements that are shared across various data sources. Reporting views are now reference the `K9_PROCESSING` dataset to access these reusable components, streamlining data access and reducing redundancy. The following external data sources are now deployed as a part of K9, into the `K9_PROCESSING` dataset:

  * `date_dimension`
  * `holiday_calendar`
  * `trends`
  * `weather`



### SAP-dependent DAGs

The following SAP-dependent DAGs are still triggered by `generate_external_dags.sh` script, but now executes during the reporting build step, and now write into the SAP reporting dataset instead of the CDC (Change Data Capture) stage.

  * `currency_conversion`
  * `inventory_snapshots`
  * `prod_hierarchy_texts`



## Migration Guide

This guide outlines the steps to upgrade your Cortex Framework Data Foundation to version 5.0.

### Deploy Cortex Framework Data Foundation 5.0

First, deploy the newest version (v5.0) of Cortex Framework Data Foundation to your projects, with the following guidelines:

  1. Use your existing RAW and CDC datasets from prior development or staging deployments as your RAW and CDC datasets of this deployment, as no modification is made to them during deployment.
  2. Set both `testData` and `SAP.deployCDC` to `False` in `config/config.json`.
  3. Create a new SAP Reporting project separate from your existing v4.2 environment for testing purposes. This safely evaluate the upgrade process without impacting your current operations.
  4. Optional. If you have active Airflow DAGs running for your previous Cortex Framework Data Foundation version, pause them before proceeding with the migration. This can be done through the Airflow UI. For detailed instructions see [Open Airflow UI from Composer](https://docs.cloud.google.com/composer/docs/how-to/accessing/airflow-web-interface) and [Pause the DAG](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html#dag-pausing-deactivation-and-deletion) documentation.



By following these steps, you can safely transition to Cortex Framework Data Foundation version 5.0 and validate the new features and functionalities.

### Migrate existing tables

To migrate your existing tables to their new location, use `jinja-cli` to format the provided migration script template to complete the migration.

  1. Install jinja-cli with the following command:
         
         pip install jinja-cli
         

  2. Identify the following parameters from your existing version 4.2 and new version 5.0 deployment:

**Name** **Description**  
`project_id_src` Source Google Cloud Project: Project where your existing SAP CDC dataset from version 4.2 deployment is located. `K9_PROCESSING` dataset is also created in this project.   
`project_id_tgt` Target Google Cloud where your newly deployed SAP Reporting dataset from the new version 5.0 deployment is located. This might be different from the source project.   
`dataset_cdc_processed` CDC BigQuery Dataset: BigQuery dataset where the CDC processed data lands the latest available records. This might be the same as the source dataset.   
`dataset_reporting_tgt` Target BigQuery reporting dataset: BigQuery dataset where the Data Foundation for SAP predefined data models are deployed.   
`k9_datasets_processing` K9 BigQuery dataset: BigQuery dataset where the K9 (augmented data sources) is deployed.   
  3. Create a JSON file with the required input data. Make sure to remove any DAGs you don't want to migrate from the `migrate_list` section:
         
         {
           "project_id_src": "your-source-project",
           "project_id_tgt": "your-target-project",
           "dataset_cdc_processed": "your-cdc-processed-dataset",
           "dataset_reporting_tgt": "your-reporting-target-dataset-OR-SAP_REPORTING",
           "k9_datasets_processing": "your-k9-processing-dataset-OR-K9_REPORTING",
           "migrate_list":
             [
                 "holiday_calendar",
                 "trends",
                 "weather",
                 "currency_conversion",
                 "inventory_snapshots",
                 "prod_hierarchy_texts"
             ]
         }
         EOF
         

For example, if you want to remove `weather` and `trends`, the script would look like the following:
         
         {
           "project_id_src": "kittycorn-demo",
           "project_id_tgt": "kittycorn-demo",
           "dataset_cdc_processed": "CDC_PROCESSED",
           "dataset_reporting_tgt": "SAP_REPORTING",
           "k9_datasets_processing": "K9_PROCESSING",
           "migrate_list":
             [
                 "holiday_calendar",
                 "currency_conversion",
                 "inventory_snapshots",
                 "prod_hierarchy_texts"
             ]
             }
         

  4. Create an output folder with the following command:
         
         mkdir output
         

  5. Generate the parsed migration script with the following command (this command assumes you are at the root of the repository):
         
         jinja -d data.json -o output/migrate_external_dags.sql docs/external_dag_migration/scripts/migrate_external_dags.sql
         

  6. Examine the output SQL file and execute in BigQuery to migrate your tables to the new location.




### Update and unpause the Airflow DAGs

Back up the current DAG Files in your Airflow bucket. Then, replace them with the newly generated files from your Cortex Framework Data Foundation version 5.0 deployment. For detail instructions, see the following documentation:

  * [Open Airflow UI from Composer](https://docs.cloud.google.com/composer/docs/how-to/accessing/airflow-web-interface)
  * [Unpause the DAG](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html#dag-pausing-deactivation-and-deletion)



### Validation and cleanup

The migration is now complete. You can now validate that all reporting views in the new v5.0 reporting deployment is working correctly. If everything works properly, go through the process again, this time targeting the v5.0 deployment to your production Reporting set. Afterwards, feel free to remove all tables using the following script:

**Warning:** This step permanently removes your old DAG tables and can't be undone after is applied. Only execute this step after all validation is complete. Consider taking backups of these tables.
    
    
        jinja -d data.json -o output/delete_old_dag_tables.sql docs/external_dag_migration/scripts/delete_old_dag_tables.sql
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
