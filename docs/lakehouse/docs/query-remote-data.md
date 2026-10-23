---
url: https://docs.cloud.google.com/lakehouse/docs/query-remote-data/
title: Query remote data \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:36.682967+00:00
---

# Query remote data  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/query-remote-data/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Query remote data Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** For support during the preview, email [biglake-help@google.com](mailto:biglake-help@google.com).

After setting up cross-cloud data access, you can query remote data from multiple sources. This capability of borderless Lakehouse lets you access data using standard SQL in BigQuery, the open-source version of Apache Spark, or Managed Service for Apache Spark. In addition to analytical queries, you can use your federated data for AI-driven insights and governance:

  * [**Conversational Analytics**](https://docs.cloud.google.com/lakehouse/docs/conversational-analytics): Build specialized agents grounded in your exact data sources, including federated tables, to analyze data across clouds from a single conversation.
  * [**Dataplex Catalog**](https://docs.cloud.google.com/dataplex/docs/catalog-overview#supported-sources): Use Knowledge Catalog features for data profiling and insights with federated data sources.



For deeper insights, you can author specialized agents grounded in your data sources, from projects, datasets, and tables to views, graphs, and user-defined functions. Because your data rarely lives in one place, conversational analytics reaches beyond BigQuery Standard tables to Apache Iceberg tables managed by Lakehouse and Lakehouse sources like Databricks Unity, AWS Glue, SAP, and Salesforce. This lets you break down data silos and analyze data across clouds from a single conversation.

This page shows you how to query remote data after you set up cross-cloud data access.

## Before you begin

Before you can query your data, you must complete the following:

  1. Ensure that you have data within your remote catalog.
  2. Set up a cross-cloud connection for [AWS Glue](https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-aws-glue), [Databricks Unity Catalog](https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-databricks), [Snowflake Horizon Catalog](https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-snowflake), [Workday Data Lake](https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-workday), or [SAP Business Data Cloud](https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-sap-bdc).



### Required roles

To get the permissions that you need to query federated data, ask your administrator to grant you the following IAM roles on your project: 

  * Query data in BigQuery: [BigQuery Data Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataViewer) (`roles/bigquery.dataViewer`) 
  * Run BigQuery jobs: [BigQuery Job User ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.jobUser) (`roles/bigquery.jobUser`) 
  * Discover and read table metadata in Lakehouse catalogs: [BigLake Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.viewer) (`roles/biglake.viewer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Query data

After you set up federation, you can query your remote data using standard SQL in BigQuery or Apache Spark in [Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc/docs).

_Lakehouse_ handles the metadata translation and secure data access, which lets you treat remote Apache Iceberg tables as if they were local to your Google Cloud environment.

### Query from BigQuery

To query federated Apache Iceberg tables, use standard BigQuery SQL. The table path follows a 4-part structure: `project.federated_catalog.namespace.table`. Caching, credential vending, and CCI transit routing are automatically handled.
    
    
    SELECT
      user_id,
      action,
      COUNT(*) as total_actions
    FROM `PROJECT_ID.FEDERATED_CATALOG_NAME.NAMESPACE_NAME.TABLE_NAME`
    WHERE event_date >= '2026-04-01'
    GROUP BY 1, 2;

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `FEDERATED_CATALOG_NAME`: the name of the federated catalog.
  * `NAMESPACE_NAME`: the namespace within the catalog.
  * `TABLE_NAME`: the name of the table.
  * `REGION`: the Google Cloud region. For example, `us-east4`.



You can also run the query using the `bq` command-line tool:
    
    
    bq --location="REGION" --project_id="PROJECT_ID" query --use_legacy_sql=false \
      "SELECT * FROM \`PROJECT_ID.FEDERATED_CATALOG_NAME.NAMESPACE_NAME.TABLE_NAME\` LIMIT 10"

### Query from Managed Service for Apache Spark

Submit a [PySpark batch workload](https://docs.cloud.google.com/dataproc-serverless/docs/quickstarts/spark-batch#submit_a_spark_batch_workload) to Managed Service for Apache Spark with [credential vending](https://docs.cloud.google.com/lakehouse/docs/credential-vending) enabled using `X-Iceberg-Access-Delegation=vended-credentials`. Spark will use the short-lived scoped vended credentials to connect to S3 securely, all without needing to manage separate AWS credentials or S3 connectors.

  1. Enable outbound connectivity for Managed Service for Apache Spark.

Managed Service for Apache Spark cannot connect to AWS S3 with its default [network configuration](https://docs.cloud.google.com/dataproc/docs/concepts/network-serverless). You must provision a Cloud Router and Cloud NAT.
         
         gcloud compute routers create lakehouse-router \
           --network=NETWORK_NAME \
           --region=REGION
         
         gcloud compute routers nats create lakehouse-nat \
           --router=lakehouse-router \
           --auto-allocate-nat-external-ips \
           --nat-all-subnet-ip-ranges \
           --region=REGION

Replace the following:

     * `NETWORK_NAME`: the network for the Managed Service for Apache Spark batch workload (for example, `default`).
     * `REGION`: the region for the Managed Service for Apache Spark batch workload.
  2. Create a PySpark application file and run the PySpark job.
         
         from pyspark.sql import SparkSession
         spark = SparkSession.builder.appName("CATALOG_NAME").getOrCreate()
         
         df = spark.table("CATALOG_NAME.NAMESPACE_NAME.TABLE_NAME")
         df.show(10, truncate=False)

Upload this to Cloud Storage at `PYSPARK_FILE`.

**Note:** The properties and parameters required for the Spark job might vary depending on your data source (For example, Databricks or AWS Glue) and underlying storage. For a list of parameters, see Spark Configuration Parameters.
         
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
             spark.sql.catalog.CATALOG_NAME.io-impl=IO_IMPL,\
             spark.sql.catalog.CATALOG_NAME.header.X-Iceberg-Access-Delegation=vended-credentials,\
             spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions"

Replace the following:

     * `NAMESPACE_NAME`: the namespace in the federated catalog.
     * `TABLE_NAME`: the name of the table in the federated catalog.
     * `CATALOG_NAME`: a name for the local Spark catalog (for example, `my_catalog`).
     * `PYSPARK_FILE`: the `gs://` Cloud Storage path to your PySpark application file.
     * `REGION`: the region for the Managed Service for Apache Spark batch workload.
     * `RUNTIME_VERSION`: the Managed Service for Apache Spark runtime version, for example `2.3`.
     * `PROJECT_ID`: the project that is billed for using the Apache Iceberg REST catalog endpoint.
     * `FEDERATED_CATALOG_NAME`: the name of the federated catalog.
     * `IO_IMPL`: the FileIO implementation matching your underlying storage.

### Spark Configuration Parameters

The following table lists common parameters required for all connections:

Parameter | Description  
---|---  
`spark.sql.defaultCatalog` | The default catalog name (for example, `CATALOG_NAME`).  
`spark.sql.catalog.CATALOG_NAME` | The catalog implementation class. Set to `org.apache.iceberg.spark.SparkCatalog`.  
`spark.sql.catalog.CATALOG_NAME.type` | The catalog backend type. Set to `rest` for the Iceberg REST catalog.  
`spark.sql.catalog.CATALOG_NAME.uri` | The URI of the REST catalog endpoint. Set to `https://biglake.googleapis.com/iceberg/v1/restcatalog`.  
`spark.sql.catalog.CATALOG_NAME.warehouse` | The warehouse location path for the federated catalog. Set to `bl://projects/PROJECT_ID/catalogs/FEDERATED_CATALOG_NAME`.  
`spark.sql.catalog.CATALOG_NAME.header.x-goog-user-project` | The Google Cloud project ID used for billing and quota attribution. Set to `PROJECT_ID`.  
`spark.sql.extensions` | The Spark session extensions for Iceberg SQL syntax and features. Set to `org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions`.  
  
The following table lists authentication parameters:

**Note:** Personal Access Token (PAT) authentication (`spark.sql.catalog.CATALOG_NAME.token` and `spark.sql.catalog.CATALOG_NAME.oauth2-server-uri`) and custom authentication type (`spark.sql.catalog.CATALOG_NAME.rest.auth.type`) are mutually exclusive. When both are set, PAT takes priority and the authentication type is assumed to be `BEARER`.Parameter | Description  
---|---  
`spark.sql.catalog.CATALOG_NAME.rest.auth.type` | The custom authentication manager class. Set to `org.apache.iceberg.gcp.auth.GoogleAuthManager` for OAuth flow authentication.  
`spark.sql.catalog.CATALOG_NAME.oauth2-server-uri` | The OAuth2 token server endpoint URI. Set to `https://oauth2.googleapis.com/token` for Personal Access Token (PAT) authentication.  
`spark.sql.catalog.CATALOG_NAME.token` | The Bearer token or Personal Access Token (PAT). Typically set to `$(gcloud auth application-default print-access-token)` for PAT authentication.  
  
The following table lists unique parameters based on your storage provider (`IO_IMPL`):

Storage | `spark.sql.catalog.CATALOG_NAME.io-impl` | Notes  
---|---|---  
**Amazon S3** | `org.apache.iceberg.aws.s3.S3FileIO` | Requires credential vending (`X-Iceberg-Access-Delegation=vended-credentials`) if enabled.  
Additional parameter: `spark.sql.catalog.CATALOG_NAME.s3.region` (for a list of regions, see [Amazon S3 endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/s3.html#s3_region)).  
**Google Cloud Storage** | `org.apache.iceberg.gcp.gcs.GCSFileIO` | Additional parameter: `spark.sql.catalog.CATALOG_NAME.gcs.oauth2.refresh-credentials-endpoint`=`https://oauth2.googleapis.com/token`.  
**Azure Blob Storage** | `org.apache.iceberg.azure.adlsv2.ADLSFileIO` | No additional storage parameters required.  
  
For Snowflake, you may encounter issues when querying `STRING` columns because they are automatically storage-optimized. You can resolve this in one of two ways:

     * **Option 1: Disable vectorization in Spark** : Add the following Spark configuration properties to the `--properties` flag:
     * `spark.sql.iceberg.vectorization.enabled=false`
     * `spark.sql.catalog.CATALOG_NAME.table-override.read.parquet.vectorization.enabled=false`

     * **Option 2: Change serialization policy in Snowflake** : Change the storage serialization policy to `COMPATIBLE` for the table in Snowflake.




### Monitor cache usage and egress cost savings

Lakehouse caching is enabled automatically for all cross-cloud queries. When a query runs, Lakehouse automatically caches data blocks locally within Google Cloud storage. Subsequent queries targeting the same data blocks read directly from the local cache instead of refetching the data from the remote cloud.

To verify cache hit rates and measure your egress cost savings, inspect the job details in the BigQuery console or retrieve the query job statistics (`JobStatistics2`) using the BigQuery API or `bq` CLI:
    
    
    bq show --format=prettyjson --j JOB_ID

In the JSON output under `statistics.query.objectStorageStats` (or `object_storage_stats` in the proto API), the job statistics return a list with an entry for each cloud provider accessed during execution. Each entry contains the following fields:

  * **`cloudProvider`** (`cloud_provider`): The remote cloud provider hosting the object storage (for example, `AWS` or `AZURE`).
  * **`cacheBytesRead`** (`cache_bytes_read`): The total bytes read from the local Google Cloud cache, avoiding a remote object storage read.
  * **`objectStorageBytesRead`** (`object_storage_bytes_read`): The total bytes read directly from the remote cloud provider's object storage.



For more information about caching concepts and data residency considerations, see [Intelligent caching](https://docs.cloud.google.com/lakehouse/docs/about-cross-cloud-data-access#intelligent-caching).

## What's next

  * [Supported regions and capabilities](https://docs.cloud.google.com/lakehouse/docs/regions-capabilities-cross-cloud-connections).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
