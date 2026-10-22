---
url: https://docs.cloud.google.com/cortex/docs/v6/optional-step-task-dependent-dags/
title: Task dependent DAGs \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:29.831204+00:00
---

# Task dependent DAGs  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/v6/optional-step-task-dependent-dags/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Version 6 Guides ](https://docs.cloud.google.com/cortex/docs/v6/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Task dependent DAGs

This page outlines the steps to enable task dependent Directed Acyclic Graphs (DAGs) to specify task dependencies between SQL table nodes within a single DAG, rather than relying on cron scheduling across multiple DAGs. Customizable settings are used to generate Managed Service for Apache Airflow DAGs with multiple table refresh nodes that depend on each other. Cortex Framework provides recommended settings for task dependent [SAP DAGs (ECC and S/4HANA)](https://docs.cloud.google.com/cortex/docs/v6/operational-sap). However, you can customize them further or define task dependent DAGs for any [data sources](https://docs.cloud.google.com/cortex/docs/v6/data-sources-and-workloads).

## Enable task dependent DAGs

  1. Modify the [_config.json_](https://github.com/GoogleCloudPlatform/cortex-data-foundation/blob/main/config/config.json) file by setting the `enableTaskDependencies` field to `True`. This setting activates the Cortex Framework's search for task-dependent reporting settings files with the suffix `_task_dep.yaml`.
  2. Create a dedicated reporting settings file with the suffix `_task_dep.yaml` for each data source requiring task dependencies. For more details, see [Define task-dependent reporting settings](https://docs.cloud.google.com/cortex/docs/v6/optional-step-task-dependent-dags#define_task-dependent_reporting_settings).
  3. Customize the task dependencies by adding `table_setting.dag_setting` as a new section to `table` type nodes. For more details, see [Specify and customize task dependencies](https://docs.cloud.google.com/cortex/docs/v6/optional-step-task-dependent-dags#specify_and_customize_task_dependencies).
  4. Build Cortex Framework using the [standard build process](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-six#Cloud%20Composer).
  5. Examine the generated files that are located in the target bucket under `dags/data_source/reporting/task_dep_dags/dag_name`. This folder will contain a Python file defining the Managed Airflow DAG and a SQL file with the refresh query for each table node within the DAG.
  6. Copy the files to the Managed Airflow DAG bucket to deploy Cortex Framework using the [standard build process](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-six#Cloud%20Composer).



## Define task-dependent reporting settings

For each data source requiring task dependencies, Cortex Framework expects task-dependent reporting settings files with the suffix `_task_dep.yaml`. When creating and updating these files, consider the following:

  * For SAP you may customize and use the provided setting files [`reporting_settings_ecc_task_dep.yaml`](https://github.com/GoogleCloudPlatform/cortex-data-foundation/blob/main/src/SAP/SAP_REPORTING/reporting_settings_ecc_task_dep.yaml) and [`reporting_settings_s4_task_dep.yaml`](https://github.com/GoogleCloudPlatform/cortex-data-foundation/blob/main/src/SAP/SAP_REPORTING/reporting_settings_s4_task_dep.yaml).
  * For other data sources, create your own task-dependent reporting settings alongside the original, for example: `reporting_settings_task_dep.yaml.`

**Note:** These settings are distinct from the standard `reporting_settings.yaml` files so they can be enabled and deployed independently. If a data source lacks a `reporting_settings_task_dep.yaml` file, it will use the regular `reporting_settings.yaml` file without task dependencies regardless of the `enableTaskDependencies` value in _config.json_ .

For more information about the fields available within reporting settings files, see [dag_types.py](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/common/materializer/dag_types.py).

## Specify and customize task dependencies

Customize the task dependencies by adding `table_setting.dag_setting` as a new section to `table` type nodes:
    
    
        - sql_file: dependent_table2.sql
          type: table
          table_setting:
            dag_setting:
              name: "dag1"
              parents: ["dependent_table1.sql"]
    

  * DAG settings include two fields:

    * `name`: A required string for **all nodes in a task dependent DAG** that designates the name of the DAG to which the table node belongs. This includes top level nodes which are referenced as a _parent_ by other nodes within the DAG.
    * `parents`: An optional list of strings containing the `sql_file` path of other table nodes within the same DAG. These parents must run successfully before the node is triggered.



**Additional considerations** :

  * Nodes without defined parents are considered top level nodes and will run at the start of the DAG.
  * At least one top level node must have `table_setting.load_frequency` defined, which will be used as the DAG schedule.
  * If multiple top level nodes have defined `load_frequency`, they must be the same.
  * Child nodes that have `parents` defined can't define `load_frequency`.
  * Nodes that don't have `dag_setting` defined will be generated the same as before as a DAG with a single table refresh node and no task dependencies.
  * Other node types like views and scripts can't be included in task dependent DAGs, which only generate nodes with DML to refresh tables.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
