---
url: https://docs.cloud.google.com/alloydb/docs/sync-bigquery-iceberg-data/
title: Sync BigQuery data to AlloyDB \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:21:04.661416+00:00
---

# Sync BigQuery data to AlloyDB  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/sync-bigquery-iceberg-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Sync BigQuery data to AlloyDB Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

For information about access to this release, see the [ access request page](https://forms.gle/qoq87WBbnTvmegTN9). 

**Note:** The sync data feature is supported for PostgreSQL version 18 only.

This page shows you how to sync tables from BigQuery into your AlloyDB for PostgreSQL instance.

By syncing analytical data from BigQuery into AlloyDB, you can build operational systems that benefit from low-latency, transactional access to your data lake. Unlike a [foreign data wrapper (FDW)](https://docs.cloud.google.com/alloydb/docs/bigquery-view-alloydb-overview) which queries data in place, sync table moves the data into AlloyDB storage for maximum performance.

AlloyDB provides the following ways to move BigQuery data into your instance:

  * **One-time sync:** creates a writable, independent copy of your BigQuery table.

  * **Periodic sync (mirroring):** creates a read-only local table that automatically refreshes on a schedule—for example, every 6 hours or daily.




## Performance and operational considerations

When you use BigQuery sync tables, consider the following:

  * Resource usage: data movement consumes CPU and memory. For very large tables, consider scheduling syncs during off-peak hours to avoid affecting your primary transactional workload.
  * Data visibility: during a replace operation, the existing target table is dropped and recreated upfront. Queries during the import see an empty table initially, followed by newly imported data appearing incrementally as batch transactions commit.



## Before you begin

  1. Familiarize yourself with how the `bigquery_fdw` handles BigQuery data types and column mappings, because the `alloydb_sync` extension uses `bigquery_fdw` to connect to BigQuery.

  2. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  3. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Cloud APIs necessary to create and connect to AlloyDB.

[Enable the APIs](https://console.cloud.google.com/flows/enableapi?apiid=alloydb.googleapis.com,compute.googleapis.com,cloudresourcemanager.googleapis.com,servicenetworking.googleapis.com,bigquerystorage.googleapis.com)

  8. To confirm the name of the project you are going to make changes to, in the **Confirm project** step, click **Next**.

  9. In the **Enable APIs** step, click **Enable** to enable the following:

     * AlloyDB API
     * Compute Engine API
     * Cloud Resource Manager API
     * Service Networking API
     * BigQuery Storage API

The Service Networking API is required if you plan to configure network connectivity to AlloyDB using a VPC network that resides in the same Google Cloud project as AlloyDB. 

The Compute Engine API and Cloud Resource Manager API are required if you plan to configure network connectivity to AlloyDB using a VPC network that resides in a different Google Cloud project.

  10. Ensure you have an existing BigQuery table to sync data from. For more information, see [Create and use BigQuery tables](https://docs.cloud.google.com/bigquery/docs/tables).



### Required roles

To grant the BigQuery dataset access to the AlloyDB cluster service account, you need the following permissions:

  * BigQuery Data Viewer ([`roles/bigquery.dataViewer`](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.dataViewer)) or any custom role with permissions `bigquery.tables.get` and `bigquery.tables.getData`. When granted on a service account, this role provides permissions to read data and metadata from the table or view.
  * BigQuery Read Session User ([`roles/bigquery.readSessionUser`](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.readSessionUser)) or any custom role with permissions `bigquery.readsessions.create` and `bigquery.readsessions.getData`. Provides the ability to create and use read sessions.
  * BigQuery Job User ([`roles/bigquery.jobUser`](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.jobUser)) or any custom role with permissions `bigquery.jobs.create`. Provides the ability to create and run jobs, including query jobs. When you provide a separate runtime project, the job is run in that project instead of in the data project. This means that you must grant the Job User role on the runtime project.



### Configure the extension

Before you sync tables from BigQuery, enable the required extension and configure the connection to BigQuery. If you use the Google Cloud console, AlloyDB performs these steps automatically.

  1. Create the extension.

     1. Connect to the AlloyDB instance using the psql client by following the instructions in [Connect a psql client to an instance](https://docs.cloud.google.com/alloydb/docs/connect-psql).
     2. Run the following command:
            
            CREATE EXTENSION IF NOT EXISTS alloydb_sync;
            

**Note:** You must create these extensions in every database where you want to sync BigQuery data.
  2. To let AlloyDB authenticate with BigQuery, create the user mapping.
         
         CREATE EXTENSION IF NOT EXISTS bigquery_fdw;
         CREATE SERVER IF NOT EXISTS BIGQUERY_SERVER_NAME FOREIGN DATA WRAPPER bigquery_fdw
           OPTIONS (runtime_project 'RUNTIME_PROJECT_ID');
         CREATE USER MAPPING IF NOT EXISTS FOR USER SERVER BIGQUERY_SERVER_NAME;
         

Replace the following:

     * `USER`: a database username or an IAM user that accesses the BigQuery table.
     * `BIGQUERY_SERVER_NAME`: unique identifier for the BigQuery server. Define this once in a given database. You can replace `BIGQUERY_SERVER_NAME` with your server name.
     * `RUNTIME_PROJECT_ID`: optional. The ID of the Google Cloud project that processes the query and accrues compute costs. If omitted, the queries are billed to the project that stores the data.



## Sync a BigQuery table for one-time export

You can sync a BigQuery table for one-time export using the Google Cloud console or by using [psql](https://docs.cloud.google.com/alloydb/docs/connect-psql).

### Use the Google Cloud console

To sync a BigQuery table to AlloyDB using the Google Cloud console, do the following:

  1. Open the BigQuery page in the Google Cloud console.

[Go to the BigQuery page](https://console.cloud.google.com/bigquery)

  2. In the left pane, click explore **Explorer** :

If you don't see the left pane, click last_page **Expand left pane** to open the pane.

  3. In the **Explorer** pane, expand your project, click **Datasets** , and then click your dataset.

  4. Click **Overview** > **Tables** , and then select a table.

  5. In the details pane, click upload **Export / sync** > **AlloyDB (Export once or sync)**.

  6. Under **Choose a project** , select the project for your AlloyDB cluster. If you have the required permissions, you can select a project other than your current BigQuery project.

  7. Under **Choose a target cluster** , select one of the following options:

     * Select **Use an existing cluster** to export the BigQuery table to an existing AlloyDB cluster. Then, do the following:

       1. Select the primary AlloyDB cluster.

       2. Select the destination AlloyDB database.

       3. Select the schema for your destination AlloyDB table.

       4. Specify a name for your destination AlloyDB table.

       5. For **Sync frequency** , select **Just once** to create a copy of the BigQuery table.

       6. Click **Setup export**.

When the sync setup is complete, you can use the provided SQL statements to track the import job and query the imported tables. Click **Query** to be directed to your imported table in AlloyDB studio.

     * Select **Create a new cluster** to export the BigQuery table to a new AlloyDB cluster. Then, do the following:

       1. Click **Setup export**.

       2. In the **Redirect to AlloyDB** dialog, select **Redirect**.

       3. Select a cluster type, either **Free trial cluster** or **Provisioned cluster**.

       4. Click **Continue**.

       5. In **Sync Configuration** , select the default `postgres` destination AlloyDB database, the default `public` schema for your destination AlloyDB table, and specify a name for your destination AlloyDB table.

For **Sync frequency** , select **Just once** to create a copy of the BigQuery table.

       6. Click **Continue**.

       7. Configure your cluster. For more information about each field, see [Create a new cluster and primary instance](https://docs.cloud.google.com/alloydb/docs/cluster-create#procedure).

       8. Click **Create cluster**.

When the sync setup is complete, navigate to AlloyDB studio to query your imported tables.




### Sync a BigQuery table one-time using psql

**Note:** The `alloydb_sync.import_bq_table()` function creates a writable AlloyDB table that doesn't refresh data from BigQuery automatically.

To create an editable copy of BigQuery data, use [psql](https://docs.cloud.google.com/alloydb/docs/connect-psql) to run the `alloydb_sync.import_bq_table` function.
    
    
    SELECT alloydb_sync.import_bq_table(
      'PROJECT_ID.DATASET_ID.TABLE_ID',
      'ALLOYDB_DESTINATION_TABLE_NAME',
      'ON_EXISTS',
      ARRAY['PRIMARY_KEY_COLUMN']
    );
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the BigQuery dataset resides.
  * `DATASET_ID`: the name of the BigQuery dataset for the table. For Iceberg tables with a 4-part name, this is the `Catalog.Namespace`.
  * `TABLE_ID`: the name of the BigQuery table or view.
  * `ALLOYDB_DESTINATION_TABLE_NAME`: the name of the local table in the AlloyDB database to create and import data into. You can include the schema name—for example, `public.local_sales`.
  * `ON_EXISTS`: the strategy to use if the destination table already exists.
  * `PRIMARY_KEY_COLUMN`: an optional list of column names to use as the primary key.



#### Example

The following example shows how to sync a table named `transactions` from a BigQuery dataset into a new AlloyDB table named `public.local_sales`:
    
    
    SELECT alloydb_sync.import_bq_table(
        'my-gcp-project.sales_data.transactions',
        'public.local_sales',
        'replace'
    );
    

##### `on_exists` parameter

The `on_exists` parameter determines how the function handles the sync if the destination table already exists in AlloyDB:

  * `error`: the default option. Stops the sync if the destination table already exists.
  * `skip`: skips the sync if the destination table already exists.
  * `replace`: replaces the existing local table with fresh data from BigQuery.



##### Primary key support

If you provide the optional `primary_key` parameter as a text array, AlloyDB creates the table with the specified columns as the primary key.
    
    
    SELECT alloydb_sync.import_bq_table(
        'my-gcp-project.sales_data.transactions',
        'public.local_sales',
        ARRAY['transaction_id']
    );
    

## Sync a BigQuery table for periodic export

You can sync a BigQuery table for periodic export using the Google Cloud console or by using [psql](https://docs.cloud.google.com/alloydb/docs/connect-psql).

### Use the Google Cloud console

To sync a BigQuery table to AlloyDB using the Google Cloud console, do the following:

  1. Open the BigQuery page in the Google Cloud console.

[Go to the BigQuery page](https://console.cloud.google.com/bigquery)

  2. In the left pane, click explore **Explorer** :

![Highlighted button for the Explorer pane.](https://docs.cloud.google.com/static/bigquery/images/explorer-tab.png)

If you don't see the left pane, click last_page **Expand left pane** to open the pane.

  3. In the **Explorer** pane, expand your project, click **Datasets** , and then click your dataset.

  4. Click **Overview** > **Tables** , and then select a table.

  5. In the details pane, click upload **Export / sync** > **AlloyDB (Export once or sync)**.

  6. Under **Choose a project** , select the project for your AlloyDB cluster. If you have the required permissions, you can select a project other than your current BigQuery project.

  7. Under **Choose a target cluster** , select one of the following options:

     * Select **Use an existing cluster** to export the BigQuery table to an existing AlloyDB cluster. Then, do the following:

       1. Select the primary AlloyDB cluster.

       2. Select the destination AlloyDB database.

       3. Select the schema for your destination AlloyDB table.

       4. Specify a name for your destination AlloyDB table.

       5. For **Sync frequency** , select a timeframe to create a periodic sync of the BigQuery table.—for example, **Every hour** , **Every six hours**.

       6. Click **Setup export**.

When the sync setup is complete, you can use the provided SQL statements to track the import job and query the imported table. Click **Query** to be directed to your imported table in AlloyDB studio.

     * Select **Create a new cluster** to export the BigQuery table to a new AlloyDB cluster. Then, do the following:

       1. Click **Setup export**.

       2. In the **Redirect to AlloyDB** dialog, select **Redirect**.

       3. Select a cluster type, either **Free trial cluster** or **Provisioned cluster**.

       4. Click **Continue**.

       5. In **Sync Configuration** , select the default `postgres` destination AlloyDB database, the default `public` schema for your destination AlloyDB table, and specify a name for your destination AlloyDB table.

For **Sync frequency** , select **Just once** to create a copy of the BigQuery table.

       6. Click **Continue**.

       7. Configure your cluster. For more information about each field, see [Create a new cluster and primary instance](https://docs.cloud.google.com/alloydb/docs/cluster-create#procedure).

       8. Click **Create cluster**.

When the sync setup is complete, navigate to AlloyDB studio to query your imported tables.




### Create a periodic sync

To maintain a read-only table that stays synced with BigQuery data, use psql to run the `alloydb_sync.create_bq_sync_table` function.
    
    
    SELECT alloydb_sync.create_bq_sync_table(
        'PROJECT_ID.DATASET_ID.TABLE_ID',
        'ALLOYDB_DESTINATION_TABLE_NAME',
        'REFRESH_INTERVAL',
        'ON_EXISTS',
        ARRAY['PRIMARY_KEY_COLUMN']
    );
    

Replace the following:

  * `PROJECT_ID.DATASET_ID.TABLE_ID`: The fully qualified name of the BigQuery table or view, including the project ID, dataset ID, and table ID, separated by periods. For Iceberg tables with a 4-part name, the `DATASET_ID` is represented as `Catalog.Namespace`. For example, `my-gcp-project.sales_data.transactions`.
  * `ALLOYDB_DESTINATION_TABLE_NAME`: the name of the local table in the AlloyDB database to create and sync data into.
  * `REFRESH_INTERVAL`: the interval at which AlloyDB periodically refreshes data from BigQuery—for example, `12 hours`.
  * `ON_EXISTS`: the strategy to use if the destination table already exists.
  * `PRIMARY_KEY_COLUMN`: an optional list of column names to use as the primary key.



#### Example

The following example shows how to create a customer profile mirror that refreshes every 12 hours:
    
    
    SELECT alloydb_sync.create_bq_sync_table(
        'my-gcp-project.crm_data.profiles',
        'public.customer_mirror',
        '12 hours',
        'replace'
    );
    

## Monitor and manage jobs

After you initiate a sync, you can monitor its progress and manage the jobs.

### Check job status

Large syncs can take time. You can monitor progress, including records processed and estimated completion time, by querying the `job_status` view:

**Note:** The `alloydb_sync.import_bq_table()` function returns a job UUID that you can match against the `import_id` in the `alloydb_sync.job_status` view.
    
    
    SELECT
        import_id,
        status,
        records_processed,
        total_records,
        error_message
    FROM alloydb_sync.job_status;
    

For example, to cancel the job, run the following command:
    
    
    SELECT alloydb_sync.cancel_import_job('85bb5dfa-dfb9-4017-9153-738f55abe4b1');
    

### Stop and delete a sync job

To stop mirroring a BigQuery table and delete the local table, use the `alloydb_sync.delete_bq_sync_table` function:
    
    
    SELECT alloydb_sync.delete_bq_sync_table('public.customer_mirror');
    

**Important:** You must use this function instead of standard PostgreSQL `DROP TABLE` commands to delete replicated tables. Dropping a sync table manually without this function does not remove the background scheduler hooks, which can cause the scheduler to continuously encounter errors and drain background worker slots.

## Data type mappings

When you sync or import data from BigQuery to AlloyDB using the `alloydb_sync` extension, AlloyDB maps BigQuery data types to corresponding PostgreSQL data types in your target table.

Verify that your source BigQuery table columns use the following supported data types.

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
  
## Limitations

The following limitations apply when syncing tables from BigQuery:

  * This feature is supported for PostgreSQL version 18 only.
  * If you `DROP` the `alloydb_sync` extension, you must restart the instance before creating the extension again.
  * Syncs run within a transaction. If the import job is interrupted or fails, the system rolls back the imported data.
  * If two users start sync jobs at the same time with the same target tables, the tables might overwrite each other.
  * If any interruption occurs during the initial background import for a newly registered sync table, the table remains incomplete until its next scheduled refresh interval. To resolve this, you can delete the sync table using the `alloydb_sync.delete_bq_sync_table()` function and recreate it.
  * Complex BigQuery types such as `ARRAY`, `BYTES`, `VECTOR`, and `GEOGRAPHY` aren't supported for synchronization. For a full list, see the supported BigQuery data types and column mappings.
  * Don't manually drop a replicated table. Use the `alloydb_sync.delete_bq_sync_table()` API function to safely drop the table and refreshes.
  * To drop a database that uses the `alloydb_sync` extension, you must use `DROP DATABASE ... WITH (FORCE)`.
  * If the Postgres database crashes while an import is running, the metadata might become stuck in the `RUNNING` state, blocking future imports. You must manually run `UPDATE alloydb_sync.import_job_status SET status = 'FAILED' WHERE status = 'RUNNING';` to unblock it.



## Pricing

When you sync data from BigQuery to AlloyDB, you are billed using [BigQuery streaming reads (Storage Read API) pricing](https://docs.cloud.google.com/bigquery/pricing#data-extraction-pricing).

After the data is exported, you're charged for storing the data in AlloyDB. For more information, see [AlloyDB for PostgreSQL pricing](https://docs.cloud.google.com/alloydb/pricing).

## What's next

  * Learn more about [Export data to AlloyDB (reverse ETL)](https://docs.cloud.google.com/bigquery/docs/export-to-alloydb).
  * Learn more about [querying BigQuery data in-place using FDW](https://docs.cloud.google.com/alloydb/docs/bigquery-view-alloydb-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
