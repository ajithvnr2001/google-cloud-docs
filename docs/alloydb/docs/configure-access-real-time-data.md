---
url: https://docs.cloud.google.com/alloydb/docs/configure-access-real-time-data/
title: Configure AlloyDB access to real-time data in BigQuery \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:46:36.691681+00:00
---

# Configure AlloyDB access to real-time data in BigQuery  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/configure-access-real-time-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Configure AlloyDB access to real-time data in BigQuery Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to implement _lakehouse federation_ , a capability that lets you query live data in BigQuery directly from AlloyDB without performing complex ETL (extract, transform, load) migrations. Lakehouse federation unifies your operational and analytical data stores, eliminating the need for complex and error-prone data pipelines. For more information, see [Access to real-time data overview](https://docs.cloud.google.com/alloydb/docs/access-real-time-data-overview).

By integrating AlloyDB and BigQuery, you can achieve a seamless flow of data between your transactional database and your data warehouse, which supports real-time analytics and helps you build powerful interactive applications.

You can use this integration to run queries in AlloyDB that access BigQuery data in real time. You can perform joins between tables in AlloyDB and foreign tables that reference your BigQuery datasets. This is useful when you need the most current data from BigQuery without moving it.

This page assumes that you have an [AlloyDB cluster and primary instance](https://docs.cloud.google.com/alloydb/docs/cluster-create), and that you have a BigQuery dataset and tables. For more information, see [Create datasets](https://docs.cloud.google.com/bigquery/docs/datasets) and [Create and use tables](https://docs.cloud.google.com/bigquery/docs/tables).

## Before you begin

**Note:** If you use the Google Cloud console to connect BigQuery tables, the console automatically enables the required APIs and grants the required permissions to the cluster service account. 

  1. Enable the [ `bigquery_fdw.enabled` flag](https://docs.cloud.google.com/alloydb/docs/instance-configure-database-flags) on the AlloyDB for PostgreSQL instance.
  2. Familiarize yourself with supported data types.

  3. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Enable the AlloyDB, Compute Engine, Resource Manager, and BigQuery APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=alloydb.googleapis.com,compute.googleapis.com,cloudresourcemanager.googleapis.com)

  7. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. Enable the AlloyDB, Compute Engine, Resource Manager, and BigQuery APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=alloydb.googleapis.com,compute.googleapis.com,cloudresourcemanager.googleapis.com)

  10. Enable the Cloud APIs necessary to create and connect to AlloyDB.

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=alloydb.googleapis.com,compute.googleapis.com,cloudresourcemanager.googleapis.com,servicenetworking.googleapis.com,bigquerystorage.googleapis.com,bigquery.googleapis.com)

  11. In the **Confirm project** step, click **Next** to confirm the name of the project you are going to make changes to.

  12. In the **Enable APIs** step, click **Enable** to enable the following:

     * AlloyDB API
     * Compute Engine API
     * Cloud Resource Manager API
     * Service Networking API
     * BigQuery Storage API
     * BigQuery API

The Service Networking API is required if you plan to configure network connectivity to AlloyDB using a VPC network that resides in the same Google Cloud project as AlloyDB. 

The Compute Engine API and Cloud Resource Manager API are required if you plan to configure network connectivity to AlloyDB using a VPC network that resides in a different Google Cloud project.




### Required roles

To grant read access to the BigQuery Dataset to the AlloyDB cluster service account, you need the following permissions. For more information, see Grant AlloyDB access to the BigQuery dataset.

  * BigQuery Data Viewer ([`roles/bigquery.dataViewer`](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.dataViewer)) or any custom role with permissions `bigquery.tables.get` and `bigquery.tables.getData`. When granted on a table or view, this role provides permissions to read data and metadata from the table or view.
  * BigQuery Read Session User ([`roles/bigquery.readSessionUser`](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.readSessionUser)) or any custom role with permissions `bigquery.readsessions.create` and `bigquery.readsessions.getData`. Provides the ability to create and use read sessions.
  * BigQuery Job User ([`roles/bigquery.jobUser`](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.jobUser)) or any custom role with permissions `bigquery.jobs.create`. Provides permissions to run jobs, including queries, within the project using the BigQuery API. This role can only be granted on Resource Manager resources (projects, folders, and organizations). When you provide a separate runtime project, the job is run in that project instead of in the data project. This means that you must grant the Job User role on the runtime project.



