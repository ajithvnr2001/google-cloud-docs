---
url: https://docs.cloud.google.com/lakehouse/docs/set-up-lakehouse-iceberg-rest-catalog/
title: Set up the Apache Iceberg REST catalog endpoint \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:42:34.861712+00:00
---

# Set up the Apache Iceberg REST catalog endpoint  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/set-up-lakehouse-iceberg-rest-catalog/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Set up the Apache Iceberg REST catalog endpoint Stay organized with collections  Save and categorize content based on your preferences. 

For new catalogs, we recommend using the _Apache Iceberg REST catalog endpoint_ in the _Lakehouse runtime catalog_. This endpoint provides a fully managed, standardized interface based on the open-source _Apache Iceberg REST Catalog API_.

This endpoint acts as a single source of truth, enabling seamless interoperability across your query engines. It allows engines like Apache Spark to discover, read, and manage your Google Cloud Apache Iceberg tables managed by Lakehouse.

This approach is a good choice if you use compatible OSS or third party engines to access data in Cloud Storage and need interoperability with other engines, including BigQuery. It supports features like credential vending for fine-grained access control and [cross-region replication and disaster recovery](https://docs.cloud.google.com/lakehouse/docs/about-managed-disaster-recovery).

In contrast, the [_Custom Apache Iceberg catalog for BigQuery_ endpoint](https://docs.cloud.google.com/lakehouse/docs/about-custom-iceberg-catalog-endpoint) is an earlier integration. While existing workflows can continue to use it, the REST catalog offers a more standardized and feature-rich experience.

## Before you begin

  1. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  2. Enable the BigLake API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=biglake.googleapis.com)

  3. Familiarize yourself with [Lakehouse runtime catalog](https://docs.cloud.google.com/lakehouse/docs/about-lakehouse-catalogs) and the [Iceberg REST catalog endpoint overview](https://docs.cloud.google.com/lakehouse/docs/understand-catalog-types) before continuing.
  4. If you have existing version 1 (V1) Apache Iceberg tables, you must upgrade them before using them with the Apache Iceberg REST catalog endpoint. For more information, see [Upgrade Iceberg V1 tables to V2](https://docs.cloud.google.com/lakehouse/docs/update-tables).



### Required roles

To get the permissions that you need to use the Apache Iceberg REST catalog endpoint in Lakehouse runtime catalog, ask your administrator to grant you the following IAM roles: 

  * Perform administrative tasks, such as managing catalog user access, storage access, and the catalog's credential vending mode: 
    * [BigLake Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`) on the project
    * [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) on all associated Cloud Storage buckets.
  * Create (register) tables in a Lakehouse runtime catalog: [BigLake Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`) on the project. 
  * Read table data in credential vending mode: [BigLake Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.viewer) (`roles/biglake.viewer`) on the project. If you use query engines such as Managed Service for Apache Spark, Managed Service for Apache Spark, or Dataflow to read table data, grant this role to the service account that you use to run jobs in that engine. 
  * Write table data in credential vending mode: [BigLake Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.editor) (`roles/biglake.editor`) on the project. If you use query engines such as Managed Service for Apache Spark, Managed Service for Apache Spark, or Dataflow to write table data, grant this role to the service account that you use to run jobs in that engine. 
  * Use the auto-provisioned Lakehouse runtime catalog service account in credential vending mode: [Storage Object User ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`) on all associated Cloud Storage buckets. After creating the catalog, explicitly grant the Storage Object User role (`roles/storage.objectUser`) on all associated storage buckets to your catalog's auto-provisioned Lakehouse runtime catalog service account. 
  * Read catalog resources and table data in non-credential vending mode: 
    * [BigLake Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.viewer) (`roles/biglake.viewer`) on the project
    * [Storage Object Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) (`roles/storage.objectViewer`) on all associated Cloud Storage buckets.
  * Manage catalog resources and write table data in non-credential vending mode: 
    * [BigLake Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.editor) (`roles/biglake.editor`) on the project
    * [Storage Object User ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`) on all associated Cloud Storage buckets.



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Limitations

The Apache Iceberg REST catalog endpoint is subject to the following limitations:

**General limitations**

  * Apache Iceberg V2 tables (GA) and V3 tables (Preview) are supported. Iceberg V1 tables aren't supported. Before you use existing V1 tables with the Apache Iceberg REST catalog endpoint, you must upgrade them to a supported version.
  * When using credential vending mode, if the query engine allows you to set the `io-impl` property for a catalog connection, you must set it to `org.apache.iceberg.gcp.gcs.GCSFileIO`.



**Table limitations**

  * You can't create or modify tables in the Apache Iceberg REST catalog endpoint using BigQuery data definition language (DDL) or data manipulation language (DML) statements. You can modify these tables using the BigQuery API (with the bq command-line tool or client libraries), but doing so risks making changes that are incompatible with the external engine.
  * Tables managed through the Apache Iceberg REST catalog endpoint don't support fine-grained access control (FGAC), such as row-level and column-level security.
  * Setting the Iceberg table properties `write.data.path` or `write.metadata.path` to values other than their defaults is prohibited.
  * Table paths must be nested within the parent namespace path (for example, `gs://{namespace_path}/.../{table_name}`). To prevent conflicts and improve security, a random string suffix is automatically appended to the resulting location (for example, `gs://{namespace_path}/{table_name}/{random_suffix}`).



**Data limitations**

  * Only Parquet files are supported. For more details on how BigQuery handles Parquet files, see [Loading Parquet data from Cloud Storage](https://docs.cloud.google.com/bigquery/docs/loading-data-cloud-storage-parquet).
  * The Iceberg `metadata.json` file size is limited to 1MB. To request an increase to this limit, contact your Google account team.



**Query limitations**

  * Apache Iceberg metadata tables (such as `.snapshots` or `.files`) can't be queried in BigQuery using five-part name identifiers; you can query these tables using Spark.



## Considerations

Consider the following configurations when creating a catalog.

#### Bucket type

You can choose to create a multiple-bucket catalog or a single-bucket catalog.

  * **Multiple-bucket catalog (recommended):** This configuration lets your catalog associate multiple buckets and lets you name your catalog independently of any bucket name.
  * **Single-bucket:** This configuration restricts your catalog to a single bucket and locks the catalog name to the bucket name. It is discouraged for new projects.



For more information about the differences between these configurations, see [catalog and storage locations](https://docs.cloud.google.com/lakehouse/docs/about-iceberg-rest-catalog-endpoint#warehouse-storage-locations).

#### Credential mode (scope)

You can create a catalog that uses either end-user credentials or [credential vending mode](https://docs.cloud.google.com/lakehouse/docs/understand-catalog-types#storage-single-bucket).

  * **End-user credentials:** The catalog passes the identity of the end user accessing it to Cloud Storage for authorization checks.

  * **Credential vending mode:** A storage access delegation mechanism that lets Lakehouse runtime catalog administrators control permissions directly on Lakehouse runtime catalog resources, eliminating the need for catalog users to have direct access to Cloud Storage buckets. It lets Google Cloud's _Lakehouse_ administrators give users permissions on specific data files.

The auto-provisioned Lakehouse runtime catalog service account requires the explicit Storage Object User role (`roles/storage.objectUser`) on all associated Cloud Storage buckets. By default, it has no access whatsoever. Without this role, vended credentials won't have sufficient scope to perform storage writes. If you use tools like `gcloud` or Terraform, you must grant this role manually.

Creation of the auto-provisioned catalog service account is [eventually consistent](https://wikipedia.org/wiki/Eventual_consistency). This means that it takes time for the service account to propagate through the system. If you try to grant roles to the service account immediately after creation, the request might fail. To learn how long it takes, on average, for access changes to propagate, see [Access change propagation](https://docs.cloud.google.com/iam/docs/access-change-propagation).




#### Location

Familiarize yourself with the [location requirements](https://docs.cloud.google.com/lakehouse/docs/understand-catalog-types#bucket_and_catalog_regions) before creating a catalog.

  * When you create a namespace, it automatically uses the same region as your catalog.

  * If your catalog uses a multi-region bucket and you want to use it with the BigQuery multi-regions (`US` or `EU`), you must delete and recreate the catalog to specify the primary location.

  * To route catalog requests directly to a specific region for data residency requirements, you can configure your tools and query engines to use [regional endpoints](https://docs.cloud.google.com/lakehouse/docs/regional-endpoints) (`https://biglake.LOCATION.rep.googleapis.com/iceberg/v1/restcatalog`) instead of the global endpoint (`https://biglake.googleapis.com/iceberg/v1/restcatalog`).




## Set up the Iceberg REST catalog endpoint

Before you set up your catalog, we recommend reading the [Apache Iceberg REST catalog endpoint overview](https://docs.cloud.google.com/lakehouse/docs/understand-catalog-types) to understand its resource hierarchy, catalog types, and naming structure.

The following are the general steps to follow when using the Apache Iceberg REST catalog endpoint in the Lakehouse runtime catalog:

  1. Choose your catalog type—a [multiple-bucket](https://docs.cloud.google.com/lakehouse/docs/understand-catalog-types#storage-multiple-buckets) catalog (recommended) or a [single-bucket](https://docs.cloud.google.com/lakehouse/docs/understand-catalog-types#storage-single-bucket) catalog.
  2. Create a catalog that points to your warehouse location.
  3. Configure your client application to use the Apache Iceberg REST catalog endpoint.
  4. Create a namespace or schema to organize your tables.
  5. Create and query tables using your configured client.



### Create a catalog

Follow these steps to create a catalog based on your preferred credential mode and bucket type.

###  Console 

**Create a multiple-bucket catalog (recommended)**

This configuration lets your catalog to associate multiple buckets and lets you name your catalog independently of any bucket name.

  1. Open the **Lakehouse** page in the Google Cloud console.

[Go to Lakehouse](https://console.cloud.google.com/biglake)

  2. Click **Create catalog**.

  3. For **Catalog type** , select **Iceberg Rest Catalog**.

  4. For **Lakehouse catalog bucket options** , select **Multiple bucket catalog**.

  5. For **Default Catalog Cloud Storage path** , enter or browse for the Cloud Storage path to use with your catalog.

  6. For **Catalog ID** , enter a custom name for your catalog.

  7. For **Primary location** , select a location. The location must be near the regions of the main bucket.

  8. Click **Continue**.

  9. In the **Data paths** step, add additional Cloud Storage paths if needed.

  10. Click **Continue**.

  11. For **Authentication method** , select **End-user credentials** or **Credential vending mode**.

  12. Click **Create**.

Your catalog is created and the **Catalog details** page opens.

  13. If you selected **Credential vending mode** , perform the following additional steps:

     1. Under **Authentication method** , click **Set bucket permissions**.
     2. In the dialog, click **Confirm**.



#### Create a single-bucket catalog

**Caution:** Using the single-bucket configuration is highly discouraged for new projects. This configuration restricts your catalog to a single bucket and locks the catalog name to the bucket name. 

  1. For **Catalog type** , select **Iceberg Rest Catalog**.
  2. For **Lakehouse runtime catalog bucket options** , select **Single bucket catalog**.
  3. For **Default Catalog Cloud Storage path** , enter or browse for the Cloud Storage path to use with your catalog. (For a single-bucket catalog, you can only have one catalog per bucket, and the catalog name matches the bucket name).
  4. Click **Continue**.
  5. For **Authentication method** , select **End-user credentials** or **Credential vending mode**.
  6. Click **Create**.
  7. If you selected **Credential vending mode** , perform the following additional steps: 
     1. Under **Authentication method** , click **Set bucket permissions**.
     2. In the dialog, click **Confirm**.



###  gcloud 

**Create a multiple-bucket catalog (recommended)**

This configuration lets your catalog to associate multiple buckets and lets you name your catalog independently of any bucket name.

To create a multiple-bucket catalog (recommended), run the [`gcloud biglake iceberg catalogs create`](https://docs.cloud.google.com/sdk/gcloud/reference/biglake/iceberg/catalogs/create) command.
    
    
    gcloud biglake iceberg catalogs create \
        CATALOG_NAME \
        --project PROJECT_ID \
        --catalog-type biglake \
        --default-location DEFAULT_LOCATION \
        --credential-mode CREDENTIAL_MODE \
        [--restricted-locations RESTRICTED_LOCATIONS] \
        [--primary-location LOCATION]

Replace the following:

  * `CATALOG_NAME`: a name for your catalog. For multiple-bucket catalogs (recommended), this is your custom catalog name.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `DEFAULT_LOCATION`: Specify the default storage location for the catalog. You can specify a bucket (`gs://my-bucket`) or a subpath (`gs://my-bucket/path`). All namespaces and tables in the catalog must reside under the specified path. For example, if you specify `gs://my-bucket/path`, you cannot create namespaces or tables under `gs://my-bucket/another/path`.
  * `CREDENTIAL_MODE`: the authentication method. Use `end-user` for _End-user credentials_ or `vended-credentials` for _Credential vending mode_.

**Note** : If you use _Credential vending mode_ , you must explicitly grant the _Storage Object User_ role (`roles/storage.objectUser`) on all associated storage buckets to your catalog's auto-provisioned Lakehouse runtime catalog service account.

  * `RESTRICTED_LOCATIONS`: (Optional) Comma-separated list of additional allowed storage locations, in the format `gs://my-bucket-1/...,gs://my-bucket-2/...`. If you specify a path (such as `gs://my-bucket/path`), any namespaces or tables within that bucket must be under that path. All configured cloud storage locations across the default location and restricted locations must be in the same geographic region group or jurisdiction (such as the United States, Europe, Canada, or Asia). For example, you cannot mix a bucket in the US with a bucket in Europe. For a list of supported locations, see [Lakehouse locations](https://docs.cloud.google.com/lakehouse/docs/locations).

**Warning:** Avoid configuring overlapping paths with other catalogs to prevent unauthorized credential exposure. or more information, see [Storage across Multiple buckets](https://docs.cloud.google.com/lakehouse/docs/understand-catalog-types#storage-multiple-buckets).

  * `LOCATION`: (Optional) The primary region for the catalog to ensure interoperability with BigQuery. For Cloud Storage buckets in the US region (for example, `US` or `us-central1`) or the EU region (for example, `EU` or `europe-west4`), specify `US` or `EU` respectively to ensure the catalog is accessible and available for querying from the corresponding BigQuery multi-regions. For more information, see [Bucket and catalog regions](https://docs.cloud.google.com/lakehouse/docs/understand-catalog-types#bucket_and_catalog_regions).




#### Create a single-bucket catalog

**Caution:** Using the single-bucket configuration is highly discouraged for new projects. This configuration restricts your catalog to a single bucket and locks the catalog name to the bucket name. 

To create a single-bucket catalog, run the following command:
    
    
    gcloud biglake iceberg catalogs create \
        CATALOG_NAME \
        --project PROJECT_ID \
        --catalog-type gcs-bucket \
        --credential-mode CREDENTIAL_MODE

Replace the following:

  * `CATALOG_NAME`: a name for your catalog. For single-bucket catalogs, this matches the Cloud Storage bucket ID used with the REST catalog.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `CREDENTIAL_MODE`: the authentication method. Use `end-user` for _End-user credentials_ or `vended-credentials` for _Credential vending mode_.



### Configure client application

After you create a catalog, configure your client application to use it. These examples show you how to configure with or without credential vending.

###  Cluster 

Create a Managed Service for Apache Spark on Compute Engine cluster using simplified configuration properties (recommended), or by specifying properties manually.

#### Simplified configuration using properties (recommended)

Create a cluster with the catalog property:
    
    
    gcloud dataproc clusters create CLUSTER_NAME \
      --enable-component-gateway \
      --project=PROJECT_ID \
      --region=REGION \
      --optional-components=ICEBERG \
      --image-version=DATAPROC_VERSION \
      --properties="dataproc:dataproc.lakehouse.catalog.CATALOG_NAME=projects/PROJECT_ID/catalogs/CATALOG_ID"

Replace the following:

  * `CLUSTER_NAME`: a name for your cluster.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `REGION`: the Managed Service for Apache Spark cluster region.
  * `DATAPROC_VERSION`: the Managed Service for Apache Spark image version—for example, `2.3`.
  * `CATALOG_NAME`: a name for the local Spark catalog (for example, `my_catalog`). It can be the same as `CATALOG_ID`.
  * `CATALOG_ID`: the ID of the catalog you created.

**Note:** You can configure multiple catalogs separated by commas within the `--properties` flag. For example: `--properties="dataproc:dataproc.lakehouse.catalog.CATALOG_NAME_1=projects/PROJECT_ID_1/catalogs/CATALOG_ID_1,dataproc:dataproc.lakehouse.catalog.CATALOG_NAME_2=projects/PROJECT_ID_2/catalogs/CATALOG_ID_2"`

In the PySpark application file, create the `SparkSession` without specifying catalog configs:
    
    
    from pyspark.sql import SparkSession
    
    spark = SparkSession.builder.appName("APP_NAME").getOrCreate()

#### Manual configuration

If you do not use the simplified configuration property, create a cluster as described above but without the `--properties` flag. Then, configure your `SparkSession` manually:
    
    
    import pyspark
    from pyspark.context import SparkContext
    from pyspark.sql import SparkSession
    
    catalog_name = "CATALOG_NAME"
    spark = SparkSession.builder.appName("APP_NAME") \
      .config('spark.sql.defaultCatalog', 'CATALOG_NAME') \
      .config(f'spark.sql.catalog.{catalog_name}', 'org.apache.iceberg.spark.SparkCatalog') \
      .config(f'spark.sql.catalog.{catalog_name}.type', 'rest') \
      .config(f'spark.sql.catalog.{catalog_name}.uri', 'https://biglake.googleapis.com/iceberg/REST_API_VERSION/restcatalog') \
      .config(f'spark.sql.catalog.{catalog_name}.warehouse', 'WAREHOUSE_PATH') \
      .config(f'spark.sql.catalog.{catalog_name}.header.x-goog-user-project', 'PROJECT_ID') \
      .config(f'spark.sql.catalog.{catalog_name}.rest.auth.type', 'org.apache.iceberg.gcp.auth.GoogleAuthManager') \
      .config(f'spark.sql.catalog.{catalog_name}.io-impl', 'org.apache.iceberg.gcp.gcs.GCSFileIO') \
      .config('spark.sql.extensions', 'org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions') \
      .getOrCreate()

Replace the following:

  * `CATALOG_NAME`: a name for the local Spark catalog (for example, `my_catalog`).
  * `APP_NAME`: a name for your Spark session.
  * `REST_API_VERSION`: set to `v1` for the stable version of the API.
  * `WAREHOUSE_PATH`: The path to your warehouse. For multiple-bucket catalogs, use `bl://projects/PROJECT_ID/catalogs/CATALOG_ID`. For single-bucket catalogs, use `gs://CLOUD_STORAGE_BUCKET_NAME`.
  * `PROJECT_ID`: the project that is billed for using the Apache Iceberg REST catalog endpoint, which might be different from the project that owns the Cloud Storage bucket. For details about project configuration when using a REST API, see [System parameters](https://docs.cloud.google.com/apis/docs/system-parameters).



### Configure with credential vending

To use credential vending, you must use a catalog in credential vending mode and add the `X-Iceberg-Access-Delegation` header to Iceberg REST catalog requests with a value of `vended-credentials` by adding the following line to the `SparkSession` builder: 
    
    
    .config(f'spark.sql.catalog.{catalog_name}.header.X-Iceberg-Access-Delegation','vended-credentials')

#### Example with credential vending

The following example configures the query engine with credential vending:
    
    
    import pyspark
    from pyspark.context import SparkContext
    from pyspark.sql import SparkSession
    
    catalog_name = "CATALOG_NAME"
    spark = SparkSession.builder.appName("APP_NAME") \
      .config('spark.sql.defaultCatalog', 'CATALOG_NAME') \
      .config(f'spark.sql.catalog.{catalog_name}', 'org.apache.iceberg.spark.SparkCatalog') \
      .config(f'spark.sql.catalog.{catalog_name}.type', 'rest') \
      .config(f'spark.sql.catalog.{catalog_name}.uri', 'https://biglake.googleapis.com/iceberg/REST_API_VERSION/restcatalog') \
      .config(f'spark.sql.catalog.{catalog_name}.warehouse', 'WAREHOUSE_PATH') \
      .config(f'spark.sql.catalog.{catalog_name}.header.x-goog-user-project', 'PROJECT_ID') \
      .config(f'spark.sql.catalog.{catalog_name}.rest.auth.type', 'org.apache.iceberg.gcp.auth.GoogleAuthManager') \
      .config(f'spark.sql.catalog.{catalog_name}.io-impl', 'org.apache.iceberg.gcp.gcs.GCSFileIO') \
      **. config(f'spark.sql.catalog.{catalog_name}.header.X-Iceberg-Access-Delegation','vended-credentials')** \
      .config('spark.sql.extensions', 'org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions') \
      .getOrCreate()

For more information, see the [Headers in the `RESTCatalog`](https://py.iceberg.apache.org/configuration/#headers-in-rest-catalog) section of the Apache Iceberg documentation.

Managed Service for Apache Spark clusters support Google authorization flows for Apache Iceberg in the following releases:

  * Managed Service for Apache Spark on Compute Engine 2.2 image versions 2.2.65 and later.
  * Managed Service for Apache Spark on Compute Engine 2.3 image versions 2.3.11 and later.



###  Serverless 

Submit a [PySpark batch workload](https://docs.cloud.google.com/dataproc-serverless/docs/quickstarts/spark-batch#submit_a_spark_batch_workload) to Managed Service for Apache Spark using simplified configuration properties (recommended), or by specifying properties manually.

#### Simplified configuration using properties (recommended)

Submit a batch job with the catalog property:
    
    
    gcloud dataproc batches submit pyspark PYSPARK_FILE \
        --project=PROJECT_ID \
        --region=REGION \
        --version=RUNTIME_VERSION \
        --properties="dataproc.lakehouse.catalog.CATALOG_NAME=projects/PROJECT_ID/catalogs/CATALOG_ID"

Replace the following:

  * `PYSPARK_FILE`: the `gs://` Cloud Storage path to your PySpark application file.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `REGION`: the region for the Managed Service for Apache Spark batch workload.
  * `RUNTIME_VERSION`: the Managed Service for Apache Spark runtime version, for example `2.3`.
  * `CATALOG_NAME`: a name for the local Spark catalog (for example, `my_catalog`). It can be the same as `CATALOG_ID`.
  * `CATALOG_ID`: the ID of the catalog you created.

**Note:** You can configure multiple catalogs separated by commas within the `--properties` flag. For example: `--properties="dataproc.lakehouse.catalog.CATALOG_NAME_1=projects/PROJECT_ID_1/catalogs/CATALOG_ID_1,dataproc.lakehouse.catalog.CATALOG_NAME_2=projects/PROJECT_ID_2/catalogs/CATALOG_ID_2"`

In the PySpark application file, create the `SparkSession` without specifying catalog configs:
    
    
    from pyspark.sql import SparkSession
    
    spark = SparkSession.builder.appName("APP_NAME").getOrCreate()

#### Manual configuration

If you do not use the simplified configuration property, you must manually specify catalog configs:
    
    
    gcloud dataproc batches submit pyspark PYSPARK_FILE \
        --project=PROJECT_ID \
        --region=REGION \
        --version=RUNTIME_VERSION \
        --properties="\
        spark.sql.defaultCatalog=CATALOG_NAME,\
        spark.sql.catalog.CATALOG_NAME=org.apache.iceberg.spark.SparkCatalog,\
        spark.sql.catalog.CATALOG_NAME.type=rest,\
        spark.sql.catalog.CATALOG_NAME.uri=https://biglake.googleapis.com/iceberg/REST_API_VERSION/restcatalog,\
        spark.sql.catalog.CATALOG_NAME.warehouse=WAREHOUSE_PATH,\
        spark.sql.catalog.CATALOG_NAME.header.x-goog-user-project=PROJECT_ID,\
        spark.sql.catalog.CATALOG_NAME.rest.auth.type=org.apache.iceberg.gcp.auth.GoogleAuthManager,\
        spark.sql.catalog.CATALOG_NAME.io-impl=org.apache.iceberg.gcp.gcs.GCSFileIO,\
        spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions"

Replace the following:

  * `PYSPARK_FILE`: the `gs://` Cloud Storage path to your PySpark application file.
  * `REGION`: the region for the Managed Service for Apache Spark batch workload.
  * `RUNTIME_VERSION`: the Managed Service for Apache Spark runtime version, for example `2.3`.
  * `CATALOG_NAME`: a name for the local Spark catalog (for example, `my_catalog`).
  * `REST_API_VERSION`: set to `v1` for the stable version of the API.
  * `WAREHOUSE_PATH`: The path to your warehouse. For multiple-bucket catalogs, use `bl://projects/PROJECT_ID/catalogs/CATALOG_ID`. For single-bucket catalogs, use `gs://CLOUD_STORAGE_BUCKET_NAME`.
  * `PROJECT_ID`: the project that is billed for using the Apache Iceberg REST catalog endpoint, which might be different from the project that owns the Cloud Storage bucket. For details about project configuration when using a REST API, see [System parameters](https://docs.cloud.google.com/apis/docs/system-parameters).



### Configure with credential vending

To use credential vending, you must use a catalog in credential vending mode and add the `X-Iceberg-Access-Delegation` header to the Apache Iceberg REST catalog endpoint requests with a value of `vended-credentials` by adding the following line to the Managed Service for Apache Spark configurations: 
    
    
    .config(f'spark.sql.catalog.{catalog_name}.header.X-Iceberg-Access-Delegation','vended-credentials')

#### Example with credential vending

The following example configures the query engine with credential vending:
    
    
    gcloud dataproc batches submit pyspark PYSPARK_FILE \
        --project=PROJECT_ID \
        --region=REGION \
        --version=RUNTIME_VERSION \
        --properties="\
        spark.sql.defaultCatalog=CATALOG_NAME,\
        spark.sql.catalog.CATALOG_NAME=org.apache.iceberg.spark.SparkCatalog,\
        spark.sql.catalog.CATALOG_NAME.type=rest,\
        spark.sql.catalog.CATALOG_NAME.uri=https://biglake.googleapis.com/iceberg/REST_API_VERSION/restcatalog,\
        spark.sql.catalog.CATALOG_NAME.warehouse=WAREHOUSE_PATH,\
        spark.sql.catalog.CATALOG_NAME.header.x-goog-user-project=PROJECT_ID,\
        spark.sql.catalog.CATALOG_NAME.rest.auth.type=org.apache.iceberg.gcp.auth.GoogleAuthManager,\
        spark.sql.catalog.CATALOG_NAME.io-impl=org.apache.iceberg.gcp.gcs.GCSFileIO,\
        **spark.sql.catalog. CATALOG_NAME.header.X-Iceberg-Access-Delegation=vended-credentials,\**"
        spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions

For more information, see the [Headers in the `RESTCatalog`](https://py.iceberg.apache.org/configuration/#headers-in-rest-catalog) section of the Apache Iceberg documentation.

Managed Service for Apache Spark supports Google authorization flows for Apache Iceberg in the following runtime versions:

  * Managed Service for Apache Spark 2.2 runtimes 2.2.60 and later
  * Managed Service for Apache Spark 2.3 runtimes 2.3.10 and later



###  Trino 

To use Trino with the Apache Iceberg REST catalog endpoint, create a Managed Service for Apache Spark cluster with the Trino component and configure catalog properties using the `gcloud dataproc clusters create --properties` flag. The following example creates a Trino catalog named `CATALOG_NAME`:
    
    
    gcloud dataproc clusters create CLUSTER_NAME \
        --enable-component-gateway \
        --region=REGION \
        --image-version=DATAPROC_VERSION \
        --network=NETWORK_ID \
        --optional-components=TRINO \
        --properties="\
        trino-catalog:CATALOG_NAME.connector.name=iceberg,\
        trino-catalog:CATALOG_NAME.iceberg.catalog.type=rest,\
        trino-catalog:CATALOG_NAME.iceberg.rest-catalog.uri=https://biglake.googleapis.com/iceberg/REST_API_VERSION/restcatalog,\
        trino-catalog:CATALOG_NAME.iceberg.rest-catalog.warehouse=WAREHOUSE_PATH,\
        trino-catalog:CATALOG_NAME.iceberg.rest-catalog.biglake.project-id=PROJECT_ID,\
        trino-catalog:CATALOG_NAME.iceberg.rest-catalog.rest.auth.type=org.apache.iceberg.gcp.auth.GoogleAuthManager"

Replace the following:

  * `CLUSTER_NAME`: a name for your cluster.
  * `REGION`: the Managed Service for Apache Spark cluster region.
  * `DATAPROC_VERSION`: Managed Service for Apache Spark image version, for example `2.2`.
  * `NETWORK_ID`: cluster network ID. For more information, see [Managed Service for Apache Spark cluster network configuration](https://docs.cloud.google.com/dataproc/docs/concepts/configuring-clusters/network).
  * `CATALOG_NAME`: the name of your Trino catalog using the Apache Iceberg REST catalog endpoint.
  * `REST_API_VERSION`: set to `v1` for the stable version of the API.
  * `WAREHOUSE_PATH`: The path to your warehouse. For BigLake catalogs, use `bl://projects/PROJECT_ID/catalogs/CATALOG_ID`. For Cloud Storage bucket catalogs, use `gs://CLOUD_STORAGE_BUCKET_NAME`.
  * `PROJECT_ID`: your Google Cloud project ID to use for Lakehouse runtime catalog.



After cluster creation, connect to the main VM instance, and use the Trino CLI:
    
    
    trino --catalog=CATALOG_NAME

Managed Service for Apache Spark Trino supports Google authorization flows for Apache Iceberg in the following releases:

  * Managed Service for Apache Spark on Compute Engine 2.2 runtime versions 2.2.65 and later
  * Managed Service for Apache Spark on Compute Engine 2.3 runtime versions 2.3.11 and later
  * Managed Service for Apache Spark on Compute Engine 3.0 is not supported.



### Configure with credential vending

Credential vending is only supported on Trino version 481 and later.

###  Apache Iceberg 1.10 or later 

Open source Apache Iceberg 1.10 and later releases have built-in support for Google authorization flows in `GoogleAuthManager`. The following is an example of how to configure Spark to use the Apache Iceberg REST catalog endpoint.
    
    
    import pyspark
    from pyspark.context import SparkContext
    from pyspark.sql import SparkSession
    
    catalog_name = "CATALOG_NAME"
    spark = SparkSession.builder.appName("APP_NAME") \
      .config(f'spark.sql.catalog.{catalog_name}', 'org.apache.iceberg.spark.SparkCatalog') \
      .config(f'spark.sql.catalog.{catalog_name}.type', 'rest') \
      .config(f'spark.sql.catalog.{catalog_name}.uri', 'https://biglake.googleapis.com/iceberg/REST_API_VERSION/restcatalog') \
      .config(f'spark.sql.catalog.{catalog_name}.warehouse', 'WAREHOUSE_PATH') \
      .config(f'spark.sql.catalog.{catalog_name}.header.x-goog-user-project', 'PROJECT_ID') \
      .config(f'spark.sql.catalog.{catalog_name}.rest.auth.type', 'org.apache.iceberg.gcp.auth.GoogleAuthManager') \
      .config(f'spark.sql.catalog.{catalog_name}.io-impl', 'org.apache.iceberg.gcp.gcs.GCSFileIO') \
      .config('spark.sql.extensions', 'org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions') \
      .config('spark.sql.defaultCatalog', 'CATALOG_NAME') \
      .getOrCreate()

Replace the following:

  * `CATALOG_NAME`: a name for the local Spark catalog (for example, `my_catalog`).
  * `APP_NAME`: a name for your Spark session.
  * `REST_API_VERSION`: set to `v1` for the stable version of the API.
  * `WAREHOUSE_PATH`: The path to your warehouse. For BigLake catalogs, use `bl://projects/PROJECT_ID/catalogs/CATALOG_ID`. For Cloud Storage bucket catalogs, use `gs://CLOUD_STORAGE_BUCKET_NAME`.
  * `PROJECT_ID`: the project that is billed for using the Apache Iceberg REST catalog endpoint, which might be different from the project that owns the Cloud Storage bucket. For details about project configuration when using a REST API, see [System parameters](https://docs.cloud.google.com/apis/docs/system-parameters).



### Configure with credential vending

The preceding example doesn't use credential vending. To use credential vending, you must use a catalog in credential vending mode and add the `X-Iceberg-Access-Delegation` header to the Apache Iceberg REST catalog endpoint requests with a value of `vended-credentials` by adding the following line to the `SparkSession` builder: 
    
    
    .config(f'spark.sql.catalog.{catalog_name}.header.X-Iceberg-Access-Delegation','vended-credentials')

#### Example with credential vending

The following example configures the query engine with credential vending:
    
    
    import pyspark
    from pyspark.context import SparkContext
    from pyspark.sql import SparkSession
    
    catalog_name = "CATALOG_NAME"
    spark = SparkSession.builder.appName("APP_NAME") \
      .config(f'spark.sql.catalog.{catalog_name}', 'org.apache.iceberg.spark.SparkCatalog') \
      .config(f'spark.sql.catalog.{catalog_name}.type', 'rest') \
      .config(f'spark.sql.catalog.{catalog_name}.uri', 'https://biglake.googleapis.com/iceberg/REST_API_VERSION/restcatalog') \
      .config(f'spark.sql.catalog.{catalog_name}.warehouse', 'WAREHOUSE_PATH') \
      .config(f'spark.sql.catalog.{catalog_name}.header.x-goog-user-project', 'PROJECT_ID') \
      .config(f'spark.sql.catalog.{catalog_name}.rest.auth.type', 'org.apache.iceberg.gcp.auth.GoogleAuthManager') \
      .config(f'spark.sql.catalog.{catalog_name}.io-impl', 'org.apache.iceberg.gcp.gcs.GCSFileIO') \
      **. config(f'spark.sql.catalog.{catalog_name}.header.X-Iceberg-Access-Delegation','vended-credentials')** \
      .config('spark.sql.extensions', 'org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions') \
      .config('spark.sql.defaultCatalog', 'CATALOG_NAME') \
      .getOrCreate()

For more information, see the [Headers in the `RESTCatalog`](https://py.iceberg.apache.org/configuration/#headers-in-rest-catalog) section of the Apache Iceberg documentation.

###  Prior Apache Iceberg releases 

For open source Apache Iceberg releases prior to 1.10, you can configure standard OAuth authentication by configuring a session with the following:
    
    
    import pyspark
    from pyspark.context import SparkContext
    from pyspark.sql import SparkSession
    
    catalog_name = "CATALOG_NAME"
    spark = SparkSession.builder.appName("APP_NAME") \
      .config('spark.jars.packages', 'org.apache.iceberg:iceberg-spark-runtime-3.5_2.12:1.9.1,org.apache.iceberg:iceberg-gcp-bundle:1.9.1') \
      .config(f'spark.sql.catalog.{catalog_name}', 'org.apache.iceberg.spark.SparkCatalog') \
      .config(f'spark.sql.catalog.{catalog_name}.type', 'rest') \
      .config(f'spark.sql.catalog.{catalog_name}.uri', 'https://biglake.googleapis.com/iceberg/REST_API_VERSION/restcatalog') \
      .config(f'spark.sql.catalog.{catalog_name}.warehouse', 'WAREHOUSE_PATH') \
      .config(f'spark.sql.catalog.{catalog_name}.header.x-goog-user-project', 'PROJECT_ID') \
      .config(f"spark.sql.catalog.{catalog_name}.token", "TOKEN") \
      .config(f"spark.sql.catalog.{catalog_name}.oauth2-server-uri", "https://oauth2.googleapis.com/token") \
      .config(f'spark.sql.catalog.{catalog_name}.io-impl', 'org.apache.iceberg.gcp.gcs.GCSFileIO') \
      .config('spark.sql.extensions', 'org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions') \
      .config('spark.sql.defaultCatalog', 'CATALOG_NAME') \
      .getOrCreate()

Replace the following:

  * `CATALOG_NAME`: a name for the local Spark catalog (for example, `my_catalog`).
  * `APP_NAME`: a name for your Spark session.
  * `REST_API_VERSION`: set to `v1` for the stable version of the API.
  * `WAREHOUSE_PATH`: The path to your warehouse. For BigLake catalogs, use `bl://projects/PROJECT_ID/catalogs/CATALOG_ID`. For Cloud Storage bucket catalogs, use `gs://CLOUD_STORAGE_BUCKET_NAME`.
  * `PROJECT_ID`: the project that is billed for using the Apache Iceberg REST catalog endpoint, which might be different from the project that owns the Cloud Storage bucket. For details about project configuration when using a REST API, see [System parameters](https://docs.cloud.google.com/apis/docs/system-parameters).
  * `TOKEN`: your authentication token, which is valid for one hour—for example, a token generated using `gcloud auth application-default print-access-token`.



### Configure with credential vending

The preceding example doesn't use credential vending. To use credential vending, you must use a catalog in credential vending mode and add the `X-Iceberg-Access-Delegation` header to the Apache Iceberg REST catalog endpoint requests with a value of `vended-credentials` by adding the following line to the `SparkSession` builder: 
    
    
    .config(f'spark.sql.catalog.{catalog_name}.header.X-Iceberg-Access-Delegation','vended-credentials')

#### Example with credential vending

The following example configures the query engine with credential vending:
    
    
    import pyspark
    from pyspark.context import SparkContext
    from pyspark.sql import SparkSession
    
    catalog_name = "CATALOG_NAME"
    spark = SparkSession.builder.appName("APP_NAME") \
      .config(f'spark.sql.catalog.{catalog_name}', 'org.apache.iceberg.spark.SparkCatalog') \
      .config(f'spark.sql.catalog.{catalog_name}.type', 'rest') \
      .config(f'spark.sql.catalog.{catalog_name}.uri', 'https://biglake.googleapis.com/iceberg/REST_API_VERSION/restcatalog') \
      .config(f'spark.sql.catalog.{catalog_name}.warehouse', 'WAREHOUSE_PATH') \
      .config(f'spark.sql.catalog.{catalog_name}.header.x-goog-user-project', 'PROJECT_ID') \
      .config(f"spark.sql.catalog.{catalog_name}.token", "TOKEN") \
      .config(f"spark.sql.catalog.{catalog_name}.oauth2-server-uri", "https://oauth2.googleapis.com/token") \
      .config(f'spark.sql.catalog.{catalog_name}.io-impl', 'org.apache.iceberg.gcp.gcs.GCSFileIO') \
      **. config(f'spark.sql.catalog.{catalog_name}.header.X-Iceberg-Access-Delegation','vended-credentials')** \
      .config('spark.sql.extensions', 'org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions') \
      .config('spark.sql.defaultCatalog', 'CATALOG_NAME') \
      .getOrCreate()

For more information, see the [Headers in the `RESTCatalog`](https://py.iceberg.apache.org/configuration/#headers-in-rest-catalog) section of the Apache Iceberg documentation.

### Create a namespace or schema

After you configure your client, create a namespace or schema to organize your tables. The syntax for creating a namespace or schema varies depending on your query engine. The following examples show how to create them using Spark and Trino.

**Caution:** If you're using credential vending, don't create namespaces or schemas within other namespaces or schemas, because doing so can grant users access to unintended resources.

###  Console 

  1. In the Google Cloud console, go to **Lakehouse**.

[Go to Lakehouse](https://console.cloud.google.com/biglake)

  2. Select an existing catalog or create one if you do not have one.

  3. In the menu bar, click **\+ Create namespace**.

  4. For **Namespace name** , enter a unique name for your namespace.

  5. For **Location** , specify the path to associate with your namespace:

     * **Multiple-bucket** (recommended): You can set any custom location as long as it is under a location allowed by the catalog (`default_location` or `restricted_locations`). If you do not specify a location, the namespace is created under the catalog's default location (for example, `gs://{path-to-default-location}/{namespace_name}`).
     * **Single-bucket **: The namespace location is automatically inherited from the catalog's single bucket.
  6. Click **Create**.




###  Spark 

#### Cloud Storage warehouse
    
    
    spark.sql("CREATE NAMESPACE IF NOT EXISTS NAMESPACE_NAME;")
    spark.sql("USE NAMESPACE_NAME;")

Replace `NAMESPACE_NAME` with a name for your namespace.

###  Trino 

#### Cloud Storage warehouse
    
    
    CREATE SCHEMA IF NOT EXISTS  CATALOG_NAME.SCHEMA_NAME;
    USE CATALOG_NAME.SCHEMA_NAME;

Replace the following:

  * `CATALOG_NAME`: the name of your Trino catalog using the Apache Iceberg REST catalog endpoint.
  * `SCHEMA_NAME`: a name for your schema.



## Upgrade a catalog

If you have an existing single-bucket catalog, you can upgrade it to a multiple-bucket catalog type (recommended). Upgrading lets you associate multiple buckets and configure restricted locations while retaining the original catalog name.

To upgrade your catalog, see [Update a catalog](https://docs.cloud.google.com/lakehouse/docs/update-catalog).

## What's next

  * Learn how to [manage catalogs in the Google Cloud console](https://docs.cloud.google.com/lakehouse/docs/manage-catalogs).

  * Learn about [Apache Iceberg tables managed by Lakehouse](https://docs.cloud.google.com/lakehouse/docs/lakehouse-iceberg-tables).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
