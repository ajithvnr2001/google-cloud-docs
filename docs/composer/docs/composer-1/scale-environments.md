---
url: https://docs.cloud.google.com/composer/docs/composer-1/scale-environments/
title: Scale environments \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:26:58.030062+00:00
---

# Scale environments  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-1/scale-environments/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 1 Guides ](https://docs.cloud.google.com/composer/docs/composer-1/composer-overview)



Send feedback 

#  Scale environments Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/scale-environments "View this page for Managed Airflow \(Gen 3\)") | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/scale-environments "View this page for Managed Airflow \(Gen 2\)") | **Managed Airflow (Legacy Gen 1)**

This page describes how to scale Managed Airflow environments.

  * For information about how environment scaling works, see [Environment scaling](https://docs.cloud.google.com/composer/docs/composer-1/environment-scaling).



## Scale vertically and horizontally

In Managed Airflow (Legacy Gen 1), you don't define specific CPU and memory resources for Managed Airflow and Airflow components such as workers and schedulers. Instead, you specify the number and type of machines for nodes in your environment's cluster.

**Note:** During component distribution in Managed Airflow (Legacy Gen 1), some Airflow components might be placed unevenly over the available nodes. In such a scenario, the CPU or memory load of one or more nodes is higher compared to other nodes in the cluster.

Options for horizontal scaling:

  * Adjust the number of nodes
  * Adjust the number of schedulers



Options for vertical scaling:

  * Adjust the machine type of the Cloud SQL instance
  * Adjust the web server machine type

**Note:** When configuring resource limits for Airflow components, make sure that the limits exceed the minimum resource requirements for your usage scenario. [Sidecar containers](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/) that run alongside the main Airflow component's container utilize some of the allocated resources.

## Adjust scheduler parameters

Your environment can run more than one Airflow scheduler at the same time. Use multiple schedulers to distribute load between several scheduler instances for better performance and reliability.

If your environment uses Airflow 2, you can specify a number of schedulers up to the number of nodes in your environment.

When scaling schedulers, use the following considerations:

  * Increasing the number of schedulers doesn't always improve Airflow performance.

For example, this might happen when the extra scheduler isn't utilized, and consumes resources of your environment without contributing to the overall performance. The actual scheduler performance depends on the number of Airflow workers, the number of DAGs and tasks that run in your environment, and the configuration of both Airflow and the environment.

  * We recommend starting with two schedulers and then monitoring the performance of your environment. 




For more information about configuring multiple schedulers, see [Airflow documentation](https://airflow.apache.org/docs/apache-airflow/stable/concepts/scheduler.html#scheduler-tuneables).

###  Console 

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.

  3. Go to the **Environment configuration** tab.

  4. In the **Resources** > **Workloads configuration** item, click **Edit**.

  5. In the **Resources** > **Number of schedulers** item, click **Edit**.

  6. In the **Scheduler configuration** pane, in the **Number of schedulers** field, specify the number of schedulers for your environment.

  7. Click **Save**.




###  gcloud 

The following Airflow scheduler parameters are available:

  * `--scheduler-count`: the number of schedulers in your environment.




Run the following Google Cloud CLI command:
    
    
    gcloud composer environments update ENVIRONMENT_NAME \
      --location LOCATION \
      --scheduler-count SCHEDULER_COUNT
    

Replace the following:

  * `ENVIRONMENT_NAME`: the name of the environment.
  * `LOCATION`: the region where the environment is located.




Example:
    
    
    gcloud composer environments update example-environment \
      --location us-central1 \
      --scheduler-count 2
    

###  API 

  1. Construct an [`environments.patch`](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments/patch) API request.

  2. In this request:

     1. In the `updateMask` parameter, specify the `config.workloadsConfig.schedulerCount` mask.

     2. In the request body, specify the number of schedulers for your environment.



    
    
    "config": {
      "workloadsConfig": {
        "scheduler": {
          "count": SCHEDULER_COUNT
        }
      }
    }
    

Replace the following:

  * `ENVIRONMENT_NAME`: the name of the environment.
  * `LOCATION`: the region where the environment is located.

  * `SCHEDULER_COUNT`: the number of schedulers.




Example:
    
    
    // PATCH https://composer.googleapis.com/v1/projects/example-project/
    // locations/us-central1/environments/example-environment?updateMask=
    // config.workloadsConfig.scheduler
    
    "config": {
      "workloadsConfig": {
        "scheduler": {
          "count": 2
        }
      }
    }
    

###  Terraform 

The following fields in the `workloads_config.scheduler` block control the Airflow scheduler parameters. Each scheduler uses the specified amount of resources.

  * `scheduler.count`: the number of schedulers in your environment.



    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "ENVIRONMENT_NAME"
      region = "LOCATION"
    
      config {
    
        workloads_config {
          scheduler {
            count = SCHEDULER_COUNT
          }
        }
    
      }
    }
    

Replace the following:

  * `ENVIRONMENT_NAME`: the name of the environment.
  * `LOCATION`: the region where the environment is located.

  * `SCHEDULER_COUNT`: the number of schedulers.




Example:
    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "example-environment"
      region = "us-central1"
    
      config {
    
        workloads_config {
          scheduler {
            
            count = 2
          }
        }
    
      }
    }
    

