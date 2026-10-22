---
url: https://docs.cloud.google.com/composer/docs/composer-3/scale-environments/
title: Scale environments \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:07:42.844717+00:00
---

# Scale environments  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-3/scale-environments/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 3 Guides ](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview)



Send feedback 

#  Scale environments Stay organized with collections  Save and categorize content based on your preferences. 

**Managed Airflow (Gen 3)** | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/scale-environments "View this page for Managed Airflow \(Gen 2\)") | [Managed Airflow (Legacy Gen 1)](https://docs.cloud.google.com/composer/docs/composer-1/scale-environments "View this page for Managed Airflow \(Legacy Gen 1\)")

This page describes how to scale Managed Airflow environments.

Other pages about scaling:

  * For a guide about selecting optimal scale and performance parameters for your environment, see [Optimize environment performance and costs](https://docs.cloud.google.com/composer/docs/composer-3/optimize-environments).
  * For information about how environment scaling works, see [Environment scaling](https://docs.cloud.google.com/composer/docs/composer-3/environment-scaling).



## Scale vertically and horizontally

Options for horizontal scaling:

  * Adjust the minimum and maximum number of workers.
  * Adjust the number of schedulers, DAG processors, and triggerers.



Options for vertical scaling:

  * Adjust worker, scheduler, triggerer, DAG processor, and web server. scale and performance parameters.
  * Adjust the environment size.

**Important:** For production use cases, we highly recommend to use [highly resilient (Highly Available) environments](https://docs.cloud.google.com/composer/docs/composer-3/set-up-highly-resilient-environments). The Airflow database of your environment is zonal. During a zonal outage, Airflow tasks that are executed in the affected zone are interrupted and marked as failed by Airflow. Highly resilient environments are more resilient to this issue, because their databases are located in two separate zones.

## Resource limits

Component | Minimum count | Maximum count | Minimum vCPU | Maximum vCPU | vCPU minimum step | Minimum memory (GB) | Maximum memory (GB) | Memory minimum step (GB) | Minimum memory per 1 vCPU (GB) | Maximum memory per 1 vCPU (GB) | Minimum storage (GB) | Maximum storage (GB) | Storage minimum step (GB)  
---|---|---|---|---|---|---|---|---|---|---|---|---|---  
Schedulers | 1 | 3 | 0.5 | 2 | 0.5 | 1 (2 in Airflow 3) | 8 | 0.25 | 1 | 8 | 0 | 100 | 1  
Triggerers | 0 | 10 | 0.5 | 1 | 0.5 | 1 (2 in Airflow 3) | 8 | 0.25 | 1 | 8 | - | - | -  
Web server | - | - | 1 (supported minimum) | 4 | 0.5, 1, or a multiple of 2 | 2 | 32 | 0.25 | 1 | 8 | 0 | 100 | 1  
Workers | 1 | 100 | 0.5 | 32 | 0.5, 1, or a multiple of 2 | 1 (2 in Airflow 3) | 256 | 0.25 | 1 | 8 | 0 | 100 | 1  
DAG processors | 1 | 3 | 0.5 | 32 | 0.5, 1, or a multiple of 2 | 1 (2 in Airflow 3) | 256 | 0.25 | 1 | 8 | 0 | 100 | 1  
**Note:** When configuring resource limits for Airflow components, make sure that the limits exceed the minimum resource requirements for your usage scenario. [Sidecar containers](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/) that run alongside the main Airflow component's container utilize some of the allocated resources.

## Environment presets

When you [create an environment](https://docs.cloud.google.com/composer/docs/composer-3/create-environments) in Google Cloud console, you can select one of three environment presets. These presets set the initial scale and performance configuration of your environment; after you create your environment, you can change all scale and performance parameters provided by a preset.

We recommend to select presets based on the following estimates:

  * Total number of DAGs that you plan to deploy in the environment
  * Maximum number of concurrent DAG runs
  * Maximum number of concurrent tasks



Your environment's performance depends on the implementation of specific DAGs that you run in your environment. The following table lists estimates that are based on the average resource consumption. If you expect your DAGs to consume more resources, adjust the estimates accordingly.

**Important:** Each environment preset is configured with CPU, memory, disk space, and infrastructure size to meet the listed estimates. Because Airflow performance can change with new Airflow version releases, we might adjust resource configuration of environment presets in the future.Recommended preset | Total DAGs | Max concurrent DAG runs | Max concurrent tasks  
---|---|---|---  
Small | 50 | 15 | 18  
Medium | 250 | 60 | 100  
Large | 1000 | 250 | 400  
Extra Large | 3000 | 750 | 2250  
  
For example, an environment must run 40 DAGs. All DAGs must run at the same time with one active task each. This environment would then use a Medium preset, because the maximum number of concurrent DAG runs and tasks exceed the recommended estimates for the Small preset.

## Adjust worker parameters

You can set the minimum and maximum number of workers for your environment. Managed Airflow automatically scales your environment within the set limits. You can adjust these limits at any time.

You can specify the amount of CPUs, memory, and disk space used by Airflow workers in your environment. In this way, you can increase performance of your environment, in addition to horizontal scaling provided by using multiple workers.

**Note:** For information about possible values and limits for resources, see the Resource limits section.

###  Console 

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.

  3. Go to the **Environment configuration** tab.

  4. In the **Resources** > **Workloads configuration** item, click **Edit**.

  5. In the **Workloads configuration** pane adjust the parameters for Airflow workers:

     * In the **Minimum number of workers** field, specify the number of Airflow workers that your environment must always run. The number of workers in your environment does not go below this number during the regular operation of the environment, even if a lower number of workers can handle the load.

**Note:** The number of workers can temporarily go below the minimum number of workers during [maintenance operations](https://docs.cloud.google.com/composer/docs/composer-3/specify-maintenance-windows) and when you [upgrade or update](https://docs.cloud.google.com/composer/docs/composer-3/update-environments#updates-restart) your environment.
     * In the **Maximum number of workers** field, specify the maximum number of Airflow workers that your environment can run. The number of workers in your environment does not go above this number, even if a higher number of workers is required to handle the load.

     * In the **CPU** , **Memory** , and **Storage** fields, specify the number of CPUs, memory, and storage for Airflow workers. Each worker uses the specified amount of resources.

  6. Click **Save**.




###  gcloud 

The following Airflow worker parameters are available:

  * `--min-workers`: the number of Airflow workers that your environment must always run. The number of workers in your environment does not go below this number, even if a lower number of workers can handle the load.
  * `--max-workers`: the maximum number of Airflow workers that your environment can run. The number of workers in your environment does not go above this number, even if a higher number of workers is required to handle the load.
  * `--worker-cpu`: the number of CPUs for an Airflow worker.
  * `--worker-memory`: the amount of memory for an Airflow worker.
  * `--worker-storage`: the amount of disk space for an Airflow worker.



Run the following Google Cloud CLI command:
    
    
    gcloud composer environments update ENVIRONMENT_NAME \
      --location LOCATION \
      --min-workers WORKERS_MIN \
      --max-workers WORKERS_MAX \
      --worker-cpu WORKER_CPU \
      --worker-memory WORKER_MEMORY \
      --worker-storage WORKER_STORAGE
    

Replace the following:

  * `ENVIRONMENT_NAME`: the name of the environment.
  * `LOCATION`: the region where the environment is located.
  * `WORKERS_MIN`: the minimum number of Airflow workers.
  * `WORKERS_MAX`: the maximum number of Airflow workers.
  * `WORKER_CPU`: the number of CPUs for a worker, in vCPU units.
  * `WORKER_MEMORY`: the amount of memory for a worker.
  * `WORKER_STORAGE`: the disk size for a worker.

**Note:** The specified value for memory and disk space must be a whole number followed by a size unit of `KB` for kilobyte, `MB` for megabyte, or `GB` for gigabyte. The default size unit is `GB`. For example, `10GB` produces a 10 gigabyte storage.

Example:
    
    
    gcloud composer environments update example-environment \
      --location us-central1 \
      --min-workers 2 \
      --max-workers 6 \
      --worker-cpu 1 \
      --worker-memory 2 \
      --worker-storage 2
    

###  API 

  1. Construct an [`environments.patch`](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments/patch) API request.

  2. In this request:

     1. In the `updateMask` parameter, specify the fields that you want to update. For example, to update all parameters for workers, specify the `config.workloadsConfig.worker.cpu,config.workloadsConfig.worker.memoryGb,config.workloadsConfig.worker.storageGB,config.softwareConfig.workloadsConfig.worker.minCount,config.softwareConfig.workloadsConfig.worker.maxCount` mask.

     2. In the request body, specify the new worker parameters.



    
    
    "config": {
      "workloadsConfig": {
        "worker": {
          "minCount": WORKERS_MIN,
          "maxCount": WORKERS_MAX,
          "cpu": WORKER_CPU,
          "memoryGb": WORKER_MEMORY,
          "storageGb": WORKER_STORAGE
        }
      }
    }
    

Replace the following:

  * `ENVIRONMENT_NAME`: the name of the environment.
  * `LOCATION`: the region where the environment is located.
  * `WORKERS_MIN`: the minimum number of Airflow workers.
  * `WORKERS_MAX`: the maximum number of Airflow workers.
  * `WORKER_CPU`: the number of CPUs for a worker, in vCPU units.
  * `WORKER_MEMORY`: the amount of memory for a worker, in GB.
  * `WORKER_STORAGE`: the disk size for a worker, in GB.



Example:
    
    
    // PATCH https://composer.googleapis.com/v1/projects/example-project/
    // locations/us-central1/environments/example-environment?updateMask=
    // config.workloadsConfig.worker.minCount,
    // config.workloadsConfig.worker.maxCount
    // config.workloadsConfig.worker.cpu,
    // config.workloadsConfig.worker.memoryGb,
    // config.workloadsConfig.worker.storageGB
    
    "config": {
      "workloadsConfig": {
        "worker": {
          "minCount": 2,
          "maxCount": 6,
          "cpu": 1,
          "memoryGb": 2,
          "storageGb": 2
        }
      }
    }
    

###  Terraform 

The following fields in the `workloads_config.worker` block control the Airflow worker parameters. Each worker uses the specified amount of resources.

  * `worker.min_count`: the number of Airflow workers that your environment must always run. The number of workers in your environment does not go below this number, even if a lower number of workers can handle the load.
  * `worker.max_count`: the maximum number of Airflow workers that your environment can run. The number of workers in your environment does not go above this number, even if a higher number of workers is required to handle the load.
  * `worker.cpu`: the number of CPUs for an Airflow worker.
  * The `worker.memory_gb`: the amount of memory for an Airflow worker.
  * The `worker.storage_gb`: the amount of disk space for an Airflow worker.


    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "ENVIRONMENT_NAME"
      region = "LOCATION"
    
      config {
    
        workloads_config {
          worker {
            min_count = WORKERS_MIN
            max_count = WORKERS_MAX
            cpu = WORKER_CPU
            memory_gb = WORKER_MEMORY
            storage_gb = WORKER_STORAGE
          }
        }
    
      }
    }
    

Replace the following:

  * `ENVIRONMENT_NAME`: the name of the environment.
  * `LOCATION`: the region where the environment is located.
  * `WORKERS_MIN`: the minimum number of Airflow workers.
  * `WORKERS_MAX`: the maximum number of Airflow workers.
  * `WORKER_CPU`: the number of CPUs for a worker, in vCPU units.
  * `WORKER_MEMORY`: the amount of memory for a worker, in GB.
  * `WORKER_STORAGE`: the disk size for a worker, in GB.



Example:
    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "example-environment"
      region = "us-central1"
    
      config {
    
        workloads_config {
          worker {
            min_count = 2
            max_count = 6
            cpu = 1
            memory_gb = 2
            storage_gb = 2
          }
        }
    
      }
    }
    

## Adjust scheduler parameters

Your environment can run more than one Airflow scheduler at the same time. Use multiple schedulers to distribute load between several scheduler instances for better performance and reliability.

You can have up to 3 schedulers in your environment.

When scaling schedulers, use the following considerations:

  * In Managed Airflow (Gen 3) environments, Airflow DAG processors run as separate environment components from schedulers. Because DAG processor offloads the parsing of DAGs from the scheduler, you might want to redistribute resources previously allocated to Airflow schedulers.

Because schedulers don't parse DAGs in Managed Airflow (Gen 3), they have lower resource limits for CPU and memory than in Managed Airflow (Gen 2).



  * Increasing the number of schedulers doesn't always improve Airflow performance.

For example, this might happen when the extra scheduler isn't utilized, and consumes resources of your environment without contributing to the overall performance. The actual scheduler performance depends on the number of Airflow workers, the number of DAGs and tasks that run in your environment, and the configuration of both Airflow and the environment.

  * We recommend starting with two schedulers and then monitoring the performance of your environment. If you change the number of schedulers, you can always scale your environment back to the original number of schedulers. 




For more information about configuring multiple schedulers, see [Airflow documentation](https://airflow.apache.org/docs/apache-airflow/stable/concepts/scheduler.html#scheduler-tuneables).

You can specify the amount of CPUs, memory, and disk space used by Airflow schedulers in your environment. In this way, you can increase performance of your environment, in addition to horizontal scaling provided by using multiple schedulers.

**Note:** For information about possible values and limits for resources, see the Resource limits section.

###  Console 

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.

  3. Go to the **Environment configuration** tab.

  4. In the **Resources** > **Workloads configuration** item, click **Edit**.

  5. In the **Workloads configuration** pane adjust the parameters for Airflow schedulers:

     * In the **Number of schedulers** drop-down list, select the number of schedulers for your environment.

     * In the **CPU** , **Memory** , and **Storage** fields, specify the number of CPUs, memory, and storage for Airflow schedulers. Each scheduler uses the specified amount of resources.

  6. Click **Save**.




###  gcloud 

The following Airflow scheduler parameters are available:

  * `--scheduler-count`: the number of schedulers in your environment.

  * `--scheduler-cpu`: the number of CPUs for an Airflow scheduler.

  * `--scheduler-memory`: the amount of memory for an Airflow scheduler.

  * `--scheduler-storage`: the amount of disk space for an Airflow scheduler.




Run the following Google Cloud CLI command:
    
    
    gcloud composer environments update ENVIRONMENT_NAME \
      --location LOCATION \
      --scheduler-cpu SCHEDULER_CPU \
      --scheduler-memory SCHEDULER_MEMORY \
      --scheduler-storage SCHEDULER_STORAGE \
      --scheduler-count SCHEDULER_COUNT
    

Replace the following:

  * `ENVIRONMENT_NAME`: the name of the environment.
  * `LOCATION`: the region where the environment is located.

  * `SCHEDULER_CPU`: the number of CPUs for a scheduler, in vCPU units.

  * `SCHEDULER_MEMORY`: the amount of memory for a scheduler.

  * `SCHEDULER_STORAGE`: the disk size for a scheduler.

  * `SCHEDULER_COUNT`: the number of schedulers.


**Note:** The specified value for memory and disk space must be a whole number followed by a size unit of `KB` for kilobyte, `MB` for megabyte, or `GB` for gigabyte. The default size unit is `GB`. For example, `10GB` produces a 10 gigabyte storage.

Example:
    
    
    gcloud composer environments update example-environment \
      --location us-central1 \
      --scheduler-cpu 0.5 \
      --scheduler-memory 2.5 \
      --scheduler-storage 2 \
      --scheduler-count 2
    

###  API 

  1. Construct an [`environments.patch`](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments/patch) API request.

  2. In this request:

     1. In the `updateMask` parameter, specify the `config.workloadsConfig.scheduler` mask to update all scheduler parameters or only the number of schedulers. You can also update individual scheduler parameters except `count` by specifying a mask. For example, `config.workloadsConfig.scheduler.cpu`.

     2. In the request body, specify the new scheduler parameters.



    
    
    "config": {
      "workloadsConfig": {
        "scheduler": {
          "cpu": SCHEDULER_CPU,
          "memoryGb": SCHEDULER_MEMORY,
          "storageGb": SCHEDULER_STORAGE,
          "count": SCHEDULER_COUNT
        }
      }
    }
    

Replace the following:

  * `ENVIRONMENT_NAME`: the name of the environment.
  * `LOCATION`: the region where the environment is located.

  * `SCHEDULER_CPU`: the number of CPUs for a scheduler, in vCPU units.

  * `SCHEDULER_MEMORY`: the amount of memory for a scheduler, in GB.

  * `SCHEDULER_STORAGE`: the disk size for a scheduler, in GB.

  * `SCHEDULER_COUNT`: the number of schedulers.




Example:
    
    
    // PATCH https://composer.googleapis.com/v1/projects/example-project/
    // locations/us-central1/environments/example-environment?updateMask=
    // config.workloadsConfig.scheduler
    
    "config": {
      "workloadsConfig": {
        "scheduler": {
          "cpu": 0.5,
          "memoryGb": 2.5,
          "storageGb": 2,
          "count": 2
        }
      }
    }
    

###  Terraform 

The following fields in the `workloads_config.scheduler` block control the Airflow scheduler parameters. Each scheduler uses the specified amount of resources.

  * `scheduler.count`: the number of schedulers in your environment.

  * `scheduler.cpu`: the number of CPUs for an Airflow scheduler.

  * `scheduler.memory_gb`: the amount of memory for an Airflow scheduler.

  * `scheduler.storage_gb`: the amount of disk space for a scheduler.



    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "ENVIRONMENT_NAME"
      region = "LOCATION"
    
      config {
    
        workloads_config {
          scheduler {
            cpu = SCHEDULER_CPU
            memory_gb = SCHEDULER_MEMORY
            storage_gb = SCHEDULER_STORAGE
            count = SCHEDULER_COUNT
          }
        }
    
      }
    }
    

Replace the following:

  * `ENVIRONMENT_NAME`: the name of the environment.
  * `LOCATION`: the region where the environment is located.

  * `SCHEDULER_CPU`: the number of CPUs for a scheduler, in vCPU units.

  * `SCHEDULER_MEMORY`: the amount of memory for a scheduler, in GB.

  * `SCHEDULER_STORAGE`: the disk size for a scheduler, in GB.

  * `SCHEDULER_COUNT`: the number of schedulers.




Example:
    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "example-environment"
      region = "us-central1"
    
      config {
    
        workloads_config {
          scheduler {
            
            cpu = 0.5
            memory_gb = 1.875
            storage_gb = 1
            
            count = 2
          }
        }
    
      }
    }
    

## Adjust triggerer parameters

You can set the number of triggerers to zero, but you need at least one triggerer instance in your environment (or at least two in highly resilient environments), to use [deferrable operators in your DAGs](https://docs.cloud.google.com/composer/docs/composer-2/use-deferrable-operators).

Depending on your environment's [resilience mode](https://docs.cloud.google.com/composer/docs/composer-3/set-up-highly-resilient-environments), there are different possible configurations for the number of triggerers:

  * Standard resilience: you can run up to 10 triggerers.
  * High resilience: at least 2 triggerers, up to a maximum of 10 triggerers.



Even if the number of triggerers is set to zero, a triggerer pod definition is created and visible in your environment's cluster, but no actual triggerer workloads are run.

You can also specify the amount of CPUs, memory, and disk space used by Airflow triggerers in your environment. In this way, you can increase performance of your environment, in addition to horizontal scaling provided by using multiple triggerers.

**Note:** For information about possible values and limits for resources, see the Resource limits section.

###  Console 

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.

  3. Go to the **Environment configuration** tab.

  4. In the **Resources** > **Workloads configuration** item, click **Edit**.

  5. In the **Workloads configuration** pane adjust the parameters for Airflow triggerers:

     1. In the **Triggerer** section, in the **Number of triggerers** field, enter the number of triggerers in your environment.

If you set at least one triggerer for your environment, also use the the **CPU** , and **Memory** fields to configure resource allocation for your triggerers.

     2. In the **CPU** and **Memory** , specify the number of CPUs, memory, and storage for Airflow triggerers. Each triggerer uses the specified amount of resources.

  6. Click **Save**.




###  gcloud 

The following Airflow triggerer parameters are available:

**Caution:** Always use all three arguments: `--triggerer-cpu`, `--triggerer-memory`, and `--triggerer-count`. If you omit a parameter, its current value **is reset to the default** : `0.5` vCPU, `1 (2 in Airflow 3)` GB memory, or the number of triggerers for your environment's resilience mode. 

  * `--triggerer-count`: the number of triggerers in your environment.

    * For standard resilience environments, use a value between `0` and `10`.
    * For highly resilient environments, use `0`, or a value between `2` and `10`.
  * `--triggerer-cpu`: the number of CPUs for an Airflow triggerer.

  * `--triggerer-memory`: the amount of memory for an Airflow triggerer.




Run the following Google Cloud CLI command:
    
    
    gcloud composer environments update ENVIRONMENT_NAME \
      --location LOCATION \
      --triggerer-count TRIGGERER_COUNT \
      --triggerer-cpu TRIGGERER_CPU \
      --triggerer-memory TRIGGERER_MEMORY
    

Replace the following:

  * `ENVIRONMENT_NAME`: the name of the environment.
  * `LOCATION`: the region where the environment is located.
  * `TRIGGERER_COUNT`: the number of triggerers.
  * `TRIGGERER_CPU`: the number of CPUs for a triggerer, in vCPU units.
  * `TRIGGERER_MEMORY`: the amount of memory for a triggerer.

**Note:** The specified value for memory and disk space must be a whole number followed by a size unit of `KB` for kilobyte, `MB` for megabyte, or `GB` for gigabyte. The default size unit is `GB`. For example, `10GB` produces a 10 gigabyte storage.

Examples:

  * Scale to four triggerer instances:


    
    
    gcloud composer environments update example-environment \
      --location us-central1 \
      --triggerer-count 4 \
      --triggerer-cpu 1 \
      --triggerer-memory 1
    

  * Disable triggerers by setting triggerer count to `0`. This operation doesn't require specifying CPU or memory for the triggerers.


    
    
    gcloud composer environments update example-environment \
      --location us-central1 \
      --triggerer-count 0
    

###  API 

  1. In the `updateMask` query parameter, specify the `config.workloadsConfig.triggerer` mask.

  2. In the request body, specify all three parameters for triggerers.



    
    
    "config": {
      "workloadsConfig": {
        "triggerer": {
          "count": TRIGGERER_COUNT,
          "cpu": TRIGGERER_CPU,
          "memoryGb": TRIGGERER_MEMORY
        }
      }
    }
    

Replace the following:

  * `TRIGGERER_COUNT`: the number of triggerers.

    * For standard resilience environments, use a value between `0` and `10`.
    * For highly resilient environments, use `0`, or a value between `2` and `10`.
  * `TRIGGERER_CPU`: the number of CPUs for a triggerer, in vCPU units.

  * `TRIGGERER_MEMORY`: the amount of memory for a triggerer.




Examples:

  * Disable triggerers by setting triggerer count to `0`. This operation doesn't require specifying CPU or memory for the triggerers.


    
    
    // PATCH https://composer.googleapis.com/v1/projects/example-project/
    // locations/us-central1/environments/example-environment?updateMask=
    // config.workloadsConfig.triggerer
    "config": {
      "workloadsConfig": {
        "triggerer": {
          "count": 0
        }
      }
    }
    

  * Scale to four triggerer instances:


    
    
    // PATCH https://composer.googleapis.com/v1/projects/example-project/
    // locations/us-central1/environments/example-environment?updateMask=
    // config.workloadsConfig.triggerer
    "config": {
      "workloadsConfig": {
        "triggerer": {
          "count": 4,
          "cpu": 1,
          "memoryGb": 1
        }
      }
    }
    

###  Terraform 

The following fields in the `workloads_config.triggerer` block control the Airflow triggerer parameters. Each triggerer uses the specified amount of resources.

  * `triggerer.count`: the number of triggerers in your environment.

    * For standard resilience environments, use a value between `0` and `10`.
    * For highly resilient environments, use `0`, or a value between `2` and `10`.
  * `triggerer.cpu`: the number of CPUs for an Airflow triggerer.

  * `triggerer.memory_gb`: the amount of memory for an Airflow triggerer.



    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "ENVIRONMENT_NAME"
      region = "LOCATION"
    
      config {
    
        workloads_config {
          triggerer {
            count = TRIGGERER_COUNT
            cpu = TRIGGERER_CPU
            memory_gb = TRIGGERER_MEMORY
          }
        }
    
      }
    }
    

Replace the following:

  * `ENVIRONMENT_NAME`: the name of the environment.
  * `LOCATION`: the region where the environment is located.
  * `TRIGGERER_COUNT`: the number of triggerers.
  * `TRIGGERER_CPU`: the number of CPUs for a triggerer, in vCPU units.
  * `TRIGGERER_MEMORY`: the amount of memory for a triggerer, in GB.



Example:
    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "example-environment"
      region = "us-central1"
    
      config {
    
        workloads_config {
          triggerer {
            count = 1
            cpu = 0.5
            memory_gb = 0.5
          }
        }
    
      }
    }
    

## Adjust DAG processor parameters

You can specify the number of DAG processors in your environment and the amount of CPUs, memory, and disk space used by each DAG processor. In Managed Airflow (Gen 3) environments, the Airflow DAG processor runs as a separate environment component.

Depending on your environment's [resilience mode](https://docs.cloud.google.com/composer/docs/composer-3/set-up-highly-resilient-environments), there are different possible configurations for the number of DAG processors:

  * Standard resilience: you can run up to 3 DAG processors.
  * High resilience: at least 2 DAG processors, up to a maximum of 3 DAG processors.

**Note:** For information about possible values and limits for resources, see the Resource limits section.

###  Console 

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.

  3. Go to the **Environment configuration** tab.

  4. In the **Resources** > **Workloads configuration** item, click **Edit**.

  5. In the **Workloads configuration** pane adjust the parameters for Airflow DAG processors:

     * In the **Number of DAG processors** drop-down list, select the number of DAG processors for your environment.

Highly resilient environments require at least two DAG processors.

     * In the **CPU** , **Memory** , and **Storage** fields, specify the number of CPUs, memory, and storage for Airflow DAG processors. Each DAG processor uses the specified amount of resources.

  6. Click **Save**.




###  gcloud 

The following Airflow DAG processor parameters are available:

  * `--dag-processor-count`: the number of DAG processors.



Highly resilient environments require at least two DAG processors.

  * `--dag-processor-cpu`: the number of CPUs for the DAG processor.
  * `--dag-processor-memory`: the amount of memory for the DAG processor.
  * `--dag-processor-storage`: the amount of disk space for the DAG processor.



Run the following Google Cloud CLI command:
    
    
    gcloud composer environments update ENVIRONMENT_NAME \
      --location LOCATION \
        --dag-processor-count DAG_PROCESSOR_COUNT \
        --dag-processor-cpu DAG_PROCESSOR_CPU \
        --dag-processor-memory DAG_PROCESSOR_MEMORY \
        --dag-processor-storage DAG_PROCESSOR_STORAGE
    

Replace the following:

  * `ENVIRONMENT_NAME`: the name of the environment.
  * `LOCATION`: the region where the environment is located.
  * `DAG_PROCESSOR_COUNT`: the number of DAG processors.
  * `DAG_PROCESSOR_CPU`: the number of CPUs for the DAG processor.
  * `DAG_PROCESSOR_MEMORY`: the amount of memory for the DAG processor.
  * `DAG_PROCESSOR_STORAGE`: the amount of disk space for the DAG processor.

**Note:** The specified value for memory and disk space must be a whole number followed by a size unit of `KB` for kilobyte, `MB` for megabyte, or `GB` for gigabyte. The default size unit is `GB`. For example, `10GB` produces a 10 gigabyte storage.

Example:
    
    
    gcloud composer environments update example-environment \
      --location us-central1 \
      --dag-processor-count 1 \
      --dag-processor-cpu 0.5 \
      --dag-processor-memory 2 \
      --dag-processor-storage 1
    

###  API 

  1. Construct an [`environments.patch`](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments/patch) API request.

  2. In this request:

     1. In the `updateMask` parameter, specify the `config.workloadsConfig.dagProcessor` mask to update all DAG processor parameters including the number of DAG processors. You can also update individual DAG processor parameters by specifying a mask. For example, `config.workloadsConfig.dagProcessor.cpu,config.workloadsConfig.dagProcessor.memoryGb,config.workloadsConfig.dagProcessor.storageGb`. 

     2. In the request body, specify the new DAG processor parameters.



    
    
    "config": {
      "workloadsConfig": {
        "dagProcessor": {
          "count": DAG_PROCESSOR_COUNT,
          "cpu": DAG_PROCESSOR_CPU,
          "memoryGb": DAG_PROCESSOR_MEMORY,
          "storageGb": DAG_PROCESSOR_STORAGE
        }
      }
    }
    

Replace the following:

  * `ENVIRONMENT_NAME`: the name of the environment.
  * `LOCATION`: the region where the environment is located.
  * `DAG_PROCESSOR_COUNT`: the number of DAG processors.
  * `DAG_PROCESSOR_CPU`: the number of CPUs for the DAG processor, in vCPU units.
  * `DAG_PROCESSOR_MEMORY`: the amount of memory for the DAG processor, in GB.
  * `DAG_PROCESSOR_STORAGE`: the amount of disk space for the DAG processor, in GB.



Example:
    
    
    // PATCH https://composer.googleapis.com/v1/projects/example-project/
    // locations/us-central1/environments/example-environment?updateMask=
    // config.workloadsConfig.dagProcessor
    
    "config": {
      "workloadsConfig": {
        "scheduler": {
          "count": 2
          "cpu": 0.5,
          "memoryGb": 2.5,
          "storageGb": 2
        }
      }
    }
    

###  Terraform 

The following fields in the `workloads_config.dag_processor` block control the Airflow DAG processor parameters. Each DAG processor uses the specified amount of resources.

  * `dag_processor.count`: the number of DAG processors in your environment.
  * `dag_processor.cpu`: the number of CPUs for a DAG processor.
  * `dag_processor.memory_gb`: the amount of memory for a DAG processor.
  * `dag_processor.storage_gb` the amount of disk space for a DAG processor.


    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "ENVIRONMENT_NAME"
      region = "LOCATION"
    
      config {
    
        workloads_config {
          dag_processor {
            count = DAG_PROCESSOR_COUNT
            cpu = DAG_PROCESSOR_CPU
            memory_gb = DAG_PROCESSOR_MEMORY
            storage_gb = DAG_PROCESSOR_STORAGE
          }
        }
    
      }
    }
    

Replace the following:

  * `ENVIRONMENT_NAME`: the name of the environment.
  * `LOCATION`: the region where the environment is located.
  * `DAG_PROCESSOR_COUNT`: the number of DAG processors.
  * `DAG_PROCESSOR_CPU`: the number of CPUs for the DAG processor, in vCPU units.
  * `DAG_PROCESSOR_MEMORY`: the amount of memory for the DAG processor, in GB.
  * `DAG_PROCESSOR_STORAGE`: the amount of disk space for the DAG processor, in GB.



Example:
    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "example-environment"
      region = "us-central1"
    
      config {
    
        workloads_config {
          dag_processor {
            count = 1
            cpu = 0.5
            memory_gb = 2
            storage_gb = 1
          }
        }
    
      }
    }
    

