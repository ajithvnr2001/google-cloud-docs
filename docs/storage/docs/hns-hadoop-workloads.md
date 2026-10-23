---
url: https://docs.cloud.google.com/storage/docs/hns-hadoop-workloads/
title: Use hierarchical namespace enabled buckets for Hadoop workloads \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:50.289870+00:00
---

# Use hierarchical namespace enabled buckets for Hadoop workloads  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/hns-hadoop-workloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Use hierarchical namespace enabled buckets for Hadoop workloads Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use [hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview) enabled buckets for Hadoop workloads.

## Overview

When using a Cloud Storage bucket with hierarchical namespace, you can configure the [Cloud Storage connector](https://docs.cloud.google.com/dataproc/docs/concepts/connectors/cloud-storage) to use the [rename folder](https://docs.cloud.google.com/storage/docs/rename-hns-folders) operation for workloads like Hadoop, Spark, Hive.

In a bucket without hierarchical namespace, a rename operation in Hadoop, Spark, and Hive involves multiple object copy and delete jobs, impacting performance and consistency. Renaming a folder using the Cloud Storage connector optimizes performance and ensures consistency, when handling folders with a large number of objects.

## Before you begin

To use features of hierarchical namespace buckets, use the following Cloud Storage connector versions:

  * 2.2.23 or later (if you are using version 2.x.x)
  * 3.0.1 or later (if you are using version 3.x.x)



Earlier connector versions (3.0.0 and earlier than 2.2.23) have limitations. For more information about the limitations, see [Compatibility with Cloud Storage connector version 3.0.0 or versions earlier than 2.2.23](https://docs.cloud.google.com/storage/docs/hns-hadoop-workloads#backwards-compatibility-connector).

## Enable the Cloud Storage connector on a cluster

This section describes how to enable the Cloud Storage connector on a Managed Service for Apache Spark cluster and a self-managed Hadoop cluster.

###  Managed Service for Apache Spark 

You can use the Google Cloud CLI to create a Managed Service for Apache Spark cluster and enable the Cloud Storage connector to perform the folder operations.

  1. Create a Managed Service for Apache Spark cluster using the following command:
         
         gcloud dataproc clusters create CLUSTER_NAME
           --properties=core:fs.gs.hierarchical.namespace.folders.enable=true,
           core:fs.gs.http.read-timeout=30000
           

Where:

     * `CLUSTER_NAME` is the name of the cluster. For example, `my-cluster`
     * `fs.gs.hierarchical.namespace.folders.enable` is used to enable the hierarchical namespace on a bucket.
     * `fs.gs.http.read-timeout` is the maximum time allowed, in milliseconds, to read data from an established connection. This is an optional setting.

**Note:** If you are using the Cloud Storage connector version 3.0.0 or a version earlier than 2.2.23, the configuration setting `fs.gs.hierarchical.namespace.folders.enable` is not supported and results in an error if included.



### Self-managed Hadoop

You can enable the Cloud Storage connector on your self-managed Hadoop cluster to perform the folder operations.

  1. Add the following to core-site.xml configuration file:
         
         <property>
               <name>fs.gs.hierarchical.namespace.folders.enable</name>
               <value>true</value>
             </property>
             <property>
               <name>fs.gs.http.read-timeout</name>
               <value>30000</value>
             </property>
           

Where:

     * `fs.gs.hierarchical.namespace.folders.enable` is used to enable the hierarchical namespace on a bucket
     * `fs.gs.http.read-timeout` is the maximum time allowed, in milliseconds, to read data from an established connection. This is an optional setting.

**Note:** If you are using the Cloud Storage connector version 3.0.0 or a version earlier than 2.2.23, the configuration setting `fs.gs.hierarchical.namespace.folders.enable` is not supported and results in an error if included.



## Compatibility with Cloud Storage connector version 3.0.0 or versions earlier than 2.2.23

Using the Cloud Storage connector version 3.0.0 or versions earlier than 2.2.23 or disabling folder operations for hierarchical namespace can lead to the following limitations:

  * **Inefficient folder renames** : Folder rename operations in Hadoop happen using object-level copy and delete operations, which is slower and less efficient than the dedicated `rename folder` operation.

  * **Accumulation of empty folders** : Folders are not deleted automatically, leading to the accumulation of empty folders in your bucket. Accumulation of empty folders can have the following impact:

    * Increase storage costs if not deleted explicitly.
    * Slow down the list operations and increase the risk of list operation timeouts.

**Note:** To reduce the risk of list operation timeouts, configure the `fs.gs.http.read-timeout` timeout value to `30000` milliseconds. To configure timeout settings, see the [instructions to enable the Cloud Storage connector](https://docs.cloud.google.com/storage/docs/hns-hadoop-workloads#enable-connector-on-cluster).
  * **Compatibility issues** : Mixing the usage of earlier and later connector versions, or enabling and disabling folder operations, can lead to compatibility issues, when renaming folders. Consider the following scenario which uses a combination of connector versions:

    1. Use the Cloud Storage connector version earlier than 2.2.23 to perform the following tasks:

       1. Write objects under the folder `foo/`.
       2. Rename the folder `foo/` to `bar/`. The rename operation copies and deletes the objects under `foo/` but does not delete the empty `foo/` folder.
    2. Use the Cloud Storage connector version 2.2.23 with the folder operations settings enabled to rename the folder `bar/` to `foo/`.

The connector version 2.2.23, with the folder operation enabled, detects the existing `foo/` folder, causing the rename operation to fail. The earlier connector version, did not delete the `foo/` folder as the folder operation was disabled.




## What's next

  * [Create buckets with hierarchical namespace enabled](https://docs.cloud.google.com/storage/docs/create-hns-bucket).
  * [Create and manage folders](https://docs.cloud.google.com/storage/docs/create-folders).



##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how Cloud Storage performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try Cloud Storage free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
