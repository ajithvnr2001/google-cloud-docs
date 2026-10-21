---
url: https://docs.cloud.google.com/bigquery/docs/manage-open-source-metadata/
title: Manage open source metadata with BigLake metastore (classic) \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T14:25:17.518721+00:00
---

# Manage open source metadata with BigLake metastore (classic)  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/manage-open-source-metadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage open source metadata with BigLake metastore (classic)

**Warning:** BigLake metastore (classic) is no longer recommended for Google Cloud. Use [Lakehouse runtime catalog](https://docs.cloud.google.com/bigquery/docs/about-blms) instead.

BigLake metastore (classic) is a unified physical metadata service for data analytics products on Google Cloud. BigLake metastore (classic) provides a single source of truth for metadata and lets you manage and access data from multiple sources. BigLake metastore (classic) is accessible from BigQuery and various open data processing engines on Managed Service for Apache Spark, making it a useful tool for data analysts and engineers.

For management of business metadata, see [Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog).

## How BigLake metastore (classic) works

BigLake metastore (classic) is a serverless service that does not require you to provision resources before you use it. You can use it as a serverless alternative to [Hive Metastore](https://cwiki.apache.org/confluence/display/Hive/Design#Design-Metastore) in Managed Service for Apache Spark clusters. BigLake metastore (classic) functions in the same way as Hive Metastore through its Hive-compatible APIs, and you are able to immediately query open-format tables in BigQuery without any further steps. BigLake metastore (classic) only supports [Apache Iceberg tables](https://iceberg.apache.org/docs/latest/).

BigLake metastore (classic) provides [APIs](https://docs.cloud.google.com/bigquery/docs/reference/biglake/rest), client libraries, and data engine integration (such as [Apache Spark](https://spark.apache.org/)) to manage catalogs, databases, and tables.

## Limitations

BigLake metastore (classic) is subject to the following limitations:

  * BigLake metastore (classic) does not support Apache Hive tables.
  * Identity and Access Management (IAM) roles and permissions can only be granted to projects. Giving IAM permissions to resources is not supported.
  * [Cloud Monitoring](https://docs.cloud.google.com/monitoring) is not supported.
  * BigLake metastore (classic) catalogs and databases have the following naming limitations: 
    * Names can be up to 1,024 characters in length.
    * Names can contain only UTF-8 letters (uppercase, lowercase), numbers, and underscores.
    * Names must be unique for each project and region combination.
  * BigLake metastore (classic) tables follow the same naming conventions as BigQuery tables. For more information, see [Table naming](https://docs.cloud.google.com/bigquery/docs/tables#table_naming).



## Before you begin

You need to enable billing and the BigLake API before using BigLake metastore (classic).

  1. Ask your administrator to grant you the Service Usage Admin (`roles/serviceusage.serviceUsageAdmin`) IAM role on your project. For more information about granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).
  2. Enable billing for your Google Cloud project. Learn how to [check if billing is enabled on a project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled).
  3. Enable the BigLake API.

[Enable the API](https://console.cloud.google.com/apis/library/biglake.googleapis.com)




## Required roles

  * To have full control over BigLake metastore (classic) resources, you need the BigLake Admin role (`roles/biglake.admin`). If you are using a [BigQuery Spark connector](https://docs.cloud.google.com/dataproc/docs/tutorials/bigquery-connector-spark-example) service account, a [Managed Service for Apache Spark service account](https://docs.cloud.google.com/dataproc-serverless/docs/concepts/service-account), or a [Managed Service for Apache Spark VM service account](https://docs.cloud.google.com/dataproc/docs/concepts/iam/dataproc-principals#vm_service_account_data_plane_identity), grant the BigLake Admin role to the account.
  * To have read-only access to BigLake metastore (classic) resources, you need the BigLake Viewer role (`roles/biglake.viewer`). For example, when querying a BigLake metastore (classic) table in BigQuery, the user or the BigQuery connection service account must have the BigLake Viewer role.
  * To create BigQuery tables with connections, you need the BigQuery Connection User role (`roles/bigquery.connectionUser`). For more information about sharing connections, see [Share connections with users](https://docs.cloud.google.com/bigquery/docs/create-cloud-resource-connection#share_connections).



Depending on the use case, the identity who calls BigLake metastore (classic) can be users or service accounts:

  * **User:** when directly calling the BigLake API, or when querying an Apache Iceberg managed table table without a connection from BigQuery. BigQuery uses the user's credentials in this circumstance.
  * **[BigQuery Cloud Resource Connection](https://docs.cloud.google.com/bigquery/docs/create-cloud-resource-connection):** when querying an Iceberg managed table with a connection from BigQuery. BigQuery uses the connection service account credential to access BigLake metastore (classic).
  * **[BigQuery Spark Connector](https://docs.cloud.google.com/bigquery/docs/connect-to-spark):** when using Spark with BigLake metastore (classic) in a BigQuery [Spark stored procedure](https://docs.cloud.google.com/bigquery/docs/spark-procedures). Spark uses the service account credential of the Spark Connector to access BigLake metastore (classic) and create BigQuery tables.
  * **[Managed Service for Apache Spark service account](https://docs.cloud.google.com/dataproc-serverless/docs/concepts/service-account):** when using Spark with BigLake in Managed Service for Apache Spark. Spark uses the service account credential.
  * **[Managed Service for Apache Spark VM service account](https://docs.cloud.google.com/dataproc/docs/concepts/iam/dataproc-principals#vm_service_account_data_plane_identity):** when using Managed Service for Apache Spark (not Managed Service for Apache Spark). Apache Spark uses the VM service account credential.



Depending on your permissions, you can grant these roles to yourself or ask your administrator to grant them to you. For more information about granting roles, see [Viewing the grantable roles on resources](https://docs.cloud.google.com/iam/docs/viewing-grantable-roles).

To see the exact permissions that are required to access BigLake metastore (classic) resources, expand the **Required permissions** section:

### Required permissions

  * `biglake.tables.get` at the project level, for all read-only accesses. Querying an Iceberg managed table table is read-only.
  * `biglake.{catalogs|databases|tables}.*` at the project level, for all read and write permissions. Typically, Apache Spark needs the ability to read and write data, including the ability to create, manage, and view catalogs, databases, and tables.
  * `bigquery.connections.delegate` at the BigQuery Cloud Resource Connection level or higher, for creating an Iceberg managed table table using a connection.



## Connect to BigLake metastore (classic)

The following sections explain how to connect to BigLake metastore (classic). These sections install and use the BigLake Apache Iceberg catalog plugin, indicated by the JAR files in the following methods. The catalog plugin connects to BigLake metastore (classic) from open source engines like Apache Spark.

### Connect with a Managed Service for Apache Spark VM

To connect to BigLake metastore (classic) with a Managed Service for Apache Spark VM, do the following:

  1. [Use SSH to connect to Managed Service for Apache Spark.](https://docs.cloud.google.com/dataproc/docs/concepts/accessing/ssh)
  2. In the [Spark SQL CLI](https://spark.apache.org/docs/latest/sql-distributed-sql-engine-spark-sql-cli.html), use the following statement to install and configure the Apache Iceberg custom catalog to work with BigLake metastore (classic):
         
         spark-sql \
           --packages ICEBERG_SPARK_PACKAGE \
           --jars BIGLAKE_ICEBERG_CATALOG_JAR \
           --conf spark.sql.catalog.SPARK_CATALOG=org.apache.iceberg.spark.SparkCatalog \
           --conf spark.sql.catalog.SPARK_CATALOG.catalog-impl=org.apache.iceberg.gcp.biglake.BigLakeCatalog \
           --conf spark.sql.catalog.SPARK_CATALOG.gcp_project=PROJECT_ID \
           --conf spark.sql.catalog.SPARK_CATALOG.gcp_location=LOCATION \
           --conf spark.sql.catalog.SPARK_CATALOG.blms_catalog=BLMS_CATALOG \
           --conf spark.sql.catalog.SPARK_CATALOG.warehouse=GCS_DATA_WAREHOUSE_FOLDER \
           --conf spark.sql.catalog.SPARK_HMS_CATALOG=org.apache.iceberg.spark.SparkCatalog \
           --conf spark.sql.catalog.SPARK_HMS_CATALOG.type=hive \
           --conf spark.sql.catalog.SPARK_HMS_CATALOG.uri=thrift://HMS_URI:9083
           




Replace the following:

  * `ICEBERG_SPARK_PACKAGE`: the version of Apache Iceberg with Spark to use. We recommend using the Spark version that matches the Spark version in your [Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc/docs/concepts/versioning/dataproc-version-clusters) or [Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc-serverless/docs/concepts/versions/spark-runtime-versions) instance. To view a list of available Apache Iceberg versions, see [Apache Iceberg downloads](https://iceberg.apache.org/releases/). For example, the flag for Apache Spark 3.3 is:  
`--packages org.apache.iceberg:iceberg-spark-runtime-3.3_2.13:1.2.1`
  * `BIGLAKE_ICEBERG_CATALOG_JAR`: the Cloud Storage URI of the Iceberg custom catalog plugin to install. Depending on your environment, select one of the following: 
    * `Iceberg 1.9.1`: gs://spark-lib/biglake/biglake-catalog-iceberg1.9.1-0.1.3-with-dependencies.jar
    * `Iceberg 1.5.1`: gs://spark-lib/biglake/biglake-catalog-iceberg1.5.1-0.1.2-with-dependencies.jar
    * `Iceberg 1.5.0`: gs://spark-lib/biglake/biglake-catalog-iceberg1.5.0-0.1.1-with-dependencies.jar
    * `Iceberg 1.2.0`: gs://spark-lib/biglake/biglake-catalog-iceberg1.2.0-0.1.1-with-dependencies.jar
    * `Iceberg 0.14.0`: gs://spark-lib/biglake/biglake-catalog-iceberg0.14.0-0.1.1-with-dependencies.jar
  * `SPARK_CATALOG`: the catalog identifier for Spark. It is linked to a BigLake metastore (classic) catalog.
  * `PROJECT_ID`: the Google Cloud project ID of the BigLake metastore (classic) catalog that the Spark catalog links with.
  * `LOCATION`: the [Google Cloud location](https://docs.cloud.google.com/bigquery/docs/locations) of the BigLake metastore (classic) catalog that the Spark catalog links with.
  * `BLMS_CATALOG`: the BigLake metastore (classic) catalog ID that the Spark catalog links with. The catalog does not need to exist, and it can be created in Spark.
  * `GCS_DATA_WAREHOUSE_FOLDER`: the Cloud Storage folder where Spark creates all files. It starts with `gs://`.
  * `HMS_DB`: (optional) the HMS database containing the table to copy from.
  * `HMS_TABLE`: (optional) the HMS table to copy from.
  * `HMS_URI`: (optional) the HMS Thrift endpoint.



### Connect with a Managed Service for Apache Spark cluster

Alternatively, you can submit a Managed Service for Apache Spark job to a cluster. The following sample installs the appropriate [Iceberg Custom Catalog](https://iceberg.apache.org/docs/latest/custom-catalog/).

To connect with a Managed Service for Apache Spark cluster, [submit a job](https://docs.cloud.google.com/dataproc/docs/guides/submit-job) with the following specifications:
    
    
    CONFS="spark.sql.catalog.SPARK_CATALOG=org.apache.iceberg.spark.SparkCatalog,"
    CONFS+="spark.sql.catalog.SPARK_CATALOG.catalog-impl=org.apache.iceberg.gcp.biglake.BigLakeCatalog,"
    CONFS+="spark.sql.catalog.SPARK_CATALOG.gcp_project=PROJECT_ID,"
    CONFS+="spark.sql.catalog.SPARK_CATALOG.gcp_location=LOCATION,"
    CONFS+="spark.sql.catalog.SPARK_CATALOG.blms_catalog=BLMS_CATALOG,"
    CONFS+="spark.sql.catalog.SPARK_CATALOG.warehouse=GCS_DATA_WAREHOUSE_FOLDER,"
    CONFS+="spark.jars.packages=ICEBERG_SPARK_PACKAGE"
    
    gcloud dataproc jobs submit spark-sql --cluster=MANAGED_SERVICE_FOR_APACHE_SPARK_CLUSTER \
      --project=MANAGED_SERVICE_FOR_APACHE_SPARK_PROJECT_ID \
      --region=MANAGED_SERVICE_FOR_APACHE_SPARK_LOCATION \
      --jars=BIGLAKE_ICEBERG_CATALOG_JAR \
      --properties="${CONFS}" \
      --file=QUERY_FILE_PATH

Replace the following:

  * `MANAGED_SERVICE_FOR_APACHE_SPARK_CLUSTER`: the Managed Service for Apache Spark cluster to [submit](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/spark) the job to.
  * `MANAGED_SERVICE_FOR_APACHE_SPARK_PROJECT_ID`: the project ID of the Managed Service for Apache Spark cluster. This ID can be different from `PROJECT_ID`.
  * `MANAGED_SERVICE_FOR_APACHE_SPARK_LOCATION`: the location of the Managed Service for Apache Spark cluster. This location can be different from `LOCATION`.
  * `QUERY_FILE_PATH`: the path to the file containing queries to run.



### Connect with Managed Service for Apache Spark

Similarly, you can submit a batch workload to Managed Service for Apache Spark. To do so, follow the [batch workload instructions](https://docs.cloud.google.com/dataproc-serverless/docs/quickstarts/spark-batch#submit_a_spark_batch_workload) with the following additional flags:

  * `--properties="${CONFS}"`
  * `--jars=BIGLAKE_ICEBERG_CATALOG_JAR`



### Connect with BigQuery stored procedures

You can use BigQuery stored procedures to run Managed Service for Apache Spark jobs. The process is similar to running Managed Service for Apache Spark jobs directly in Managed Service for Apache Spark.

## Create metastore resources

The following sections describe how to create resources in the metastore.

### Create catalogs

Catalog names have constraints; for more information, see Limitations. To create a catalog, select one of the following options:

###  API 

Use the [`projects.locations.catalogs.create`](https://docs.cloud.google.com/bigquery/docs/reference/biglake/rest/v1/projects.locations.catalogs/create) method and specify the name of a catalog.

###  Spark SQL 
    
    
    CREATE NAMESPACE SPARK_CATALOG;

###  Terraform 

This creates a BigLake database named 'my_database' of type 'HIVE' in the catalog specified by the 'google_biglake_catalog.default.id' variable. For more information, see the [Terraform BigLake documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/biglake_catalog).
    
    
    resource "google_biglake_catalog" "default" {
    name     = "my_catalog"
    location = "US"
    }

### Create databases

Database names have constraints; for more information, see Limitations. To ensure that your database resource is compatible with data engines, we recommend creating databases using data engines instead of manually crafting the resource body. To create a database, select one of the following options:

###  API 

Use the [`projects.locations.catalogs.databases.create`](https://docs.cloud.google.com/bigquery/docs/reference/biglake/rest/v1/projects.locations.catalogs.databases/create) method and specify the name of a database.

###  Spark SQL 
    
    
    CREATE NAMESPACE SPARK_CATALOG.BLMS_DB;

Replace the following:

  * `BLMS_DB`: the BigLake metastore (classic) database ID to create



###  Terraform 

This creates a BigLake database named 'my_database' of type 'HIVE' in the catalog specified by the 'google_biglake_catalog.default.id' variable. For more information, see the [Terraform BigLake documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/biglake_catalog).
    
    
    resource "google_biglake_database" "default" {
    name    = "my_database"
    catalog = google_biglake_catalog.default.id
    type    = "HIVE"
    hive_options {
      location_uri = "gs://${google_storage_bucket.default.name}/${google_storage_bucket_object.metadata_directory.name}"
      parameters = {
        "owner" = "Alex"
      }
    }
    }

### Create tables

Table names have constraints. For more information, see [Table naming](https://docs.cloud.google.com/bigquery/docs/tables#table_naming). To create a table, select one of the following options:

###  API 

Use the [`projects.locations.catalogs.databases.tables.create`](https://docs.cloud.google.com/bigquery/docs/reference/biglake/rest/v1/projects.locations.catalogs.databases.tables/create) method and specify the name of a table.

###  Spark SQL 
    
    
    CREATE TABLE SPARK_CATALOG.BLMS_DB.BLMS_TABLE
      (id bigint, data string) USING iceberg;

Replace the following:

  * `BLMS_TABLE`: the BigLake metastore (classic) table ID to create



###  Terraform 

This registers a BigLake metastore (classic) table with the name "my_table" and type "Hive" in the database specified by the "google_biglake_database.default.id" variable. Note that the table must exist prior to registration in the catalog, which can be accomplished by initializing the table from an engine such as Apache Spark. Refer to the Terraform Provider Documentation for more information: [BigLake Table](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/biglake_table).
    
    
    resource "google_biglake_table" "default" {
    name     = "my-table"
    database = google_biglake_database.default.id
    type     = "HIVE"
    hive_options {
      table_type = "MANAGED_TABLE"
      storage_descriptor {
        location_uri  = "gs://${google_storage_bucket.default.name}/${google_storage_bucket_object.data_directory.name}"
        input_format  = "org.apache.hadoop.mapred.SequenceFileInputFormat"
        output_format = "org.apache.hadoop.hive.ql.io.HiveSequenceFileOutputFormat"
      }
      parameters = {
        "spark.sql.create.version"          = "3.1.3"
        "spark.sql.sources.schema.numParts" = "1"
        "transient_lastDdlTime"             = "1680894197"
        "spark.sql.partitionProvider"       = "catalog"
        "owner"                             = "Alex"
        "spark.sql.sources.schema.part.0" = jsonencode({
          "type" : "struct",
          "fields" : [
            { "name" : "id", "type" : "integer",
              "nullable" : true,
              "metadata" : {}
            },
            {
              "name" : "name",
              "type" : "string",
              "nullable" : true,
              "metadata" : {}
            },
            {
              "name" : "age",
              "type" : "integer",
              "nullable" : true,
              "metadata" : {}
            }
          ]
        })
        "spark.sql.sources.provider" = "iceberg"
        "provider"                   = "iceberg"
      }
    }
    }

### E2E Terraform Example

This [GitHub example](https://github.com/terraform-google-modules/terraform-docs-samples/blob/main/bigquery/biglake/biglake_metastore_create_table/main.tf) provides a runnable E2E example that creates a BigLake metastore (classic) Catalog, Database, and Table. For more information on how to use this example, refer to [Basic Terraform Commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

#### Copy an Iceberg table from Hive Metastore to BigLake metastore (classic)

To create an Iceberg table and copy a Hive Metastore table over to BigLake metastore (classic), use the following Spark SQL statement:
    
    
    CREATE TABLE SPARK_CATALOG.BLMS_DB.BLMS_TABLE
      (id bigint, data string) USING iceberg
      TBLPROPERTIES(hms_table='HMS_DB.HMS_TABLE');

#### Link BigLake tables to BigLake metastore (classic) tables

When creating an Iceberg table in Spark, you can optionally create a linked Iceberg external table table at the same time.

##### Automatically link tables

To create an Iceberg table in Spark and automatically create an Iceberg external table at the same time, use the following Spark SQL statement:
    
    
      CREATE TABLE SPARK_CATALOG.BLMS_DB.BLMS_TABLE
        (id bigint, data string) USING iceberg
        TBLPROPERTIES(bq_table='BQ_TABLE_PATH',
        bq_connection='BQ_RESOURCE_CONNECTION');

Replace the following:

  * `BQ_TABLE_PATH`: the path of the Iceberg external table to create. Follow the [BigQuery table path syntax](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language#table_path). It uses the same project as the BigLake metastore (classic) catalog if the project is unspecified.
  * `BQ_RESOURCE_CONNECTION` (optional): the format is `project.location.connection-id`. If specified, BigQuery queries use the [Cloud Resource connection](https://docs.cloud.google.com/bigquery/docs/create-cloud-resource-connection#create-cloud-resource-connection) credentials to access BigLake metastore (classic). If not specified, BigQuery creates a regular external table instead of a BigLake table.

**Note:** The BigQuery dataset where you want to create tables must already exist. This statement does not create a dataset. The location of BigQuery datasets and tables must be the same as the BigLake metastore (classic) catalog.



##### Manually link tables

To manually create Iceberg external table links with specified BigLake metastore (classic) table URIs (`blms://…`), use the following BigQuery SQL statement:
    
    
    CREATE EXTERNAL TABLE 'BQ_TABLE_PATH'
      WITH CONNECTION `BQ_RESOURCE_CONNECTION`
      OPTIONS (
              format = 'ICEBERG',
              uris = ['blms://projects/PROJECT_ID/locations/LOCATION/catalogs/BLMS_CATALOG/databases/BLMS_DB/tables/BLMS_TABLE']
              )

## View metastore resources

The following sections describe how to view resources in BigLake metastore (classic).

### View catalogs

To see all databases in a catalog, use the [`projects.locations.catalogs.list`](https://docs.cloud.google.com/bigquery/docs/reference/biglake/rest/v1/projects.locations.catalogs/list) method and specify the name of a catalog.

To see information about a catalog, use the [`projects.locations.catalogs.get`](https://docs.cloud.google.com/bigquery/docs/reference/biglake/rest/v1/projects.locations.catalogs/get) method and specify the name of a catalog.

### View databases

To view a database, do the following:

###  Console 

To view a database and copy a link to it, do the following:

  1. In the Google Cloud console, go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. In the **Explorer** pane, expand your project and your catalog.

  3. Click the database (namespace) that you want to view. The database details open in a new tab.

  4. Optional: To share a link to the database, click link **Copy link**.




###  API 

To see all tables in a database, use the [`projects.locations.catalogs.databases.list`](https://docs.cloud.google.com/bigquery/docs/reference/biglake/rest/v1/projects.locations.catalogs.databases/list) method and specify the name of a database.

To see information about a database, use the [`projects.locations.catalogs.databases.get`](https://docs.cloud.google.com/bigquery/docs/reference/biglake/rest/v1/projects.locations.catalogs.databases/get) method and specify the name of a database.

###  Spark SQL 

To see all databases in a catalog, use the following statement:
    
    
    SHOW { DATABASES | NAMESPACES } IN SPARK_CATALOG;

To see information about a defined database, use the following statement:
    
    
    DESCRIBE { DATABASE | NAMESPACE } [EXTENDED] SPARK_CATALOG.BLMS_DB;

### View tables

To view all tables in a database or view a defined table, do the following:

###  API 

To see all tables in a database, use the [`projects.locations.catalogs.databases.tables.list`](https://docs.cloud.google.com/bigquery/docs/reference/biglake/rest/v1alpha1/projects.locations.catalogs.databases.tables/list) method and specify the name of a database.

To see information about a table, use the [`projects.locations.catalogs.databases.tables.get`](https://docs.cloud.google.com/bigquery/docs/reference/biglake/rest/v1alpha1/projects.locations.catalogs.databases.tables/get) method and specify the name of a table.

###  Spark SQL 

To see all tables in a database, use the following statement:
    
    
    SHOW TABLES IN SPARK_CATALOG.BLMS_DB;

To see information about a defined table, use the following statement:
    
    
    DESCRIBE TABLE [EXTENDED] SPARK_CATALOG.BLMS_DB.BLMS_TABLE;

## Modify metastore resources

The following sections describe how to modify resources in the metastore.

### Update tables

To avoid conflicts when multiple jobs try to update the same table at the same time, BigLake metastore (classic) uses optimistic locking. To use optimistic locking, you first need to get the current version of the table (called an _etag_) by using the `GetTable` method. Then you can make changes to the table and use the `UpdateTable` method, passing in the previously fetched etag. If another job updates the table after you fetch the etag, the `UpdateTable` method fails. This measure ensures that only one job can update the table at a time, preventing conflicts.

To update a table, select one of the following options:

###  API 

Use the [`projects.locations.catalogs.databases.tables.patch`](https://docs.cloud.google.com/bigquery/docs/reference/biglake/rest/v1/projects.locations.catalogs.databases.tables/patch) method and specify the name of a table.

###  Spark SQL 

For table update options in SQL, see [`ALTER TABLE`](https://iceberg.apache.org/docs/latest/spark-ddl/#alter-table).

### Rename tables

To rename a table, select one of the following options:

###  API 

Use the [`projects.locations.catalogs.databases.tables.rename`](https://docs.cloud.google.com/bigquery/docs/reference/biglake/rest/v1/projects.locations.catalogs.databases.tables/rename) method and specify the name of a table and a `newName` value.

###  Spark SQL 
    
    
    ALTER TABLE BLMS_TABLE RENAME TO NEW_BLMS_TABLE;

Replace the following:

  * `NEW_BLMS_TABLE`: the new name for `BLMS_TABLE`. Must be in the same dataset as `BLMS_TABLE`.



## Delete metastore resources

The following sections describe how to delete resources in BigLake metastore (classic).

### Delete catalogs

To delete a catalog, select one of the following options:

###  API 

Use the [`projects.locations.catalogs.delete`](https://docs.cloud.google.com/bigquery/docs/reference/biglake/rest/v1/projects.locations.catalogs/delete) method and specify the name of a catalog. This method does not delete the associated files on Google Cloud.

###  Spark SQL 
    
    
    DROP NAMESPACE SPARK_CATALOG;

### Delete databases

To delete a database, select one of the following options:

###  API 

Use the [`projects.locations.catalogs.databases.delete`](https://docs.cloud.google.com/bigquery/docs/reference/biglake/rest/v1/projects.locations.catalogs.databases/delete) method and specify the name of a database. This method does not delete the associated files on Google Cloud.

###  Spark SQL 
    
    
    DROP NAMESPACE SPARK_CATALOG.BLMS_DB;

### Delete tables

To delete a table, select one of the following options:

###  API 

Use the [`projects.locations.catalogs.databases.tables.delete`](https://docs.cloud.google.com/bigquery/docs/reference/biglake/rest/v1/projects.locations.catalogs.databases.tables/delete) method and specify the name of a table. This method does not delete the associated files on Google Cloud.

###  Spark SQL 

To only drop the table, use the following statement:
    
    
    DROP TABLE SPARK_CATALOG.BLMS_DB.BLMS_TABLE;

To drop the table and delete the associated files on Google Cloud, use the following statement:
    
    
    DROP TABLE SPARK_CATALOG.BLMS_DB.BLMS_TABLE PURGE;

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
