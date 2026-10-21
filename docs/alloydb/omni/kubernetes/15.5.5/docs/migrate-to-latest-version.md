---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/migrate-to-latest-version/
title: Migrate from AlloyDB Omni version 15.5.2 and earlier to the latest version \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 15.5.5 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:34:28.538614+00:00
---

# Migrate from AlloyDB Omni version 15.5.2 and earlier to the latest version  |  AlloyDB Omni for Kubernetes: 15.5.5  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/migrate-to-latest-version/

This page documents AlloyDB Omni version **15.5.5** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/overview)



Send feedback 

#  Migrate from AlloyDB Omni version 15.5.2 and earlier to the latest version Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.5.5keyboard_arrow_down

  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/migrate-to-latest-version)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/migrate-to-latest-version)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/migrate-to-latest-version)

This page provides instructions for migrating from version 15.5.2 and earlier to the latest version of AlloyDB Omni. 

Starting with AlloyDB Omni 15.5.4, you control AlloyDB Omni with common package-management tools.

If you have an existing installation of AlloyDB Omni, follow the instructions on this page to migrate to the new, single-image installation.

## Prerequisites

Before you can start upgrading to the latest version of AlloyDB Omni, complete the following prerequisites, if you haven't done so already.

### Upgrade to AlloyDB Omni 15.5.2

The latest AlloyDB Omni version that supports the AlloyDB Omni CLI is 15.5.2. To check the version of AlloyDB Omni, run the following command:
    
    
    sudo alloydb version

The output looks similar to the following:
    
    
    AlloyDB Omni CLI version: 1.6
    AlloyDB Omni database server version: 15.5.2
    

If the output displays a database version earlier than 15.5.2, run the following command to upgrade:
    
    
    sudo alloydb database-server upgrade

### Gather information about your existing installation

  1. Run the following command:
         
         cat /var/alloydb/config/dataplane.conf

  2. From the output of the `cat` command, note the values of the following variables for your reference:

     * `DATADIR_PATH`—for example, `/var/alloydb/main`
     * `ENABLE_ALLOYDB_AI`—for example, `FALSE`
     * `PGPORT`—for example, `5432`
     * `INSTANCE_TYPE`—for example, `PRIMARY/READ_REPLICA`



### Drop ScaNN indexes created with `postgres_ann` extension

**Preview — AlloyDB ScaNN index**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The `postgres_ann` extension is renamed to `alloyd_scann`. If you have installed the `postgres_ann` extension and created `ScaNN` indexes using the extension, you must drop all `ScaNN` indexes and uninstall the extension before performing an upgrade.

To handle any impact to your database due to the renaming of the `postgres_ann` extension, complete the following steps:

  1. [Run and connect to AlloyDB Omni.](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/run-connect)
  2. Identify all tables that use the `ScaNN` index.
         
         \c DATABASE_NAME
          select schemaname, relname, indexrelname, indextype, indexconfig, indexsize, indexscan FROM pg_stat_ann_indexes;

Replace `DATABASE_NAME` with the name of the database where you want to run the query.

  3. Save index definitions and parameters as a dump DDL using a utility like `pg_dump` to recreate the `ScaNN` indexes later.
         
         pg_dump -st TABLE_NAME DATABASE_NAME

Replace the following:

     * `DATABASE_NAME`: the name of the database.
     * `TABLE_NAME`: the name of the table.
  4. Drop `ScaNN` Indexes that were created using the `postgres_ann` index.
         
         DROP INDEX INDEX_NAME;

Replace `INDEX_NAME` with the name of the database where you want to run the query.

**Note:** If the index is not successfully dropped before upgrading, then the table will be not used and queried in subsequent query requests. 
  5. Verify that none of your databases include `ScaNN` indexes. Use the following SQL query to verify the deletion: The following sql should return an empty result set.
         
         \c DATABASE_NAME
          select schemaname, relname, indexrelname, indextype, indexconfig, indexsize, indexscan FROM pg_stat_ann_indexes;

  6. Drop the `postgres_ann` extension using the following steps:

     1. Verify that the `postgres_ann` extension is installed in your database.
    
    select * from pg_extension;

     1. Drop the `postgres_ann` extension.
    
    DROP EXTENSION postgres_ann CASCADE;

     1. Verify that the `postgres_ann` extension is no longer installed in your database.
    
    select * from pg_extension;




