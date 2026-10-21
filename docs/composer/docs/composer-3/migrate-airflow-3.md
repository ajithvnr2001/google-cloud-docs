---
url: https://docs.cloud.google.com/composer/docs/composer-3/migrate-airflow-3/
title: Migrate environments to Airflow 3 (side-by-side) \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:26:57.558329+00:00
---

# Migrate environments to Airflow 3 (side-by-side)  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-3/migrate-airflow-3/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 3 Guides ](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview)



Send feedback 

#  Migrate environments to Airflow 3 (side-by-side) Stay organized with collections  Save and categorize content based on your preferences. 

**Managed Airflow (Gen 3)** | Managed Airflow (Gen 2) | Managed Airflow (Legacy Gen 1)

This page explains how to transfer DAGs, data and configuration from your existing Managed Airflow (Gen 3) environment with Airflow 2 to a Managed Airflow (Gen 3) environments with Airflow 3.

**Note:** Managed Airflow supports only side-by-side transfers of your existing Managed Airflow (Gen 3) Airflow 2 environments to environments with Airflow 3. It isn't possible to upgrade Airflow 2 environments to Airflow 3 in-place. However, you can still upgrade environments with Airflow 3 to later Airflow 3 versions as usual.

## Other migration guides

From | To | Method | Guide  
---|---|---|---  
Managed Airflow (Gen 3), Airflow 2 | Managed Airflow (Gen 3), Airflow 3 | Side-by-side, manual transfer | This guide  
Managed Airflow (Gen 2) | Managed Airflow (Gen 3) | Side-by-side, using the migration script | [Script migration guide](https://docs.cloud.google.com/composer/docs/composer-2/migrate-composer-3-script)  
Managed Airflow (Gen 2) | Managed Airflow (Gen 3) | Side-by-side, using snapshots | [Snapshots migration guide](https://docs.cloud.google.com/composer/docs/composer-2/migrate-composer-3)  
Managed Airflow (Legacy Gen 1), Airflow 2 | Managed Airflow (Gen 3) | Side-by-side, using snapshots | [Snapshots migration guide](https://docs.cloud.google.com/composer/docs/composer-1/migrate-composer-1-to-3)  
Managed Airflow (Legacy Gen 1), Airflow 2 | Managed Airflow (Gen 2) | Side-by-side, using snapshots | [Snapshots migration guide](https://docs.cloud.google.com/composer/docs/composer-1/migrate-composer-2-snapshots-af-2)  
Managed Airflow (Legacy Gen 1), Airflow 2 | Managed Airflow (Gen 2) | Side-by-side, manual transfer | [Manual migration guide](https://docs.cloud.google.com/composer/docs/composer-1/migrate-composer-2-af-2)  
Managed Airflow (Legacy Gen 1), Airflow 1 | Managed Airflow (Gen 2), Airflow 2 | Side-by-side, using snapshots | [Snapshots migration guide](https://docs.cloud.google.com/composer/docs/composer-1/migrate-composer-2-snapshots-af-1)  
Managed Airflow (Legacy Gen 1), Airflow 1 | Managed Airflow (Gen 2), Airflow 2 | Side-by-side, manual transfer | [Manual migration guide](https://docs.cloud.google.com/composer/docs/composer-1/migrate-composer-2-af-1)  
Managed Airflow (Legacy Gen 1), Airflow 1 | Managed Airflow (Legacy Gen 1), Airflow 2 | Side-by-side, manual transfer | [Manual migration guide](https://docs.cloud.google.com/composer/docs/composer-1/migrate-environments-airflow-2)  
  
## Changes introduced in Airflow 3

Before you start using Managed Airflow environments with Airflow 3, consider changes that Airflow 3 brings to Managed Airflow (Gen 3) environments.

For an overview of changes introduced in the community version of Airflow 3, see [Apache Airflow 3 is Generally Available!](https://airflow.apache.org/blog/airflow-three-point-oh-is-here/).

### DAG versioning

  * In Airflow 3, a DAG will run through to completion based on the version at start, even if a new version was uploaded while the DAG run was running.

    * All DAG runs in the Airflow UI are now associated with the corresponding DAG version (the version at the moment of execution). This includes task structure and DAG code.

**Note:** Airflow 3 **DAG bundles** aren't yet supported in Managed Airflow. We're working to add support for DAG bundles in later Managed Airflow (Gen 3) versions. While this feature isn't supported, Airflow 3 always runs the latest version of the uploaded DAG code. However, all other aspects of Airflow 3 DAG versioning such as task structure, code and DAG run history are supported in the Airflow UI.

### Backfills improvements

Airflow 3 introduces a major overhaul to how backfills (re-running pipelines for historical data) are handled. Backfills are moving from a manual process to a fully observable feature integrated into the core Airflow engine:

  * Backfills are now managed directly within the Airflow scheduler, rather than being treated as separate, manual processes. This leads to better scalability and more precise control.
  * You can now trigger, stop, and monitor backfill progress directly through the Airflow UI or API calls, in addition to Airflow CLI.
  * Airflow scheduler provides better visibility into the status and health of the historical backfill runs.
  * While heavily requested by the machine learning community (for retraining models on old data), backfill improvements apply to all ETL/ELT workflows.



### Improved security and reliability

  * In Airflow 3, tasks communicate only with the central API Server through the Task SDK (in Airflow 2 tasks could have direct database access). The API Server pools these connections efficiently. Your database is protected from connection spikes, making the entire environment more stable under heavy loads.

  * By utilizing a new Task Execution Interface, Airflow 3 supports better isolation between tasks preventing one task from potentially interfering with or accessing another task's data.

  * The CLI of Airflow 3 is moving away from direct database access. A new `airflowctl` command-line interface is a separate package designed specifically for remote access through the API. Instead of direct access to the database, it interacts with Airflow through APIs, which is more secure.




### Event-driven scheduling and Data Assets

  * [Datasets](https://airflow.apache.org/docs/apache-airflow/2.10.5/authoring-and-scheduling/datasets.html#what-is-a-dataset) have evolved into [Data Assets](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/assets.html#what-is-an-asset). Data Assets allow Airflow to better track and react to data created or updated by systems outside of Airflow.

  * A new concept called _Watchers_ was introduced in Airflow 3. These are components that watch for changes to a Data Asset, allowing Airflow to trigger workflows the moment data arrives. Instead of polling (checking every minute if a file exists), a DAG can now be triggered instantly the moment a message hits a message queue.

  * Airflow 3 introduces a new Asset-Centric Syntax using Python decorators, making the code cleaner and more intuitive for developers.




### Modernized Airflow UI

  * Airflow UI was rewritten from scratch using React (frontend) and FastAPI (backend).
  * The new Airflow UI performs its operations through a standardized REST API and a specialized API for UI operations.
  * By replacing the Flask implementation with FastAPI, the Airflow UI is significantly more responsive.
  * The Grid and Graph views were unified for a smoother workflow, making it easier to jump between high-level DAG structures and specific task logs.



## Breaking changes in Airflow 3

Airflow 3 introduces some major changes some of which are breaking:

  * Existing DAGs from Airflow 2 aren't guaranteed to work with Airflow 3 out of the box. They must to be tested and possibly adjusted by changing imports, DAG parameters, and other implementation details.
  * Some Airflow 2 configuration options are renamed or removed in Airflow 3. See the [Airflow Configuration Reference](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html) for more information about parameters.

  * No direct access to the Airflow database access from the task code:

    * Task code can no longer directly import and use Airflow database sessions or models.
    * It's not possible to use `PostgresHook` and `PostgresOperator` with the `airflow_db` connection.
  * Some custom PyPI packages might be incompatible with the new version of Airflow and its dependencies.

  * REST API (`/api/v1`) replaced with [`/api/v2`](https://airflow.apache.org/docs/apache-airflow/stable/stable-rest-api-ref.html).

  * SubDAGs are replaced by TaskGroups, Assets, and Data Aware Scheduling.

  * SLAs are deprecated and removed. They are replaced with [Deadline Alerts](https://airflow.apache.org/docs/apache-airflow/stable/howto/deadline-alerts.html).

  * The subdir argument in CLI commands was removed.

  * Some Airflow context variables were removed. For more information, see [Breaking Changes](https://airflow.apache.org/docs/apache-airflow/stable/installation/upgrading_to_airflow3.html#breaking-changes) in the Airflow documentation.

  * The `catchup_by_default` DAG parameter is now `False` by default.

  * The `create_cron_data_intervals` configuration is now `False` by default. This means that the `CronTriggerTimetable` will be used by default instead of the `CronDataIntervalTimetable`.

  * [List of changes for Airflow 3.0.0](https://airflow.apache.org/docs/apache-airflow/stable/release_notes.html#airflow-3-0-0-2025-04-22).

  * [List of changes for Airflow 3.1.0](https://airflow.apache.org/docs/apache-airflow/stable/release_notes.html#airflow-3-1-0-2025-09-25).




## Differences between environments with Airflow 3 and Airflow 2

The major differences between Managed Airflow environments with Airflow 2 and environments with Airflow 3 are:

  * Workloads configuration in Airflow 3 environments:

    * The [minimum amount of memory](https://docs.cloud.google.com/composer/docs/composer-3/scale-environments#limits) for all Airflow components is 2 GB.
    * Configurations for Airflow triggerers and workers in [environment presets](https://docs.cloud.google.com/composer/docs/composer-3/environment-scaling#scale-and-performance-parameters) are changed compared to Airflow 2 environments.
    * The default number of CPUs for triggerers is 1.
    * The default number of memory for triggerers is 2 GB.
  * The automatic calculation of the `[celery]worker_concurrency` configuration option's is changed to accommodate different memory usage by Airflow 3 components.

  * In Airflow 3, there is no way to directly [access the Airflow database](https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-database) from the task code.

  * Airflow 3 uses the [`airflowctl` command-line utility](https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-cli#airflowctl) to run Airflow CLI commands.

  * Preinstalled PyPI packages are different in Airflow 3 environments. For a list of preinstalled PyPI packages, see [Preinstalled packages changelog](https://docs.cloud.google.com/composer/docs/versions-packages).




## Migrate to Airflow 3 side-by-side

The side-by-side migration process has the following steps:

  1. Check compatibility with Airflow 3.
  2. Create an Airflow 3 environment, transfer configuration overrides and environment variables.
  3. Install PyPI packages to the Airflow 3 environment.
  4. Transfer variables, connections and pools to Airflow 3.
  5. Transfer other data from your Airflow 2.* environment bucket.
  6. Transfer users and roles.
  7. Make sure that your DAGs are ready for Airflow 3.
  8. Transfer DAGs to the Airflow 3 environment.
  9. Monitor your Airflow 3 environment.



### Step 1: Check compatibility with Airflow 3

To check compatibility with Airflow 3:

  * Check that your environment uses Airflow version 2.7 or later. We recommend to [upgrade](https://docs.cloud.google.com/composer/docs/composer-3/upgrade-environments) to the latest Airflow 2 version first, and only then migrate to Airflow 3.
  * Check that the [environment is healthy](https://docs.cloud.google.com/composer/docs/composer-3/use-monitoring-dashboard#environment-overview) and is running without issues for some time.
  * Make sure that your DAGs and Airflow configuration don't use any features or functionality that was removed in Airflow 3.
  * Read instructions for changing your DAGs to be compatible with Airflow 3 to see if any changes in your DAGs will be required during the migration process.
  * Check your Airflow DAGs for compatibility using the `ruff` tool provided by the community version of Airflow. For instructions, see [Check your Airflow DAGs for compatibility](https://airflow.apache.org/docs/apache-airflow/stable/installation/upgrading_to_airflow3.html#step-3-dag-authors-check-your-airflow-dags-for-compatibility) in the Airflow documentation. 



### Step 2: Create an Airflow 3 environment, transfer configuration overrides and environment variables

In this step, you create a new Managed Airflow (Gen 3) environment with Airflow 3 and start transferring the configuration parameters from your Airflow 2 environment:

Follow the [steps for creating a Managed Airflow (Gen 3) environment](https://docs.cloud.google.com/composer/docs/composer-3/create-environments) and do the following:

  1. When you select an Airflow build, select a build with Airflow 3.
  2. Copy all compatible Airflow configuration option overrides from your Airflow 2 environment.

**Important:** Some configuration options **use a different name and section** in Airflow 3. This page provides a non-exhaustive list of such options.
  3. Copy all environment variables from your Airflow 2 environment.

  4. Proceed to create an environment with Airflow 3.




The following table lists some Airflow configuration options changes. The list is non-exhaustive. For more information about changes in Airflow configuration options, see [Airflow Configuration Reference](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html) and [Airflow Release Notes](https://airflow.apache.org/docs/apache-airflow/stable/release_notes.html) in the Airflow documentation.

Airflow 2 option | Airflow 3 option  
---|---  
`[scheduler]min_file_process_interval` |  `[dag_processor]min_file_process_interval`  
`[webserver]rbac_user_registration_role` |  `[api]rbac_user_registration_role`  
`[core]dag_file_processor_timeout` |  `[dag_processor]dag_file_processor_timeout`  
`[scheduler]dag_dir_list_interval` |  `[dag_processor]refresh_interval`  
`[scheduler]max_threads` |  `[dag_processor]parsing_processes`  
`[scheduler]parsing_processes` |  `[dag_processor]parsing_processes`  
`[webserver]instance_name` |  `[api]instance_name`  
`[scheduler]scheduler_zombie_task_threshold` |  `[scheduler]task_instance_heartbeat_timeout`  
`[webserver]rbac` |  Deprecated   
`[api]auth_backend=airflow.api.auth.backend.deny_all` |  Deprecated   
`[api]auth_backends=airflow.api.auth.backend.deny_all` |  Deprecated   
`[api]composer_auth_user_registration_role` |  Deprecated   
  
### Step 3: Install PyPI packages to the Airflow 3 environment

After your Airflow 3 environment is created, [install PyPI packages](https://docs.cloud.google.com/composer/docs/composer-3/install-python-dependencies) to it:

  1. Copy PyPI package requirements from your Airflow 2 environment.
  2. Start the PyPI packages update operation and wait until the environment is updated.



Because Airflow 3 environments use a different set of preinstalled packages, you might encounter PyPI package conflicts during the update operation. For more information about troubleshooting PyPI package conflicts, see [Conflicts with preinstalled PyPI packages](https://docs.cloud.google.com/composer/docs/composer-3/troubleshooting-package-installation#conflicts).

### Step 4: Export variables, connections and pools from Airflow 2

If you don't have variables or connections, skip respective export and import commands.

You only need to transfer pools if you have custom pools other than `default_pool`. Otherwise, skip commands that export and import pools.

**Note:** Airflow CLI commands executed on the Airflow 2 environment operate on local files in the Airflow web server. To upload or download the files, use the `/data` directory in the environment's bucket of this environment. This directory synchronizes to the `/home/airflow/gcs/data/` directory in the Airflow web server. In the Airflow CLI commands, specify `/home/airflow/gcs/data/` in the `FILEPATH` parameter.

  1. Export variables from your Airflow 2 environment:
         
         gcloud composer environments run AIRFLOW_2_ENV \
             --location AIRFLOW_2_LOCATION \
             variables -- export /home/airflow/gcs/data/variables.json
         

Replace the following:

     * `AIRFLOW_2_ENV`: the name of your Airflow 2 environment.
     * `AIRFLOW_2_LOCATION`: the region where the Airflow 2 environment is located.
  2. Export connections from your Airflow 2 environment:
         
         gcloud composer environments run AIRFLOW_2_ENV \
             --location AIRFLOW_2_LOCATION \
             connections -- export /home/airflow/gcs/data/connections.json
         

Replace the following:

     * `AIRFLOW_2_ENV`: the name of your Airflow 2 environment.
     * `AIRFLOW_2_LOCATION`: the region where the Airflow 2 environment is located.
  3. Export pools from your Airflow 2 environment:
         
         gcloud composer environments run AIRFLOW_2_ENV \
             --location AIRFLOW_2_LOCATION \
             pools -- export /home/airflow/gcs/data/pools.json
         

Replace the following:

     * `AIRFLOW_2_ENV`: the name of your Airflow 2 environment.
     * `AIRFLOW_2_LOCATION`: the region where the Airflow 2 environment is located.
  4. Obtain the name of your Airflow 2 environment's bucket:
         
         gcloud composer environments describe AIRFLOW_2_ENV \
             --location AIRFLOW_2_LOCATION \
             --format="value(storageConfig.bucket)"
         

Replace the following:

     * `AIRFLOW_2_ENV`: the name of your Airflow 2 environment.
     * `AIRFLOW_2_LOCATION`: the region where the Airflow 2 environment is located.
  5. Download `variables.json`, `connections.json` and `pools.json` files from the `/data` directory of your Airflow 2 environment's bucket to a local directory:
         
         gcloud storage cp gs://AIRFLOW_2_BUCKET/data/variables.json ./variables.json
         gcloud storage cp gs://AIRFLOW_2_BUCKET/data/connections.json ./connections.json
         gcloud storage cp gs://AIRFLOW_2_BUCKET/data/pools.json ./pools.json
         

Replace the following:

     * `AIRFLOW_2_BUCKET`: name of your Airflow 2 environment's bucket, obtained in the previous step.



### Step 5: Import variables, connections and pools to Airflow 3

If you don't have variables or connections, skip respective export and import commands.

You only need to transfer pools if you have custom pools other than `default_pool`. Otherwise, skip commands that export and import pools.

  1. [Configure `airflowctl`](https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-cli#airflowctl) to run Airflow CLI commands for the Airflow 3 environment.

  2. Import variables, connections and pools to the Airflow 3 environment using `airflowctl`:
         
         airflowctl variables import ./variables.json
         airflowctl connections import ./connections.json
         airflowctl pools import ./pools.json
         

  3. Confirm that variables, connections and pools are imported to the Airflow 3 environment:
         
         airflowctl variables list
         airflowctl connections list
         airflowctl pools list
         

  4. Clean up JSON files:
         
         gcloud storage rm gs://AIRFLOW_2_BUCKET/data/variables.json
         gcloud storage rm gs://AIRFLOW_2_BUCKET/data/connections.json
         gcloud storage rm gs://AIRFLOW_2_BUCKET/data/pools.json
         rm ./variables.json
         rm ./connections.json
         rm ./pools.json
         

Replace the following:

     * `AIRFLOW_2_BUCKET`: name of your Airflow 2 environment's bucket.



### Step 6: Transfer other data from your Airflow 2 environment's bucket

In this step, you transfer remaining data from your Airflow 2 environment's bucket.

  1. Obtain the name of your Airflow 3 environment's bucket:
         
         gcloud composer environments describe AIRFLOW_3_ENV \
             --location AIRFLOW_3_LOCATION \
             --format="value(storageConfig.bucket)"
         

Replace the following:

     * `AIRFLOW_3_ENV`: the name of your Airflow 3 environment.
     * `AIRFLOW_3_LOCATION`: the region where the Airflow 3 environment is located.
  2. Export plugins from your Airflow 2 environment's bucket to the `/plugins` directory in your Airflow 3 environment's bucket:
         
         gcloud composer environments storage plugins export \
           --destination=AIRFLOW_3_BUCKET/plugins \
           --environment=AIRFLOW_2_ENV \
           --location=AIRFLOW_2_LOCATION
         

Replace the following:

     * `AIRFLOW_3_BUCKET`: name of your Airflow 3 environment's bucket, obtained in the previous step.
     * `AIRFLOW_2_ENV`: the name of your Airflow 2 environment.
     * `AIRFLOW_2_LOCATION`: the region where the Airflow 2 environment is located.
  3. Check that the `/plugins` directory is successfully imported:
         
         gcloud composer environments storage plugins list \
           --environment=AIRFLOW_3_ENV \
           --location=AIRFLOW_3_LOCATION
         

Replace the following:

     * `AIRFLOW_3_ENV`: the name of your Airflow 3 environment.
     * `AIRFLOW_3_LOCATION`: the region where the Airflow 3 environment is located.
  4. Export the `/data` directory from your Airflow 2 environment to the Airflow 3 environment:
         
         gcloud composer environments storage data export \
           --destination=AIRFLOW_3_BUCKET/data \
           --environment=AIRFLOW_2_ENV \
           --location=AIRFLOW_2_LOCATION
         

Replace the following:

     * `AIRFLOW_3_BUCKET`: name of your Airflow 3 environment's bucket, obtained in the previous step.
     * `AIRFLOW_2_ENV`: the name of your Airflow 2 environment.
     * `AIRFLOW_2_LOCATION`: the region where the Airflow 2 environment is located.
  5. Check that the `/data` folder is successfully imported:
         
         gcloud composer environments storage data list \
           --environment=AIRFLOW_3_ENV \
           --location=AIRFLOW_3_LOCATION
         

**Note:** if you have plugins that use Flask-AppBuilder views (`appbuilder_views`), Flask-AppBuilder menu items (`appbuilder_menu_items`), or Flask blueprints (`flask_blueprints`), consider **converting them to FastAPI apps**. If you don't convert them, they will still work in Airflow 3 because the FAB provider is preinstalled in Managed Airflow and has backwards compatibility layer for Airflow 3. However, we still recommend converting your plugins to the Airflow 3 Plugin interface: External Views (`external_views`), Fast API apps (`fastapi_apps`) and FastAPI middlewares (`fastapi_root_middlewares`).



### Step 7: Transfer users and roles

It's not possible to migrate users and roles because `airflowctl` doesn't support `users` and `roles` commands yet.

### Step 8: Make sure that your DAGs are ready for Airflow 3

  1. Adjust your Airflow DAGs to [make them compatible with Airflow 3](https://airflow.apache.org/docs/apache-airflow/stable/installation/upgrading_to_airflow3.html#step-3-dag-authors-check-your-airflow-dags-for-compatibility).

  2. Review custom written tasks for direct Airflow database access:

In Airflow 3, operators can't access the Airflow metadata database directly using database sessions. If you have custom operators, review your code to make sure that there are no direct database access calls.

You can use one of the alternative approaches to migrate away from direct Airflow database access in the tasks:

     * Access to the Airflow database through [exporting Airflow database contents to a Cloud SQL instance](https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-database#export-to-cloudsql).

     * Use the [Airflow Python client](https://airflow.apache.org/docs/apache-airflow/stable/installation/upgrading_to_airflow3.html#recommended-approach-use-airflow-python-client). The Python client provided by the community version of Airflow has APIs defined for the majority of tables, such as `DagRuns`, `TaskInstances`, `Variables`, `Connections`, `XComs`. The `apache-airflow-client` package is already preinstalled in the Managed Airflow Airflow 3 builds. 

     * Run `airflowctl` through `BashOperator` from a DAG. 

If querying the exported Airflow database isn't an option for your use case and both Airflow python client and `airflowctl` don't provide required functionality, consider requesting new API endpoints or Task SDK features in the community version of Airflow.

**Note:** The [workaround of using DbApiHook](https://airflow.apache.org/docs/apache-airflow/stable/installation/upgrading_to_airflow3.html#known-workaround-use-dbapihook-postgreshook-or-mysqlhook) described in the Airflow documentation can't be used to access the Airflow database in Managed Airflow because Airflow workers (tasks) can't communicate with the Airflow database.
  3. If you have `KubernetesExecutor` tasks, adjust its operator definitions by replacing `queue="kubernetes"` with `executor="KubernetesExecutor"`.

Example of a `KubernetesExecutor` task in Airflow 3:
         
         PythonOperator(
         task_id="airflow3_kubernetes_executor_task",
         dag=dag,
         python_callable=f,
         executor="KubernetesExecutor",
         )
         

  4. If you use the `AIRFLOW__WEBSERVER__BASE_URL` environment variable in the tasks code, replace it with the `[api]base_url` Airflow configuration option.

Example of obtaining this value in Airflow 3:
         
         from airflow.configuration import conf
         
         webserver_base_url = conf.get("api", "base_url")
         




### Step 9: Transfer DAGs to the Airflow 3 environment

**Warning:** This step explains how to avoid potential problems with **duplicate, missing, erroneous and otherwise invalid DAG runs** when transferring your DAGs between environments.

The following potential problems might happen when you transfer DAGs between environments:

  * If a DAG is enabled (not paused) in both environments, each environment runs its own copy of the DAG, as scheduled. This might lead to concurrent DAG runs for the same data and execution time.

  * Because of [DAG catchup](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dag-run.html#catchup), Airflow schedules extra DAG runs, beginning from the start date specified in your DAGs. This happens because the new Airflow instance does not take into account the history of DAG runs from the Airflow 2 environment. This might lead to a large number of DAG runs scheduled starting from the specified start date.




#### Prevent concurrent DAG runs

In your Airflow 3 environment, [override the `dags_are_paused_at_creation`](https://docs.cloud.google.com/composer/docs/composer-3/override-airflow-configurations) Airflow configuration option. After you make this change, all new DAGs are paused by default.

Section | Key | Value  
---|---|---  
`core` | `dags_are_paused_at_creation` | `True`  
**Note:** You can remove this override after you transfer all your DAGs to the Airflow 3 environment.

#### Prevent extra or missing DAG runs

Specify a new **static start date** in DAGs that you transfer to your Airflow 3 environment.

To avoid gaps and overlaps in [logical dates](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dag-run.html#data-interval), the first DAG run must happen in the Airflow 3 environment at the next occurrence of the schedule interval. To do so, set the new start date in your DAG to be before the date of the last run in the Airflow 2 environment.

As an example, if your DAG runs at 15:00, 17:00 and 21:00 every day in the Airflow 2 environment, the last DAG run happened at 15:00, and you plan to transfer the DAG at 15:15, then the start date for the Airflow 3 environment can be today at 14:45. After you enable the DAG in the Airflow 3 environment, Airflow schedules a DAG run for 17:00.

As another example, if your DAG runs at 00:00 every day in the Airflow 2 environment, the last DAG run happened at 00:00 on 26 March, 2026, and you plan to transfer the DAG at 13:00 on 26 March, 2026, then the start date for the Airflow 3 environment can be 23:45 on 25 March, 2026. After you enable the DAG in the Airflow 3 environment, Airflow schedules a DAG run for 00:00 on 27 March, 2026.

#### Transfer your DAGs one by one to the Airflow 3 environment

For each DAG, follow this procedure to transfer it:

  1. Make sure that the new start date in the DAG is set as described in the previous section.

  2. [Upload the updated DAG](https://docs.cloud.google.com/composer/docs/composer-3/manage-dags#add) to the Airflow 3 environment. This DAG is paused in the Airflow 3 environment because of the configuration override, so no DAG runs are scheduled yet.

  3. In [the Airflow web interface](https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-web-interface), go to **DAGs** and check for reported DAG syntax errors.

  4. At the time when you plan to transfer the DAG:

     1. Pause the DAG in your Airflow 2 environment.

     2. Un-pause the DAG in your Airflow 3 environment.

     3. Check that the new DAG run is scheduled at the correct time.

     4. Wait for the DAG run to happen in the Airflow 3 environment and check if the run is successful.

  5. Depending on whether the DAG run is successful:

     * If the DAG run is successful, you can proceed and use the DAG from your Airflow 3 environment. Eventually, consider deleting the Airflow 2 version of the DAG.

     * If the DAG run failed, attempt to [troubleshoot the DAG](https://docs.cloud.google.com/composer/docs/composer-3/troubleshooting-dags) until it successfully runs in Airflow 3.

If required, you can always fall back to the Airflow 2 version of the DAG:

       1. Pause the DAG in your Airflow 3 environment.

       2. Un-pause the DAG in your Airflow 3 environment. This schedules a new DAG run for the same date and time as the failed DAG run.

       3. When you are ready to continue with the Airflow 3 version of the DAG, adjust the start date, upload the new version of the DAG to your Airflow 3 environment, and repeat the procedure.




### Step 10: Monitor your Airflow 3 environment

After you transfer all DAGs and configuration to the Airflow 3 environment, monitor it for potential issues, failed DAG runs, and overall environment health. If the Airflow 3 environment runs without problems for a sufficient period of time, you can remove the Airflow 2 environment.

## What's next

  * [Troubleshooting DAGs](https://docs.cloud.google.com/composer/docs/composer-3/troubleshooting-dags)
  * [Troubleshooting environment creation](https://docs.cloud.google.com/composer/docs/composer-3/troubleshooting-environment-creation)
  * [Troubleshooting environment updates and upgrades](https://docs.cloud.google.com/composer/docs/composer-3/troubleshooting-updates-upgrades)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
