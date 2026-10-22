---
url: https://docs.cloud.google.com/bigtable/docs/hbase-api-changes/
title: Migrate from earlier HBase versions \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:36:47.367821+00:00
---

# Migrate from earlier HBase versions  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/hbase-api-changes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Migrate from earlier HBase versions

The Cloud Bigtable HBase client for Java targets versions 1.x and 2.x of the [Apache HBase API](https://hbase.apache.org/apidocs/). Version 1.0 of the API included some notable changes from earlier versions of HBase. If you are migrating to Bigtable from HBase, and your application targets an older version of the HBase API, you will need to update your application to make it compatible with Bigtable.

To assist with your migration, this page summarizes the most notable changes in the HBase 1.0 API.

## Connection interface

In HBase 1.0 and later, instead of relying upon the deprecated `HConnection` interface, you should use [`org.apache.hadoop.hbase.client.ConnectionFactory`](https://hbase.apache.org/apidocs/org/apache/hadoop/hbase/client/ConnectionFactory.html). This class creates objects that implement the new [`Connection` interface](https://hbase.apache.org/apidocs/org/apache/hadoop/hbase/client/Connection.html). `ConnectionFactory` replaces the deprecated classes `ConnectionManager` and `HConnectionManager`.

Creating a `Connection` object is a relatively expensive operation. You should create one `Connection` object per process and share the object as needed. `Connection` objects are thread-safe.

In addition, be sure to close the connection once you are done using it. In HBase 1.0 and later, it is the application's responsibility to manage the lifecycle of the connection.

Your updated code should look similar to the following example:
    
    
    Connection connection = ConnectionFactory.createConnection(config);
    // ...
    connection.close();
    

## TableName class

In previous versions of HBase, when you manipulated a table, you could specify the table name as a `String` or `byte[]` value. In HBase 1.0 and later, you must specify the table name by creating an instance of [`org.apache.hadoop.hbase.TableName`](https://hbase.apache.org/apidocs/org/apache/hadoop/hbase/TableName.html):
    
    
    String tableName = "MyTable";
        // or byte[] tableName = Bytes.toBytes("MyTable");
    TableName tableNameObj = TableName.valueOf(tableName);
    

## Table, BufferedMutator, and RegionLocator interfaces

In HBase 1.0, the `HTable` class is replaced by the following interfaces:

  * [`org.apache.hadoop.hbase.client.Table`](https://hbase.apache.org/apidocs/org/apache/hadoop/hbase/client/Table.html): Enables you to work with data in a single table.
  * [`org.apache.hadoop.hbase.client.BufferedMutator`](https://hbase.apache.org/devapidocs/org/apache/hadoop/hbase/client/BufferedMutator.html): Enables you to perform asynchronous batch writes to a table. Use this class instead of calling the `setAutoFlush(boolean)` method in `HTableInterface`.
  * [`org.apache.hadoop.hbase.client.RegionLocator`](https://hbase.apache.org/apidocs/org/apache/hadoop/hbase/client/RegionLocator.html): Provides access to information about a table's regions.

**Note:** You cannot use `new HTable(config)` to access Bigtable.

Use a `Connection` object to obtain an instance of these interfaces:
    
    
    Table table = connection.getTable(tableNameObj);
    BufferedMutator mutator = connection.getBufferedMutator(tableNameObj);
    RegionLocator regionLocator = connection.getRegionLocator(tableNameObj);
    

Instances of `Table`, `BufferedMutator`, and `RegionLocator` are not thread-safe. However, these are lightweight objects, so you can create them as needed within the context of a single thread.

## Admin interface

In HBase 1.0, the `HBaseAdmin` class is replaced by the [`org.apache.hadoop.hbase.client.Admin` interface](https://hbase.apache.org/apidocs/org/apache/hadoop/hbase/client/Admin.html). Because Bigtable handles maintenance tasks automatically, many of the methods in the `Admin` interface are not supported. See [Differences between the HBase and Bigtable APIs](https://docs.cloud.google.com/bigtable/docs/hbase-differences#admin) for details.

**Note:** You cannot use `new HBaseAdmin(config)` to access Bigtable.

Use a `Connection` object to obtain an instance of the `Admin` interface:
    
    
    Admin admin = connection.getAdmin();
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
