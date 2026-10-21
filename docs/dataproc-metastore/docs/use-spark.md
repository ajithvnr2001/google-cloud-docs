---
url: https://docs.cloud.google.com/dataproc-metastore/docs/use-spark/
title: Use Spark SQL with Dataproc Metastore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:39:58.662569+00:00
---

# Use Spark SQL with Dataproc Metastore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataproc-metastore/docs/use-spark/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataproc Metastore ](https://docs.cloud.google.com/dataproc-metastore/docs)
  * [ Guides ](https://docs.cloud.google.com/dataproc-metastore/docs/create-service-cluster)



Send feedback 

#  Use Spark SQL with Dataproc Metastore Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you an example of using Spark SQL with a Dataproc Metastore service. In this example, you launch a Spark SQL session on a Managed Service for Apache Spark cluster and run some sample commands to create a database and table.

## Before you begin

  * Create a [Dataproc Metastore service](https://docs.cloud.google.com/dataproc-metastore/docs/create-service).
  * Attach the [Dataproc Metastore service to a Managed Service for Apache Spark cluster](https://docs.cloud.google.com/dataproc-metastore/docs/attach-dataproc).



## Connect to Spark SQL

To start using Spark SQL, use SSH to connect to the Managed Service for Apache Spark cluster that's associated with your Dataproc Metastore service. After you connect to the cluster with SSH, you can run Spark commands to manage your metadata.

**To connect to Spark SQL**

  1. In the Google Cloud console, go to the [VM Instances](https://console.cloud.google.com/compute/instances) page.
  2. In the list of virtual machine instances, click **SSH** in the row of the Managed Service for Apache Spark VM instance that you want to connect to.



A browser window opens in your home directory on the node with an output similar to the following:
    
    
    Connected, host fingerprint: ssh-rsa ...
    Linux cluster-1-m 3.16.0-0.bpo.4-amd64 ...
    ...
    example-cluster@cluster-1-m:~$
    

To start Hive and create a database and table, run the following commands in the SSH session:

  1. Start the Spark shell.
         
         spark-shell
         

  2. Create a database called `myDB`.
         
         spark.sql("create database myDB");
         

  3. Use the database you created.
         
         spark.sql("use myDB");
         

  4. Create a table called `myTable`.
         
         spark.sql("create table bar(id int,name string)");
         

  5. List the tables under `myDB`.
         
         spark.sql("show tables").show();
         

  6. Show the table rows in the table you created.
         
         desc myTable;
         




Running these commands shows an output similar to the following:
    
    
    $spark-shell
    
    scala>spark.sql("create database myDB");
    
    scala>spark.sql("use myTable");
    
    scala>spark.sql("create table myTable(id int,name string)");
    
    scala>spark.sql("show tables").show();
    
    +--------+---------+-----------+
    |database|tableName|isTemporary|
    +--------+---------+-----------+
    |    myDB|  myTable|      false|
    +--------+---------+-----------+
    +--------+---------+-------+
    |col_name|data_type|comment|
    +--------+---------+-------+
    |      id|      int|   null|
    |    name|   string|   null|
    +--------+---------+-------+
    

## What's next

  * [Import metadata](https://docs.cloud.google.com/dataproc-metastore/docs/import-metadata)
  * [Export metadata](https://docs.cloud.google.com/dataproc-metastore/docs/export-metadata)
  * [Use Apache Hive](https://docs.cloud.google.com/dataproc-metastore/docs/use-hive)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
