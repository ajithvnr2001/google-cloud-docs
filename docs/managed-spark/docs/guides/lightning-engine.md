---
url: https://docs.cloud.google.com/managed-spark/docs/guides/lightning-engine/
title: Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:03.839257+00:00
---

# Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/guides/lightning-engine/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use Lightning Engine

Lightning Engine is a high-performance execution environment for Apache Spark on Managed Service for Apache Spark that accelerates compute-intensive workloads and reduces runtime costs without requiring changes to your Spark code. It's designed for data engineers and analytics practitioners running compute-intensive workloads that use Spark DataFrame APIs, Spark Dataset APIs, or Spark SQL queries.

If your workloads are primarily I/O-bound or rely heavily on Resilient Distributed Datasets (RDDs), the standard engine might be more appropriate.

## Benefits

Lightning Engine benefits include the following:

  * **Accelerated data operations** : Achieve significant performance gains and cost savings through optimizations to cloud storage interaction, including metadata handling, write workloads, and vectored I/O.

  * **Intelligent query execution** : Leverage advanced optimizer enhancements that dynamically reduce data scanned, optimize data processing, and generate more efficient execution plans for faster, more cost-effective queries.

  * **Streamlined AI and ML workloads** : Reduce cluster startup times for GPU-based workloads, and simplify deployment in secure environments using images optimized for AI.




While Lightning Engine offers substantial performance gains, the specific impact varies with the workload.

## Comparison to standard engine

Lightning Engine is an alternative to the standard engine used to execute Spark jobs on a Managed Service for Apache Spark cluster. The following table compares Lightning Engine to standard engine activation properties, workload applicability, and key benefits.

Feature | Standard engine | Lightning Engine  
---|---|---  
**CLI flag** | `--engine=default` or unset the flag | `--engine=lightning`  
**Best For** | General purpose jobs, development, and testing | Enterprise-scale workloads requiring significant acceleration  
**Key Benefits** | Baseline performance | Optimized cloud storage interaction, intelligent query execution  
  
## Lightning Engine requirements

The following requirements apply to the Lightning Engine feature:

  * **Image version** : Lightning Engine must be used with Managed Service for Apache Spark image version `2.3.3` and later `2.3` subminor image version releases, or `3.0.2` and later `3.0` subminor image version releases (`debian13` and `ubuntu24` images).
  * **Supported jobs** : Spark, PySpark, SparkSQL, and SparkR are supported. The standard engine runs on other job types submitted to a Lightning Engine cluster.



## Native Query Execution

