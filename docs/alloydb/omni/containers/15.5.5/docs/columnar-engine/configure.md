---
url: https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/columnar-engine/configure/
title: Configure the columnar engine in AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni for containers: 15.5.5 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:23:33.990574+00:00
---

# Configure the columnar engine in AlloyDB Omni  |  AlloyDB Omni for containers: 15.5.5  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/columnar-engine/configure/

This page documents AlloyDB Omni version **15.5.5** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/overview)



Send feedback 

#  Configure the columnar engine in AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.5.5keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/columnar-engine/configure)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/columnar-engine/configure)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/columnar-engine/configure)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/columnar-engine/configure)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/columnar-engine/configure)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/columnar-engine/configure)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/columnar-engine/configure)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/columnar-engine/configure)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/columnar-engine/configure)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/columnar-engine/configure)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/columnar-engine/configure)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/columnar-engine/configure)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/columnar-engine/configure)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/columnar-engine/configure)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/columnar-engine/configure)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/columnar-engine/configure)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/columnar-engine/configure)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/columnar-engine/configure)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/columnar-engine/configure)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/columnar-engine/configure)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/columnar-engine/configure)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/columnar-engine/configure)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/columnar-engine/configure)

This page describes how to enable or disable the columnar engine on an AlloyDB Omni database cluster. It also covers how to configure an appropriate initial size for its column store. 

To use the columnar engine when using AlloyDB for PostgreSQL on Google Cloud, see [Configure the columnar engine](https://docs.cloud.google.com/alloydb/docs/columnar-engine/configure).

For a conceptual overview of the AlloyDB columnar engine, see [About the AlloyDB columnar engine](https://docs.cloud.google.com/alloydb/docs/columnar-engine/about).

## Enable the columnar engine

To use columnar engine on an instance, set the instance's [`google_columnar_engine.enabled`](https://docs.cloud.google.com/alloydb/docs/reference/columnar-engine-flags#enabled) flag to `on`.

To set this flag on an instance, do the following:

  1. Run [the `ALTER SYSTEM` PostgreSQL command](https://www.postgresql.org/docs/current/sql-altersystem.html):
         
         ALTER SYSTEM SET google_columnar_engine.enabled = 'on'
         

  2. If you want to adjust the columnar engine's configuration, then follow the instructions in the next section before you restart the database server. Otherwise, follow the next two steps to restart the database server now.

  3. [Stop the database server.](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/run-connect#stop)

  4. [Start the database server.](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/run-connect#start)




## Configure the size of the column store

While the columnar engine is enabled on an instance, AlloyDB allocates a portion of the instance's memory to store its columnar data. Dedicating high-speed RAM to your column store ensures that AlloyDB can access the columnar data as rapidly as possible.

You can also you set the allocation to a fixed and specific size using the [`google_columnar_engine.memory_size_in_mb`](https://docs.cloud.google.com/alloydb/docs/reference/columnar-engine-flags#memory-size-in-mb) flag.

**Warning:** The default value of `google_columnar_engine.memory_size_in_mb` is 1024 MB.

To set this flag on an instance, do the following:

  1. Run [the `ALTER SYSTEM` PostgreSQL command](https://www.postgresql.org/docs/current/sql-altersystem.html):
         
         ALTER SYSTEM SET google_columnar_engine.memory_size_in_mb = COLUMN_STORE_SIZE;
         

Replace `COLUMN_STORE_SIZE` with the new size of the column store, in megabytes.

  2. [Stop the database server.](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/run-connect#stop)

  3. [Start the database server.](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/run-connect#start)




## Enable vectorized join

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The columnar engine has a _vectorized join_ feature that can improve the performance of joins by applying vectorized processing to qualifying queries.

After you enable vectorized join, the AlloyDB query planner has the option to apply the vectorized join operator instead of the standard PostgreSQL hash join operator. The planner makes this decision by comparing the cost of executing the query using either method.

To enable vectorized join on an instance, set the instance's [`google_columnar_engine.enable_vectorized_join`](https://docs.cloud.google.com/alloydb/docs/reference/columnar-engine-flags#enable-vectorized-join) flag to `on`.

To set this flag on an instance, run [the `ALTER SYSTEM` PostgreSQL command](https://www.postgresql.org/docs/current/sql-altersystem.html):
    
    
    ALTER SYSTEM SET google_columnar_engine.enable_vectorized_join = 'on';
    

AlloyDB allocates one thread to the vectorized join feature by default. You can increase the number of threads available to this feature by setting the [`google_columnar_engine.vectorized_join_threads`](https://docs.cloud.google.com/alloydb/docs/reference/columnar-engine-flags#vectorized-join-threads) flag to a larger value.

## Manually refresh your columnar engine

By default, the columnar engine is set to automatically refresh the column store in the background when enabled. You may need to manually refresh the columnar store in certain situations, such as if auto-refresh doesn't refresh a relation with a high number of invalid blocks.

To manually refresh the column engine, run the following SQL query:
    
    
    SELECT google_columnar_engine_refresh('TABLE_NAME');
    

Replace `TABLE_NAME` with the name of the table or the materialized view you want to manually refresh.

## Disable the columnar engine

To disable the columbar engine on an instance, set the `google_columnar_engine.enabled` flag to `off`.

To set this flag on an instance, do the following:

  1. Run [the `ALTER SYSTEM` PostgreSQL command](https://www.postgresql.org/docs/current/sql-altersystem.html):
         
         ALTER SYSTEM SET google_columnar_engine.enabled = 'off'
         

  2. [Stop the database server.](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/run-connect#stop)

  3. [Start the database server.](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/run-connect#start)




## Troubleshoot the columnar engine

### Fix an "insufficient shared memory" error

If you run AlloyDB Omni without enough shared memory for the columnar engine to use, then you might see this error:
    
    
    Insufficient shared memory for generating the columnar formats.
    

You can address this issue by specifying the amount of shared memory that is available to the AlloyDB Omni container. The way that you do this differs depending upon your host operating system

###  Linux 

Increase the size of your host machine's `/dev/shm` partition, using a technique such as editing your `/etc/fstab` file.

**Note:** This requires that you installed AlloyDB Omni with your `/dev/shm` directory mounted on the container, as shown in [Customize your AlloyDB Omni installation](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/install#one-omni).

###  macOS 

[Install a new AlloyDB Omni container](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/install#one-omni), specifying a larger shared-memory value for the `--shm-size` flag.

**Caution:** Back up your data before switching to using a new container.

### Fix columns not getting populated

If columns don't populate in the columnar engine, then one of the following situations might be true:

  * The columns you want to add include an unsupported data type.

  * The requirements of the columnar engine aren't being met.




To find the cause of this issue, try the following:

  * [Confirm](https://docs.cloud.google.com/alloydb/docs/columnar-engine/monitor-tune#relations-view) that the tables or materialized views in our query are in the columnar engine.

  * Verify the usage of the columnar engine using the [`EXPLAIN`](https://docs.cloud.google.com/alloydb/docs/columnar-engine/monitor-tune) statement.




## What's next

  * See the [full list of columnar engine database flags](https://docs.cloud.google.com/alloydb/docs/reference/columnar-engine-flags).

  * Learn about [auto-columnarization](https://docs.cloud.google.com/alloydb/docs/columnar-engine/manage-content-recommendations).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
