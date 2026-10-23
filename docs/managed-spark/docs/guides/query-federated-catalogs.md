---
url: https://docs.cloud.google.com/managed-spark/docs/guides/query-federated-catalogs/
title: Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:45.406248+00:00
---

# Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/guides/query-federated-catalogs/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Query federated catalogs with Spark and Lakehouse runtime catalog

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

After you set up cross-cloud data access in Lakehouse runtime catalog, you can query remote Iceberg tables from Managed Service for Apache Spark without migrating files or managing separate cloud storage credentials.

Lakehouse runtime catalog handles metadata synchronization and secure data access through [credential vending](https://docs.cloud.google.com/lakehouse/docs/credential-vending). When Spark queries a federated table, Lakehouse runtime catalog translates the catalog metadata and issues short-lived, scoped credentials for Spark to read data from Amazon S3 or Cloud Storage, treating the tables as if they were local to your Google Cloud environment.

## Supported federated catalog types

Managed Service for Apache Spark supports querying the following federated catalog types through the Lakehouse runtime catalog Iceberg REST Catalog endpoint:

Federated catalog type | Supported storage backends | Setup guide in Lakehouse runtime catalog  
---|---|---  
**AWS Glue Data Catalog** | Amazon S3 (`s3://`—default AWS account catalog or Amazon S3 table bucket) | [Connect to AWS Glue](https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-aws-glue)  
**Databricks Unity Catalog** | Amazon S3 (`s3://`) or Cloud Storage (`gs://`) external locations | [Connect to Databricks Unity Catalog](https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-databricks)  
**Snowflake Horizon Catalog** | Amazon S3 (`s3://`) or Cloud Storage (`gs://`) | [Connect to Snowflake Horizon Catalog](https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-snowflake)  
  
To learn about the catalog readiness requirements and underlying Spark parameter definitions for each storage provider, see [Query remote data in Lakehouse runtime catalog](https://docs.cloud.google.com/lakehouse/docs/query-remote-data) and [Spark Configuration Parameters](https://docs.cloud.google.com/lakehouse/docs/query-remote-data#spark-parameters).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. Verify that you have the permissions required to complete this guide. 

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. Enable the Dataproc, BigLake, and BigQuery APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataproc.googleapis.com,biglake.googleapis.com,bigquery.googleapis.com)

  6. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  7. Verify that you have the permissions required to complete this guide. 

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. Enable the Dataproc, BigLake, and BigQuery APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataproc.googleapis.com,biglake.googleapis.com,bigquery.googleapis.com)

  10. Ensure that you have Iceberg tables in your remote catalog.
  11. Set up a cross-cloud connection and federated catalog in Lakehouse runtime catalog for your remote catalog provider: 
     * [AWS Glue Data Catalog](https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-aws-glue)
     * [Databricks Unity Catalog](https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-databricks)
     * [Snowflake Horizon Catalog](https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-snowflake)



#### Required Identity and Access Management (IAM) roles

