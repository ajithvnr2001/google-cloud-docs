---
url: https://docs.cloud.google.com/dataproc-metastore/docs/use-hive/
title: Use Apache Hive with Dataproc Metastore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:36.936754+00:00
---

# Use Apache Hive with Dataproc Metastore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataproc-metastore/docs/use-hive/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataproc Metastore ](https://docs.cloud.google.com/dataproc-metastore/docs)
  * [ Guides ](https://docs.cloud.google.com/dataproc-metastore/docs/create-service-cluster)



Send feedback 

#  Use Apache Hive with Dataproc Metastore Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you an example of using Apache Hive with a Dataproc Metastore service. In this example, you launch a Hive session on a Managed Service for Apache Spark cluster, and then run sample commands to create a database and table.

**Note:** Dataproc Metastore doesn't support Hive queries in Managed Service for Apache Spark 3.0 image version clusters. However, you can use Dataproc Metastore for Spark queries.

## Before you begin

  * Create a [Dataproc Metastore service](https://docs.cloud.google.com/dataproc-metastore/docs/create-service). 
  * Attach the [Dataproc Metastore service to a Managed Service for Apache Spark cluster](https://docs.cloud.google.com/dataproc-metastore/docs/attach-dataproc). 
    * [Set the Hive metastore password](https://docs.cloud.google.com/dataproc/docs/concepts/configuring-clusters/secure-hive-metastore#set_the_hive_metastore_password).



## Connect to Apache Hive

To start using Hive, use SSH to connect to the Managed Service for Apache Spark cluster that's associated with your Dataproc Metastore service. Once connected, you can run Hive commands from the SSH terminal window in your browser to manage your metadata.

**To connect to Hive**

  1. In the Google Cloud console, go to the [VM Instances](https://console.cloud.google.com/compute/instances) page.
  2. In the list of virtual machine instances, click **SSH** in the row of the Managed Service for Apache Spark VM instance that you want to connect to.



A browser window opens in your home directory on the node with an output similar to the following:
    
    
    Connected, host fingerprint: ssh-rsa ...
    Linux cluster-1-m 3.16.0-0.bpo.4-amd64 ...
    ...
    example-cluster@cluster-1-m:~$
    

To start Hive and create a database and table, run the following commands in the SSH session:

  1. Start Hive.
         
         hive
         

  2. Create a database named `myDatabase`.
         
         create database myDatabase;
         

  3. Show the database that you created.
         
         show databases;
         

  4. Use the database that you created.
         
         use myDatabase;
         

  5. Create a table named `myTable`.
         
         create table myTable(id int,name string);
         

  6. List the tables under `myDatabase`.
         
         show tables;
         

  7. Show the table rows in the table that you created.
         
         desc myTable;
         




Running the following commands generates output similar to the following:
    
    
    $hive
    
    hive> show databases;
    OK
    default
    hive> create database myDatabase;
    OK
    hive> use myDatabase;
    OK
    hive> create table myTable(id int,name string);
    OK
    hive> show tables;
    OK
    myTable
    hive> desc myTable;
    OK
    id                      int                                         
    name                    string 
    

## What's next

  * [Import metadata](https://docs.cloud.google.com/dataproc-metastore/docs/import-metadata)
  * [Export metadata](https://docs.cloud.google.com/dataproc-metastore/docs/export-metadata)
  * [Use Spark SQL](https://docs.cloud.google.com/dataproc-metastore/docs/use-spark)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