## Adjust web server parameters

You can specify the amount of CPUs, memory, and disk space used by the Airflow web server in your environment. In this way, you can scale the performance of Airflow UI, for example, to match the demand coming from a large number of users or a large number of managed DAGs.

**Note:** For information about possible values and limits for resources, see the Resource limits section.

###  Console 

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.

  3. Go to the **Environment configuration** tab.

  4. In the **Resources** > **Workloads configuration** item, click **Edit**.

  5. In the **Workloads configuration** pane adjust the parameters for the web server. In the **CPU** , **Memory** , and **Storage** fields, specify the number of CPUs, memory, and storage for the web server.

  6. Click **Save**.




###  gcloud 

The following Airflow web server parameters are available:

  * `--web-server-cpu`: the number of CPUs for the Airflow web server.
  * `--web-server-memory`: the amount of memory for the Airflow web server.
  * `--web-server-storage`: the amount of disk space for the Airflow web server.



Run the following Google Cloud CLI command:
    
    
    gcloud composer environments update ENVIRONMENT_NAME \
      --location LOCATION \
      --web-server-cpu WEB_SERVER_CPU \
      --web-server-memory WEB_SERVER_MEMORY \
      --web-server-storage WEB_SERVER_STORAGE
    

Replace the following:

  * `ENVIRONMENT_NAME`: the name of the environment.
  * `LOCATION`: the region where the environment is located.
  * `WEB_SERVER_CPU`: the number of CPUs for web server, in vCPU units.
  * `WEB_SERVER_MEMORY`: the amount of memory for web server.
  * `WEB_SERVER_STORAGE`: the amount of memory for the web server.

