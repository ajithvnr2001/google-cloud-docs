---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/confidential-compute/
title: Encrypt memory with Confidential VM clusters \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:04:38.556136+00:00
---

# Encrypt memory with Confidential VM clusters  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/confidential-compute/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Encrypt memory with Confidential VM clusters Stay organized with collections  Save and categorize content based on your preferences. 

You can use the Confidential Computing feature to create a Managed Service for Apache Spark cluster with [Confidential VMs](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/about-cvm) to provide inline memory encryption.

## Requirements

A cluster with Confidential VMs must meet following requirements:

  * Master and worker instances must use a machine type supported by the selected [Confidential Computing technology](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#machine-type-cpu-zone). Supported machines associated with each technology include: 
    * **SEV:** `c4d`, `c3d`, `c2d`, `n2d`, `g4-standard-48`
    * **SEV_SNP:** `n2d`
    * **TDX:** `c3-standard-*`, `a3-highgpu-1g`
    * **NVIDIA** `g4-standard-48`
  * The cluster must use one of the [supported Ubuntu images](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-versions#ubuntu_images).
  * The cluster must be created in a Compute Engine zone that supports the CPU platform required by the selected Confidential Computing technology—see [View supported zones](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#supported-zones). 
    * You can run the following command to list the CPUs supported in a Compute Engine zone: 
          
          gcloud compute zones describe ZONE --format="value(availableCpuPlatforms)"
          




## Create a cluster with Confidential VMs

You can use the Google Cloud console, Google Cloud CLI, or the Managed Service for Apache Spark API to create a cluster that uses Confidential VMs.

### Google Cloud console

To create a cluster that uses Confidential VMs, complete the following steps:

Some machine types required for certain Confidential Compute technologies might not be available in the Google Cloud console. You can specify these configurations using gcloud CLI or the API.

  1. Open the [Create an Apache Spark cluster on Compute Engine](https://console.cloud.google.com/dataproc/clustersAdd) page in the Google Cloud console. 
  2. Under **Define your cluster** , select a [supported zone](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#supported-zones). 
  3. Under **Advanced configurations - Infrastructure** , select a [supported master and worker node machine type](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#machine-type-cpu-zone). 
  4. Under **Advanced configurations - Security** , select "Enable confidential computing".
  5. Confirm or specify other cluster settings, then click **Create**. 



### Google Cloud CLI

To create a cluster that uses Confidential VMs, use the `gcloud dataproc clusters create` command with the [\--confidential-compute-type](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create#--confidential-compute-type) flag.
    
    
    gcloud dataproc clusters create CLUSTER_NAME \
        --confidential-compute-type=CONFIDENTIAL_COMPUTING_TECHNOLOGY (such as SEV, SEV_SNP, or TDX) \
        --image-version=UBUNTU_IMAGE_VERSION \
        --zone=ZONE \
        --master-machine-type=MACHINE_TYPE \
        --worker-machine-type=MACHINE_TYPE \
        other args ...
    

The `--confidential-compute` flag is deprecated. If used, it is replaced with `--confidential-compute-type=SEV`.

### REST API

To create a cluster that uses Confidential VMs, include the [`ConfidentialInstanceConfig`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#confidentialinstanceconfig) as part of a [`clusters.create`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create) request. Set `confidentialInstanceType` to the selected technology, such as `SEV`, `SEV_SNP`, or `TDX`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
