---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/compute/min-cpu/
title: Minimum CPU platform \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-18T05:42:47.507834+00:00
---

# Minimum CPU platform  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/compute/min-cpu/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Minimum CPU platform Stay organized with collections  Save and categorize content based on your preferences. 

This feature lets you select a [minimum CPU platform](https://docs.cloud.google.com/compute/docs/instances/specify-min-cpu-platform) for your Managed Service for Apache Spark clusters. For example, when you create a cluster, you can select Intel Skylake CPUs for the cluster nodes to improve job performance.

Before using this feature, see [Available regions & zones](https://docs.cloud.google.com/compute/docs/regions-zones#available), which lists the platforms available in each zone. You can also run the `gcloud compute zones describe zone` command to list the `availableCpuPlatforms` in the cluster zone. For more information, see [Specifying a minimum CPU platform for VM instances](https://docs.cloud.google.com/compute/docs/instances/specify-min-cpu-platform).

## Use minimum CPU platform

### Console

To specify a minimum CPU platform for cluster nodes:

  1. Open the [Create cluster](https://console.cloud.google.com/dataproc/clusters/create) page. 
  2. In the **Worker configuration** section, under **CPU platform and GPU** , confirm or select a CPU platform.
  3. By default, driver (master) node settings are the same as primary worker settings. Under **Additional configuration** , you can edit **Driver node** to clear the **Default driver node to the same as primary worker** checkbox, then specify driver node settings.



### gcloud CLI command

To specify a minimum CPU platform for your cluster's master and/or worker (including preemptible) nodes, pass one or both of the following flags to the [`gcloud dataproc clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) command:
    
    
    gcloud dataproc clusters create \
        --region=region \
        --master-min-cpu-platform=cpu-platform-name \
        --worker-min-cpu-platform=cpu-platform-name \
        other args ...
    

### REST API

To specify a minimum CPU platform for your cluster's master, primary worker, and/or secondary (preemptible) worker nodes, set the `minCpuPlatform` field in [InstanceGroupConfig](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#InstanceGroupConfig) for your master, primary worker, and/or secondary (preemptible) instances in your [cluster.create](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create) request.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
