---
url: https://docs.cloud.google.com/bigtable/docs/hbase-differences/
title: Differences between HBase and Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:29:19.079076+00:00
---

# Differences between HBase and Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/hbase-differences/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Differences between HBase and Bigtable

One way to access Bigtable is to use a customized version of the Apache HBase client for Java. In general, the customized client exposes the [same API](https://hbase.apache.org/apidocs/) as a standard installation of HBase. This page describes the differences between the Cloud Bigtable HBase client for Java and a standard HBase installation. Many of these difference are related to management tasks that Bigtable handles automatically.

The Cloud Bigtable HBase client for Java is for customers who are migrating to Bigtable from HBase and want to continue using the HBase API. In all other cases, Java developers should instead use the [Cloud Bigtable client for Java](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/overview), which calls the Bigtable APIs. 

## Column families

When you create a column family, you cannot configure the block size or compression method, either with the HBase shell or through the HBase API. Bigtable manages the block size and compression for you.

In addition, if you use the HBase shell to get information about a table, the HBase shell will always report that each column family does not use compression. In reality, Bigtable uses proprietary compression methods for all of your data.

Bigtable requires that column family names follow the regular expression `[_a-zA-Z0-9][-_.a-zA-Z0-9]*`. If you are importing data into Bigtable from HBase, you might need to first change the family names to follow this pattern.

## Rows and cells

  * You cannot define an ACL for an individual row.
  * You cannot set the visibility of individual cells.
  * Tags are not supported. You cannot use the class [`org.apache.hadoop.hbase.Tag`](https://hbase.apache.org/devapidocs/org/apache/hadoop/hbase/Tag.html) to add metadata to individual cells.



## Mutations and deletions

  * [`Append`](https://hbase.apache.org/apidocs/org/apache/hadoop/hbase/client/Append.html) operations in Bigtable are fully atomic for both readers and writers. Readers will never be able to read a partially applied `Append` operation.
  * Deleting a specific version of a specific column based on its timestamp is supported, but deleting all values with a specific timestamp in a given column family or row is not supported. The following methods in the class [`org.apache.hadoop.hbase.client.Delete`](https://hbase.apache.org/apidocs/org/apache/hadoop/hbase/client/Delete.html) are not supported: 
    * `new Delete(byte[] row, long timestamp)`
    * `addColumn(byte[] family, byte[] qualifier)`
    * `addFamily(byte[] family, long timestamp)`
    * `addFamilyVersion(byte[] family, long timestamp)`
  * In HBase, [deletes mask puts](http://hbase.apache.org/book.html#_deletes_mask_puts), but Bigtable does not mask puts after deletes when put requests are sent after deletion requests. This means that in Bigtable, a write request sent to a cell is not affected by a previously sent delete request to the same cell.



## Gets and scans

  * Reverse scans let you read a range of rows backwards. For details, see [Reverse scans](https://docs.cloud.google.com/bigtable/docs/reads#reverse-scan).
  * Unlike HBase, when you send a read request, Bigtable doesn't automatically filter out expired data that is marked for deletion in an upcoming garbage collection cycle. To avoid reading expired data, use a filter in the read request. For more information, see the [Garbage collection overview](https://docs.cloud.google.com/bigtable/docs/garbage-collection).
  * Querying versions of column families within a timestamp range is not supported. You cannot call the following methods: 
    * [`org.apache.hadoop.hbase.client.Query#setColumnFamilyTimeRange(byte[] cf, long minStamp, long maxStamp)`](https://hbase.apache.org/apidocs/org/apache/hadoop/hbase/client/Query.html#setColumnFamilyTimeRange-byte:A-long-long-)
    * [`org.apache.hadoop.hbase.client.Get#setColumnFamilyTimeRange(byte[] cf, long minStamp, long maxStamp)`](https://hbase.apache.org/apidocs/org/apache/hadoop/hbase/client/Get.html#setColumnFamilyTimeRange-byte:A-long-long-)
    * [`org.apache.hadoop.hbase.client.Scan#setColumnFamilyTimeRange(byte[] cf, long minStamp, long maxStamp)`](https://hbase.apache.org/apidocs/org/apache/hadoop/hbase/client/Scan.html#setColumnFamilyTimeRange-byte:A-long-long-)
  * Limiting the number of values per row per column family is not supported. You cannot call the method [`org.apache.hadoop.hbase.client.Scan#setMaxResultsPerColumnFamily(int limit)`](https://hbase.apache.org/apidocs/org/apache/hadoop/hbase/client/Scan.html#setMaxResultsPerColumnFamily-int-).
  * Setting the maximum number of cells to return for each call to `next()` is not supported. Calls to the method [`org.apache.hadoop.hbase.client.Scan#setBatch(int batch)`](https://hbase.apache.org/apidocs/org/apache/hadoop/hbase/client/Scan.html#setBatch-int-) are ignored.
  * Setting the number of rows for caching is not supported. Calls to the method [`org.apache.hadoop.hbase.client.Scan#setCaching(int caching)`](https://hbase.apache.org/apidocs/org/apache/hadoop/hbase/client/Scan.html#setCaching-int-) are ignored.



## Coprocessors

Coprocessors are not supported. You cannot create classes that implement the interface [`org.apache.hadoop.hbase.coprocessor`](https://hbase.apache.org/apidocs/org/apache/hadoop/hbase/coprocessor/package-summary.html).

## Filters

The following table shows which filters are supported. All of these filters are in the package [`org.apache.hadoop.hbase.filter`](https://hbase.apache.org/apidocs/org/apache/hadoop/hbase/filter/package-summary.html).

Supported | Supported, with limitations | Not supported  
---|---|---  
  
  1. Supports only a single column family. 
  2. Calling `setLenAsVal(true)` is not supported. 
  3. Supports only the `BinaryComparator` comparator. If any operator other than `EQUAL` is used, only a single column family is supported. 
  4. Supports only the following comparators: 
     * `BinaryComparator`
     * `RegexStringComparator` with no flags (flags are ignored) and the `EQUAL` operator 
  5. If a `PageFilter` is in a `FilterList`, `PageFilter` will only work similarly to HBase when the `FilterList` is set to `MUST_PASS_ALL`, which is the default behavior. If the `FilterList` is set to `MUST_PASS_ONE`, Bigtable will treat the `PageFilter` as a `MUST_PASS_ALL` and only return a number of rows corresponding to the `PageFilter`'s pageSize. 
  6. `PrefixFilter` scans for rows in the `PrefixFilter` in most cases. However, if `PrefixFilter` is part of a `FilterList` and has the operator `MUST_PASS_ONE`, Bigtable cannot determine the implied range and instead performs an unfiltered scan from the start row to the stop row. Use `PrefixFilter` with `BigtableExtendedScan` or a combination of filters to optimize performance in this case. 
  7. Relies on the Bigtable condition filter, which can be slow. Supported but not recommended. 

  
`ColumnPrefixFilter`  
`FamilyFilter`  
`FilterList`  
`FuzzyRowFilter`  
`MultipleColumnPrefixFilter`  
`MultiRowRangeFilter`  
`PrefixFilter` 6  
`RandomRowFilter`  
`TimestampsFilter` |  `ColumnCountGetFilter` 1  
`ColumnPaginationFilter` 1  
`ColumnRangeFilter` 1  
`FirstKeyOnlyFilter` 1  
`KeyOnlyFilter` 2  
`PageFilter` 5  
`QualifierFilter` 3  
`RowFilter` 1, 4  
`SingleColumnValueExcludeFilter` 1, 4, 7  
`SingleColumnValueFilter` 4, 7  
`ValueFilter` 4 |  `DependentColumnFilter`  
`FirstKeyValueMatchingQualifiersFilter`  
`InclusiveStopFilter`  
`ParseFilter`  
`SkipFilter`  
`WhileMatchFilter`  
  
  
In addition, the following differences affect Bigtable filters:

  * In filters that use the regular expression comparator (`org.apache.hadoop.hbase.filter.RegexStringComparator`), regular expressions use [RE2 syntax](https://github.com/google/re2/wiki/Syntax), not Java syntax.
  * Custom filters are not supported. You cannot create classes that inherit from [`org.apache.hadoop.hbase.filter.Filter`](https://hbase.apache.org/apidocs/org/apache/hadoop/hbase/filter/Filter.html).
  * There is a size limit of 20 KB on filter expressions. As a workaround to reduce the size of a filter expression, use a supplementary column that stores the hash value of the filter criteria.



## Timestamps

Bigtable stores timestamps in microseconds, while HBase stores timestamps in milliseconds. This distinction has implications when you use the HBase client library for Bigtable and you have data with reversed timestamps.

The client library converts between microseconds and milliseconds, but because that the largest HBase timestamp that Bigtable can store is Long.MAX_VALUE/1000, any value larger than that is converted to Long.MAX_VALUE/1000. As a result, large reversed timestamp values might not convert correctly.

## Administration

This section describes methods in the interface [`org.apache.hadoop.hbase.client.Admin`](https://hbase.apache.org/apidocs/org/apache/hadoop/hbase/client/Admin.html) that are not available on Bigtable, or that behave differently on Bigtable than on HBase. These lists are not exhaustive, and they might not reflect the most recently added HBase API methods.

Most of these methods are unnecessary on Bigtable, because management tasks are handled automatically. A few methods are not available because they relate to features that Bigtable does not support.

### General maintenance tasks

Bigtable handles most maintenance tasks automatically. As a result, the following methods are not available:

  * `abort(String why, Throwable e)`
  * `balancer()`
  * `enableCatalogJanitor(boolean enable)`
  * `getMasterInfoPort()`
  * `getOperationTimeout()`
  * `isCatalogJanitorEnabled()`
  * `rollWALWriter(ServerName serverName)`
  * `runCatalogScan()`
  * `setBalancerRunning(boolean on, boolean synchronous)`
  * `shutdown()`
  * `stopMaster()`
  * `updateConfiguration()`
  * `updateConfiguration(ServerName serverName)`



### Locality groups

Bigtable does not allow you to specify locality groups for column families. As a result, you cannot call HBase methods that return a locality group.

### Namespaces

Bigtable does not use namespaces. You can [use row key prefixes to simulate namespaces](https://docs.cloud.google.com/bigtable/docs/schema-design#multitenancy). The following methods are not available:

  * `createNamespace(NamespaceDescriptor descriptor)`
  * `deleteNamespace(String name)`
  * `getNamespaceDescriptor(String name)`
  * `listNamespaceDescriptors()`
  * `listTableDescriptorsByNamespace(String name)`
  * `listTableNamesByNamespace(String name)`
  * `modifyNamespace(NamespaceDescriptor descriptor)`



### Region management

Bigtable uses tablets, which are similar to regions. Bigtable manages your tablets automatically. As a result, the following methods are not available:

  * `assign(byte[] regionName)`
  * `closeRegion(byte[] regionname, String serverName)`
  * `closeRegion(ServerName sn, HRegionInfo hri)`
  * `closeRegion(String regionname, String serverName)`
  * `closeRegionWithEncodedRegionName(String encodedRegionName, String serverName)`
  * `compactRegion(byte[] regionName)`
  * `compactRegion(byte[] regionName, byte[] columnFamily)`
  * `compactRegionServer(ServerName sn, boolean major)`
  * `flushRegion(byte[] regionName)`
  * `getAlterStatus(byte[] tableName)`
  * `getAlterStatus(TableName tableName)`
  * `getCompactionStateForRegion(byte[] regionName)`
  * `getOnlineRegions(ServerName sn)`
  * `majorCompactRegion(byte[] regionName)`
  * `majorCompactRegion(byte[] regionName, byte[] columnFamily)`
  * `mergeRegions(byte[] encodedNameOfRegionA, byte[] encodedNameOfRegionB, boolean forcible)`
  * `move(byte[] encodedRegionName, byte[] destServerName)`
  * `offline(byte[] regionName)`
  * `splitRegion(byte[] regionName)`
  * `splitRegion(byte[] regionName, byte[] splitPoint)`
  * `stopRegionServer(String hostnamePort)`
  * `unassign(byte[] regionName, boolean force)`



### Snapshots

The following methods are not available.

  * `deleteSnapshots(Pattern pattern)`
  * `deleteSnapshots(String regex)`
  * `isSnapshotFinished(HBaseProtos.SnapshotDescription snapshot)`
  * `restoreSnapshot(byte[] snapshotName)`
  * `restoreSnapshot(String snapshotName)`
  * `restoreSnapshot(byte[] snapshotName, boolean takeFailSafeSnapshot)`
  * `restoreSnapshot(String snapshotName, boolean takeFailSafeSnapshot)`
  * `snapshot(HBaseProtos.SnapshotDescription snapshot)`



### Table management

Tasks such as table compaction are handled automatically. As a result, the following methods are not available:

  * `compact(TableName tableName)`
  * `compact(TableName tableName, byte[] columnFamily)`
  * `flush(TableName tableName)`
  * `getCompactionState(TableName tableName)`
  * `majorCompact(TableName tableName)`
  * `majorCompact(TableName tableName, byte[] columnFamily)`
  * `modifyTable(TableName tableName, HTableDescriptor htd)`
  * `split(TableName tableName)`
  * `split(TableName tableName, byte[] splitPoint)`



### Coprocessors

Bigtable does not support coprocessors. As a result, the following methods are not available:

  * `coprocessorService()`
  * `coprocessorService(ServerName serverName)`
  * `getMasterCoprocessors()`



### Distributed procedures

Bigtable does not support distributed procedures. As a result, the following methods are not available:

  * `execProcedure(String signature, String instance, Map<String, String> props)`
  * `execProcedureWithRet(String signature, String instance, Map<String, String> props)`
  * `isProcedureFinished(String signature, String instance, Map<String, String> props)`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
