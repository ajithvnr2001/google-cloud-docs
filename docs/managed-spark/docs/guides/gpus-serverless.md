---
url: https://docs.cloud.google.com/managed-spark/docs/guides/gpus-serverless/
title: Use GPUs \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:47.086023+00:00
---

# Use GPUs  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/guides/gpus-serverless/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Use GPUs Stay organized with collections  Save and categorize content based on your preferences. 

You can attach GPU accelerators to your Managed Service for Apache Spark batch workloads to achieve the following results:

  * Speed up the processing of large-scale data analytics workloads.

  * Accelerate model training on large datasets using GPU machine learning libraries.

  * Perform advanced data analytics, such as video or natural language processing.




All [supported Managed Service for Apache Spark runtimes](https://docs.cloud.google.com/managed-spark/docs/concepts/versions/serverless-versions#supported_versions) add the [NVIDIA cuDF for Apache Spark library](https://docs.nvidia.com/cudf-spark/latest/index.html) to each workload node. Managed Service for Apache Spark runtime [version 1.1](https://docs.cloud.google.com/managed-spark/docs/concepts/versions/spark-runtime-versions#spark_runtime_version_11) also adds the [XGBoost library](https://xgboost.ai/) to workload nodes. These libraries provide a powerful data transformation and machine learning tools that you can use in your GPU-accelerated workloads.

## GPU benefits

Here are some of the benefits when you use GPUs with your Managed Service for Apache Spark Spark workloads:

  * **Performance improvement:** GPU acceleration can significantly boost Spark workloads performance, particularly for compute-intensive tasks, such as machine and deep learning, graph processing, and complex analytics.

  * **Faster model training:** For machine learning tasks, attaching GPUs can dramatically reduce the time required to train models, enabling data scientists and engineers to iterate and experiment quickly.

  * **Scalability:** Customers can add more GPUs nodes or more powerful GPUs to nodes for handling increasingly complex processing needs.

  * **Cost efficiency:** Although GPUs require an initial investment, you can achieve cost savings over time due to reduced processing times and more efficient resource utilization.

  * **Enhanced data analytics:** GPU acceleration lets you perform advanced analytics, such as image and video analysis and natural language processing, on large datasets.

  * **Improved products:** Faster processing enables quicker decision-making and more responsive applications.




## Limitations and considerations

  * GPU accelerators are available with the [premium pricing tier](https://docs.cloud.google.com/managed-spark/docs/tiers#premium_tier_benefits).

  * You can attach [NVIDIA A100](https://docs.cloud.google.com/compute/docs/gpus#a100-gpus) or [NVIDIA L4](https://docs.cloud.google.com/compute/docs/gpus#l4-gpus) GPUs to Managed Service for Apache Spark batch workloads. A100 and L4 accelerators are subject to [Compute Engine GPU regional availability](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones).

  * The XGBoost library is only provided to Managed Service for Apache Spark GPU-accelerated workloads when using Managed Service for Apache Spark [Spark runtime version 1.x](https://docs.cloud.google.com/managed-spark/docs/concepts/versions/spark-runtime-versions).

  * Managed Service for Apache Spark GPU-accelerated batches with XGBoost utilize increased [Compute Engine quotas](https://docs.cloud.google.com/managed-spark/quotas). For example, to run a serverless batch workload that uses an NVIDIA L4 GPU, you must allocate the [NVIDIA_L4_GPUS quota](https://docs.cloud.google.com/compute/resource-usage#gpu_quota).

  * Accelerator-enabled jobs are not compatible with the [`constraints/compute.requireShieldedVm`](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#organization-policy-constraint) organization policy. If your organization enforces this policy, its accelerator-enabled jobs won't run successfully.

  * You must set the default character set to UTF-8 when using CUDA-X GPU acceleration with [supported Managed Service for Apache Spark runtimes prior to version `2.2`](https://docs.cloud.google.com/managed-spark/docs/concepts/versions/serverless-versions#supported_versions). See Create a serverless batch workload with GPU accelerators for more information.




## Pricing

GPU accelerators are available with the [premium pricing tier](https://docs.cloud.google.com/managed-spark/docs/tiers#premium_tier_benefits). See [Managed Service for Apache Spark pricing](https://cloud.google.com/managed-spark/pricing#accelerator_pricing) for accelerator pricing information.

## Before you begin

Before creating a serverless batch workload with attached GPU accelerators, do the following:

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Dataproc, Compute Engine, and Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataproc,compute_component,storage_component)

  5. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  6. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  7. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  8. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  10. Enable the Dataproc, Compute Engine, and Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataproc,compute_component,storage_component)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  14. In the Google Cloud console, go to the Cloud Storage **Buckets** page. 

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  15. Click add_box **Create**. 
  16. On the **Create a bucket** page, enter your bucket information. To go to the next step, click **Continue**. 
     1. In the **Get started** section, do the following: 
        * Enter a globally unique name that meets the [bucket naming requirements](https://docs.cloud.google.com/storage/docs/bucket-naming#requirements).
        * To add a [bucket label](https://docs.cloud.google.com/storage/docs/tags-and-labels#bucket-labels), expand the **Labels** section (expand_more), click _add_box_ **Add label** , and specify a `key` and a `value` for your label. 
     2. In the **Choose where to store your data** section, do the following: 
        1. Select a [Location type](https://docs.cloud.google.com/storage/docs/locations).
        2. Choose a location where your bucket's data is permanently stored from the **[Location type](https://docs.cloud.google.com/storage/docs/locations#available-locations)** drop-down menu. 
           * If you select the [dual-region](https://docs.cloud.google.com/storage/docs/locations#location-dr) location type, you can also choose to enable [turbo replication](https://docs.cloud.google.com/storage/docs/availability-durability#turbo-replication) by using the relevant checkbox. 
        3. To set up [cross-bucket replication](https://docs.cloud.google.com/storage/docs/availability-durability#cross-bucket-replication), select **Add cross-bucket replication via Storage Transfer Service** and follow these steps: 

#### Set up cross-bucket replication

           1. In the **Bucket** menu, select a bucket.
           2. In the **Replication settings** section, click **Configure** to configure settings for the replication job.

The **Configure cross-bucket replication** pane appears.

              * To filter objects to replicate by object name prefix, enter a prefix that you want to include or exclude objects from, then click add **Add a prefix**.
              * To set a storage class for the replicated objects, select a storage class from the **Storage class** menu. If you skip this step, the replicated objects will use the destination bucket's storage class by default.
              * Click **Done**.

     3. In the **Choose how to store your data** section, do the following: 
        1. Select a [default storage class](https://docs.cloud.google.com/storage/docs/storage-classes) for the bucket or [Autoclass](https://docs.cloud.google.com/storage/docs/autoclass) for automatic storage class management of your bucket's data.
        2. To enable [hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview), in the **Optimize storage for data-intensive workloads** section, select **Enable hierarchical namespace on this bucket**. **Note:** You cannot enable hierarchical namespace in existing buckets.
     4. In the **Choose how to control access to objects** section, select whether or not your bucket enforces [public access prevention](https://docs.cloud.google.com/storage/docs/public-access-prevention), and select an [access control method](https://docs.cloud.google.com/storage/docs/access-control) for your bucket's objects. **Note:** You cannot change the **Prevent public access** setting if this setting is enforced at an [organization policy](https://docs.cloud.google.com/storage/docs/org-policy-constraints#public-access-prevention).
     5. In the **Choose how to protect object data** section, do the following: 
        * Select any of the options under **Data protection** that you want to set for your bucket. 
          * To enable [soft delete](https://docs.cloud.google.com/storage/docs/soft-delete), click the **Soft delete policy (For data recovery)** checkbox, and specify the number of days you want to retain objects after deletion.
          * To set [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning), click the **Object versioning (For version control)** checkbox, and specify the maximum number of versions per object and the number of days after which the noncurrent versions expire.
          * To enable the retention policy on objects and buckets, click the **Retention (For compliance)** checkbox, and then do the following: 
            * To enable [Object Retention Lock](https://docs.cloud.google.com/storage/docs/object-lock), click the **Enable object retention** checkbox.
            * To enable [Bucket Lock](https://docs.cloud.google.com/storage/docs/bucket-lock), click the **Set bucket retention policy** checkbox, and choose a unit of time and a length of time for your retention period.
        * To choose how your object data will be encrypted, expand the **Data encryption** section (expand_more), and select a [**Data encryption** method](https://docs.cloud.google.com/storage/docs/encryption).
  17. Click **Create**. 



## Create a serverless batch workload with GPU accelerators

Submit a Managed Service for Apache Spark batch workload that uses [ NVIDIA L4](https://www.nvidia.com/en-us/data-center/l4/) GPUs to run a parallelized PySpark task. Follow these steps using the gcloud CLI:

  1. Click **Expand me** , then create and save the listed PySpark code to a `test-py-spark-gpu.py` file on your local machine using a text or code editor.

Expand me Collapse me
         
         #!/usr/bin/env python
         
         """S8s Accelerators Example."""
         
         import subprocess
         from typing import Any
         from pyspark.sql import SparkSession
         from pyspark.sql.functions import col
         from pyspark.sql.types import IntegerType
         from pyspark.sql.types import StructField
         from pyspark.sql.types import StructType
         
         spark = SparkSession.builder.appName("joindemo").getOrCreate()
         
         
         def get_num_gpus(_: Any) -> int:
           """Returns the number of GPUs."""
           p_nvidia_smi = subprocess.Popen(
               ["nvidia-smi", "-L"], stdin=None, stdout=subprocess.PIPE
           )
           p_wc = subprocess.Popen(
               ["wc", "-l"],
               stdin=p_nvidia_smi.stdout,
               stdout=subprocess.PIPE,
               stderr=subprocess.PIPE,
               universal_newlines=True,
           )
           [out, _] = p_wc.communicate()
           return int(out)
         
         
         num_workers = 5
         result = (
             spark.sparkContext.range(0, num_workers, 1, num_workers)
             .map(get_num_gpus)
             .collect()
         )
         num_gpus = sum(result)
         print(f"Total accelerators: {num_gpus}")
         
         # Run the join example
         schema = StructType([StructField("value", IntegerType(), True)])
         df = (
             spark.sparkContext.parallelize(range(1, 10000001), 6)
             .map(lambda x: (x,))
             .toDF(schema)
         )
         df2 = (
             spark.sparkContext.parallelize(range(1, 10000001), 6)
             .map(lambda x: (x,))
             .toDF(schema)
         )
         joined_df = (
             df.select(col("value").alias("a"))
             .join(df2.select(col("value").alias("b")), col("a") == col("b"))
             .explain()
         )

  2. Use the gcloud CLI on your local machine to submit the Managed Service for Apache Spark serverless batch job with five workers, with each worker accelerated with L4 GPUs:
         
         gcloud dataproc batches submit pyspark test-py-spark-gpu.py \
             --project=PROJECT_ID \
             --region=[REGION](https://docs.cloud.google.com/compute/docs/regions-zones#available) \
             --deps-bucket=BUCKET_NAME \
             --version=1.1 \
             --properties=spark.dataproc.executor.compute.tier=premium,spark.dataproc.executor.disk.tier=premium,spark.dataproc.executor.resource.accelerator.type=l4,spark.executor.instances=5,spark.dataproc.driverEnv.LANG=C.UTF-8,spark.executorEnv.LANG=C.UTF-8,spark.shuffle.manager=com.nvidia.spark.rapids.RapidsShuffleManager
         




Notes:

  * PROJECT_ID: Your Google Cloud project ID.
  * REGION: An available Compute Engine [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) to run the workload.
  * BUCKET_NAME: The name of your Cloud Storage bucket. Spark uploads workload dependencies to a `/dependencies` folder in this bucket before running the batch workload.
  * **\--version:** All [Supported Managed Service for Apache Spark runtimes](https://docs.cloud.google.com/managed-spark/docs/concepts/versions/serverless-versions#supported_versions) add the [NVIDIA cuDF for Apache Spark library](https://docs.nvidia.com/cudf-spark/latest/index.html) to each node of a GPU-accelerated workload. Only runtime version 1.1 adds the [XGBoost](https://xgboost.ai/) library to each node of a GPU-accelerated workload.
  * **\--properties** (see [Spark resource allocation properties](https://docs.cloud.google.com/managed-spark/docs/concepts/properties#resource_allocation_properties)) :

    * `spark.dataproc.driverEnv.LANG=C.UTF-8` and `spark.executorEnv.LANG=C.UTF-8` (required with runtime versions prior to `2.2`): These properties set the default character set to C.UTF-8.
    * `spark.dataproc.executor.compute.tier=premium` (required): GPU-accelerated workloads are billed using **premium** Data Compute Units (DCUs). See Managed Service for Apache Spark [Accelerator pricing](https://cloud.google.com/managed-spark/pricing#accelerator_pricing).

    * `spark.dataproc.executor.disk.tier=premium` (required): Nodes with A100-40, A100-80, or L4 accelerators must use the premium disk tier.

    * `spark.dataproc.executor.resource.accelerator.type=l4` (required): Only one GPU type must be specified. The example job selects the L4 GPU. The following accelerator types can be specified with the following argument names: 

GPU type | Argument name  
---|---  
A100 40GB | `a100-40`  
A100 80GB | `a100-80`  
    * `spark.executor.instances=5` (required): Must be at least two. Set to five for this example.

    * `spark.executor.cores` (optional): You can set this property to specify the number of core vCPUs. Valid values for L4 GPUs are `4`, the default, or `8`, `12`, `16`, `24`, `48` or `96`. The only valid, and default, value for A100 GPUs is `12`. Configurations with L4 GPUs and `24`, `48` or `96` cores have `2`, `4` or `8` GPUs attached to each executor. All other configurations have `1` GPU attached.

    * `spark.dataproc.executor.disk.size` (required): L4 GPUs have a fixed disk size of 375 GB, except for configurations with `24`, `48` or `96` cores, which have `750`, `1,500`, or `3,000` GB, respectively. If you set this property to a different value when submitting an L4-accelerated workload, an error occurs. If you select an A100 40 or A100 80 GPU, valid sizes are 375g, 750g, 1500g, 3000g, 6000g, and 9000g.

    * `spark.executor.memory` (optional) and `spark.executor.memoryOverhead` (restricted): You can set memory, but not memoryOverhead. The amount of available memory not consumed by the set property is applied to the unset property. `spark.executor.memoryOverhead` is set to 40% of available memory for PySpark batch workloads, and 10% for other workloads (see [Spark resource allocation properties](https://docs.cloud.google.com/managed-spark/docs/concepts/properties#resource_allocation_properties)).

The following table shows the maximum amount of memory that can be set for different A100 and L4 GPU configurations. The minimum value for either property is `1024` MB.

| A100 (40 GB) | A100 (80 GB) | L4 (4 cores) | L4 (8 cores) | L4 (12 cores) | L4 (16 cores) | L4 (24 cores) | L4 (48 cores) | L4 (96 cores)  
---|---|---|---|---|---|---|---|---|---  
Maximum total memory (MB) | 78040 | 165080 | 13384 | 26768 | 40152 | 53536 | 113072 | 160608 | 321216  
    * NVIDIA cuDF for Apache Spark library properties (optional): By default, Managed Service for Apache Spark sets the following NVIDIA cuDF for Apache Spark library property values:

      * `spark.plugins`=com.nvidia.spark.SQLPlugin
      * `spark.executor.resource.gpu.amount`=1
      * `spark.task.resource.gpu.amount`=1/$spark_executor_cores
      * `spark.shuffle.manager`=''. By default, this property is unset. NVIDIA recommends turning on the [CUDA-X shuffle manager](https://docs.nvidia.com/spark-rapids/user-guide/latest/additional-functionality/rapids-shuffle.html) when using GPUs to improve performance. To do this, set `spark.shuffle.manager=com.nvidia.spark.rapids.RapidsShuffleManager` when you submit a workload.
      * `spark.rapids.sql.concurrentGpuTasks`= minimum of (`gpuMemoryinMB` / 8, 4)
      * `spark.rapids.shuffle.multiThreaded.writer.threads`= minimum of (cpu cores in the VM / gpu count per VM, 32)
      * `spark.rapids.shuffle.multiThreaded.reader.threads`= minimum of (cpu cores in the VM / gpu count per VM, 32)

See [NVIDIA cuDF plug-in for Apache Spark Configuration](https://nvidia.github.io/spark-rapids/docs/configs.html) to set NVIDIA cuDF for Apache Spark library properties, and [NVIDIA cuDF plug-in for Apache Spark Advanced Configuration](https://nvidia.github.io/spark-rapids/docs/additional-functionality/advanced_configs.html) to set Spark advanced properties.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