Native Query Execution (NQE) is an optional component of Lightning Engine that provides a deeper level of acceleration for specific jobs. It is a native engine based on [Apache Gluten](https://gluten.apache.org/) and [Velox](https://github.com/facebookincubator/velox?tab=readme-ov-file#readme), optimized for Google hardware, which boosts performance by running parts of a Spark query outside the JVM.

**NQE is recommended for** :
    Compute-intensive tasks that leverage Spark DataFrame APIs and Spark Dataset APIs, and Spark SQL queries that read data from Parquet, ORC, Apache Iceberg, and Delta Lake files and tables. The output file format doesn't affect its performance.
**NQE is not recommended for** :
    Jobs that rely heavily on Resilient Distributed Datasets (RDDs), User-Defined Functions (UDFs), most Spark Machine Learning (ML) libraries, and I/O-bound operations with delays due to storage access.

### Native Query Execution on ARM

Managed Service for Apache Spark supports Native Query Execution within Lightning Engine on ARM architecture, specifically optimized for Google Axion processors on [C4A ARM VMs](https://docs.cloud.google.com/compute/docs/instances/arm-on-compute#arm-c4-vms) (see [ARM machine types supported on Managed Service for Apache Spark](https://docs.cloud.google.com/managed-spark/docs/concepts/compute/supported-machine-types#arm-machine-types)) using the `2.3-ubuntu22-arm` image. Google Axion C4A instances are ARM-based VMs built on ARM Neoverse V2 cores that deliver significant price-performance improvements.

Running NQE on Google Axion ARM instances combines hardware-level price-performance and high per-core memory bandwidth with software-level native vectorized query acceleration, significantly reducing query runtimes and total cost of ownership (TCO).

Key benefits on ARM include:

  * **2.5x to 4x speedup over open source Spark** : Delivers 2.5x to 4x performance improvements compared to open source Apache Spark on analytical workloads.
  * **Cost optimization** : Maximizes the price-performance advantage of Google Axion C4A instances (which deliver [up to 65% better price-performance](https://cloud.google.com/blog/products/compute/first-google-axion-processor-c4a-now-ga-with-titanium-ssd) compared to comparable x86 instances).
  * **Full operator and format parity** : Full parity with x86 NQE operators, with native acceleration for Cloud Storage Parquet, Apache Iceberg, and Delta Lake table formats.
  * **Zero code changes** : Seamless activation on ARM clusters using standard configuration flags without modifying your Spark application code.



## Native Query Execution requirements

The following requirements apply to the Native Query Execution feature:

  * **Execution engine** : NQE is available only on clusters enabled with Lightning engine at cluster creation.

  * **Supported jobs** : Spark, PySpark, Spark SQL, and SparkR are supported. The standard engine will run (without NQE) on other job types submitted to a Lightning Engine cluster.

  * **No GPUs and Accelerators** : NQE-enabled jobs submitted on GPU accelerators will fail (but can benefit from Lightning Engine without NQE).

  * **Data types** : Inputs of the following data types are not supported:

    * Byte: ORC and Parquet
    * Struct, Array, Map: Parquet



### Architecture and operating system requirements

NQE requirements differ based on the processor architecture:

Architecture | Supported machine types | Supported operating system and image  
---|---|---  
**x86** | Intel and AMD machine families | `Debian-12` and `Ubuntu-22` (image version `2.3.3` and later `2.3` releases); `Debian-13` and `Ubuntu-24` (image version `3.0.2` and later `3.0` releases)  
**ARM** | [C4A machine series](https://docs.cloud.google.com/compute/docs/instances/arm-on-compute#arm-c4-vms) (Google Axion ARM VMs) | `2.3-ubuntu22-arm` image (version `2.3.3` and later `2.3` releases)  
  
## Pricing

For pricing information, see [Managed Service for Apache Spark pricing](https://docs.cloud.google.com/managed-spark/pricing#on_pricing).

## Create a Lightning Engine cluster

This section shows you how to create a Managed Service for Apache Spark cluster that enables Lightning Engine on Spark jobs submitted to the cluster.

You can also enable Native Query Execution (NQE) on the cluster when you create the cluster, or you can enable NQE later for specific Spark jobs submitted to the cluster.

### Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. Verify that you have the permissions required to complete this guide. 

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. Enable the Dataproc API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=dataproc.googleapis.com)

  6. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  7. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  8. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  9. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  10. Verify that you have the permissions required to complete this guide. 

  11. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  12. Enable the Dataproc API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=dataproc.googleapis.com)

  13. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  14. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  15. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init




#### Required roles

Certain Identity and Access Management (IAM) roles are required to create a Managed Service for Apache Spark cluster and submit jobs to the cluster. Depending on organization policies, a cloud project owner or service administrator might have already granted these roles to you or a service account. To check role grants, see [Do you need to grant roles?](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/iam#do_you_need_to_grant_roles).

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

**User roles**

To get the permissions that you need to create a Managed Service for Apache Spark cluster, ask your administrator to grant you the following IAM roles: 

  * [Dataproc Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.editor) (`roles/dataproc.editor`) on the project
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the Compute Engine default service account



**Service account role**

To ensure that the Compute Engine default service account has the necessary permissions to create a Managed Service for Apache Spark cluster, ask your administrator to grant the [Dataproc Worker ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`) IAM role to the Compute Engine default service account on the project. **Important:** You must grant this role to the Compute Engine default service account, _not_ to your user account. Failure to grant the role to the correct principal might result in permission errors. 

### Create the cluster

The following examples show you how to create a Lightning Engine cluster using the Google Cloud console, Google Cloud CLI, Dataproc API, Cloud Client Libraries for Python, or Terraform. You can also create a cluster with the Lightning Engine enabled using the [Go](https://docs.cloud.google.com/managed-spark/docs/guides/create-cluster#dataproc-create-cluster-go), [Java](https://docs.cloud.google.com/managed-spark/docs/guides/create-cluster#dataproc-create-cluster-java), and [Node.js](https://docs.cloud.google.com/managed-spark/docs/guides/create-cluster#dataproc-create-cluster-nodejs) Cloud Client Libraries.

### Console

  1. Open the [**Create cluster**](https://console.cloud.google.com/dataproc/clusters/create) page.
  2. Click **Additional configuration** to expand that section.
  3. Edit **Customization & Other**.
  4. In the panel that opens, confirm that the **Enable Lightning Engine** checkbox is selected.
  5. Optional: To enable the native execution runtime by default for Spark jobs, select the **Enable Native Execution** checkbox.
  6. Click **Save**.
  7. Configure other cluster settings as needed.
  8. Click **Create cluster**.



**Create an ARM cluster** :

To create an ARM cluster with Google Axion and Native Query Execution:

  1. In **Worker configuration** , select the **C4A** machine series and choose your ARM machine type.
  2. In **Image** , select the `2.3-ubuntu22-arm` image.
  3. In **Additional configuration** > **Customization & Other**, confirm that **Enable Lightning Engine** and **Enable Native Execution** are selected.
  4. Click **Create cluster**.



### gcloud

  1. To create a cluster with the Lightning Engine enabled, run the `gcloud dataproc clusters create` command with the `--engine=lightning` flag. For more information, see [create a cluster with gcloud CLI](https://docs.cloud.google.com/managed-spark/docs/guides/create-cluster#dataproc-create-cluster-gcloud).
         
         gcloud dataproc clusters create CLUSTER_NAME \
             --region=REGION \
             --engine=lightning \
             --image-version=2.3
         

  2. Optional: To enable the native execution runtime by default for Spark jobs, include the `spark:spark.dataproc.lightningEngine.runtime=native` property.
         
         gcloud dataproc clusters create CLUSTER_NAME \
             --region=REGION \
             --engine=lightning \
             --image-version=2.3 \
             --properties='spark:spark.dataproc.lightningEngine.runtime=native'
         

  3. Create an ARM cluster with NQE: To create a Managed Service for Apache Spark cluster with Google Axion C4A ARM nodes and NQE enabled:
         
         gcloud dataproc clusters create CLUSTER_NAME \
             --region=REGION \
             --image-version=2.3-ubuntu22-arm \
             --master-machine-type=c4a-standard-16 \
             --worker-machine-type=c4a-standard-16 \
             --engine=lightning \
             --properties='spark:spark.dataproc.lightningEngine.runtime=native'
         




### API

To create a cluster with the Lightning Engine enabled, send a `clusters.create` request. For more information, see [create a cluster with the REST API](https://docs.cloud.google.com/managed-spark/docs/guides/create-cluster#dataproc-create-cluster-drest).

  1. In the request body, set the [`engine`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#engine) field to `LIGHTNING`.
         
         {
           "projectId": "PROJECT_ID",
           "clusterName": "CLUSTER_NAME",
           "config": {
             "engine": "LIGHTNING",
             "gceClusterConfig": {},
             "softwareConfig": {
               "imageVersion": "2.3"
             }
           }
         }
         

  2. Optional: To enable the native execution runtime by default for all jobs, include the `spark:spark.dataproc.lightningEngine.runtime` property.
         
         {
           "projectId": "PROJECT_ID",
           "clusterName": "CLUSTER_NAME",
           "config": {
             "engine": "LIGHTNING",
             "gceClusterConfig": {},
             "softwareConfig": {
               "imageVersion": "2.3",
               "properties": {
                 "spark:spark.dataproc.lightningEngine.runtime": "native"
               }
             }
           }
         }
         




### Python

  1. To create a cluster with the Lightning Engine enabled, use the `create_cluster` method and set the `engine` field in the cluster configuration to `LIGHTNING`. For more information, see [create a cluster with Python](https://docs.cloud.google.com/managed-spark/docs/guides/create-cluster#dataproc-create-cluster-python).
         
         from google.cloud import [dataproc_v1](https://docs.cloud.google.com/python/docs/reference/dataproc/latest)
         
         def create_lightning_cluster(project_id, region, cluster_name):
             client_options = {"api_endpoint": f"{region}-dataproc.googleapis.com:443"}
             cluster_client = [dataproc_v1](https://docs.cloud.google.com/python/docs/reference/dataproc/latest).[ClusterControllerClient](https://docs.cloud.google.com/python/docs/reference/dataproc/latest/google.cloud.dataproc_v1.services.cluster_controller.ClusterControllerClient.html)(client_options=client_options)
         
             cluster = {
                 "project_id": project_id,
                 "cluster_name": cluster_name,
                 "config": {
                     "engine": "LIGHTNING",
                     "software_config": {
                         "image_version": "2.3-debian12",
                     },
                 }
             }
         
             operation = cluster_client.[create_cluster](https://docs.cloud.google.com/python/docs/reference/dataproc/latest/google.cloud.dataproc_v1.services.cluster_controller.ClusterControllerClient.html#google_cloud_dataproc_v1_services_cluster_controller_ClusterControllerClient_create_cluster)(
                 project_id=project_id,
                 region=region,
                 cluster=cluster
             )
             result = operation.result()
             print(f"Cluster created successfully: {result.cluster_name}")
         

  2. Optional: To enable the native execution runtime by default for Spark jobs, include the `spark:spark.dataproc.lightningEngine.runtime` property.
         
         from google.cloud import [dataproc_v1](https://docs.cloud.google.com/python/docs/reference/dataproc/latest)
         
         def create_lightning_native_cluster(project_id, region, cluster_name):
             client_options = {"api_endpoint": f"{region}-dataproc.googleapis.com:443"}
             cluster_client = [dataproc_v1](https://docs.cloud.google.com/python/docs/reference/dataproc/latest).[ClusterControllerClient](https://docs.cloud.google.com/python/docs/reference/dataproc/latest/google.cloud.dataproc_v1.services.cluster_controller.ClusterControllerClient.html)(client_options=client_options)
         
             cluster = {
                 "project_id": project_id,
                 "cluster_name": cluster_name,
                 "config": {
                     "engine": "LIGHTNING",
                     "software_config": {
                         "image_version": "2.3-debian12",
                         "properties": {
                             "spark:spark.dataproc.lightningEngine.runtime": "native"
                         }
                     }
                 }
             }
         
             operation = cluster_client.[create_cluster](https://docs.cloud.google.com/python/docs/reference/dataproc/latest/google.cloud.dataproc_v1.services.cluster_controller.ClusterControllerClient.html#google_cloud_dataproc_v1_services_cluster_controller_ClusterControllerClient_create_cluster)(
                 project_id=project_id,
                 region=region,
                 cluster=cluster
             )
             result = operation.result()
             print(f"Cluster created successfully: {result.cluster_name}")
         




### Terraform

  1. In your `google_dataproc_cluster` resource configuration, set the `engine` argument to `LIGHTNING`.
  2. For more details and advanced options, refer to the official Terraform documentation for the [`google_dataproc_cluster`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/dataproc_cluster#example-usage---advanced) resource.



### Verify the cluster engine

### Console

  1. In the Google Cloud console, go to the **Cluster Details** page.
  2. Verify that `Lightning Engine` value is listed in the **Engine** field.
  3. If you enabled Native Query Execution, verify that `native` is listed in the **Native Execution** field.



### gcloud

  1. To verify the engine and NQE (if enabled), run the `gcloud dataproc clusters describe` command:
         
         gcloud dataproc clusters describe CLUSTER_NAME --project=PROJECT_ID --region=REGION
         

  2. Check the output for the `engine` and `lightningEngine.runtime` properties:
         
         clusterName: lightning-engine-cluster
         engine: lightningEngine
         lightningEngine.runtime: native
         




## Submit a job with Lightning Engine

If you enabled Lightning Engine when you created a cluster, when you submit a Spark job to the cluster, Lightning Engine is enabled by default on the job.

### Enable Native Query Execution for a job

If you enabled Native Query Execution (NQE) when you created a Lightning Engine cluster, all Spark jobs run with NQE enabled unless you disable NQE on a specific job.

If you didn't enable NQE when you created the Lightning Engine cluster, you can enable NQE for a job when you submit the job, as shown in the following examples.

### gcloud

To enable Native Query Execution when you [submit a Spark job](https://docs.cloud.google.com/managed-spark/docs/guides/submit-job#dataproc-submit-job-gcloud), include the `spark.dataproc.lightningEngine.runtime=native` property:
    
    
    gcloud dataproc jobs submit spark \
        --cluster=CLUSTER_NAME \
        --region=REGION \
        --properties=spark.dataproc.lightningEngine.runtime=native \
        -- ...
    

### API

To enable Native Query Execution when you [submit a Spark job](https://docs.cloud.google.com/managed-spark/docs/guides/submit-job#dataproc-submit-job-drest), include the `spark.dataproc.lightningEngine.runtime` property in your request:
    
    
    {
      "job":{
        "placement":{
          "clusterName": ...
        },
        "sparkJob":{
          "mainClass": ...,
          "properties":{
             "spark.dataproc.lightningEngine.runtime":"native"
          }
        }
      }
    }
    

### Disable Native Query Execution for a job

If you enabled Native Query Execution (NQE) when you created a Lightning Engine cluster, all Spark jobs will run with NQE enabled unless you disable NQE on a specific job.

You can disable NQE for a specific Spark job when you submit the job, as shown in the following examples.

### gcloud

To disable Native Query Execution when you [submit a Spark job](https://docs.cloud.google.com/managed-spark/docs/guides/submit-job#dataproc-submit-job-gcloud), to a Lightning Engine cluster, include the `spark.dataproc.lightningEngine.runtime=default` property:
    
    
    gcloud dataproc jobs submit spark \
        --cluster=CLUSTER_NAME \
        --region=REGION \
        --properties=spark.dataproc.lightningEngine.runtime=default \
        -- ...
    

### API

To disable Native Query Execution when you [submit a Spark job](https://docs.cloud.google.com/managed-spark/docs/guides/submit-job#dataproc-submit-job-drest), to a Lightning Engine cluster, include the `spark.dataproc.lightningEngine.runtime=default` property:
    
    
    {
      "job":{
        "placement":{
          "clusterName": ...
        },
        "sparkJob":{
          "mainClass": ...,
          "properties":{
             "spark.dataproc.lightningEngine.runtime":"default"
          }
        }
      }
    }
    

### Verify Native Query Execution for a job

After you submit a job to a Lightning Engine cluster, you can verify that Native Query Execution is enabled for the job.

### Console

  1. In the Google Cloud console, go to the **Jobs** page.
  2. Click the job ID to open the **Job details** page.
  3. Verify that `native` is listed in the **Native Execution** field.



### gcloud

  1. Run the `gcloud dataproc jobs describe` command:
         
         gcloud dataproc jobs describe JOB_ID --project=PROJECT_ID --region=REGION
         

  2. Check the output for the `lightningEngine.runtime` in the **Properties** section:
         
         lightningEngine.runtime: native
         




## Configuration parameters

The following table summarizes the main configuration parameters for Lightning Engine and Native Query Execution.

Parameter Name | Description | Applicable engine(s) | Default value | Default value (Lightning Engine) | User overridable (job level) | Scope  
---|---|---|---|---|---|---  
`--engine` | Cluster-level setting to select the engine during cluster creation. | Cluster-wide | `default` | `lightning` | No | Cluster  
`spark:spark.dataproc.lightningEngine.runtime` | Cluster-level setting to select the Lightning engine runtime during cluster creation. | Lightning only | `default` | `default` | No | Cluster  
`spark.dataproc.lightningEngine.runtime` | Enables or disables Native Query Execution (NQE) within the Lightning Engine. | Lightning only | `default` | `default` | Yes. Can be set to `native` or `default`. | Job  
  
## Limitations

Enabling Native Query Execution in the following scenarios can cause exceptions, Spark incompatibilities, or workload fallback to the default Spark engine.

### Fallbacks

Native Query Execution in the following scenarios can result in a workload fallback to the Spark execution engine:

  * **ANSI** : If ANSI mode is enabled, execution falls back to Spark.
  * **Case-sensitive mode** : Native Query Execution supports only the Spark default case-insensitive mode. If case-sensitive mode is enabled, incorrect results can occur.
  * **Partitioned table scan** : Native Query Execution supports the partitioned table scan only when the path contains the partition information. Otherwise, the workload falls back to the Spark execution engine.



### Incompatible behavior

Incompatible behavior or incorrect results can occur when you use Native Query Execution in the following cases:

  * **JSON functions** : Native Query Execution supports strings surrounded by double quotes, not single quotes. Incorrect results occur with single quotes. Using `*` in the path with the `get_json_object` function returns `NULL`.
  * **Parquet read configuration** : 
    * Native Query Execution treats `spark.files.ignoreCorruptFiles` as set to the default `false` value, even when set to `true`.
    * Native Query Execution ignores `spark.sql.parquet.datetimeRebaseModeInRead`, and returns only the Parquet file contents. Differences between the legacy hybrid calendar and the Proleptic Gregorian calendar are not considered. Spark results can differ.
  * **NaN** : not supported. Unexpected results can occur, for example, when you use `NaN` in a numeric comparison.
  * **Spark columnar reading** : a fatal error can occur because the Spark columnar vector is incompatible with Native Query Execution.
  * **Spill** : when you set shuffle partitions to a large number, the spill-to-disk feature can trigger an `OutOfMemoryException`. If this occurs, reducing the number of partitions can eliminate this exception.



## What's next

  * [Accelerate Spark batch workloads and sessions with Lightning Engine](https://docs.cloud.google.com/managed-spark/docs/guides/lightning-engine-serverless).
  * Review [ARM machine types supported on Managed Service for Apache Spark](https://docs.cloud.google.com/managed-spark/docs/concepts/compute/supported-machine-types#arm-machine-types).
  * Learn how to [tune Spark jobs for optimal performance](https://docs.cloud.google.com/managed-spark/docs/support/spark-job-tuning).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
