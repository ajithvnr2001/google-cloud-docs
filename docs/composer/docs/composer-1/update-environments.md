---
url: https://docs.cloud.google.com/composer/docs/composer-1/update-environments/
title: Update Managed Airflow environments \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:27:11.514909+00:00
---

# Update Managed Airflow environments  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-1/update-environments/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 1 Guides ](https://docs.cloud.google.com/composer/docs/composer-1/composer-overview)



Send feedback 

#  Update Managed Airflow environments Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/update-environments "View this page for Managed Airflow \(Gen 3\)") | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/update-environments "View this page for Managed Airflow \(Gen 2\)") | **Managed Airflow (Legacy Gen 1)**

This page explains how an environment can be updated.

## About update operations

When you change parameters of your environment, such as specifying new scaling and performance parameters, or installing custom PyPI packages, your environment updates.

After this operation is completed, changes become available in your environment.

For a single Managed Airflow environment, you can start only one update operation at a time. You must wait for an update operation to complete before starting another environment operation.

**Important:** Do not upgrade the GKE clusters of your Managed Airflow environments to newer GKE versions. Use the GKE version pre-configured during the environment creation and rely on auto-upgrades performed by the GKE service.

## How updates affect running Airflow tasks

**Caution:** Some update operations **terminate all running tasks**.

When you run an update operation, Airflow schedulers and workers in your environment might require a restart. In this case, all currently running tasks are terminated. After the update operation is completed, Airflow schedules these tasks for a retry, depending on the way you configure retries for your DAGs.

**Note:** Airflow workers can get restarted as part of the environment maintenance, during the maintenance windows.

The following changes **cause** Airflow task termination:

  * Upgrading your environment to a new version.
  * Adding, changing, or deleting custom PyPI packages.
  * Changing Managed Airflow environment variables.
  * Adding or removing Airflow configuration options overrides, or changing their values.
  * Changing Airflow workers' CPU, memory, or storage.
  * Reducing the maximum number of Airflow workers, if the new value is lower than the number of currently running workers. For example, if an environment currently runs three workers, and the maximum is reduced to two.




The following changes **don't cause** Airflow task termination:

  * Creating, updating, or deleting a DAG (not an update operation).
  * Pausing or unpausing DAGs (not an update operation).
  * Changing Airflow variables (not an update operation).
  * Changing Airflow connections (not an update operation).
  * Enabling or disabling Knowledge Catalog Data Lineage integration.
  * Changing environment's size.
  * Changing the number of schedulers.
  * Changing Airflow schedulers' CPU, memory, or storage.
  * Changing the number of triggerers.
  * Changing Airflow triggerers' CPU, memory, or storage.
  * Changing Airflow web server's CPU, memory, or storage.
  * Increasing or decreasing the minimum number of workers.
  * Reducing the maximum number of Airflow workers. For example, if an environment currently runs two workers, and the maximum is reduced to three.
  * Changing maintenance windows.
  * Changing scheduled snapshots settings.
  * Changing environment labels.



## Updating with Terraform

**Warning:** If you attempt to change a configuration parameter that cannot be updated, Terraform **deletes your environment and creates a new one** with the new parameter value.

Run `terraform plan` before `terraform apply` to see if Terraform creates a new environment instead of updating it.

