---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/columnar-engine/configure/
title: Configure the columnar engine in AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 16.9.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:25:25.590958+00:00
---

# Configure the columnar engine in AlloyDB Omni  |  AlloyDB Omni for Kubernetes: 16.9.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/columnar-engine/configure/

This page documents AlloyDB Omni version **16.9.0** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/overview)



Send feedback 

#  Configure the columnar engine in AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 16.9.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/columnar-engine/configure)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/columnar-engine/configure)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/columnar-engine/configure)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/columnar-engine/configure)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/columnar-engine/configure)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/columnar-engine/configure)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/columnar-engine/configure)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/columnar-engine/configure)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/columnar-engine/configure)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/columnar-engine/configure)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/columnar-engine/configure)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/columnar-engine/configure)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/columnar-engine/configure)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/columnar-engine/configure)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/columnar-engine/configure)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/columnar-engine/configure)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/columnar-engine/configure)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/columnar-engine/configure)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/columnar-engine/configure)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/columnar-engine/configure)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/columnar-engine/configure)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/columnar-engine/configure)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/columnar-engine/configure)

This page describes how to enable or disable the columnar engine on an AlloyDB Omni database cluster. It also covers how to configure an appropriate initial size for its column store. 

For a conceptual overview of the AlloyDB columnar engine, see [AlloyDB Omni columnar engine overview](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/columnar-engine/overview).

## Enable the columnar engine

To use columnar engine on an instance, set the instance's [`google_columnar_engine.enabled`](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/columnar-engine-flags#enabled) flag to `on`.

###  Kubernetes 

To set the `google_columnar_engine.enabled` flag to `on`, modify your database cluster manifest to add the `parameters` attribute to the `primarySpec` section:
    
    
        apiVersion: alloydbomni.dbadmin.goog/v1
        kind: DBCluster
        metadata:
          name: CLUSTER_NAME
        spec:
          databaseVersion: "16.9.0"
          primarySpec:
            parameters:
              google_columnar_engine.enabled: "on"
    