**Note:** The specified value for memory and disk space must be a whole number followed by a size unit of `KB` for kilobyte, `MB` for megabyte, or `GB` for gigabyte. The default size unit is `GB`. For example, `10GB` produces a 10 gigabyte storage.

Example:
    
    
    gcloud composer environments update example-environment \
      --location us-central1 \
      --web-server-cpu 1 \
      --web-server-memory 2.5 \
      --web-server-storage 2
    

###  API 

  1. Construct an [`environments.patch`](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments/patch) API request.

  2. In this request:

     1. In the `updateMask` parameter, specify the `config.workloadsConfig.webServer` mask to update all web server parameters. You can also update individual web server parameters by specifying a mask for those arameters: `config.workloadsConfig.webServer.cpu`, `config.workloadsConfig.webServer.memoryGb`, `config.workloadsConfig.webServer.storageGb`.

     2. In the request body, specify the new web server parameters.



    
    
    "config": {
      "workloadsConfig": {
        "webServer": {
          "cpu": WEB_SERVER_CPU,
          "memoryGb": WEB_SERVER_MEMORY,
          "storageGb": WEB_SERVER_STORAGE
        }
      }
    }
    

Replace the following:

  * `ENVIRONMENT_NAME`: the name of the environment.
  * `LOCATION`: the region where the environment is located.
  * `WEB_SERVER_CPU`: the number of CPUs for the web server, in vCPU units.
  * `WEB_SERVER_MEMORY`: the amount of memory for the web server, in GB.
  * `WEB_SERVER_STORAGE`: the disk size for the web server, in GB.



