---
url: https://docs.cloud.google.com/dataproc-metastore/docs/import-metadata/
title: Import metadata into Dataproc Metastore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:56:06.075458+00:00
---

# Import metadata into Dataproc Metastore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataproc-metastore/docs/import-metadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataproc Metastore ](https://docs.cloud.google.com/dataproc-metastore/docs)
  * [ Guides ](https://docs.cloud.google.com/dataproc-metastore/docs/create-service-cluster)



Send feedback 

#  Import metadata into Dataproc Metastore Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to import metadata into a Dataproc Metastore service.

The import metadata feature lets you populate an existing Dataproc Metastore service with metadata that's stored in a portable storage format.

This portable metadata is typically [exported from another Dataproc Metastore](https://docs.cloud.google.com/dataproc-metastore/docs/export-metadata) service or from a self-managed Hive Metastore (HMS).

## About importing metadata

You can import the following file formats into Dataproc Metastore:

  * A set of Avro files stored in a folder.
  * A single MySQL dump file stored in a Cloud Storage folder.



The MySQL or Avro files you're importing must be generated from a relational database.

If your files are in a different format, such as PostgreSQL, you must convert them to the Avro or MySQL format. After the conversion, you can import them into Dataproc Metastore.

### Avro

Avro based imports are only supported for Hive versions 2.3.6 and 3.1.2. When importing Avro files, Dataproc Metastore expects a series of `<table-name>.avro` files for each table in your database.

To import Avro files, your Dataproc Metastore service can use the MySQL or Spanner database type.

### MySQL

MySQL based imports are supported for all Hive versions. When importing MySQL files, Dataproc Metastore expects a single SQL file containing all of your table information. MySQL dumps obtained from a Managed Service for Apache Spark cluster using Native SQL are also supported.

To import MySQL files, your Dataproc Metastore service must use the MySQL database type. The Spanner database type doesn't support MySQL imports.

### Import considerations

  * Importing overwrites all existing metadata stored in a Dataproc Metastore service.

  * The metadata import feature only imports metadata. Data that's created by Apache Hive in internal tables isn't replicated in the import.

  * Importing doesn't transform database content and doesn't handle file migration. If you move your data to a different location, you must manually update your table data locations and schema in your Dataproc Metastore service.

  * Importing doesn't restore or replace fine-grained IAM policies.

  * If you're using [VPC Service Controls](https://docs.cloud.google.com/dataproc-metastore/docs/vpc-sc), then you can only import data from a Cloud Storage bucket that resides in the same service perimeter as the Dataproc Metastore service.




## Before you begin

  * [Enable Dataproc Metastore](https://docs.cloud.google.com/dataproc-metastore/docs/enable-service) in your project.
  * [Understand networking requirements](https://docs.cloud.google.com/dataproc-metastore/docs/access-service) specific to your project.
  * [Create a Dataproc Metastore service](https://docs.cloud.google.com/dataproc-metastore/docs/create-service).



### Required roles

To get the permissions that you need to import metadata into Dataproc Metastore, ask your administrator to grant you the following IAM roles: 

  * To import metadata: 
    * [Dataproc Metastore Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`) on the metadata service.
    * [Dataproc Metastore Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`) on the project.
  * For MySQL, to use the Cloud Storage object (SQL dump file) for import: [grant your user account and the Dataproc Metastore service agent the Storage Object Viewer role ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) (`roles/storage.objectViewer`) on the Cloud Storage bucket containing the metadata dump being imported. 
  * For Avro, to use the Cloud Storage bucket for import: [grant your user account and the Dataproc Metastore service agent the Storage Object Viewer role ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) (`roles/storage.objectViewer`) on the Cloud Storage bucket containing the metadata dump being imported. 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to import metadata into Dataproc Metastore. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to import metadata into Dataproc Metastore:

  * To import metadata: `metastore.imports.create` on the metastore service. 
  * For MySQL, to use the Cloud Storage object (SQL dump file) for import, grant your user account and the Dataproc Metastore service agent: `storage.objects.get` on the Cloud Storage bucket containing the metadata dump being imported. 
  * For Avro, to use the Cloud Storage bucket for import, grant your user account and the Dataproc Metastore service agent: `storage.objects.get` on the Cloud Storage bucket containing the metadata dump being imported. 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about specific Dataproc Metastore roles and permissions, see [Dataproc Metastore IAM overview](https://docs.cloud.google.com/dataproc-metastore/docs/iam-and-access-control). 

## Import your metadata

The import operation is a two-step process. First, you prepare your import files and then you import them into Dataproc Metastore.

When you start an import, Dataproc Metastore performs a Hive metadata schema validation. This validation verifies the tables in the SQL dump file and the filenames for Avro. If a table is missing, the import fails with an error message describing the missing table.

To check Hive metadata compatibility before an import, you can use the [ Dataproc Metastore Toolkit](https://github.com/GoogleCloudPlatform/dataproc-metastore-toolkit).

### Prepare the import files before import

Before you can import your files into Dataproc Metastore, you must copy your metadata dump files into Cloud Storage, such as your [artifacts Cloud Storage bucket](https://docs.cloud.google.com/dataproc-metastore/docs/hive-metastore#create-bucket).

#### Move your files to Cloud Storage

  1. Create a database dump of the external database that you want to import into Dataproc Metastore.

For instructions on creating a database dump, see the following pages:

     * [Avro files](https://avro.apache.org/docs/current/index.html)
     * [MySQL dump file](https://dev.mysql.com/doc/refman/5.7/en/mysqldump-sql-format.html)
     * [Cloud SQL MySQL instance](https://docs.cloud.google.com/sql/docs/mysql/import-export/exporting)

**Note:** If you're exporting your dump files from another Dataproc Metastore, you can use the [Dataproc Metastore export](https://docs.cloud.google.com/dataproc-metastore/docs/export-metadata) feature to generate a valid set of files.
  2. Upload the files into Cloud Storage.

Make sure you write down the Cloud Storage path that you upload your files to, you need to use it later to perform the import.

     * If you're importing MySQL files, upload the SQL file into a [Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/uploading-objects).

     * If you're importing Avro files, upload the files into a [Cloud Storage folder](https://docs.cloud.google.com/storage/docs/objects#simulated-folders).

       * Your Avro import should include an Avro file for each Hive table, even if the table is empty.
       * The Avro filenames must follow the format `<table-name>.avro`. The `<table-name>` must be all caps. For example, `AUX_TABLE.avro`.



### Import the files into Dataproc Metastore

Before importing metadata, review the import considerations.

While an import is running, you can't update a Dataproc Metastore service — for example changing configuration settings. However, you can still use it for normal operations, such as using it to access its metadata from attached Managed Service for Apache Spark or self-managed clusters.

**Caution:** Import overwrites existing data.

### Console

  1. In the Google Cloud console, open the **Dataproc Metastore** page:

[Open Dataproc Metastore](https://console.cloud.google.com/dataproc/metastore/services)

  2. On the **Dataproc Metastore** page, click the name of the service you want to import metadata into.

The **Service detail** page opens.

![Service detail page](https://docs.cloud.google.com/static/dataproc-metastore/images/service-detail-page.png)**Figure 1.** The Dataproc Metastore Service detail page. 
  3. In the navigation bar, click **Import**.

The **Import** dialog opens.

  4. Enter the **Import name**.

  5. In the **Destination** section, choose either **MySQL** or **Avro**.

  6. In the **Destination URI** field, click **Browse** and select the **Cloud Storage URI** where you want to import your files to.

You can also manually enter your bucket location in the provided text field. Use the following format: `bucket/object` or `bucket/folder/object`.

  7. Optional: Enter a **Description** of the import.

You can edit the description on the **Service detail** page.

  8. To update the service, click **Import**.

After the import completes, it appears in a table on the **Service detail** page on the **Import/Export** tab.




### gcloud CLI

  1. To import metadata, run the following [`gcloud metastore services import gcs`](https://docs.cloud.google.com/sdk/gcloud/reference/metastore/services/import/gcs) command:
         
         gcloud metastore services import gcs SERVICE_ID \
           --location=LOCATION \
           --import-id=IMPORT_ID \
           --description=DESCRIPTION \
           --dump-type=DUMP_TYPE \
           --database-dump=DATABASE_DUMP
         

Replace the following:

     * `SERVICE_ID`: the ID or fully qualified name of your Dataproc Metastore service.
     * `LOCATION`: the Google Cloud region in which your Dataproc Metastore service resides.
     * `IMPORT_ID`: an ID or fully qualified name for your metadata import. For example, `import1`.
     * `DESCRIPTION`: Optional: A description of your import. You can edit this later using `gcloud metastore services imports update IMPORT`.
     * `DUMP_TYPE`: the type of the external database you're importing. Accepted values include `mysql` and `avro`. The default value is `mysql`.
     * `DATABASE_DUMP`: the path to the Cloud Storage containing the database files. This path must begin with `gs://`. For Avro, provide the path to the folder where the Avro files are stored (the Cloud Storage folder). For MySQL, provide the path to the MySQL file (the Cloud Storage object).
  2. Verify that the import was successful.




### REST

Follow the API instructions to [import metadata into a service](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services.metadataImports/create) by using the APIs Explorer.

Using the API, you can create, list, describe, and update imports, but you can't delete imports. However, deleting a Dataproc Metastore service deletes all stored nested imports.

When the import succeeds, Dataproc Metastore automatically returns to the [active state](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#state). If the import fails, then Dataproc Metastore rolls back to its previous healthy state.

### View import history

To view the import history of a Dataproc Metastore service in the Google Cloud console, complete the following steps:

  1. In the Google Cloud console, open the [**Dataproc Metastore**](https://console.cloud.google.com/dataproc/metastore/services) page.
  2. In the navigation bar, click **Import/Export**.

Your import history appears in the **Import history** table.

The history displays up to the last 25 imports.




Deleting a Dataproc Metastore service also deletes all associated import history.

## Troubleshoot common issues

Some common issues include the following:

  * [Import fails because the Hive versions don't match](https://docs.cloud.google.com/dataproc-metastore/docs/troubleshooting#import-and-export-error-scenarios).
  * [The service agent or user account doesn't have necessary permissions](https://docs.cloud.google.com/dataproc-metastore/docs/troubleshooting#service-agent-or-user-permissions).
  * [Job fails because the database file is too large](https://docs.cloud.google.com/dataproc-metastore/docs/troubleshooting#job-failed-database-file-size).



For more help solving common troubleshooting issues, see [Import and export error scenarios](https://docs.cloud.google.com/dataproc-metastore/docs/troubleshooting#import-and-export-error-scenarios).

## What's next

  * [Export metadata from a service](https://docs.cloud.google.com/dataproc-metastore/docs/export-metadata)
  * [Update and delete a service](https://docs.cloud.google.com/dataproc-metastore/docs/manage-service)
  * [Hive Metastore](https://docs.cloud.google.com/dataproc-metastore/docs/hive-metastore)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
