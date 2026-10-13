---
url: https://docs.cloud.google.com/alloydb/docs/cluster-create/
title: Create a cluster and its primary instance \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:53:03.025824+00:00
---

# Create a cluster and its primary instance  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/cluster-create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Create a cluster and its primary instance Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to perform a complete AlloyDB for PostgreSQL cluster setup. You learn how to create a new AlloyDB cluster and its primary instance using the Google Cloud console, the Google Cloud CLI, the REST API, or Terraform.

## Before you begin

  * The Google Cloud project you are using must be [enabled to access AlloyDB](https://docs.cloud.google.com/alloydb/docs/project-enable-access).
  * A VPC network in the Google Cloud project that you are using must already be [configured for private services access](https://docs.cloud.google.com/alloydb/docs/configure-connectivity) to AlloyDB.
  * For development and sandbox workloads, consider your region and machine type. To use the 1 vCPU shape, make sure that you select a region that supports that shape. For more information, see Considerations when using 1 vCPU.



### Required roles

Before you can create your first postgres cluster, you must have the correct Identity and Access Management (IAM) roles.

  * You must have one of these IAM roles in the Google Cloud project that you're using: 
    * `roles/alloydb.admin` (the AlloyDB Admin predefined IAM role)
    * `roles/owner` (the Owner basic IAM role)
    * `roles/editor` (the Editor basic IAM role)
  * If you don't have any of these roles, contact your Organization Administrator to request access.
  * You must also have the `compute.networks.list` permission in the Google Cloud project you are using. To gain this permission while following the principle of least privilege, ask your administrator to grant you the Compute Network User (`roles/compute.networkUser`) role.



## Create a new cluster and primary instance

###  Console 

  1. Go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click **Create cluster**.

  3. Choose a cluster configuration. For more information about the difference between highly available and basic configurations, see [Nodes and instances](https://docs.cloud.google.com/alloydb/docs/overview#instances).

If you're not sure whether your new cluster needs read pool instances, choose one of the configurations with no read pools. You can add read pool instances to the cluster later, whenever needed.

  4. Click **Continue**.

  5. In the **Configure your cluster** section, in the **Cluster ID** field, enter an ID for your cluster.

  6. In the **Password** field, enter an initial password for the new cluster. AlloyDB assigns the provided password to the `postgres` database user while creating the cluster.

  7. Optional: To set the `alloydb.iam_authentication` flag manually, deselect **Create an IAM database user**. For more information, see [Configure database flags](https://docs.cloud.google.com/alloydb/docs/instance-configure-database-flags).

By default, **Create an IAM database user** is selected, which does the following:

     * Enables the `alloydb.iam_authentication` flag on the primary instance.

     * Creates an IAM database user for you.

  8. In the **Database version** field, select the major version of PostgreSQL for your new AlloyDB cluster.

  9. Select a region. For developmental and sandbox workloads, consider the 1 vCPU shape, which is available in selected regions. For more information, see Considerations when using 1 vCPU.

  10. Select a network path.

  11. Optional: To apply a specific IP address range to this cluster, instead of allowing AlloyDB to choose an IP address range, follow these steps:

     1. Click **Show allocated IP range option**.

     2. From the **Allocated IP range** list, select an IP address range.

For more information about this option, see Create a cluster with a specific IP address range.

  12. Optional: To encrypt this cluster using a [customer-managed encryption key (CMEK)](https://docs.cloud.google.com/alloydb/docs/cmek) instead of Google-managed encryption, follow these additional steps:

     1. Click **Advanced encryption options**.

     2. Select **Customer-managed encryption key (CMEK)**.

     3. In the menu that appears, select a customer-managed key.

The Google Cloud console limits this list to keys within the same Google Cloud project and region as the new cluster. To use a key that is not on this list, click **Don't see your key? Enter key resource name** , and then type the key's resource name into the resulting dialog.

Note that using CMEK with AlloyDB requires some additional setup. For more information, see [Using CMEK with AlloyDB](https://docs.cloud.google.com/alloydb/docs/use-cmek).

     4. Click **Continue**.

  13. Configure your primary instance:

     1. In the **Instance ID** field, enter an ID for your primary instance.
     2. Select one of the following machine series:

        * C4A (Google Axion-based machine series).
        * N2 (x86-based machine series). This is the default machine series.
        * C4 (x86-based machine series).
        * Z3 (Intel Xeon-based machine series).
     3. Select a machine type. For more information, see [Choose a machine type](https://docs.cloud.google.com/alloydb/docs/choose-machine-type).

        * C4A supports 1, 2, 4, 8, 16, 32, 48, 64, and 72 vCPUs.
        * N2 supports 2, 4, 8, 16, 32, 64, 96, and 128 vCPUs.
        * C4 supports 4, 8, 16, 24, 32, 48, 96, 144, 192, and 288 vCPUs.
        * Z3 supports 8, 14, 16, 22, 32, 44, and 88 vCPUs.

For more information about using C4A Axion-based machine series, including the 1 vCPU machine type see Considerations when using the C4A Axion-based machine series.

     4. Optional: Set custom flags for your instance. For each flag, follow these steps:

        1. Click **Add flag**.
        2. In the **New database flag** list, select a flag.
        3. Provide a value for the flag.
        4. Click **Done**.
  14. Click **Create cluster**.

**Note:** After you create your cluster, you can monitor cluster and instance health using prioritized health issues in the Google Cloud console. For more information, see [Monitor the health of your AlloyDB clusters and instances](https://docs.cloud.google.com/alloydb/docs/monitor-health-clusters-instances).



###  gcloud 

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

You must create both an AlloyDB cluster and primary instance before you start using AlloyDB.

### Create a cluster

  1. To create the cluster with either private service access or Private Service Connect enabled, use the [`gcloud alloydb clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/clusters/create) command.

### Private services access
         
         gcloud alloydb clusters create CLUSTER_ID \
             --database-version=POSTGRES_VERSION \
             --password=PASSWORD \
             --region=REGION_ID \
             --project=PROJECT_ID \
             --network=NETWORK

### Private Service Connect
         
         gcloud alloydb clusters create CLUSTER_ID \
             --database-version=POSTGRES_VERSION \
             --password=PASSWORD \
             --region=REGION_ID \
             --project=PROJECT_ID \
             --enable-private-service-connect

Replace the following:

     * `CLUSTER_ID`: the ID of the cluster that you are creating. It must begin with a lowercase letter and can contain lowercase letters, numbers, and hyphens.

     * `VERSION`: the major version of PostgreSQL that you want the cluster's database servers to be compatible with. Choose one of the following:

       * `14`, for compatibility with PostgreSQL 14

       * `15`, for compatibility with PostgreSQL 15

       * `16`, for compatibility with PostgreSQL 16

       * `17`, for compatibility with PostgreSQL 17, which is the default PostgreSQL version supported

       * `18`, for compatibility with PostgreSQL 18

     * `PASSWORD`: the password to use for the default `postgres` user.

     * `NETWORK` (Optional): the name of the VPC network [that you configured for private services access](https://docs.cloud.google.com/alloydb/docs/configure-connectivity) to AlloyDB. If you omit the `--network` flag, AlloyDB uses the `default` network.

In case of Shared VPC network, set to the fully qualified path of the VPC network—for example, `projects/cymbal-project/global/networks/shared-vpc-network`.

     * `--enable-private-service-connect` (Optional): set to enable Private Service Connect as the connectivity method for the cluster and its instances.

     * `REGION_ID`: the region where you want the cluster placed.

**Note:** For developmental and sandbox workloads, consider the 1 vCPU shape, which is available in selected regions. For more information, see Considerations when using 1 vCPU.
     * `PROJECT_ID`: the ID of the project where you want the cluster placed.

This command initiates a long-running operation, returning an operation ID.

  2. Optional: To apply a specific IP address range to this cluster, instead of allowing AlloyDB to choose an IP address range, provide the following argument:
         
         --allocated-ip-range-name=RANGE
         

Replace `RANGE` with the name of the IP address range that you want this cluster to use for private services access.

For more information about this option, see Create a cluster with a specific IP address range.

  3. Optional: To encrypt this cluster using a [customer-managed encryption key (CMEK)](https://docs.cloud.google.com/alloydb/docs/cmek) instead of the default Google-managed encryption, provide the following arguments:
         
         --kms-key=KEY_ID \
         --kms-keyring=KEYRING_ID \
         --kms-location=LOCATION_ID \
         --kms-project=PROJECT_ID
         

Replace the following:

     * `KEY_ID`: the ID of the CMEK key to use.

     * `KEYRING_ID`: the ID of the key's key ring.

     * `LOCATION_ID`: the ID of the key ring's region, which must be the same as the cluster's region.

     * `PROJECT_ID`: the ID of the key ring's project.

**Note:** Using CMEK requires some additional setup. For more information, see [Using CMEK with AlloyDB](https://docs.cloud.google.com/alloydb/docs/use-cmek).
  4. Confirm that the operation was successful.
         
         gcloud alloydb operations describe OPERATION_ID \
             --region=REGION_ID \
             --project=PROJECT_ID

Replace `OPERATION_ID` with the operation ID that was returned from the previous step.




After creating the primary cluster, you must create a primary instance.

### Create a primary instance

To create a primary instance, use the [`gcloud alloydb instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/create) command.
    
    
        gcloud alloydb instances create INSTANCE_ID \
            --instance-type=PRIMARY \
            --region=REGION_ID \
            --cluster=CLUSTER_ID \
            --project=PROJECT_ID \
            --cpu-count=CPU_COUNT \
            --machine-type=MACHINE_TYPE \
            --allowed-psc-projects=ALLOWED_PROJECT_LIST

Replace the following:

  * `INSTANCE_ID`: the ID of the instance you are creating. It must begin with a lowercase letter and can contain lowercase letters, numbers, and hyphens.

  * `REGION_ID`: the region where you want the instance located.

  * `CLUSTER_ID`: the ID of the cluster you created earlier.

  * `PROJECT_ID`: the ID of the project where your cluster was created.

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

  * `ALLOWED_PROJECT_LIST`: (Optional) if you're using Private Service Connect, `ALLOWED_PROJECT_LIST` is the comma-separated list of project IDs or the [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) that you want to allow access the instance.




###  Terraform 

**Warning:** To keep your Terraform state consistent, update configurations directly in your Terraform files. If you make manual changes using the Google Cloud console, gcloud CLI, or REST API, the following issues can occur: 

  * API errors
  * Perpetual diffs
  * Overwritten changes during `terraform apply`



### Create a cluster and a primary instance

To create a cluster and its primary instance, use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/alloydb_instance).

The following is a code snippet for creating a cluster and a primary instance based on the [AlloyDB instance full](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/alloydb_instance#example-usage---alloydb-instance-basic) example:
    
    
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
      cluster_id       = "alloydb-cluster"
      location         = "us-central1"
      network_config {
        network = google_compute_network.default.id
      }
      database_version = "POSTGRES_16"
      initial_user {
        password = "alloydb-cluster"
      }
    }
    
    data "google_project" "project" {}
    
    resource "google_compute_network" "default" {
      name = "alloydb-network"
    }
    
    resource "google_compute_global_address" "private_ip_alloc" {
      name          = "alloydb-cluster"
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
  3. Review the `main.tf` file and modify the sample parameters to apply to your environment.
  4. Save your changes.
  5. Initialize Terraform. You only need to do this once per directory. 
         
         terraform init

Optional: To use the latest Google provider version, include the `-upgrade`option: 
         
         terraform init -upgrade




### Apply the changes

**Note:** Terraform samples typically assume that the required APIs are enabled in your Google Cloud project. 

  1. Review the configuration to confirm that the Terraform updates match your expectations: 
         
         terraform plan

Make corrections to the configuration as necessary.
  2. Apply the Terraform configuration by running the following command and entering `yes` at the prompt: 
         
         terraform apply

Wait until Terraform displays the `Apply complete!` message.
  3. [Open your Google Cloud project](https://console.cloud.google.com/) to view the results. In the Google Cloud console, navigate to your resources in the UI to make sure that Terraform has created or updated them.



###  REST v1 

### Create a cluster

This example creates a cluster. For a complete list of parameters for this call, see [Method: projects.locations.clusters.create](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters/create). For information about cluster settings, see [View cluster and instance settings](https://docs.cloud.google.com/alloydb/docs/cluster-settings?resource=primary).

Don't include sensitive or personally identifiable information in your cluster ID because it's externally visible. You don't need to include the project ID in the cluster name. This is done automatically where appropriate, for example, in the log files.

To send your request, save the request body in a file named `cluster_request.json`:
    
    
    {
      "databaseVersion": "<var>DATABASE_VERSION</var>",
      "initialUser": {
        "user": "<var>INITIAL_USERNAME</var>",
        "password": "<var>INITIAL_USER_PASSWORD</var>"
      },
      "labels": {
        "test": "alloydb-cluster-full"
      }
    }
    

Make the following replacements:

  * `DATABASE_VERSION`: enum string of the database version—for example, `POSTGRES_17`.
  * `INITIAL_USERNAME`: the username that you use for the default postgres user.
  * `INITIAL_USER_PASSWORD`: the password that you use for the default postgres user.



Use the following HTTP method and URL:
    
    
    POST https://alloydb.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/clusters?cluster_id=CLUSTER_ID
    

Make the following replacements:

  * `PROJECT_ID`: the ID of the project where you want the cluster located.
  * `LOCATION_ID`: the ID of the cluster's region.
  * `CLUSTER_ID`: the ID of the cluster that you create. The cluster ID must begin with a lowercase letter and can contain lowercase letters, numbers, and hyphens.



You can use the following curl to execute the preceding request:
    
    
    curl -X POST   -H "Authorization: Bearer $(gcloud auth print-access-token)"   -H "Content-Type: application/json"   https://alloydb.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION_ID/clusters?cluster_id=CLUSTER_ID   -d @cluster_request.json
    

### Create a primary instance

This example creates a primary instance. For a complete list of parameters for this call, see [Method: projects.locations.clusters.instances.create](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters.instances/create). For information about cluster settings, see [View cluster and instance settings](https://docs.cloud.google.com/alloydb/docs/cluster-settings?resource=primary).

Don't include sensitive or personally identifiable information in your cluster ID, because it's externally visible. You don't need to include the project ID in the cluster name because this is done automatically where appropriate —for example, in the log files.

To send your request, save the following request body in a file named `instance_request.json`.
    
    
    {
      "instance_type": "PRIMARY",
      "machine_config": {
        "cpu_count": "vCPU_COUNT"
      }
    }
    

Make the following replacement:

  * `VCPU_COUNT`: the number of visible CPU cores on the instance that you want to create.



The preceding example creates an N2 instance with the following specifications:

  * 2: 2 vCPUs, 16 GB RAM
  * 4: 4 vCPUs, 32 GB RAM
  * 8: 8 vCPUs, 64 GB RAM
  * 16: 16 vCPUs, 128 GB RAM
  * 32: 32 vCPUs, 256 GB RAM
  * 64: 64 vCPUs, 512 GB RAM
  * 96: 96 vCPUs, 768 GB RAM
  * 128: 128 vCPUs, 864 GB RAM



The following example shows how to create an instance for a machine type:
    
    
    machine_config: {
      machine_type : MACHINE_TYPE,
    },
    

Replace MACHINE_TYPE with a supported machine type such as `n2-highmem-4`, `c4-highmem-4-lssd`, or `c4a-highmem-4-lssd`. For more information about supported machine types, see [Choose an AlloyDB machine type.](https://docs.cloud.google.com/alloydb/docs/choose-machine-type)

Use the following HTTP method and URL:
    
    
    POST https://alloydb.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/clusters/CLUSTER_ID/instances?instance_id=INSTANCE_ID
    

Make the following replacements:

  * `PROJECT_ID`: the ID of the project where you want the cluster located.
  * `LOCATION_ID`: the ID of the cluster's region.
  * `CLUSTER_ID`: the ID of the cluster that you create. The ID must begin with a lowercase letter and it can contain lowercase letters, numbers, and hyphens.
  * `INSTANCE_ID`: the name of the primary instance that you want to create.



You can use curl to execute the request, as shown in the following example:
    
    
    curl -X POST   -H "Authorization: Bearer $(gcloud auth print-access-token)"   -H "Content-Type: application/json"   https://alloydb.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION_ID/clusters/CLUSTER_ID/instances?instance_id=INSTANCE_ID   -d @instance_request.json
    

## Clone an active cluster

To create a clone of an active cluster, containing a copy of all the source cluster's data and running in the same region, [perform a point-in-time recovery on that cluster](https://docs.cloud.google.com/alloydb/docs/backup/restore-pitr#cbr). You can specify a very recent point in time when doing so—for example, the first second of the current minute.

This process copies only the source cluster's data into the clone—not any of the source cluster's configuration. To encrypt the clone's data using CMEK, you need to specify CMEK details as part of the point-in-time recovery command, even if the source cluster's data is already CMEK-encrypted. After the new cluster is created, you need to add instances, database flags, backup schedules, and any other configuration necessary to suit your needs.

A cluster created this way exists independently of its source, with its data having no relationship to the source cluster's data after the initial duplication has completed. If you want to create secondary clusters that automatically track and replicate data changes made in their source clusters, see [About cross-region replication](https://docs.cloud.google.com/alloydb/docs/cross-region-replication/about-cross-region-replication).

## Create a cluster with a specific IP address range

AlloyDB uses private services access to allow a cluster's internal resources to communicate with each other. Before you can create a cluster, your Virtual Private Cloud (VPC) network must contain at least one IP address range [configured with a private services access connection](https://docs.cloud.google.com/alloydb/docs/about-private-services-access#supported).

## Considerations when using the C4A Axion-based machine series

AlloyDB offers a C4A machine series based on Google Axion, Google's custom Arm-based processor. C4A virtual machines (VM) are available as predefined configurations for 1, 2, 4, 8, 16, 32, 48, 64, and 72 vCPUs, with up to 576 GB of Double Data Rate 5 (DDR5) memory.

When you choose C4A, keep in mind the following:

  * To switch an existing N2 instance to a C4A instance, you modify the `machine_type` of the current instance using the Google Cloud console, the gcloud CLI, Terraform, or the API.
  * Don't delete the N2 instance and create a new C4A instance in the same cluster.



### C4A is supported in the following regions:

  * `asia-east1`
  * `asia-southeast1`
  * `europe-west1`
  * `europe-west2`
  * `europe-west3`
  * `europe-west4`
  * `us-central1`
  * `us-east1`
  * `us-east4`

**Note:** For `asia-southeast1`, only 1 vCPU is supported.

### Considerations when using the 1 vCPU machine type

AlloyDB offers a 1 vCPU shape with C4A and is intended for development and testing purposes only. For production workloads, choose two or more vCPUs.

When you choose 1 vCPU, keep the following limitations in mind:

  * 1 vCPU is offered with 8 GB of memory without ultra-fast cache support.
  * 1 vCPU configuration is recommended for development and sandbox environments with smaller database sizes in the tens of gigabytes. For larger databases and for production workloads, consider using 2 vCPU or higher.
  * You can configure with high availability (HA), but no uptime SLAs are offered.
  * To learn where you can deploy 1 vCPUs, see C4A supported regions.



## What's next

  * [Create a read pool instance.](https://docs.cloud.google.com/alloydb/docs/instance-read-pool-create)

  * [Connect a psql client to an instance.](https://docs.cloud.google.com/alloydb/docs/connect-psql)

  * [Create a database.](https://docs.cloud.google.com/alloydb/docs/database-create)

  * [Upgrade a cluster's major server version.](https://docs.cloud.google.com/alloydb/docs/cluster-upgrade)

  * [Connect using Private Service Connect.](https://docs.cloud.google.com/alloydb/docs/configure-private-service-connect)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
