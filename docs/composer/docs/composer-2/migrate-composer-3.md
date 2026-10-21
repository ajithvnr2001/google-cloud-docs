---
url: https://docs.cloud.google.com/composer/docs/composer-2/migrate-composer-3/
title: Migrate environments to Managed Airflow\u00a0(Gen\u00a03) \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:26:56.578898+00:00
---

# Migrate environments to Managed Airflow (Gen 3)  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-2/migrate-composer-3/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 2 Guides ](https://docs.cloud.google.com/composer/docs/composer-2/composer-overview)



Send feedback 

#  Migrate environments to Managed Airflow (Gen 3) Stay organized with collections  Save and categorize content based on your preferences. 

Managed Airflow (Gen 3) | **Managed Airflow (Gen 2)** | Managed Airflow (Legacy Gen 1)

This page explains how to transfer DAGs, data and configuration from your existing Managed Airflow (Gen 2) environment to Managed Airflow (Gen 3).

## Other migration guides

From | To | Method | Guide  
---|---|---|---  
Managed Airflow (Gen 3), Airflow 2 | Managed Airflow (Gen 3), Airflow 3 | Side-by-side, manual transfer | [Manual migration guide](https://docs.cloud.google.com/composer/docs/composer-3/migrate-airflow-3)  
Managed Airflow (Gen 2) | Managed Airflow (Gen 3) | Side-by-side, using the migration script | [Script migration guide](https://docs.cloud.google.com/composer/docs/composer-2/migrate-composer-3-script)  
Managed Airflow (Gen 2) | Managed Airflow (Gen 3) | Side-by-side, using snapshots | This guide  
Managed Airflow (Legacy Gen 1), Airflow 2 | Managed Airflow (Gen 3) | Side-by-side, using snapshots | [Snapshots migration guide](https://docs.cloud.google.com/composer/docs/composer-1/migrate-composer-1-to-3)  
Managed Airflow (Legacy Gen 1), Airflow 2 | Managed Airflow (Gen 2) | Side-by-side, using snapshots | [Snapshots migration guide](https://docs.cloud.google.com/composer/docs/composer-1/migrate-composer-2-snapshots-af-2)  
Managed Airflow (Legacy Gen 1), Airflow 2 | Managed Airflow (Gen 2) | Side-by-side, manual transfer | [Manual migration guide](https://docs.cloud.google.com/composer/docs/composer-1/migrate-composer-2-af-2)  
Managed Airflow (Legacy Gen 1), Airflow 1 | Managed Airflow (Gen 2), Airflow 2 | Side-by-side, using snapshots | [Snapshots migration guide](https://docs.cloud.google.com/composer/docs/composer-1/migrate-composer-2-snapshots-af-1)  
Managed Airflow (Legacy Gen 1), Airflow 1 | Managed Airflow (Gen 2), Airflow 2 | Side-by-side, manual transfer | [Manual migration guide](https://docs.cloud.google.com/composer/docs/composer-1/migrate-composer-2-af-1)  
Managed Airflow (Legacy Gen 1), Airflow 1 | Managed Airflow (Legacy Gen 1), Airflow 2 | Side-by-side, manual transfer | [Manual migration guide](https://docs.cloud.google.com/composer/docs/composer-1/migrate-environments-airflow-2)  
  
## Before you begin

  * This migration guide uses [snapshots](https://docs.cloud.google.com/composer/docs/composer-2/save-load-snapshots). Snapshots are supported in Managed Airflow (Gen 2) version 2.0.9 and later.

  * Managed Airflow supports side-by-side migration from Managed Airflow (Gen 2) to Managed Airflow (Gen 3). It is not possible to upgrade from Managed Airflow (Gen 2) to Managed Airflow (Gen 3) in-place.

  * Check the [list of differences between Managed Airflow (Gen 2) and Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-versioning-overview). Make sure that your environment doesn't use features that aren't yet available in Managed Airflow (Gen 3).

  * The maximum size of the Airflow database that supports snapshots is 20 GB. If your environment's database takes more than 20 GB, [reduce the size of the Airflow database](https://docs.cloud.google.com/composer/docs/composer-2/cleanup-airflow-database).

  * The total number of objects in the `/dags`, `/plugins` and `/data` folders in the environment's bucket must be less than 100,000 to create snapshots.

  * If you use the XCom mechanism to transfer files, make sure that you [use it according to Airflow's guidelines](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/xcoms.html#object-storage-xcom-backend). Transferring big files or a large number of files using XCom impacts Airflow database's performance and can lead to failures when loading snapshots or upgrading your environment. Consider using alternatives such as Cloud Storage to transfer large volumes of data.




## Make sure that your DAGs are compatible with Managed Airflow (Gen 3)

Make sure that your DAGs are compatible with Managed Airflow (Gen 3) by following these suggestions:

  * The [list of packages](https://docs.cloud.google.com/composer/docs/composer-versions) in the Managed Airflow (Gen 3) environment can be different than in your Managed Airflow (Gen 2) environment. This might affect the compatibility of your DAGs with Managed Airflow (Gen 3).

  * Managed Airflow loads configuration overrides, environment variables, and PyPI packages from your Managed Airflow (Gen 2) environment's snapshot to Managed Airflow (Gen 3) without changing or adjusting them for compatibility. To solve conflicts between these configuration parameters, you can skip loading custom PyPI packages, environment variables, and Airflow configuration overrides when you load the snapshot.

  * In Managed Airflow (Gen 3), the environment's cluster [is located in the tenant project](https://docs.cloud.google.com/composer/docs/composer-3/environment-architecture). Make sure that your DAGs are compatible with this change. In particular, [`KubernetesPodOperator`](https://docs.cloud.google.com/composer/docs/composer-3/use-kubernetes-pod-operator) workloads now scale independently from your environment and it's not possible to use Pod affinity configs. 




## Pause DAGs in your Managed Airflow (Gen 2) environment

**Warning:** If a DAG is enabled (not paused) in both environments, each environment runs its own copy of the DAG, as scheduled. This might lead to duplicate DAG runs for the same data and execution time.

To avoid duplicate DAG runs, pause all DAGs in your Managed Airflow (Gen 2) environment before saving its snapshot. Skip the liveness monitoring DAG (`airflow_monitoring`), it is used for monitoring purposes and is not included in environment snapshots.

You can use any of the following options to pause DAGs:

  * Pause DAGs one by one in Google Cloud console:

    1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

    2. Select an environment to view its details.

    3. On the **Environment details** page, go to the **DAGs** tab.

    4. Click the name of a DAG.

    5. On the **DAG details** page, click **Pause DAG**.

  * In [the Airflow web interface](https://docs.cloud.google.com/composer/docs/composer-2/access-airflow-web-interface), go to **DAGs** and pause all DAGs manually.

  * Use the [composer_dags](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/main/composer/tools/composer_dags.py) script to pause all DAGs:
        
        python3 composer_dags.py --environment COMPOSER_2_ENV \
          --project PROJECT_ID \
          --location COMPOSER_2_LOCATION \
          --operation pause
        

Replace:

    * `COMPOSER_2_ENV` with the name of your Managed Airflow (Gen 2) environment.
    * `PROJECT_ID` with the [Project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).
    * `COMPOSER_2_LOCATION` with the region where the environment is located.



## Save a snapshot of your Managed Airflow (Gen 2) environment

**Caution:** If any changes or DAG runs happen in your Managed Airflow (Gen 2) environment after you save its snapshot, information about these changes is not transferred when you load the snapshot later.

###  Console 

Create a snapshot of your environment:

  1. In Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your Managed Airflow (Gen 2) environment. The **Environment details** page opens.

  3. Click **Create snapshot**.

  4. In the **Create snapshot** dialog, click **Submit**. In this guide, you save the snapshot in the Managed Airflow (Gen 2) environment's bucket, but you can select a different location, if you want to. If you specify a custom location, the [service accounts of both environments](https://docs.cloud.google.com/composer/docs/composer-2/access-control#service-account) must have read and write permissions for the specified location.

  5. Wait until Managed Airflow creates the snapshot.

  6. After the snapshot is created, the displayed message outputs the location of the snapshot. Save this information to use later when you load this snapshot to the Managed Airflow (Gen 3) environment.

For example, the snapshot location might look like: `gs://us-central1-example-916807e1-bucket/snapshots/snapshots_example-project_us-central1_example-environment/2024-05-15T15-23-12`.




###  gcloud 

  1. Create a snapshot of your Managed Airflow (Gen 2) environment:
         
         gcloud composer environments snapshots save \
           COMPOSER_2_ENV \
           --location COMPOSER_2_LOCATION
         

Replace:

     * `COMPOSER_2_ENV` with the name of your Managed Airflow (Gen 2) environment.
     * `COMPOSER_2_LOCATION` with the region where the Managed Airflow (Gen 2) environment is located.
     * (optional) You can use the `--snapshot-location` argument to specify a a custom location where the environment's snapshot must be stored.

In this guide, you save the snapshot in the Managed Airflow (Gen 2) environment's bucket, but you can select a different location, if you want to. If you specify a custom location, the [service accounts of both environments](https://docs.cloud.google.com/composer/docs/composer-2/access-control#service-account) must have read and write permissions for the specified location.

  2. After the snapshot is created, the displayed message outputs the location of the snapshot. Save this information to use later when you load this snapshot to the Managed Airflow (Gen 3) environment.

For example, the snapshot location might look like: `gs://us-central1-example-916807e1-bucket/snapshots/snapshots_example-project_us-central1_example-environment/2024-05-15T15-23-12`.




## Create a Managed Airflow (Gen 3) environment

[Create a Managed Airflow (Gen 3) environment](https://docs.cloud.google.com/composer/docs/composer-3/create-environments) using the following guidelines:

  * You can start with the same resource limits configuration as your Managed Airflow (Gen 2) environment and later scale and optimize the configuration further.

  * In Managed Airflow (Gen 3) environments, [Airflow DAG processor](https://docs.cloud.google.com/composer/docs/composer-3/scale-environments#dag-processor-parameters) runs as a separate environment component. Because DAG processor offloads the parsing of DAGs from the scheduler, you might want to redistribute resources previously allocated to Airflow schedulers. You can do it later after you migrate to Managed Airflow (Gen 3) and monitor the scheduler and DAG processor performance.

  * Managed Airflow (Gen 3) provides a more streamlined and simplified networking setup compared to Managed Airflow (Gen 2). It is possible to switch between Public IP and Private IP networking configuration and attach and detach VPC networks. You don't need to specify IP ranges . Make sure that your Managed Airflow (Gen 3) environment's networking configuration matches the corresponding Managed Airflow (Gen 2) configuration.

  * You don't need to specify configuration overrides and environment variables because you replace them later when you load the snapshot of your Managed Airflow (Gen 2) environment.




## Load the snapshot to your Managed Airflow (Gen 3) environment

###  Console 

To load the snapshot to your Managed Airflow (Gen 3) environment:

  1. In Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your Managed Airflow (Gen 3) environment. The **Environment details** page opens.

  3. Click **Load snapshot**.

  4. In the **Load snapshot** dialog, click **Browse**.

  5. Select the folder with the snapshot.

If you use the default location for this guide, this folder is located in your Managed Airflow (Gen 2) environment bucket in the `/snapshots` folder, and its name is the timestamp of the snapshot save operation. The same location was displayed in the message about the successful creation of the snapshot.

For example: `us-central1-example-916807e1-bucket/snapshots_example-project_us-central1_example-environment/2024-05-15T15-23-12`.

  6. Click **Load** and wait until Managed Airflow loads the snapshot.




###  gcloud 

Load the snapshot of your Managed Airflow (Gen 2) environment to your Managed Airflow (Gen 3) environment:
    
    
    gcloud composer environments snapshots load \
      COMPOSER_3_ENV \
      --location COMPOSER_3_LOCATION \
      --snapshot-path "SNAPSHOT_PATH"
    

Replace:

  * `COMPOSER_3_ENV` with the name of your Managed Airflow (Gen 3) environment.
  * `COMPOSER_3_LOCATION` with the region where the Managed Airflow (Gen 3) environment is located.
  * `SNAPSHOT_PATH` with the URI of your Managed Airflow (Gen 2) environment's bucket, followed by the path to the snapshot. The same location was displayed in the message about the successful creation of the snapshot. For example: `gs://us-central1-example-916807e1-bucket/snapshots/example-project_us-central1_example-environment_2024-05-15T15-23-12`.



## Unpause DAGs in the Managed Airflow (Gen 3) environment

You can use any of the following options:

  * Unpause DAGs one by one in Google Cloud console:

    1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

    2. Select an environment to view its details.

    3. On the **Environment details** page, go to the **DAGs** tab.

    4. Click the name of a DAG.

    5. On the **DAG details** page, click **Unpause DAG**.

  * In [the Airflow web interface](https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-web-interface), go to **DAGs** and unpause all DAGs manually one by one.

  * Use the [composer_dags](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/main/composer/tools/composer_dags.py) script to unpause all DAGs:
        
        python3 composer_dags.py --environment COMPOSER_3_ENV \
          --project PROJECT_ID \
          --location COMPOSER_3_LOCATION \
          --operation unpause
        

Replace:

    * `COMPOSER_3_ENV` with the name of your Managed Airflow (Gen 3) environment.
    * `PROJECT_ID` with the [Project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).
    * `COMPOSER_3_LOCATION` with the region where the environment is located.



## Check for DAG errors

  1. In [the Airflow web interface](https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-web-interface), go to **DAGs** and check for reported DAG syntax errors.

  2. Check that DAG runs are scheduled at the correct time.

  3. Wait for the DAG runs to happen in the Managed Airflow (Gen 3) environment and check if they were successful. If a DAG run was successful, don't unpause it in the Managed Airflow (Gen 2) environment; if you do so, a DAG run for the same time and date happens in your Managed Airflow (Gen 2) environment.

  4. If a specific DAG runs fails, attempt to [troubleshoot the DAG](https://docs.cloud.google.com/composer/docs/composer-3/troubleshooting-dags) until it successfully runs in Managed Airflow (Gen 3).




## Monitor your Managed Airflow (Gen 3) environment

After you transfer all DAGs and configuration to the Managed Airflow (Gen 3) environment, monitor it for potential issues, failed DAG runs, and overall environment health.

If the Managed Airflow (Gen 3) environment runs without problems for a sufficient period of time, consider deleting the Managed Airflow (Gen 2) environment.

## What's next

  * [Troubleshooting DAGs](https://docs.cloud.google.com/composer/docs/composer-3/troubleshooting-dags)
  * [Troubleshooting environment creation](https://docs.cloud.google.com/composer/docs/composer-3/troubleshooting-environment-creation)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