Example:
    
    
    // PATCH https://composer.googleapis.com/v1/projects/example-project/
    // locations/us-central1/environments/example-environment?updateMask=
    // config.workloadsConfig.webServer.cpu,
    // config.workloadsConfig.webServer.memoryGb,
    // config.workloadsConfig.webServer.storageGb
    
    "config": {
      "workloadsConfig": {
        "webServer": {
          "cpu": 0.5,
          "memoryGb": 2.5,
          "storageGb": 2
        }
      }
    }
    

###  Terraform 

The following fields in the `workloads_config.web_server` block control the web server parameters.

  * The `web_server.cpu`: the number of CPUs for the web server.
  * The `web_server.memory_gb`: the amount of memory for the web server.
  * The `web_server.storage_gb`: the amount of disk space for the web server.


    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "ENVIRONMENT_NAME"
      region = "LOCATION"
    
      config {
    
        workloads_config {
          web_server {
            cpu = WEB_SERVER_CPU
            memory_gb = WEB_SERVER_MEMORY
            storage_gb = WEB_SERVER_STORAGE
          }
        }
    
      }
    }
    

Replace the following:

  * `ENVIRONMENT_NAME`: the name of the environment.
  * `LOCATION`: the region where the environment is located.
  * `WEB_SERVER_CPU`: the number of CPUs for the web server, in vCPU units.
  * `WEB_SERVER_MEMORY`: the amount of memory for the web server, in GB.
  * `WEB_SERVER_STORAGE`: the disk size for the web server, in GB.



