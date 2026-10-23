---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/compute/gpus/
title: Attach GPUs to clusters \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:12.392949+00:00
---

# Attach GPUs to clusters  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/compute/gpus/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Attach GPUs to clusters Stay organized with collections  Save and categorize content based on your preferences. 

Managed Service for Apache Spark provides the ability for graphics processing units (GPUs) to be attached to the master and worker Compute Engine nodes in a Managed Service for Apache Spark cluster. You can use these GPUs to accelerate specific workloads on your instances, such as machine learning and data processing.

For more information about what you can do with GPUs and what types of GPU hardware are available, read [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus).

There are no additional [Managed Service for Apache Spark pricing](https://docs.cloud.google.com/managed-spark/pricing) charges added to Compute Engine charges for GPUs used in Managed Service for Apache Spark clusters.

## Before you begin

  * GPUs require special drivers and software. These items are pre-installed in Managed Service for Apache Spark `-ml` images (using the `-ml` images is recommended), and can be manually installed when and if needed.
  * Read about [GPU pricing on Compute Engine](https://cloud.google.com/compute/pricing#gpus) to understand the cost to use GPUs in your instances.
  * Read about [restrictions for instances with GPUs](https://docs.cloud.google.com/compute/docs/gpus#restrictions) to learn how these instances function differently from non-GPU instances.
  * Check the [quotas page](https://console.cloud.google.com/iam-admin/quotas) for your project to ensure that you have sufficient GPU quota (`NVIDIA_T4_GPUS`, `NVIDIA_P100_GPUS`, or `NVIDIA_V100_GPUS`) available in your project. If GPUs are not listed on the quotas page or you require additional GPU quota, [request a quota increase](https://docs.cloud.google.com/compute/quotas#requesting_additional_quota).



## Types of GPUs

Managed Service for Apache Spark nodes support the following GPU types. You must specify GPU type when attaching GPUs to your Managed Service for Apache Spark cluster.

**Caution:** NVIDIA P100 GPUs reach end of support on September 15, 2026. For more information, see [NVIDIA P100 end of support](https://docs.cloud.google.com/compute/docs/eol/p100-eos). 

  * `nvidia-tesla-l4` \- NVIDIA® Tesla® L4
  * `nvidia-tesla-a100` \- NVIDIA® Tesla® A100
  * `nvidia-tesla-p100` \- NVIDIA® Tesla® P100
  * `nvidia-tesla-v100` \- NVIDIA® Tesla® V100
  * `nvidia-tesla-p4` \- NVIDIA® Tesla® P4
  * `nvidia-tesla-t4` \- NVIDIA® Tesla® T4
  * `nvidia-rtx-pro-6000` \- NVIDIA® RTX® PRO 6000
  * `nvidia-tesla-p100-vws` \- NVIDIA® Tesla® P100 Virtual Workstations
  * `nvidia-tesla-p4-vws` \- NVIDIA® Tesla® P4 Virtual Workstations
  * `nvidia-tesla-t4-vws` \- NVIDIA® Tesla® T4 Virtual Workstations



## Attach GPUs to a cluster

To attach GPUs to a Managed Service for Apache Spark cluster, when you create the cluster you must either specify a `-ml` image (**recommended**) or use an initialization action to install GPU drivers.

**Note:** All Managed Service for Apache Spark `3.0` image versions except `3.0-ml-ubuntu` enable [`cgroups V2`](https://kubernetes.io/docs/concepts/architecture/cgroups/). Since YARN doesn't support GPU discovery when `cgroups V2` is enabled, use GPUs in Managed Service for Apache Spark `3.0` clusters with the `3.0-ml-ubuntu` image version.

The following examples specify or assume the use of the [`2.3-ml-ubuntu`](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-release-2.3#image_version_23_machine_learning_ml_components) image when creating a cluster.

### Google Cloud console

To attach GPUs to a Managed Service for Apache Spark cluster, perform the following steps:

  1. Open the [**Create cluster**](https://console.cloud.google.com/dataproc/clusters/create) page. 
  2. In the **Worker configuration** section, click the **GPUs** tab, and then specify the type and number of GPUs.
  3. By default, driver (master) node settings are the same as primary worker settings. Under **Additional configuration** , you can click **Driver node** to clear the **Default driver node to the same as primary worker** checkbox and specify the machine type for the driver node.



### gcloud CLI

To attach GPUs to the master and primary and secondary worker nodes in a Managed Service for Apache Spark cluster, create the cluster using the `gcloud dataproc clusters create` [`‑‑master-accelerator`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create#--master-accelerator), [`‑‑worker-accelerator`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create#--worker-accelerator), and [`‑‑secondary-worker-accelerator`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create#--secondary-worker-accelerator) flags. These flags take the following values:

  * The type of GPU to attach to a node
  * The number of GPUs to attach to the node



The type of GPU is required and the number of GPUs is optional (the default is 1 GPU).

**Example:**
    
    
    gcloud dataproc clusters create cluster-name \
        --image-version=2.3-ml-ubuntu \
        --region=region \
        --master-accelerator type=nvidia-tesla-t4 \
        --worker-accelerator type=nvidia-tesla-t4,count=4 \
        --secondary-worker-accelerator type=nvidia-tesla-t4,count=4 \
        ... other flags
    

### REST API

To attach GPUs to the master and primary and secondary worker nodes in a Managed Service for Apache Spark cluster, fill in the [InstanceGroupConfig.AcceleratorConfig](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#AcceleratorConfig) `acceleratorTypeUri` and `acceleratorCount` fields as part of the [cluster.create](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create) API request. These fields take the following values:

  * The type of GPU to attach to a node
  * The number of GPUs to attach to the node



## Install GPU drivers

GPU drivers are required to utilize GPUs attached to Managed Service for Apache Spark nodes. As an alternative to using the GPU drivers installed in the Managed Service for Apache Spark `-ml` images, you can use the following initialization actions to install GPU drivers when you create a cluster:

  * [NVIDIA cuDF for Apache Sparkx](https://github.com/GoogleCloudDataproc/initialization-actions/tree/master/spark-rapids)
  * [GPU ML Libraries](https://github.com/GoogleCloudDataproc/initialization-actions/tree/master/gpu)



## Verify GPU driver installation

You can verify GPU driver installation on a cluster by [connecting using SSH](https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/ssh) to the cluster master node, and then running the following command:
    
    
    nvidia-smi
    

If the driver is functioning properly, the output will display the driver version and GPU statistics (see [Verifying the GPU driver install](https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu#verify-driver-install)).

**Note:** The driver may not work correctly after a restart of the VM following a Linux [Unattended Upgrade](https://wiki.debian.org/UnattendedUpgrades). Possible solutions: You can disable unattended upgrades or exclude kernel updates by editing the unattended upgrades service config.

## Spark configuration

When you [submit a job](https://docs.cloud.google.com/managed-spark/docs/guides/submit-job) to Spark, you can use the `spark.executorEnv` Spark configuration [runtime environment property](https://spark.apache.org/docs/latest/configuration.html#runtime-environment) property with the `LD_PRELOAD` environment variable to preload needed libraries.

Example:
    
    
    gcloud dataproc jobs submit spark --cluster=CLUSTER_NAME \
      --region=REGION \
      --class=org.apache.spark.examples.SparkPi \
      --jars=file:///usr/lib/spark/examples/jars/spark-examples.jar \
      --properties=spark.executorEnv.LD_PRELOAD=libnvblas.so,spark.task.resource.gpu.amount=1,spark.executor.resource.gpu.amount=1,spark.executor.resource.gpu.discoveryScript=/usr/lib/spark/scripts/gpu/getGpusResources.sh
    

## Example GPU job

You can test GPUs on Managed Service for Apache Spark by running any of the following jobs, which benefit when run with GPUs:

  1. Run one of the [Spark ML examples](https://github.com/apache/spark/blob/master/mllib/src/main/scala/org/apache/spark/ml/classification/MultilayerPerceptronClassifier.scala).
  2. Run the following example with `spark-shell` to run a matrix computation:


    
    
    import org.apache.spark.mllib.linalg._
    import org.apache.spark.mllib.linalg.distributed._
    import java.util.Random
    
    def makeRandomSquareBlockMatrix(rowsPerBlock: Int, nBlocks: Int): BlockMatrix = {
      val range = sc.parallelize(1 to nBlocks)
      val indices = range.cartesian(range)
      return new BlockMatrix(
          indices.map(
              ij => (ij, Matrices.rand(rowsPerBlock, rowsPerBlock, new Random()))),
          rowsPerBlock, rowsPerBlock, 0, 0)
    }
    
    val N = 1024 * 4
    val n = 2
    val mat1 = makeRandomSquareBlockMatrix(N, n)
    val mat2 = makeRandomSquareBlockMatrix(N, n)
    val mat3 = mat1.multiply(mat2)
    mat3.blocks.persist.count
    println("Processing complete!")
    

## What's Next

  * Learn how to [create a Compute Engine instance with attached GPUs](https://docs.cloud.google.com/compute/docs/gpus/add-gpus).
  * Learn more about [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
