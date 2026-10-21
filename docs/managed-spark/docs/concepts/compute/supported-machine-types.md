---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/compute/supported-machine-types/
title: Supported machine types \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:36:57.627784+00:00
---

# Supported machine types  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/compute/supported-machine-types/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Supported machine types Stay organized with collections  Save and categorize content based on your preferences. 

Managed Service for Apache Spark clusters are built on [Compute Engine](https://docs.cloud.google.com/compute) instances. [Machine types](https://docs.cloud.google.com/compute/docs/machine-types) define the virtualized hardware resources available to an instance. Compute Engine offers both [predefined machine types](https://docs.cloud.google.com/compute/docs/machine-types#predefined_machine_types) and [custom machine types](https://docs.cloud.google.com/compute/docs/machine-types#custom_machine_types). Managed Service for Apache Spark clusters can use both predefined and custom types for both master and worker nodes.

Managed Service for Apache Spark clusters support the following Compute Engine predefined machine types (machine type availability varies by [region](https://docs.cloud.google.com/compute/docs/regions-zones#available)):

  * [General purpose machine types](https://docs.cloud.google.com/compute/docs/machine-types#general_purpose), which include N1, N2, N2D, E2, C3, C4, N4 and N4D machine types (Managed Service for Apache Spark also supports N1, N2, N2D, E2, N4 and N4D custom machine types). 

**Limitations:**

    * The n1-standard-1 machine type is **not supported** for 2.0+ images (the n1-standard-1 machine type is **not recommended** for pre-2.0 images—instead, use a machine type with higher memory).
    * Shared-core machine types are **not supported** , which include the following unsupported machine types: 
      * E2: e2-micro, e2-small, and e2-medium shared-core machine types, and
      * N1: f1-micro and g1-small shared-core machine types.
    * Managed Service for Apache Spark selects [`hyperdisk-balanced`](https://docs.cloud.google.com/compute/docs/disks/hyperdisks) as the boot-disk type if machine type is C4, N4 or N4D.
  * [Compute-optimized machine types](https://docs.cloud.google.com/compute/docs/machine-resource#compute-optimized_machine_family_guide), which include C2 and C2D machine types.
  * [Memory-optimized machine types](https://docs.cloud.google.com/compute/docs/machine-resource#memory-optimized_machine_family_guide), which include M1 and M2 machine types.
  * ARM machine types, which include [C4A](https://docs.cloud.google.com/compute/docs/instances/arm-on-compute#arm-c4-vms) machine types.

For help in choosing a machine type, see [Optimize Managed Service for Apache Spark costs using VM machine type](https://cloud.google.com/blog/products/data-analytics/optimize-dataproc-costs-using-vm-machine-type). 

## Custom machine types

Managed Service for Apache Spark supports N1, N2, N2D, E2, N4 and N4D series [custom machine types](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type).

Custom machine types are ideal for the following workloads:

  * Workloads that are not a good fit for the predefined machine types.
  * Workloads that require more processing power or more memory, but don't need all of the upgrades that are provided by the next machine type level.



For example, if you have a workload that needs more processing power than that provided by an `n1-standard-4` instance, but the next step up, an `n1-standard-8` instance, provides too much capacity. With custom machine types, you can create Managed Service for Apache Spark clusters with master and/or worker nodes in the middle range, with 6 virtual CPUs and 25 GB of memory.

### Specify a custom machine type

Custom machine types use a special `machine type` specification and are subject to [limitations](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type#limitations). For example, the custom machine type specification for a custom VM with 6 virtual CPUs and 22.5 GB of memory is `custom-6-23040`.

The numbers in the machine type specification correspond to the number of virtual CPUs (vCPUs)in the machine (`6`) and the amount of memory (`23040`). The amount of memory is calculated by multiplying the amount of memory in gigabytes by `1024` (see [Expressing memory in GB or MB](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type#memory_units)). In this example, 22.5 (GB) is multiplied by 1024: `22.5 * 1024 = 23040`.

**Note:** Managed Service for Apache Spark requires machine types to have a minimum of 3.5GB (3584) memory.

You specify the custom machine type when you create a cluster. You can set the machine type for either master or worker nodes or both when you create a cluster. If you set both, the master node can use a custom machine type that is different from the custom machine type used by workers. The machine type used by any secondary workers follow the settings for primary workers and cannot be separately set (see [Secondary workers - preemptible and non-preemptible VMs](https://docs.cloud.google.com/managed-spark/docs/concepts/compute/secondary-vms)).

See Create a Managed Service for Apache Spark cluster with custom machine type with extended memory to increase CPU memory above the standard limits.

### Custom machine type pricing

[Custom machine type pricing](https://cloud.google.com/compute/pricing#custommachinetypepricing) is based on the resources used in a custom machine. [Managed Service for Apache Spark pricing](https://cloud.google.com/managed-spark/pricing) is added to the cost of compute resources, and is based on the total number of virtual CPUs (vCPUs) used in a cluster.

### Create a cluster with a specified machine type

### Google Cloud console

* Open the [Create cluster](https://console.cloud.google.com/dataproc/clusters/create) page. 
* In the **Worker configuration** , select machine family, series, and type.
* By default, driver(master) node settings are the same as primary worker settings. Under **Additional configuration** , you can edit **Driver node** to clear the **Default driver node to the same as primary worker** checkbox, then specify driver node settings.

### gcloud CLI command

Run the [`gcloud dataproc clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) command with the following flags to create a Managed Service for Apache Spark cluster with master and/or worker machine types:

  * The `--master-machine-type machine-type` flag lets you set the predefined or custom machine type used by the master VM instance in your cluster (or master instances if you create a [HA cluster](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/high-availability))
  * The `--worker-machine-type custom-machine-type` flag lets you set the predefined or custom machine type used by the worker VM instances in your cluster



**Example** :
    
    
    gcloud dataproc clusters create test-cluster /
        --master-machine-type custom-6-23040 /
        --worker-machine-type custom-6-23040 /
        other args
    

**Let the Google Cloud console construct your cluster create request.** At the bottom of the [Create cluster](https://console.cloud.google.com/dataproc/clusters/create) page, click **Equivalent command line** or **Equivalent REST** to have the Google Cloud console construct an equivalent gcloud CLI command or API REST request.

Once the Managed Service for Apache Spark cluster starts, cluster details are displayed in the terminal window. The following is a partial sample listing of cluster properties displayed in the terminal window: 
    
    
    ...
    properties:
      distcp:mapreduce.map.java.opts: -Xmx1638m
      distcp:mapreduce.map.memory.mb: '2048'
      distcp:mapreduce.reduce.java.opts: -Xmx4915m
      distcp:mapreduce.reduce.memory.mb: '6144'
      mapred:mapreduce.map.cpu.vcores: '1'
      mapred:mapreduce.map.java.opts: -Xmx1638m
    ...
    

### API

To create a cluster with custom machine types, set the `machineTypeUri` in the `masterConfig` and/or `workerConfig` [InstanceGroupConfig](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#InstanceGroupConfig.FIELDS.machine_type_uri) in the [cluster.create](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create) API request.

**Example** :
    
    
    POST /v1/projects/my-project-id/regions/is-central1/clusters/
    {
      "projectId": "my-project-id",
      "clusterName": "test-cluster",
      "config": {
        "configBucket": "",
        "gceClusterConfig": {
          "subnetworkUri": "default",
          "zoneUri": "us-central1-a"
        },
        "masterConfig": {
          "numInstances": 1,
          **"machineTypeUri": "n1-highmem-4"** ,
          "diskConfig": {
            "bootDiskSizeGb": 500,
            "numLocalSsds": 0
          }
        },
        "workerConfig": {
          "numInstances": 2,
          **"machineTypeUri": "n1-highmem-4"** ,
          "diskConfig": {
            "bootDiskSizeGb": 500,
            "numLocalSsds": 0
          }
        }
      }
    }
    

**Let the Google Cloud console construct your cluster create request.** At the bottom of the [Create cluster](https://console.cloud.google.com/dataproc/clusters/create) page, click **Equivalent command line** or **Equivalent REST** to have the Google Cloud console construct an equivalent gcloud CLI command or API REST request.

### Create a cluster with custom machine type with extended memory

Managed Service for Apache Spark supports custom machine types with [extended memory](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type#extendedmemory) beyond the [6.5GB per vCPU limit](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type#create) (see [Extended Memory Pricing](https://cloud.google.com/compute/pricing#extendedmemory)).

Although there is no limit on the amount of extended memory per CPU, there is a limit on the total [extended memory per VM instance](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type).

### Google Cloud console

* Open the Managed Service for Apache Spark [Create cluster](https://console.cloud.google.com/dataproc/clusters/create) page. 
* In the **Worker configuration** , select machine family, series, and type.
* By default, driver (master) node settings are the same as primary worker settings. Under **Additional configuration** , you can edit **Driver node** to clear the **Default driver node to the same as primary worker** checkbox, then specify driver node settings.

### gcloud CLI

To create a cluster from the gcloud command line with custom CPUs with extended memory, add a `-ext` suffix to the `‑‑master-machine-type` and/or `‑‑worker-machine-type` flags.

**Example**

The following gcloud command-line sample creates a Managed Service for Apache Spark cluster with 1 CPU and 50 GB memory (50 * 1024 = 51200) in each node:
    
    
    gcloud dataproc clusters create test-cluster /
        --master-machine-type custom-1-51200-ext /
        --worker-machine-type custom-1-51200-ext /
        other args
    

### API

The following sample [](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#InstanceGroupConfig) JSON snippet from a Dataproc REST API [clusters.create](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create) request specifies 1 CPU and 50 GB memory (50 * 1024 = 51200) in each node:
    
    
    ...
        "masterConfig": {
          "numInstances": 1,
          "machineTypeUri": "custom-1-51200-ext",
        ...
        },
        "workerConfig": {
          "numInstances": 2,
          "machineTypeUri": "custom-1-51200-ext",
         ...
    ...
    

## ARM machine types

Managed Service for Apache Spark supports creating a cluster with nodes that use ARM machine types, such as the [C4A machine type](https://docs.cloud.google.com/compute/docs/instances/arm-on-compute#arm-c4-vms).

Requirements and limitations:

  * The Managed Service for Apache Spark image must be compatible with ARM chipset. The Managed Service for Apache Spark [`2.1-ubuntu20-arm`](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-release-2.1), [`2.2-ubuntu22-arm`](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-release-2.2), and [`2.3-ubuntu22-arm`](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-release-2.3) (and later `-arm` suffix) images are compatible with the ARM chipset. ARM-compatible images don't support many optional and initialization-action components as noted on the [image release version pages](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-version-clusters#supported-dataproc-image-versions).
  * Since one image must be specified for a cluster, the master, worker, and secondary-worker nodes must use an ARM machine type that is compatible with the selected Managed Service for Apache Spark ARM image.
  * Managed Service for Apache Spark features that are not compatible with ARM machine types aren't available (for example, [local SSDs](https://docs.cloud.google.com/managed-spark/docs/concepts/compute/local-ssds) aren't supported by C4A machine types).
  * ARM images only support pre-installed components and a limited set of optional components. Other optional components and all initialization actions are unsupported.
  * [Lightning Engine with Native Query Execution (NQE)](https://docs.cloud.google.com/managed-spark/docs/guides/lightning-engine) is supported on ARM machine types when using [`2.3-ubuntu22-arm`](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/image-release-2.3) images.



## Create a cluster with an ARM machine type

### Console

To create a Managed Service for Apache Spark cluster that uses an ARM machine type, do the following:

  1. Open the Managed Service for Apache Spark [Create cluster](https://console.cloud.google.com/dataproc/clusters/create) page. 
  2. In the **Worker configuration** , select machine family, series, and type.
  3. By default, driver (master) node settings are the same as primary worker settings. Under **Additional configuration** , you can edit **Driver node** to clear the **Default driver node to the same as primary worker** checkbox, then specify driver node settings.



### gcloud

To create a Managed Service for Apache Spark cluster that uses an ARM machine type, run the following `gcloud` command locally in a terminal window or in [Cloud Shell](https://console.cloud.google.com/?cloudshell=true). This example specifies the `2.1-ubuntu20-arm` image and the `c4a-standard-4` ARM machine type.
    
    
    gcloud dataproc clusters create cluster-name \
        --region=REGION \
        --image-version=2.1-ubuntu20-arm \
        --master-machine-type=c4a-standard-4 \
        --worker-machine-type=c4a-standard-4
    

Notes:

  * REGION: The [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) where the cluster will be located.

  * See the [gcloud dataproc clusters create](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) reference documentation for information on additional command-line flags you can use to customize your cluster.




### API

The following sample Dataproc REST API [clusters.create](/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create) request creates cluster that uses the `c4a-standard-4` ARM machine type.
    
    
    POST /v1/projects/my-project-id/regions/is-central1/clusters/
    {
      "projectId": "my-project-id",
      "clusterName": "sample-cluster",
      "config": {
        "configBucket": "",
        "gceClusterConfig": {
          "subnetworkUri": "default",
          "zoneUri": "us-central1-a"
        },
        "masterConfig": {
          "numInstances": 1,
          **"machineTypeUri": "c4a-standard-4"**,
          "diskConfig": {
            "bootDiskSizeGb": 500,
          }
        },
        "workerConfig": {
          "numInstances": 2,
          **"machineTypeUri": "c4a-standard-4"**,
          "diskConfig": {
            "bootDiskSizeGb": 500,
            "numLocalSsds": 0
          }
        },
        "softwareConfig": {
          **"imageVersion": "2.1-ubuntu20-arm"**
        }
      }
    }
    

## What's next

  * Learn more about [ARM VMs on Compute](https://docs.cloud.google.com/compute/docs/instances/arm-on-compute).
  * Learn how to [create a VM with a custom machine type](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type).
  * Learn how to [create and start a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
