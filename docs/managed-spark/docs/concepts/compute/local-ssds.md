---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/compute/local-ssds/
title: Managed Service for Apache Spark local SSDs \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:37.260440+00:00
---

# Managed Service for Apache Spark local SSDs  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/compute/local-ssds/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Managed Service for Apache Spark local SSDs Stay organized with collections  Save and categorize content based on your preferences. 

To supplement the boot disk, you can attach [local Solid State Drives (local SSDs)](https://docs.cloud.google.com/compute/docs/disks/local-ssd) to master, primary worker, and secondary worker nodes in your cluster. When local SSDs are provided to the cluster, both HDFS and scratch data, such as shuffle outputs, use the local SSDs instead of the boot persistent disk.

  * Local SSDs can provide faster read and write times than persistent disk (see [Local SSD Performance](https://docs.cloud.google.com/compute/docs/disks/local-ssd#performance)).
  * The 375GB size of each local SSD is fixed, but you can attach multiple local SSDs to increase SSD storage (see [About Local SSDs](https://docs.cloud.google.com/compute/docs/disks/local-ssd)).
  * Each local SSD is mounted to `/mnt/<id>` in Managed Service for Apache Spark cluster nodes.
  * Local SSDs use [`ext4`](https://en.wikipedia.org/wiki/Ext4) as the default filesystem.



## Use local SSDs

### Google Cloud console

Create a cluster and attach local SSDs to the nodes:

  1. Open the Managed Service for Apache Spark [Create cluster](https://console.cloud.google.com/dataproc/clusters/create) page. 
  2. Click **Additional configuration** to expand that section.
  3. Edit **Primary workers** and **Secondary workers** to configure local SSD settings.
  4. By default, driver (master) node settings are the same as primary worker settings. Under **Additional configuration** , you can click **Driver node** to clear the **Default driver node to the same as primary worker** checkbox, then specify driver node settings.



### gcloud CLI command

Use the [`gcloud dataproc clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) command with the `--num-master-local-ssds`, `--num-workers-local-ssds`, and `--num-secondary-worker-local-ssds` flags to attach local SSDs to the cluster's master, primary, and secondary worker nodes.

Local SSDs can be attached to Managed Service for Apache Spark VMs using a SCSI (Small Computer System Interface) or NVME (Non-Volatile Memory Express) interface (see [local SSD performance](https://docs.cloud.google.com/compute/docs/disks/local-ssd#performance)). The default Managed Service for Apache Spark cluster VM local SSD interface is the SCSI interface. Use the [gcloud dataproc clusters create](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) command with the `--master-local-ssd-interface`, `--worker-local-ssd-interface`, and `--secondary-worker-local-ssd-interface` flags to specify the local SSD interface for master, primary, and secondary worker nodes.

**Example:**
    
    
    gcloud dataproc clusters create cluster-name \
        --region=region \
        --num-master-local-ssds=1 \
        --num-worker-local-ssds=1 \
        --num-secondary-worker-local-ssds=1 \
        --master-local-ssd-interface=NVME \
        --worker-local-ssd-interface=NVME \
        --secondary-worker-local-ssd-interface=NVME \
        ... other args ...
    

### REST API

Set the [numLocalSsds](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#diskconfig) field in the `masterConfig`, `workerConfig`, and `secondaryWorkerConfig` [InstanceGroupConfig](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#InstanceGroupConfig) in a [cluster.create](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create) API request to attach local SSDs to the cluster's master, primary worker, and secondary worker nodes.

Local SSDs can be attached to Managed Service for Apache Spark VMs using a SCSI (Small Computer System Interface) or NVME (Non-Volatile Memory Express) interface (see [local SSD performance](https://docs.cloud.google.com/compute/docs/disks/local-ssd#performance)). The default Managed Service for Apache Spark cluster VM local SSD interface is the SCSI interface. Set the [localSsdInterface](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#diskconfig) field in the `masterConfig`, `workerConfig`, and `secondaryWorkerConfig` [InstanceGroupConfig](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#InstanceGroupConfig) in a [cluster.create](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create) API request to specify the "SCSI" or "NVME" interface to attach local SSDs to the cluster's master, primary worker, and secondary worker nodes.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