## Adjust the number of nodes

You can change the number of nodes in your environment.

This number corresponds to the number of Airflow workers in your environment. In addition to running Airflow workers, your environment nodes also run Airflow schedulers and other environment components.

###  Console 

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.

  3. Go to the **Environment configuration** tab.

  4. In the **Worker nodes** > **Node count** item, click **Edit**.

  5. In the **Worker nodes configuration** pane, in the **Node count** field, specify the number of nodes in your environment.

  6. Click **Save**.




###  gcloud 

The `--node-count` argument controls the number of nodes in your environment:
    
    
    gcloud composer environments update ENVIRONMENT_NAME \
        --location LOCATION \
        --zone NODE_ZONE \
        --node-count NODE_COUNT
    

Replace the following:

  * `ENVIRONMENT_NAME`: the name of the environment.
  * `LOCATION`: the region where the environment is located.
  * `NODE_COUNT`: the number of nodes. The minimum number of nodes is `3`.
  * `NODE_ZONE`: the Compute Engine zone for your environment VMs.



Example:
    
    
    gcloud composer environments update example-environment \
        --location us-central1 \
        --zone us-central1-a \
        --node-count 6
    

###  API 

  1. Create an [`environments.patch`](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments/patch) API request.

  2. In this request:

     1. In the `updateMask` parameter, specify the `config.nodeCount` mask.

     2. In the request body, specify the number of nodes for your environment.



    
    
      "config": {
        "nodeCount": NODE_COUNT
      }
    

Replace the following:

  * `NODE_COUNT`: the number of nodes. The minimum number of nodes is `3`.



Example:
    
    
    // PATCH https://composer.googleapis.com/v1/projects/example-project/
    // locations/us-central1/environments/example-environment?updateMask=
    // config.nodeCount
    
    "config": {
      "nodeCount": 6
    }
    

###  Terraform 