To access BigLake Metastore tables:

  * BigLake Viewer ([`roles/biglake.viewer`](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.viewer)) or any custom role with permissions `biglake.catalogs.get`, `biglake.namespaces.get`, `biglake.tables.get`, and `biglake.tables.getData`. Provides permissions to read BigLake Metastore catalogs, namespaces, and tables.
  * Storage Object Viewer ([`roles/storage.objectViewer`](https://docs.cloud.google.com/storage/docs/access-control/iam-roles#storage.bucketViewer)) or any custom role with permissions `storage.objects.get`. Provides permissions to access BigQuery external tables and read underlying Cloud Storage objects backing BigLake and BigLake Metastore tables. Must be granted at the project or bucket level.



## Grant AlloyDB access to the BigQuery dataset

After you enable the required roles and permissions for lakehouse federation, you must grant the AlloyDB cluster service account access to the BigQuery dataset.

The Google Cloud console automatically grants the required permissions to the cluster service account when you connect a BigQuery table using AlloyDB Studio.

To grant access using gcloud CLI, follow these steps:

###  gcloud 

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

  1. Open the gcloud CLI. If you don't have the gcloud CLI installed, [install and initialize](https://docs.cloud.google.com/sdk/docs/install) the gcloud CLI, or use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

  2. Run the [`gcloud beta alloydb clusters describe`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/alloydb/clusters/describe) command:
         
         gcloud beta alloydb clusters describe CLUSTER --region=REGION

Replace the following:

     * `CLUSTER`: the AlloyDB cluster ID.
     * `REGION`: the location of the AlloyDB cluster, for example, `asia-east1`, `us-east1`. See the full list of regions at [AlloyDB locations](https://docs.cloud.google.com/alloydb/docs/locations).

The output contains a `serviceAccountEmail` field, which is the service account for this cluster. You can also find the service account on the **Cluster overview** page.

  3. Grant the required permissions. For more information, see [Control access to resources with IAM](https://docs.cloud.google.com/bigquery/docs/control-access-to-resources-iam).

If the cluster service account doesn't have the required permissions, the following errors appear when a query is executed against the BigQuery table:

     * `The user does not have bigquery.readsessions.create permissions`
     * `Permission bigquery.tables.get denied on table`
     * `Permission bigquery.tables.getData denied on table`
**Note:** If `bigquery.readsessions.getData` isn't provided, empty results are returned without an error.



## Configure the extension

To configure the extension, follow these steps:

###  Console 

  1. Go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click the ID of the cluster you want to use.

  3. In the navigation menu, click **AlloyDB Studio**.

  4. Sign in to your database.

  5. In the **Explorer** pane, expand the relevant schema.

  6. Click the more_vert**Actions** menu next to **BigQuery Tables** and click **Connect BigQuery table**.

  7. In the **Connect BigQuery table** pane, choose a source project, source dataset, and a table.

  8. The **Review and select columns** table displays the columns from the selected table. Select the columns you want to map.

  9. In the **Table name** field, enter a name for the foreign table.

  10. Optional: Click **View SQL Command** to view the generated command.

  11. Click **Connect table**. A dialog shows the progress. After the process completes, you can query the table like you query any table in AlloyDB.




###  psql 

  1. Create the extension.

     1. Connect to the AlloyDB instance using the psql client by following the instructions in [Connect a psql client to an instance](https://docs.cloud.google.com/alloydb/docs/connect-psql). Or, you can use AlloyDB Studio. For more information, see [Manage your data using the Google Cloud console](https://docs.cloud.google.com/alloydb/docs/manage-data-using-studio).
     2. Run the following command:
            
            CREATE EXTENSION bigquery_fdw;
            

**Note:** You must create this extension in all the databases where BigQuery datasets need to be accessed.
  2. Create a foreign server to define the connection parameters for the remote BigQuery dataset.
         
         CREATE SERVER BIGQUERY_SERVER_NAME FOREIGN DATA WRAPPER bigquery_fdw
           OPTIONS (runtime_project 'RUNTIME_PROJECT_ID');
         

Replace the following:

     * `BIGQUERY_SERVER_NAME`: unique identifier for the foreign server. Define this once in a given database. You can replace `BIGQUERY_SERVER_NAME` with your server name.
     * `RUNTIME_PROJECT_ID`: optional. The ID of the Google Cloud project that processes the query and accrues compute costs. If you omit this ID, the queries are billed to the project that stores the data.
  3. Create the user mapping by running the `CREATE USER MAPPING` command, which maps a local PostgreSQL user that you want to connect to the foreign server.
         
         CREATE USER MAPPING FOR USERNAME SERVER BIGQUERY_SERVER_NAME ;
         

Replace the following:

     * `USERNAME`: a database username or an IAM user that accesses the foreign table.
     * `BIGQUERY_SERVER_NAME`: unique identifier for the foreign server that you created.
  4. Define foreign tables that correspond to the tables that you want to access in BigQuery using the `CREATE FOREIGN TABLE` command. This command lets you define the structure of a remote table. The foreign table can either have all or a subset of the columns in the source table in BigQuery.

**Note:** Make sure that the data type that you're using maps to the supported data types. For more information, see Data type mappings.
         
         CREATE FOREIGN TABLE TABLENAME (
           COLUMN1_NAME DATA_TYPE,
           COLUMN2_NAME DATA_TYPE,
           ...
         ) SERVER BIGQUERY_SERVER_NAME OPTIONS (
           project 'BIGQUERY_PROJECT_ID',
           dataset 'BIGQUERY_DATASET_NAME',
           table 'BIGQUERY_TABLE_NAME',
           runtime_project 'RUNTIME_PROJECT_ID'
         );
         

Replace the following:

     * `TABLENAME`: the name of the foreign table in the local AlloyDB database.
     * `COLUMNX_NAME`: the AlloyDB column name. The column name must exactly match the name of the corresponding column in the BigQuery source table. `X` indicates that the table can be created with multiple columns. The name must also match the exact casing of the BigQuery column. If the BigQuery column name contains uppercase letters (for example, `employeeID`), the AlloyDB identifier must be enclosed in double quotes (for example, `"employeeID"`) to preserve mixed or uppercase letters.
     * `DATA_TYPE`: the data type of the column. When you define the `DATA_TYPE` for each column in your foreign table, verify that it's a compatible PostgreSQL type. For more information about how BigQuery types are converted, see Data type mappings.
     * `BIGQUERY_SERVER_NAME`: unique identifier for the foreign server that you created.
     * `BIGQUERY_PROJECT_ID`: ID of the project where the BigQuery dataset resides.
     * `BIGQUERY_DATASET_NAME`: name of the BigQuery dataset for the table.
     * `BIGQUERY_TABLE_NAME`: name of the BigQuery table.
     * `RUNTIME_PROJECT_ID`: optional. The ID of the Google Cloud project to bill for query execution. Setting this at the table level overrides the runtime project defined at the server level.

After the foreign table is created, you can query this table the same way that you query any table in AlloyDB.




## Data type mappings

Use the following table to learn about data type mappings between BigQuery and AlloyDB. For more information, see [Data type considerations for federated queries](https://docs.cloud.google.com/alloydb/docs/access-real-time-data-overview#data-type-considerations).

The following table lists the data type mappings between BigQuery and AlloyDB. 

BigQuery table [data types](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types) | Recommended PostgreSQL foreign table [data types](https://www.postgresql.org/docs/current/datatype.html)  
---|---  
`BOOLEAN` | `BOOLEAN`  
`INTEGER (INT64)` | `BIGINT`  
`FLOAT (FLOAT64)` | `DOUBLE PRECISION`  
`STRING` | `VARCHAR`  
`NUMERIC` | `NUMERIC(38, 9)`  
`NUMERIC(P[, S])` | `NUMERIC(P, S)`  
`BIGNUMERIC` | `NUMERIC(77, 38)`  
`BIGNUMERIC(P[, S])` | `NUMERIC(P, S)`  
`DATE` | `DATE`  
`TIMESTAMP` | `TIMESTAMPTZ`  
`TIME` | `TIME`  
`JSON` | `JSONB`  
`BYTES` | `BYTEA`  
`GEOGRAPHY` |  `GEOGRAPHY(POINT), ...` For more information, see [PostGIS_Geography](https://postgis.net/docs/using_postgis_dbmanagement.html#PostGIS_Geography).  
`DATETIME` | `TIMESTAMP`  
`ARRAY` |  `VECTOR(N)` `N` is the dimension of the vector. You must set the `bigquery_fdw.enable_vector_downcasting` flag in the session. Because the `VECTOR` type in AlloyDB uses `float4` type, you might experience precision loss in this conversion. For more information, see [`pgvector` extension.](https://github.com/pgvector/pgvector)  
  
## What's next

  * [Choose how to access BigQuery data](https://docs.cloud.google.com/alloydb/docs/choose-access-bigquery-data-from-alloydb).
  * [Access to real-time data overview](https://docs.cloud.google.com/alloydb/docs/access-real-time-data-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
