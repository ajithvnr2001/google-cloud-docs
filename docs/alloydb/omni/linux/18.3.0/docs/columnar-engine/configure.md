---
url: https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/columnar-engine/configure/
title: Configure the columnar engine in AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni using RPM: 18.3.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:53:13.905713+00:00
---

# Configure the columnar engine in AlloyDB Omni  |  AlloyDB Omni using RPM: 18.3.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/columnar-engine/configure/

This page documents AlloyDB Omni version **18.3.0** using the **RPM** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM: 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/overview)



Send feedback 

#  Configure the columnar engine in AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.3.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/columnar-engine/configure)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/columnar-engine/configure)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/columnar-engine/configure)
  * [ 18.1.1 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/columnar-engine/configure)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/columnar-engine/configure)

This page describes how to enable or disable the columnar engine on an AlloyDB Omni database cluster. It also covers how to configure an appropriate initial size for its column store. 

For a conceptual overview of the AlloyDB columnar engine, see [AlloyDB Omni columnar engine overview](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/columnar-engine/overview).

## Enable the columnar engine

To use columnar engine on an instance, set the instance's [`google_columnar_engine.enabled`](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/reference/columnar-engine-flags#enabled) flag to `on`.

###  Single-server 

To set the `google_columnar_engine.enabled` to `on`, do the following steps:

  1. Run [the `ALTER SYSTEM` PostgreSQL command](https://www.postgresql.org/docs/current/sql-altersystem.html):
         
         ALTER SYSTEM SET google_columnar_engine.enabled = 'on'
         

  2. If you want to adjust the columnar engine's configuration, then follow the instructions in the [next section](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/columnar-engine/configure#configure) before you restart the database server. Otherwise, complete the following step to restart the database server now.

  3. For the configuration parameters change to take effect, restart your database server:
         
         sudo systemctl restart alloydbomni18




## Configure the size of the column store

While the columnar engine is enabled on an instance, AlloyDB Omni allocates a portion of the instance's memory to store its columnar data. Dedicating high-speed RAM to your column store verifies that AlloyDB Omni can access the columnar data as rapidly as possible.

Memory and storage cache together represent the overall capacity of the columnar engine.

### Configure memory

**Warning:** The default value of `google_columnar_engine.memory_size_in_mb` is 1024 MB.

You can set the allocation to a fixed size using the [`google_columnar_engine.memory_size_in_mb`](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/reference/columnar-engine-flags#memory-size-in-mb) flag.

###  Single-server 

To set the `google_columnar_engine.memory_size_in_mb` flag on an instance, do the following:

  1. Configure memory by running the [`ALTER SYSTEM`](https://www.postgresql.org/docs/current/sql-altersystem.html) PostgreSQL command:
         
         ALTER SYSTEM SET google_columnar_engine.memory_size_in_mb = COLUMN_MEMORY_SIZE;
         

Replace `COLUMN_MEMORY_SIZE` with the new size of the column storage, in megabytes—for example, `256`.

  2. For the configuration parameters change to take effect, restart your database server:
         
         sudo systemctl restart alloydbomni18




### Configure storage cache

**Note:** This step is optional for enabling the columnar engine.

###  Single-server 

#### Shared or dedicated devices

You can configure the columnar engine storage cache on either dedicated or shared devices.

##### Provision and mount the cache directory

On dedicated devices, you need to provision disks, create a file system, mount the cache directory on a host path (for example, `/var/lib/postgresql/18/data/columnar_cache`), and ensure it has write permissions for the `postgres` user.

##### Enable the columnar storage cache

  1. Run `ALTER SYSTEM` to configure the cache directory path and size:
         
         ALTER SYSTEM SET google_columnar_engine.omni_storage_cache_directory = 'CACHE_DIR_PATH';
         ALTER SYSTEM SET google_columnar_engine.storage_cache_size = STORAGE_CACHE_SIZE;
         

Replace the following:

     * `CACHE_DIR_PATH`: The path to the cache directory (for example, `/var/lib/postgresql/18/data/columnar_cache`).
     * `STORAGE_CACHE_SIZE`: The size of your columnar engine storage cache, in megabytes.
  2. Restart your database server:
         
         sudo systemctl restart alloydbomni18




## Enable vectorized join

The columnar engine has a _vectorized join_ feature that can improve the performance of joins by applying vectorized processing to qualifying queries.

After you enable vectorized join, the AlloyDB query planner has the option to apply the vectorized join operator instead of the standard PostgreSQL hash join operator. The planner makes this decision by comparing the cost of executing the query using each method.

To enable vectorized join on an instance, set the instance's [`google_columnar_engine.enable_vectorized_join`](https://docs.cloud.google.com/alloydb/omni/16.8.0/docs/reference/columnar-engine-flags#enable-vectorized-join) flag to `on`.

To set this flag on an instance, run [the `ALTER SYSTEM` PostgreSQL command](https://www.postgresql.org/docs/current/sql-altersystem.html):
    
    
    ALTER SYSTEM SET google_columnar_engine.enable_vectorized_join = 'on';
    

AlloyDB Omni allocates one thread to the vectorized join feature by default. You can increase the number of threads available to this feature by setting the [`google_columnar_engine.vectorized_join_threads`](https://docs.cloud.google.com/alloydb/omni/current/docs/reference/columnar-engine-flags#vectorized-join-threads) flag to a larger value. The maximum value is `cpu_count * 2`.

## Manually refresh your columnar engine

By default, when the columnar engine is enabled it refreshes the column store in the background.

To manually refresh the column engine, run the following SQL query:
    
    
    SELECT google_columnar_engine_refresh(relation =>'TABLE_NAME');
    

Replace `TABLE_NAME` with the name of the table or the materialized view you want to manually refresh.

## Disable the columnar engine

To disable the columnar engine on an instance, set the `google_columnar_engine.enabled` flag to `off`.

###  Single-server 

To set the `google_columnar_engine.enabled` to `off`, do the following steps:

  1. Run [the `ALTER SYSTEM` PostgreSQL command](https://www.postgresql.org/docs/current/sql-altersystem.html):


    
    
    ALTER SYSTEM SET google_columnar_engine.enabled = 'off'
    

  1. For the configuration parameters change to take effect, restart your database server:
         
         sudo systemctl restart alloydbomni18




## What's next

  * See the [complete list of columnar engine database flags](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/reference/columnar-engine-flags).

  * Try out the codelab [Accelerating analytical queries with columnar engine in AlloyDB Omni](https://codelabs.developers.google.com/alloydb-omni-columnar).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