The `node_count` field in the `node_config` block specifies the number of nodes in your environment.
    
    
    resource "google_composer_environment" "example" {
    
      config {
        node_config {
          node_count = NODE_COUNT
        }
    }
    

Replace the following:

  * `NODE_COUNT`: the number of nodes.



Example:
    
    
    resource "google_composer_environment" "example" {
      name = "example-environment"
      region = "us-central1"
    
      config {
    
        node_config {
          node_count = 4
        }
    
    }
    

**Note:** Changing the node count of an environment does not trigger the rebuilding of Airflow images used for the environment.

## Adjust the machine type of the Cloud SQL instance

You can change the machine type of the Cloud SQL instance that stores the Airflow database of your environment.

###  Console 

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.

  3. Go to the **Environment configuration** tab.

  4. In the **Resources** > **Cloud SQL machine type** item, click **Edit**.

  5. In the **Cloud SQL configuration** pane, in the **Cloud SQL machine type** drop-down list, select the machine type for the Cloud SQL instance of your environment.

  6. Click **Save**.




###  gcloud 

The `--cloud-sql-machine-type` arguments controls the machine type of the Cloud SQL instance in your environment.

Run the following Google Cloud CLI command:
    
    
    gcloud composer environments update ENVIRONMENT_NAME \
      --location LOCATION \
      --cloud-sql-machine-type SQL_MACHINE_TYPE
    

Replace the following:

  * `ENVIRONMENT_NAME`: the name of the environment.
  * `LOCATION`: the region where the environment is located.
  * `SQL_MACHINE_TYPE`: the [machine type for the Cloud SQL instance](https://docs.cloud.google.com/composer/pricing#db-machine-types).



Example:
    
    
    gcloud composer environments update example-environment \
      --location us-central1 \
      --cloud-sql-machine-type db-n1-standard-2
    

###  API 

  1. Create an [`environments.patch`](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments/patch) API request.

  2. In this request:

     1. In the `updateMask` parameter, specify the `config.databaseConfig.machineType` mask.

     2. In the request body, specify the machine type for the Cloud SQL instance.



    
    
    {
      "config": {
        "databaseConfig": {
          "machineType": "SQL_MACHINE_TYPE"
        }
      }
    }
    

Replace the following:

  * `SQL_MACHINE_TYPE`: the machine type [for the Cloud SQL instance](https://docs.cloud.google.com/composer/pricing#db-machine-types).



Example:
    
    
    // PATCH https://composer.googleapis.com/v1/projects/example-project/
    // locations/us-central1/environments/example-environment?updateMask=
    // config.databaseConfig.machineType
    
    {
      "config": {
        "databaseConfig": {
          "machineType": "db-n1-standard-2"
        }
      }
    }
    

###  Terraform 

The `machine_type` field in the `database_config` block specifies the machine type for the Cloud SQL instance.
    
    
    resource "google_composer_environment" "example" {
    
      config {
        database_config {
          machine_type = "SQL_MACHINE_TYPE"
        }
      }
    }
    

Replace the following:

  * `SQL_MACHINE_TYPE`: the machine type [for the Cloud SQL instance](https://docs.cloud.google.com/composer/pricing#db-machine-types).



Example:
    
    
    resource "google_composer_environment" "example" {
      name = "example-environment"
      region = "us-central1"
    
      config {
        database_config {
          machine_type = "db-n1-standard-2"
        }
    }
    

## Adjust the web server machine type

You can change the machine type for the Airflow web server of your environment.

###  Console 

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.

  3. Go to the **Environment configuration** tab.

  4. In the **Resources** > **Web server machine type** item, click **Edit**.

  5. In the **Web server configuration** pane, in the **Web server machine type** drop-down list, select the machine type for the Airflow web server.

  6. Click **Save**.




###  gcloud 

The `--web-server-machine-type` arguments controls the machine type of the Airflow web server instance in your environment.

Run the following Google Cloud CLI command:
    
    
    gcloud composer environments update ENVIRONMENT_NAME \
      --location LOCATION \
      --web-server-machine-type WS_MACHINE_TYPE
    

Replace the following:

  * `ENVIRONMENT_NAME`: the name of the environment.
  * `LOCATION`: the region where the environment is located.
  * `WS_MACHINE_TYPE`: the [machine type for the Airflow web server instance](https://docs.cloud.google.com/composer/pricing#ws-machine-types).



Example:
    
    
    gcloud composer environments update example-environment \
      --location us-central1 \
      --web-server-machine-type composer-n1-webserver-2
    

###  API 

  1. Create an [`environments.patch`](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments/patch) API request.

  2. In this request:

     1. In the `updateMask` parameter, specify the `config.webServerConfig.machineType` mask.

     2. In the request body, specify the machine type for the web server.



    
    
    {
      "config": {
        "webServerConfig": {
          "machineType": "WS_MACHINE_TYPE"
        }
      }
    }
    

Replace the following:

  * `WS_MACHINE_TYPE`: the [machine type for the Airflow web server instance](https://docs.cloud.google.com/composer/pricing#ws-machine-types).



Example:
    
    
    // PATCH https://composer.googleapis.com/v1/projects/example-project/
    // locations/us-central1/environments/example-environment?updateMask=
    // config.webServerConfig.machineType
    
    {
      "config": {
        "webServerConfig": {
          "machineType": "composer-n1-webserver-2"
        }
      }
    }
    

###  Terraform 

The `machine_type` field in the `web_server_config` block specifies the machine type for the Airflow web server instance.
    
    
    resource "google_composer_environment" "example" {
    
      config {
        web_server_config {
          machine_type = "WS_MACHINE_TYPE"
        }
      }
    }
    

Replace the following:

  * `WS_MACHINE_TYPE`: the [machine type for the Airflow web server instance](https://docs.cloud.google.com/composer/pricing#ws-machine-types).



Example:
    
    
    resource "google_composer_environment" "example" {
      name = "example-environment"
      region = "us-central1"
    
      config {
        web_server_config {
          machine_type = "composer-n1-webserver-2"
        }
    }
    

## What's next

  * [Environment scaling and performance](https://docs.cloud.google.com/composer/docs/composer-1/environment-scaling)
  * [Managed Airflow pricing](https://docs.cloud.google.com/composer/pricing)
  * [Update environments](https://docs.cloud.google.com/composer/docs/composer-1/update-environments)
  * [Environment architecture](https://docs.cloud.google.com/composer/docs/composer-1/environment-architecture)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