Example:
    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "example-environment"
      region = "us-central1"
    
      config {
    
        workloads_config {
          web_server {
            cpu = 0.5
            memory_gb = 1.875
            storage_gb = 1
          }
        }
    
      }
    }
    

## Adjust the environment size

The environment size controls the performance parameters of the managed Managed Airflow infrastructure that includes, for example, the Airflow database.

Consider selecting a larger environment size if you want to run a large number of DAGs and tasks.

**Note:** Environment size is different from the environment presets. Environment presets, which you can select when you create an environment, determine all limits, scale, and performance parameters of your environment, including the environment size. Environment size determines only the performance parameters of the managed Managed Airflow infrastructure of your environment.

###  Console 

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.

  3. Go to the **Environment configuration** tab.

  4. In the **Resources** > **Workloads configuration** item, click **Edit**.

  5. In the **Resources** > **Core infrastructure** item, click **Edit**.

  6. In the **Core infrastructure** pane, in the **Environment size** field, specify the environment size.

  7. Click **Save**.




###  gcloud 

The `--environment-size` argument controls the environment size:
    
    
    gcloud composer environments update ENVIRONMENT_NAME \
        --location LOCATION \
        --environment-size ENVIRONMENT_SIZE
    

Replace the following:

  * `ENVIRONMENT_NAME`: the name of the environment.
  * `LOCATION`: the region where the environment is located.
  * `ENVIRONMENT_SIZE`: `small`, `medium`, `large`, `extra-large`.



