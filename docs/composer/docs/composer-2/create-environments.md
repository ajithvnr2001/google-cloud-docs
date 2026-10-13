---
url: https://docs.cloud.google.com/composer/docs/composer-2/create-environments/
title: Create Managed Service for Apache Airflow environments \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:38:00.860039+00:00
---

# Create Managed Service for Apache Airflow environments  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-2/create-environments/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 2 Guides ](https://docs.cloud.google.com/composer/docs/composer-2/composer-overview)



Send feedback 

#  Create Managed Service for Apache Airflow environments Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/create-environments "View this page for Managed Airflow \(Gen 3\)") | **Managed Airflow (Gen 2)** | [Managed Airflow (Legacy Gen 1)](https://docs.cloud.google.com/composer/docs/composer-1/create-environments "View this page for Managed Airflow \(Legacy Gen 1\)")

This page explains how to create a Managed Airflow environment.

  * For more information about environments, see [Environment architecture](https://docs.cloud.google.com/composer/docs/composer-2/environment-architecture).
  * For more information about creating an environment with Terraform, see [Create environments (Terraform)](https://docs.cloud.google.com/composer/docs/composer-2/terraform-create-environments).



## Before you begin

  * [Enable the Cloud Composer API](https://docs.cloud.google.com/composer/docs/composer-2/enable-composer-service). For the full list of services used by Managed Airflow, see [Services required by Managed Airflow](https://docs.cloud.google.com/composer/docs/composer-2/enable-composer-service#required-services).

  * Enable the [service group with APIs required by Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/enable-composer-service#enable-gen-2-dependencies).

  * The approximate time to create an environment is 25 minutes.

  * If you create an environment with Terraform, the service account used by Terraform must [have a role](https://docs.cloud.google.com/composer/docs/composer-2/access-control#service-account) with the `composer.environments.create` permission enabled.

For more information about the service account for Terraform, see [Google Provider Configuration Reference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/guides/provider_reference#credentials).

For more information about using Terraform to create a Managed Airflow environment, see [Terraform documentation](https://www.terraform.io/docs/providers/google/r/composer_environment).

For more information about additional parameters, see [Terraform Argument Reference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/composer_environment#argument-reference---cloud-composer-2).

  * **Private IP** : There are specific network and peering requirements to create a Private IP environment. For more information, see [Configuring private IP](https://docs.cloud.google.com/composer/docs/composer-2/configure-private-ip).

  * **Shared VPC** : There are specific network requirements to use Shared VPC with Managed Airflow. For information, see [Configuring shared VPC](https://docs.cloud.google.com/composer/docs/composer-2/configure-shared-vpc).

  * **VPC SC** : To deploy Managed Airflow environments inside a security perimeter, see [Configuring VPC SC](https://docs.cloud.google.com/composer/docs/composer-2/configure-vpc-sc). When used with Managed Airflow, VPC Service Controls have several [known limitations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#composer).

  * You might notice [Compute Engine metadata](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips#project-metadata) entries for the GKE clusters that belong to environments in your project. During GKE cluster creation and upgrades, Google Kubernetes Engine automatically adds project-level metadata entries (`google_compute_project_metadata`) to track secondary IP address range usage. Don't modify or remove these entries. Google Kubernetes Engine manages them automatically.


**Important:** For production use cases, we highly recommend to use highly resilient environments. The Airflow database of your environment is zonal. During a zonal outage, Airflow tasks that are executed in the affected zone are interrupted and marked as failed by Airflow. Highly resilient environments are more resilient to this issue, because their databases are located in two separate zones.

## Step 1. Create or choose an environment's service account

When you create an environment, you specify a service account. This service account is called _environment's service account_. Your environment uses this service account to perform most of the operations.

The service account for your environment is not a user account. A service account is a special kind of account used by an application or a virtual machine (VM) instance, not a person.

You can't change the service account of your environment later.

**Warning:** Your environment's service account can have **too broad permissions on your project**. Because your environment runs DAGs on behalf of your environment's service account, users who can add and modify DAGs in your environment's bucket or modify Artifact Registry repositories in your project **can run their code on behalf of the environment's service account** and **exercise all permissions of this account**. Make sure that you are familiar with [security considerations for environment's service accounts](https://docs.cloud.google.com/composer/docs/composer-2/access-control#service-account-security) and understand how this account interacts with permissions and roles that you grant to individual users in your project.

If you don't have a service account for Managed Airflow environments in your project yet, create it.

See [Create environments (Terraform)](https://docs.cloud.google.com/composer/docs/composer-2/terraform-create-environments) for an extended example of creating a service account for your environment in Terraform.

**Important:** You can use the same service account for more than one Managed Airflow environment. In this case, if you grant extra permissions to access resources in your project to this account, all environments that use it will get the same permissions.

To create a new service account for your environment:

  1. [Create a new service account](https://docs.cloud.google.com/iam/docs/service-accounts-create#creating) as described in the Identity and Access Management documentation.

  2. [Grant a role to it](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role), as described in the Identity and Access Management documentation. The required role is **Composer Worker** (`composer.worker`).

  3. If your environment [uses resource location restrictions](https://docs.cloud.google.com/composer/docs/composer-2/configure-resource-location-restrictions), or installs PyPI packages [from an Artifact Registry repository](https://docs.cloud.google.com/composer/docs/composer-2/install-python-dependencies#install-ar-repo) or [from a private repository](https://docs.cloud.google.com/composer/docs/composer-2/install-python-dependencies#install-private-repo), then grant the **Service Account User** (`iam.serviceAccountUser`) role to the **user-managed service account** that runs your environment on itself (both the principal and the resource are the same service account).

  4. To access other resources in your Google Cloud project, grant extra permissions to access those resources to this service account. The **Composer Worker** (`composer.worker`) role provides this required set of permissions in most cases. Add extra permissions to this service account only when it's necessary for the operation of your DAGs.




## Step 2. Basic setup

This step creates a Managed Airflow environment with default parameters in the specified location.

All other steps in this guide explain how to customize and configure different aspects of your environment. All of the remaining steps are optional.

###  Console 

  1. In the Google Cloud console, go to the **Create environment** page.

[Go to Create environment](https://console.cloud.google.com/composer/environments/create-composer-2)

  2. In the **Name** field, enter a name for your environment.

The name must start with a lowercase letter followed by up to 62 lowercase letters, numbers, or hyphens, and can't end with a hyphen. The environment name is used to create subcomponents for the environment, so you must provide a name that is also valid as a Cloud Storage bucket name. See [Bucket naming guidelines](https://docs.cloud.google.com/storage/docs/buckets#naming) for a list of restrictions. 

  3. In the **Location** drop-down list, choose a location for your environment.

A location is the region where the environment is located. 

  4. In the **Image version** drop-down list, select a [Managed Airflow image](https://docs.cloud.google.com/composer/docs/composer-versions#images) with the required version of Airflow.

  5. In the **Service account** drop-down list, select a service account for your environment.

If you don't have a service account for your environment yet, see Create or choose an environment's service account.




###  gcloud 
    
    
    gcloud composer environments create ENVIRONMENT_NAME \
        --location LOCATION \
        --image-version IMAGE_VERSION \
        --service-account "SERVICE_ACCOUNT"
    

**Important:** We are gradually rolling out a change that **switches the default version from Managed Airflow (Gen 2) to Managed Airflow (Gen 3)**. In some regions, if you don't specify an image version, a Managed Airflow (Gen 3) environment will be created. For more information about the rollout of this change, see [Release Notes](https://docs.cloud.google.com/composer/docs/release-notes). To address this change, we recommend to explicitly specify an image version for Managed Airflow (Gen 2). 

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.

The name must start with a lowercase letter followed by up to 62 lowercase letters, numbers, or hyphens, and can't end with a hyphen. The environment name is used to create subcomponents for the environment, so you must provide a name that is also valid as a Cloud Storage bucket name. See [Bucket naming guidelines](https://docs.cloud.google.com/storage/docs/buckets#naming) for a list of restrictions. 

  * `LOCATION` with the region for the environment.

A location is the region where the environment is located. 

  * `SERVICE_ACCOUNT` with the service account for your environment.

  * `IMAGE_VERSION` with the name of a Managed Airflow image.




Example:
    
    
    gcloud composer environments create example-environment \
        --location us-central1 \
        --image-version composer-2.17.14-airflow-2.11.1 \
        --service-account "
    example-account@example-project.iam.gserviceaccount.com
    "
    

###  API 

Construct an [`environments.create`](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments/create) API request. Specify the configuration in the [`Environment`](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments#Environment) resource.
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/environments/ENVIRONMENT_NAME",
      "config": {
        "softwareConfig": {
          "imageVersion": "IMAGE_VERSION"
        },
        "nodeConfig": {
          "serviceAccount": "SERVICE_ACCOUNT"
        }
      }
    }
    

**Important:** We are gradually rolling out a change that **switches the default version from Managed Airflow (Gen 2) to Managed Airflow (Gen 3)**. In some regions, if you don't specify an image version, a Managed Airflow (Gen 3) environment will be created. For more information about the rollout of this change, see [Release Notes](https://docs.cloud.google.com/composer/docs/release-notes). To address this change, we recommend to explicitly specify an image version for Managed Airflow (Gen 2). 

Replace:

  * `PROJECT_ID` with the [Project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

  * `LOCATION` with the region for the environment.

A location is the region where the environment is located. 

  * `ENVIRONMENT_NAME` with the environment name.

The name must start with a lowercase letter followed by up to 62 lowercase letters, numbers, or hyphens, and can't end with a hyphen. The environment name is used to create subcomponents for the environment, so you must provide a name that is also valid as a Cloud Storage bucket name. See [Bucket naming guidelines](https://docs.cloud.google.com/storage/docs/buckets#naming) for a list of restrictions. 

  * `IMAGE_VERSION` with the name of a Managed Airflow image.

  * `SERVICE_ACCOUNT` with the service account for your environment.




Example:
    
    
    // POST https://composer.googleapis.com/v1/{parent=projects/*/locations/*}/environments
    
    {
      "name": "projects/example-project/locations/us-central1/environments/example-environment",
      "config": {
        "softwareConfig": {
          "imageVersion": "composer-2.17.14-airflow-2.11.1"
        },
        "nodeConfig": {
          "serviceAccount": "
    example-account@example-project.iam.gserviceaccount.com
    "
        }
      }
    }
    

###  Terraform 

To create an environment with default parameters is a specified location, add the following resource block to your Terraform configuration and run `terraform apply`.
    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "ENVIRONMENT_NAME"
      region = "LOCATION"
    
      config {
        software_config {
          image_version = "IMAGE_VERSION"
        }
        node_config {
          service_account = "SERVICE_ACCOUNT"
        }
      }
    }
    

**Important:** We are gradually rolling out a change that **switches the default version from Managed Airflow (Gen 2) to Managed Airflow (Gen 3)**. In some regions, if you don't specify an image version, a Managed Airflow (Gen 3) environment will be created. For more information about the rollout of this change, see [Release Notes](https://docs.cloud.google.com/composer/docs/release-notes). To address this change, we recommend to explicitly specify an image version for Managed Airflow (Gen 2). 

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.

The name must start with a lowercase letter followed by up to 62 lowercase letters, numbers, or hyphens, and can't end with a hyphen. The environment name is used to create subcomponents for the environment, so you must provide a name that is also valid as a Cloud Storage bucket name. See [Bucket naming guidelines](https://docs.cloud.google.com/storage/docs/buckets#naming) for a list of restrictions. 

  * `LOCATION` with the region for the environment.

A location is the region where the environment is located. 

  * `IMAGE_VERSION` with the name of a Managed Airflow image.

  * `SERVICE_ACCOUNT` with the service account for your environment.




Example:
    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "example-environment"
      region = "us-central1"
    
      config {
        software_config {
          image_version = "composer-2.17.14-airflow-2.11.1"
        }
        node_config {
          service_account = "
    example-account@example-project.iam.gserviceaccount.com
    "
        }
      }
    }
    

## Step 3. Grant required permissions to Managed Airflow service account

When you enable Cloud Composer API in your project, the **Composer Service Agent** account is created in your project. Managed Airflow uses this account to perform operations in your Google Cloud project.

**Cloud Composer v2 API Service Agent Extension** role provides additional permissions to Managed Airflow Service Agent account. **This role is not granted automatically**. You must grant it manually.

**Warning:** After you grant these permissions, the Composer Service Agent account **can modify the IAM policy of your environment's service account**. For more information about the additional permissions, see [Grant roles to Managed Airflow Service Agent account](https://docs.cloud.google.com/composer/docs/composer-2/access-control#composer-sa).

###  Console 

When you create an environment in your project, if Managed Airflow Service Agent does not have required permissions on the environment's service account, then a **Grant required permissions to Cloud Composer service account** section appears.

You add Managed Airflow Service Agent account as a new principal on your environment's service account and grant the **Cloud Composer v2 API Service Agent Extension** role to it.

Confirm that you use the intended service account for your environment, and click **Grant**.

###  gcloud 

You add Managed Airflow Service Agent account as a new principal on your environment's service account and grant the **Cloud Composer v2 API Service Agent Extension** role to it.
    
    
    gcloud iam service-accounts add-iam-policy-binding \
        SERVICE_ACCOUNT \
        --member serviceAccount:service-PROJECT_NUMBER@cloudcomposer-accounts.iam.gserviceaccount.com \
        --role roles/composer.ServiceAgentV2Ext
    

Replace:

  * `SERVICE_ACCOUNT` with the service account for your environment.
  * `PROJECT_NUMBER` with the [Project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).



Example:
    
    
    gcloud iam service-accounts add-iam-policy-binding \
        example-account@example-project.iam.gserviceaccount.com \
        --member serviceAccount:service-00000000000@cloudcomposer-accounts.iam.gserviceaccount.com \
        --role roles/composer.ServiceAgentV2Ext
    
    

###  API 

To grant the role, you must modify the existing [allow policy](https://docs.cloud.google.com/guides/product-specific/iam/iam-terms) using the read-modify-write pattern:

  1. Read the existing allow policy for the service account of your environment.
  2. Modify it to include the `roles/composer.ServiceAgentV2Ext` role for the Managed Airflow Service Agent.
  3. Rewrite the existing allow policy.



For more information, see [Controlling access programmatically](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#programmatic).
    
    
    {
      "role": "roles/composer.ServiceAgentV2Ext",
      "members": [
        "serviceAccount:service-PROJECT_NUMBER@cloudcomposer-accounts.iam.gserviceaccount.com"
      ]
    }
    

Replace:

  * `PROJECT_NUMBER` with the [Project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).



Example:
    
    
    {
      "role": "roles/composer.ServiceAgentV2Ext",
      "members": [
        "serviceAccount:service-00000000000@cloudcomposer-accounts.iam.gserviceaccount.com"
      ]
    }
    

###  Terraform 

Add a new role binding to your environment's service account [allow policy](https://docs.cloud.google.com/guides/product-specific/iam/iam-terms).

You add Managed Airflow Service Agent account as a new principal on your environment's service account and grant the **Cloud Composer v2 API Service Agent Extension** role to it.

If you are not using Terraform to define your environment's service account allow policy, do not use the following example. Instead, add this binding using other methods.
    
    
    resource "google_service_account_iam_member" "custom_service_account" {
      provider = google-beta
      service_account_id = "SERVICE_ACCOUNT"
      role = "roles/composer.ServiceAgentV2Ext"
      member = "serviceAccount:service-PROJECT_NUMBER@cloudcomposer-accounts.iam.gserviceaccount.com"
    }
    

Replace:

  * `SERVICE_ACCOUNT` with the service account for your environment.
  * `PROJECT_NUMBER` with the [Project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).



Example:
    
    
    resource "google_service_account_iam_member" "custom_service_account" {
      provider = google-beta
      service_account_id = "example-account@example-project.iam.gserviceaccount.com"
      role = "roles/composer.ServiceAgentV2Ext"
      member = "serviceAccount:service-00000000000@cloudcomposer-accounts.iam.gserviceaccount.com"
    }
    

## Step 4. (Optional) Configure environment scale and performance parameters

To specify the scale and performance configuration for your environment, select the environment size and workloads configuration.

You can change all performance and scale parameters after you create an environment.

Following parameters control the scale and performance:

  * **Environment size**. Controls the performance parameters of the managed Managed Airflow infrastructure that includes the Airflow database. Consider selecting a larger environment size if you want to run a large number of DAGs and tasks with higher infrastructure performance. For example, larger environment's size increases the amount of Airflow task log entries that your environment can process with minimal delay.

  * **Workloads configuration**. Controls the scale and performance of Airflow components that run in a GKE cluster of your environment.

    * **Airflow scheduler**. Parses DAG definition files, schedules DAG runs based on the schedule interval, and queues tasks for execution by Airflow workers.

Your environment can run more than one Airflow scheduler at the same time. Use multiple schedulers to distribute load between several scheduler instances for better performance and reliability.

Increasing the number of schedulers does not always improve Airflow performance. For example, having only one scheduler might provide better performance than having two. This might happen when the extra scheduler is not utilized, and thus consumes resources of your environment without contributing to overall performance. The actual scheduler performance depends on the number of Airflow workers, the number of DAGs and tasks that run in your environment, and the configuration of both Airflow and the environment.

We recommend starting with two schedulers and then monitoring the performance of your environment. If you change the number of schedulers, you can always scale your environment back to the original number of schedulers.

For more information about configuring multiple schedulers, see [Airflow documentation](https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/scheduler.html#fine-tuning-your-scheduler-performance). 

    * **Airflow triggerer**. Asynchronously monitors all deferred tasks in your environment. If you have at least one triggerer instance in your environment (or at least two in highly resilient environments), you can use [deferrable operators in your DAGs](https://docs.cloud.google.com/composer/docs/composer-2/use-deferrable-operators).

In Managed Airflow (Gen 2), the Airflow triggerer is disabled by default. If you want to create an environment with a triggerer, set the number of triggerers to one or more.

    * **Airflow web server**. Runs the Airflow web interface where you can monitor, manage, and visualize your DAGs.

    * **Airflow workers**. Execute tasks that are scheduled by Airflow schedulers. The minimum and maximum number of workers in your environment changes dynamically depending on the number of tasks in the queue.


**Note:** When configuring resource limits for Airflow components, make sure that the limits exceed the minimum resource requirements for your usage scenario. [Sidecar containers](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/) that run alongside the main Airflow component's container utilize some of the allocated resources.

###  Console 

You can select a preset for your environment. When you select a preset, the scale and performance parameters for that preset are automatically selected. You also have an option to select a custom preset and specify all scale and performance parameters for your environment.

To select the scale and performance configuration for your environment, on the **Create environment** page:

  * To use predefined values, in the **Environment resources** section, click **Small** , **Medium** , **Large**.

  * To specify custom values for the scale and performance parameters:

    1. In the **Environment resources** section, click **Custom**.

    2. In the **Scheduler** section, set the number of schedulers you want to use, and the resource allocation for their CPU, memory, and storage.

    3. In the **Triggerer** section, use the **Number of triggerers** field to enter the number of triggerers in your environment.

If you don't want to [use deferrable operators in your DAGs](https://docs.cloud.google.com/composer/docs/composer-2/use-deferrable-operators), set the number of triggerers to zero. By default, the triggerer is disabled in Managed Airflow (Gen 2). 

If you set at least one triggerer for your environment, use the the **CPU** , and **Memory** fields to configure resource allocation for your triggerers.

    4. In the **DAG processor** section, specify the number of DAG processors in your environment and the amount of CPUs, memory, and storage for each DAG processor.

Highly resilient environments require at least two DAG processors.

    5. In the **Web server** section, specify the amount of CPUs, memory, and storage for the web server.

    6. In the **Worker** section, specify:

       * The minimum and maximum number of workers for autoscaling limits in your environment.
       * The CPU, memory, and storage allocation for your workers
    7. In the **Core infrastructure** section, in the **Environment size** drop-down list, select the environment size.




###  gcloud 

When you create an environment, the following arguments control the scale and performance parameters of your environment.

**Note:** If you omit an argument, Managed Airflow uses the default value.

  * `--environment-size` specifies the environment size.
  * `--scheduler-count` specifies the number of schedulers.
  * `--scheduler-cpu` specifies the number of CPUs for an Airflow scheduler.
  * `--scheduler-memory` specifies the amount of memory for an Airflow scheduler.
  * `--scheduler-storage` specifies the amount of disk space for an Airflow scheduler.

  * `--triggerer-count` specifies the number of Airflow triggerers in your environment. The default value for this flag is `0`. You need triggerers if you want to [use deferrable operators in your DAGs](https://docs.cloud.google.com/composer/docs/composer-2/use-deferrable-operators).

    * For standard resilience environments, use a value between `0` and `10`.
    * For highly resilient environments, use `0` or a value between `2` and `10`.
  * `--triggerer-cpu` specifies the number of CPUs for an Airflow triggerer, in vCPU units. Allowed values: `0.5`, `0.75`, `1`. The default value is `0.5`.

  * `--triggerer-memory` specifies the amount of memory for an Airflow triggerer, in GB. The default value is `0.5`.

The minimum required memory is equal to the number of CPUs allocated for the triggerers. The maximum allowed value is equal to the number of triggerer CPUs multiplied by 6.5.

For example, if you set the `--triggerer-cpu` flag to `1`, the **minimum value** for `--triggerer-memory` is `1` and the **maximum value** is `6.5`.

  * `--web-server-cpu` specifies the number of CPUs for the Airflow web server.

  * `--web-server-memory` specifies the amount of memory for the Airflow web server.

  * `--web-server-storage` specifies the amount of disk space for the Airflow web server.

  * `--worker-cpu` specifies the number of CPUs for an Airflow worker.

  * `--worker-memory` specifies the amount of memory for an Airflow worker.

  * `--worker-storage` specifies the amount of disk space for an Airflow worker.

  * `--min-workers` specifies the minimum number of Airflow workers. Your environment's cluster runs at least this number of workers.

  * `--max-workers` specifies the maximum number of Airflow workers. Your environment's cluster runs at most this number of workers.



    
    
    gcloud composer environments create ENVIRONMENT_NAME \
        --location LOCATION \
        --image-version composer-2.17.14-airflow-2.11.1 \
        --service-account "SERVICE_ACCOUNT" \
        --environment-size ENVIRONMENT_SIZE \
        --scheduler-count SCHEDULER_COUNT \
        --scheduler-cpu SCHEDULER_CPU \
        --scheduler-memory SCHEDULER_MEMORY \
        --scheduler-storage SCHEDULER_STORAGE \
        --triggerer-count TRIGGERER_COUNT \
        --triggerer-cpu TRIGGERER_CPU \
        --triggerer-memory TRIGGERER_MEMORY \
        --web-server-cpu WEB_SERVER_CPU \
        --web-server-memory WEB_SERVER_MEMORY \
        --web-server-storage WEB_SERVER_STORAGE \
        --worker-cpu WORKER_CPU \
        --worker-memory WORKER_MEMORY \
        --worker-storage WORKER_STORAGE \
        --min-workers WORKERS_MIN \
        --max-workers WORKERS_MAX
    

Replace:

  * `ENVIRONMENT_SIZE` with `small`, `medium`, `large`.
  * `SCHEDULER_COUNT` with the number of schedulers.
  * `SCHEDULER_CPU` with the number of CPUs for a scheduler, in vCPU units.
  * `SCHEDULER_MEMORY` with the amount of memory for a scheduler.
  * `SCHEDULER_STORAGE` with the disk size for a scheduler.
  * `TRIGGERER_COUNT` with the number of triggerers.
  * `TRIGGERER_CPU` with the number of CPUs for a triggerer, in vCPU units.
  * `TRIGGERER_MEMORY` with the amount of memory for a triggerer, in GB.

  * `WEB_SERVER_CPU` with the number of CPUs for the web server, in vCPU units.

  * `WEB_SERVER_MEMORY` with the amount of memory for the web server.

  * `WEB_SERVER_STORAGE` with the amount of memory for the web server.

  * `WORKER_CPU` with the number of CPUs for a worker, in vCPU units.

  * `WORKER_MEMORY` with the amount of memory for a worker.

  * `WORKER_STORAGE` with the disk size for a worker.

  * `WORKERS_MIN` with the minimum number of Airflow workers that your environment can run. The number of workers in your environment does not go above this number, even if a lower number of workers can handle the load.

  * `WORKERS_MAX` with the maximum number of Airflow workers that your environment can run. The number of workers in your environment does not go above this number, even if a higher number of workers is required to handle the load.


**Note:** The specified value for memory and disk space must be a whole number followed by a size unit of `KB` for kilobyte, `MB` for megabyte, or `GB` for gigabyte. The default size unit is `GB`. For example, `10GB` produces a 10 gigabyte storage.

Example:
    
    
    gcloud composer environments create example-environment \
        --location us-central1 \
        --image-version composer-2.17.14-airflow-2.11.1 \
        --service-account "
    example-account@example-project.iam.gserviceaccount.com
    " \
        --environment-size small \
        --scheduler-count 1 \
        --scheduler-cpu 0.5 \
        --scheduler-memory 2.5GB \
        --scheduler-storage 2GB \
        --triggerer-count 1 \
        --triggerer-cpu 0.5 \
        --triggerer-memory 0.5GB \
        --web-server-cpu 1 \
        --web-server-memory 2.5GB \
        --web-server-storage 2GB \
        --worker-cpu 1 \
        --worker-memory 2GB \
        --worker-storage 2GB \
        --min-workers 2 \
        --max-workers 4
    

###  API 

When you create an environment, in the [Environment](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments#Environment) > [EnvironmentConfig](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments#EnvironmentConfig) > [WorkloadsConfig](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments#WorkloadsConfig) resource, specify environment scale and performance parameters.
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/environments/ENVIRONMENT_NAME",
      "config": {
        "workloadsConfig": {
          "scheduler": {
            "cpu": SCHEDULER_CPU,
            "memoryGb": SCHEDULER_MEMORY,
            "storageGb": SCHEDULER_STORAGE,
            "count": SCHEDULER_COUNT
          },
          "triggerer": {
            "count": TRIGGERER_COUNT,
            "cpu": TRIGGERER_CPU,
            "memoryGb": TRIGGERER_MEMORY
          },
          "webServer": {
            "cpu": WEB_SERVER_CPU,
            "memoryGb": WEB_SERVER_MEMORY,
            "storageGb": WEB_SERVER_STORAGE
          },
          "worker": {
            "cpu": WORKER_CPU,
            "memoryGb": WORKER_MEMORY,
            "storageGb": WORKER_STORAGE,
            "minCount": WORKERS_MIN,
            "maxCount": WORKERS_MAX
          }
        },
        "environmentSize": "ENVIRONMENT_SIZE",
        "nodeConfig": {
          "serviceAccount": "SERVICE_ACCOUNT"
        }
      }
    }
    

Replace:

  * `SCHEDULER_CPU` with the number of CPUs for a scheduler, in vCPU units.
  * `SCHEDULER_MEMORY` with the amount of memory for a scheduler, in GB.
  * `SCHEDULER_STORAGE` with the disk size for a scheduler, in GB.
  * `SCHEDULER_COUNT` with the number of schedulers.

  * `TRIGGERER_COUNT` with the number of triggerers. The default value is `0`. You need triggerers if you want to [use deferrable operators in your DAGs](https://docs.cloud.google.com/composer/docs/composer-2/use-deferrable-operators).

    * For standard resilience environments, use a value between `0` and `10`.
    * For highly resilient environments, use `0` or a value between `2` and `10`.

If you use at least one triggerer, you must also specify the `TRIGGERER_CPU`, and `TRIGGERER_MEMORY` parameters:

  * `TRIGGERER_CPU` specifies the number of CPUs for a triggerer, in vCPU units. Allowed values: `0.5`, `0.75`, `1`.

  * `TRIGGERER_MEMORY` configures the amount of memory for a triggerer. The minimum required memory is equal to the number of CPUs allocated for the triggerers. The maximum allowed value is equal to the number of triggerer CPUs multiplied by 6.5.

For example, if you set the `TRIGGERER_CPU` to `1`, the **minimum value** for `TRIGGERER_MEMORY` is `1` and the **maximum value** is `6.5`.

  * `WEB_SERVER_CPU` with the number of CPUs for the web server, in vCPU units.

  * `WEB_SERVER_MEMORY` with the amount of memory for the web server, in GB.

  * `WEB_SERVER_STORAGE` with the disk size for the web server, in GB.

  * `WORKER_CPU` with the number of CPUs for a worker, in vCPU units.

  * `WORKER_MEMORY` with the amount of memory for a worker, in GB.

  * `WORKER_STORAGE` with the disk size for a worker, in GB.

  * `WORKERS_MIN` with the minimum number of Airflow workers that your environment can run. The number of workers in your environment does not go above this number, even if a lower number of workers can handle the load.

  * `WORKERS_MAX` with the maximum number of Airflow workers that your environment can run. The number of workers in your environment does not go above this number, even if a higher number of workers is required to handle the load.

  * `ENVIRONMENT_SIZE` with the environment size: `ENVIRONMENT_SIZE_SMALL`, `ENVIRONMENT_SIZE_MEDIUM`, `ENVIRONMENT_SIZE_LARGE`.




Example:
    
    
    // POST https://composer.googleapis.com/v1/{parent=projects/*/locations/*}/environments
    
    {
      "name": "projects/example-project/locations/us-central1/environments/example-environment",
      "config": {
        "workloadsConfig": {
          "scheduler": {
            "cpu": 2.5,
            "memoryGb": 2.5,
            "storageGb": 2,
            "count": 1
          },
          "triggerer": {
            "cpu": 0.5,
            "memoryGb": 0.5,
            "count": 1
          },
          "webServer": {
            "cpu": 1,
            "memoryGb": 2.5,
            "storageGb": 2
          },
          "worker": {
            "cpu": 1,
            "memoryGb": 2,
            "storageGb": 2,
            "minCount": 2,
            "maxCount": 4
          }
        },
        "environmentSize": "ENVIRONMENT_SIZE_SMALL",
        "nodeConfig": {
          "serviceAccount": "
    example-account@example-project.iam.gserviceaccount.com
    "
        }
      }
    }
    

###  Terraform 

When you create an environment, following arguments control the scale and performance parameters of your environment.

  * In the `config` block:

    * The `environment_size` field controls the environment size.
  * In the `workloads_config` block:

    * The `scheduler.cpu` field specifies the number of CPUs for an Airflow scheduler.
    * The `scheduler.memory_gb` field specifies the amount of memory for an Airflow scheduler.
    * The `scheduler.storage_gb` field specifies the amount of disk space for a scheduler.
    * The `scheduler.count` field specifies the number of schedulers in your environment.
    * The `triggerer.cpu` field specifies the number of CPUs for an Airflow triggerer.
    * The `triggerer.memory_gb` field specifies the amount of memory for an Airflow triggerer.
    * The `triggerer.count` field specifies the number of triggerers in your environment.

    * The `web_server.cpu` field specifies the number of CPUs for the Airflow web server.

    * The `web_server.memory_gb` field specifies the amount of memory for the Airflow web server.

    * The `web_server.storage_gb` field specifies the amount of disk space for the Airflow web server.

    * The `worker.cpu` field specifies the number of CPUs for an Airflow worker.

    * The `worker.memory_gb` field specifies the amount of memory for an Airflow worker.

    * The `worker.storage_gb` field specifies the amount of disk space for an Airflow worker.

    * The `worker.min_count` field specifies the minimum number of workers in your environment.

    * The `worker.max_count` field specifies the maximum number of workers in your environment.



    
    
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
          triggerer {
            count = TRIGGERER_COUNT
            cpu = TRIGGERER_CPU
            memory_gb = TRIGGERER_MEMORY
          }
          web_server {
            cpu = WEB_SERVER_CPU
            memory_gb = WEB_SERVER_MEMORY
            storage_gb = WEB_SERVER_STORAGE
          }
          worker {
            cpu = WORKER_CPU
            memory_gb = WORKER_MEMORY
            storage_gb = WORKER_STORAGE
            min_count = WORKERS_MIN
            max_count = WORKERS_MAX
          }
        }
    
        environment_size = "ENVIRONMENT_SIZE"
    
        node_config {
          service_account = "SERVICE_ACCOUNT"
        }
      }
    }
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `LOCATION` with the region where the environment is located.
  * `SERVICE_ACCOUNT` with the service account for your environment.
  * `SCHEDULER_CPU` with the number of CPUs for a scheduler, in vCPU units.
  * `SCHEDULER_MEMORY` with the amount of memory for a scheduler, in GB.
  * `SCHEDULER_STORAGE` with the disk size for a scheduler, in GB.
  * `SCHEDULER_COUNT` with the number of schedulers.
  * `TRIGGERER_COUNT` with the number of triggerers.
  * `TRIGGERER_CPU` with the number of CPUs for a triggerer, in vCPU units.
  * `TRIGGERER_MEMORY` with the amount of memory for a triggerer, in GB.

  * `WEB_SERVER_CPU` with the number of CPUs for the web server, in vCPU units.

  * `WEB_SERVER_MEMORY` with the amount of memory for the web server, in GB.

  * `WEB_SERVER_STORAGE` with the disk size for the web server, in GB.

  * `WORKER_CPU` with the number of CPUs for a worker, in vCPU units.

  * `WORKER_MEMORY` with the amount of memory for a worker, in GB.

  * `WORKER_STORAGE` with the disk size for a worker, in GB.

  * `WORKERS_MIN` with the minimum number of Airflow workers that your environment can run. The number of workers in your environment does not go above this number, even if a lower number of workers can handle the load.

  * `WORKERS_MAX` with the maximum number of Airflow workers that your environment can run. The number of workers in your environment does not go above this number, even if a higher number of workers is required to handle the load.

  * `ENVIRONMENT_SIZE` with the environment size: `ENVIRONMENT_SIZE_SMALL`, `ENVIRONMENT_SIZE_MEDIUM`, `ENVIRONMENT_SIZE_LARGE`.




Example:
    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "example-environment"
      region = "us-central1"
    
      config {
    
        workloads_config {
    
          scheduler {
            cpu = 2.5
            memory_gb = 2.5
            storage_gb = 2
            count = 1
          }
          triggerer {
            count = 1
            cpu = 0.5
            memory_gb = 0.5
          }
          dag_processor {
            cpu = 1
            memory_gb = 2
            storage_gb = 1
            count = 1
        }
          web_server {
            cpu = 1
            memory_gb = 2.5
            storage_gb = 2
          }
          worker {
            cpu = 1
            memory_gb = 2
            storage_gb = 2
            min_count = 2
            max_count = 4
          }
        }
    
        environment_size = "ENVIRONMENT_SIZE_SMALL"
    
        node_config {
          service_account = "
    example-account@example-project.iam.gserviceaccount.com
    "
        }
    
      }
    }
    

## Step 5. (Optional) Enable high resilience mode

[Highly resilient](https://docs.cloud.google.com/composer/docs/composer-2/set-up-highly-resilient-environments) (Highly Available) Managed Airflow environments are environments that use built-in redundancy and failover mechanisms that reduce the environment's susceptibility to zonal failures and single point of failure outages.

**Important:** We strongly recommend to **use highly resilient environments for production use cases**.

A highly resilient environment is multi-zonal and runs across at least two zones of a selected region. The following components run in separate zones:

  * Exactly two Airflow schedulers

  * At least two triggerers (if the number of triggerers isn't set to `0`)

  * Two web servers




The minimum number of workers is set to two, and your environment's cluster distributes worker instances between zones. In case of a zonal outage, affected worker instances are rescheduled in a different zone. The Cloud SQL component of a highly resilient environment has a primary instance and a standby instance that are distributed between zones.

**Important:** In Managed Airflow (Gen 2), highly resilient environments are available only for Private IP environments.

###  Console 

On the **Create environment** page:

  1. In the **Resilience mode** section, select **High resilience**.

  2. In the **Environment resources** section, select scale parameters for a highly resilient environment. Highly resilient environments require exactly two schedulers, zero or between two and ten triggerers, and at least two workers:

     1. Click **Custom**.

     2. In the **Number of schedulers** drop-down list, select `2`.

     3. In the **Number of triggerers** drop-down list, select `0`, or a value between `2` and `10`. Configure the **CPU** and **Memory** allocation for your triggerers.

     4. In the **Minimum number of workers** drop-down list, select `2` or more, depending on the required number of workers.

  3. In the **Network configuration** section:

     1. In the **Networking type** , select **Private IP environment**.

     2. If required, specify other networking parameters.




###  gcloud 

When you create an environment, the `--enable-high-resilience` argument enables the high resilience mode.

Set the following arguments:

  * `--enable-high-resilience`
  * `--enable-private-environment`, and other networking parameters for a Private IP environment, if required
  * `--scheduler-count` to `2`
  * `--triggerer-count` to `0` or a value between `2` and `10`. If you use triggerers, the `--triggerer-cpu and`\--triggerer-memory` flags are also required for environment creation.

For more information about `--triggerer-count`, `--triggerer-cpu`, and `--triggerer-memory` flags, see Configure environment scale and performance parameters.

  * `--min-workers` to `2` or more



    
    
    gcloud composer environments create ENVIRONMENT_NAME \
        --location LOCATION \
        --image-version composer-2.17.14-airflow-2.11.1 \
        --service-account "SERVICE_ACCOUNT" \
        --enable-high-resilience \
        --enable-private-environment \
        --scheduler-count 2 \
        --triggerer-count 2 \
        --triggerer-cpu 0.5 \
        --triggerer-memory 0.5 \
        --min-workers 2
    

###  API 

When you create an environment, in the [Environment](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments#Environment) > [EnvironmentConfig](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments#EnvironmentConfig) resource, enable the high resilience mode.
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/environments/ENVIRONMENT_NAME",
      "config": {
        "resilience_mode": "HIGH_RESILIENCE",
        "nodeConfig": {
          "serviceAccount": "SERVICE_ACCOUNT"
        }
    
      }
    }
    

Example:
    
    
    // POST https://composer.googleapis.com/v1/{parent=projects/*/locations/*}/environments
    
    {
      "name": "projects/example-project/locations/us-central1/environments/example-environment",
      "config": {
        "resilience_mode": "HIGH_RESILIENCE",
        "nodeConfig": {
          "serviceAccount": "
    example-account@example-project.iam.gserviceaccount.com
    "
        }
    
      }
    }
    

###  Terraform 

**Note:** An update to the resilience mode field causes a failure instead of leading to recreating the Managed Airflow environment.

When you create an environment, the `resilience_mode` field in the `config` block enables the high resilience mode.
    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "ENVIRONMENT_NAME"
      region = "LOCATION"
    
      config {
    
        resilience_mode = "HIGH_RESILIENCE"
    
        node_config {
          service_account = "SERVICE_ACCOUNT"
        }
    
      }
    }
    

Example:
    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "example-environment"
      region = "us-central1"
    
      config {
    
        resilience_mode = "HIGH_RESILIENCE"
    
        node_config {
          service_account = "
    example-account@example-project.iam.gserviceaccount.com
    "
        }
      }
    }
    

## Step 6. (Optional) Specify a zone for the environment's database

You can specify a preferred Cloud SQL zone when creating a standard resilience environment.

**Note:** If your environment uses high resilience mode, you can't specify a zone for the database. Instead, Managed Airflow automatically selects two zones in the region where the environment is located. If you enable high resilience for an existing environment with the preferred Cloud SQL zone, the preferred zone configuration is removed and two zones are selected automatically.

###  Console 

On the **Create environment** page:

  1. In the **Advanced configuration** section, expand the **Show advanced configuration** item.

  2. In the **Airflow database zone** list, select a preferred Cloud SQL zone.




###  gcloud 

When you create an environment, the `--cloud-sql-preferred-zone` argument specifies a preferred Cloud SQL zone.
    
    
    gcloud composer environments create ENVIRONMENT_NAME \
        --location LOCATION \
        --image-version composer-2.17.14-airflow-2.11.1 \
        --service-account "SERVICE_ACCOUNT" \
        --cloud-sql-preferred-zone SQL_ZONE
    

Replace the following:

  * `SQL_ZONE`: preferred Cloud SQL zone. This zone must be located in the region where the environment is located.



Example:
    
    
    gcloud composer environments create example-environment \
        --location us-central1 \
        --image-version composer-2.17.14-airflow-2.11.1 \
        --service-account "
    example-account@example-project.iam.gserviceaccount.com
    " \
        --cloud-sql-preferred-zone us-central1-a
    

###  API 

When you create an environment, in the [Environment](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments#Environment) > [DatabaseConfig](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments#DatabaseConfig) resource, specify the preferred Cloud SQL zone.
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/environments/ENVIRONMENT_NAME",
      "config": {
        "databaseConfig": {
          "zone": "SQL_ZONE"
        },
          "nodeConfig": {
          "serviceAccount": "SERVICE_ACCOUNT"
        }
      }
    }
    

Replace the following:

  * `SQL_ZONE`: preferred Cloud SQL zone. This zone must be located in the region where the environment is located.



Example:
    
    
    // POST https://composer.googleapis.com/v1/{parent=projects/*/locations/*}/environments
    
    {
      "name": "projects/example-project/locations/us-central1/environments/example-environment",
      "config": {
        "databaseConfig": {
          "zone": "us-central1-a"
        },
        "nodeConfig": {
          "serviceAccount": "
    example-account@example-project.iam.gserviceaccount.com
    "
        }
      }
    }
    

###  Terraform 

When you create an environment, the `zone` field in the `database_config` block specifies the preferred Cloud SQL zone.
    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "ENVIRONMENT_NAME"
      region = "LOCATION"
    
      config {
        database_config {
          zone = "SQL_ZONE"
        }
    
        node_config {
          service_account = "SERVICE_ACCOUNT"
        }
      }
    }
    

Replace the following:

  * `SQL_ZONE`: preferred Cloud SQL zone. This zone must be located in the region where the environment is located.



## Step 7. (Optional) Configure your environment's networking

Networking parameters depend on the type of environment that you want to create:

  * **Public IP environment**. Use the default networking parameters.

  * **Private IP environment (with PSC)**. In this configuration, your environment uses Private Service Connect for connectivity. 

Configure your Private IP environment:

    1. [Configure your project's networking for Private IP environments](https://docs.cloud.google.com/composer/docs/composer-2/configure-private-ip).
    2. [Configure Private Service Connect](https://docs.cloud.google.com/composer/docs/composer-2/configure-private-service-connect#creating-psc) when you create your environment.
    3. Specify other parameters for your Private IP environment, as described further in this section.

For a Private IP environment with PSC, you need to know:

    * Your VPC network ID
    * Your VPC subnetwork ID
    * Two secondary IP ranges in your VPC subnetwork:

      * Secondary IP range for pods
      * Secondary IP range for services
    * IP ranges for the components of the environment:

      * GKE Control Plane IP range. IP range for the GKE control plane.
      * Managed Airflow connection subnetwork. IP range for the Managed Airflow connection subnetwork.
  * **Private IP environment (VPC peerings)**. In this configuration, your environment uses VPC peerings for connectivity.

Configure your Private IP environment:

    1. [Configure your project's networking for Private IP environments](https://docs.cloud.google.com/composer/docs/composer-2/configure-private-ip).
    2. Specify other parameters for your Private IP environment, as described further in this section.

For a Private IP environment with VPC peerings, you need to know:

    * Your VPC network ID
    * Your VPC subnetwork ID
    * Two secondary IP ranges in your VPC subnetwork:

      * Secondary IP range for pods
      * Secondary IP range for services
    * IP ranges for the components of the environment: 

      * IP range for the GKE control plane.

      * IP range for VPC peering to export from the internal Managed Airflow network to the selected network. Managed Airflow infrastructure components use IP addresses from this range.

      * IP range for the Cloud SQL instance.

  * For a **Shared VPC environment** , you must do additional networking setup for the host project, then create a Public or a Private IP environment in a service project. Follow the instructions on the [Configuring Shared VPC](https://docs.cloud.google.com/composer/docs/composer-2/configure-shared-vpc) page.

**Important:** If you create an environment in the service project using Google Cloud console, then your account must have the `compute.subnetworks.use` permission in the host project. Otherwise, the list of available subnetworks does not contain subnetworks from the host project. If you create an environment using `gcloud`, API, or Terraform, then your account does not need this additional permission.

For a Shared VPC environment, you need to know:

    * Your host project VPC network ID
    * Your host project VPC subnetwork ID

    * Two secondary IP ranges in your host project VPC subnetwork:

      * Secondary IP range for pods
      * Secondary IP range for services

When creating a **Public IP Shared VPC environment** , you still need to specify your host project VPC network, subnetwork, and secondary IP ranges for pods and services.

  * To create a **VPC SC environment** , you must create a service perimeter and then create Private IP environments inside this perimeter. Follow the instructions outlined in [Configuring VPC Service Controls](https://docs.cloud.google.com/composer/docs/composer-2/configure-vpc-sc).

  * To create an environment with **Restricted Endpoint Usage** , you must have an already configured `constraints/gcp.restrictEndpointUsage` organization policy, and then create a new Managed Airflow (Gen 2) environment. Private IP environments require additional networking setup. Follow the instructions outlined in [Configure environments with Restrict Endpoint Usage policy](https://docs.cloud.google.com/composer/docs/composer-2/configure-restrict-endpoint-usage-environments).




Additional networking options for environments are:

  * **Privately used public IP addresses**. If you want to use more IP addresses, your environment can [privately use certain public IP address ranges](https://docs.cloud.google.com/composer/docs/composer-2/configure-privately-used-public-ip) as internal, subnet IP address ranges for pods and services.
  * **Authorized networks**. If you want to access the control plane of your Private IP environment using HTTPS, you can use [authorized networks](https://docs.cloud.google.com/composer/docs/composer-2/configure-authorized-networks) to specify CIDR ranges that can do so.
  * **IP Masquerade agent**. By using environments with the IP Masquerade agent, you can use many-to-one IP address translations in your environment's networking configurations. For more information about creating environments with IP Masquerade agent, see [Enable the IP Masquerade agent](https://docs.cloud.google.com/composer/docs/composer-2/enable-ip-masquerade-agent).



###  Console 

To create a Private IP environment:

  1. Make sure that your networking is configured for the type of environment that you want to create.

  2. In the **Network configuration** section, expand the **Show network configuration** item.

  3. In the **Network** drop-down list, select your VPC network ID.

  4. In the **Subnetwork** drop-down list, select your VPC subnetwork ID.

  5. In the **Secondary IP range for pods** section, select or specify the secondary IP range for pods. You can use an existing secondary range in your VPC network, or choose to use an auto-created range.

  6. In the **Secondary IP range for services** section, select or specify the secondary IP range for services. You can use an existing secondary range in your VPC network, or choose to use an auto-created range.

  7. In the **Networking type** section, select the **Private IP environment** option to create a Private IP environment.

  8. In the **Composer connectivity** section, select the networking type for your environment and specify IP ranges for environment components:

For an environment that uses Private Service Connect:

     1. Select **Private Service Connect** for an environment that uses [Private Service Connect](https://docs.cloud.google.com/composer/docs/composer-2/configure-private-service-connect).

     2. In the **Composer connection subnetwork** section specify an IP range for the Managed Airflow connection subnetwork. The address for the PSC endpoint is selected from this range. You can specify a custom range, or choose to use the default one.

For an environment that uses VPC peerings:

     1. Select **VPC peerings** for an environment that uses VPC peerings.

**Note:** Environments with VPC peerings [have more limitations](https://docs.cloud.google.com/composer/docs/composer-2/configure-private-ip#requirements) than environments with PSC.
     2. In the **IP range for Composer tenant network** section specify an IP range for the Managed Airflow tenant network. This network hosts the [SQL proxy component](https://docs.cloud.google.com/composer/docs/composer-2/environment-architecture) of your environment. You can specify a custom range, or choose to use the default one.

     3. In the **IP range for Cloud SQL network** section, specify an IP range for the Cloud SQL instance. You can specify a custom range, or choose to use the default one.

**Caution:** The `172.17.0.0/16` range [is reserved in Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/private-ip#network_issues).
  9. In the **IP range for GKE control plane network** section, specify an IP range for the GKE control plane:

     * To use the [default IP range](https://docs.cloud.google.com/composer/docs/composer-2/configure-private-ip#defaults) for the region where your environment is located, select **Default IP range**.

     * To specify a custom IP range, select **Custom IP range** and enter a range in the CIDR notation in the **GKE cluster master private IP** field.

  10. Select the level access for the GKE control plane. The control plane has two endpoints. One endpoint is private, for use by cluster nodes and VMs. Another endpoint is public. You can specify the level of access for the public endpoint:

     * To enable access to the public endpoint from authorized networks, select the **Access cluster control plane endpoint using its external IP address** checkbox.

Using this option sets the level of access for the control plane to ["Public endpoint access enabled, authorized networks enabled"](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/private-cluster-concept#overview). This provides restricted access to the control plane from authorized networks. By default, no source IP addresses are specified. You can add [authorized networks to the cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks#add).

     * To disable access to the public endpoint from authorized networks, clear the **Access cluster control plane endpoint using its external IP address** checkbox.

Using this option sets the level of access for the control plane to ["Public endpoint access disabled"](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/private-cluster-concept#overview). This prevents all internet access to the control plane.




###  gcloud 

Make sure that your networking is configured for the type of environment that you want to create.

When you create an environment, the following arguments control the networking parameters. If you omit a parameter, the default value is used.

  * `--enable-private-environment` enables a Private IP environment.

  * `--network` specifies your VPC network ID.

  * `--subnetwork` specifies your VPC subnetwork ID.

  * `--cluster-secondary-range-name` or `--cluster-ipv4-cidr` configures the the secondary range for pods.

  * `--services-secondary-range-name` or`--services-ipv4-cidr` to configure the secondary range for services.

  * `--master-ipv4-cidr` specifies a range for the GKE control plane.



  * _(Environments with PSC)_ `--connection-subnetwork` specifies a range for the Managed Airflow connection subnetwork, which hosts the PSC endpoint.

  * _(Environments with VPC peerings)_ `--connection-type=VPC_PEERING` specifies that an environment must use VPC peerings.

  * _(Environments with VPC peerings)_ `--composer-network-ipv4-cidr` specifies a range for the Managed Airflow tenant network. This network hosts the [SQL proxy component](https://docs.cloud.google.com/composer/docs/composer-2/environment-architecture) of your environment.

  * _(Environments with VPC peerings)_ `--cloud-sql-ipv4-cidr` specifies a range for the Cloud SQL instance.




  * `--enable-private-endpoint` controls the level access for the GKE control plane. The control plane has two endpoints. One endpoint is private, for use by cluster nodes and VMs. Another endpoint is public. You can specify the level of access for the public endpoint:

    * To enable access to the public endpoint from authorized networks, omit the `--enable-private-endpoint` argument.

Using this option sets the level of access for the control plane to ["Public endpoint access enabled, authorized networks enabled"](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/private-cluster-concept#overview). This provides restricted access to the control plane from authorized networks. By default, no source IP addresses are specified. You can add [authorized networks to the cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks#add).

    * To disable access to the public endpoint from authorized networks, specify the `--enable-private-endpoint` argument.

Using this option sets the level of access for the control plane to ["Public endpoint access disabled"](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/private-cluster-concept#overview). This prevents all internet access to the control plane.

  * `--enable-master-authorized-networks` and `--master-authorized-networks` arguments configure [authorized networks](https://docs.cloud.google.com/composer/docs/composer-2/configure-authorized-networks) for your environment.

  * `--enable-privately-used-public-ips` configures [privately used public IP addresses](https://docs.cloud.google.com/composer/docs/composer-2/configure-privately-used-public-ip) for your environment.

  * `--enable-ip-masq-agent` [enables the IP Masquerade agent](https://docs.cloud.google.com/composer/docs/composer-2/enable-ip-masquerade-agent).




Example (Private IP environment )
    
    
    gcloud composer environments create ENVIRONMENT_NAME \
        --location LOCATION \
        --image-version composer-2.17.14-airflow-2.11.1 \
        --service-account "SERVICE_ACCOUNT" \
        --enable-private-environment \
        --network NETWORK_ID \
        --subnetwork SUBNETWORK_ID \
        --cluster-ipv4-cidr PODS_RANGE \
        --services-ipv4-cidr SERVICES_RANGE \
        --master-ipv4-cidr CONTROL_PLANE_RANGE \
        --connection-subnetwork COMPOSER_PSC_RANGE \
    

Replace:

  * `NETWORK_ID` with your VPC network ID.
  * `SUBNETWORK_ID` with your VPC subnetwork ID.

  * `PODS_RANGE` with the secondary range for pods.

  * `SERVICES_RANGE` with the secondary range for services.

  * `CONTROL_PLANE_RANGE` with the secondary range for the GKE control plane.

  * `COMPOSER_PSC_RANGE` with the range for the Managed Airflow connection subnetwork. 




## Step 8. (Optional) Add network tags

Network [tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags) are applied to all node VMs in your environment's cluster. Tags are used to identify valid sources or targets for network firewalls. Each tag within the list must comply with [RFC 1035](https://www.ietf.org/rfc/rfc1035.txt).

For example, you might want to add network tags if you plan to restrict traffic for a Private IP environment with firewall rules.

**Caution:** You can't change network tags later. If you want to later configure firewall rules that target only VMs in your environment's cluster, specify network tags when you create your environment.

###  Console 

On the **Create environment** page:

  1. Locate the **Network configuration** section.
  2. In the **Network tags** field, enter network tags for your environment.



###  gcloud 

When you create an environment, following arguments control network tags:

  * `--tags` specifies a comma-separated list of network tags applied to all node VMs.


    
    
    gcloud composer environments create ENVIRONMENT_NAME \
        --location LOCATION \
        --image-version composer-2.17.14-airflow-2.11.1 \
        --service-account "SERVICE_ACCOUNT" \
        --tags TAGS
    

Replace:

  * `TAGS` with a comma-separated list of network tags.



Example:
    
    
    gcloud composer environments create example-environment \
        --location us-central1 \
        --image-version composer-2.17.14-airflow-2.11.1 \
        --tags group1,production
    

###  API 

When you create an environment, in the [Environment](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments#Environment) > [EnvironmentConfig](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments#EnvironmentConfig) resource, specify network tags for your environment.
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/environments/ENVIRONMENT_NAME",
      "config": {
        "nodeConfig": {
          "tags": [
            "TAG"
          ],
          "serviceAccount": "SERVICE_ACCOUNT"
        }
      }
    }
    

Replace:

  * `TAG` with a network tag.



Example:
    
    
    // POST https://composer.googleapis.com/v1/{parent=projects/*/locations/*}/environments
    
    {
      "name": "projects/example-project/locations/us-central1/environments/example-environment",
      "config": {
        "nodeConfig": {
          "tags": [
            "group1",
            "production"
          ],
          "serviceAccount": "
    example-account@example-project.iam.gserviceaccount.com
    "
        }
      }
    }
    

###  Terraform 

When you create an environment, following fields define network tags for your environment:

  * `tags` field in the `node_config` block specifies a comma-separated list of network tags applied to all node VMs.


    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "ENVIRONMENT_NAME"
      region = "LOCATION"
    
      config {
    
        node_config {
          tags = ["TAGS"]
          service_account = "SERVICE_ACCOUNT"
        }
      }
    }
    

Replace:

  * `TAGS` with a comma-separated list of network tags.



Example:
    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "example-environment"
      region = "us-central1"
    
      config {
        node_config {
          tags = ["group1","production"]
          service_account = "
    example-account@example-project.iam.gserviceaccount.com
    "
        }
      }
    }
    

## Step 9. (Optional) Configure web server network access

The Airflow web server access parameters do not depend on the type of your environment. Instead, you can configure web server access separately. For example, a Private IP environment can still have the Airflow UI accessible from the internet.

You can't configure the allowed IP ranges using private IP addresses.

**Caution:** In some cases, changes to the web server access parameters can take up to 10 minutes to propagate.

###  Console 

On the **Create environment** page:

  1. In the **Network configuration** section, expand the **Show network configuration** item.

  2. In the **Web server network access control** section:

     * To provide access to the Airflow web server from all IP addresses, select **Allow access from all IP addresses**.

     * To restrict access only to specific IP ranges, select **Allow access only from specific IP addresses**. In the **IP range** field, specify an IP range in the CIDR notation. In the **Description** field, specify an optional description for this range. If you want to specify more than one range, click **Add IP range**.

     * To forbid access for all IP addresses, select **Allow access only from specific IP addresses** and click **Delete item** next to the empty range entry.


**Note:** The Airflow web server of your environment is always protected by IAM, regardless of the IP ranges that are allowed to access it.

###  gcloud 

When you create an environment, following arguments control web server access level:

  * `--web-server-allow-all` provides access to Airflow from all IP addresses. This is the default option.

  * `--web-server-allow-ip` restricts access only to specific source IP ranges. To specify several IP ranges, use this argument multiple times.

  * `--web-server-deny-all` forbids access for all IP addresses.


**Note:** The Airflow web server of your environment is always protected by IAM, regardless of the IP ranges that are allowed to access it.
    
    
    gcloud composer environments create ENVIRONMENT_NAME \
        --location LOCATION \
        --image-version composer-2.17.14-airflow-2.11.1 \
        --web-server-allow-ip ip_range=WS_IP_RANGE,description=WS_RANGE_DESCRIPTION
    

Replace:

  * `WS_IP_RANGE` with the IP range, in the CIDR notation, that can access Airflow UI.
  * `WS_RANGE_DESCRIPTION` with the description of the IP range.



Example:
    
    
    gcloud composer environments create example-environment \
        --location us-central1 \
        --image-version composer-2.17.14-airflow-2.11.1 \
        --service-account "
    example-account@example-project.iam.gserviceaccount.com
    " \
        --web-server-allow-ip ip_range=192.0.2.0/24,description="office net 1" \
        --web-server-allow-ip ip_range=192.0.4.0/24,description="office net 3"
    

###  API 

When you create an environment, in the [Environment](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments#Environment) > [EnvironmentConfig](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments#EnvironmentConfig) resource, specify web server access parameters.

  * To provide access to the Airflow web server from all IP addresses, omit `webServerNetworkAccessControl`.

  * To restrict access only to specific IP ranges, specify one or more ranges in `allowedIpRanges`.

  * To forbid access for all IP addresses, add `allowedIpRanges` and make it an empty list. Do not specify IP ranges in it.


**Note:** The Airflow web server of your environment is always protected by IAM, regardless of the IP ranges that are allowed to access it.
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/environments/ENVIRONMENT_NAME",
      "config": {
        "webServerNetworkAccessControl": {
          "allowedIpRanges": [
            {
              "value": "WS_IP_RANGE",
              "description": "WS_RANGE_DESCRIPTION"
            }
          ]
        },
          "nodeConfig": {
          "serviceAccount": "SERVICE_ACCOUNT"
        }
      }
    }
    

Replace:

  * `WS_IP_RANGE` with the IP range, in the CIDR notation, that can access Airflow UI.
  * `WS_RANGE_DESCRIPTION` with the description of the IP range.



Example:
    
    
    // POST https://composer.googleapis.com/v1/{parent=projects/*/locations/*}/environments
    
    {
      "name": "projects/example-project/locations/us-central1/environments/example-environment",
      "config": {
        "webServerNetworkAccessControl": {
          "allowedIpRanges": [
            {
              "value": "192.0.2.0/24",
              "description": "office net 1"
            },
            {
              "value": "192.0.4.0/24",
              "description": "office net 3"
            }
          ]
        },
          "nodeConfig": {
            "serviceAccount": "
    example-account@example-project.iam.gserviceaccount.com
    "
        }
      }
    }
    

###  Terraform 

When you create an environment, the `allowed_ip_range` block in the `web_server_network_access_control` block contains IP ranges that can access web server.

**Note:** The Airflow web server of your environment is always protected by IAM, regardless of the IP ranges that are allowed to access it.
    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "ENVIRONMENT_NAME"
      region = "LOCATION"
    
      config {
    
        web_server_network_access_control {
    
          allowed_ip_range {
            value = "WS_IP_RANGE"
            description = "WS_RANGE_DESCRIPTION"
          }
        }
    
        node_config {
          service_account = "SERVICE_ACCOUNT"
        }
      }
    }
    

Replace:

  * `WS_IP_RANGE` with the IP range, in the CIDR notation, that can access Airflow UI.
  * `WS_RANGE_DESCRIPTION` with the description of the IP range.



Example:
    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "example-environment"
      region = "us-central1"
    
      config {
    
        web_server_network_access_control {
          allowed_ip_range {
            value = "192.0.2.0/24"
            description = "office net 1"
          },
          allowed_ip_range {
            value = "192.0.4.0/24"
            description = "office net 3"
          }
        }
    
        node_config {
          service_account = "
    example-account@example-project.iam.gserviceaccount.com
    "
        }
    
    }
    

## Step 10. (Optional) Specify Airflow configuration overrides and environment variables

You can set up [Airflow configuration overrides](https://docs.cloud.google.com/composer/docs/composer-2/override-airflow-configurations) and [environment variables](https://docs.cloud.google.com/composer/docs/composer-2/set-environment-variables) when you create an environment. As an alternative, you can do it later, after your environment is created.

Some Airflow configuration options [are blocked](https://docs.cloud.google.com/composer/docs/airflow-configurations) and you can't override them.

For the list of available Airflow configuration options, see [Configuration reference for Airflow 2](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html) and [Airflow 1.10.*](https://airflow.apache.org/docs/apache-airflow/1.10.15/configurations-ref.html)

To specify Airflow configuration overrides and environment variables:

###  Console 

On the **Create environment** page:

  1. In the **Environment variables** section, click **Add environment variable**.

  2. Enter the **Name** and **Value** for the environment variable.

  3. In the **Airflow configuration overrides** section, click **Add Airflow configuration override**.

  4. Enter the **Section** , **Key** , and **Value** for the configuration option override.

For example:

Section | Key | Value  
---|---|---  
`webserver` | `dag_orientation` | `TB`  



###  gcloud 

When you create an environment, following arguments control environment variables and Airflow configuration overrides:

  * `--env-variables` specifies a comma-separated list of environment variables.

Variable names may contain upper and lowercase letters, digits, and underscores, but they may not begin with a digit.

  * `--airflow-configs` specifies a comma-separated list of keys and values for Airflow configuration overrides.



    
    
    gcloud composer environments create ENVIRONMENT_NAME \
        --location LOCATION \
        --image-version composer-2.17.14-airflow-2.11.1 \
        --service-account "SERVICE_ACCOUNT" \
        --env-variables ENV_VARS \
        --airflow-configs CONFIG_OVERRIDES
    

Replace:

  * `ENV_VARS` with a list of comma-separated `NAME=VALUE` pairs for environment variables.
  * `CONFIG_OVERRIDES` with a list of comma-separated `SECTION-KEY=VALUE` pairs for configuration overrides. Separate the name of the configuration section with a `-` symbol, followed by the key name. For example: `core-dags_are_paused_at_creation`.



Example:
    
    
    gcloud composer environments create example-environment \
        --location us-central1 \
        --image-version composer-2.17.14-airflow-2.11.1 \
        --service-account "
    example-account@example-project.iam.gserviceaccount.com
    " \
        --env-variables SENDGRID_MAIL_FROM=user@example.com,SENDGRID_API_KEY=example-key \
        --airflow-configs core-dags_are_paused_at_creation=True,webserver-dag_orientation=TB
    

###  API 

When you create an environment, in the [Environment](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments#Environment) > [EnvironmentConfig](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments#EnvironmentConfig) resource, specify environment variables and Airflow configuration overrides.
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/environments/ENVIRONMENT_NAME",
      "config": {
        "softwareConfig": {
          "airflowConfigOverrides": {
            "SECTION-KEY": "OVERRIDE_VALUE"
          },
          "envVariables": {
            "VAR_NAME": "VAR_VALUE",
          }
        },
        "nodeConfig": {
          "serviceAccount": "SERVICE_ACCOUNT"
        }
      }
    }
    

Replace:

  * `SECTION` with the section in the configuration file where the Airflow configuration option is located.
  * `KEY` with the name of the Airflow configuration option.
  * `OVERRIDE_VALUE` with a value of the Airflow configuration option.
  * `VAR_NAME` with the name of the environment variable.
  * `VAR_VALUE` with the value of the environment variable.



Example:
    
    
    // POST https://composer.googleapis.com/v1/{parent=projects/*/locations/*}/environments
    
    {
      "name": "projects/example-project/locations/us-central1/environments/example-environment",
      "config": {
        "softwareConfig": {
          "airflowConfigOverrides": {
            "core-dags_are_paused_at_creation": "True",
            "webserver-dag_orientation": "TB"
          },
          "envVariables": {
            "SENDGRID_MAIL_FROM": "user@example.com",
            "SENDGRID_API_KEY": "example-key"
          }
        },
        "nodeConfig": {
            "serviceAccount": "
    example-account@example-project.iam.gserviceaccount.com
    "
        }
      }
    }
    

###  Terraform 

When you create an environment, following blocks control environment variables and Airflow configuration overrides:

  * `env_variables` block in the `software_config` block specifies environment variables.

Variable names may contain upper and lowercase letters, digits, and underscores, but they may not begin with a digit.

  * `airflow_config_overrides` block in the `software_config` block specifies Airflow configuration overrides.



    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "ENVIRONMENT_NAME"
      region = "LOCATION"
    
      config {
    
        software_config {
    
          airflow_config_overrides = {
            SECTION-KEY = "OVERRIDE_VALUE"
          }
    
          env_variables = {
            VAR_NAME = "VAR_VALUE"
          }
        }
    
        node_config {
          service_account = "SERVICE_ACCOUNT"
        }
    
      }
    }
    

Replace:

  * `SECTION` with the section in the configuration file where the Airflow configuration option is located.
  * `KEY` with the name of the Airflow configuration option.
  * `OVERRIDE_VALUE` with a value of the Airflow configuration option.
  * `VAR_NAME` with the name of the environment variable.
  * `VAR_VALUE` with the value of the environment variable.



Example:
    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "example-environment"
      region = "us-central1"
    
      config {
    
        software_config {
    
          airflow_config_overrides = {
            core-dags_are_paused_at_creation = "True"
            webserver-dag_orientation = "TB"
          }
    
          env_variables = {
            SENDGRID_MAIL_FROM = "user@example.com"
            SENDGRID_API_KEY = "example-key"
          }
        }
    
        node_config {
          service_account = "
    example-account@example-project.iam.gserviceaccount.com
    "
        }
      }
    }
    

## Step 11. (Optional) Specify maintenance windows

Default maintenance windows in Managed Airflow (Gen 2) are from 00:00:00 to 04:00:00 (GMT) on Friday, Saturday, and Sunday every week.

To specify custom maintenance windows for your environment:

###  Console 

On the **Create environment** page

  1. Locate the **Maintenance windows** section.

  2. In the **Timezone** drop-down list, choose a time zone for maintenance windows.

  3. Set **Start time** , **Days** , and **Length** , so that:

     * At least 12 hours of time is allocated in a single week.

     * You can use several time slots, but each slot duration must be at least 4 hours.

For example, a period of 4 hours every Monday, Wednesday, and Friday provides the required amount of time.




###  gcloud 

The following arguments define maintenance windows parameters:

  * `--maintenance-window-start` sets the start time of a maintenance window.
  * `--maintenance-window-end` sets the end time of a maintenance window.
  * `--maintenance-window-recurrence` sets the [maintenance window recurrence](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions#maintenance-window).


    
    
    gcloud composer environments create ENVIRONMENT_NAME \
        --location LOCATION \
        --image-version composer-2.17.14-airflow-2.11.1 \
        --service-account "SERVICE_ACCOUNT" \
        --maintenance-window-start 'DATETIME_START' \
        --maintenance-window-end 'DATETIME_END' \
        --maintenance-window-recurrence 'MAINTENANCE_RECURRENCE'
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `DATETIME_START` with the start date and time in the [date/time input format](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes). Only the specified time of the day is used, the specified date is ignored.
  * `DATETIME_END` with the end date and time in the [date/time input format](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes). Only the specified time of the day is used, the specified date is ignored. The specified date and time must be after the start date.
  * `MAINTENANCE_RECURRENCE` with an [RFC 5545](https://www.ietf.org/rfc/rfc5545.txt) RRULE for maintenance windows recurrence. Managed Airflow supports two formats:

  * The `FREQ=DAILY` format specifies a daily recurrence.

  * The `FREQ=WEEKLY;BYDAY=SU,MO,TU,WE,TH,FR,SA` format specifies a recurrence on selected days of the week.




The following example specifies a 6-hour maintenance window between 01:00 and 07:00 (UTC) on Wednesdays, Saturdays, and Sundays. The 1 January, 2023 date is ignored.
    
    
    gcloud composer environments create example-environment \
      --location us-central1 \
      --image-version composer-2.17.14-airflow-2.11.1 \
      --service-account "
    example-account@example-project.iam.gserviceaccount.com
    " \
      --maintenance-window-start '2023-01-01T01:00:00Z' \
      --maintenance-window-end '2023-01-01T07:00:00Z' \
      --maintenance-window-recurrence 'FREQ=WEEKLY;BYDAY=SU,WE,SA'
    

###  API 

When you create an environment, in the [Environment](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments#Environment) > [EnvironmentConfig](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments#EnvironmentConfig) resource, specify maintenance windows parameters:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/environments/ENVIRONMENT_NAME",
      "config": {
        "maintenanceWindow": {
            "startTime": "DATETIME_START",
            "endTime": "DATETIME_END",
            "recurrence": "MAINTENANCE_RECURRENCE"
        },
        "nodeConfig": {
          "serviceAccount": "SERVICE_ACCOUNT"
        }
      }
    }
    

Replace:

  * `DATETIME_START` with the start date and time in the [date/time input format](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes). Only the specified time of the day is used, the specified date is ignored.
  * `DATETIME_END` with the end date and time in the [date/time input format](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes). Only the specified time of the day is used, the specified date is ignored. The specified date and time must be after the start date.
  * `MAINTENANCE_RECURRENCE` with an RFC 5545 RRULE for maintenance windows recurrence. Managed Airflow supports two formats:

  * The `FREQ=DAILY` format specifies a daily recurrence.

  * The `FREQ=WEEKLY;BYDAY=SU,MO,TU,WE,TH,FR,SA` format specifies a recurrence on selected days of the week.




The following example specifies a 6-hour maintenance window between 01:00 and 07:00 (UTC) on Wednesdays, Saturdays, and Sundays. The 1 January, 2023 date is ignored.

Example:
    
    
    // POST https://composer.googleapis.com/v1/{parent=projects/*/locations/*}/environments
    
    {
      "name": "projects/example-project/locations/us-central1/environments/example-environment",
      "config": {
        "maintenanceWindow": {
            "startTime": "2023-01-01T01:00:00Z",
            "endTime": "2023-01-01T07:00:00Z",
            "recurrence": "FREQ=WEEKLY;BYDAY=SU,WE,SA"
        },
        "nodeConfig": {
          "serviceAccount": "SERVICE_ACCOUNT"
        }
      }
    }
    

###  Terraform 

The `maintenance_window` block specifies the maintenance windows for your environment:
    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "ENVIRONMENT_NAME"
      region = "LOCATION"
    
      config {
        maintenance_window {
          start_time = "DATETIME_START"
          end_time = "DATETIME_END"
          recurrence = "MAINTENANCE_RECURRENCE"
        }
    
        node_config {
          service_account = "SERVICE_ACCOUNT"
        }
      }
    }
    

Replace:

  * `DATETIME_START` with the start date and time in the [date/time input format](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes). Only the specified time of the day is used, the specified date is ignored.
  * `DATETIME_END` with the end date and time in the [date/time input format](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes). Only the specified time of the day is used, the specified date is ignored. The specified date and time must be after the start date.
  * `MAINTENANCE_RECURRENCE` with an RFC 5545 RRULE for maintenance windows recurrence. Managed Airflow supports two formats:

    * The `FREQ=DAILY` format specifies a daily recurrence.
    * The `FREQ=WEEKLY;BYDAY=SU,MO,TU,WE,TH,FR,SA` format specifies a recurrence on selected days of the week.



The following example specifies a 6-hour maintenance window between 01:00 and 07:00 (UTC) on Wednesdays, Saturdays, and Sundays. The 1 January, 2023 date is ignored.
    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "example-environment"
      region = "us-central1"
    
      config {
        maintenance_window {
          start_time = "2023-01-01T01:00:00Z"
          end_time = "2023-01-01T07:00:00Z"
          recurrence = "FREQ=WEEKLY;BYDAY=SU,WE,SA"
        }
      }
    }
    

## Step 12. (Optional) Data lineage integration

Data lineage is a Knowledge Catalog feature that lets you track data movement.

[Data lineage integration](https://docs.cloud.google.com/composer/docs/composer-2/lineage-integration) is available in Managed Airflow (Gen 2) versions 2.1.2 and later with Airflow versions 2.2.5 and later. 

Data lineage integration is **automatically enabled** in a new Managed Airflow environment if the following conditions are met:

  * Data Lineage API is enabled in your project. For more information, see [Enabling Data Lineage API](https://docs.cloud.google.com/dataplex/docs/use-lineage) in Knowledge Catalog documentation.

**Caution:** After you enable Data Lineage API, Knowledge Catalog **automatically starts ingesting data** for BigQuery, Cloud Data Fusion, Managed Service for Apache Spark. This happens even if you don't create a Managed Airflow environment with data lineage integration.  
You can [configure the ingestion of data lineage](https://docs.cloud.google.com/dataplex/docs/use-lineage#control-ingestion) to enable or deactivate automatic data lineage ingestion for BigQuery or Managed Service for Apache Spark.
  * A custom [Lineage Backend](https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/lineage.html#lineage-backend) isn't configured in Airflow.




You can disable data lineage integration when you create an environment. For example, if you want to override the automatic behavior or choose to [enable data lineage later](https://docs.cloud.google.com/composer/docs/composer-2/lineage-integration), after the environment is created.

###  Console 

To disable data lineage integration, on the **Create environment** page, do the following:

  1. In the **Advanced configuration** section, expand **Show advanced configuration**.

  2. In the **Knowledge Catalog Lineage integration** menu, select **Disable integration with Knowledge Catalog Lineage**.




###  gcloud 

When you create an environment, the `--disable-cloud-data-lineage-integration` argument disables the data lineage integration.
    
    
    gcloud composer environments create ENVIRONMENT_NAME \
        --location LOCATION \
        --image-version composer-2.17.14-airflow-2.11.1 \
        --service-account "SERVICE_ACCOUNT" \
        --disable-cloud-data-lineage-integration
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `LOCATION` with the region where the environment is located.



Example:
    
    
    gcloud composer environments create example-environment \
        --location us-central1 \
        --image-version composer-2.17.14-airflow-2.11.1 \
        --service-account "
    example-account@example-project.iam.gserviceaccount.com
    " \
        --disable-cloud-data-lineage-integration
    

## Step 13. (Optional) Configure data encryption (CMEK)

By default, data in your environment is encrypted with a key provided by Google.

To use customer-managed encryption keys (CMEK) to encrypt data in your environment, follow the instructions outlined in [Using customer-managed encryption keys](https://docs.cloud.google.com/composer/docs/composer-2/configure-cmek-encryption).

## Step 14. (Optional) Use a custom environment's bucket

**Warning:** Because your environment runs DAGs on behalf of your environment's service account, users who can add and modify DAGs in the custom environment's bucket **can run their code on behalf of the environment's service account** and **exercise all permissions of this account**. Make sure that you are familiar with [security considerations for environment's service accounts](https://docs.cloud.google.com/composer/docs/composer-2/access-control#service-account-security) and understand how this account interacts with permissions and roles that you grant to individual users in your project.

When you create an environment, Managed Airflow creates a bucket for your environment automatically.

As an alternative, you can specify a custom Cloud Storage bucket from your project. Your environment uses this bucket in the same way as the automatically created bucket.

To use a custom environment bucket, follow the instructions outlined in [Use a custom environment's bucket](https://docs.cloud.google.com/composer/docs/composer-2/use-custom-bucket).

## Step 15. (Optional) Specify environment labels

You can assign labels to your environments to [break down billing costs based on these labels](https://docs.cloud.google.com/composer/docs/composer-2/manage-environment-labels).

###  Console 

On the **Create environment** page, in the **Labels** section:

  1. Click **Add label**.

  2. In **Key** and **Value** fields, specify key and value pairs for the environment labels.




###  gcloud 

When you create an environment, the `--labels` argument specifies a comma-separated list of keys and values with environment labels.
    
    
    gcloud composer environments create ENVIRONMENT_NAME \
        --location LOCATION \
        --image-version composer-2.17.14-airflow-2.11.1 \
        --service-account "SERVICE_ACCOUNT" \
        --labels LABELS
    

Replace:

  * `LABELS` with a list of comma-separated `KEY=VALUE` pairs for environment labels.



Example:
    
    
    gcloud composer environments create example-environment \
        --location us-central1 \
        --image-version composer-2.17.14-airflow-2.11.1 \
        --service-account "
    example-account@example-project.iam.gserviceaccount.com
    " \
        --labels owner=engineering-team,env=production
    

###  API 

When you create an environment, in the [Environment](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments#Environment) resource, specify labels for your environment.
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/environments/ENVIRONMENT_NAME",
      "labels": {
        "LABEL_KEY": "LABEL_VALUE"
      }
    }
    

Replace:

  * `LABEL_KEY` with a key of the environment label.
  * `LABEL_VALUE` with a value of the environment label.



Example:
    
    
    // POST https://composer.googleapis.com/v1/{parent=projects/*/locations/*}/environments
    
    {
      "name": "projects/example-project/locations/us-central1/environments/example-environment",
      "labels": {
        "owner": "engineering-team",
        "env": "production"
      }
    }
    

###  Terraform 

When you create an environment, specify labels in the `labels` block ( outside of the `config` block).
    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "ENVIRONMENT_NAME"
      region = "LOCATION"
    
      labels = {
        LABEL_KEY = "LABEL_VALUE"
      }
    
    }
    

Replace:

  * `LABEL_KEY` with a key of the environment label.
  * `LABEL_VALUE` with a value of the environment label.



Example:
    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "example-environment"
      region = "us-central1"
    
      labels = {
        owner = "engineering-team"
        env = "production"
      }
    
    }
    

## What's next

  * [Troubleshooting environment creation](https://docs.cloud.google.com/composer/docs/composer-2/troubleshooting-environment-creation)
  * [Configuring Shared VPC](https://docs.cloud.google.com/composer/docs/composer-2/configure-shared-vpc)
  * [Configuring VPC Service Controls](https://docs.cloud.google.com/composer/docs/composer-2/configure-vpc-sc)
  * [Adding and updating DAGs](https://docs.cloud.google.com/composer/docs/composer-2/manage-dags)
  * [Accessing Airflow UI](https://docs.cloud.google.com/composer/docs/composer-2/access-airflow-web-interface)
  * [Updating and deleting environments](https://docs.cloud.google.com/composer/docs/composer-2/update-environments)
  * [About Managed Airflow versions](https://docs.cloud.google.com/composer/docs/composer-versioning-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