## Perform an in-place upgrade

  1. Stop the existing database:
         
         sudo alloydb database-server stop

  2. Start the new single-image AlloyDB Omni, mounting your existing data directory from before:
         
         docker run --name CONTAINER_NAME \
             -e POSTGRES_PASSWORD=PASSWORD \
             -e PGDATA=/var/lib/postgresql/data \
             -v /var/alloydb/main/data:/var/lib/postgresql/data \
             -v /dev/shm:/dev/shm \
             -p PGPORT:5432 \
             --network=host \
             --ulimit=nice=-20:-20 \
             --ulimit=core=-1:-1 \
             --log-driver=journald \
             -d google/alloydbomni:15.5.5

Replace the following:

     * `CONTAINER_NAME`: The name to assign this new AlloyDB Omni container in your host machine's container registry—for example, `my-omni`.

     * `PASSWORD`: The password assigned the new container's `postgres` user after its creation.

     * `PGPORT`: The IP address of the port the AlloyDB Omni runs on. This is the value you noted down in step 2 of Gather information about your existing installation.

The arguments to `docker run` are the ones used in earlier versions of AlloyDB Omni, but you may further customize them. See [Customize your AlloyDB Omni installation](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/install) for details.

  3. If your database instance type is `PRIMARY`, run the following command to create the following users. These are usernames which are unused at the moment, but reserved for future extensions.
         
         for name in alloydbagent alloydbexport alloydbiamgroupuser alloydbiamuser alloydbimportexport alloydbobservability alloydbsqllogical alloydbsuperuser; do
           echo docker exec -it CONTAINER_NAME psql -h localhost -U postgres alloydbadmin \
             -c "CREATE ROLE ${name} NOLOGIN;" \
             -c "CREATE TABLE ${name}_table();" \
             -c "ALTER TABLE ${name}_table OWNER TO ${name};"
         done

  4. If `ENABLE_ALLOYDB_AI` is set to `TRUE`, follow instructions in [Install AlloyDB Omni with AlloyDB AI](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/install-with-alloydb-ai) to set up AlloyDB AI.

  5. Connect to the database to verify that the data is unchanged:
         
         docker exec -it CONTAINER_NAME psql -h localhost -U postgres

  6. Uninstall the AlloyDB Omni CLI:
         
         sudo alloydb database-server uninstall

The AlloyDB Omni CLI uninstallation does not affect your data stored in AlloyDB Omni.




## Recreate ScaNN indexes using `alloydb_scann` extension

After you upgrade AlloyDB Omni, the `alloydb_scann` extension is also installed. Complete the following steps to recreate ScaNN indexes that you dropped in the Drop ScaNN indexes created with `postgres_ann` extension section before the upgrade.

  1. Create the `alloydb_scann` extension using the following steps:

     1. To create the `alloydb_scann` extension, run the following query:
    
    create extension alloydb_scann cascade;

     1. Verify that the `alloydb_scann` extension was created successfully. 
    
    select * from pg_extension;

  2. Recreate `ScaNN` index for your table, and then restore the previous `pg_dump` DDL index definitions.

     1. Create `ScaNN` index on the table:
    
    CREATE INDEX INDEX_NAME ON TABLE_NAME
        USING scann (VECTOR_COLUMN DISTANCE)
        WITH (num_leaves = NUM_LEAVES_VALUE);

Replace the following:

     * INDEX_NAME: the name of the index.
     * TABLE_NAME: the name of the table.
     * VECTOR_COLUMN: the name of the column that stores vector data.
     * DISTANCE: the distance function to use with this index.
     * NUM_LEAVES_VALUE: the number of partitions to apply to the index.
     1. Verify that the index is created.
    
    \d TABLE_NAME

     1. Recommended: Backup your indexes data. We recommend creating a backup of your database and indexes as a best practice.
**Caution:** Any backup that includes the `postgres_ann` extension and was taken before the upgrade cannot be restored after the upgrade.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