Example:
    
    
    gcloud composer environments update example-environment \
        --location us-central1 \
        --environment-size medium
    

###  API 

  1. Create an [`environments.patch`](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments/patch) API request.

  2. In this request:

     1. In the `updateMask` parameter, specify the `config.environmentSize` mask.

     2. In the request body, specify the environment size.



    
    
      "config": {
        "environmentSize": "ENVIRONMENT_SIZE"
      }
    

Replace the following:

  * `ENVIRONMENT_SIZE`: the environment size: `ENVIRONMENT_SIZE_SMALL`, `ENVIRONMENT_SIZE_MEDIUM`, `ENVIRONMENT_SIZE_LARGE`, `ENVIRONMENT_SIZE_EXTRA_LARGE`.



Example:
    
    
    // PATCH https://composer.googleapis.com/v1/projects/example-project/
    // locations/us-central1/environments/example-environment?updateMask=
    // config.environmentSize
    
    "config": {
      "environmentSize": "ENVIRONMENT_SIZE_MEDIUM"
    }
    

###  Terraform 

The `environment_size` field in the `config` block controls the environment size:
    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "ENVIRONMENT_NAME"
      region = "LOCATION"
    
      config {
    
        environment_size = "ENVIRONMENT_SIZE"
    
      }
    }
    

Replace the following:

  * `ENVIRONMENT_NAME`: the name of the environment.
  * `LOCATION`: the region where the environment is located.
  * `ENVIRONMENT_SIZE`: the environment size: `ENVIRONMENT_SIZE_SMALL`, `ENVIRONMENT_SIZE_MEDIUM`, `ENVIRONMENT_SIZE_LARGE`, `ENVIRONMENT_SIZE_EXTRA_LARGE`.



Example:
    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "example-environment"
      region = "us-central1"
    
      config {
    
        environment_size = "ENVIRONMENT_SIZE_SMALL"
    
        }
      }
    }
    

## What's next

  * [Environment scaling and performance](https://docs.cloud.google.com/composer/docs/composer-3/environment-scaling)
  * [Managed Airflow pricing](https://docs.cloud.google.com/composer/pricing)
  * [Update environments](https://docs.cloud.google.com/composer/docs/composer-3/update-environments)
  * [Environment architecture](https://docs.cloud.google.com/composer/docs/composer-3/environment-architecture)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
