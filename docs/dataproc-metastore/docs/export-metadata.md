---
url: https://docs.cloud.google.com/dataproc-metastore/docs/export-metadata/
title: Export metadata from Dataproc Metastore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:29:12.166409+00:00
---

# Export metadata from Dataproc Metastore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataproc-metastore/docs/export-metadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataproc Metastore ](https://docs.cloud.google.com/dataproc-metastore/docs)
  * [ Guides ](https://docs.cloud.google.com/dataproc-metastore/docs/create-service-cluster)



Send feedback 

#  Export metadata from Dataproc Metastore Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to export metadata from Dataproc Metastore.

The export metadata feature lets you save your metadata in a portable storage format.

After you export your data, you can then [import the metadata](https://docs.cloud.google.com/dataproc-metastore/docs/import-metadata) into another Dataproc Metastore service or a self-managed Hive Metastore (HMS).

## About exporting metadata

When you export metadata from Dataproc Metastore, the service stores the data in one of the following file formats:

  * A set of Avro files stored in a folder.
  * A single MySQL dump file stored in a Cloud Storage folder.



### Avro

Avro based exports are only supported for Hive versions 2.3.6 and 3.1.2. When you export Avro files, Dataproc Metastore creates a `<table-name>.avro` file for each table in your database.

To export Avro files, your Dataproc Metastore service can use the MySQL or Spanner database type.

### MySQL

MySQL based exports are supported for all versions of Hive. When you export MySQL files, Dataproc Metastore creates a single SQL file that contains all your table information.

To export MySQL files, your Dataproc Metastore service must use the MySQL database type. The Spanner database type doesn't support MySQL imports.

## Before you begin

  * [Enable Dataproc Metastore](https://docs.cloud.google.com/dataproc-metastore/docs/enable-service) in your project.
  * [Understand networking requirements](https://docs.cloud.google.com/dataproc-metastore/docs/access-service) specific to your project.
  * [Create a Dataproc Metastore service](https://docs.cloud.google.com/dataproc-metastore/docs/create-service).



### Required roles

To get the permissions that you need to export metadata into Dataproc Metastore, ask your administrator to grant you the following IAM roles: 

  * To export metadata, either: 
    * [Dataproc Metastore Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`) on the Dataproc Metastore service
    * [Dataproc Metastore Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`) on the Dataproc Metastore service
    * [Dataproc Metastore Metadata Operator ](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.metadataOperator) (`roles/metastore.metadataOperator`) on the Dataproc Metastore service
  * For MySQL and Avro, to use the Cloud Storage object for export: [grant your user account and the Dataproc Metastore service agent the Storage Creator role ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectCreator) (`roles/storage.objectCreator`) on the Cloud Storage bucket 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to export metadata into Dataproc Metastore. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to export metadata into Dataproc Metastore:

  * To export metadata: `metastore.services.export` on the metastore service 
  * For MySQL and Avro, to use the Cloud Storage object for export, grant your user account and the Dataproc Metastore service agent: `storage.objects.create` on the Cloud Storage bucket 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about specific Dataproc Metastore roles and permissions, see [Dataproc Metastore IAM overview](https://docs.cloud.google.com/dataproc-metastore/docs/iam-and-access-control). 

## Export metadata

Before exporting your metadata, note the following considerations:

  * While an export is running, you can't update a Dataproc Metastore service — for example changing configuration settings. However, you can still use it for normal operations, such as using it to access its metadata from attached Managed Service for Apache Spark or self-managed clusters.
  * The metadata export feature only exports metadata. Data that's created by Apache Hive in internal tables isn't replicated in the export.



To export metadata from a Dataproc Metastore service, perform the following steps.

### Console

  1. In the Google Cloud console, open the **Dataproc Metastore** page:

[Open Dataproc Metastore](https://console.cloud.google.com/dataproc/metastore/services)

  2. On the **Dataproc Metastore** page, click the name of the service you want to export metadata from.

The **Service detail** page opens.

![Service detail page](https://docs.cloud.google.com/static/dataproc-metastore/images/service-detail-page.png) Dataproc Metastore Service detail page 
  3. In the navigation bar, click **Export**.

The **Export metadata** page opens.

  4. In the **Destination** section, choose either **MySQL** or **Avro**.

  5. In the **Destination URI** field, click **Browse** and select the **Cloud Storage URI** where you want to export your files to.

You can also enter your bucket location in the provided text field. Use the following format: `bucket/object` or `bucket/folder/object`.

**Note:** To store your exported metadata, the export job creates a new subfolder in your **Cloud Storage URI** destination.
  6. To start the export, click **Submit**.

When finished, your export appears in a table on the **Service detail** page on the **Import/Export** tab.

When the export completes, Dataproc Metastore automatically returns to the [active state](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#state), regardless of whether or not the export succeeded.




### gcloud CLI

  1. To export metadata from a service, run the following [`gcloud metastore services export gcs`](https://docs.cloud.google.com/sdk/gcloud/reference/metastore/services/export/gcs) command:
         
         gcloud metastore services export gcs SERVICE \
             --location=LOCATION \
             --destination-folder=gs://bucket-name/path/to/folder \
             --dump-type=DUMP_TYPE
         

Replace the following:

     * `SERVICE`: the name of your Dataproc Metastore service.
     * `LOCATION`: the Google Cloud region in which your Dataproc Metastore service resides.
     * `bucket-name/path/to/folder`: the Cloud Storage destination folder where you want to store your export.
     * `DUMP_TYPE`: the type of database dump to be generated by the export. Accepted values include `mysql` and `avro`. The default value is `mysql`.
  2. Verify that the export was successful.

When the export completes, Dataproc Metastore automatically returns to the [active state](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#state), regardless of whether or not the export succeeded.




### REST

Follow the API instructions to [export metadata into a service](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services/exportMetadata) by using the APIs Explorer.

When the export completes, the service automatically returns to the [active state](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#state), regardless of whether or not it succeeded.

### View export history

To view the export history of a Dataproc Metastore service in the Google Cloud console, complete the following steps:

  1. In the Google Cloud console, open the [**Dataproc Metastore**](https://console.cloud.google.com/dataproc/metastore/services) page.
  2. In the navigation bar, click **Import/Export**.

Your export history appears in the **Export history** table.

The history displays up to the last 25 exports.




Deleting a Dataproc Metastore service also deletes all associated export history.

## Troubleshoot common issues

Some common issues include the following:

  * [The service agent or user account doesn't have necessary permissions](https://docs.cloud.google.com/dataproc-metastore/docs/troubleshooting#service-agent-or-user-permissions).
  * [Job fails because the database file is too large](https://docs.cloud.google.com/dataproc-metastore/docs/troubleshooting#job-failed-database-file-size).



For more help solving common troubleshooting issues, see [Import and export error scenarios](https://docs.cloud.google.com/dataproc-metastore/docs/troubleshooting#import-and-export-error-scenarios).

## What's next

  * [Import metadata into a service](https://docs.cloud.google.com/dataproc-metastore/docs/import-metadata)
  * [Update and delete a service](https://docs.cloud.google.com/dataproc-metastore/docs/manage-service)
  * [Hive Metastore](https://docs.cloud.google.com/dataproc-metastore/docs/hive-metastore)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
