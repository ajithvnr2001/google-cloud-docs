---
url: https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/migrate-to-latest-version/
title: Migrate from AlloyDB Omni version 15.5.2 and earlier to the latest version \u00a0|\u00a0 AlloyDB Omni for containers: 15.5.4 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:42:22.438134+00:00
---

# Migrate from AlloyDB Omni version 15.5.2 and earlier to the latest version  |  AlloyDB Omni for containers: 15.5.4  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/migrate-to-latest-version/

This page documents AlloyDB Omni version **15.5.4** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/overview)



Send feedback 

#  Migrate from AlloyDB Omni version 15.5.2 and earlier to the latest version Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.5.4keyboard_arrow_down

  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/migrate-to-latest-version)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/migrate-to-latest-version)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/migrate-to-latest-version)

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
             -d google/alloydbomni:15.5.4

Replace the following:

     * `CONTAINER_NAME`: The name to assign this new AlloyDB Omni container in your host machine's container registry—for example, `my-omni`.

     * `PASSWORD`: The password assigned the new container's `postgres` user after its creation.

     * `PGPORT`: The IP address of the port the AlloyDB Omni runs on. This is the value you noted down in step 2 of Gather information about your existing installation.

The arguments to `docker run` are the ones used in earlier versions of AlloyDB Omni, but you may further customize them. See [Customize your AlloyDB Omni installation](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/install) for details.

  3. If your database instance type is `PRIMARY`, run the following command to create the following users. These are usernames which are unused at the moment, but reserved for future extensions.
         
         for name in alloydbagent alloydbexport alloydbiamgroupuser alloydbiamuser alloydbimportexport alloydbobservability alloydbsqllogical alloydbsuperuser; do
           echo docker exec -it CONTAINER_NAME psql -h localhost -U postgres alloydbadmin \
             -c "CREATE ROLE ${name} NOLOGIN;" \
             -c "CREATE TABLE ${name}_table();" \
             -c "ALTER TABLE ${name}_table OWNER TO ${name};"
         done

  4. If `ENABLE_ALLOYDB_AI` is set to `TRUE`, follow instructions in [Install AlloyDB Omni with AlloyDB AI](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/install-with-alloydb-ai) to set up AlloyDB AI.

  5. Connect to the database to verify that the data is unchanged:
         
         docker exec -it CONTAINER_NAME psql -h localhost -U postgres

  6. Uninstall the AlloyDB Omni CLI:
         
         sudo alloydb database-server uninstall

The AlloyDB Omni CLI uninstallation does not affect your data stored in AlloyDB Omni.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
