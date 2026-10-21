---
url: https://docs.cloud.google.com/composer/docs/composer-1/migrate-composer-2-af-2/
title: Migrate environments to Cloud Composer\u00a02 (from Airflow 2) \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:27:55.653264+00:00
---

# Migrate environments to Cloud Composer 2 (from Airflow 2)  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-1/migrate-composer-2-af-2/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 1 Guides ](https://docs.cloud.google.com/composer/docs/composer-1/composer-overview)



Send feedback 

#  Migrate environments to Cloud Composer 2 (from Airflow 2) Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Composer 3 | Cloud Composer 2 | **Cloud Composer 1**

This page explains how to transfer DAGs, data and configuration from your existing Cloud Composer 1, Airflow 2 environments to Cloud Composer 2, Airflow 2.

## Other migration guides

From | To | Method | Guide  
---|---|---|---  
Cloud Composer 2 | Cloud Composer 3 | Side-by-side, using the migration script | [Script migration guide](https://docs.cloud.google.com/composer/docs/composer-2/migrate-composer-3-script)  
Cloud Composer 2 | Cloud Composer 3 | Side-by-side, using snapshots | [Snapshots migration guide](https://docs.cloud.google.com/composer/docs/composer-2/migrate-composer-3)  
Cloud Composer 1, Airflow 2 | Cloud Composer 3 | Side-by-side, using snapshots | [Snapshots migration guide](https://docs.cloud.google.com/composer/docs/composer-1/migrate-composer-1-to-3)  
Cloud Composer 1, Airflow 2 | Cloud Composer 2 | Side-by-side, using snapshots | [Snapshots migration guide](https://docs.cloud.google.com/composer/docs/composer-1/migrate-composer-2-snapshots-af-2)  
Cloud Composer 1, Airflow 2 | Cloud Composer 2 | Side-by-side, manual transfer | This guide  
Cloud Composer 1, Airflow 1 | Cloud Composer 2, Airflow 2 | Side-by-side, using snapshots | [Snapshots migration guide](https://docs.cloud.google.com/composer/docs/composer-1/migrate-composer-2-snapshots-af-1)  
Cloud Composer 1, Airflow 1 | Cloud Composer 2, Airflow 2 | Side-by-side, manual transfer | [Manual migration guide](https://docs.cloud.google.com/composer/docs/composer-1/migrate-composer-2-af-1)  
Cloud Composer 1, Airflow 1 | Cloud Composer 1, Airflow 2 | Side-by-side, manual transfer | [Manual migration guide](https://docs.cloud.google.com/composer/docs/composer-1/migrate-environments-airflow-2)  
  
## Before you begin

  * Cloud Composer supports side-by-side migration from Cloud Composer 1 to Cloud Composer 2. It is not possible to upgrade from Cloud Composer 1 to Cloud Composer 2 in-place.
  * Check the [list of differences betweeen Cloud Composer 1 and Cloud Composer 2](https://docs.cloud.google.com/composer/docs/composer-versioning-overview).



## Step 1: Get the list of configuration overrides, custom PyPI packages, and environment variables

###  Console 

Get the list of your Cloud Composer 1 environment's configuration overrides, custom PyPI packages, and environment variables:

  1. Go to the **Environments** page in the Google Cloud console:

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. Select your Cloud Composer 1 environment.

  3. View environment variables on the **Environment variables** tab.

  4. View configuration overrides on the **Airflow configurations overrides** tabs.

  5. View custom PyPI packages on the **PyPI packages** tab.




###  gcloud 

To get the list of environment variables, run:
    
    
    gcloud composer environments describe \
        COMPOSER_1_ENV \
        --location COMPOSER_1_LOCATION \
        --format="value(config.softwareConfig.envVariables)"
    

To get the list of environment's Airflow configuration overrides, run:
    
    
    gcloud composer environments describe \
        COMPOSER_1_ENV \
        --location COMPOSER_1_LOCATION \
        --format="value(config.softwareConfig.airflowConfigOverrides)"
    

To get the list of custom PyPI packages, run:
    
    
    gcloud composer environments describe \
        COMPOSER_1_ENV \
        --location COMPOSER_1_LOCATION \
        --format="value(config.softwareConfig.pypiPackages)"
    

Replace:

  * `COMPOSER_1_ENV` with the name of your Cloud Composer 1 environment.
  * `COMPOSER_1_LOCATION` with the region where the Cloud Composer 1 environment is located.



###  Terraform 

Skip this step. Your Cloud Composer 1 environment's configuration already lists configuration overrides, custom PyPI packages, and environment variables for your environment.

## Step 2: Create a Cloud Composer 2 environment

In this step, create a Cloud Composer 2 environment. You can [start with an environment preset](https://docs.cloud.google.com/composer/docs/composer-2/optimize-environments#presets) that matches your expected resource demands, and later scale and optimize your environment further.

###  Console 

[Create a Cloud Composer 2 environment](https://docs.cloud.google.com/composer/docs/composer-2/create-environments) and [specify configuration overrides and environment variables](https://docs.cloud.google.com/composer/docs/composer-2/create-environments#overrides-env-vars).

As an alternative, you can [override](https://docs.cloud.google.com/composer/docs/composer-2/override-airflow-configurations) Airflow configurations and [environment variables](https://docs.cloud.google.com/composer/docs/composer-2/set-environment-variables) after you create an environment.

###  gcloud 

[Create a Cloud Composer 2 environment](https://docs.cloud.google.com/composer/docs/composer-2/create-environments) and [specify configuration overrides and environment variables](https://docs.cloud.google.com/composer/docs/composer-2/create-environments#overrides-env-vars).

As an alternative, you can [override](https://docs.cloud.google.com/composer/docs/composer-2/override-airflow-configurations) Airflow configurations and [environment variables](https://docs.cloud.google.com/composer/docs/composer-2/set-environment-variables) after you create an environment.

###  Terraform 

Create a Cloud Composer 2 environment based on the configuration of the Cloud Composer 1 environment:

  1. Copy your Cloud Composer 1 environment's configuration.
  2. Change the name of your environment.
  3. Use the `google-beta` provider:
         
         resource "google_composer_environment" "example_environment_composer_2" {
           provider = google-beta
           # ...
         }
         

  4. Specify a Cloud Composer 2 image in the `config.software_config` block:
         
         software_config {
           image_version = "composer-2.16.3-airflow-2.10.5"
           # ...
         }
         

  5. If not aleady, [specify configuration overrides and environment variables](https://docs.cloud.google.com/composer/docs/composer-2/create-environments#overrides-env-vars).

  6. Specify custom PyPI packages in the `config.software_config.pypi_packages` block:
         
         software_config {
         
           # ...
         
           pypi_packages = {
             numpy = ""
             scipy = ">=1.1.0"
           }
         
         }
         




## Step 3: Install PyPI packages to the Cloud Composer 2 environment

**Note:** If your environment does not use custom PyPI packages, then skip this step. Custom PyPI packages are the packages that you install in addition to preinstalled packages in your environment.

After your Cloud Composer 2 environment is created, install custom PyPI packages to it.

###  Console 

  1. Go to the **Environments** page in the Google Cloud console:

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. Select your Cloud Composer 2 environment.

  3. Go to the **PyPI packages** tab and click **Edit**.

  4. Copy PyPI package requirements from your Cloud Composer 1 environment. Click **Save** and wait until the environment updates.




###  gcloud 

  1. Create a `requirements.txt` file with the list of custom PyPI packages:
         
         numpy
           scipy>=1.1.0
         

  2. Update your environment and pass the `requirements.txt` file in the :to the `--update-pypi-packages-from-file` command:
         
         gcloud composer environments update COMPOSER_2_ENV \
           --location COMPOSER_2_LOCATION  \
           --update-pypi-packages-from-file requirements.txt
         

Replace:

     * `COMPOSER_2_ENV` with the name of your Cloud Composer 2 environment.
     * `COMPOSER_2_LOCATION` with the region where the Cloud Composer 2 environment is located.



###  Terraform 

Skip this step. You already installed custom PyPI packages when you created the environment.

## Step 4: Transfer variables and pools

**Note:** If your environment does not use Airflow variables or pools other than `default_pool`, skip this step.

Airflow supports exporting variables and pools to JSON files. You can then import these files to your Cloud Composer 2 environment.

Airflow CLI commands used in this step operate on local files in Airflow workers. To upload or download the files, use the `/data` folder in the Cloud Storage bucket of your environment. This folder syncs to the `/home/airflow/gcs/data/` directory in Airflow workers. In the Airflow CLI commands, specify `/home/airflow/gcs/data/` in the `FILEPATH` parameter.

###  gcloud 

  1. Export variables from your Cloud Composer 1 environment:
         
         gcloud composer environments run \
             COMPOSER_1_ENV \
             --location COMPOSER_1_LOCATION \
              variables export -- /home/airflow/gcs/data/variables.json
         

Replace:

     * `COMPOSER_1_ENV` with the name of your Cloud Composer 1 environment.
     * `COMPOSER_1_LOCATION` with the region where the Cloud Composer 1 environment is located.
  2. Export pools from your Cloud Composer 1 environment:
         
         gcloud composer environments run \
             COMPOSER_1_ENV \
             --location COMPOSER_1_LOCATION \
              pools export -- /home/airflow/gcs/data/pools.json
         

Replace:

     * `COMPOSER_1_ENV` with the name of your Cloud Composer 1 environment.
     * `COMPOSER_1_LOCATION` with the region where the Cloud Composer 1 environment is located.
  3. Get your Cloud Composer 2 environment's bucket URI.

     1. Run the following command:
            
            gcloud composer environments describe COMPOSER_2_ENV \
                --location COMPOSER_2_LOCATION \
                 --format="value(config.dagGcsPrefix)"
            

Replace:

        * `COMPOSER_2_ENV` with the name of your Cloud Composer 2 environment.
        * `COMPOSER_2_LOCATION` with the region where the environment is located.
     2. In the output, remove the `/dags` folder. The result is the URI of your Cloud Composer 2 environment's bucket.

For example, change `gs://us-central1-example-916807e1-bucket/dags` to `gs://us-central1-example-916807e1-bucket`.

  4. Transfer JSON files with variables and pools to your Cloud Composer 2 environment:
         
         gcloud composer environments storage data export \
             --destination=COMPOSER_2_BUCKET/data \
             --environment=COMPOSER_1_ENV \
             --location=COMPOSER_1_LOCATION \
             --source=variables.json
         
         
         gcloud composer environments storage data export \
             --destination=COMPOSER_2_BUCKET/data \
             --environment=COMPOSER_1_ENV \
             --location=COMPOSER_1_LOCATION \
             --source=pools.json
         

Replace:

     * `COMPOSER_2_BUCKET` with the URI of your Cloud Composer 2 environment bucket, obtained on the previous step.
     * `COMPOSER_1_ENV` with the name of your Cloud Composer 1 environment.
     * `COMPOSER_1_LOCATION` with the region where the Cloud Composer 1 environment is located.
  5. Import variables and pools to Cloud Composer 2:
         
         gcloud composer environments run \
             COMPOSER_2_ENV \
             --location COMPOSER_2_LOCATION \
             variables import \
             -- /home/airflow/gcs/data/variables.json
         
         
         gcloud composer environments run \
             COMPOSER_2_ENV \
             --location COMPOSER_2_LOCATION \
             pools import \
             -- /home/airflow/gcs/data/pools.json
         

  6. Check that variables and pools are imported:
         
         gcloud composer environments run \
             COMPOSER_2_ENV \
             --location COMPOSER_2_LOCATION \
             variables list
         
         
         gcloud composer environments run \
             COMPOSER_2_ENV \
             --location COMPOSER_2_LOCATION \
             pools list
         

  7. Remove JSON files from the buckets:
         
         gcloud composer environments storage data delete \
             variables.json \
             --environment=COMPOSER_2_ENV \
             --location=COMPOSER_2_LOCATION
         
         
         gcloud composer environments storage data delete \
             pools.json \
             --environment=COMPOSER_2_ENV \
             --location=COMPOSER_2_LOCATION
         
         
         gcloud composer environments storage data delete \
             variables.json \
             --environment=COMPOSER_1_ENV \
             --location=COMPOSER_1_LOCATION
         
         
         gcloud composer environments storage data delete \
             pools.json \
             --environment=COMPOSER_1_ENV \
             --location=COMPOSER_1_LOCATION
         




## Step 5: Transfer other data from your Cloud Composer 1 environment's bucket

Transfer plugins and other data from your Cloud Composer 1 environment's bucket.

###  gcloud 

  1. Transfer [plugins](https://docs.cloud.google.com/composer/docs/composer-1/install-plugins) to your Cloud Composer 2 environment. To do so, export plugins from your Cloud Composer 1 environment's bucket to the `/plugins` folder in your Cloud Composer 2 environment's bucket:
         
         gcloud composer environments storage plugins export \
             --destination=COMPOSER_2_BUCKET/plugins \
             --environment=COMPOSER_1_ENV \
             --location=COMPOSER_1_LOCATION
         

  2. Check that the `/plugins` folder is successfully imported:
         
         gcloud composer environments storage plugins list \
             --environment=COMPOSER_2_ENV \
             --location=COMPOSER_2_LOCATION
         

  3. Export the `/data` folder from your Cloud Composer 1 environment to the Airflow 2 environment:
         
         gcloud composer environments storage data export \
             --destination=COMPOSER_2_BUCKET/data \
             --environment=COMPOSER_1_ENV \
             --location=COMPOSER_1_LOCATION
         

  4. Check that the `/data` folder is successfully imported:
         
         gcloud composer environments storage data list \
             --environment=COMPOSER_2_ENV \
             --location=COMPOSER_2_LOCATION
         




## Step 6: Transfer connections

**Caution:** Cloud Composer environments have many default connections that are already configured for an environment. Do not transfer these connections because your Cloud Composer 2 environment already has them. If your environment uses only the default connections, skip this step.

This step explains how to transfer connections by creating them manually.

###  gcloud 

  1. To get a list of connections in your Cloud Composer 1 environment, run:
         
         gcloud composer environments run \
             COMPOSER_1_ENV \
             --location COMPOSER_1_LOCATION \
             connections list
         

  2. To create a new connection in your Cloud Composer 2 environment, run the [`connections` Airflow CLI command](https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html#connections) through `gcloud`. For example:
         
         gcloud composer environments run \
             COMPOSER_2_ENV \
             --location COMPOSER_2_LOCATION \
             connections add \
             -- --conn-host postgres.example.com \
             --conn-port 5432 \
             --conn-type postgres \
             --conn-login example_user \
             --conn-password example_password \
             --conn-description "Example connection" \
             example_connection
         




## Step 7: Transfer user accounts

This step explains how to transfer users by creating them manually.

**Note:** To view users, your account must [have the `Admin` role](https://docs.cloud.google.com/composer/docs/composer-1/airflow-rbac#registering-users).

###  Airflow UI 

  1. To view a list of users in your Cloud Composer 1 environment:

     1. [Open the Airflow web interface](https://docs.cloud.google.com/composer/docs/composer-1/access-airflow-web-interface) for your Cloud Composer 1 environment.

     2. Go to **Security** > **List Users**.

  2. To create a user in your Cloud Composer 2 environment:

     1. [Open the Airflow web interface](https://docs.cloud.google.com/composer/docs/composer-2/access-airflow-web-interface) for your Cloud Composer 2 environment.

     2. Go to **Security** > **List Users**.

     3. Click **Add a new record**.




###  gcloud 

  1. To view a list of users in your Cloud Composer 1 environment, run the `users list` Airflow CLI command through `gcloud`:
         
         gcloud composer environments run \
             COMPOSER_1_ENV \
             --location COMPOSER_1_LOCATION \
             users list
         

Replace:

     * `COMPOSER_1_ENV` with the name of your Cloud Composer 1 environment.
     * `COMPOSER_1_LOCATION` with the region where the Cloud Composer 1 environment is located.
  2. To create a new user account in your Cloud Composer 2 environment, run the [`users create` Airflow CLI command](https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html#create_repeat1) through `gcloud`. For example:
         
         gcloud composer environments run \
             COMPOSER_2_ENV \
             --location COMPOSER_2_LOCATION \
             users create \
             -- --username example_username \
             --firstname Example-Name \
             --lastname Example-Surname \
             --email example-user@example.com \
             --use-random-password \
             --role Op
         

Replace:

     * `COMPOSER_2_ENV` with the name of your Cloud Composer 2 environment.
     * `COMPOSER_2_LOCATION` with the region where the Cloud Composer 2 environment is located.
     * All user configuration parameters with their values from your Cloud Composer 1 environment, including user's role.



### Alternative way to transfer user accounts

As an alternative, you can use `users export` and `users import` Airflow CLI commands.

  1. Export user accounts to a file in your environment's bucket `/data` folder:
         
         gcloud composer environments run \
             COMPOSER_1_ENV \
             --location COMPOSER_1_LOCATION \
             users export -- /home/airflow/gcs/data/users.json
         

  2. Export this file to your Cloud Composer 2 environment's bucket:
         
         gcloud composer environments storage data export \
             --destination=COMPOSER_2_BUCKET/data \
             --environment=COMPOSER_1_ENV \
             --location=COMPOSER_1_LOCATION \
             --source=users.json
         

  3. Import user accounts from this file to your Cloud Composer 2 environment:
         
         gcloud composer environments run \
             COMPOSER_2_ENV \
             --location COMPOSER_2_LOCATION \
             users import \
             -- /home/airflow/gcs/data/users.json
         

  4. Delete the JSON files in both environments:
         
         gcloud composer environments storage data delete \
             --environment=COMPOSER_1_ENV \
             --location=COMPOSER_1_LOCATION  \
             users.json
         
         
         gcloud composer environments storage data delete \
             --environment=COMPOSER_2_ENV \
             --location=COMPOSER_2_LOCATION  \
             users.json
         




Replace:

  * `COMPOSER_1_ENV` with the name of your Cloud Composer 1 environment.
  * `COMPOSER_2_ENV` with the name of your Cloud Composer 2 environment.
  * `COMPOSER_1_LOCATION` with the region where the Cloud Composer 1 environment is located.
  * `COMPOSER_2_LOCATION` with the region where the Cloud Composer 2 environment is located.
  * `COMPOSER_2_BUCKET` with the URI of your Cloud Composer 2 environment bucket, obtained on the previous step.



## Step 8: Transfer DAGs to the Cloud Composer 2 environment

**Warning:** This step explains how to avoid potential problems with **duplicate, missing, erroneous and otherwise invalid DAG runs** when transferring your DAGs between environments.

The following potential problems might happen when you transfer DAGs between environments:

  * If a DAG is enabled (not paused) in both environments, each environment runs its own copy of the DAG, as scheduled. This might lead to duplicate DAG runs for the same data and execution time.

  * Because of [DAG catchup](https://airflow.apache.org/docs/apache-airflow/stable/dag-run.html#catchup), Airflow schedules extra DAG runs, beginning from the start date specified in your DAGs. This happens because the new Airflow instance does not take into account the history of DAG runs from the Cloud Composer 1 environment. This might lead to a large number of DAG runs scheduled starting from the specified start date.




### Prevent duplicate DAG runs

In your Cloud Composer 2 environment, In your Airflow 2 environment, add an [Airflow configuration option override](https://docs.cloud.google.com/composer/docs/composer-2/override-airflow-configurations) for the `dags_are_paused_at_creation` option. After you make this change, all new DAGs are paused by default.

Section | Key | Value  
---|---|---  
`core` | `dags_are_paused_at_creation` | `True`  
**Note:** You can remove this override after you transfer all your DAGs to the Cloud Composer 2 environment.

### Prevent extra or missing DAG runs

To avoid gaps and overlaps in [execution dates](https://airflow.apache.org/docs/apache-airflow/stable/concepts.html#execution-date) disable catch up in your Cloud Composer 2. In this way, after you upload DAGs to your Cloud Composer 2 environment, Airflow does not schedule DAG runs that were already run in the Cloud Composer 1 environment. Add an [Airflow configuration option override](https://docs.cloud.google.com/composer/docs/composer-2/override-airflow-configurations) for the `catchup_by_default` option:

Section | Key | Value  
---|---|---  
`scheduler` | `catchup_by_default` | `False`  
**Caution:** Do not remove this override. If you do so, your environment schedules catch up DAG runs. These DAG runs might overlap with the ones that were already executed in your Cloud Composer 1 environment.

### Transfer your DAGs to the Cloud Composer 2 environment

To transfer your DAGs to the Cloud Composer 2 environment:

  1. [Upload the DAG](https://docs.cloud.google.com/composer/docs/composer-2/manage-dags#adding) from the Cloud Composer 1 environment to the Cloud Composer 2 environment. Skip the `airflow_monitoring.py` DAG.

  2. The DAGs are paused in the Cloud Composer 2 environment because of the configuration override, so no DAG runs are scheduled.

  3. In [the Airflow web interface](https://docs.cloud.google.com/composer/docs/composer-2/access-airflow-web-interface), go to **DAGs** and check for reported DAG syntax errors.

  4. At the time when you plan to transfer the DAG:

     1. Pause the DAGs in your Cloud Composer 1 environment.

     2. Un-pause the DAGs in your Cloud Composer 2 environment.

     3. Check that the new DAG runs are scheduled at the correct time.

     4. Wait for the DAG runs to happen in the Cloud Composer 2 environment and check if they were successful. If a DAG run was successful, do not unpause it in the Cloud Composer 1 environment; if you do so, a DAG run for the same time and date happens in your Cloud Composer 1 environment.

  5. If a specific DAG runs fails, attempt to [troubleshoot the DAG](https://docs.cloud.google.com/composer/docs/composer-1/troubleshooting-dags) until it successfully runs in Cloud Composer 2.

If required, you can always fall back to the Cloud Composer 1 version of the DAG and execute DAG runs that failed in Cloud Composer 2 from your Cloud Composer 1 environment:

     1. Pause the DAG in your Cloud Composer 2 environment.

     2. Un-pause the DAG in your Cloud Composer 1 environment. This schedules catch up DAG runs for the time when the DAG was paused in Cloud Composer 1 environment.




## Step 9: Monitor your Cloud Composer 2 environment

After you transfer all DAGs and configuration to the Cloud Composer 2 environment, monitor it for potential issues, failed DAG runs, and overall environment health. If the Cloud Composer 2 environment runs without problems for a sufficient period of time, consider deleting the Cloud Composer 1 environment.

## What's next

  * [Troubleshooting DAGs](https://docs.cloud.google.com/composer/docs/composer-2/troubleshooting-dags)
  * [Troubleshooting environment creation](https://docs.cloud.google.com/composer/docs/composer-2/troubleshooting-environment-creation)
  * [Troubleshooting environment updates](https://docs.cloud.google.com/composer/docs/composer-2/troubleshooting-updates-upgrades)
  * [Using backport packages](https://docs.cloud.google.com/composer/docs/composer-1/backport-packages)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-09 UTC."],[],[]] 
