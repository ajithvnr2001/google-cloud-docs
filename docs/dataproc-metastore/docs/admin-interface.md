---
url: https://docs.cloud.google.com/dataproc-metastore/docs/admin-interface/
title: Dataproc Metastore administrator interface \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:39:58.405586+00:00
---

# Dataproc Metastore administrator interface  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataproc-metastore/docs/admin-interface/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataproc Metastore ](https://docs.cloud.google.com/dataproc-metastore/docs)
  * [ Guides ](https://docs.cloud.google.com/dataproc-metastore/docs/create-service-cluster)



Send feedback 

#  Dataproc Metastore administrator interface Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to use the Dataproc Metastore administrator interface.

The administrator interface provides you with a centralized tool to inspect and manage the metadata stored in your Dataproc Metastore service, all without having to connect to a Managed Service for Apache Spark cluster or a Hive instance. Instead, you can manage your metadata with the Google Cloud CLI or Dataproc Metastore APIs.

For example, by using the administrator interface, you can run a SQL query directly on your backend metadata to fetch a specific table name. This process involves following fewer steps than the typical workflow, such as creating a Managed Service for Apache Spark cluster, connecting to the cluster using SSH, starting a Hive instance, and then finally running a query (for example, `SELECT * FROM table_name`).

As a result, the administrator interface can help you save time and help decrease the amount of Google Cloud resources required to retrieve your data.

## Before you begin

  * [Enable Dataproc Metastore](https://docs.cloud.google.com/dataproc-metastore/docs/enable-service) in your project.
  * [Create a Dataproc Metastore service](https://docs.cloud.google.com/dataproc-metastore/docs/create-service).
  * [Import metadata into Dataproc Metastore](https://docs.cloud.google.com/dataproc-metastore/docs/import-metadata).



### Required roles

To get the permissions that you need to use the Dataproc Metastore administrator interface, ask your administrator to grant you the following IAM roles on your project, based on the principle of least privilege: 

  * To query Dataproc Metastore metadata: Metadata query administrator (`roles/metastore.metadataQueryAdmin`) on the user account or service account 
  * To alter the resource location of your metadata, including databases, tables and partitions, or move a table to another database: 
    * Metadata mutate administrator (`roles/metastore.metadataMutateAdmin`) on the user account or service account 
    * Dataproc Metastore Editor (`roles/metastore.editor`) on the user account or service account 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to use the Dataproc Metastore administrator interface. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to use the Dataproc Metastore administrator interface:

  * To query Dataproc Metastore metadata: `metastore.services.queryMetadata`
  * To alter or move Dataproc Metastore tables: `metastore.services.mutateMetadata`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about specific Dataproc Metastore roles and permissions, see [Dataproc Metastore Identity and Access Management overview](https://docs.cloud.google.com/dataproc-metastore/docs/iam-and-access-control). 

## Supported administrator operations

You can only run administrator interface operations by using the gcloud CLI or the Dataproc Metastore APIs. Administrator interface operations aren't supported in the Google Cloud console.

The administrator interface supports the following operations.

  * **Read-only operations.**

    * Query metadata.
**Warning:** Only run read-only queries interactively. Don't automate or run non-interactive read-only queries on production-critical processes. Running non-interactive queries can cause problems if the underlying database schema changes without notice.
  * **Read and write operations.**

    * Alter the resource location of your metadata, including databases, tables and partitions.
    * Alter table properties, such as custom key-value pairs.
    * Move a table to another database.



If the administrator interface doesn't support a different operation, you can [query the Hive metastore directly](https://github.com/apache/hive/blob/d06452c283df741fe51d2411d81f5eb2f8f640b0/standalone-metastore/metastore-server/src/main/sql/hive/hive-schema-3.0.0.hive.sql#L80). For example, to list all tables in a Dataproc Metastore instance, you can query the Hive metastore schema directly. In this case, you can run `select * from TBLS` to list all tables stored in your service.

## Query metadata

This operation lets you look up metadata information in your database using SQL queries. After you run a query, the results are dumped into your [artifacts Google Cloud bucket](https://docs.cloud.google.com/dataproc-metastore/docs/hive-metastore#create-bucket).

Before running this operation, note the following considerations:

  * Supported operations only include `read-only` MySQL or Spanner queries. If the query tries to modify the data, the operation fails.
  * The output file contains a maximum of 1000 rows. This configuration can't be changed.
  * The output files aren't automatically deleted. Instead, you must manually delete them from your Google Cloud bucket. If you don't delete them, you might incur extra storage costs.




###  gcloud CLI 

  1. To query metadata, run the following [`gcloud metastore services query-metadata`](https://docs.cloud.google.com/sdk/gcloud/reference/metastore/services/query-metadata) command:
         
         gcloud metastore services query-metadata SERVICE \
           --location=LOCATION \
           --query=QUERY

Replace the following:

     * `SERVICE`: the name of your Dataproc Metastore service.
     * `LOCATION`: the Google Cloud region that your Dataproc Metastore service resides in.
     * `QUERY`: the SQL query to target your metadata. 
       * If you're using a MySQL database, use a regular MySQL query.
       * If you're using a Spanner database, use a [GoogleSQL query](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/query-syntax).
  2. View the output file in your [artifacts Google Cloud bucket](https://docs.cloud.google.com/dataproc-metastore/docs/hive-metastore#create-bucket).




### REST

**Note:** The following command assumes that you've logged in to the gcloud CLI with your user account. You can log in by running [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login), or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the gcloud CLI. You can check the active account by executing [gcloud auth list](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list).
    
    
    curl -X POST -s -i \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -X POST -d '{"query": "QUERY"}' \
      -H "Content-Type:application/json" \
      https://metastore.googleapis.com/projects/PROJECT_ID/locations/LOCATION/services/SERVICE:queryMetadata
    

Replace the following:

  * `QUERY`: the SQL query you're using to target your metadata. 
    * If you're using a MySQL database, use a regular MySQL query.
    * If you're using a Spanner database, use a [GoogleSQL query](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/query-syntax).
  * `PROJECT_ID`: the Google Cloud project ID that your Dataproc Metastore service resides in.
  * `SERVICE`: the name of your Dataproc Metastore service.
  * `LOCATION`: the region that your Dataproc Metastore resides in.



The following example shows a sample command that runs a `select *` query from a database named DBS.
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" -X POST -d  '{"query": "select * from DBS;"}' \
      https://metastore.googleapis.com/projects/dpms/locations/us-central1/services/dpms1:queryMetadata
    

### Interpret the output of a query metadata operation

When you first run a query metadata command, Dataproc Metastore automatically creates a Google Cloud folder in your artifacts Google Cloud bucket. This folder is named `query-results`. After every successful query execution (API call), a new folder is created inside the `query-results` folder (which is named with a randomly generated UUID).

Each new folder contains a `result manifest` file with your query results. The location of this folder is returned in the response of your API call.

For example, in the response, the `resultManifestUri` field contains the location of the file.
    
    
    "response": {
        "@type": "type.googleapis.com/google.cloud.metastore.QueryMetadataResponse",
        "resultManifestUri": "gs://gcs-bucket-6a3638b8-e319-46363-ad33-e632a5e/query-results/800156f5-2d13-4b80-bec3-2345a9e880f6/result-manifest"
      }
    

The output of the `result manifest` file is similar to the following:
    
    
    {
      "status": {
        "code": 0,
        "message": "Query results are successfully uploaded to cloud storage",
        "details": []
      },
      "filenames": ["result-001"]
    }
    

Result manifest file details:

  * The `status` field shows whether the query was a success or failure.
  * If the query execution is successful, the `filenames` field lists all the files created. These files are in the same folder as the `result manifest` file.
  * If the query resulted in a failure, the `details` field shows the error message.

**Note:** By default, the output files don't have a TTL (Time to live). You must manually delete them from your Google Cloud bucket or create a custom TTL rule on the `query-results` folder. If you don't delete them, you might incur extra storage costs.

## Alter the resource location of your metadata

This operation lets you alter the resource location of a database, table, or partition.

When you run this command, it only updates the parent directory or the respective metadata resource. This command doesn't transfer any existing data to the new location.

###  gcloud CLI 

  1. To alter the resource location of metadata, run the following [`gcloud metastore services alter-metadata-resource-location`](https://docs.cloud.google.com/sdk/gcloud/reference/metastore/services/alter-metadata-resource-location) command:
         
         gcloud metastore services alter-metadata-resource-location SERVICE \
           --location=LOCATION \
           --resource_name=RESOURCE_NAME \
           --location_uri=LOCATION_URI

Replace the following:

     * `SERVICE`: the name of your Dataproc Metastore service.
     * `LOCATION`: the Google Cloud region that your Dataproc Metastore service resides in.
     * `RESOURCE_NAME`: the name of the database, table, or partition you're altering.
     * `LOCATION_URI`: the new Cloud Storage Path for the contents of `RESOURCE_NAME`. This value is the path that you're moving your metadata resource location to. This path must begin with `gs://`. For example, `gs://bucket/object`.
  2. Verify that the resource location change was successful.




### REST

**Note:** The following command assumes that you've logged in to the gcloud CLI with your user account. You can sign in by executing [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login), or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which checks the active account by executing [gcloud auth list](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list).
    
    
    curl -X POST -s -i \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      POST -d '{"resource_name": "RESOURCE_NAME", "location_uri":"LOCATION_URI"}' \
      -H "Content-Type:application/json" \
      https://metastore.googleapis.com/projects/PROJECT_ID/locations/LOCATION/services/SERVICE:alterLocation
    

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID that your Dataproc Metastore service resides in.
  * `SERVICE`: the name of your Dataproc Metastore service.
  * `LOCATION`: the region that your Dataproc Metastore resides in.
  * `RESOURCE_NAME`: the name of the database, table, or partition you're altering.
  * `LOCATION_URI`: the new Cloud Storage Path for the contents of `RESOURCE_NAME`. This value is the path that you're moving your metadata resource location to. This path must begin with `gs://`. For example, `gs://bucket/object`.



The following example shows a sample command that moves a table called `test-table2` to a new Cloud Storage bucket.
    
    
     curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
       -H "Content-Type: application/json" \
       -X POST -d  '{"resource_name": "databases/testdb1/tables/test-table2",
       "location_uri":"gs://gcs-bucket-dpms1-9425bd83-b794-4f1c-9e79-2d833f758cc1/empty"}'
       https://metastore.googleapis.com/projects/dpms/locations/us-central1/services/dpms1:alterLocation
    

## Alter table properties

This operation lets you alter the properties of a table, such as a custom key-value pair that you're using to store data. For example, you can change a key-value pair of `properties.customerID_1` to `properties.customerID_2`.

###  gcloud CLI 

  1. To alter table properties, run the following [`gcloud metastore services alter-table-properties`](https://docs.cloud.google.com/sdk/gcloud/reference/metastore/services/alter-table-properties) command:
         
         gcloud metastore services alter-table-properties SERVICE \
           --location=LOCATION \
           --table-name=TABLE_NAME \
           --update-mask=UPDATE_MASK \
           --properties=PROPERTIES

Replace the following:

     * `SERVICE`: the name of your Dataproc Metastore service.
     * `LOCATION`: the Google Cloud region that your Dataproc Metastore service resides in.
     * `TABLE_NAME`: the name of the table containing the properties you're altering in the following format, `databases/{database_id}/tables/{table_id}`.
     * `UPDATE_MASK`: the existing property values you're updating. Use a comma separated list to describe the key-value pairs for example, `properties.1,properties.2,properties.3,...`.
     * `PROPERTIES`: the new properties for your table. Use a comma separated list to describe the key-value pairs. For example, `a=1,b=2,c=3,...`. The values you list here overwrite the values in `UPDATE_MASK`.



### REST

**Note:** The following command assumes that you've logged in to the gcloud CLI with your user account. You can log in by executing [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login), or by using [Cloud Shell](https://cloud.google.com/shell/docs), which automatically logs you into the gcloud CLI. You can check the active account by executing [gcloud auth list](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list).
    
    
    curl -X POST -s -i \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      POST -d '{"table_name": "TABLE_NAME", "update_mask":"UPDATE_MASK", "properties":PROPERTIES}'\
      -H "Content-Type:application/json" \
      https://metastore.googleapis.com/projects/PROJECT_ID/locations/LOCATION/services/SERVICE:alterTableProperties
    

Replace the following:

  * `SERVICE`: the name of your Dataproc Metastore service.
  * `LOCATION`: the Google Cloud region that your Dataproc Metastore service resides in.
  * `TABLE_NAME`: the name of the table containing the properties you're altering in the following format, `databases/{database_id}/tables/{table_id}`.
  * `UPDATE_MASK`: the existing property values you're updating. Use a comma separated list to describe the key-value pairs for example, `properties.1,properties.2,properties.3,...`.
  * `PROPERTIES`: the new properties for your table. Use a comma separated list to describe the key-value pairs for example, `a=1,b=2,c=3,...`. The values that you list here overwrite the values in `UPDATE_MASK`.



The following example shows a sample command that alters the table properties of a table called `test-table`. In this example the existing key-value pair, `properties.customerID_1` is updated to the new value `properties.customerID_2`
    
    
      curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
       -H "Content-Type: application/json"
       -X POST -d  '{"table_name": "databases/default/tables/test-table", "update_mask":{"paths":"properties.customerID_1"}, "properties":{"customerID_1":"customerID_2"}}' https://metastore.googleapis.com/projects/dpms-p
    

## Move a table to another database

This operation lets you move an internal table (managed table) to another database. In this case, both the database parent directory and its data are moved.

You can't move data stored in external tables.

###  gcloud CLI 

  1. To move a table to another database, run the following [`gcloud metastore services move-table-to-database`](https://docs.cloud.google.com/sdk/gcloud/reference/metastore/services/move-table-to-database) command:
         
         gcloud metastore services move-table-to-database SERVICE \
           --location=LOCATION \
           --db_name=DB_NAME \
           --table_name=TABLE_NAME \
           --destination_db_name=DESTINATION_DB_NAME

Replace the following:

     * `SERVICE`: the name of your Dataproc Metastore service.
     * `LOCATION`: the Google Cloud region that your Dataproc Metastore service resides in.
     * `DB_NAME`: the name of the source database that contains the table you want to move.
     * `TABLE_NAME`: the name of the table that you want to move.
     * `DESTINATION_DB_NAME`: the name of the new database that you want to move the table to.
  2. Verify that the table change was successful.




### REST

**Note:** The following command assumes that you've logged in to the gcloud CLI with your user account. You can log in by executing [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login), or by using [Cloud Shell](https://cloud.google.com/shell/docs), which automatically logs you into the gcloud CLI. You can check the active account by executing [gcloud auth list](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list).
    
    
    curl -X POST -s -i \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      POST -d '{"table_name": "TABLE_NAME", "db_name": "DB_NAME", "destination_db_name": "DESTINATION_DB_NAME"}'\
      -H "Content-Type:application/json" \
      https://metastore.googleapis.com/projects/PROJECT_ID/locations/LOCATION/services/SERVICE:moveTableToDatabase
    

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID that your Dataproc Metastore service resides in.
  * `SERVICE`: the name of your Dataproc Metastore service.
  * `LOCATION`: the region that your Dataproc Metastore resides in.
  * `DB_NAME`: the name of the source database that contains the table you want to move.
  * `TABLE_NAME`: the name of the table that you want to move.
  * `DESTINATION_DB_NAME`: the name of the new database that you want to move the table to.



The following example shows a sample command that moves a database called `testdb1` to a different database called `testdb2`.
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
     -H "Content-Type: application/json"
     -X POST -d  '{"table_name": "testtb1", "db_name": "testdb1",
     "destination_db_name": "testdb2"}' https://metastore.googleapis.com/projects/dpms/locations/asia-northeast2/services/dpms1:moveTableToDatabase
    

## What's next

  * [Export metadata](https://docs.cloud.google.com/dataproc-metastore/docs/export-metadata)
  * [Update a metastore](https://docs.cloud.google.com/dataproc-metastore/docs/manage-service)
  * [Back up a metastore](https://docs.cloud.google.com/dataproc-metastore/docs/backup-metadata)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
