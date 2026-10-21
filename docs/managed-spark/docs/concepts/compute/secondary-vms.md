---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/compute/secondary-vms/
title: Managed Service for Apache Spark secondary workers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:32.380521+00:00
---

# Managed Service for Apache Spark secondary workers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/compute/secondary-vms/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Managed Service for Apache Spark secondary workers Stay organized with collections  Save and categorize content based on your preferences. 

In addition to using standard Compute Engine VMs as Managed Service for Apache Spark workers (called "primary" workers), Managed Service for Apache Spark clusters can use `secondary` workers.

The following characteristics apply to all secondary workers in a Managed Service for Apache Spark cluster:

  * **Processing only** —Secondary workers do not store data. They only function as processing nodes. Therefore, you can use secondary workers to scale compute without scaling storage.

  * **Secondary workers only** —You can create a [zero-scale cluster](https://docs.cloud.google.com/dataproc/docs/guides/create-zero-scale-cluster) with secondary workers only. However, if you create a standard cluster and only specify secondary workers (you don't specify the number of primary workers), Managed Service for Apache Spark adds two primary workers to the cluster.

  * **Machine type** —By default, secondary workers use the [machine type](https://docs.cloud.google.com/compute/docs/machine-types "machine type") of the cluster's primary workers. For example, if you create a cluster with primary workers that use `n1-standard-4` machine types, by default, all secondary workers added to the cluster will also use `n1-standard-4` machines.

Instead of using the default primary worker machine type for secondary workers, you can specify one or more ranked lists of machine types for secondary workers. See [Managed Service for Apache Spark Flexible VMs](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/flexible-vms) for more information.

  * **Persistent disk size** —As a default, secondary workers are created with the smaller of 1000GB or the primary worker boot disk size. This disk space is used for local caching of data and is not available through HDFS. You can override the default disk size with the [`gcloud dataproc clusters create --secondary-worker-boot-disk-size`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) command at cluster creation. You can specify this flag even if the cluster won't have secondary workers when it is created.

  * **Asynchronous Creation** —When you add secondary workers by creating or scaling up a cluster, the secondary workers may not be provisioned by the time the create or update operation finishes. This is because Managed Service for Apache Spark manages secondary workers using Managed Instance Groups (MIGs), which create VMs asynchronously as soon as they can be provisioned (see [Checking the status of managed instances](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#verify_instances)).




## Preemptible and non-preemptible secondary workers

There are three types of secondary workers: [spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot), standard [preemptible VMs](https://docs.cloud.google.com/compute/docs/instances/preemptible), and [non-preemptible VMs](https://docs.cloud.google.com/compute/docs/instances). The default Managed Service for Apache Spark secondary worker type is the standard preemptible VM. You can specify a mix of Spot and non-preemptible secondary workers.

**Key Term:** A **spot VM** is the latest type of Compute Engine preemptible VM. It shares the lower-cost pricing model of preemptible VMs, but unlike the preemptible VM with a 24-hour maximum lifetime, the spot VM has no maximum lifetime. Both spot and standard preemptible VM workers are reclaimed and removed from a Managed Service for Apache Spark cluster if they are required by Google Cloud for other tasks.

Example: If you select three secondary workers when you create a cluster, you can specify three spot VMs, three preemptible VMS, three non-preemptible VMs, or a mix of spot and non-preemptible workers.

### Preemptible workers

**Note:** When the term "preemptible" is used in the following sections to refer to a VM, worker, or node, it refers to both the standard preemptible and spot preemptible VM types unless it is used to expressly refer to the "standard preemptible" VM type only.

  * Although the potential removal of preemptible workers can affect job stability, you may decide to use preemptible instances to lower per-hour compute costs for non-critical data processing or to create very large clusters at a lower total cost (you can use the [Google Cloud pricing calculator](https://cloud.google.com/products/calculator/) to estimate costs).

  * For best results, the number of preemptible workers in your cluster should be less than 50% of the total number of all workers (primary plus all secondary workers) in your cluster.

  * When using preemptible workers, your jobs will most likely experience a greater number of transient single-worker task failures compared to jobs run on non-preemptible workers. To increase job tolerance to low-level task failures, you can set cluster property values similar to the [default property values used with autoscaling clusters](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/autoscaling#autoscaling_default_sparkhadoop_property_settings) to increase the maximum number of task retries and help avoid job failures.

**Tip:** Consider using [Enhanced Flexibility Mode](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/flex) if you are using preemptible VMs with Spark.
  * **A cost-savings consideration:** Using preemptible VMs does not always save costs since preemptions can cause longer job execution with resulting higher job costs. Although using [Enhanced Flexibility Mode (EFM)](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/flex) with preemptible VMs can help mitigate this result, the overall cost savings of preemptible VMs will vary with each use case. Generally, short-lived jobs are more suitable for preemptible VM use, since the probability of preemptions during job execution will be lower. Try different job options, such as no preemptible VMs and preemptible VMs with EFM, to estimate costs and arrive at the best solution.




### Non-preemptible workers

  * You can create a cluster with non-preemptible secondary workers to scale compute without sacrificing job stability. To do this, specify `non-preemptible` as the secondary worker type. You can mix non-preemptible with spot secondary workers.



## Select secondary workers

You can specify the number and type of secondary workers when you create a cluster using the [Google Cloud console](https://console.cloud.google.com/dataproc/clusters), [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/update) or the [Dataproc API](https://docs.cloud.google.com/managed-spark/docs/reference).

  * You can mix spot with non-preemptible secondary workers.
  * You can [update your cluster](https://docs.cloud.google.com/managed-spark/docs/guides/manage-cluster#updating_a_cluster) after it is created to change the number, but not the type, of secondary workers in your cluster.
  * [Label updates](https://docs.cloud.google.com/managed-spark/docs/guides/creating-managing-labels) propagate to all preemptible secondary workers within 24 hours. Label updates don't propagate to existing non-preemptible secondary workers. Label updates propagate to all workers added to a cluster **after** a label update. For example, if you scale up the cluster, all new primary and secondary workers will have the new labels.

**Tip:** If you plan to add secondary workers to a cluster later, you can specify `0` secondary workers when you create your cluster, then update the cluster later to specify a positive number. You must specify the `secondary-worker-type` when you create the cluster.

### Console

You can specify the number of secondary workers when creating a Managed Service for Apache Spark cluster from the Google Cloud console. After a cluster has been created, you can add and remove secondary workers by editing the cluster configuration from the Google Cloud console.

#### Create a cluster with secondary workers

  1. Open the [Create cluster](https://console.cloud.google.com/dataproc/clusters/create) page. 
  2. Click **Additional configuration** to expand that section.
  3. Edit **Secondary workers**.
  4. In the panel that opens, specify the number, type, and other secondary worker settings.



#### Update a cluster with secondary instances

To update the number of secondary workers in a cluster, click the name of the cluster on the [**Clusters**](https://console.cloud.google.com/dataproc/clusters) page of the Google Cloud console. On the **Cluster details** page. Click the **Configuration** tab, then click **Edit** and update the number in the Secondary worker nodes field.

#### Remove all secondary instances from a cluster

To remove all secondary workers from a cluster, update the cluster configuration as explained earlier, specifying `0` in the Secondary worker nodes field.

### gcloud CLI command

Use the [`gcloud dataproc clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) command to add secondary workers to a cluster when the cluster is created. After a cluster is created, you can add or remove secondary workers to or from the cluster with the [`gcloud dataproc clusters update`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/update) command (the number but not type of secondary workers can be updated).

#### Create a cluster with secondary workers

To create a cluster with secondary workers, use the [`gcloud dataproc clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) command with the `--num-secondary-workers` argument. Secondary workers are standard preemptible VMs by default. You can specify non-preemptible or spot secondary workers when you create a cluster by setting `--secondary-worker-type` flag to `non-preemptible` or `spot`. The following examples show how to create a cluster with each secondary worker type: the `preemptible` (default), spot (preemptible), and non-preemptible. You can use additional flags to mix spot with non-preemptible secondary workers. 

**Example 1**  


The following command creates "cluster1" with two standard preemptible (default type) secondary workers.
    
    
    gcloud dataproc clusters create cluster1 \
        --num-secondary-workers=2 \
        --region=us-central1
    

**Example 2**  


The following command uses the `secondary-worker-type` flag to create "cluster2" with two spot (preemptible) secondary workers.
    
    
    gcloud dataproc clusters create cluster2 \
        --num-secondary-workers=2 \
        --secondary-worker-type=spot \
        --region=us-central1
    

**Example 3**

The following command uses the `secondary-worker-type` flag to create "cluster3" with two **non-preemptible** secondary workers.
    
    
    gcloud dataproc clusters create cluster3 \
        --num-secondary-workers=2 \
        --secondary-worker-type=non-preemptible \
        --region=us-central1
    

**Change the secondary worker boot disk size**. As a default, all secondary workers are created with the smaller of 1000GB or the primary worker boot disk size. This disk space is used for local caching of data and is not available through HDFS. You can override the default disk size with the [`gcloud dataproc clusters create --secondary-worker-boot-disk-size`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) command at cluster creation. This flag can be specified even if the cluster does not have any secondary workers at creation time.

**Let the Google Cloud console construct your cluster create request.** At the bottom of the [Create cluster](https://console.cloud.google.com/dataproc/clusters/create) page, click **Equivalent command line** or **Equivalent REST** to have the Google Cloud console construct an equivalent gcloud CLI command or API REST request.

#### Update a cluster with secondary workers

To update a cluster to add or remove secondary workers, use the [`gcloud dataproc clusters update`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/update) command with the `--num-secondary-workers` flag.

**Example**  


The following command updates **example-cluster** to use four secondary workers (of the default type or type specified when you created the cluster).
    
    
    gcloud dataproc clusters update example-cluster \
        --num-secondary-workers=4 \
        --region=us-central1
    

#### Remove all secondary workers from a cluster

To remove all secondary workers from a cluster, use the [`gcloud dataproc clusters update`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/update) command with `--num-secondary-workers` set to `0`.

**Example**  


The following command removes all secondary workers from "example-cluster".
    
    
    gcloud dataproc clusters update example-cluster \
        --num-secondary-workers=0 \
        --region=us-central1
    

### REST API

#### Create a cluster with secondary workers

Use the Managed Service for Apache Spark [clusters.create](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create) API add secondary workers to a cluster when the cluster is created. The following examples show how to create a cluster with each [secondary worker type](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/InstanceGroupConfig#Preemptibility): `preemptible` (default), `spot` (preemptible), and `non-preemptible`. You can use additional fields to mix spot with non-preemptible secondary workers.

**Example 1**  


The following POST request creates a "cluster1" with two standard preemptible (default type) VM workers.
    
    
    
    POST https://dataproc.googleapis.com/v1/projects/project-id/regions/region/clusters
    
    {
      "clusterName": "cluster1",
      "config": {
        "secondaryWorkerConfig": {
          "numInstances": 2
        }
      }
    }
    

**Example 2**  


The following POST request creates a "cluster2" with two spot (preemptible) VM workers.
    
    
    
    POST https://dataproc.googleapis.com/v1/projects/project-id/regions/region/clusters
    
    {
      "clusterName": "cluster2",
      "config": {
        "secondaryWorkerConfig": {
          "numInstances": 2,
          "preemptibility": "SPOT"
        }
      }
    }
    

**Example 3**

The following POST request creates "cluster3" with two **non-preemptible** secondary workers.
    
    
    
    POST https://dataproc.googleapis.com/v1/projects/project-id/regions/region/clusters
    
    {
      "clusterName": "cluster3",
      "config": {
        "secondaryWorkerConfig": {
          "numInstances": 2,
          "preemptibility": "NON_PREEMPTIBLE"
        }
      }
    }
    

#### Update a cluster with secondary workers

Use the Managed Service for Apache Spark [clusters.patch](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/patch) API to add and remove secondary workers.

**Example**  


The following PATCH request updates a cluster to have four secondary workers (of the default type or type specified when you created the cluster).
    
    
    
    PATCH /v1/projects/project-id/regions/region/clusters/cluster-name?updateMask=config.secondary_worker_config.num_instances
    {
      "config": {
        "secondaryWorkerConfig": {
          "numInstances": 4
        }
      }
    }
    

**Let the Google Cloud console construct your cluster create request.** At the bottom of the [Create cluster](https://console.cloud.google.com/dataproc/clusters/create) page, click **Equivalent command line** or **Equivalent REST** to have the Google Cloud console construct an equivalent gcloud CLI command or API REST request.

## Troubleshoot secondary workers

  * **Service account permission issues:** Secondary workers are created through a [managed instance group](https://docs.cloud.google.com/compute/docs/access/iam#managed-instance-groups-and-iam). If there is a permission issue, Managed Service for Apache Spark logs won't report the failure to create secondary workers, but failed workers are listed under the **VM Instances** tab of the **Cluster details** page in the Google Cloud console without a green checkmark. To view the listing, open the Managed Service for Apache Spark [**Clusters**](https://console.cloud.google.com/dataproc/clusters) page, then click the cluster name to open the **Cluster details** page for the cluster.

  * **Managed instance group permissions issues:** To check if there is an issue with managed instance group permissions: 

    1. Find the name of the managed instance group (`instanceGroupManagerName`). 

### Google Cloud console

       1. Open the [**Clusters**](https://console.cloud.google.com/dataproc/clusters) page, then click the cluster name to open the **Cluster details** page for the cluster.
       2. Click **Equivalent REST** at the bottom of the page, then view the `config.secondaryWorkerConfig.managedGroupConfig.instanceGroupManagerName` value. 

### gcloud CLI

Run the [`gcloud dataproc clusters describe`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/describe) command with the `--format` flag to display the `instanceGroupManagerName`.
    
    gcloud dataproc clusters describe CLUSTER_NAME \
        --region=REGION \
        --format='value(config.secondaryWorkerConfig.managedGroupConfig.instanceGroupManagerName)'
    

### REST API

Submit a [`clusters.get`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/get) [](https://docs.cloud.google.com/managed-spark/docs/concepts/compute/secondary-vms/) request to return the value of `config.secondaryWorkerConfig.managedGroupConfig.instanceGroupManagerName`.

    2. View the logs in [Logs Explorer](https://docs.cloud.google.com/logging/docs/write-query-log-entries-gcloud#explore).
    * Select the `Google Compute Engine Instance Group` resource type, and filter for the managed instance group name.

    * Alternatively, you can apply a logging filter for `resource.type="gce_instance_group" and `resource.labels.instance_group_name=INSTANCE_GROUP_MANAGER_NAME`. 




## Mix spot with non-preemptible secondary workers

You can specify a mix of spot and non-preemptible secondary workers when you create a Managed Service for Apache Spark cluster.

### Secondary worker settings to mix spot with non-preemptible secondary workers

Use the following secondary worker settings when you create a Managed Service for Apache Spark cluster to obtain a minimum level of secondary worker capacity with the ability to increase capacity when spot VMs are available:

  * **secondary worker number:** The total number of secondary workers to provision.

  * **secondary worker type:** `spot` is the secondary worker type when mixing spot with non-preemptible secondary workers.

  * **standardCapacityBase:** The number of non-preemptible (standard) secondary workers to provision. Non-preemptible secondary workers are provisioned before other types of secondary workers.

  * **standardCapacityPercentAboveBase:** After the `standardCapacityBase` number of secondary workers is filled, the remaining number of secondary workers needed to meet the total number of secondary workers requested is filled with a mix of non-preemptible and spot VMS as follows:

    * `standardCapacityPercentAboveBase`: The percent of the remaining secondary workers to fill with non-preemptible VMS.
    * The remaining number needed to meet the total number of requested secondary workers are filled with spot VMs.



**Example:**

  * Number of secondary workers: 15
  * `standardCapacityBase`: 5
  * `standardCapacityPercentAboveBase` 30%



Result:

  * Non-preemptible: **8** = 5 (`standardCapacityBase`) + 3 (30% of remaining 10)
  * Spot: **7** (70% of remaining 10)
  * Total = **15**



### Create a cluster with a mix of spot and non-preemptible secondary workers

You can use the gcloud CLI or the Dataproc API to mix spot with non-preemptible secondary workers when you create a cluster.

### gcloud

Run the following command locally or in [Cloud Shell](https://console.cloud.google.com/?cloudshell=true%22) to create a cluster with a mix of spot and non-preemptible secondary workers.
    
    
    gcloud dataproc clusters create CLUSTER_NAME \
        --project=PROJECT_ID \
        --region=REGION \
        --secondary-worker-type=spot \
        --num-secondary-workers=NUMBER_SECONDARY_WORKERS \
        --secondary-worker-standard-capacity-base=STANDARD_CAPACITY_BASE \
        --secondary-worker-standard-capacity-percent-above-base=STANDARD_CAPACITY_PERCENT_ABOVE_BASE \
        OTHER_FLAGS_AS_NEEDED
    

Notes:

  * CLUSTER_NAME: The name of the new cluster.
  * PROJECT_ID: Your Google Cloud project ID. Project IDs are listed in the **Project info** section on the Google Cloud console [Dashboard](https://console.cloud.google.com/home/dashboard).
  * REGION: An available Compute Engine [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) to run the workload.
  * `--secondary-worker-type`: When mixing spot and non-preemptible secondary workers, specify the secondary worker type as `spot`.
  * STANDARD_CAPACITY_BASE and STANDARD_CAPACITY_PERCENT_ABOVE_BASE: See Secondary worker settings to mix spot with non-preemptible secondary workers.
  * OTHER_FLAGS_AS_NEEDED: See [gcloud dataproc clusters create](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create).



### API

To mix spot with non-preemptible secondary workers, set the Managed Service for Apache Spark `preemptibility`, `standardCapacityBase`, and `standardCapacityPercentAboveBase` API fields as part of a [cluster.create](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create) request, as shown in the following JSON sample:
    
    
    {
      "clusterName": "CLUSTER_NAME",
      "config": {
        "secondaryWorkerConfig": {
          "numInstances": 15,
          **"preemptibility": "spot"**,
          "instanceFlexibilityPolicy": {
            "provisioningModelMix": {
              **"standardCapacityBase": STANDARD_CAPACITY_BASE**
              **"standardCapacityPercentAboveBase": STANDARD_CAPACITY_PERCENT_ABOVE_BASE**
            }
          }
        }
      }
    }
    

Notes:

  * CLUSTER_NAME: The name of the new cluster.
  * `preemptibility`: When mixing spot and non-preemptible secondary workers, specify `spot`.
  * STANDARD_CAPACITY_BASE and STANDARD_CAPACITY_PERCENT_ABOVE_BASE: See Secondary worker settings to mix spot with non-preemptible secondary workers.



### Combine secondary worker mixing with flexible VMs

You can [mix spot and non-preemptible secondary workers](https://docs.cloud.google.com/managed-spark/docs/concepts/compute/secondary-vms#mix_spot_with_non-preemptible_secondary_workers) and specify [flexible VM shapes](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/flexible-vms) for secondary workers when you create a cluster.

gcloud CLI example:
    
    
    gcloud dataproc clusters create cluster-name \
        --project=project-id \
        --region=us-central1 \
        --secondary-worker-type=spot \
        --num-secondary-workers=15 \
        --secondary-worker-standard-capacity-base=5 \
        --secondary-worker-standard-capacity-percent-above-base=30 \
        --secondary-worker-machine-types="type=n2-standard-8,rank=0" \
        --secondary-worker-machine-types="type=e2-standard-8,type=t2d-standard-8,rank=1"
        ...other flags as needed
    

### Secondary worker mixing characteristics

This section describes some of the behavior and characteristics associated with mixing spot and non-preemptible secondary workers.

#### Secondary worker preference

Managed Service for Apache Spark doesn't give preference to either spot or non-preemptible VMs when scheduling applications on secondary workers.

#### Secondary worker scaling

When secondary workers are scaled through [autoscaling](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/autoscaling) or manual scaling, Managed Service for Apache Spark maintains the requested spot-to-non-preemptible ratio when it adds secondary workers.

#### Updating secondary worker mix settings

You specify the mix of spot and non-preemptible secondary workers when you create a Managed Service for Apache Spark cluster. You can't change the secondary worker mix settings after you create the cluster.

#### Spot secondary worker preemption

  * Managed Service for Apache Spark doesn't control the timing of spot VM preemption (see [Preemption of Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot#preemption)).
  * When spot preemption occurs, the secondary worker group can run with reduced capacity temporarily until Compute Engine reprovisions the preempted VMs.
  * Managed Service for Apache Spark won't add capacity to a secondary worker group in excess of the group's initial settings.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