Replace `CLUSTER_NAME` with the name of your database cluster. It is the same database cluster name you declared when [you created it](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/deploy-kubernetes#create).

## Configure the size of the column store

While the columnar engine is enabled on an instance, AlloyDB Omni allocates a portion of the instance's memory to store its columnar data. Dedicating high-speed RAM to your column store verifies that AlloyDB Omni can access the columnar data as rapidly as possible.

Memory and storage cache together represent the overall capacity of the columnar engine.

### Configure memory

**Warning:** The default value of `google_columnar_engine.memory_size_in_mb` is 1024 MB.

You can set the allocation to a fixed size using the [`google_columnar_engine.memory_size_in_mb`](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/columnar-engine-flags#memory-size-in-mb) flag.

###  Kubernetes 

To set the `google_columnar_engine.memory_size_in_mb` flag, modify your database cluster manifest to add the `parameters` attribute to the `primarySpec` section:
    
    
        apiVersion: alloydbomni.dbadmin.goog/v1
        kind: DBCluster
        metadata:
          name: CLUSTER_NAME
        spec:
          databaseVersion: "16.9.0"
          primarySpec:
            parameters:
              google_columnar_engine.memory_size_in_mb: "COLUMN_MEMORY_SIZE"
    

Replace the following:

  * `CLUSTER_NAME`: the name of your database cluster. It is the same database cluster name you declared when [you created it](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/deploy-kubernetes#create).
  * `COLUMN_MEMORY_SIZE`: the new size of the column storage, in megabytes—for example, `256`.



### Configure storage cache

**Note:** This step is optional for enabling the columnar engine.

###  Kubernetes 

To enable storage cache for your database, modify your database cluster manifest to add the `columnarSpillToDisk` attribute to the `features` section of the `primarySpec` section:
    
    
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: DBCluster
    metadata:
      name: CLUSTER_NAME
    spec:
      databaseVersion: "16.9.0"
      primarySpec:
        features:
          columnarSpillToDisk:
            cacheSize: STORAGE_CACHE_SIZE
          ultraFastCache:
            cacheSize: ULTRAFAST_CACHE_SIZE
            genericVolume:
              storageClass: "STORAGE_CLASS_NAME"
    ...
    

Replace the following:

  * `CLUSTER_NAME`: the name of your database cluster. It is the same database cluster name you declared when [you created it](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/deploy-kubernetes#create).
  * `STORAGE_CACHE_SIZE`: the size of the columnar storage cache—for example, `5Gi`. If you don't specify a value for this field, 5% of the disk cache gets allocated to the columnar engine by default.
  * `ULTRAFAST_CACHE_SIZE`: the size of the cache—for example, `100Gi`. It must be greater than `shared_buffers`. This field is optional. If you don't specify the value of this field, AlloyDB Omni uses all space left on the disk, which applies to both AlloyDB Omni in a container and on a Kubernetes cluster. For more information about units of measure, see [Memory resource units](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#meaning-of-memory).
  * `STORAGE_CLASS_NAME`: the name of the [storage class](https://kubernetes.io/docs/concepts/storage/persistent-volumes#class-1) of the ultra fast cache volume—for example, `local-storage`.

**Note:** If both `spec.primarySpec.features.ultrafastCache.cacheSize` and `spec.primarySpec.features.columnarSpillToDisk.cacheSize` are specified, their total sum equals the amount of reserved disk space. For example, if you specify `50 Gi` for `spec.primarySpec.features.columnarSpillToDisk.cacheSize` and `200 Gi` for `spec.primarySpec.features.ultrafastCache.cacheSize`, the total reserved disk space is `250Gi`.

## Enable vectorized join

The columnar engine has a _vectorized join_ feature that can improve the performance of joins by applying vectorized processing to qualifying queries.

After you enable vectorized join, the AlloyDB query planner has the option to apply the vectorized join operator instead of the standard PostgreSQL hash join operator. The planner makes this decision by comparing the cost of executing the query using each method.

To enable vectorized join on an instance, set the instance's [`google_columnar_engine.enable_vectorized_join`](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/columnar-engine-flags#enable-vectorized-join) flag to `on`.

To set this flag on an instance, run [the `ALTER SYSTEM` PostgreSQL command](https://www.postgresql.org/docs/current/sql-altersystem.html):
    
    
    ALTER SYSTEM SET google_columnar_engine.enable_vectorized_join = 'on';
    

AlloyDB Omni allocates one thread to the vectorized join feature by default. You can increase the number of threads available to this feature by setting the [`google_columnar_engine.vectorized_join_threads`](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/columnar-engine-flags#vectorized-join-threads) flag to a larger value. The maximum value is `cpu_count * 2`.

## Manually refresh your columnar engine

By default, when the columnar engine is enabled it refreshes the column store in the background.

To manually refresh the column engine, run the following SQL query:
    
    
    SELECT google_columnar_engine_refresh(relation =>'TABLE_NAME');
    

Replace `TABLE_NAME` with the name of the table or the materialized view you want to manually refresh.

## Disable the columnar engine

To disable the columbar engine on an instance, set the `google_columnar_engine.enabled` flag to `off`.

###  Kubernetes 

To set the `google_columnar_engine.enabled` flag to `off`, modify your database cluster manifest to add the `parameters` attribute to the `primarySpec` section:
    
    
      apiVersion: alloydbomni.dbadmin.goog/v1
      kind: DBCluster
      metadata:
        name: CLUSTER_NAME
      spec:
        databaseVersion: "16.9.0"
        primarySpec:
          parameters:
            google_columnar_engine.enabled: "off"
    

Replace `CLUSTER_NAME` with the name of your database cluster. It is the same database cluster name you declared when [you created it](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/deploy-kubernetes#create).

## What's next

  * See the [full list of columnar engine database flags](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/columnar-engine-flags).

  * Work through the [Accelerating analytical queries with columnar engine in AlloyDB Omni](https://codelabs.developers.google.com/alloydb-omni-columnar) Google CodeLab tutorial.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
