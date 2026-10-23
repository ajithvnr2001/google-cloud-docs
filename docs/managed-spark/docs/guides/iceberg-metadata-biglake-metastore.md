---
url: https://docs.cloud.google.com/managed-spark/docs/guides/iceberg-metadata-biglake-metastore/
title: Create an Apache Iceberg table with metadata in Lakehouse runtime catalog \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:04.147122+00:00
---

# Create an Apache Iceberg table with metadata in Lakehouse runtime catalog  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/guides/iceberg-metadata-biglake-metastore/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Create an Apache Iceberg table with metadata in Lakehouse runtime catalog Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** To provide feedback or ask questions that are related to this preview feature, contact [dataproc-previews@google.com](mailto:dataproc-previews@google.com).

This document shows you how to create an Apache Iceberg table with metadata in Lakehouse runtime catalog using the Managed Service for Apache Spark Jobs service, the [Spark SQL CLI](https://spark.apache.org/docs/3.5.2/sql-distributed-sql-engine-spark-sql-cli.html) or the [Zeppelin](https://docs.cloud.google.com/managed-spark/docs/concepts/components/zeppelin) web interface running on a Managed Service for Apache Spark cluster.

## Before you begin

If you haven't done so, create a Google Cloud project, a Cloud Storage [bucket](https://docs.cloud.google.com/storage/docs/xml-api/put-bucket-create), and a Managed Service for Apache Spark cluster.

  1. **Set up your project**

     1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
     2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

        * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
        * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

     3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

     4. Enable the Dataproc, BigQuery, and Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataproc.googleapis.com,bigquery.googleapis.com,storage-component.googleapis.com)

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

     10. Enable the Dataproc, BigQuery, and Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataproc.googleapis.com,bigquery.googleapis.com,storage-component.googleapis.com)

     11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

     12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

     13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
            
            gcloud init

  2. **Create a Cloud Storage[bucket](https://docs.cloud.google.com/storage/docs/xml-api/put-bucket-create)** in your project. 

     1. In the Google Cloud console, go to the Cloud Storage **Buckets** page. 

[Go to Buckets](https://console.cloud.google.com/storage/browser)

     2. Click add_box **Create**. 
     3. On the **Create a bucket** page, enter your bucket information. To go to the next step, click **Continue**. 
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
     4. Click **Create**. 
  3. [Create a Managed Service for Apache Spark cluster](https://docs.cloud.google.com/managed-spark/docs/guides/create-cluster#creating_a_cloud_dataproc_cluster). To save resources and costs, you can [create a single-node Managed Service for Apache Spark cluster](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/single-node-clusters#creating_a_single_node_cluster) to run the examples presented in this document.

     * The subnet in the region where the cluster is created must have [Private Google Access (PGA)](https://docs.cloud.google.com/vpc/docs/private-google-access) enabled. By default, Managed Service for Apache Spark cluster VMs, created with a 2.2 (default) or later image version, have [internal IP addresses only](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/network#create-a-dataproc-cluster-with-internal-IP-addresses-only). To allow cluster VMs to communicate with Google APIs, [enable Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#config-pga) on the `default` (or user-specified network name, if applicable) network subnet in the region where the cluster is created..

     * If you want to run the Zeppelin web interface example in this guide, you must use or create a Managed Service for Apache Spark cluster with the [Zeppelin optional component enabled](https://docs.cloud.google.com/managed-spark/docs/concepts/components/zeppelin#install_the_component).

  4. Grant roles to a custom service account (if needed): By default, Managed Service for Apache Spark cluster VMs use the [Compute Engine default service account](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/service-accounts#VM_service_account) to interact with Managed Service for Apache Spark. If you want to specify a [custom service account](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/service-accounts#create_a_cluster_with_a_custom_vm_service_account) when you create your cluster, it must have the [Managed Service for Apache Spark Worker role (`roles/dataproc.worker`)](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) role or a custom role with needed Worker role permissions.




## OSS database to BigQuery dataset mapping

Note the following mapping between open source database and BigQuery dataset terms:

**OSS database** | **BigQuery dataset**  
---|---  
Namespace, Database | Dataset  
Partitioned or Unpartitioned Table | Table  
View | View  
  
## Create an Iceberg table

This section shows you how to create an Iceberg table with metadata in Lakehouse runtime catalog by submitting a Spark SQL code to the [Managed Service for Apache Spark](https://docs.cloud.google.com/managed-spark/docs/guides/submit-job), the [Spark SQL CLI](https://spark.apache.org/docs/latest/sql-distributed-sql-engine-spark-sql-cli.html), and the [Zeppelin component](https://docs.cloud.google.com/managed-spark/docs/concepts/components/zeppelin) web interface, which run on a Managed Service for Apache Spark cluster.

### Managed Service for Apache Spark job

You can submit a job to Managed Service for Apache Spark by [submitting the job to a Managed Service for Apache Spark cluster](https://docs.cloud.google.com/managed-spark/docs/guides/submit-job#how_to_submit_a_job) using the [Google Cloud console](https://console.cloud.google.com/dataproc/jobs/jobsSubmit) or the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit), or via a HTTP [REST](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.jobs) request or programmatic [gRPC](https://docs.cloud.google.com/managed-spark/docs/reference/rpc) Managed Service for Apache Spark [Cloud Client Libraries](https://docs.cloud.google.com/managed-spark/docs/reference/libraries) call to the Jobs API.

The examples in this section show you how to submit a Managed Service for Apache Spark Spark SQL job to the Managed Service for Apache Spark service to create an Iceberg table with metadata in BigQuery using the gcloud CLI, Google Cloud console, or REST API.

### Prepare job files

Perform the following steps to create a Spark SQL job file. The file contains Spark SQL commands to create and update an Iceberg table.

  1. In a local terminal window or in [Cloud Shell](https://console.cloud.google.com/?cloudshell=true), use a text editor, such as the `vi` or `nano`, to copy the following commands into an `iceberg-table.sql` file, then save the file in the current directory.
         
         USE CATALOG_NAME;
         CREATE NAMESPACE IF NOT EXISTS example_namespace;
         USE example_namespace;
         DROP TABLE IF EXISTS example_table;
         CREATE TABLE example_table (id int, data string) USING ICEBERG LOCATION 'gs://BUCKET/WAREHOUSE_FOLDER';
         INSERT INTO example_table VALUES (1, 'first row');
         ALTER TABLE example_table ADD COLUMNS (newDoubleCol double);
         DESCRIBE TABLE example_table;
         

Replace the following:

     * CATALOG_NAME: Iceberg catalog name.
     * BUCKET and WAREHOUSE_FOLDER: Cloud Storage bucket and folder used for the Iceberg warehouse.
  2. Use [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) to copy the local `iceberg-table.sql` to your bucket in Cloud Storage.
         
         gcloud storage cp iceberg-table.sql gs://BUCKET/
         




Next, download and copy the `iceberg-spark-runtime-3.5_2.12-1.6.1` JAR file to Cloud Storage.

  1. In a local terminal window or in [Cloud Shell](https://console.cloud.google.com/?cloudshell=true), run the following `curl` command to download the `iceberg-spark-runtime-3.5_2.12-1.6.1` JAR file to the current directory.
         
         curl -o iceberg-spark-runtime-3.5_2.12-1.6.1.jar https://storage-download.googleapis.com/maven-central/maven2/org/apache/iceberg/iceberg-spark-runtime-3.5_2.12/1.6.1/iceberg-spark-runtime-3.5_2.12-1.6.1.jar
         

  2. Uses the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) to copy the local `iceberg-spark-runtime-3.5_2.12-1.6.1` JAR file from the current directory to your bucket in Cloud Storage.
         
         gcloud storage cp iceberg-spark-runtime-3.5_2.12-1.6.1.jar gs://BUCKET/
         




### Submit the Spark SQL job

Select a tab to follow the instructions to submit the Spark SQL job to the Managed Service for Apache Spark using the gcloud CLI, Google Cloud console, or Managed Service for Apache Spark REST API.

### gcloud

  1. Run the following [gcloud dataproc jobs submit spark-sql](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/spark-sql) command locally in a local terminal window or in [Cloud Shell](https://console.cloud.google.com/?cloudshell=true) to submit the Spark SQL job to create the Iceberg table.
         
         gcloud dataproc jobs submit spark-sql \
             --project=PROJECT_ID \
             --cluster=CLUSTER_NAME \
             --region=REGION \
             --jars="gs://BUCKET/1.6.1/iceberg-spark-runtime-3.5_2.12-1.6.1.jar,BIGLAKE_ICEBERG_CATALOG_JAR" \
             --properties="spark.sql.catalog.CATALOG_NAME=org.apache.iceberg.spark.SparkCatalog,spark.sql.catalog.CATALOG_NAME.catalog-impl=org.apache.iceberg.gcp.bigquery.BigQueryMetastoreCatalog,spark.sql.catalog.CATALOG_NAME.gcp_project=PROJECT_ID,spark.sql.catalog.CATALOG_NAME.gcp_location=LOCATION,spark.sql.catalog.CATALOG_NAME.warehouse=gs://BUCKET/WAREHOUSE_FOLDER" \
             -f="gs://BUCKETiceberg-table.sql"
         

Notes:

     * PROJECT_ID: Your Google Cloud project ID. Project IDs are listed in the **Project info** section on the Google Cloud console [Dashboard](https://console.cloud.google.com/home/dashboard).
     * CLUSTER_NAME: The name of your Managed Service for Apache Spark cluster.
     * REGION: The Compute Engine [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) where your cluster is located.
     * `BIGLAKE_ICEBERG_CATALOG_JAR`: the Cloud Storage URI of the Iceberg custom catalog plugin to use. Depending on your Iceberg version number, select one of the following: 
       * Iceberg 1.9.1: `gs://spark-lib/bigquery/iceberg-bigquery-catalog-1.9.1-1.0.1.jar`
       * Iceberg 1.6.1: `gs://spark-lib/bigquery/iceberg-bigquery-catalog-1.6.1-1.0.2.jar`
     * CATALOG_NAME: Iceberg catalog name.
     * BUCKET and WAREHOUSE_FOLDER: Cloud Storage bucket and folder used for the Iceberg warehouse.
     * LOCATION: A supported [BigQuery location](https://docs.cloud.google.com/bigquery/docs/locations#supported_locations). The default location is "US".
     * `--jars`: The listed jars are necessary to create table metadata in Lakehouse runtime catalog.
     * `--properties`: [Catalog properties](https://iceberg.apache.org/docs/latest/spark-configuration/).
     * `-f`: The `iceberg-table.sql` job file you copied to your bucket in Cloud Storage.
  2. View the table description in the terminal output when the job finishes.
         
         Time taken: 2.194 seconds
         id                      int
         data                    string
         newDoubleCol            double
         Time taken: 1.479 seconds, Fetched 3 row(s)
         Job JOB_ID finished successfully.
         

  3. To view table metadata in BigQuery

     1. In the Google Cloud console, go to the **BigQuery** page.

[Go to BigQuery Studio](https://console.cloud.google.com/bigquery)

     2. View Iceberg table metadata.

![](https://docs.cloud.google.com/static/managed-spark/images/bigquery-table-metadata.png)



### Console

Perform the following steps to use the Google Cloud console to submit the Spark SQL job to Managed Service for Apache Spark to create an Iceberg table with metadata in Lakehouse runtime catalog.

  1. In the Google Cloud console, go to the Managed Service for Apache Spark **Submit a job**.

[Go to Submit a job](https://console.cloud.google.com/dataproc/jobs/jobsSubmit) page, then complete the following fields:

     * **Job ID** : Accept the suggested ID or insert your own ID.
     * **Region** : Select the region where your cluster is located.
     * **Cluster** : Select your cluster.
     * **Job type** : Select `SparkSql`.
     * **Query source type** : Select `Query file`.
     * **Query file** : Insert `gs://BUCKET/iceberg-table.sql`
     * **Jar files** : Insert the following: 
           
           gs://BUCKET/iceberg-spark-runtime-3.5_2.12-1.6.1.jar,BIGLAKE_ICEBERG_CATALOG_JAR
           

     * **BIGLAKE_ICEBERG_CATALOG_JAR** : the Cloud Storage URI of the Iceberg custom catalog plugin to use. Depending on your Iceberg version number, select one of the following: 
       * Iceberg 1.9.1: `gs://spark-lib/bigquery/iceberg-bigquery-catalog-1.9.1-1.0.1.jar`
       * Iceberg 1.6.1: `gs://spark-lib/bigquery/iceberg-bigquery-catalog-1.6.1-1.0.2.jar`
     * **Properties** : Click add**Add Property** five times to create a list of five `key` `value` input fields, then copy the following **Key** and **Value** pairs to define five properties. # | Key | Value  
---|---|---  
1. | 
           
           spark.sql.catalog.CATALOG_NAME
           

| 
           
           org.apache.iceberg.spark.SparkCatalog
             
  
2. | 
           
           spark.sql.catalog.CATALOG_NAME.catalog-impl
           

| 
           
           org.apache.iceberg.gcp.bigquery.BigQueryMetastoreCatalog
             
  
3. | 
           
           spark.sql.catalog.CATALOG_NAME.gcp_project
           

| 
           
           PROJECT_ID
             
  
4. | 
           
           spark.sql.catalog.CATALOG_NAME.gcp_location
           

| 
           
           LOCATION
             
  
5. | 
           
           spark.sql.catalog.CATALOG_NAME.warehouse
           

| 
           
           gs://BUCKET/WAREHOUSE_FOLDER
             
  
Notes:

     * CATALOG_NAME: Iceberg catalog name.
     * PROJECT_ID: Your Google Cloud project ID. Project IDs are listed in the **Project info** section on the Google Cloud console [Dashboard](https://console.cloud.google.com/home/dashboard). [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) where your cluster is located.
     * LOCATION: A supported [BigQuery location](https://docs.cloud.google.com/bigquery/docs/locations#supported_locations). The default location is "US".
     * BUCKET and WAREHOUSE_FOLDER: Cloud Storage bucket and folder used for the Iceberg warehouse.
  2. Click **Submit**

  3. To monitor job progress and view job output, go to the Managed Service for Apache Spark [**Jobs**](https://console.cloud.google.com/dataproc/jobs) page in the Google Cloud console, then click the `Job ID` to open the **Job details** page.

![](https://docs.cloud.google.com/static/managed-spark/images/iceberg-table-job-details.png)
  4. To view table metadata in BigQuery

     1. In the Google Cloud console, go to the **BigQuery** page.

[Go to BigQuery Studio](https://console.cloud.google.com/bigquery)

     2. View Iceberg table metadata.

![](https://docs.cloud.google.com/static/managed-spark/images/bigquery-table-metadata.png)



### REST

You can use the Managed Service for Apache Spark [jobs.submit](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.jobs/submit) API to submit the Spark SQL job to Managed Service for Apache Spark to create an Iceberg table with metadata in Lakehouse runtime catalog.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID. Project IDs are listed in the **Project info** section on the Google Cloud console [Dashboard](https://console.cloud.google.com/home/dashboard).
  * CLUSTER_NAME: The name of your Managed Service for Apache Spark cluster.
  * REGION: The [Compute Engine region](https://docs.cloud.google.com/compute/docs/regions-zones#available) where your cluster is located.
  * CATALOG_NAME: Iceberg catalog name.
  * BUCKET and WAREHOUSE_FOLDER: Cloud Storage bucket and folder used for the Iceberg warehouse.
LOCATION: A supported [BigQuery location](https://docs.cloud.google.com/bigquery/docs/locations#supported_locations). The default location is "US". 
  * `BIGLAKE_ICEBERG_CATALOG_JAR`: the Cloud Storage URI of the Iceberg custom catalog plugin to use. Depending on your Iceberg version number, select one of the following: 
    * Iceberg 1.9.1: `gs://spark-lib/bigquery/iceberg-bigquery-catalog-1.9.1-1.0.1.jar`
    * Iceberg 1.6.1: `gs://spark-lib/bigquery/iceberg-bigquery-catalog-1.6.1-1.0.2.jar`
  * `jarFileUris`: The listed jars are necessary to create table metadata in BigQuery Metastore.
  * `properties`: [Catalog properties](https://iceberg.apache.org/docs/latest/spark-configuration/).
  * `queryFileUri`: The `iceberg-table.sql` job file you copied to your bucket in Cloud Storage.



HTTP method and URL: 
    
    
    POST https://dataproc.googleapis.com/v1/projects/PROJECT_ID/regions/REGION/jobs:submit

Request JSON body: 
    
    
    {
      "projectId": "PROJECT_ID",
      "job": {
        "placement": {
          "clusterName": "CLUSTER_NAME"
        },
        "statusHistory": [],
        "reference": {
          "jobId": "",
          "projectId": "PROJECT_ID"
        },
        "sparkSqlJob": {
          "properties": {
            "spark.sql.catalog."CATALOG_NAME": "org.apache.iceberg.spark.SparkCatalog",
            "spark.sql.catalog."CATALOG_NAME".catalog-impl": "org.apache.iceberg.gcp.bigquery.BigQueryMetastoreCatalog",
            "spark.sql.catalog."CATALOG_NAME".gcp_project": "PROJECT_ID",
            "spark.sql.catalog."CATALOG_NAME".gcp_location": "LOCATION",
            "spark.sql.catalog."CATALOG_NAME".warehouse": "gs://BUCKET/WAREHOUSE_FOLDER"
          },
          "jarFileUris": [
            "gs://BUCKET/iceberg-spark-runtime-3.5_2.12-1.6.1.jar,BIGLAKE_ICEBERG_CATALOG_JAR"
          ],
          "scriptVariables": {},
          "queryFileUri": "gs://BUCKET/iceberg-table.sql"
        }
      }
    }
    
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://dataproc.googleapis.com/v1/projects/PROJECT_ID/regions/REGION/jobs:submit"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://dataproc.googleapis.com/v1/projects/PROJECT_ID/regions/REGION/jobs:submit" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "reference": {
        "projectId": "PROJECT_ID",
        "jobId": "..."
      },
      "placement": {
        "clusterName": "CLUSTER_NAME",
        "clusterUuid": "..."
      },
      "status": {
        "state": "PENDING",
        "stateStartTime": "..."
      },
      "submittedBy": "USER",
      "sparkSqlJob": {
        "queryFileUri": "gs://BUCKET/iceberg-table.sql",
        "properties": {
          "spark.sql.catalog.USER_catalog": "org.apache.iceberg.spark.SparkCatalog",
          "spark.sql.catalog.USER_catalog.catalog-impl": "org.apache.iceberg.gcp.bigquery.BigQueryMetastoreCatalog",
          "spark.sql.catalog.USER_catalog.gcp_project": "PROJECT_ID",
          "spark.sql.catalog.USER_catalog.gcp_location": "LOCATION",
          "spark.sql.catalog.USER_catalog.warehouse": "gs://BUCKET/WAREHOUSE_FOLDER"
        },
        "jarFileUris": [
          "gs://BUCKET/iceberg-spark-runtime-3.5_2.12-1.6.1.jar",
          "BIGLAKE_ICEBERG_CATALOG_JAR"
        ]
      },
      "driverControlFilesUri": "gs://dataproc-...",
      "driverOutputResourceUri": "gs://dataproc-.../driveroutput",
      "jobUuid": "...",
      "region": "REGION"
    }
    

To monitor job progress and view job output, go to the Managed Service for Apache Spark [**Jobs**](https://console.cloud.google.com/dataproc/jobs) page in the Google Cloud console, then click the `Job ID` to open the **Job details** page.

![](https://docs.cloud.google.com/static/managed-spark/images/iceberg-table-job-details.png)

To view table metadata in BigQuery

  1. In the Google Cloud console, go to the **BigQuery** page.

[Go to BigQuery Studio](https://console.cloud.google.com/bigquery)

  2. View Iceberg table metadata.

![](https://docs.cloud.google.com/static/managed-spark/images/bigquery-table-metadata.png)




### Spark SQL CLI

The following steps show you how to create an Iceberg table with table metadata stored in Lakehouse runtime catalog using the Spark SQL CLI running on the master node of a Managed Service for Apache Spark cluster.

  1. Use [SSH](https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/ssh) to connect to the master node of your Managed Service for Apache Spark cluster.

  2. In the SSH session terminal, use the `vi` or `nano` text editor to copy the following commands into an `iceberg-table.sql` file.
         
         SET CATALOG_NAME = `CATALOG_NAME`;
         SET BUCKET = `BUCKET`;
         SET WAREHOUSE_FOLDER = `WAREHOUSE_FOLDER`;
         USE `${CATALOG_NAME}`;
         CREATE NAMESPACE IF NOT EXISTS `${CATALOG_NAME}`.example_namespace;
         DROP TABLE IF EXISTS `${CATALOG_NAME}`.example_namespace.example_table;
         CREATE TABLE `${CATALOG_NAME}`.example_namespace.example_table (id int, data string) USING ICEBERG LOCATION 'gs://${BUCKET}/${WAREHOUSE_FOLDER}';
         INSERT INTO `${CATALOG_NAME}`.example_namespace.example_table VALUES (1, 'first row');
         ALTER TABLE `${CATALOG_NAME}`.example_namespace.example_table ADD COLUMNS (newDoubleCol double);
         DESCRIBE TABLE `${CATALOG_NAME}`.example_namespace.example_table;
         

Replace the following:

     * CATALOG_NAME: Iceberg catalog name.
     * BUCKET and WAREHOUSE_FOLDER: Cloud Storage bucket and folder used for the Iceberg warehouse.
  3. In the SSH session terminal, run the following `spark-sql` command to create the iceberg table.
         
         spark-sql \
         --packages org.apache.iceberg:iceberg-spark-runtime-3.5_2.12:1.6.1 \
         --jars https://storage-download.googleapis.com/maven-central/maven2/org/apache/iceberg/iceberg-spark-runtime-3.5_2.12/1.6.1/iceberg-spark-runtime-3.5_2.12-1.6.1.jar,BIGLAKE_ICEBERG_CATALOG_JAR \
         --conf spark.sql.catalog.CATALOG_NAME=org.apache.iceberg.spark.SparkCatalog \
         --conf spark.sql.catalog.CATALOG_NAME.catalog-impl=org.apache.iceberg.gcp.bigquery.BigQueryMetastoreCatalog \
         --conf spark.sql.catalog.CATALOG_NAME.gcp_project=PROJECT_ID \
         --conf spark.sql.catalog.CATALOG_NAME.gcp_location=LOCATION \
         --conf spark.sql.catalog.CATALOG_NAME.warehouse=gs://BUCKET/WAREHOUSE_FOLDER \
         -f iceberg-table.sql
         

Replace the following:

     * `BIGLAKE_ICEBERG_CATALOG_JAR`: the Cloud Storage URI of the Iceberg custom catalog plugin to use. Depending on your Iceberg version number, select one of the following: 
       * Iceberg 1.9.1: `gs://spark-lib/bigquery/iceberg-bigquery-catalog-1.9.1-1.0.1.jar`
       * Iceberg 1.6.1: `gs://spark-lib/bigquery/iceberg-bigquery-catalog-1.6.1-1.0.2.jar`
     * PROJECT_ID: Your Google Cloud project ID. Project IDs are listed in the **Project info** section on the Google Cloud console [Dashboard](https://console.cloud.google.com/home/dashboard).
     * LOCATION: A supported [BigQuery location](https://docs.cloud.google.com/bigquery/docs/locations#supported_locations). The default location is "US".
  4. View table metadata in BigQuery

     1. In the Google Cloud console, go to the **BigQuery** page.

[Go to BigQuery Studio](https://console.cloud.google.com/bigquery)

     2. View Iceberg table metadata.

![](https://docs.cloud.google.com/static/managed-spark/images/bigquery-table-metadata.png)



### Zeppelin web interface

The following steps show you how to to create an Iceberg table with table metadata stored in Lakehouse runtime catalog using the Zeppelin web interface running on the master node of a Managed Service for Apache Spark cluster .

**Note:** You must use a Managed Service for Apache Spark cluster that was created with the [Zeppelin optional component enabled](https://docs.cloud.google.com/managed-spark/docs/concepts/components/zeppelin#install_the_component).

  1. In the Google Cloud console, go to the Managed Service for Apache Spark **Clusters** page.

[Go to the Managed Service for Apache Spark Clusters page](https://console.cloud.google.com/dataproc/clusters)

  2. Select your cluster name to open the **Cluster details** page.

  3. Click the **Web Interfaces** tab display a list of **Component Gateway** links to the web interfaces of default and optional components installed on the cluster.

  4. Click the **Zeppelin** link to open the Zeppelin web interface.

![](https://docs.cloud.google.com/static/managed-spark/images/zeppelin-link.png)
  5. In the Zeppelin web interface, click the **anonymous** menu, then click **Interpreter** to open the **Interpreters** page.

![](https://docs.cloud.google.com/static/managed-spark/images/zeppelin-select-interpreter.png)
  6. Add two jars to the Zeppelin Spark interpreter, as follows:

     1. Type "Spark" in `Search interpreters` box to scroll to the **Spark** interpreter section.
     2. Click **edit**.
     3. Paste the following in the **spark.jars** field: 
            
            https://storage-download.googleapis.com/maven-central/maven2/org/apache/iceberg/iceberg-spark-runtime-3.5_2.12/1.6.1/iceberg-spark-runtime-3.5_2.12-1.6.1.jar,BIGLAKE_ICEBERG_CATALOG_JAR
            
            

     4. Add the following note:

        * `BIGLAKE_ICEBERG_CATALOG_JAR`: the Cloud Storage URI of the Iceberg custom catalog plugin to use. Depending on your Iceberg version number, select one of the following:
        * Iceberg 1.9.1: `gs://spark-lib/bigquery/iceberg-bigquery-catalog-1.9.1-1.0.1.jar`
        * Iceberg 1.6.1: `gs://spark-lib/bigquery/iceberg-bigquery-catalog-1.6.1-1.0.2.jar` ![](https://docs.cloud.google.com/static/managed-spark/images/spark-jars.png)
     5. Click **Save** at the bottom of the Spark interpreter section, then click **OK** to update the interpreter and restart the Spark interpreter with the new settings.

  7. From the Zeppelin notebook menu, click **Create new note**.

![](https://docs.cloud.google.com/static/managed-spark/images/create-zeppelin-notebook.png)
  8. In the **Create new note** dialog, input a name for the notebook, and accept the default **spark** interpreter. Click **Create** to open The notebook.

  9. Copy the following PySpark code into your Zeppelin notebook after filling in the variables.
         
         %pyspark  
         
         from pyspark.sql import SparkSession  
         project_id = "PROJECT_ID"
         catalog = "CATALOG_NAME"
         namespace = "NAMESPACE"
         location = "LOCATION"
         warehouse_dir = "gs://BUCKET/WAREHOUSE_DIRECTORY"  
         spark = SparkSession.builder \
         .appName("BigQuery Metastore Iceberg") \
         .config(f"spark.sql.catalog.{catalog}", "org.apache.iceberg.spark.SparkCatalog") \
         .config(f"spark.sql.catalog.{catalog}.catalog-impl", "org.apache.iceberg.gcp.bigquery.BigQueryMetastoreCatalog") \
         .config(f"spark.sql.catalog.{catalog}.gcp_project", f"{project_id}") \
         .config(f"spark.sql.catalog.{catalog}.gcp_location", f"{location}") \
         .config(f"spark.sql.catalog.{catalog}.warehouse", f"{warehouse_dir}") \
         .getOrCreate()  
         
         spark.sql(f"USE `{catalog}`;")
         spark.sql(f"CREATE NAMESPACE IF NOT EXISTS `{namespace}`;")
         spark.sql(f"USE `{namespace}`;")  
         \# Create table and display schema (without LOCATION)
         spark.sql("DROP TABLE IF EXISTS example_iceberg_table")
         spark.sql("CREATE TABLE example_iceberg_table (id int, data string) USING ICEBERG")
         spark.sql("DESCRIBE example_iceberg_table;")  
         \# Insert table data.
         spark.sql("INSERT INTO example_iceberg_table VALUES (1, 'first row');")  
         \# Alter table, then display schema.
         spark.sql("ALTER TABLE example_iceberg_table ADD COLUMNS (newDoubleCol double);")  
         \# Select and display the contents of the table.
         spark.sql("SELECT * FROM example_iceberg_table").show()

Replace the following:

     * PROJECT_ID: Your Google Cloud project ID. Project IDs are listed in the **Project info** section on the Google Cloud console [Dashboard](https://console.cloud.google.com/home/dashboard).
     * CATALOG_NAME and NAMESPACE: The Iceberg catalog name and namespace combine to identify the Iceberg table (`catalog.namespace.table_name`).
     * LOCATION: A supported [BigQuery location](https://docs.cloud.google.com/bigquery/docs/locations#supported_locations). The default location is "US".
     * BUCKET and WAREHOUSE_DIRECTORY: Cloud Storage bucket and folder used as Iceberg warehouse directory.
  10. Click the run icon or press `Shift-Enter` to run the code. When the job completes, the status message shows "Spark Job Finished", and the output displays the table contents:

![](https://docs.cloud.google.com/static/managed-spark/images/zeppelin-job-finished.png)
  11. View table metadata in BigQuery

     1. In the Google Cloud console, go to the **BigQuery** page.

[Go to BigQuery Studio](https://console.cloud.google.com/bigquery)

     2. View Iceberg table metadata.

![](https://docs.cloud.google.com/static/managed-spark/images/bigquery-table-metadata.png)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
