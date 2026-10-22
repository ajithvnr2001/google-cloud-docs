---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/configure-bigquery-batch-source/
title: BigQuery batch source \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:17.175667+00:00
---

# BigQuery batch source  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/configure-bigquery-batch-source/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  BigQuery batch source Stay organized with collections  Save and categorize content based on your preferences. 

This page provides guidance about configuring the BigQuery batch source plugin in Cloud Data Fusion. 

The BigQuery source plugin lets you connect and load data from BigQuery tables. Data from a BigQuery table is exported into a temporary location in Cloud Storage, and then gets read into the pipeline from there.

## Before you begin

Cloud Data Fusion typically has two service accounts:

  * Design-time service account: [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/data-fusion/docs/concepts/service-accounts)
  * Execution-time service account: [Compute Engine Service Account ](https://docs.cloud.google.com/data-fusion/docs/concepts/service-accounts)



Before using the BigQuery batch source plugin, grant the following roles or permissions to each service account.

#### Cloud Data Fusion API Service Agent

This service account already has all the required permissions and you don't need to add additional permissions. For reference, it has the following permissions:

  * `bigquery.datasets.get`
  * `bigquery.tables.create`
  * `bigquery.tables.get`
  * `bigquery.tables.updateData`
  * `bigquery.tables.update`
  * `bigquery.tables.export`



If you're using a [namespace service account](https://docs.cloud.google.com/data-fusion/docs/how-to/control-access-in-namespace) in addition to the default design-time service account, add the permissions from the preceding list to it.

#### Compute Engine Service Account

In your Google Cloud project, grant the following IAM roles or permissions to the Compute Engine Service Account:

  * [BigQuery Job User](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.jobUser) (`roles/bigquery.jobUser`). This predefined role contains the required `bigquery.jobs.create` permission.
  * [BigQuery Data Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) (`roles/bigquery.dataEditor`). This predefined role contains the following required permissions:

    * `bigquery.datasets.get`
    * `bigquery.tables.create`
    * `bigquery.tables.get`
    * `bigquery.tables.updateData`
    * `bigquery.tables.update`
    * `bigquery.tables.export`



These roles and permissions can also be assigned on the BigQuery dataset or table, depending on your use case.

  * [Storage Legacy Bucket Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketWriter) (`roles/storage.legacyBucketWriter`). This predefined role contains the following required permissions:

    * `storage.buckets.get`
    * `storage.objects.get`
    * `storage.objects.list`



This role and these permissions can also be assigned on the Cloud Storage bucket, depending on your use case.

**Note:** If you don't provide a temporary bucket name when you configure the plugin properties, you need `storage.buckets.create` and `storage.buckets.delete` permissions, which can be assigned using the [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) role (`roles/storage.admin`) on the project.

## Configure the plugin

  1. [Go to the Cloud Data Fusion web interface](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline#navigate-web-interface) and click **Studio**.
  2. Check that **Data Pipeline - Batch** is selected (not **Realtime**).
  3. In the **Source** menu, click **BigQuery**. The BigQuery node appears in your pipeline.
  4. To configure the source, go to the BigQuery node and click **Properties**.
  5. Enter the following properties. For a complete list, see Properties.

     1. Enter a **Label** for the BigQuery node—for example, `BigQuery tables`.
     2. Enter the connection details. You can set up a new, one-time connection, or an existing, reusable connection.

### New connection

To add a one-time connection to BigQuery, follow these steps:

        1. In the **Project ID** field, leave the value as auto-detect.
        2. If the BigQuery dataset is in a different project, in the **Dataset Project ID** field, enter the ID.
        3. In the **Service account type** field, choose one of the following and enter the content in the next field:

           * **File path**
           * **JSON**

### Reusable connection

To reuse an existing connection, follow these steps:

        1. Turn on **Use connection**.
        2. Click **Browse connections**.
        3. Click the connection name—for example, **BigQuery Default**.

**Note:** For more information about adding, importing, and editing the connections that appear when you browse connections, see [Manage connections](https://docs.cloud.google.com/data-fusion/docs/how-to/managing-connections).
        4. Optional: If a connection doesn't exist and you want to create a new reusable connection, click **Add connection** and refer to the steps in the **New connection** tab on this page.

     3. In the **Reference name** field, enter a name to use for lineage.

     4. Optional: If your dataset is already available in your instance, click **Browse** and select the data to read.

     5. In the **Dataset** field, enter the name of the dataset that contains the table.

     6. In the **Table** field, enter the name of the table.

     7. To test connectivity, click **Get schema**.

     8. Optional: In the **Partition start date** field, enter the inclusive start date string—for example, `2021-01-11`.

     9. Optional: In the **Partition end date** field, enter the inclusive end date string—for example, `2024-01-11`.

     10. Optional: In the **Filter** field, enter a BigQuery [`WHERE` clause](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax#where_clause).

     11. Optional: In the **Temporary bucket name** field, enter a name for the Cloud Storage bucket.

     12. Optional: In the **Encryption Key Name** field, enter the Cloud Key Management Service (Cloud KMS) encryption key name. For more information, see [Get the resource name for the key](https://docs.cloud.google.com/data-fusion/docs/how-to/customer-managed-encryption-keys#get-the-resource-name).

     13. Optional: Turn on **Enable querying views**. If you enable them, do the following:

        * In the **Temporary table creation project** field, enter the project name where the temporary table is created.
        * In the **Temporary table creation dataset** field, enter the dataset name where the temporary table is created.
     14. Optional: Click **Validate** and address any errors found.

     15. Click close **Close**. Properties are saved and you can continue to build your data pipeline in the Cloud Data Fusion web interface.




### Properties

Property | Macro enabled | Required property | Description  
---|---|---|---  
**Label** | No | Yes | The name of the node in your data pipeline.  
**Use connection** | No | No | Browse for a reusable connection to the source. For more information about adding, importing, and editing the connections that appear when you browse connections, see [Manage connections](https://docs.cloud.google.com/data-fusion/docs/how-to/managing-connections).  
**Connection** | Yes | Yes | If **Use connection** is turned on, the name of the reusable connection you select appears in this field.  
**Project ID** | Yes | No | Used only when **Use connection** is turned off. A globally unique identifier for the project where the BigQuery job runs.  
Default is `auto-detect`.  
**Dataset project ID** | Yes | No | Used only when **Use connection** is turned off. If the dataset is in a different project than the one where the BigQuery job runs, this value is the globally unique identifier for the project with the BigQuery dataset. If no value is given, the field defaults to the **Project ID** value. The BigQuery Data Viewer role must be granted to the specified service account to read BigQuery data on the project.  
**Service account type** | Yes | No | Select one of the following options:  


  * **File path** : the path where the service account is located.
  * **JSON** : JSON content of the service account.

  
**Service account file path** | Yes | No | Used only when the Service account type value is **File path**. The path on the local file system of the service account key used for authorization. If jobs run on Managed Service for Apache Spark clusters, set the value to auto-detect. If jobs run on other types of clusters, the file must be present on every node in the cluster.  
Default is `auto-detect`.  
**Service account JSON** | Yes | No | Used only when the Service account type value is **JSON**. The JSON file content of the service account.  
**Reference name** | No | Yes | Name that uniquely identifies this source for other services, such as lineage and annotating metadata.  
**Dataset** | Yes | Yes | The dataset the table belongs to. A dataset is contained within a specific project. Datasets are top-level containers that organize and control access to tables and views.  
**Table** | Yes | Yes | The table to read from. A table contains individual records organized in rows. Each record is composed of columns (also called fields). Every table is defined by a schema that describes the column names, data types, and other information.  
**Partition start date** | Yes | No | Inclusive partition start date, specified as `yyyy-mm-dd`. If no value is given, all partitions up to the partition end date will be read.  
**Partition end date** | Yes | No | Exclusive partition end date, specified as `yyyy-mm-dd`. If no value is given, all partitions up from the partition start date are read.  
**Filter** | Yes | No | A SQL query that filters for the given conditions. For example, this query returns all rows from the `Roster` table where the `SchoolID` column has the value `SchoolID > 52`:  
`SELECT * FROM Roster WHERE SchoolID > 52;`. This is the same as the [`WHERE` clause](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax#where_clause) in BigQuery.  
**Temporary bucket name** | Yes | No | The Cloud Storage bucket for temporary data storage. It is automatically created if it does not exist. Temporary data is deleted after it has been read. If a name isn't provided, a unique bucket is created and then deleted after the run finishes.  
**Encryption key name** | Yes | No | Key that encrypts data written to any bucket created by the plugin. If the bucket exists, this value is ignored. For more information, see [CMEK](https://docs.cloud.google.com/data-fusion/docs/how-to/customer-managed-encryption-keys).  
**Enable querying views** | Yes | No | Whether to allow BigQuery Logical and Materialized views. Since BigQuery views aren't enabled by default, querying them may have performance overhead.  
Default is No.  
**Temporary table creation project** | Yes | No | Used only when **Enable querying views** is turned on. The project name where the temporary table should be created. Defaults to the same project the table is in.  
**Temporary table creation dataset** | Yes | No | The dataset in the specified project where the temporary table should be created. Defaults to the same dataset the table is in.  
**Output schema** | Yes | Yes | Schema of the table to read. You can fetch it by clicking **Get schema**.  
  
### Data type mappings

The following table is a list of BigQuery data types with corresponding CDAP types.

BigQuery data type | CDAP schema data type  
---|---  
`BOOL` | `boolean`  
`BYTES` | `bytes`  
`DATE` | `date`  
`DATETIME` | `datetime, string`  
`FLOAT64` | `double`  
`GEO` | `unsupported`  
`INT64` | `long`  
`NUMERIC` | `decimal`  
`BIGNUMERIC` | `decimal`  
`REPEATED` | `array`  
`STRING` | `string`, `datetime` (ISO 8601 format)  
`STRUCT` | `record`  
`TIME` | `time` (microseconds)  
`TIMESTAMP` | `timestamp` (microseconds)  
`JSON` | `unsupported`  
  
## Release notes

  * [February 8, 2024](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1280901131/CDAP+Hub+Release+Log#Feb-8%2C-2024)
  * [January 16, 2024](https://docs.cloud.google.com/data-fusion/docs/release-notes#January_16_2024)
  * [September 6, 2023](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1280901131/CDAP+Hub+Release+Log#September-6%2C-2023)
  * [June 14, 2023](https://docs.cloud.google.com/data-fusion/docs/release-notes#June_14_2023)
  * [December 6, 2022](https://docs.cloud.google.com/data-fusion/docs/release-notes#December_06_2022)



## What's next

  * Learn more about [plugins in Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/plugins).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
