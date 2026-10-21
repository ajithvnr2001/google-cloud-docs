---
url: https://docs.cloud.google.com/composer/docs/composer-1/create-environments/
title: Create Managed Service for Apache Airflow environments \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:26:50.046506+00:00
---

# Create Managed Service for Apache Airflow environments  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-1/create-environments/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 1 Guides ](https://docs.cloud.google.com/composer/docs/composer-1/composer-overview)



Send feedback 

#  Create Managed Service for Apache Airflow environments Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/create-environments "View this page for Managed Airflow \(Gen 3\)") | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/create-environments "View this page for Managed Airflow \(Gen 2\)") | **Managed Airflow (Legacy Gen 1)**

This page explains how to create a Managed Airflow environment.

  * For more information about environments, see [Environment architecture](https://docs.cloud.google.com/composer/docs/composer-1/environment-architecture).
  * For more information about creating an environment with Terraform, see [Create environments (Terraform)](https://docs.cloud.google.com/composer/docs/composer-1/terraform-create-environments).



## Before you begin

**Caution:** It's **no longer possible to create Managed Airflow (Legacy Gen 1) environments in Google Cloud console**. You can still create Managed Airflow (Legacy Gen 1) environments through Google Cloud CLI, Terraform, and API if your project supports creating new Managed Airflow (Legacy Gen 1) environments.

  * [Enable the Cloud Composer API](https://docs.cloud.google.com/composer/docs/composer-1/enable-composer-service). For the full list of services used by Managed Airflow, see [Services required by Managed Airflow](https://docs.cloud.google.com/composer/docs/composer-1/enable-composer-service#required-services).

  * The approximate time to create an environment is 25 minutes.

  * If you create an environment with Terraform, the service account used by Terraform must [have a role](https://docs.cloud.google.com/composer/docs/composer-1/access-control#service-account) with the `composer.environments.create` permission enabled.

For more information about the service account for Terraform, see [Google Provider Configuration Reference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/guides/provider_reference#credentials).

For more information about using Terraform to create a Managed Airflow environment, see [Terraform documentation](https://www.terraform.io/docs/providers/google/r/composer_environment).

For more information about additional parameters, see [Terraform Argument Reference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/composer_environment#argument-reference---cloud-composer-1).

  * **Private IP** : There are specific network and peering requirements to create a Private IP environment. For more information, see [Configuring private IP](https://docs.cloud.google.com/composer/docs/composer-1/configure-private-ip).

  * **Shared VPC** : There are specific network requirements to use Shared VPC with Managed Airflow. For information, see [Configuring shared VPC](https://docs.cloud.google.com/composer/docs/composer-1/configure-shared-vpc).

  * **VPC SC** : To deploy Managed Airflow environments inside a security perimeter, see [Configuring VPC SC](https://docs.cloud.google.com/composer/docs/composer-1/configure-vpc-sc). When used with Managed Airflow, VPC Service Controls have several [known limitations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#composer).


**Important:** For production use cases, we highly recommend to use highly resilient environments. The Airflow database of your environment is zonal. During a zonal outage, Airflow tasks that are executed in the affected zone are interrupted and marked as failed by Airflow. Highly resilient environments are more resilient to this issue, because their databases are located in two separate zones.

## Step 1. Create or choose an environment's service account

When you create an environment, you specify a service account. This service account is called _environment's service account_. Your environment uses this service account to perform most of the operations.

The service account for your environment is not a user account. A service account is a special kind of account used by an application or a virtual machine (VM) instance, not a person.

You can't change the service account of your environment later.

**Warning:** Your environment's service account can have **too broad permissions on your project**. Because your environment runs DAGs on behalf of your environment's service account, users who can add and modify DAGs in your environment's bucket **can run their code on behalf of the environment's service account** and **exercise all permissions of this account**. Make sure that you are familiar with [security considerations for environment's service accounts](https://docs.cloud.google.com/composer/docs/composer-1/access-control#service-account-security) and understand how this account interacts with permissions and roles that you grant to individual users in your project.

If you don't have a service account for Managed Airflow environments in your project yet, create it.

See [Create environments (Terraform)](https://docs.cloud.google.com/composer/docs/composer-1/terraform-create-environments) for an extended example of creating a service account for your environment in Terraform.

**Important:** You can use the same service account for more than one Managed Airflow environment. In this case, if you grant extra permissions to access resources in your project to this account, all environments that use it will get the same permissions.

To create a new service account for your environment:

  1. [Create a new service account](https://docs.cloud.google.com/iam/docs/service-accounts-create#creating) as described in the Identity and Access Management documentation.

  2. [Grant a role to it](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role), as described in the Identity and Access Management documentation. The required role is **Composer Worker** (`composer.worker`).

  3. If your environment [uses resource location restrictions](https://docs.cloud.google.com/composer/docs/composer-1/configure-resource-location-restrictions), or installs PyPI packages [from an Artifact Registry repository](https://docs.cloud.google.com/composer/docs/composer-1/install-python-dependencies#install-ar-repo) or [from a private repository](https://docs.cloud.google.com/composer/docs/composer-1/install-python-dependencies#install-private-repo), then grant the **Service Account User** (`iam.serviceAccountUser`) role to the **user-managed service account** that runs your environment on itself (both the principal and the resource are the same service account).

  4. To access other resources in your Google Cloud project, grant extra permissions to access those resources to this service account. The **Composer Worker** (`composer.worker`) role provides this required set of permissions in most cases. Add extra permissions to this service account only when it's necessary for the operation of your DAGs.




## Step 2. Basic setup

This step creates a Managed Airflow environment with default parameters in the specified location.

All other steps in this guide explain how to customize and configure different aspects of your environment. All of the remaining steps are optional.

###  Console 

  1. In the Google Cloud console, go to the **Create environment** page.

[Go to Create environment](https://console.cloud.google.com/composer/environments/create-composer-1)

  2. In the **Name** field, enter a name for your environment.

The name must start with a lowercase letter followed by up to 62 lowercase letters, numbers, or hyphens, and can't end with a hyphen. The environment name is used to create subcomponents for the environment, so you must provide a name that is also valid as a Cloud Storage bucket name. See [Bucket naming guidelines](https://docs.cloud.google.com/storage/docs/buckets#naming) for a list of restrictions. 

  3. In the **Location** drop-down list, choose a location for your environment.

A location is the region where the environment is located. 

  4. In the **Image version** drop-down list, select a [Managed Airflow image](https://docs.cloud.google.com/composer/docs/composer-versions#images) with the required version of Airflow.

  5. In in the **Node configuration** section, in the **Service account** drop-down list, select a service account for your environment.

If you don't have a service account for your environment yet, see Create or choose an environment's service account.




###  gcloud 
    
    
    gcloud composer environments create ENVIRONMENT_NAME \
        --location LOCATION \
        --image-version IMAGE_VERSION \
        --service-account "SERVICE_ACCOUNT"
    

**Important:** You must specify an image version for Managed Airflow (Legacy Gen 1). By default, Cloud Composer API uses the [default image](https://docs.cloud.google.com/composer/docs/composer-versions#images) for Managed Airflow (Gen 2). 

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
        --image-version composer-1.20.12-airflow-1.10.15 \
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
    

**Important:** You must specify an image version for Managed Airflow (Legacy Gen 1). By default, Cloud Composer API uses the [default image](https://docs.cloud.google.com/composer/docs/composer-versions#images) for Managed Airflow (Gen 2). 

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
          "imageVersion": "composer-1.20.12-airflow-1.10.15"
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
    

**Important:** You must specify an image version for Managed Airflow (Legacy Gen 1). By default, Cloud Composer API uses the [default image](https://docs.cloud.google.com/composer/docs/composer-versions#images) for Managed Airflow (Gen 2). 

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
          image_version = "composer-1.20.12-airflow-1.10.15"
        }
        node_config {
          service_account = "
    example-account@example-project.iam.gserviceaccount.com
    "
        }
      }
    }
    

## Step 3. (Optional) Configure environment scale and performance parameters

To specify the scale and performance configuration for your environment, provide the number of nodes in your environment's GKE cluster and select machine types for environment components.

###  Console 

On the **Create environment** page:

  1. In the **Node configuration** section:

     * Enter the **Node count**.

Node count is the number of Google Kubernetes Engine nodes in the environment's cluster. By default, environments have 3 nodes.

You can change this value after you create your environment. 

     * Choose **Machine type** for nodes.

The machine type for nodes is [Compute Engine machine type](https://docs.cloud.google.com/composer/pricing#machine-type) used for cluster instances. This parameter determines the number of CPUs and the amount of memory for your environment. The default machine type is `n1-standard-1`.

To change this value after you create your environment, you must [manually reconfigure the environment cluster](https://docs.cloud.google.com/composer/docs/composer-1/update-environments#upgrading-mt). 

     * Enter the **Disk size**.

The disk size, in GB, for environment nodes. Each node in your environment has this amount of disk space. Select a larger disk size if you expect to store a large volume of data in folders that are synchronized with environment VMs. For example, in the `/data` folder of your environment's bucket.

The minimum size is 30 GB. The default size is 100 GB. You can't change this parameter after you create an environment. 

     * Choose the **Number of schedulers**.

Your environment can run more than one Airflow scheduler at the same time. Use multiple schedulers to distribute load between several scheduler instances for better performance and reliability.

Increasing the number of schedulers does not always improve Airflow performance. For example, having only one scheduler might provide better performance than having two. This might happen when the extra scheduler is not utilized, and thus consumes resources of your environment without contributing to overall performance. The actual scheduler performance depends on the number of Airflow workers, the number of DAGs and tasks that run in your environment, and the configuration of both Airflow and the environment.

We recommend starting with two schedulers and then monitoring the performance of your environment. If you change the number of schedulers, you can always scale your environment back to the original number of schedulers.

For more information about configuring multiple schedulers, see [Airflow documentation](https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/scheduler.html#fine-tuning-your-scheduler-performance). 

  2. Expand the **Networking, Airflow config overrides, and additional features** item.

  3. In the **Cloud SQL configuration** section, choose **Cloud SQL machine type**.

This parameter determines the machine type for the [Cloud SQL instance](https://docs.cloud.google.com/composer/pricing#db-machine-types) that runs the Airflow database. The default Cloud SQL machine type is `db-n1-standard-2`. 

  4. In the **Web server configuration** section, choose **Web server machine type**.

This parameter determines the machine type for the [Compute Engine instance](https://docs.cloud.google.com/composer/pricing#ws-machine-types) that runs the Airflow web server.

The default web server machine type is `composer-n1-webserver-2`. 




###  gcloud 

When you create an environment, following arguments control environment scale and performance parameters:

  * `--node-count` specifies the number of nodes in your environment.

Node count is the number of Google Kubernetes Engine nodes in the environment's cluster. By default, environments have 3 nodes.

You can change this value after you create your environment. 

  * `--scheduler-count` specifies the number of schedulers in your environment.

Your environment can run more than one Airflow scheduler at the same time. Use multiple schedulers to distribute load between several scheduler instances for better performance and reliability.

Increasing the number of schedulers does not always improve Airflow performance. For example, having only one scheduler might provide better performance than having two. This might happen when the extra scheduler is not utilized, and thus consumes resources of your environment without contributing to overall performance. The actual scheduler performance depends on the number of Airflow workers, the number of DAGs and tasks that run in your environment, and the configuration of both Airflow and the environment.

We recommend starting with two schedulers and then monitoring the performance of your environment. If you change the number of schedulers, you can always scale your environment back to the original number of schedulers.

For more information about configuring multiple schedulers, see [Airflow documentation](https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/scheduler.html#fine-tuning-your-scheduler-performance). 

  * `--disk-size` specifies the disk size for environment VMs.

The disk size, in GB, for environment nodes. Each node in your environment has this amount of disk space. Select a larger disk size if you expect to store a large volume of data in folders that are synchronized with environment VMs. For example, in the `/data` folder of your environment's bucket.

The minimum size is 30 GB. The default size is 100 GB. You can't change this parameter after you create an environment. 

  * `--machine-type` specifies the machine type for node VMs.

The machine type for nodes is [Compute Engine machine type](https://docs.cloud.google.com/composer/pricing#machine-type) used for cluster instances. This parameter determines the number of CPUs and the amount of memory for your environment. The default machine type is `n1-standard-1`.

To change this value after you create your environment, you must [manually reconfigure the environment cluster](https://docs.cloud.google.com/composer/docs/composer-1/update-environments#upgrading-mt). 

  * `--cloud-sql-machine-type` specifies the machine type for the Cloud SQL instance.

This parameter determines the machine type for the [Cloud SQL instance](https://docs.cloud.google.com/composer/pricing#db-machine-types) that runs the Airflow database. The default Cloud SQL machine type is `db-n1-standard-2`. 

  * `--web-server-machine-type` specifies the machine type for the Airflow web server instance.

This parameter determines the machine type for the [Compute Engine instance](https://docs.cloud.google.com/composer/pricing#ws-machine-types) that runs the Airflow web server.

The default web server machine type is `composer-n1-webserver-2`. 



    
    
    gcloud composer environments create ENVIRONMENT_NAME \
        --location LOCATION \
        --image-version composer-1.20.12-airflow-1.10.15 \
        --service-account "SERVICE_ACCOUNT" \
        --zone NODE_ZONE \
        --node-count NODE_COUNT \
        --scheduler-count SCHEDULER_COUNT \
        --disk-size DISK_SIZE \
        --machine-type NODE_MACHINE_TYPE \
        --cloud-sql-machine-type SQL_MACHINE_TYPE \
        --web-server-machine-type WS_MACHINE_TYPE
    

Replace:

  * `NODE_COUNT` with the number of nodes.
  * `NODE_ZONE` with the Compute Engine zone for your environment VMs.
  * `SCHEDULER_COUNT` with the number of schedulers.
  * `DISK_SIZE` with the disk size for environment VMs, in GB.
  * `NODE_MACHINE_TYPE` with the [machine type for node VMs](https://docs.cloud.google.com/composer/pricing#machine-type).
  * `SQL_MACHINE_TYPE` with the [machine type for the Cloud SQL instance](https://docs.cloud.google.com/composer/pricing#db-machine-types).
  * `WS_MACHINE_TYPE` with the [machine type for the Airflow web server instance](https://docs.cloud.google.com/composer/pricing#ws-machine-types).



Example:
    
    
    gcloud composer environments create example-environment \
        --location us-central1 \
        --image-version composer-1.20.12-airflow-1.10.15 \
        --service-account "
    example-account@example-project.iam.gserviceaccount.com
    " \
        --zone us-central1-a \
        --node-count 6 \
        --scheduler-count 1 \
        --disk-size 50 \
        --machine-type n1-standard-2 \
        --cloud-sql-machine-type db-n1-standard-2 \
        --web-server-machine-type composer-n1-webserver-2
    

###  API 

When you create an environment, in the [Environment](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments#Environment) > [EnvironmentConfig](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments#EnvironmentConfig) resource, specify environment scale and performance parameters.
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/environments/ENVIRONMENT_NAME",
      "config": {
        "nodeCount": NODE_COUNT,
        "nodeConfig": {
          "machineType": "NODE_MACHINE_TYPE",
          "diskSizeGb": DISK_SIZE,
          "serviceAccount": "SERVICE_ACCOUNT"
        },
        "softwareConfig": {
          "schedulerCount": SCHEDULER_COUNT
        },
        "databaseConfig": {
          "machineType": "SQL_MACHINE_TYPE"
        },
        "webServerConfig": {
          "machineType": "WS_MACHINE_TYPE"
        }
      }
    }
    

Replace:

  * `NODE_COUNT` with the number of nodes.
  * `DISK_SIZE` with the disk size for environment VMs, in GB.
  * `NODE_MACHINE_TYPE` with the machine type [for node VMs](https://docs.cloud.google.com/composer/pricing#machine-type). This value must contain a zone for your environment VMs.
  * `SCHEDULER_COUNT` with the number of schedulers.
  * `SQL_MACHINE_TYPE` with the machine type [for the Cloud SQL instance](https://docs.cloud.google.com/composer/pricing#db-machine-types).
  * `WS_MACHINE_TYPE` with the machine type [for the Airflow web server instance](https://docs.cloud.google.com/composer/pricing#ws-machine-types).



Example:
    
    
    // POST https://composer.googleapis.com/v1/{parent=projects/*/locations/*}/environments
    
    {
      "name": "projects/example-project/locations/us-central1/environments/example-environment",
      "config": {
        "nodeCount": 6,
        "nodeConfig": {
          "machineType": "projects/example-project/zones/us-central1-a/machineTypes/n1-standard-2",
          "diskSizeGb": 50,
          "serviceAccount": "
    example-account@example-project.iam.gserviceaccount.com
    "
        },
        "softwareConfig": {
          "schedulerCount": 1
        },
        "databaseConfig": {
          "machineType": "db-n1-standard-2"
        },
        "webServerConfig": {
          "machineType": "composer-n1-webserver-2"
        }
      }
    }
    

###  Terraform 

When you create an environment, following fields control environment scale and performance parameters:

  * `node_count` in the `node_config` block specifies the number of nodes in your environment.

Node count is the number of Google Kubernetes Engine nodes in the environment's cluster. By default, environments have 3 nodes.

You can change this value after you create your environment. 

  * `disk_size_gb` in the `node_config` block specifies the disk size for environment VMs.

The disk size, in GB, for environment nodes. Each node in your environment has this amount of disk space. Select a larger disk size if you expect to store a large volume of data in folders that are synchronized with environment VMs. For example, in the `/data` folder of your environment's bucket.

The minimum size is 30 GB. The default size is 100 GB. You can't change this parameter after you create an environment. 

  * `machine_type` in the `node_config` block specifies the machine type for node VMs. When you specify this field, also provide a [Compute Engine zone](https://docs.cloud.google.com/compute/docs/regions-zones/regions-zones) for your environment VMs in the `zone` field.

The machine type for nodes is [Compute Engine machine type](https://docs.cloud.google.com/composer/pricing#machine-type) used for cluster instances. This parameter determines the number of CPUs and the amount of memory for your environment. The default machine type is `n1-standard-1`.

To change this value after you create your environment, you must [manually reconfigure the environment cluster](https://docs.cloud.google.com/composer/docs/composer-1/update-environments#upgrading-mt). 

  * `machine_type` in the `database_config` block specifies the machine type for the Cloud SQL instance.

This parameter determines the machine type for the [Cloud SQL instance](https://docs.cloud.google.com/composer/pricing#db-machine-types) that runs the Airflow database. The default Cloud SQL machine type is `db-n1-standard-2`. 

  * `machine_type` in the `web_server_config` block specifies the machine type for the Airflow web server instance.

This parameter determines the machine type for the [Compute Engine instance](https://docs.cloud.google.com/composer/pricing#ws-machine-types) that runs the Airflow web server.

The default web server machine type is `composer-n1-webserver-2`. 

  * `scheduler_count` field in the `software_config` block specifies the number of schedulers in your environment. Your environment must use Airflow 2.



    
    
    resource "google_composer_environment" "example" {
      name = "ENVIRONMENT_NAME"
      region = "LOCATION"
    
      config {
    
        node_config {
          node_count = NODE_COUNT
          disk_size_gb = DISK_SIZE
          machine_type = "NODE_MACHINE_TYPE"
          zone = "NODE_ZONE"
          service_account = "SERVICE_ACCOUNT"
        }
    
        software_config {
          scheduler_count = SCHEDULER_COUNT
        }
    
        database_config {
          machine_type = "SQL_MACHINE_TYPE"
        }
    
        web_server_config {
          machine_type = "WS_MACHINE_TYPE"
        }
      }
    }
    

Replace:

  * `NODE_COUNT` with the number of nodes.
  * `DISK_SIZE` with the disk size for environment VMs, in GB.
  * `NODE_MACHINE_TYPE` with the machine type [for node VMs](https://docs.cloud.google.com/composer/pricing#machine-type).
  * `NODE_ZONE` with the Compute Engine zone for your environment VMs.
  * `SCHEDULER_COUNT` with the number of schedulers.
  * `SQL_MACHINE_TYPE` with the machine type [for the Cloud SQL instance](https://docs.cloud.google.com/composer/pricing#db-machine-types).
  * `WS_MACHINE_TYPE` with the machine type [for the Airflow web server instance](https://docs.cloud.google.com/composer/pricing#ws-machine-types).



Example:
    
    
    resource "google_composer_environment" "example" {
      name = "example-environment"
      region = "us-central1"
    
      config {
    
        node_config {
          node_count = 4
          disk_size_gb = 100
          zone = "us-central1-a"
          machine_type = "n1-standard-2"
          service_account = "
    example-account@example-project.iam.gserviceaccount.com
    "
        }
    
        software_config {
          scheduler_count = 2
        }
    
        database_config {
          machine_type = "db-n1-standard-2"
        }
    
        web_server_config {
          machine_type = "composer-n1-webserver-2"
        }
      }
    }
    

## Step 4. (Optional) Configure your environment's networking

Networking parameters depend on the type of environment that you want to create:

  * **Public IP environment**. Use the default networking parameters.

  * **Private IP environment (VPC peerings)**. In this configuration, your environment uses VPC peerings for connectivity.

**Note:** Managed Airflow (Legacy Gen 1) supports only private IP environments with VPC peerings. Managed Airflow (Gen 2) environments can use both VPC peerings and Private Service Connect for connectivity in Private IP.

Configure your Private IP environment:

    1. [Configure your project's networking for Private IP environments](https://docs.cloud.google.com/composer/docs/composer-1/configure-private-ip).
    2. Specify other parameters for your Private IP environment, as described further in this section.

For a Private IP environment with VPC peerings, you need to know:

    * Your VPC network ID
    * Your VPC subnetwork ID
    * Two secondary IP ranges in your VPC subnetwork:

      * Secondary IP range for pods
      * Secondary IP range for services
    * IP ranges for the components of the environment:

      * IP range for the GKE control plane.
      * Web server IP range.
      * IP range for the Cloud SQL instance.
  * For a **Shared VPC environment** , you must do additional networking setup for the host project, then create a Public or a Private IP environment in a service project. Follow the instructions on the [Configuring Shared VPC](https://docs.cloud.google.com/composer/docs/composer-1/configure-shared-vpc) page.

**Important:** If you create an environment in the service project using Google Cloud console, then your account must have the `compute.subnetworks.use` permission in the host project. Otherwise, the list of available subnetworks does not contain subnetworks from the host project. If you create an environment using `gcloud`, API, or Terraform, then your account does not need this additional permission.

For a Shared VPC environment, you need to know:

    * Your host project VPC network ID
    * Your host project VPC subnetwork ID

    * Two secondary IP ranges in your host project VPC subnetwork:

      * Secondary IP range for pods
      * Secondary IP range for services

When creating a **Public IP Shared VPC environment** , you still need to specify your host project VPC network, subnetwork, and secondary IP ranges for pods and services.

  * To create a **VPC SC environment** , you must create a service perimeter and then create Private IP environments inside this perimeter. Follow the instructions outlined in [Configuring VPC Service Controls](https://docs.cloud.google.com/composer/docs/composer-1/configure-vpc-sc).




Additional networking options for environments are:

  * **Privately used public IP addresses**. If you want to use more IP addresses, your environment can [privately use certain public IP address ranges](https://docs.cloud.google.com/composer/docs/composer-1/configure-privately-used-public-ip) as internal, subnet IP address ranges for pods and services.
  * **Authorized networks**. If you want to access the control plane of your Private IP environment using HTTPS, you can use [authorized networks](https://docs.cloud.google.com/composer/docs/composer-1/configure-authorized-networks) to specify CIDR ranges that can do so.
  * **IP Masquerade agent**. By using environments with the IP Masquerade agent, you can use many-to-one IP address translations in your environment's networking configurations. For more information about creating environments with IP Masquerade agent, see [Enable the IP Masquerade agent](https://docs.cloud.google.com/composer/docs/composer-1/enable-ip-masquerade-agent).



###  Console 

To create a Private IP environment:

  1. Make sure that your networking is configured for the type of environment that you want to create.

  2. Expand the **Networking, Airflow config overrides, and additional features** item.

  3. In the **Network configuration** section, select the **Enable VPC-native (using alias-IP)** checkbox.

  4. In the **Network** drop-down list, select your VPC network ID.

  5. In the **Subnetwork** drop-down list, select your VPC subnetwork ID.

  6. In the **Pod IP Address Allocation** section, specify the secondary IP range for pods. You can use an existing secondary range in your VPC network, or specify a new one in the CIDR notation.

  7. In the **Service IP Address Allocation** section, specify the secondary IP range for services. You can use an existing secondary range in your VPC network, or specify a new one in the CIDR notation.

  8. In the **Private IP** section, select the **Enable private IP** checkbox.

  9. In the **GKE cluster master private IP** section, specify an IP range for the GKE control plane:

     * To use the [default IP range](https://docs.cloud.google.com/composer/docs/composer-1/configure-private-ip#defaults) for the region where your environment is located, select **Default IP range**.

     * To specify a custom IP range, select **Custom IP range** and enter a range in the CIDR notation in the **GKE cluster master private IP** field.

  10. Select the level access for the GKE control plane. The control plane has two endpoints. One endpoint is private, for use by cluster nodes and VMs. Another endpoint is public. You can specify the level of access for the public endpoint:

     * To enable access to the public endpoint from authorized networks, select the **Access master endpoint using its external IP address** checkbox.

Using this option sets the level of access for the control plane to ["Public endpoint access enabled, authorized networks enabled"](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/private-cluster-concept#overview). This provides restricted access to the control plane from authorized networks. By default, no source IP addresses are specified. You can add [authorized networks to the cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks#add).

     * To disable access to the public endpoint from authorized networks, clear the **Access master endpoint using its external IP address** checkbox.

Using this option sets the level of access for the control plane to ["Public endpoint access disabled"](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/private-cluster-concept#overview). This prevents all internet access to the control plane.

  11. In the **Web Server private IP** section, specify an IP range for the Airflow web server instance.

  12. In the **Cloud SQL private IP** section, specify an IP range for the Cloud SQL instance.

**Caution:** The `172.17.0.0/16` range [is reserved in Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/private-ip#network_issues).



###  gcloud 

Make sure that your networking is configured for the type of environment that you want to create.

When you create an environment, the following arguments control the networking parameters. If you omit a parameter, the default value is used.

  * `--enable-private-environment` enables a Private IP environment.

  * `--enable-ip-alias` enables VPC Native using alias IP addresses.

This parameter is required when using `--enable-private-environment` or when configuring secondary ranges for pods and services.

  * `--network` specifies your VPC network ID.

  * `--subnetwork` specifies your VPC subnetwork ID.

  * `--cluster-secondary-range-name` or `--cluster-ipv4-cidr` configures the the secondary range for pods.

  * `--services-secondary-range-name` or`--services-ipv4-cidr` to configure the secondary range for services.

  * `--master-ipv4-cidr` specifies a range for the GKE control plane.



  * `--web-server-ipv4-cidr` specifies a range for the Airflow web server instance.

  * `--cloud-sql-ipv4-cidr` specifies a range for the Cloud SQL instance.



  * `--enable-private-endpoint` controls the level access for the GKE control plane. The control plane has two endpoints. One endpoint is private, for use by cluster nodes and VMs. Another endpoint is public. You can specify the level of access for the public endpoint:

    * To enable access to the public endpoint from authorized networks, omit the `--enable-private-endpoint` argument.

Using this option sets the level of access for the control plane to ["Public endpoint access enabled, authorized networks enabled"](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/private-cluster-concept#overview). This provides restricted access to the control plane from authorized networks. By default, no source IP addresses are specified. You can add [authorized networks to the cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks#add).

    * To disable access to the public endpoint from authorized networks, specify the `--enable-private-endpoint` argument.

Using this option sets the level of access for the control plane to ["Public endpoint access disabled"](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/private-cluster-concept#overview). This prevents all internet access to the control plane.

  * `--enable-master-authorized-networks` and `--master-authorized-networks` arguments configure [authorized networks](https://docs.cloud.google.com/composer/docs/composer-1/configure-authorized-networks) for your environment.

  * `--enable-privately-used-public-ips` configures [privately used public IP addresses](https://docs.cloud.google.com/composer/docs/composer-1/configure-privately-used-public-ip) for your environment.

  * `--enable-ip-masq-agent` [enables the IP Masquerade agent](https://docs.cloud.google.com/composer/docs/composer-1/enable-ip-masquerade-agent).




Example (Private IP environment )
    
    
    gcloud composer environments create ENVIRONMENT_NAME \
        --location LOCATION \
        --image-version composer-1.20.12-airflow-1.10.15 \
        --service-account "SERVICE_ACCOUNT" \
        --enable-private-environment \
        --enable-ip-alias \
        --network NETWORK_ID \
        --subnetwork SUBNETWORK_ID \
        --cluster-ipv4-cidr PODS_RANGE \
        --services-ipv4-cidr SERVICES_RANGE \
        --master-ipv4-cidr CONTROL_PLANE_RANGE \
        --web-server-ipv4-cidr WEB_SERVER_RANGE \
        --cloud-sql-ipv4-cidr SQL_RANGE
    

Replace:

  * `NETWORK_ID` with your VPC network ID.
  * `SUBNETWORK_ID` with your VPC subnetwork ID.

  * `PODS_RANGE` with the secondary range for pods.

  * `SERVICES_RANGE` with the secondary range for services.

  * `CONTROL_PLANE_RANGE` with the secondary range for the GKE control plane.

  * `WEB_SERVER_RANGE` with the secondary range for the Airflow web server instance.

  * `SQL_RANGE` with the range for the Cloud SQL instance.

**Caution:** The `172.17.0.0/16` range [is reserved in Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/private-ip#network_issues).



## Step 5. (Optional) Add network tags

Network [tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags) are applied to all node VMs in your environment's cluster. Tags are used to identify valid sources or targets for network firewalls. Each tag within the list must comply with [RFC 1035](https://www.ietf.org/rfc/rfc1035.txt).

For example, you might want to add network tags if you plan to restrict traffic for a Private IP environment with firewall rules.

**Caution:** You can't change network tags later. If you want to later configure firewall rules that target only VMs in your environment's cluster, specify network tags when you create your environment.

###  Console 

On the **Create environment** page:

  1. Locate the **Node configuration** section.
  2. In the **Tags** field, specify instance tags for node VMs.



###  gcloud 

When you create an environment, following arguments control network tags:

  * `--tags` specifies a comma-separated list of network tags applied to all node VMs.


    
    
    gcloud composer environments create ENVIRONMENT_NAME \
        --location LOCATION \
        --image-version composer-1.20.12-airflow-1.10.15 \
        --service-account "SERVICE_ACCOUNT" \
        --tags TAGS
    

Replace:

  * `TAGS` with a comma-separated list of network tags.



Example:
    
    
    gcloud composer environments create example-environment \
        --location us-central1 \
        --image-version composer-1.20.12-airflow-1.10.15 \
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
    

## Step 6. (Optional) Configure web server network access

The Airflow web server access parameters do not depend on the type of your environment. Instead, you can configure web server access separately. For example, a Private IP environment can still have the Airflow UI accessible from the internet.

You can't configure the allowed IP ranges using private IP addresses.

###  Console 

On the **Create environment** page, in the **Web server configuration** section:

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
        --image-version composer-1.20.12-airflow-1.10.15 \
        --web-server-allow-ip ip_range=WS_IP_RANGE,description=WS_RANGE_DESCRIPTION
    

Replace:

  * `WS_IP_RANGE` with the IP range, in the CIDR notation, that can access Airflow UI.
  * `WS_RANGE_DESCRIPTION` with the description of the IP range.



Example:
    
    
    gcloud composer environments create example-environment \
        --location us-central1 \
        --image-version composer-1.20.12-airflow-1.10.15 \
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
    

## Step 7. (Optional) Specify Airflow configuration overrides and environment variables

You can set up [Airflow configuration overrides](https://docs.cloud.google.com/composer/docs/composer-1/override-airflow-configurations) and [environment variables](https://docs.cloud.google.com/composer/docs/composer-1/set-environment-variables) when you create an environment. As an alternative, you can do it later, after your environment is created.

Some Airflow configuration options [are blocked](https://docs.cloud.google.com/composer/docs/airflow-configurations) and you can't override them.

For the list of available Airflow configuration options, see [Configuration reference for Airflow 2](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html) and [Airflow 1.10.*](https://airflow.apache.org/docs/apache-airflow/1.10.15/configurations-ref.html)

To specify Airflow configuration overrides and environment variables:

###  Console 

On the **Create environment** page:

  1. Expand the **Networking, Airflow config overrides, and additional features** item.

  2. In the **Environment variables** section, click **Add environment variable**.

  3. Enter the **Name** and **Value** for the environment variable.

  4. In the **Airflow configuration overrides** section, click **Add Airflow configuration override**.

  5. Enter the **Section** , **Key** , and **Value** for the configuration option override.

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
        --image-version composer-1.20.12-airflow-1.10.15 \
        --service-account "SERVICE_ACCOUNT" \
        --env-variables ENV_VARS \
        --airflow-configs CONFIG_OVERRIDES
    

Replace:

  * `ENV_VARS` with a list of comma-separated `NAME=VALUE` pairs for environment variables.
  * `CONFIG_OVERRIDES` with a list of comma-separated `SECTION-KEY=VALUE` pairs for configuration overrides. Separate the name of the configuration section with a `-` symbol, followed by the key name. For example: `core-dags_are_paused_at_creation`.



Example:
    
    
    gcloud composer environments create example-environment \
        --location us-central1 \
        --image-version composer-1.20.12-airflow-1.10.15 \
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
    

## Step 8. (Optional) Specify maintenance windows

By default, Managed Airflow (Legacy Gen 1) environments do not have defined [maintenance windows](https://docs.cloud.google.com/composer/docs/composer-1/specify-maintenance-windows) if you create them using Google Cloud console, API, or Terraform. We recommend to specify maintenance windows for your new and existing environments.

If you create your environment using gcloud CLI, your environment has default maintenance windows from 00:00:00 to 04:00:00 (GMT) on Friday, Saturday, and Sunday every week.

To specify custom maintenance windows for your environment:

###  Console 

On the **Create environment** page:

  1. Expand the **Networking, Airflow config overrides, and additional features** item.

  2. In the **Maintenance windows** section, select the **Set custom time for maintenance windows** checkbox.

  3. In the **Timezone** drop-down list, choose a time zone for maintenance windows.

  4. Set **Start time** , **Days** , and **Length** , so that combined time for the specified schedule is at least 12 hours in a 7-day rolling window. For example, a period of 4 hours every Monday, Wednesday, and Friday provides the required amount of time.




###  gcloud 

The following arguments define maintenance windows parameters:

  * `--maintenance-window-start` sets the start time of a maintenance window.
  * `--maintenance-window-end` sets the end time of a maintenance window.
  * `--maintenance-window-recurrence` sets the [maintenance window recurrence](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions#maintenance-window).


    
    
    gcloud composer environments create ENVIRONMENT_NAME \
        --location LOCATION \
        --image-version composer-1.20.12-airflow-1.10.15 \
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
      --image-version composer-1.20.12-airflow-1.10.15 \
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
    

## Step 9. (Optional) Configure data encryption (CMEK)

By default, data in your environment is encrypted with a key provided by Google.

To use customer-managed encryption keys (CMEK) to encrypt data in your environment, follow the instructions outlined in [Using customer-managed encryption keys](https://docs.cloud.google.com/composer/docs/composer-1/configure-cmek-encryption).

## Step 10. (Optional) Specify environment labels

You can assign labels to your environments to [break down billing costs based on these labels](https://docs.cloud.google.com/composer/docs/composer-1/manage-environment-labels).

###  Console 

On the **Create environment** page:

  1. Expand the **Networking, Airflow config overrides, and additional features** item.

  2. In the **Labels** section, click **Add label**.

  3. In **Key** and **Value** fields, specify key and value pairs for the environment labels.




###  gcloud 

When you create an environment, the `--labels` argument specifies a comma-separated list of keys and values with environment labels.
    
    
    gcloud composer environments create ENVIRONMENT_NAME \
        --location LOCATION \
        --image-version composer-1.20.12-airflow-1.10.15 \
        --service-account "SERVICE_ACCOUNT" \
        --labels LABELS
    

Replace:

  * `LABELS` with a list of comma-separated `KEY=VALUE` pairs for environment labels.



Example:
    
    
    gcloud composer environments create example-environment \
        --location us-central1 \
        --image-version composer-1.20.12-airflow-1.10.15 \
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
    

## Step 11. (Optional) Configure other parameters

Other parameters include:

  * Zone for your environment nodes

Compute Engine zone in which to deploy cluster nodes. In this parameter, you can select a specific zone in the location of your environment.

By default, a random zone is selected automatically.

  * OAuth scopes

OAuth scopes are a set of [Google API scopes](https://developers.google.com/identity/protocols/oauth2/scopes) to be made available on all node VMs. If empty, defaults to `https://www.googleapis.com/auth/cloud-platform`.

If you specify custom OAuth scopes, include `https://www.googleapis.com/auth/cloud-platform` in the list of specified scopes.

  * Python version

If your environment uses Airflow 1.10.* and earlier Airflow versions, you can make your environment use Python 2. The default Python version is Python 3. For more information about Python 2 support in Managed Airflow, see [Supported Python versions](https://docs.cloud.google.com/composer/docs/python-version).




###  Console 

On the **Create environment** page:

  1. In the **Node configuration** section:

     * In the **Zone** drop-down list, select a zone for your environment nodes.

You can't change zone later.

     * In the **OAuth Scopes** field, specify OAuth scopes for node VMs.

You can't change OAuth scopes later.

To specify several OAuth scopes, provide a comma-separated list of values. Include `https://www.googleapis.com/auth/cloud-platform` in the list of specified scopes.

     * In the **Python version** field, choose the version of Python.

You can't change the Python version later.




###  gcloud 

When you create an environment, following arguments control miscellaneous parameters of your environment:

  * `--zone` specifies a Compute Engine zone for your environment VMs.

  * `--oauth-scopes` specifies a comma-separted list of OAuth scopes. Include `https://www.googleapis.com/auth/cloud-platform` in the list of specified scopes.

  * `--python-version` specifies the version of Python.



    
    
    gcloud composer environments create ENVIRONMENT_NAME \
        --location LOCATION \
        --image-version composer-1.20.12-airflow-1.10.15 \
        --service-account "SERVICE_ACCOUNT" \
        --zone ZONE \
        --oauth-scopes OAUTH_SCOPES \
        --python-version PYTHON_VERSION
    

Replace:

  * `ZONE` with the name of the Compute Engine zone.
  * `OAUTH_SCOPES` with a comma-separated list of OAuth scopes.
  * `PYTHON_VERSION` with the Python version (`3` or `2`).



Example:
    
    
    gcloud composer environments create example-environment \
        --location us-central1 \
        --image-version composer-1.20.12-airflow-1.10.15 \
        --service-account "
    example-account@example-project.iam.gserviceaccount.com
    " \
        --zone us-central1-a \
        --oauth-scopes https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/bigquery  \
        --python-version 3
    

###  API 

When you create an environment, in the [Environment](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments#Environment) > [EnvironmentConfig](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments#EnvironmentConfig) resource, specify miscellaneous parameters of your environment.
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/environments/ENVIRONMENT_NAME",
      "config": {
        "nodeConfig": {
          "location": "projects/PROJECT_ID/zones/ZONE",
          "oauthScopes": [
            "OAUTH_SCOPE"
          ],
          "serviceAccount": "SERVICE_ACCOUNT"
        },
        "softwareConfig": {
            "pythonVersion": "PYTHON_VERSION"
        }
      }
    }
    

Replace:

  * `ZONE` with the name of the Compute Engine zone.
  * `OAUTH_SCOPE` with an OAuth scope. To specify additional scopes, add the `https://www.googleapis.com/auth/cloud-platform` scope, followed by the additional scope items. scopes.
  * `PYTHON_VERSION` with the Python version (`3` or `2`).



Example:
    
    
    // POST https://composer.googleapis.com/v1/{parent=projects/*/locations/*}/environments
    
    {
      "name": "projects/example-project/locations/us-central1/environments/example-environment",
      "config": {
        "nodeConfig": {
          "location": "projects/example-project/zones/us-central1-a",
          "oauthScopes": [
            "https://www.googleapis.com/auth/cloud-platform",
            "https://www.googleapis.com/auth/bigquery"
          ],
          "serviceAccount": "
    example-account@example-project.iam.gserviceaccount.com
    "
        },
        "softwareConfig": {
            "pythonVersion": "3"
        }
      }
    }
    

###  Terraform 

When you create an environment, following fields control miscellaneous parameters of your environment:

  * `zone` field in the `node_config` block specifies a Compute Engine zone for your environment VMs.

  * `oauth_scopes` field in the `node_config` block specifies a comma-separated list of OAuth scopes.

  * `python_version` field in the `software_config` block specifies the version of Python.



    
    
    resource "google_composer_environment" "example" {
      name = "ENVIRONMENT_NAME"
      region = "LOCATION"
    
      config {
    
        node_config {
          zone = "ZONE"
          oauth_scopes = "[OAUTH_SCOPES]"
          service_account = "SERVICE_ACCOUNT"
        }
    
        software_config {
          python_version = "PYTHON_VERSION"
        }
      }
    }
    

Replace:

  * `ZONE` with the name of the Compute Engine zone.
  * `OAUTH_SCOPES` with a comma-separated list of OAuth scopes.
  * `PYTHON_VERSION` with the Python version (`3` or `2`).



Example:
    
    
    resource "google_composer_environment" "example" {
      name = "example-environment"
      region = "us-central1"
    
      config {
        node_config {
          zone = "us-central1-a"
          oauth_scopes = "[https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/bigquery]"
          service_account = "
    example-account@example-project.iam.gserviceaccount.com
    "
        }
        software_config {
          python_version = "3"
        }
      }
    }
    

## Step 12. (Optional) Enforce Beta API usage

**Preview — Enforcing beta API usage**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can explicitly make your environment use beta Cloud Composer API API, even if your environment does not have any preview features. If you do so, your environment is created using the `v1beta1` service endpoint.

###  Console 

On the **Create environment** page:

  1. Expand the **Networking, Airflow config overrides, and additional features** item.

  2. In the **Beta API** section, select the **Enforce the usage of Beta API** checkbox.




###  gcloud 

Create your environment using the [`gcloud beta composer`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/composer/environments/create) command.

###  API 

Create your environment using the [`v1beta1`](https://docs.cloud.google.com/composer/docs/reference/rest/v1beta1/projects.locations.environments/create) service endpoint.

###  Terraform 

The Terraform provider for Managed Airflow uses beta API by default.

## What's next

  * [Troubleshooting environment creation](https://docs.cloud.google.com/composer/docs/composer-1/troubleshooting-environment-creation)
  * [Configuring Shared VPC](https://docs.cloud.google.com/composer/docs/composer-1/configure-shared-vpc)
  * [Configuring VPC Service Controls](https://docs.cloud.google.com/composer/docs/composer-1/configure-vpc-sc)
  * [Adding and updating DAGs](https://docs.cloud.google.com/composer/docs/composer-1/manage-dags)
  * [Accessing Airflow UI](https://docs.cloud.google.com/composer/docs/composer-1/access-airflow-web-interface)
  * [Updating and deleting environments](https://docs.cloud.google.com/composer/docs/composer-1/update-environments)
  * [About Managed Airflow versions](https://docs.cloud.google.com/composer/docs/composer-versioning-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
