---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/compute/persistent-disks/
title: Managed Service for Apache Spark boot disks \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:51.452027+00:00
---

# Managed Service for Apache Spark boot disks  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/compute/persistent-disks/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Managed Service for Apache Spark boot disks Stay organized with collections  Save and categorize content based on your preferences. 

You select standard, SSD, balanced [Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/persistent-disks), or [Google Cloud Hyperdisk balanced](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced) as boot disks for Managed Service for Apache Spark cluster nodes.

**Boot disk type options** :

  * You can select a **standard** , **SSD** , or **balanced Persistent Disk** , boot disk for **master** , **primary worker** , and **secondary worker** cluster nodes.

  * You can select [**hyperdisk balanced**](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced) as the boot disk for **master** and **primary worker** nodes. Note that Managed Service for Apache Spark automatically sets the secondary worker boot disk type to hyperdisk balanced when the primary worker boot disk type is set to hyperdisk balanced.




The default persistent boot disk type for Managed Service for Apache Spark cluster master and primary worker nodes is **standard** (`pd-standard`). If the VM [machine type](https://docs.cloud.google.com/managed-spark/docs/concepts/compute/supported-machine-types) supports only [hyperdisk balanced](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced) as the boot disk, the default boot disk is **hyperdisk balanced** (`hyperdisk-balanced`). The default persistent boot disk type for cluster secondary worker nodes is the primary worker node persistent boot disk type.

## Select persistent boot disk types for cluster nodes

You can select the persistent boot disk type when you create a cluster using the Google Cloud console, Google Cloud CLI, or Dataproc API.

### Google Cloud console

To select cluster node boot disk types:

  1. Open the Managed Service for Apache Spark [Create a cluster](https://console.cloud.google.com/dataproc/clusters/create) page. 
  2. Click **Additional configuration** to expand that section.
  3. Click **Primary workers** and **Secondary workers** to confirm or change the default settings.
  4. By default, driver (master) node settings are the same as primary worker settings. Under **Additional configuration** , you can click **Driver node** to clear the **Default driver node to the same as primary worker** checkbox, then specify driver node settings.



### gcloud CLI

You can create a cluster and select cluster node boot disk types using the [gcloud dataproc clusters create](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) command with the `--master-boot-disk-type`, `--worker-boot-disk-type`, and `--secondary-worker-boot-disk-type` flags.

**Example:**
    
    
    gcloud dataproc clusters create CLUSTER_NAME \
        --region=REGION \
        --master-boot-disk-type=pd-ssd \
        --worker-boot-disk-type=hyperdisk-balanced \
        other args ...
    

p You can set the size of persistent boot disks using the [`--master-boot-disk-size`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create#--master-boot-disk-size), [`--worker-boot-disk-size`, and ](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create#--worker-boot-disk-size)[`--secondary-worker-boot-disk-size`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create#--secondary-worker-boot-disk-size) flags. 

### REST API

You can set a value of `pd-standard`, `pd-ssd`, `pd-balanced`, or `hyperdisk-balanced` in the [`InstanceGroupConfig.DiskConfig.bootDiskType`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/InstanceGroupConfig#DiskConfig) field in the `masterConfig`, `workerConfig`, and `secondaryWorkerConfig` as part of a [`cluster.create`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create) API request.

Note: Set the per-node boot disk **size** using the [`InstanceGroupConfig.DiskConfig.bootDiskSizeGb`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/InstanceGroupConfig#DiskConfig) field in the master, worker, or secondary worker config.

### Hyperdisk settings

When you create a cluster with a hyperdisk balanced volume as the boot disk for a Managed Service for Apache Spark cluster node, you can set the [provisioned IOPS and throughput](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced#about-provisioned-performance-for-hyperdisk-balanced).

### Console

To configure provisioned IOPS and throughput:

  1. Open the Managed Service for Apache Spark [Create a cluster](https://console.cloud.google.com/dataproc/clusters/create) page.
  2. Click **Additional configuration** to expand that section.
  3. Click **Driver node** or **Primary workers**.
  4. In the panel that opens, configure the provisioned IOPS and throughput settings, then click **Save**.



### gcloud CLI

You can set provisioned IOPS and provisioned throughput for cluster nodes with the hyperdisk-balanced boot disks using the [gcloud dataproc clusters create](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) command `--master-boot-disk-provisioned-iops`, `--worker-boot-disk-provisioned-iops`, `--master-boot-disk-provisioned-throughput`, and `--worker-boot-disk-provisioned-throughput` flags.

**Example:**
    
    
      gcloud dataproc clusters create CLUSTER_NAME \
          --region=REGION \
          --master-boot-disk-type=hyperdisk-balanced \
          --master-boot-disk-provisioned-iops=MASTER_BOOT_DISK_IOPS  \
          --master-boot-disk-provisioned-throughput=MASTER_BOOT_DISK_THROUGHPUT \
          --worker-boot-disk-type=hyperdisk-balanced \
          --worker-boot-disk-provisioned-iops=WORKER_BOOT_DISK_IOPS \
          --worker-boot-disk-provisioned-throughput=WORKER_BOOT_DISK_THROUGHPUT \
          other args ...
      

### REST API

You can set provisioned IOPS and provisioned throughput for cluster nodes with hyperdisk boot disks using the [`InstanceGroupConfig.DiskConfig.bootDiskProvisionedIops`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/InstanceGroupConfig#DiskConfig.FIELDS.boot_disk_provisioned_iops) and [`InstanceGroupConfig.DiskConfig.bootDiskProvisionedThroughput`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/InstanceGroupConfig#DiskConfig.FIELDS.boot_disk_provisioned_throughput) fields for the master and worker configs. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
