---
url: https://docs.cloud.google.com/managed-spark/docs/guides/performance-enhancements/
title: Managed Service for Apache Spark performance enhancements \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:04.608934+00:00
---

# Managed Service for Apache Spark performance enhancements  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/guides/performance-enhancements/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Managed Service for Apache Spark performance enhancements Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to enable the Managed Service for Apache Spark Spark performance enhancements to help your Managed Service for Apache Spark jobs process more data in less time with reduced costs.

Managed Service for Apache Spark performance enhancements include:

  * Spark Optimizer enhancements: 
    * Optimizer rules written for better Spark plans
    * Improved performance of the Managed Service for Apache Spark BigQuery connector when used in Spark jobs
  * Spark Execution enhancements: 
    * Spark execution engine improvements



**Other Managed Service for Apache Spark performance improvements:** See Managed Service for Apache Spark [cluster caching](https://docs.cloud.google.com/managed-spark/docs/concepts/cluster-caching), which helps reduce the amount of time spent accessing data in Cloud Storage.

You can enable Spark performance enhancements on a cluster or on a Spark job:

  * Spark performance enhancements enabled on a cluster apply, by default, to all Spark jobs run on the cluster, whether submitted to the Managed Service for Apache Spark or [submitted directly to the cluster](https://docs.cloud.google.com/managed-spark/docs/guides/submit-job#submit_a_job_directly_on_your_cluster).

  * Spark performance enhancements can also be enabled or disabled on a job that is submitted to Managed Service for Apache Spark. Spark performance enhancements settings applied to a job override any conflicting settings set at the cluster level for the specified job only.




## Pricing

Spark performance enhancements don't incur additional charges. Standard [Managed Service for Apache Spark pricing](https://cloud.google.com/managed-spark/pricing#on_pricing) applies.

## Considerations

Spark performance enhancements adjusts Spark properties, including the following properties:

  * [`spark.sql.shuffle.partitions`](https://docs.cloud.google.com/managed-spark/docs/support/spark-job-tuning#configuring_partitions): Spark performance enhancements set this property to `1000` for `2.2` image version clusters. This setting can slow small jobs.
  * `spark.dataproc.sql.catalog.file.index.stats.enabled`: This setting can result in driver OOM (Out-Of-Memory) conditions if the Hive partition count is high. Disabling this property can fix the OOM condition.



## Enable enhancements at cluster creation

You can use the Google Cloud console, Google Cloud CLI, and the Dataproc API to enable Managed Service for Apache Spark performance enhancements when you create a Managed Service for Apache Spark cluster with image versions 2.0.69+, 2.1.17+, 2.2.0+, and later image releases.

### Console

  1. In the Google Cloud console, open the [**Create cluster**](https://console.cloud.google.com/dataproc/clusters/create) page. 
  2. Click **Additional configuration** to expand that section.
  3. Edit **Customization & Other**.
  4. In the **Cluster properties** section, add the following properties: 
     * To enable Spark optimization enhancements: 
       1. Click **\+ Add properties**.
       2. Select **spark** in the **Prefix** list.
       3. Enter `spark.dataproc.enhanced.optimizer.enabled` in the **Key** field and `true` in the **Value** field.
     * To enable Spark execution enhancements: 
       1. Click **\+ Add properties**.
       2. Select **spark** in the **Prefix** list.
       3. Enter `spark.dataproc.enhanced.execution.enabled` in the **Key** field and `true` in the **Value** field.
  5. Complete other cluster fields, then click **Create cluster**.



### gcloud

  1. Run the following [gcloud dataproc clusters create](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) command locally in a terminal window or in [Cloud Shell](https://console.cloud.google.com/?cloudshell=true%22).
         
         gcloud dataproc clusters create CLUSTER_NAME \
             --project=PROJECT_ID \
             --region=REGION \
             --image-version=IMAGE \
             --properties=PROPERTIES
         

Notes:

     * CLUSTER_NAME: The cluster name, which must be unique within a project. The name must start with a lowercase letter, and can contain up to 51 lowercase letters, numbers, and hyphens. It cannot end with a hyphen. The name of a deleted cluster can be reused.
     * PROJECT_ID: The project to associate with the cluster.
     * REGION: The [Compute Engine region](https://docs.cloud.google.com/compute/docs/regions-zones#available) where the cluster will be located, such as `us-central1`. 
       * You can add the optional `--zone=ZONE` flag to specify a zone within the specified region, such as `us-central1-a`. If you do not specify a zone, the Managed Service for Apache Spark [autozone placement](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/auto-zone) feature selects a zone with the specified region.
     * IMAGE: The Managed Service for Apache Spark optimizer and execution performance enhancements are available in Managed Service for Apache Spark image versions `2.0.69+` and `2.1.17+` and later releases. If you omit this flag, Managed Service for Apache Spark will select the latest subminor version of the default Managed Service for Apache Spark image for the cluster (see [Default Managed Service for Apache Spark image version](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-version-clusters#default_dataproc_image_version)).
     * PROPERTIES:

       * To enable Spark optimization enhancements, specify:
    
    spark:spark.dataproc.enhanced.optimizer.enabled=true
    

       * To enable Spark execution enhancements, specify:
    
    spark:spark.dataproc.enhanced.execution.enabled=true
    

       * To enable Spark optimization and execution enhancements, specify:
    
    spark:spark.dataproc.enhanced.optimizer.enabled=true,spark:spark.dataproc.enhanced.execution.enabled=true
    




### API

  1. Specify the following [`SoftwareConfig.properties`](https://docs.cloud.google.com/static/managed-spark/docs/reference/rest/v1/ClusterConfig#SoftwareConfig.FIELDS.properties) as part of a [`clusters.create`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create) request:

     * To enable Spark optimization enhancements, specify:
    
    "spark:spark.dataproc.enhanced.optimizer.enabled": "true"
    

     * To enable Spark execution enhancements, specify:
    
    "spark:spark.dataproc.enhanced.execution.enabled": "true"
    

     * To enable Spark optimization and execution enhancements, specify:
    
    "spark:spark.dataproc.enhanced.optimizer.enabled": "true","spark:spark.dataproc.enhanced.execution.enabled": "true"
    




## Enable or disable enhancements at job submission

You can use the Google Cloud console, Google Cloud CLI, and the Dataproc API to enable or disable Spark performance enhancements on a Spark job submitted to Managed Service for Apache Spark.

### Console

  1. In the Google Cloud console, open the [Jobs](https://console.cloud.google.com/dataproc/jobs) page.
  2. On the **Jobs** page, click **Submit job** , then scroll to the job **Properties** section. 
     1. To enable Spark optimization enhancements: 
        1. Click **\+ Add properties**. Add "spark.dataproc.enhanced.optimizer.enabled" in the **Key** field and "true" in **Value** field.
     2. To enable Spark execution enhancements: 
        1. Click **\+ Add properties**.
        2. Add "spark.dataproc.enhanced.execution.enabled" in the **Key** field and "true" in **Value** field.
  3. Complete filling in or confirming the other job submission fields, then click **Submit**.



### gcloud

  1. Run the following [gcloud dataproc jobs submit](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit) command locally in a terminal window or in [Cloud Shell](https://console.cloud.google.com/?cloudshell=true%22).
         
         gcloud dataproc jobs submit SPARK_JOB_TYPE \
             --cluster=CLUSTER_NAME \
             --region=REGION \
             --properties=PROPERTIES
         

Notes:

     * SPARK_JOB_TYPE: Specify `spark`, `pyspark`, `spark-sql` or `spark-r` .
     * CLUSTER_NAME: The name of the job where the job will run.
     * REGION: The region where the cluster is located.
     * PROPERTIES:

       * To enable Spark optimization enhancements, specify:
    
    spark.dataproc.enhanced.optimizer.enabled=true
    

       * To enable Spark execution enhancements, specify:
    
    spark.dataproc.enhanced.execution.enabled=true
    

       * To enable Spark optimization and execution enhancements, specify:
    
    spark.dataproc.enhanced.optimizer.enabled=true,spark.dataproc.enhanced.execution.enabled=true
    




### API

  1. Specify the following `properties` for a [SparkJob](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/SparkJob), [PySparkJob](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/PySparkJob), [SparkSqlJob](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/SparkSqlJob), or [SparkRJob](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/SparkRJob) as part of a [`jobs.submit`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.jobs/submit) request:

     * To enable Spark optimization enhancements, specify:
    
    "spark.dataproc.enhanced.optimizer.enabled=true"
    

     * To enable Spark execution enhancements, specify:
    
    "spark.dataproc.enhanced.execution.enabled=true"
    

     * To enable Spark optimization and execution enhancements, specify:
    
    "spark.dataproc.enhanced.execution.enabled=true,spark.dataproc.enhanced.optimizer.enabled=true"
    




**Note:** At the bottom of the [Create cluster](https://console.cloud.google.com/dataproc/clusters/create) page, click **Equivalent command line** or **Equivalent REST** to have the Google Cloud console construct an equivalent gcloud CLI command or API REST request.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
