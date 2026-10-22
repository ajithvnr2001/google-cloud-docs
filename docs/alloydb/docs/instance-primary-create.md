---
url: https://docs.cloud.google.com/alloydb/docs/instance-primary-create/
title: Create a primary instance \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:29:07.327995+00:00
---

# Create a primary instance  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/instance-primary-create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Create a primary instance Stay organized with collections  Save and categorize content based on your preferences. 

To support read and write workloads in an AlloyDB for PostgreSQL cluster, you can create a primary instance by using the Google Cloud console, the Google Cloud CLI, Terraform, or the AlloyDB API. The primary instance provides the compute resources that process transactions and coordinate read and write operations for your cluster.

## Before you begin

  * The Google Cloud project you are using must have been [enabled to access AlloyDB](https://docs.cloud.google.com/alloydb/docs/quickstart/create-and-connect#before-you-begin). 
  * You must have one of these IAM roles in the Google Cloud project you are using: 
    * `roles/alloydb.admin` (the AlloyDB Admin predefined IAM role)
    * `roles/owner` (the Owner basic IAM role)
    * `roles/editor` (the Editor basic IAM role)

If you don't have any of these roles, contact your Organization Administrator to request access.




## Create an AlloyDB primary instance

###  Console 

  1. Go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click a cluster in the **Resource Name** column.

  3. In the **Overview** page, go to **Instances in your cluster** , and click **Create primary instance**.

  4. Configure your primary instance:

     1. In the **Instance ID** field, enter an ID for your primary instance.
     2. Under **Zonal availability** , select one of the following options: 
        1. To create a highly available production instance with automated failover, select **Multiple zones (Highly available)**.
        2. To create a basic instance that does not need to be highly available, select **Single zone**.
     3. Select one of the following machine series:

        * C4A (Google Axion-based machine series)
        * N2 (x86-based machine series). This is the default machine series.
        * C4 (x86-based machine series)
        * Z3 (Intel Xeon-based machine series)
     4. Select a machine type.

        * C4A supports 1, 2, 4, 8, 16, 32, 48, 64, and 72 vCPUs
        * N2 supports 2, 4, 8, 16, 32, 64, 96, and 128 vCPUs
        * C4 supports 4, 8, 16, 24, 32, 48, 96, 144, 192, and 288 vCPUs
        * Z3 supports 8, 14, 16, 22, 32, 44, and 88 vCPUs
     5. Optional: To connect your applications and clients over the public internet, check the box **Enable Public IP** under **Public IP Connectivity**. Enabling public IP might require additional configuration to make sure that you have a secure connection. For more information, see [Connect using public IP](https://docs.cloud.google.com/alloydb/docs/connect-public-ip).

By default, private IP is always enabled. For more information, see [Enable private services access](https://docs.cloud.google.com/alloydb/docs/configure-connectivity).

     6. Optional: To enable managed connection pooling, select **Enable managed connection pool** under **Managed connection pool**. For more information, see [Configure managed connection pooling](https://docs.cloud.google.com/alloydb/docs/configure-managed-connection-pooling).

     7. Optional: To set custom flags for your instance, expand **Advanced configuration options** , then do the following for each flag:

        1. Click **Add flag**.
        2. Select a flag from the **New database flag** list.
        3. Provide a value for the flag.
        4. Click **Done**.
     8. Optional: To configure SSL or connector requirements on the instance, expand **Advanced configuration options** , then do the following:

        1. By default, AlloyDB instances require all connections to use SSL encryption. To allow non-SSL connections, clear the **Only allow SSL connections** checkbox.
        2. To require that all database connections to the instance use the AlloyDB Auth Proxy or the secure connector libraries provided by Google, select **Enforce mTLS via AlloyDB connectors**.
  5. Click **Create instance**.




###  gcloud 

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

Use the [`gcloud alloydb instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/create) command to create a primary instance.
    
    
    gcloud alloydb instances create INSTANCE_ID \
        --instance-type=PRIMARY \
        --availability-type=AVAILABILITY \
        --region=REGION_ID \
        --cluster=CLUSTER_ID \
        --cpu-count=CPU_COUNT \
        --machine-type=MACHINE_TYPE \
        --project=PROJECT_ID

  * `INSTANCE_ID`: The ID of the instance you are creating. It must begin with a lowercase letter and can contain lowercase letters, numbers, and hyphens.
  * `AVAILABILITY`: Whether or not this instance should be highly available (HA), with nodes in multiple zones. Valid values include: 
    * `REGIONAL`: Creates an HA instance with separate active and standby nodes, and automated failover between them. This is the default value, suitable for production environments.
    * `ZONAL`: Creates a basic instance, containing only one node, and no automated failover.
  * `REGION_ID`: The region where you want the instance placed. For example, `us-central1`.
  * `CLUSTER_ID`: The ID of the cluster where you want the instance placed.
  * `CPU_COUNT`: the number of vCPUs that you want for the instance.

    * You must specify either `cpu_count` or `machine_type`.
    * If only `cpu_count` is provided, an N2 instance is created with the following specifications: 
      * 2: 2 vCPUs, 16 GB RAM
      * 4: 4 vCPUs, 32 GB RAM
      * 8: 8 vCPUs, 64 GB RAM
      * 16: 16 vCPUs, 128 GB RAM
      * 32: 32 vCPUs, 256 GB RAM
      * 64: 64 vCPUs, 512 GB RAM
      * 96: 96 vCPUs, 768 GB RAM
      * 128: 128 vCPUs, 864 GB RAM
    * If both `machine_type` and `cpu_count` are provided, the `cpu_count` value must align with the number of vCPUs specified in the `machine_type`. For example, if `machine_type` is `n2-highmem-4`, then you must set `cpu_count` to `4`.
  * `MACHINE_TYPE`: Select from a list of supported machine-types such as `n2-highmem-4`, `c4-highmem-4-lssd`, or `c4a-highmem-4-lssd`. For more information, see [Choose an AlloyDB machine type.](https://docs.cloud.google.com/alloydb/docs/choose-machine-type)

When you use `machine_type` and `cpu_count` together, the values in `cpu_count` and `machine_type` must match. For example, if `machine_type` is `n2-highmem-4`, then you must set `cpu_count` to `4`.

  * `PROJECT_ID`: The ID of the project where the cluster is placed.




By default, new instances require all connections to use SSL encryption. To allow non-SSL connections to the instance, add the `--ssl-mode=ALLOW_UNENCRYPTED_AND_ENCRYPTED` flag to the command:
    
    
    gcloud alloydb instances create INSTANCE_ID \
      --instance-type=PRIMARY \
      --region=REGION_ID \
      --cluster=CLUSTER_ID \
      --project=PROJECT_ID \
      --cpu-count=CPU_COUNT \
      --machine-type=MACHINE_TYPE \
      --ssl-mode=ALLOW_UNENCRYPTED_AND_ENCRYPTED

To enforce a secure connection between the client and an AlloyDB instance through the Auth Proxy or other applications that use Google-provided connector libraries, add the `--require-connectors` flag to the command:
    
    
    gcloud alloydb instances create INSTANCE_ID \
     --instance-type=PRIMARY \
     --region=REGION_ID \
     --cluster=CLUSTER_ID \
     --cpu-count=CPU_COUNT \
     --machine-type=MACHINE_TYPE \
     --project=PROJECT_ID \
     --require-connectors

To enable managed connection pooling in your AlloyDB instance, add the `--enable-connection-pooling` flag to the [`gcloud alloydb instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/create) command:
    
    
    gcloud alloydb instances create INSTANCE_ID \
      --instance-type=PRIMARY \
      --region=REGION_ID \
      --cluster=CLUSTER_ID \
      --cpu-count=CPU_COUNT \
      --machine-type=MACHINE_TYPE \
      --project=PROJECT_ID \
      --enable-connection-pooling

You can also create an AlloyDB instance with Private Service Connect-enabled. For information about creating a primary instance for a Private Service Connect-enabled cluster, see [Create an AlloyDB instance](https://docs.cloud.google.com/alloydb/docs/configure-private-service-connect#create-cluster).

###  Terraform 

**Warning:** To keep your Terraform state consistent, update configurations directly in your Terraform files. If you make manual changes using the Google Cloud console, gcloud CLI, or REST API, the following issues can occur: 

  * API errors
  * Perpetual diffs
  * Overwritten changes during `terraform apply`



### Create an instance

To create an instance within your database cluster, use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/alloydb_instance).
    
    
    resource "google_alloydb_instance" "default" {
      cluster       = google_alloydb_cluster.default.name
      instance_id   = "alloydb-instance"
      instance_type = "PRIMARY"
    
      machine_config {
        cpu_count = 2
      }
    
      depends_on = [google_service_networking_connection.vpc_connection]
    }
    
    resource "google_alloydb_cluster" "default" {
      cluster_id = "alloydb-cluster"
      location   = "us-central1"
      network_config {
        network = google_compute_network.default.id
      }
    
      initial_user {
        password = "alloydb-cluster"
      }
    }
    
    data "google_project" "project" {}
    
    resource "google_compute_network" "default" {
      name = "alloydb-network"
    }
    
    resource "google_compute_global_address" "private_ip_alloc" {
      name          =  "alloydb-cluster"
      address_type  = "INTERNAL"
      purpose       = "VPC_PEERING"
      prefix_length = 16
      network       = google_compute_network.default.id
    }
    
    resource "google_service_networking_connection" "vpc_connection" {
      network                 = google_compute_network.default.id
      service                 = "servicenetworking.googleapis.com"
      reserved_peering_ranges = [google_compute_global_address.private_ip_alloc.name]
    }
    

This example creates an N2 instance. For a list of other supported machine-types such as `n2-highmem-4`, `c4-highmem-4-lssd`, or `c4a-highmem-4-lssd`, see [Choose an AlloyDB machine type.](https://docs.cloud.google.com/alloydb/docs/choose-machine-type)

### Prepare Cloud Shell

To apply your Terraform configuration in a Google Cloud project, prepare Cloud Shell as follows:

  1. Launch [Cloud Shell](https://shell.cloud.google.com/).
  2. Set the default Google Cloud project where you want to apply your Terraform configurations.

You only need to run this command once per project, and you can run it in any directory.
         
         export GOOGLE_CLOUD_PROJECT=PROJECT_ID

Environment variables are overridden if you set explicit values in the Terraform configuration file.




### Prepare the directory

Each Terraform configuration file must have its own directory, also called a _root module_.

  1. In [Cloud Shell](https://shell.cloud.google.com/), create a directory and a new file within that directory. The filename must be a TF file—for example, `main.tf`. In this document, the file is referred to as `main.tf`. 
         
         mkdir DIRECTORY && cd DIRECTORY && touch main.tf

  2. Copy the sample code into the newly created `main.tf`. Optionally, copy the code from GitHub. This is recommended when the Terraform snippet is part of an end-to-end solution. 
         
         git clone https://github.com/terraform-google-modules/terraform-docs-samples

  3. In the `terraform-docs-samples` directory, navigate to the `alloydb` directory. 
         
         cd terraform-docs-samples/alloydb

  4. Copy the sample code into the newly created `main.tf`. 
         
         cp SAMPLE_FILE main.tf

Replace `<var>SAMPLE_FILE</var>` with the name of the sample file to copy—for example, `main.tf`.
  5. Review and modify the sample parameters to apply to your environment.
  6. Save your changes.
  7. Initialize Terraform. You only need to do this once per directory. 
         
         terraform init

Optional: To use the latest Google provider version, include the `-upgrade` option: 
         
         terraform init -upgrade




### Apply the changes

**Note:** Terraform samples typically assume that the required APIs are enabled in your Google Cloud project. 

  1. Review the configuration to confirm that the Terraform updates match your expectations: 
         
         terraform plan

Make corrections to the configuration as necessary.
  2. Apply the Terraform configuration by running the following command and entering `yes` at the prompt: 
         
         terraform apply

Wait until Terraform displays the `Apply complete!` message.



[Open your Google Cloud project](https://console.cloud.google.com/) to view the results. In the Google Cloud console, navigate to your resources in the UI to make sure that Terraform has created or updated them.

###  REST v1 

### Create an instance

This example creates a primary instance. For a complete list of parameters for this call, see [Method: projects.locations.clusters.instances.create](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters.instances/create). For information about cluster settings, see [View cluster and instance settings](https://docs.cloud.google.com/alloydb/docs/reference/cluster-settings?resource=primary).

Don't include sensitive or personally identifiable information in your cluster ID, because it's externally visible. You don't need to include the project ID in the cluster name because this is done automatically where appropriate—for example, in the log files.

To send your request, save the request body in a file named `instance_request.json`.
    
    
    {
      "instance_type": "PRIMARY",
      "machine_config": {
        "cpu_count": CPU_COUNT
      }
    }
    

Make the following replacement:

  * `CPU_COUNT`: the number of visible CPU cores on the instance that you want to create.



The preceding example creates an N2 instance with the following specifications:

  * 2: 2 vCPUs, 16 GB RAM
  * 4: 4 vCPUs, 32 GB RAM
  * 8: 8 vCPUs, 64 GB RAM
  * 16: 16 vCPUs, 128 GB RAM
  * 32: 32 vCPUs, 256 GB RAM
  * 64: 64 vCPUs, 512 GB RAM
  * 96: 96 vCPUs, 768 GB RAM
  * 128: 128 vCPUs, 864 GB RAM


    
    
    "machine_config": {
      "machine_type": "MACHINE_TYPE"
    }
    

Replace `MACHINE_TYPE` with a supported machine type such as `n2-highmem-4`, `c4-highmem-4-lssd`, or `c4a-highmem-4-lssd`. For more information about supported machine types, see [Choose an AlloyDB machine type.](https://docs.cloud.google.com/alloydb/docs/choose-machine-type)

Use the following HTTP method and URL:
    
    
    POST https://alloydb.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/clusters/CLUSTER_ID/instances?instance_id=INSTANCE_ID
    

Make the following replacements:

  * `PROJECT_ID`: the ID of the project where you want the cluster located.
  * `LOCATION_ID`: the ID of the cluster's region.
  * `CLUSTER_ID`: the ID of the cluster that you create. The ID must begin with a lowercase letter and can contain lowercase letters, numbers, and hyphens.
  * `INSTANCE_ID`: the name of the primary instance that you want to create.



You can use curl to execute the request, as shown in the following example:
    
    
    curl -X POST   -H "Authorization: Bearer $(gcloud auth print-access-token)"   -H "Content-Type: application/json"   https://alloydb.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/clusters/CLUSTER_ID/instances?instance_id=INSTANCE_ID   -d @instance_request.json
    

## What's next

  * [Create a read pool instance](https://docs.cloud.google.com/alloydb/docs/instance-read-pool-create).

  * [Reduce costs using basic instances](https://docs.cloud.google.com/alloydb/docs/basic-instance).

  * [Learn about sizing recommendations](https://docs.cloud.google.com/alloydb/docs/use-sizing-recommendations).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