Certain IAM roles are required to run the examples on this page. Depending on organization policies, these roles might have already been granted. To check role grants, see [Do you need to grant roles?](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/iam#do_you_need_to_grant_roles). For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

The roles that you need depend on how your workload runs. Managed Service for Apache Spark clusters and Managed Service for Apache Spark serverless runtimes 2.3 and earlier run workloads as a service account. Managed Service for Apache Spark serverless runtimes 3.0 and later run workloads with your end-user credentials (EUC) by default, so you grant data access roles to your user account instead of a service account. If you specify a custom service account for a 3.0 or later runtime, the workload runs with service account credentials. For more information, see [Serverless deployments roles](https://docs.cloud.google.com/managed-spark/docs/concepts/iam-serverless#s8s-role-requirements).

##### User roles

To get the permissions that you need to create a Managed Service for Apache Spark cluster, submit a batch workload, or create an interactive session, ask your administrator to grant you the following IAM roles: 

  * Use a cluster or a serverless runtime 2.3 or earlier: 
    * [Dataproc Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.editor) (`roles/dataproc.editor`) on the project
    * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the Compute Engine default service account or a custom service account
  * Use a serverless runtime 3.0 or later: [Dataproc Serverless Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serverlessEditor) (`roles/dataproc.serverlessEditor`) on the project 
  * Read federated tables with end-user credentials on a serverless runtime 3.0 or later: [BigLake Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.viewer) (`roles/biglake.viewer`) on the project that contains the federated catalog 
  * Use service account credentials on a serverless runtime 3.0 or later: [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the custom service account 



##### Service account roles

Grant the following roles to the service account that runs your workload. Managed Service for Apache Spark serverless runtimes 3.0 and later need these roles only if the workload runs with service account credentials.

To ensure that the Compute Engine default service account or a custom service account has the necessary permissions to run Managed Service for Apache Spark jobs and read federated tables, ask your administrator to grant the following IAM roles to the Compute Engine default service account or a custom service account: 

**Important:** You must grant these roles to the Compute Engine default service account or a custom service account, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 

  * Run Managed Service for Apache Spark jobs on a cluster or a serverless runtime 2.3 or earlier: [Dataproc Worker ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`) on the project 
  * Run Managed Service for Apache Spark jobs on a serverless runtime 3.0 or later: 
    * [Dataproc Serverless Node ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serverlessNode) (`roles/dataproc.serverlessNode`) on the project
    * [Dataproc Resource Manager Node Service Agent ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocrm#dataprocrm.nodeServiceAgent) (`roles/dataprocrm.nodeServiceAgent`) on the project
  * Discover and read federated table metadata at runtime: [BigLake Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.viewer) (`roles/biglake.viewer`) on the project that contains the federated catalog 



To ensure that the Managed Service for Apache Spark Service Agent (`service-PROJECT_NUMBER@dataproc-accounts.iam.gserviceaccount.com`) has the necessary permissions to resolve the `dataproc.lakehouse.catalog.` simplified configuration property when you create a cluster, submit a batch workload, or create an interactive session, ask your administrator to grant the [BigLake Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.viewer) (`roles/biglake.viewer`) IAM role to the Managed Service for Apache Spark Service Agent (`service-PROJECT_NUMBER@dataproc-accounts.iam.gserviceaccount.com`) on the project that contains the federated catalog. **Important:** You must grant this role to the Managed Service for Apache Spark Service Agent (`service-PROJECT_NUMBER@dataproc-accounts.iam.gserviceaccount.com`), _not_ to your user account. Failure to grant the role to the correct principal might result in permission errors. 

#### Configure outbound network connectivity for Amazon S3

When you query federated catalogs backed by Amazon S3, Managed Service for Apache Spark serverless batch workloads and interactive sessions, and internal-IP Managed Service for Apache Spark clusters can't connect to Amazon S3 endpoints with their default [network configuration](https://docs.cloud.google.com/managed-spark/docs/concepts/network-serverless). Provision a Cloud Router and Cloud NAT on your workload VPC network to allow outbound traffic to Amazon S3:
    
    
    gcloud compute routers create lakehouse-router \
        --network=NETWORK_NAME \
        --region=REGION
    
    gcloud compute routers nats create lakehouse-nat \
        --router=lakehouse-router \
        --auto-allocate-nat-external-ips \
        --nat-all-subnet-ip-ranges \
        --region=REGION

Replace the following:

  * `NETWORK_NAME`: the VPC network for your Managed Service for Apache Spark cluster, batch workload, or interactive session, for example, `default`.
  * `REGION`: the Google Cloud region for your Managed Service for Apache Spark cluster, batch workload, or interactive session.



## Configure Managed Service for Apache Spark and query federated tables

You can configure a Managed Service for Apache Spark cluster, serverless batch workload, or interactive session to connect to your federated catalog in Lakehouse runtime catalog. These Managed Service for Apache Spark resources support the `dataproc.lakehouse.catalog.CATALOG_NAME` simplified configuration property (recommended), which reads the federated catalog definition from Lakehouse runtime catalog and generates the required Iceberg REST Catalog Spark properties, including the storage `io-impl` and credential-vending headers (the cluster form of the property adds the `dataproc:` prefix).

Both simplified configuration and manual configuration use Google authorization for Iceberg (`GoogleAuthManager`), which requires one of the following cluster image or serverless runtime versions:

  * Managed Service for Apache Spark clusters: 2.2 image versions 2.2.65 and later, or 2.3 image versions 2.3.11 and later.
  * Managed Service for Apache Spark serverless batch workloads and interactive sessions: 2.2 runtimes 2.2.60 and later, 2.3 runtimes 2.3.10 and later, or 3.0 runtimes.



For serverless batch workloads and interactive sessions, the required roles depend on the runtime version. Runtimes 3.0 and later use end-user credentials by default. For details, see Required IAM roles and [Serverless deployments roles](https://docs.cloud.google.com/managed-spark/docs/concepts/iam-serverless#s8s-role-requirements).

###  Cluster 

Create a Managed Service for Apache Spark cluster with the Iceberg optional component using simplified configuration properties (recommended), or by manually specifying catalog properties.

#### Simplified configuration using properties (recommended)

Create the cluster with the federated catalog property:
    
    
    gcloud dataproc clusters create CLUSTER_NAME \
      --project=PROJECT_ID \
      --region=REGION \
      --image-version=IMAGE_VERSION \
      --optional-components=ICEBERG,JUPYTER \
      --enable-component-gateway \
      --properties="dataproc:dataproc.lakehouse.catalog.CATALOG_NAME=projects/PROJECT_ID/catalogs/FEDERATED_CATALOG_NAME,spark:spark.sql.defaultCatalog=CATALOG_NAME"

Replace the following:

  * `CLUSTER_NAME`: a name for your cluster.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `REGION`: the Google Cloud region for the cluster, for example, `us-central1`.
  * `IMAGE_VERSION`: the Managed Service for Apache Spark image version—for example, `2.3-debian12`. For supported versions, see the requirements earlier in this section.
  * `CATALOG_NAME`: a name for the local Spark catalog, for example, `federated_catalog`. It can be the same as `FEDERATED_CATALOG_NAME`.
  * `FEDERATED_CATALOG_NAME`: the ID of the federated catalog that you created in Before you begin.

**Note:** You can pass multiple comma-separated catalogs to the `--properties` flag. Each cluster catalog property requires the `dataproc:` prefix.

#### Querying the Snowflake Horizon Catalog

If you are querying a Snowflake Horizon Catalog, note the following:

  * **Snowflake storage:** Simplified configuration supports Snowflake tables stored in Amazon S3. For Snowflake tables stored in Cloud Storage, use manual configuration with `io-impl` set to `org.apache.iceberg.gcp.gcs.GCSFileIO`.

  * **Snowflake`STRING` columns:** If you encounter errors querying Snowflake `STRING` columns where the table's storage serialization policy in Snowflake isn't `COMPATIBLE`, you can change the storage serialization policy to `COMPATIBLE` in Snowflake or disable Parquet vectorization in Spark by adding the following properties to the `--properties` flag:
        
        spark:spark.sql.iceberg.vectorization.enabled=false,spark:spark.sql.catalog.CATALOG_NAME.table-override.read.parquet.vectorization.enabled=false
            




In your Jupyter notebook or PySpark application, create the `SparkSession` without specifying catalog configs:
    
    
    from pyspark.sql import SparkSession
    
    spark = SparkSession.builder.appName("APP_NAME").getOrCreate()

Replace `APP_NAME` with the name of your Spark application.

#### Manual configuration

If you don't use the simplified configuration property, create the cluster as previously described in this section, without passing the `dataproc:dataproc.lakehouse.catalog.` property to the `--properties` flag, and then configure your `SparkSession` manually. For a list of storage provider parameter values, see [Spark Configuration Parameters](https://docs.cloud.google.com/lakehouse/docs/query-remote-data#spark-parameters).
    
    
    from pyspark.sql import SparkSession
    
    catalog_name = "CATALOG_NAME"
    
    spark = SparkSession.builder.appName("APP_NAME") \
    .config('spark.sql.defaultCatalog', catalog_name) \
    .config(f'spark.sql.catalog.{catalog_name}', 'org.apache.iceberg.spark.SparkCatalog') \
    .config(f'spark.sql.catalog.{catalog_name}.type', 'rest') \
    .config(f'spark.sql.catalog.{catalog_name}.uri', 'https://biglake.googleapis.com/iceberg/v1/restcatalog') \
    .config(f'spark.sql.catalog.{catalog_name}.warehouse', 'bl://projects/PROJECT_ID/catalogs/FEDERATED_CATALOG_NAME') \
    .config(f'spark.sql.catalog.{catalog_name}.header.x-goog-user-project', 'PROJECT_ID') \
    .config(f'spark.sql.catalog.{catalog_name}.rest.auth.type', 'org.apache.iceberg.gcp.auth.GoogleAuthManager') \
    .config(f'spark.sql.catalog.{catalog_name}.header.X-Iceberg-Access-Delegation', 'vended-credentials') \
    .config(f'spark.sql.catalog.{catalog_name}.io-impl', 'IO_IMPL') \
    .config(f'spark.sql.catalog.{catalog_name}.s3.client-factory-impl', 'org.apache.iceberg.aws.s3.DefaultS3FileIOAwsClientFactory') \
    .config('spark.sql.extensions', 'org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions') \
    .getOrCreate()

Replace `IO_IMPL` with the `FileIO` implementation for the storage that contains your tables:

  * Tables in Amazon S3: `org.apache.iceberg.aws.s3.S3FileIO`
  * Tables in Cloud Storage: `org.apache.iceberg.gcp.gcs.GCSFileIO`



The `s3.client-factory-impl` property applies only to tables in Amazon S3. Omit this line for Cloud Storage tables.

###  Serverless 

Submit a PySpark batch workload to Managed Service for Apache Spark serverless using simplified configuration properties (recommended), or by manually specifying catalog properties.

#### Simplified configuration using properties (recommended)

Pass the federated catalog property without the `dataproc:` prefix when you submit the batch workload:
    
    
    gcloud dataproc batches submit pyspark PYSPARK_FILE \
      --project=PROJECT_ID \
      --region=REGION \
      --version=RUNTIME_VERSION \
      --properties="dataproc.lakehouse.catalog.CATALOG_NAME=projects/PROJECT_ID/catalogs/FEDERATED_CATALOG_NAME,spark.sql.defaultCatalog=CATALOG_NAME"

Replace the following:

  * `PYSPARK_FILE`: the `gs://` Cloud Storage path to your PySpark application file.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `REGION`: the region for the batch workload.
  * `RUNTIME_VERSION`: the Managed Service for Apache Spark serverless runtime version, for example, `3.0`. For supported versions, see the requirements earlier in this section. The required IAM roles depend on the runtime version.
  * `CATALOG_NAME`: a name for the local Spark catalog, for example, `federated_catalog`. It can be the same as `FEDERATED_CATALOG_NAME`.
  * `FEDERATED_CATALOG_NAME`: the ID of the federated catalog that you created in Before you begin.

**Note:** You can pass multiple comma-separated catalogs to the `--properties` flag.

#### Querying the Snowflake Horizon Catalog

If you are querying a Snowflake Horizon Catalog, note the following:

  * **Snowflake storage:** Simplified configuration supports Snowflake tables stored in Amazon S3. For Snowflake tables stored in Cloud Storage, use manual configuration with `io-impl` set to `org.apache.iceberg.gcp.gcs.GCSFileIO`.

  * **Snowflake`STRING` columns:** If you encounter errors querying Snowflake `STRING` columns where the table's storage serialization policy in Snowflake isn't `COMPATIBLE`, you can change the storage serialization policy to `COMPATIBLE` in Snowflake or disable Parquet vectorization in Spark by adding the following properties to the `--properties` flag:
        
        spark.sql.iceberg.vectorization.enabled=false,spark.sql.catalog.CATALOG_NAME.table-override.read.parquet.vectorization.enabled=false
            




In the PySpark application file, create the `SparkSession` without specifying catalog configs:
    
    
    from pyspark.sql import SparkSession
    
    spark = SparkSession.builder.appName("APP_NAME").getOrCreate()

#### Manual configuration

If you don't use the simplified configuration property, specify the catalog properties with the `--properties` flag of the `gcloud dataproc batches submit` command. For a list of storage provider parameter values, see [Spark Configuration Parameters](https://docs.cloud.google.com/lakehouse/docs/query-remote-data#spark-parameters).
    
    
    gcloud dataproc batches submit pyspark PYSPARK_FILE \
      --project=PROJECT_ID \
      --region=REGION \
      --version=RUNTIME_VERSION \
      --properties="\
    spark.sql.defaultCatalog=CATALOG_NAME,\
    spark.sql.catalog.CATALOG_NAME=org.apache.iceberg.spark.SparkCatalog,\
    spark.sql.catalog.CATALOG_NAME.type=rest,\
    spark.sql.catalog.CATALOG_NAME.uri=https://biglake.googleapis.com/iceberg/v1/restcatalog,\
    spark.sql.catalog.CATALOG_NAME.warehouse=bl://projects/PROJECT_ID/catalogs/FEDERATED_CATALOG_NAME,\
    spark.sql.catalog.CATALOG_NAME.header.x-goog-user-project=PROJECT_ID,\
    spark.sql.catalog.CATALOG_NAME.rest.auth.type=org.apache.iceberg.gcp.auth.GoogleAuthManager,\
    spark.sql.catalog.CATALOG_NAME.header.X-Iceberg-Access-Delegation=vended-credentials,\
    spark.sql.catalog.CATALOG_NAME.io-impl=IO_IMPL,\
    spark.sql.catalog.CATALOG_NAME.s3.client-factory-impl=org.apache.iceberg.aws.s3.DefaultS3FileIOAwsClientFactory,\
    spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions"

Replace `IO_IMPL` with the `FileIO` implementation for the storage that contains your tables:

  * Tables in Amazon S3: `org.apache.iceberg.aws.s3.S3FileIO`
  * Tables in Cloud Storage: `org.apache.iceberg.gcp.gcs.GCSFileIO`



The `s3.client-factory-impl` property applies only to tables in Amazon S3. Omit this property for Cloud Storage tables.

###  Serverless 

Create a Managed Service for Apache Spark serverless interactive session in a notebook through the [`DataprocSparkSession`](https://docs.cloud.google.com/managed-spark/docs/guides/spark-connect-client) API using simplified configuration properties (recommended) or by manually specifying catalog properties.

#### Simplified configuration using properties (recommended)

In a notebook that has the `dataproc-spark-connect` package installed, such as a BigQuery Studio notebook or a Vertex AI Workbench notebook, pass the federated catalog property without the `dataproc:` prefix when you create the session:
    
    
    from google.cloud.dataproc_spark_connect import DataprocSparkSession
    from google.cloud.dataproc_v1 import [Session](https://docs.cloud.google.com/python/docs/reference/dataproc/latest/google.cloud.dataproc_v1.types.Session.html)
    
    catalog_name = "CATALOG_NAME"
    
    session_config = Session()
    session_config.runtime_config.version = 'RUNTIME_VERSION'
    
    spark = DataprocSparkSession.builder.appName("APP_NAME") \
    .dataprocSessionConfig(session_config) \
    .config(f'dataproc.lakehouse.catalog.{catalog_name}', 'projects/PROJECT_ID/catalogs/FEDERATED_CATALOG_NAME') \
    .config('spark.sql.defaultCatalog', catalog_name) \
    .getOrCreate()

Replace the following:

  * `CATALOG_NAME`: a name for the local Spark catalog, for example, `federated_catalog`. It can be the same as `FEDERATED_CATALOG_NAME`.
  * `RUNTIME_VERSION`: the Managed Service for Apache Spark serverless runtime version, for example, `3.0`. For supported versions, see the requirements earlier in this section. The required IAM roles depend on the runtime version.
  * `APP_NAME`: the name of your Spark application.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `FEDERATED_CATALOG_NAME`: the ID of the federated catalog that you created in Before you begin.



You can also set these properties in a [session template](https://docs.cloud.google.com/managed-spark/docs/guides/create-serverless-sessions-templates).

#### Querying the Snowflake Horizon Catalog

If you are querying a Snowflake Horizon Catalog, note the following:

  * **Snowflake storage:** Simplified configuration supports Snowflake tables stored in Amazon S3. For Snowflake tables stored in Cloud Storage, use manual configuration with `io-impl` set to `org.apache.iceberg.gcp.gcs.GCSFileIO`.

  * **Snowflake`STRING` columns:** If you encounter errors querying Snowflake `STRING` columns where the table's storage serialization policy in Snowflake isn't `COMPATIBLE`, you can change the storage serialization policy to `COMPATIBLE` in Snowflake or disable Parquet vectorization in Spark by adding the following `.config()` calls to the session builder:
        
        .config('spark.sql.iceberg.vectorization.enabled', 'false') \
        .config(f'spark.sql.catalog.{catalog_name}.table-override.read.parquet.vectorization.enabled', 'false')
            




#### Manual configuration

If you don't use the simplified configuration property, specify the catalog properties when you create the session. For a list of storage provider parameter values, see [Spark Configuration Parameters](https://docs.cloud.google.com/lakehouse/docs/query-remote-data#spark-parameters).
    
    
    from google.cloud.dataproc_spark_connect import DataprocSparkSession
    from google.cloud.dataproc_v1 import [Session](https://docs.cloud.google.com/python/docs/reference/dataproc/latest/google.cloud.dataproc_v1.types.Session.html)
    
    catalog_name = "CATALOG_NAME"
    
    session_config = Session()
    session_config.runtime_config.version = 'RUNTIME_VERSION'
    
    spark = DataprocSparkSession.builder.appName("APP_NAME") \
    .dataprocSessionConfig(session_config) \
    .config('spark.sql.defaultCatalog', catalog_name) \
    .config(f'spark.sql.catalog.{catalog_name}', 'org.apache.iceberg.spark.SparkCatalog') \
    .config(f'spark.sql.catalog.{catalog_name}.type', 'rest') \
    .config(f'spark.sql.catalog.{catalog_name}.uri', 'https://biglake.googleapis.com/iceberg/v1/restcatalog') \
    .config(f'spark.sql.catalog.{catalog_name}.warehouse', 'bl://projects/PROJECT_ID/catalogs/FEDERATED_CATALOG_NAME') \
    .config(f'spark.sql.catalog.{catalog_name}.header.x-goog-user-project', 'PROJECT_ID') \
    .config(f'spark.sql.catalog.{catalog_name}.rest.auth.type', 'org.apache.iceberg.gcp.auth.GoogleAuthManager') \
    .config(f'spark.sql.catalog.{catalog_name}.header.X-Iceberg-Access-Delegation', 'vended-credentials') \
    .config(f'spark.sql.catalog.{catalog_name}.io-impl', 'IO_IMPL') \
    .config(f'spark.sql.catalog.{catalog_name}.s3.client-factory-impl', 'org.apache.iceberg.aws.s3.DefaultS3FileIOAwsClientFactory') \
    .config('spark.sql.extensions', 'org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions') \
    .getOrCreate()

Replace `RUNTIME_VERSION` as described in the simplified configuration example earlier in this tab.

Replace `IO_IMPL` with the `FileIO` implementation for the storage that contains your tables:

  * Tables in Amazon S3: `org.apache.iceberg.aws.s3.S3FileIO`
  * Tables in Cloud Storage: `org.apache.iceberg.gcp.gcs.GCSFileIO`



The `s3.client-factory-impl` property applies only to tables in Amazon S3. Omit this line for Cloud Storage tables.

## Query federated tables

After you configure your Spark session, you can query tables in your federated catalog using PySpark or Spark SQL.

**Note:** The `dataproc.lakehouse.catalog.` property registers the catalog with Spark, but it doesn't set it as the _default_ catalog. The previous examples set the serverless `spark.sql.defaultCatalog` or the `spark:spark.sql.defaultCatalog` cluster property, which lets you use unqualified table names. If you omit these properties, you must qualify table names with the catalog name, as shown in the following examples.

  1. Read a federated table using the PySpark DataFrame API:
         
         df = spark.table("CATALOG_NAME.NAMESPACE_NAME.TABLE_NAME")
         df.show(10, truncate=False)

Replace the following:

     * `CATALOG_NAME`: the local Spark catalog name. If you set `spark.sql.defaultCatalog` to `CATALOG_NAME`, you can omit this prefix.
     * `NAMESPACE_NAME`: the namespace (database or schema) in the federated catalog.
     * `TABLE_NAME`: the table name in the federated catalog.
  2. Query the federated table using Spark SQL:
         
         spark.sql("""
             SELECT *
             FROM CATALOG_NAME.NAMESPACE_NAME.TABLE_NAME
             LIMIT 10
         """).show()




### Join or materialize data across federated and local catalogs

Federated catalogs are read-only. To join remote cross-cloud data with local tables or materialize federated query results into Cloud Storage, attach your federated catalog and a read-write catalog in Lakehouse runtime catalog using comma-separated `dataproc.lakehouse.catalog.` properties:

###  Cluster 

Managed Service for Apache Spark cluster example:
    
    
    --properties="dataproc:dataproc.lakehouse.catalog.FEDERATED_SPARK_CATALOG=projects/PROJECT_ID/catalogs/FEDERATED_CATALOG_NAME,dataproc:dataproc.lakehouse.catalog.LOCAL_SPARK_CATALOG=projects/PROJECT_ID/catalogs/LOCAL_CATALOG_ID,spark:spark.sql.defaultCatalog=LOCAL_SPARK_CATALOG"

###  Serverless 

Managed Service for Apache Spark serverless batch workload example:
    
    
    --properties="dataproc.lakehouse.catalog.FEDERATED_SPARK_CATALOG=projects/PROJECT_ID/catalogs/FEDERATED_CATALOG_NAME,dataproc.lakehouse.catalog.LOCAL_SPARK_CATALOG=projects/PROJECT_ID/catalogs/LOCAL_CATALOG_ID,spark.sql.defaultCatalog=LOCAL_SPARK_CATALOG"

###  Serverless 

Managed Service for Apache Spark serverless interactive session example:
    
    
    from google.cloud.dataproc_spark_connect import DataprocSparkSession
    from google.cloud.dataproc_v1 import [Session](https://docs.cloud.google.com/python/docs/reference/dataproc/latest/google.cloud.dataproc_v1.types.Session.html)
    
    session_config = Session()
    session_config.runtime_config.version = 'RUNTIME_VERSION'
    
    spark = DataprocSparkSession.builder.appName("APP_NAME") \
      .dataprocSessionConfig(session_config) \
      .config('dataproc.lakehouse.catalog.FEDERATED_SPARK_CATALOG', 'projects/PROJECT_ID/catalogs/FEDERATED_CATALOG_NAME') \
      .config('dataproc.lakehouse.catalog.LOCAL_SPARK_CATALOG', 'projects/PROJECT_ID/catalogs/LOCAL_CATALOG_ID') \
      .config('spark.sql.defaultCatalog', 'LOCAL_SPARK_CATALOG') \
      .getOrCreate()

Replace `RUNTIME_VERSION` as described in the interactive session example earlier on this page.

After setting these properties, you can query the federated catalog and write the results into a table in your local Lakehouse runtime catalog.

The principal that runs your workload is the service account for clusters, serverless runtimes 2.3 and earlier, and serverless runtimes 3.0 and later with service account credentials. For serverless runtimes 3.0 and later with end-user credentials (the default), the principal is your user account.

To ensure that the principal that runs your workload has the necessary permissions to write table data into your local catalog, ask your administrator to grant the following IAM roles to the principal that runs your workload: 

  * Write table data in credential vending mode: [BigLake Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.editor) (`roles/biglake.editor`) on the project that contains the local catalog 
  * Write table data in non-credential vending mode: 
    * [BigLake Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.editor) (`roles/biglake.editor`) on the project that contains the local catalog
    * [Storage Object User ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`) on all Cloud Storage buckets associated with the local catalog



The following example creates a table in your local catalog from a federated table:
    
    
    spark.sql("""
        CREATE TABLE IF NOT EXISTS LOCAL_SPARK_CATALOG.LOCAL_NAMESPACE.materialized_table
        USING iceberg
        AS SELECT *
        FROM FEDERATED_SPARK_CATALOG.REMOTE_NAMESPACE.REMOTE_TABLE
    """)

## What's next

  * [Create a lakehouse with Spark and Lakehouse runtime catalog](https://docs.cloud.google.com/managed-spark/docs/guides/create-lakehouse).
  * Learn more about [querying remote data in Lakehouse runtime catalog](https://docs.cloud.google.com/lakehouse/docs/query-remote-data).
  * Read [About cross-cloud data access](https://docs.cloud.google.com/lakehouse/docs/about-cross-cloud-data-access).
  * Learn about [credential vending](https://docs.cloud.google.com/lakehouse/docs/credential-vending).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