## Before you begin

  * Check that your account, the service account of your environment, and the Managed Airflow Service Agent account in your project have required permissions:

    * Your account must have a role that [can trigger environment update operations](https://docs.cloud.google.com/composer/docs/composer-1/access-control#user-account).

    * The service account of your environment must have a role that [has enough permissions to perform update operations](https://docs.cloud.google.com/composer/docs/composer-1/access-control#service-account).

  * The `gcloud composer environments update` command terminates when the operation is finished. You can use the `--async` flag to avoid waiting for the operation to complete.




## Update environments

For more information about updating your environment, see other documentation pages about specific update operations. For example:

  * [Override Airflow configuration options](https://docs.cloud.google.com/composer/docs/composer-1/override-airflow-configurations)
  * [Set environment variables](https://docs.cloud.google.com/composer/docs/composer-1/set-environment-variables)
  * [Install Python dependencies](https://docs.cloud.google.com/composer/docs/composer-1/install-python-dependencies)
  * [Scale environments](https://docs.cloud.google.com/composer/docs/composer-1/scale-environments)




## View environment details

###  Console 

  1. In Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.




###  gcloud 

Run the following `gcloud` command:
    
    
    gcloud composer environments describe ENVIRONMENT_NAME \
      --location LOCATION
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `LOCATION` with the region where the environment is located.



###  API 

Construct an [`environments.get`](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments/get) API request.

Example:
    
    
    GET https://composer.googleapis.com/v1/projects/example-project/
    locations/us-central1/environments/example-environment
    

###  Terraform 

Run the `terraform state show` command for your environment's resource.

The name of your environment's Terraform resource might be different than the name of your environment.
    
    
    terraform state show google_composer_environment.RESOURCE_NAME
    

Replace:

  * `RESOURCE_NAME` with the name of your environment's resource.



### Rolling back update changes

In some rare situations, an update operation might be interrupted (for example, because of a timeout) and the requested changes might not be rolled back in all environment components (such as the Airflow web server).

For example, an update operation might be installing or removing additional PyPI modules, re-defining or defining a new Airflow or Managed Airflow environment variable, or changing some Airflow-related parameters.

Such a situation might occur if an update operation is triggered when other operations are in progress, for example Managed Airflow cluster's autoscaling or a maintenance operation.

In such a situation, it's recommended to repeat the operation.

### Duration of update or upgrade operations

The duration of update and upgrade operations is affected by the following factors:

  * Most update or upgrade operations require restarting Airflow components like Airflow schedulers, workers and web servers. After a component is restarted, it must be initialized. During the initialization, Airflow schedulers and workers download the contents of `/dags` and `/plugins` folders from the environment's bucket. The process of syncing files to Airflow schedulers and workers isn't instantaneous and depends on the total size and number of all objects in these folders.

We recommend to keep only DAG and plugin files in `/dags` and `/plugins` folders (respectively) and remove all other files. Too much data in `/dags` and `/plugins` folders might slow down the initialization of Airflow components and in certain cases might make the initialization not possible.

We recommend to keep less than 30 MB of data in `/dags` and `/plugins` folders, and to definitely not exceed 100 MB size of data. For more information, also see [Handling large number of DAGs and plugins](https://docs.cloud.google.com/composer/docs/composer-1/troubleshooting-dags#large-number-of-dags)

  * The size of the Airflow database might significantly increase the time of upgrade operations. We recommend to [maintain the Airflow database](https://docs.cloud.google.com/composer/docs/composer-1/cleanup-airflow-database) size of your environment. 




## Upgrading the machine type for GKE nodes

You can manually upgrade the machine type for your environment's GKE cluster by deleting the existing `default-pool` and creating a new `default-pool` with the desired machine type.

We recommend you to specify a suitable machine type for the type of computing that occurs in your Managed Airflow environment when you [create an environment](https://docs.cloud.google.com/composer/docs/composer-1/create-environments).

If you are running jobs that perform resource-intensive computation, you might want to use [GKE Operators](https://docs.cloud.google.com/composer/docs/composer-1/use-gke-operator).

**Caution:** The execution of your DAGs might be interrupted during the upgrade. Before upgrading, consider pausing all DAGs and wait for in-progress tasks to finish.

After an upgrade, the previous machine type is still listed in your environment's details. For example, the Environment details page does not reflect the new machine type.

###  Console 

To upgrade the machine type:

  1. In Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.

  3. Get information about the default node pool:

     1. Go to the **Environment configuration** tab.

     2. Click the **view cluster details** link.

     3. On the **Clusters page** in the **Nodes** section, click **default-pool**.

     4. Note all the information for **default-pool** on the Node pool details page. You use this information to create a new default node pool for your environment.

  4. To delete **default-pool** :

     1. On the **Node pool details** page, click the back arrow to return to the **Clusters** page for your environment.

     2. In the **Node Pools** section, click the trash icon for the **default-pool**. Then click **Delete** to confirm the operation.

  5. To create the new **default-pool** :

**Caution:** Use the same service account that runs the Managed Airflow environment. If you use a custom service account and rely on access scopes then you must use gcloud CLI to create a new pool with proper scopes. To do so, follow the instructions on the [Add and manage node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools#gcloud-config) page. Specify access scopes using the [`--scopes` parameter](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/access-scopes#changes).
     1. On the **Clusters** page, click **Add node pool**.

     2. For Name, enter `default-pool`. You must use the `default-pool` name so that workflows in your environment can run in this pool.

     3. Enter the Size and Nodes settings.

     4. (Only for default Compute Engine service accounts) For Access scopes, select **Allow full access to all Cloud APIs**.

     5. Click **Save**.

  6. If you notice that workloads are distributed unevenly, [scale down](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/scaling-apps#scaling_an_application) the airflow-worker deployment to zero and scale up again.




## What's next

  * [Upgrade environments](https://docs.cloud.google.com/composer/docs/composer-1/upgrade-environments)
  * [Override Airflow configuration options](https://docs.cloud.google.com/composer/docs/composer-1/override-airflow-configurations)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
