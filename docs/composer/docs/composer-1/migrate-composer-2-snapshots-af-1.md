---
url: https://docs.cloud.google.com/composer/docs/composer-1/migrate-composer-2-snapshots-af-1/
title: Migrate environments to Managed Airflow\u00a0(Gen\u00a02) (from Airflow 1) using snapshots \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:26:49.035977+00:00
---

# Migrate environments to Managed Airflow (Gen 2) (from Airflow 1) using snapshots  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-1/migrate-composer-2-snapshots-af-1/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 1 Guides ](https://docs.cloud.google.com/composer/docs/composer-1/composer-overview)



Send feedback 

#  Migrate environments to Managed Airflow (Gen 2) (from Airflow 1) using snapshots Stay organized with collections  Save and categorize content based on your preferences. 

Managed Airflow (Gen 3) | Managed Airflow (Gen 2) | **Managed Airflow (Legacy Gen 1)**

This page explains how to transfer DAGs, data and configuration from your existing Managed Airflow (Legacy Gen 1), Airflow 1 environments to Managed Airflow (Gen 2), Airflow 2.

This migration guide uses the [Snapshots](https://docs.cloud.google.com/composer/docs/composer-1/save-load-snapshots) feature.

## Other migration guides

From | To | Method | Guide  
---|---|---|---  
Managed Airflow (Gen 3), Airflow 2 | Managed Airflow (Gen 3), Airflow 3 | Side-by-side, manual transfer | [Manual migration guide](https://docs.cloud.google.com/composer/docs/composer-3/migrate-airflow-3)  
Managed Airflow (Gen 2) | Managed Airflow (Gen 3) | Side-by-side, using the migration script | [Script migration guide](https://docs.cloud.google.com/composer/docs/composer-2/migrate-composer-3-script)  
Managed Airflow (Gen 2) | Managed Airflow (Gen 3) | Side-by-side, using snapshots | [Snapshots migration guide](https://docs.cloud.google.com/composer/docs/composer-2/migrate-composer-3)  
Managed Airflow (Legacy Gen 1), Airflow 2 | Managed Airflow (Gen 3) | Side-by-side, using snapshots | [Snapshots migration guide](https://docs.cloud.google.com/composer/docs/composer-1/migrate-composer-1-to-3)  
Managed Airflow (Legacy Gen 1), Airflow 2 | Managed Airflow (Gen 2) | Side-by-side, using snapshots | [Snapshots migration guide](https://docs.cloud.google.com/composer/docs/composer-1/migrate-composer-2-snapshots-af-2)  
Managed Airflow (Legacy Gen 1), Airflow 2 | Managed Airflow (Gen 2) | Side-by-side, manual transfer | [Manual migration guide](https://docs.cloud.google.com/composer/docs/composer-1/migrate-composer-2-af-2)  
Managed Airflow (Legacy Gen 1), Airflow 1 | Managed Airflow (Gen 2), Airflow 2 | Side-by-side, using snapshots | This guide  
Managed Airflow (Legacy Gen 1), Airflow 1 | Managed Airflow (Gen 2), Airflow 2 | Side-by-side, manual transfer | [Manual migration guide](https://docs.cloud.google.com/composer/docs/composer-1/migrate-composer-2-af-1)  
Managed Airflow (Legacy Gen 1), Airflow 1 | Managed Airflow (Legacy Gen 1), Airflow 2 | Side-by-side, manual transfer | [Manual migration guide](https://docs.cloud.google.com/composer/docs/composer-1/migrate-environments-airflow-2)  
  
## Before you begin

  * Snapshots are supported in Managed Airflow (Gen 2) version 2.0.9 and later. Managed Airflow (Legacy Gen 1) supports saving environment snapshots in 1.18.5.

  * Managed Airflow supports side-by-side migration from Managed Airflow (Legacy Gen 1) to Managed Airflow (Gen 2). It is not possible to upgrade from Managed Airflow (Legacy Gen 1) to Managed Airflow (Gen 2) in-place.

  * Check the [list of differences between Managed Airflow (Legacy Gen 1) and Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-versioning-overview).

  * The maximum size of the Airflow database that supports snapshots is 20 GB. If your environment's database takes more than 20 GB, [reduce the size of the Airflow database](https://docs.cloud.google.com/composer/docs/composer-1/cleanup-airflow-database).

  * The total number of objects in the `/dags`, `/plugins` and `/data` folders in the environment's bucket must be less than 100,000 to create snapshots.

  * If you use the XCom mechanism to transfer files, make sure that you [use it according to Airflow's guidelines](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/xcoms.html#object-storage-xcom-backend). Transferring big files or a large number of files using XCom impacts Airflow database's performance and can lead to failures when loading snapshots or upgrading your environment. Consider using alternatives such as Cloud Storage to transfer large volumes of data.



  * Because Managed Airflow (Gen 2) uses Airflow 2, the migration includes switching your DAGs and environment configuration to Airflow 2. Check the [migration guide from Airflow 1 to Airflow 2](https://docs.cloud.google.com/composer/docs/composer-1/migrate-environments-airflow-2) for information about the breaking changes between Airflow 1 and Airflow 2 in Managed Airflow.

  * In this guide, you combine migration to Airflow 2 and migration to Managed Airflow (Gen 2) in one migration procedure. In this way, you do not need to migrate to a Managed Airflow (Legacy Gen 1) environment with Airflow 2 before migrating to Managed Airflow (Gen 2).




## Step 1: Upgrade to Airflow 1.10.15

If your environment uses an Airflow version earlier than 1.10.15, [upgrade your environment](https://docs.cloud.google.com/composer/docs/composer-1/upgrade-environments) to a [Managed Airflow version](https://docs.cloud.google.com/composer/docs/composer-versions) that uses Airflow 1.10.15 and supports snapshots. 

## Step 2: Check compatibility with Airflow 2

To check for potential conflicts with Airflow 2, consult the Upgrading to Airflow 2.0+ guide, in the section about [upgrading DAGs](https://airflow.apache.org/docs/apache-airflow/stable/upgrading-to-2.html#step-5-upgrade-airflow-dags).

One common issue that you might encounter is related to incompatible import paths. For more information about solving this compatibility issue, in the Upgrading to Airflow 2.0+ guide, see the [section about backport providers](https://airflow.apache.org/docs/apache-airflow/stable/upgrading-to-2.html#step-4-import-operators-from-backport-providers).

## Step 3: Make sure that your DAGs are ready for Airflow 2

Before transferring DAGs to your Managed Airflow (Gen 2) environment, make sure that:

  1. Your DAGs run successfully and there are no remaining compatibility issues.

  2. Your DAGs use [correct import statements](https://airflow.apache.org/docs/apache-airflow/stable/upgrading-to-2.html#step-4-import-operators-from-backport-providers).

For example, the new import statement for `BigQueryCreateDataTransferOperator` can look like this:
         
         from airflow.providers.google.cloud.operators.bigquery_dts \
             import BigQueryCreateDataTransferOperator
         

  3. Your DAGs are [upgraded for Airflow 2](https://airflow.apache.org/docs/apache-airflow/stable/upgrading-to-2.html#step-5-upgrade-airflow-dags). This change is compatible with Airflow 1.10.14 and later versions.




## Step 4: Pause DAGs in your Managed Airflow (Legacy Gen 1) environment

**Warning:** If a DAG is enabled (not paused) in both environments, each environment runs its own copy of the DAG, as scheduled. This might lead to duplicate DAG runs for the same data and execution time.

To avoid duplicate DAG runs, pause all DAGs in your Managed Airflow (Legacy Gen 1) environment before saving its snapshot.

You can use any of the following options:

  * In [the Airflow web interface](https://docs.cloud.google.com/composer/docs/composer-1/access-airflow-web-interface), go to **DAGs** and pause all DAGs manually.

  * Use the [composer_dags](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/main/composer/tools/composer_dags.py) script to pause all DAGs:
        
        python3 composer_dags.py --environment COMPOSER_1_ENV \
          --project PROJECT_ID \
          --location COMPOSER_1_LOCATION \
          --operation pause
        

Replace:

    * `COMPOSER_1_ENV` with the name of your Managed Airflow (Legacy Gen 1) environment.
    * `PROJECT_ID` with the [Project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).
    * `COMPOSER_1_LOCATION` with the region where the environment is located.



## Step 5: Save the snapshot of your Managed Airflow (Legacy Gen 1) environment

**Caution:** If any changes or DAG runs happen in your Managed Airflow (Legacy Gen 1) environment after you save its snapshot, information about these changes is not transferred when you load the snapshot later.

###  Console 

Create a snapshot of your environment:

  1. In Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your Managed Airflow (Legacy Gen 1) environment. The **Environment details** page opens.

  3. Click **Create snapshot**.

  4. In the **Create snapshot** dialog, click **Submit**. In this guide, you save the snapshot in the Managed Airflow (Legacy Gen 1) environment's bucket, but you can select a different location, if you want to.

  5. Wait until Managed Airflow creates the snapshot.




###  gcloud 

  1. Get your Managed Airflow (Legacy Gen 1) environment's bucket URI: 

     1. Run the following command:
            
            gcloud composer environments describe COMPOSER_1_ENV \
                --location COMPOSER_1_LOCATION \
                 --format="value(config.dagGcsPrefix)"
            

Replace:

        * `COMPOSER_1_ENV` with the name of your Managed Airflow (Legacy Gen 1) environment.
        * `COMPOSER_1_LOCATION` with the region where the environment is located.
     2. In the output, remove the `/dags` folder. The result is the URI of your Managed Airflow (Legacy Gen 1) environment's bucket.

For example, change `gs://us-central1-example-916807e1-bucket/dags` to `gs://us-central1-example-916807e1-bucket`.

  2. Create a snapshot of your Managed Airflow (Legacy Gen 1) environment:
         
         gcloud composer environments snapshots save \
           COMPOSER_1_ENV \
           --location COMPOSER_1_LOCATION \
           --snapshot-location "COMPOSER_1_SNAPSHOTS_FOLDER"
         

Replace:

     * `COMPOSER_1_ENV` with the name of your Managed Airflow (Legacy Gen 1) environment.
     * `COMPOSER_1_LOCATION` with the region where the Managed Airflow (Legacy Gen 1) environment is located.
     * `COMPOSER_1_SNAPSHOTS_FOLDER` with the URI of your Managed Airflow (Legacy Gen 1) environment's bucket. In this guide, you save the snapshot in the Managed Airflow (Legacy Gen 1) environment's bucket, but you can select a different location, if you want to. If you specify a custom location, the [service accounts of both environments](https://docs.cloud.google.com/composer/docs/composer-1/access-control#service-account) must have read and write permissions for the specified location.



## Step 6: Create a Managed Airflow (Gen 2) environment

[Create a Managed Airflow (Gen 2) environment](https://docs.cloud.google.com/composer/docs/composer-2/create-environments). You can [start with an environment preset](https://docs.cloud.google.com/composer/docs/composer-2/optimize-environments#presets) that matches your expected resource demands, and later scale and optimize your environment further.

You do not need to specify configuration overrides and environment variables, since you replace them later when you load the snapshot of your Managed Airflow (Legacy Gen 1) environment.

**Note:** Managed Airflow loads configuration overrides, environment variables, and PyPI packages from your Managed Airflow (Legacy Gen 1) environment to Managed Airflow (Gen 2) without changing or adjusting them for compatibility. If custom PyPI packages cause dependency conflicts, you can skip their installation when you load the snapshot.

Some configuration options from Airflow 1 use a different name and section in Airflow 2. For more information, see [Configuration changes](https://github.com/apache/airflow/blob/master/UPDATING.md#configuration-changes).

## Step 7: Load the snapshot to your Managed Airflow (Gen 2) environment

###  Console 

To load the snapshot to your Managed Airflow (Gen 2) environment:

  1. In Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your Managed Airflow (Gen 2) environment. The **Environment details** page opens.

  3. Click **Load snapshot**.

  4. In the **Load snapshot** dialog, click **Browse**.

  5. Select the folder with the snapshot. If you use the default location for this guide, this folder is located in your Managed Airflow (Legacy Gen 1) environment bucket in the `/snapshots` folder, and its name is the timestamp of the snapshot save operation. For example, `us-central1-example-916807e1-bucket/snapshots_example-project_us-central1_example-environment/2022-01-05T18-59-00`.

  6. Click **Load** and wait until Managed Airflow loads the snapshot.




###  gcloud 

Load the snapshot of your Managed Airflow (Legacy Gen 1) environment to your Managed Airflow (Gen 2) environment:
    
    
    gcloud composer environments snapshots load \
      COMPOSER_2_ENV \
      --location COMPOSER_2_LOCATION \
      --snapshot-path "SNAPSHOT_PATH"
    

Replace:

  * `COMPOSER_2_ENV` with the name of your Managed Airflow (Gen 2) environment.
  * `COMPOSER_2_LOCATION` with the region where the Managed Airflow (Gen 2) environment is located.
  * `SNAPSHOT_PATH` with the URI of your Managed Airflow (Legacy Gen 1) environment's bucket, followed by the path to the snapshot. For example, `gs://us-central1-example-916807e1-bucket/snapshots/example-project_us-central1_example-environment_2022-01-05T18-59-00`.



## Step 8: Unpause DAGs in the Managed Airflow (Gen 2) environment

You can use any of the following options:

  * In [the Airflow web interface](https://docs.cloud.google.com/composer/docs/composer-2/access-airflow-web-interface), go to **DAGs** and unpause all DAGs manually one by one.

  * Use the [composer_dags](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/main/composer/tools/composer_dags.py) script to unpause all DAGs:
        
        python3 composer_dags.py --environment COMPOSER_2_ENV \
          --project PROJECT_ID \
          --location COMPOSER_2_LOCATION \
          --operation unpause
        

Replace:

    * `COMPOSER_2_ENV` with the name of your Managed Airflow (Gen 2) environment.
    * `PROJECT_ID` with the [Project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).
    * `COMPOSER_2_LOCATION` with the region where the environment is located.
  * _(Airflow versions 2.9.1 and later)_ If there are quota errors while unpausing a large number of DAGs, you can use the following Airflow CLI commands to unpause all DAGs at once:
        
        gcloud composer environments run COMPOSER_2_ENV dags unpause \
          --project PROJECT_ID \
          --location COMPOSER_2_LOCATION \
          -- -y --treat-dag-id-as-regex ".*"
        

  * _(Airflow versions earlier than 2.9.1)_ If there are quota errors while unpausing a large number of DAGs, it's possible to unpause DAGs using the [Airflow REST API](https://docs.cloud.google.com/composer/docs/composer-2/access-airflow-api). Also see [Trying the API](https://airflow.apache.org/docs/apache-airflow/stable/stable-rest-api-ref.html#section/Trying-the-API) in the Airflow documentation.




## Step 9: Check for DAG errors

  1. In [the Airflow web interface](https://docs.cloud.google.com/composer/docs/composer-2/access-airflow-web-interface), go to **DAGs** and check for reported DAG syntax errors.

  2. Check that DAG runs are scheduled at the correct time.

  3. Wait for the DAG runs to happen in the Managed Airflow (Gen 2) environment and check if they were successful. If a DAG run was successful, do not unpause it in the Managed Airflow (Legacy Gen 1) environment; if you do so, a DAG run for the same time and date happens in your Managed Airflow (Legacy Gen 1) environment.

  4. If a specific DAG runs fails, attempt to [troubleshoot the DAG](https://docs.cloud.google.com/composer/docs/composer-1/troubleshooting-dags) until it successfully runs in Managed Airflow (Gen 2).




## Step 10: Monitor your Managed Airflow (Gen 2) environment

After you transfer all DAGs and configuration to the Managed Airflow (Gen 2) environment, monitor it for potential issues, failed DAG runs, and overall environment health.

If the Managed Airflow (Gen 2) environment runs without problems for a sufficient period of time, consider deleting the Managed Airflow (Legacy Gen 1) environment.

## What's next

  * [Troubleshooting DAGs](https://docs.cloud.google.com/composer/docs/composer-1/troubleshooting-dags)
  * [Troubleshooting environment creation](https://docs.cloud.google.com/composer/docs/composer-1/troubleshooting-environment-creation)
  * [Troubleshooting environment updates](https://docs.cloud.google.com/composer/docs/composer-1/troubleshooting-updates-upgrades)
  * [Using backport packages](https://docs.cloud.google.com/composer/docs/composer-1/backport-packages)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
