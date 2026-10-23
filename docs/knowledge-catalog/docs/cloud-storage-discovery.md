---
url: https://docs.cloud.google.com/knowledge-catalog/docs/cloud-storage-discovery/
title: Discover and catalog Cloud Storage data \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:21:26.119604+00:00
---

# Discover and catalog Cloud Storage data  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/cloud-storage-discovery/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Discover and catalog Cloud Storage data Stay organized with collections  Save and categorize content based on your preferences. 

Knowledge Catalog automatic discovery, a feature in Knowledge Catalog also called standalone discovery, lets you scan data in Cloud Storage buckets to extract and catalog metadata. You can use this centralized table data to simplify AI-powered data insights, data security, and governance.

## Discovery scan overview

To use automatic discovery of Cloud Storage data, you create and run a discovery scan. A discovery scan does the following:

  * Scans the data in the Cloud Storage bucket or path.
  * Groups structured and semi-structured data into tables.
  * Collects metadata, such as the table name, schema, and partition definition.
  * Creates and updates [BigLake external](https://docs.cloud.google.com/bigquery/docs/biglake-intro), [non-BigLake external](https://docs.cloud.google.com/bigquery/docs/external-tables), or [BigLake object](https://docs.cloud.google.com/bigquery/docs/object-table-introduction) tables in BigQuery using the schema and partition definition.



### Structured and semi-structured data

Structured and semi-structured data includes formats like Avro, Parquet, and CSV. The discovery scan registers groups of these files as BigLake external tables. The scan detects files only if they are located in folders that contain the same data format and a compatible schema.

  * **Use case** : Centralize strongly typed, structured files into BigQuery to run analytical SQL queries without manually defining schemas.
  * **Workflow** : 
    1. Organize your structured files into folders. Ensure that the files in each folder share the same data format and have a compatible schema.
    2. Create a discovery scan and provide your Google Cloud resource connection ID.
    3. The scan groups the data and registers it as BigLake external tables.
    4. Query the published tables directly in BigQuery using SQL.



#### Supported formats

  * Parquet
  * Avro
  * ORC
  * JSON (only the [newline-delimited format](https://github.com/ndjson/ndjson-spec))
  * CSV (but not CSV files that have comment rows)



#### Compression formats

For structured and semi-structured data, the discovery scan supports the following compression formats:

  * Internal compression for the following formats:

Compression | File extension sample | Supported format  
---|---|---  
gzip | `.gz.parquet` | Parquet  
lz4 | `.lz4.parquet` | Parquet  
Snappy | `.snappy.parquet` | Parquet, ORC, Avro  
lzo | `.lzo.parquet` | Parquet, ORC  
  * External compression for JSON and CSV files:

    * gzip
    * bzip2



### Unstructured data

For unstructured data, such as images and videos, the discovery scan detects and registers groups of files that share the same data file format. Files must be located in folders that contain the same file format. For example, `gs://images/group1` must only contain GIF images, and `gs://images/group2` must only contain JPEG images for the discovery scan to detect and register two BigLake object tables.

  * **Use case** : Catalog unstructured files like images or documents to perform machine learning inference using BigQuery ML or remote functions.
  * **Workflow** : 
    1. Organize your unstructured files into folders. Ensure that the files in each folder share the same file format.
    2. Create a discovery scan.
    3. The scan groups the unstructured data and registers it as BigLake object tables.
    4. Perform inference on your unstructured files directly in BigQuery.



#### Supported formats

The discovery scan supports the following unstructured formats:

  * Image (such as JPEG, PNG, and BMP)
  * Documents (such as PDF, slide presentations, and text reports)
  * Audio or video (such as WAV, MP3, and MP4)



For more information, see [supported object files](https://docs.cloud.google.com/bigquery/docs/object-table-introduction#supported_object_files).

#### Compression formats

For object tables, compression is managed primarily through [Cloud Storage object metadata](https://docs.cloud.google.com/storage/docs/metadata), rather than BigQuery internal settings.

  * Standard metadata compression: BigQuery automatically recognizes files compressed with gzip and bzip2 if they use the standard .gz or .bz2 extensions.
  * Content-Encoding: you can use the [Content-Encoding gzip](https://docs.cloud.google.com/storage/docs/metadata#content-encoding) metadata in Cloud Storage to serve compressed files while maintaining their original content-type.
  * Media-internal compression: formats that are inherently compressed (such as JPEG for images, MP3 for audio, MP4 for video) are natively supported.



### Table registration and availability

The discovered tables are registered in BigQuery as one of the following table types, depending on the data format and your scan configuration:

  * **BigLake object tables**. Created for unstructured data, such as images and videos. Object tables provide a metadata index over unstructured data in Cloud Storage. For more information, see [Introduction to object tables](https://docs.cloud.google.com/bigquery/docs/object-table-introduction).
  * **BigLake external tables**. Created for structured and semi-structured data when you provide a Google Cloud resource connection ID during the scan configuration. BigLake tables let you query structured data in external datastores. For more information, see [Introduction to BigLake tables](https://docs.cloud.google.com/bigquery/docs/biglake-intro).
  * **External tables (non-BigLake)**. Created for structured and semi-structured data if you don't provide a resource connection ID. External tables let you query structured data in external datastores. For more information, see [Introduction to external tables](https://docs.cloud.google.com/bigquery/docs/external-tables).



This registration makes their data available for analysis in BigQuery. Metadata caching for BigLake tables and object tables is also enabled. All the BigLake tables are automatically ingested into Knowledge Catalog for search and discovery.

To start working with your newly registered tables, you can:

  * [Run a query](https://docs.cloud.google.com/bigquery/docs/running-queries) in BigQuery.
  * [Search for resources](https://docs.cloud.google.com/knowledge-catalog/docs/search-assets) in Knowledge Catalog.



### Limitations and quotas

A discovery scan doesn't support Apache Iceberg and Delta Lake table formats.

To see the limit of how many tables a discovery scan supports, see [Quotas and limits](https://docs.cloud.google.com/bigquery/quotas#dataplex-discovery).

## Before you begin

Enable the Dataplex API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=dataplex.googleapis.com)

**Note:** The roles listed in the next section are for a standard discovery scan. 

### Required roles for the Knowledge Catalog service account

Before you begin, assign the IAM permissions to the Knowledge Catalog service account in your project.
    
    
      service-PROJECT_NUMBER@gcp-sa-dataplex.iam.gserviceaccount.com
      

Replace `PROJECT_NUMBER` with the project in which the Dataplex API is enabled.

To ensure that the Knowledge Catalog service account has the necessary permissions to create and run a discovery scan, ask your administrator to grant the following IAM roles to the Knowledge Catalog service account: 

**Important:** You must grant these roles to the Knowledge Catalog service account, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 

  * [**Dataplex Discovery Service Agent** ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.discoveryServiceAgent) (`roles/dataplex.discoveryServiceAgent`) on the storage bucket
  * [**Dataplex Discovery Publishing Service Agent** ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.discoveryPublishingServiceAgent) (`roles/dataplex.discoveryPublishingServiceAgent`) on the user project
  * Create BigLake tables: [**Dataplex Discovery BigLake Publishing Service Agent** ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.discoveryBigLakePublishingServiceAgent) (`roles/dataplex.discoveryBigLakePublishingServiceAgent`) on the BigQuery connection 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to create and run a discovery scan. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create and run a discovery scan:

  * `bigquery.datasets.create` on the data source project
  * `storage.buckets.get` on the data source bucket
  * `storage.objects.get` on the data source bucket
  * `storage.objects.list` on the data source bucket
  * `bigquery.datasets.get` on the data source project
  * Provide a connection: 
    * `bigquery.connections.delegate` on the BigQuery connection
    * `bigquery.connections.use` on the BigQuery connection



Your administrator might also be able to give the Knowledge Catalog service account these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Required roles for the BigQuery connection service account

To ensure that the BigQuery Connection Service account has the necessary permissions to create a discovery scan, ask your administrator to grant the [**Dataplex Discovery Service Agent** ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.discoveryServiceAgent) (`roles/dataplex.discoveryServiceAgent`) IAM role to the BigQuery Connection Service account on the Cloud Storage bucket. **Important:** You must grant this role to the BigQuery Connection Service account, _not_ to your user account. Failure to grant the role to the correct principal might result in permission errors.  For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create a discovery scan. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create a discovery scan:

  * `bigquery.datasets.create` on the data source project
  * `storage.buckets.get` on the data source bucket
  * `storage.objects.get` on the data source bucket
  * `storage.objects.list` on the data source bucket
  * `bigquery.datasets.get` on the data source project
  * Provide a connection: 
    * `bigquery.connections.delegate` on the BigQuery connection
    * `bigquery.connections.use` on the BigQuery connection



Your administrator might also be able to give the BigQuery Connection Service account these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Required roles for end users

To get the permissions that you need to create and manage data discovery scans, ask your administrator to grant you the following IAM roles on the Cloud Storage bucket: 

  * Full access to DataScan resources: **Dataplex DataScan Administrator** (`roles/dataplex.dataScanAdmin`) - your project 
  * Write access to DataScan resources: **Dataplex DataScan Editor** (`roles/dataplex.dataScanEditor`) - your project 
  * Read access to DataScan resources, excluding the results: **Dataplex DataScan Viewer** (`roles/dataplex.dataScanViewer`) - your project 
  * Read access to DataScan resources, including the results: **Dataplex DataScan DataViewer** (`roles/dataplex.dataScanDataViewer`) - your project 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to create and manage data discovery scans. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create and manage data discovery scans:

  * Create a DataScan: `dataplex.datascans.create` on your project 
  * Delete a DataScan: `dataplex.datascans.delete` on your project or a DataScan resource 
  * View DataScan details excluding results: `dataplex.datascans.get` on your projector a DataScan resource 
  * View DataScan details including results: `dataplex.datascans.getData` on your project or a DataScan resource 
  * List DataScans: `dataplex.datascans.list` on your project or a DataScan resource 
  * Run a DataScan: `dataplex.datascans.run` on your project or a DataScan resource 
  * Update the description of a DataScan: `dataplex.datascans.update` on your projector a DataScan resource 
  * View the IAM permissions of the DataScan: `dataplex.datascans.getIamPolicy` on your project or a DataScan resource 
  * Set the IAM permissions on the DataScan: `dataplex.datascans.setIamPolicy` on your project or a DataScan resource 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a discovery scan

To discover data, you must create and run a discovery scan. You can set a schedule for the scan or run the scan on demand.

When the discovery scan runs, it creates a new dataset in BigQuery that corresponds to the Cloud Storage bucket that was scanned. The BigQuery dataset name is the same as the Cloud Storage bucket name. Invalid characters in the bucket name are replaced by an underscore. If the dataset name isn't available, a suffix is expanded (for example, `_discovered_001`). The dataset contains the BigLake external or non-BigLake external tables that were created by the discovery scan for further analysis.

### Console

  1. In the Google Cloud console, go to the **Cloud Storage discovery** page.

[Go to Cloud Storage discovery](https://console.cloud.google.com/dataplex/cloud-storage-discovery)

  2. Click **Create**.

  3. Enter a name for the scan.

  4. In the **ID** field, enter a unique ID that follows the [resource naming conventions in Google Cloud](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format). If you don't provide an ID, the discovery scan generates the scan ID.

  5. Optional: Provide a description of the scan.

  6. To specify the Cloud Storage bucket that contains the files to scan, in the **Bucket** field, browse to and select the bucket.

  7. Optional: Define the data to include or exclude from the discovery scan by providing a list of glob patterns for file filtering. Knowledge Catalog supports the following glob patterns:

     * `*`: Matches zero or more characters, without crossing directory boundaries. For example, `*.csv` matches `file.csv`, but not `folder/file.csv`.
     * `**`: Matches zero or more characters, crossing directory boundaries. For example, `**/*.csv` matches `file.csv` and `folder/subfolder/file.csv`.
     * `?`: Matches exactly one character. For example, `file_?.csv` matches `file_1.csv` and `file_a.csv`, but not `file_10.csv`.
     * `[...]`: Matches one character from a set of characters. For example, `[abc]` matches `a`, `b`, or `c`, and `[a-z]` matches any lowercase letter.
     * `{...}`: Matches a comma-separated list of subpatterns. For example, `{sun,moon,stars}` matches `sun`, `moon`, or `stars`.
     * `\`: Escapes a character (`*`, `?`, or `\`). For example, `file\*.csv` matches the literal filename `file*.csv`.

You can specify the following types of patterns:

     * **Include** : if only a subset of the data should be scanned, provide a list of glob patterns that match the objects to include.
     * **Exclude** : provide a list of glob patterns that match the objects to exclude.

For example, if you want to exclude `gs://test_bucket/foo/..` from the discovery scan, enter `**/foo/**` as the exclude path. Quotation marks cause errors. Make sure to enter `**/foo/**` instead of `"**/foo/**"`.

If you provide both include patterns and exclude patterns, the exclude patterns are applied first. 

  8. Optional: In **Project ID** , select the BigQuery dataset project that contains the BigLake external or non-BigLake external tables created by the discovery scan. If not provided, the dataset is created in the project that contains the Cloud Storage bucket.

  9. In **Location type** , select either **Region** or **Multi-region** (whichever is available) where the BigQuery publishing dataset is created.

  10. To create BigLake tables from the scanned data, in the **Connection ID** field, provide your Google Cloud resource connection ID. For more information, see [Google Cloud resource connections in BigQuery](https://docs.cloud.google.com/bigquery/docs/connections-api-intro#cloud-resource-connections).

You can create a new connection ID in the same location as the BigQuery dataset location, which is [compatible with the Cloud Storage bucket location](https://docs.cloud.google.com/bigquery/docs/external-tables#storage-location-considerations).

If you don't provide a resource connection ID, the discovery scan creates [non-BigLake external tables](https://docs.cloud.google.com/bigquery/docs/external-tables). To understand the differences between these external table types and why the discovery service might choose one over the other, see the [behavioral differences comparison](https://docs.cloud.google.com/bigquery/docs/external-data-sources#external_data_source_feature_comparison).

  11. In the **Discovery frequency** section, configure when you want the discovery scan to run:

     * **Repeat** : the scan runs on a predefined schedule. Provide the start time, days to run the scan, and the frequency, such as hourly.

     * **On demand** : the scan runs on demand.

  12. Optional: In the **JSON or CSV specifications** section, specify how the scan should process JSON and CSV files. Click **JSON or CSV specifications**.

     1. To configure JSON options, select **Enable JSON parsing options**. 
        * **Disable type inference** : whether the discovery scan should infer data types when scanning data. If you disable type inference for JSON data, all columns are registered as their primitive types, such as string, number, or boolean.
        * **Encoding format** : the character encoding of the data, such as UTF-8, US-ASCII, or ISO-8859-1. If you don't specify a value, UTF-8 is used as the default.
     2. To configure CSV options, select **Enable CSV parsing options**. 
        * **Disable type inference** : whether the discovery scan should infer data types when scanning data. If you disable type inference for CSV data, all columns are registered as strings.
        * **Header rows** : the number of header rows, either `0` or `1`. If you specify the value `0`, the discovery scan infers headings and extracts the column names from the file. The default is `0`.
        * **Column delimiter character** : the character that is used to separate values. Provide a single character, `\r` (carriage return), or `\n` (newline). The default is a comma (`,`).
        * **Encoding format** : the character encoding of the data, such as `UTF-8`, `US-ASCII`, or `ISO-8859-1`. If you don't specify a value, UTF-8 is used as the default.
  13. Click **Create** (for a scheduled scan), **Run now** (for an on-demand scan), or **Create and run** (for a one-time scan).

     * **Scheduled scan** : is run according to the schedule that you set.
     * **On-demand scan** : is run once initially when you create it, and you can run the scan at any time. It can take several minutes for the discovery scan to run.
     * **One-time scan** : executes automatically. It's automatically deleted when it reaches its defined time to live (TTL) threshold, a value that determines the duration a discovery scan remains active after execution. The TTL value can range from 0 seconds (immediate deletion) to 365 days. A discovery scan without a specified TTL is automatically deleted after 24 hours.



### gcloud

To create a discovery scan, use the [`gcloud dataplex datascans create data-discovery`](https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/datascans/create/data-discovery) command.
    
    
    gcloud dataplex datascans create data-discovery --location=LOCATION \
      --data-source-resource=BUCKET_PATH

Replace the following:

  * `LOCATION`: the location in which you'd like to create your discovery scan
  * `BUCKET_PATH`: the Cloud Storage path of the bucket you want to scan



### REST

To create a discovery scan, use the [`dataScans.create` method](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans/create).

## Query published BigLake tables

After you run the discovery scan, BigLake tables are published in a new dataset in BigQuery. The tables are then available for analysis in BigQuery using SQL.

You can view or query tables in BigQuery. For more information about how to run queries in BigQuery, see [Run a query](https://docs.cloud.google.com/bigquery/docs/running-queries).

## Manage published BigLake tables

Published BigLake tables are created and managed in BigQuery by the discovery scan. By default, the discovery scan handles new data discovery, schema inferences, and schema evolution every time the scheduled or on-demand scans are run. To indicate that metadata is managed by the scan, the scan publishes tables with the label `metadata-managed-mode` set to `discovery-managed`.

If you want to manage the schema and other metadata like CSV or JSON options yourself, set the `metadata-managed-mode` label to `user_managed`. This way, the schema remains unchanged when the next discovery scan runs. This approach can be useful in scenarios where the schema that's inferred by the discovery scan is incorrect or different from what is expected for a given table. When the `metadata-managed-mode` label is set to `user_managed`, it can reduce the cost.

To update the label, you can [edit the value of the label key](https://docs.cloud.google.com/bigquery/docs/updating-labels#updating_a_table_or_view_label) `metadata-managed-mode` to `user_managed` instead of `discovery-managed`. In this case, the discovery scan doesn't update the schema of the table as long as the `user_managed` label is attached to the table.

**Note:** You can apply access policies, such as [column-level security](https://docs.cloud.google.com/bigquery/docs/column-level-security-intro) and [row-level security](https://docs.cloud.google.com/bigquery/docs/row-level-security-intro), even if your tables are managed by the discovery scan.

### Update published BigLake tables

For BigLake tables published using the discovery scan jobs with the default configuration, the schema and other metadata are automatically updated with every discovery scan job run at the scheduled frequency.

To update a published BigLake table, follow these steps:

  1. In the Google Cloud console, go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. [Update one or more table properties](https://docs.cloud.google.com/bigquery/docs/managing-tables#updating_table_properties).

  3. In the left pane, click explore **Explorer** :

![Highlighted button for the Explorer pane.](https://docs.cloud.google.com/static/bigquery/images/explorer-tab.png)

If you don't see the left pane, click last_page **Expand left pane** to open the pane.

  4. In the **Explorer** pane, expand your project, click **Datasets** , and then select a dataset.

  5. Click **Overview > Tables**, and then select the table.

  6. In the **Details** tab, in the **Labels** section, make sure that the **metadata-managed-mode** label is set to **user_managed**. If it is set to a different value, follow these steps:

     1. Click edit **Edit details**.

     2. Next to the **metadata-managed-mode** key, in the **value** field, enter `user_managed`.


**Note:** A table with an updated schema becomes available for SQL and Spark queries. When the next discovery scans run, the table metadata remains unchanged.

### Delete published BigLake tables

To delete a published BigLake table, follow these steps:

  1. [Delete the data files for the table in the Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/deleting-objects).

  2. In the Google Cloud console, go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  3. In the left pane, click explore **Explorer** :

![Highlighted button for the Explorer pane.](https://docs.cloud.google.com/static/bigquery/images/explorer-tab.png)

  4. In the **Explorer** pane, expand your project, click **Datasets** , and then select a dataset.

  5. Click **Overview > Tables**, and then select the table.

  6. In the **Details** pane, in the **Labels** section, make sure the **metadata-managed-mode** label isn't set to `user_managed`. If it's set to `user_managed`, follow these steps:

     1. Click **Edit details** edit.

     2. Next to the **metadata-managed-mode** key, in the **value** field, enter `discovery-managed`.

**Note:** If the **metadata-managed-mode** label is set to `user_managed`, the discovery scan doesn't override the table metadata, which causes your table not to be deleted.
  7. Click **Run**. The discovery scan runs on demand.




After the discovery scan runs, the BigLake table is deleted in BigQuery and isn't available to list or query through Spark.

## Run a discovery scan on demand

To run a discovery scan on demand, select one of the following options:

### Console

  1. In the Google Cloud console, go to the **Cloud Storage discovery** page.

[Go to Cloud Storage discovery](https://console.cloud.google.com/dataplex/cloud-storage-discovery)

  2. Click the discovery scan you want to run.

  3. Click **Run now**.




### gcloud

To run a discovery scan, use the [`gcloud dataplex datascans run` command](https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/datascans/run):
    
    
    gcloud dataplex datascans run DATASCAN \
      --location=LOCATION
    

Replace the following variables:

  * `LOCATION`: the Google Cloud region in which the discovery scan was created.
  * `DATASCAN`: the name of the discovery scan.



### REST

To run a discovery scan on demand, use the [`dataScans.run` method](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans/run) in the Dataplex API.

## List discovery scans

To list your discovery scans, select one of the following options.

### Console

  1. In the Google Cloud console, go to the **Cloud Storage discovery** page.

[Go to Cloud Storage discovery](https://console.cloud.google.com/dataplex/cloud-storage-discovery)

  2. The discovery scans created in the project are listed.




### gcloud
    
    
    gcloud dataplex datascans list --location=LOCATION --project=PROJECT_ID

Replace the following:

  * `LOCATION`: the location of your project
  * `PROJECT_ID`: your Google Cloud project ID



### REST

To retrieve the list of discovery scans in your project, use the [`dataScans.list` method](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans/list) in the Dataplex API.

## View a discovery scan

To view a discovery scan, select one of the following options.

### Console

  1. In the Google Cloud console, go to the **Cloud Storage discovery** page.

[Go to Cloud Storage discovery](https://console.cloud.google.com/dataplex/cloud-storage-discovery)

  2. Click the discovery scan you want to view details for.

     * The **Scan details** section shows details about the discovery scan.
     * The **Scan status** section shows the discovery results of the latest scan job.



### gcloud
    
    
    gcloud dataplex datascans jobs describe JOB \
      --location=LOCATION \
      --datascan=DATASCAN \
      --view=FULL

Replace the following:

  * `JOB`: the job ID of the discovery scan job.
  * `LOCATION`: the Google Cloud region in which the discovery scan was created.
  * `DATASCAN`: the name of the discovery scan the job belongs to.



### REST

To view the results of a data discovery scan, use the [`dataScans.get` method](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans/get) in the Dataplex API.

### View historical discovery scan results

To view historical discovery scan results, select one of the following options.

### Console

  1. In the Google Cloud console, go to the **Cloud Storage discovery** page.

[Go to Cloud Storage discovery](https://console.cloud.google.com/dataplex/cloud-storage-discovery)

  2. Click the discovery scan you want to view details for.

  3. Click the **Scan history** pane. The **Scan history** pane provides information about past jobs, including the number of records scanned in each job, each job's status, and the time the jobs were run.

  4. To view detailed information about a job, click the job in the **Job ID** column.




### gcloud
    
    
    gcloud dataplex datascans jobs list \
      --location=LOCATION \
      --datascan=DATASCAN

Replace the following:

  * `LOCATION`: the Google Cloud region in which the discovery scan was created.
  * `DATASCAN`: the name of the discovery scan the job belongs to.



### REST

To view all the jobs of a discovery scan, use the [`dataScans.jobs.list` method](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans.jobs/list) in the Dataplex API.

## Update a discovery scan

To change the schedule of a discovery scan, for example, to change the schedule from on-demand to recurring, update the discovery scan.

**Note:** Updating a discovery scan is not supported for one-time discovery scans.

### Console

  1. In the Google Cloud console, go to the **Cloud Storage discovery** page.

[Go to Cloud Storage discovery](https://console.cloud.google.com/dataplex/cloud-storage-discovery)

  2. For the discovery scan you want to update, click **Actions > Edit**.

  3. Edit the values.

  4. Click **Save**.




### gcloud

To update a discovery scan, use the [`gcloud dataplex datascans update data-discovery`](https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/datascans/update/data-discovery) command.
    
    
    gcloud dataplex datascans update data-discovery SCAN_ID --location=LOCATION --description=DESCRIPTION

Replace the following:

  * `SCAN_ID`: the ID of the discovery scan you want to update
  * `LOCATION`: the Google Cloud region in which the discovery scan was created
  * `DESCRIPTION`: the new description for the discovery scan



### REST

To update a discovery scan, use the [`dataScans.patch` method](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans/patch) in the Dataplex API.

## Delete a discovery scan

To delete a discovery scan, select one of the following options.

### Console

  1. In the Google Cloud console, go to the **Cloud Storage discovery** page.

[Go to Cloud Storage discovery](https://console.cloud.google.com/dataplex/cloud-storage-discovery)

  2. For the discovery scan you want to delete, click **Actions > Delete**.

  3. Click **Delete**.




### gcloud
    
    
    gcloud dataplex datascans delete SCAN_ID --location=LOCATION --async

Replace the following:

  * `SCAN_ID`: the ID of the discovery scan you want to delete.
  * `LOCATION`: the Google Cloud region in which the discovery scan was created.



### REST

To delete a discovery scan, use the [`dataScans.delete` method](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans/delete) in the Dataplex API.

## What's next

  * Learn how to [search for resources in Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/search-assets).
  * Learn how to use [Knowledge Catalog client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
