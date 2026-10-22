---
url: https://docs.cloud.google.com/composer/docs/composer-1/migrate-environments-airflow-2/
title: Migrate environments to Airflow 2 \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:07:50.767267+00:00
---

# Migrate environments to Airflow 2  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-1/migrate-environments-airflow-2/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 1 Guides ](https://docs.cloud.google.com/composer/docs/composer-1/composer-overview)



Send feedback 

#  Migrate environments to Airflow 2 Stay organized with collections  Save and categorize content based on your preferences. 

Managed Airflow (Gen 3) | Managed Airflow (Gen 2) | **Managed Airflow (Legacy Gen 1)**

This page explains how to transfer DAGs, data and configuration from your existing Airflow 1.10.* environments to environments with Airflow 2 and later Airflow versions.

**Note:** Managed Airflow supports manual transfers from Airflow 1.10.* environments to Airflow 2 environments. It is not possible to upgrade Airflow 1.10.* environments to Airflow 2. You can upgrade environments with Airflow 2 to later Airflow versions as usual.

## Other migration guides

From | To | Method | Guide  
---|---|---|---  
Managed Airflow (Gen 3), Airflow 2 | Managed Airflow (Gen 3), Airflow 3 | Side-by-side, manual transfer | [Manual migration guide](https://docs.cloud.google.com/composer/docs/composer-3/migrate-airflow-3)  
Managed Airflow (Gen 2) | Managed Airflow (Gen 3) | Side-by-side, using the migration script | [Script migration guide](https://docs.cloud.google.com/composer/docs/composer-2/migrate-composer-3-script)  
Managed Airflow (Gen 2) | Managed Airflow (Gen 3) | Side-by-side, using snapshots | [Snapshots migration guide](https://docs.cloud.google.com/composer/docs/composer-2/migrate-composer-3)  
Managed Airflow (Legacy Gen 1), Airflow 2 | Managed Airflow (Gen 3) | Side-by-side, using snapshots | [Snapshots migration guide](https://docs.cloud.google.com/composer/docs/composer-1/migrate-composer-1-to-3)  
Managed Airflow (Legacy Gen 1), Airflow 2 | Managed Airflow (Gen 2) | Side-by-side, using snapshots | [Snapshots migration guide](https://docs.cloud.google.com/composer/docs/composer-1/migrate-composer-2-snapshots-af-2)  
Managed Airflow (Legacy Gen 1), Airflow 2 | Managed Airflow (Gen 2) | Side-by-side, manual transfer | [Manual migration guide](https://docs.cloud.google.com/composer/docs/composer-1/migrate-composer-2-af-2)  
Managed Airflow (Legacy Gen 1), Airflow 1 | Managed Airflow (Gen 2), Airflow 2 | Side-by-side, using snapshots | [Snapshots migration guide](https://docs.cloud.google.com/composer/docs/composer-1/migrate-composer-2-snapshots-af-1)  
Managed Airflow (Legacy Gen 1), Airflow 1 | Managed Airflow (Gen 2), Airflow 2 | Side-by-side, manual transfer | [Manual migration guide](https://docs.cloud.google.com/composer/docs/composer-1/migrate-composer-2-af-1)  
Managed Airflow (Legacy Gen 1), Airflow 1 | Managed Airflow (Legacy Gen 1), Airflow 2 | Side-by-side, manual transfer | This guide  
  
## Side-by-side upgrades

Managed Airflow provides the [Managed Airflow database transfer script](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/composer/tools/composer_db_transfer.md) to migrate the metadata database, DAGs, data and plugins from Managed Airflow environments with Airflow 1.10.14 and Airflow 1.10.15 to existing Managed Airflow environments with Airflow 2.0.1 and later Airflow versions.

This is an alternate path to the one that is described in this guide. Some parts of this guide still apply when using the provided script. For example, you might want to check your DAGs for compatibility with Airflow 2 before migrating them, or to make sure that concurrent DAG runs do not happen, and there are no extra or missing DAG runs.

## Before you begin

Before you start using Managed Airflow environments with Airflow 2, consider changes that Airflow 2 brings to Managed Airflow environments.

### Multiple schedulers

You can use more than one Airflow scheduler in your environment. You can set the number of schedulers when you [create an environment](https://docs.cloud.google.com/composer/docs/enhow-to/managing/creating), or by [updating an existing environment](https://docs.cloud.google.com/composer/docs/composer-1/update-environments).

**Note:** You can [override](https://docs.cloud.google.com/composer/docs/composer-1/override-airflow-configurations) the Airflow 2 [scheduler configuration options](https://airflow.apache.org/docs/apache-airflow/stable/scheduler.html#scheduler-tuneables). Doing so configures the scheduler behavior, but does not enable multiple schedulers.

### Celery+Kubernetes Executor

Airflow 2 [Celery+Kubernetes Executor](https://airflow.apache.org/docs/apache-airflow/stable/executor/celery_kubernetes.html) is supported in Managed Airflow (Gen 3).

### Breaking changes

Airflow 2 introduces many major changes some of which are breaking:

  * Existing DAGs from Airflow 1.10.* are not guaranteed to work with Airflow 2. They need to be tested and possibly adjusted.
  * Operators, transfers, hooks migrated to providers packages. Import statements in DAGs must use [new provider packages](https://airflow.apache.org/docs/apache-airflow/stable/upgrading-to-2.html#step-4-import-operators-from-backport-providers). Old import statements might no longer work in Airflow 2.
  * Some Airflow 1.10.* configurations may no longer be supported because Airflow 2 [no longer supports certain configuration options](https://github.com/apache/airflow/blob/master/UPDATING.md#configuration-changes).
  * Some custom PyPI packages might be incompatible with the new version of Airflow or Python.
  * Airflow UI with Access Control is the default Airflow 2 UI. Airflow 2 does not support other Airflow UI types.
  * The experimental REST API is replaced by the [stable Airflow API](https://airflow.apache.org/docs/apache-airflow/stable/stable-rest-api-ref.html). The experimental REST API [is disabled by default](https://github.com/apache/airflow/blob/master/UPDATING.md#the-experimental-rest-api-is-disabled-by-default) in Airflow 2.
  * [Other major changes in Airflow 2.0.0](https://github.com/apache/airflow/blob/master/UPDATING.md#airflow-200)
  * [Other major changes in Airflow 2.0.1](https://github.com/apache/airflow/blob/master/UPDATING.md#airflow-201)



### Differences between environments with Airflow 2 and Airflow 1.10.*

Major differences between Managed Airflow environments with Airflow 1.10.* and environments with Airflow 2:

  * Environments with Airflow 2 [use Python 3.8](https://docs.cloud.google.com/composer/docs/composer-versions). This is a newer version than the one used in Airflow 1.10.* environments. Python 2, Python 3.6, Python 3.7 are not supported.
  * Airflow 2 uses a [different CLI format](https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html). Managed Airflow supports the new format in environments with Airflow 2 through the [`gcloud composer environments run`](https://docs.cloud.google.com/sdk/gcloud/reference/composer/environments/run) command.
  * Preinstalled PyPI packages are different in Airflow 2 environments. For a list of preinstalled PyPI packages, see [Managed Airflow version list](https://docs.cloud.google.com/composer/docs/composer-versions).
  * [DAG serialization](https://docs.cloud.google.com/composer/docs/composer-1/dag-serialization) is always enabled in Airflow 2. As a result, [asynchronous DAG loading](https://docs.cloud.google.com/composer/docs/composer-1/access-airflow-web-interface#asynchronous-load) is no longer needed, and it is not supported in Airflow 2. As a result of it, configuring `[core]store_serialized_dags` and `[core]store_dag_code` parameters is not supported for Airflow 2, and attempts to setting them will be reported as errors.
  * Airflow web server plugins are not supported. This doesn't impact scheduler or worker plugins, including Airflow operators and sensors.
  * In Airflow 2 environments, the [default Airflow user role](https://docs.cloud.google.com/composer/docs/composer-1/airflow-rbac) is `Op`. For environments with Airflow 1.10.*, the default role is `Admin`.



## Step 1: Check compatibility with Airflow 2

To check for potential conflicts with Airflow 2, consult the Upgrading to Airflow 2.0+ guide, in the section about [upgrading DAGs](https://airflow.apache.org/docs/apache-airflow/stable/upgrading-to-2.html#step-5-upgrade-airflow-dags).

One common issue that you might encounter is related to incompatible import paths. For more information about solving this compatibility issue, in the Upgrading to Airflow 2.0+ guide, see the [section about backport providers](https://airflow.apache.org/docs/apache-airflow/stable/upgrading-to-2.html#step-4-import-operators-from-backport-providers).

## Step 2: Create an Airflow 2 environment, transfer configuration overrides and environment variables

Create an Airflow 2 environment and transfer configuration overrides and environment variables:

  1. Follow the steps for [creating an environment](https://docs.cloud.google.com/composer/docs/enhow-to/managing/creating). Before you create an environment, also specify configuration overrides and environment variables, as explained further.

  2. When you select an image, choose an [image with Airflow 2](https://docs.cloud.google.com/composer/docs/composer-versions).

  3. Manually transfer configuration parameters from your Airflow 1.10.* environment to the new Airflow 2 environment.

### Console

     1. When you create an environment, expand the **Networking, Airflow config overrides, and additional features** section.

     2. Under **Airflow configuration overrides** , click **Add Airflow configuration override**.

     3. Copy all configuration overrides from your Airflow 1.10.* environment.

Some configuration options use a different name and section in Airflow 2. For more information, see [Configuration changes](https://github.com/apache/airflow/blob/master/UPDATING.md#configuration-changes).

     4. Under **Environment variables** , click **Add environment variable**

     5. Copy all environment variables from your Airflow 1.10.* environment.

     6. Click **Create** to create an environment.




## Step 3: Install PyPI packages to the Airflow 2 environment

After your Airflow 2 environment is created, install PyPI packages to it:

### Console

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. Select your Airflow 2 environment.

  3. Go to the **PyPI packages** tab and click **Edit**.

  4. Copy PyPI package requirements from your Airflow 1.10.* environment. Click **Save** and wait until the environment updates.

Because Airflow 2 environments use a [different set of preinstalled packages](https://docs.cloud.google.com/composer/docs/composer-versions) and a different Python version, you might encounter PyPI package conflicts that are difficult to resolve.




## Step 4: Transfer variables and pools to Airflow 2

Airflow 1.10.* supports exporting variables and pools to JSON files. You can then import these files to your Airflow 2 environment.

You only need to transfer pools if you have custom pools other than `default_pool`. Otherwise, skip commands that export and import pools.

**Note:** Airflow CLI commands used on this step operate on local files in Airflow workers. To upload or download the files, use the `/data` folder in the Cloud Storage bucket of your environment. This folder syncs to the `/home/airflow/gcs/data/` directory in Airflow workers. In the Airflow CLI commands, specify `/home/airflow/gcs/data/` in the `FILEPATH` parameter.

### gcloud

  1. Export variables from your Airflow 1.10.* environment:
         
         gcloud composer environments run AIRFLOW_1_ENV \
             --location AIRFLOW_1_LOCATION \
              variables -- -e /home/airflow/gcs/data/variables.json
         

Replace:

     * `AIRFLOW_1_ENV` with the name of your Airflow 1.10.* environment.
     * `AIRFLOW_1_LOCATION` with the region where the environment is located.
  2. Export pools from your Airflow 1.10.* environment:
         
         gcloud composer environments run AIRFLOW_1_ENV \
             --location AIRFLOW_1_LOCATION \
              pool -- -e /home/airflow/gcs/data/pools.json
         

  3. Get your Airflow 2 environment bucket URI.

     1. Run the following command:
            
            gcloud composer environments describe AIRFLOW_2_ENV \
                --location AIRFLOW_2_LOCATION \
                 --format="value(config.dagGcsPrefix)"
            

Replace:

        * `AIRFLOW_2_ENV` with the name of your Airflow 2 environment.
        * `AIRFLOW_2_LOCATION` with the region where the environment is located.
     2. In the output, remove the `/dags` folder. The result is the URI of your Airflow 2 environment bucket.

For example, change `gs://us-central1-example-916807e1-bucket/dags` to `gs://us-central1-example-916807e1-bucket`.

  4. Transfer JSON files with variables and pools to your Airflow 2 environment:
         
         gcloud composer environments storage data export \
             --destination=AIRFLOW_2_BUCKET/data \
             --environment=AIRFLOW_1_ENV \
             --location=AIRFLOW_1_LOCATION \
             --source=variables.json
         
         gcloud composer environments storage data export \
             --destination=AIRFLOW_2_BUCKET/data \
             --environment=AIRFLOW_1_ENV \
             --location=AIRFLOW_1_LOCATION \
             --source=pools.json
         

Replace `AIRFLOW_2_BUCKET` with the URI of your Airflow 2 environment bucket, obtained on the previous step.

  5. Import variables and pools to Airflow 2:
         
         gcloud composer environments run \
             AIRFLOW_2_ENV \
             --location AIRFLOW_2_LOCATION \
             variables import \
             -- /home/airflow/gcs/data/variables.json
         
         gcloud composer environments run \
             AIRFLOW_2_ENV \
             --location AIRFLOW_2_LOCATION \
             pools import \
             -- /home/airflow/gcs/data/pools.json
         

  6. Check that variables and pools are imported:
         
         gcloud composer environments run \
             AIRFLOW_2_ENV \
             --location AIRFLOW_2_LOCATION \
             variables list
         
         gcloud composer environments run \
             AIRFLOW_2_ENV \
             --location AIRFLOW_2_LOCATION \
             pools list
         

  7. Remove JSON files from the buckets:
         
         gcloud composer environments storage data delete \
             variables.json \
             --environment=AIRFLOW_2_ENV \
             --location=AIRFLOW_2_LOCATION
         
         gcloud composer environments storage data delete \
             pools.json \
             --environment=AIRFLOW_2_ENV \
             --location=AIRFLOW_2_LOCATION
         
         gcloud composer environments storage data delete \
             variables.json \
             --environment=AIRFLOW_1_ENV \
             --location=AIRFLOW_1_LOCATION
         
         gcloud composer environments storage data delete \
             pools.json \
             --environment=AIRFLOW_1_ENV \
             --location=AIRFLOW_1_LOCATION
         




## Step 5: Transfer other data from your Airflow 1.10.* environment bucket

### gcloud

  1. Transfer [plugins](https://docs.cloud.google.com/composer/docs/composer-1/install-plugins) to your Airflow 2 environment. To do so, export plugins from your Airflow 1.10.* environment bucket to the `/plugins` folder in your Airflow 2 environment bucket:
         
         gcloud composer environments storage plugins export \
             --destination=AIRFLOW_2_BUCKET/plugins \
             --environment=AIRFLOW_1_ENV \
             --location=AIRFLOW_1_LOCATION
         

  2. Check that the `/plugins` folder is successfully imported:
         
         gcloud composer environments storage plugins list \
             --environment=AIRFLOW_2_ENV \
             --location=AIRFLOW_2_LOCATION
         

  3. Export the `/data` folder from your Airflow 1.10.* environment to the Airflow 2 environment:
         
         gcloud composer environments storage data export \
                 --destination=AIRFLOW_2_BUCKET/data \
                 --environment=AIRFLOW_1_ENV \
                 --location=AIRFLOW_1_LOCATION
         

  4. Check that the `/data` folder is successfully imported:
         
         gcloud composer environments storage data list \
             --environment=AIRFLOW_2_ENV \
             --location=AIRFLOW_2_LOCATION
         




## Step 6: Transfer connections and users

Airflow 1.10.* does not support exporting users and connections. To transfer users and connections, manually create new user accounts and connections in your Airflow 2 environment.

**Important:** Managed Airflow environments have many default connections. Do not transfer these connections because Airflow 2 environments already have them.

### gcloud

  1. To get a list of connections in your Airflow 1.10.* environment, run:
         
         gcloud composer environments run AIRFLOW_1_ENV \
             --location AIRFLOW_1_LOCATION \
              connections -- --list
         

  2. To create a new connection in your Airflow 2 environment, run the [`connections` Airflow CLI command](https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html#connections) through gcloud. For example:
         
         gcloud composer environments run \
             AIRFLOW_2_ENV \
             --location AIRFLOW_2_LOCATION \
             connections add \
             -- --conn-host postgres.example.com \
             --conn-port 5432 \
             --conn-type postgres \
             --conn-login example_user \
             --conn-password example_password \
             --conn-description "Example connection" \
             example_connection
         

  3. To view a list of users in your Airflow 1.10.* environment:

     1. [Open the Airflow web interface](https://docs.cloud.google.com/composer/docs/composer-1/access-airflow-web-interface) for your Airflow 1.10.* environment.

     2. Go to **Admin** > **Users**.

  4. To create a new user account in your Airflow 2 environment, run the [`users create` Airflow CLI command](https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html#create_repeat1) through gcloud. For example:
         
         gcloud composer environments run \
             AIRFLOW_2_ENV \
             --location AIRFLOW_2_LOCATION \
             users create \
             -- --username example_username \
             --firstname Example-Name \
             --lastname Example-Surname \
             --email example-user@example.com \
             --use-random-password \
             --role Admin
         




## Step 7: Make sure that your DAGs are ready for Airflow 2

Before transferring DAGs to your Airflow 2 environment, make sure that:

  1. Your DAGs run successfully and there are no remaining compatibility issues.

  2. Your DAGs use [correct import statements](https://airflow.apache.org/docs/apache-airflow/stable/upgrading-to-2.html#step-4-import-operators-from-backport-providers).

For example, the new import statement for `BigQueryCreateDataTransferOperator` can look like this:
         
         from airflow.providers.google.cloud.operators.bigquery_dts \
             import BigQueryCreateDataTransferOperator
         

  3. Your DAGs are [upgraded for Airflow 2](https://airflow.apache.org/docs/apache-airflow/stable/upgrading-to-2.html#step-5-upgrade-airflow-dags). This change is compatible with Airflow 1.10.14 and later versions.




## Step 8: Transfer DAGs to the Airflow 2 environment

**Warning:** This step explains how to avoid **potential problems** with duplicate, missing, erroneous and otherwise invalid DAG runs when transferring your DAGs between environments.

The following potential problems might happen when you transfer DAGs between environments:

  * If a DAG is enabled (not paused) in both environments, each environment runs its own copy of the DAG, as scheduled. This might lead to concurrent DAG runs for the same data and execution time.

  * Because of [DAG catchup](https://airflow.apache.org/docs/apache-airflow/stable/dag-run.html#catchup), Airflow schedules extra DAG runs, beginning from the start date specified in your DAGs. This happens because the new Airflow instance does not take into account the history of DAG runs from the 1.10.* environment. This might lead to a large number of DAG runs scheduled starting from the specified start date.




### Prevent concurrent DAG runs

In your Airflow 2 environment, [override the `dags_are_paused_at_creation`](https://docs.cloud.google.com/composer/docs/composer-1/override-airflow-configurations) Airflow configuration option. After you make this change, all new DAGs are paused by default.

Section | Key | Value  
---|---|---  
`core` | `dags_are_paused_at_creation` | `True`  
**Note:** You can remove this override after you transfer all your DAGs to the Airflow 2 environment.

### Prevent extra or missing DAG runs

Specify a new **static start date** in DAGs that you transfer to your Airflow 2 environment.

To avoid gaps and overlaps in [execution dates](https://airflow.apache.org/docs/apache-airflow/stable/concepts.html#execution-date), the first DAG run should happen in the Airflow 2 environment at the next occurrence of the schedule interval. To do so, set the new start date in your DAG to be before the date of the last run in the Airflow 1.10.* environment.

As an example, if your DAG runs at 15:00, 17:00 and 21:00 every day in the Airflow 1.10.* environment, the last DAG run happened at 15:00, and you plan to transfer the DAG at 15:15, then the start date for the Airflow 2 environment can be today at 14:45. After you enable the DAG in the Airflow 2 environment, Airflow schedules a DAG run for 17:00.

As another example, if your DAG runs at 00:00 every day in the Airflow 1.10.* environment, the last DAG run happened at 00:00 on 26 April, 2021, and you plan to transfer the DAG at 13:00 on 26 April, 2021, then the start date for the Airflow 2 environment can be 23:45 on 25 April, 2021. After you enable the DAG in the Airflow 2 environment, Airflow schedules a DAG run for 00:00 on 27 April, 2021.

### Transfer your DAGs one by one to the Airflow 2 environment

For each DAG, follow this procedure to transfer it:

  1. Make sure that the new start date in the DAG is set as described in the previous section.

  2. [Upload the updated DAG](https://docs.cloud.google.com/composer/docs/composer-1/manage-dags#add) to the Airflow 2 environment. This DAG is paused in the Airflow 2 environment because of the configuration override, so no DAG runs are scheduled yet.

  3. In [the Airflow web interface](https://docs.cloud.google.com/composer/docs/composer-1/access-airflow-web-interface), go to **DAGs** and check for reported DAG syntax errors.

**Note:** The Airflow web interface does not correctly display DAGs located in zip files. [This behavior is a known limitation in Airflow](https://github.com/apache/airflow/issues/14412).
  4. At the time when you plan to transfer the DAG:

     1. Pause the DAG in your Airflow 1.10.* environment.

     2. Un-pause the DAG in your Airflow 2 environment.

     3. Check that the new DAG run is scheduled at the correct time.

     4. Wait for the DAG run to happen in the Airflow 2 environment and check if the run is successful.

  5. Depending on whether the DAG run is successful:

     * If the DAG run is successful, you can proceed and use the DAG from your Airflow 2 environment. Eventually, consider deleting the Airflow 1.10.* version of the DAG.

     * If the DAG run failed, attempt to [troubleshoot the DAG](https://docs.cloud.google.com/composer/docs/composer-1/troubleshooting-dags) until it successfully runs in Airflow 2.

If required, you can always fall back to the Airflow 1.10.* version of the DAG:

       1. Pause the DAG in your Airflow 2 environment.

       2. Un-pause the DAG in your Airflow 1.10.* environment. This schedules a new DAG run for the same date and time as the failed DAG run.

       3. When you are ready to continue with the Airflow 2 version of the DAG, adjust the start date, upload the new version of the DAG to your Airflow 2 environment, and repeat the procedure.




## Step 9: Monitor your Airflow 2 environment

After you transfer all DAGs and configuration to the Airflow 2 environment, monitor it for potential issues, failed DAG runs, and overall environment health. If the Airflow 2 environment runs without problems for a sufficient period of time, you can remove the Airflow 1.10.* environment.

## What's next

  * [Troubleshooting DAGs](https://docs.cloud.google.com/composer/docs/composer-1/troubleshooting-dags)
  * [Troubleshooting environment creation](https://docs.cloud.google.com/composer/docs/composer-1/troubleshooting-environment-creation)
  * [Troubleshooting environment updates and upgrades](https://docs.cloud.google.com/composer/docs/composer-1/troubleshooting-updates-upgrades)
  * [Using backport packages](https://docs.cloud.google.com/composer/docs/composer-1/backport-packages)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
