---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceGrpc.HiveMetastoreServiceBlockingStub
title: Class HiveMetastoreServiceGrpc.HiveMetastoreServiceBlockingStub (0.87.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:34:59.661049+00:00
---

# Class HiveMetastoreServiceGrpc.HiveMetastoreServiceBlockingStub (0.87.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceGrpc.HiveMetastoreServiceBlockingStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class HiveMetastoreServiceGrpc.HiveMetastoreServiceBlockingStub (0.87.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.87.0 (latest)  0.83.0  0.82.0  0.81.1  0.79.0  0.76.0  0.75.0  0.73.0  0.71.0  0.70.0  0.69.0  0.68.0  0.66.0  0.64.0  0.63.0  0.62.0  0.61.0  0.60.0  0.58.0  0.56.0  0.55.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static final class HiveMetastoreServiceGrpc.HiveMetastoreServiceBlockingStub extends AbstractBlockingStub<HiveMetastoreServiceGrpc.HiveMetastoreServiceBlockingStub>

A stub to allow clients to do limited synchronous rpc calls to service HiveMetastoreService.

Hive Metastore Service is a biglake service that allows users to manage their external Hive catalogs. Full API compatibility with OSS Hive Metastore APIs is not supported. The methods match the Hive Metastore API spec mostly except for a few exceptions. These include listing resources with pattern, environment context which are combined in a single List API, return of ListResponse object instead of a list of resources, transactions, locks, etc. The BigLake Hive Metastore API defines the following resources:

  * A collection of Google Cloud projects: `/projects/*`
  * Each project has a collection of catalogs: `/catalogs/*`
  * Each catalog has a collection of databases: `/databases/*`
  * Each database has a collection of tables: `/tables/*`



## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractBlockingStub > HiveMetastoreServiceGrpc.HiveMetastoreServiceBlockingStub

## Inherited Members

io.grpc.stub.AbstractBlockingStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel)

io.grpc.stub.AbstractBlockingStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel,io.grpc.CallOptions)

io.grpc.stub.AbstractStub.<T>withOption(io.grpc.CallOptions.Key<T>,T)

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

io.grpc.stub.AbstractStub.getCallOptions()

io.grpc.stub.AbstractStub.getChannel()

io.grpc.stub.AbstractStub.withCallCredentials(io.grpc.CallCredentials)

io.grpc.stub.AbstractStub.withChannel(io.grpc.Channel)

io.grpc.stub.AbstractStub.withCompression(java.lang.String)

io.grpc.stub.AbstractStub.withDeadline(io.grpc.Deadline)

io.grpc.stub.AbstractStub.withDeadlineAfter(java.time.Duration)

io.grpc.stub.AbstractStub.withDeadlineAfter(long,java.util.concurrent.TimeUnit)

io.grpc.stub.AbstractStub.withExecutor(java.util.concurrent.Executor)

io.grpc.stub.AbstractStub.withInterceptors(io.grpc.ClientInterceptor...)

io.grpc.stub.AbstractStub.withMaxInboundMessageSize(int)

io.grpc.stub.AbstractStub.withMaxOutboundMessageSize(int)

io.grpc.stub.AbstractStub.withOnReadyThreshold(int)

io.grpc.stub.AbstractStub.withWaitForReady()

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Methods 

### batchCreatePartitions(BatchCreatePartitionsRequest request)
    
    
    public BatchCreatePartitionsResponse batchCreatePartitions(BatchCreatePartitionsRequest request)

Adds partitions to a table.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchCreatePartitionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.BatchCreatePartitionsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreatePartitionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.BatchCreatePartitionsResponse)` |   
  
### batchDeletePartitions(BatchDeletePartitionsRequest request)
    
    
    public Empty batchDeletePartitions(BatchDeletePartitionsRequest request)

Deletes partitions from a table.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchDeletePartitionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.BatchDeletePartitionsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)` |   
  
### batchUpdatePartitions(BatchUpdatePartitionsRequest request)
    
    
    public BatchUpdatePartitionsResponse batchUpdatePartitions(BatchUpdatePartitionsRequest request)

Updates partitions in a table.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchUpdatePartitionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.BatchUpdatePartitionsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdatePartitionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.BatchUpdatePartitionsResponse)` |   
  
### build(Channel channel, CallOptions callOptions)
    
    
    protected HiveMetastoreServiceGrpc.HiveMetastoreServiceBlockingStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[HiveMetastoreServiceGrpc.HiveMetastoreServiceBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceGrpc.HiveMetastoreServiceBlockingStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createHiveCatalog(CreateHiveCatalogRequest request)
    
    
    public HiveCatalog createHiveCatalog(CreateHiveCatalogRequest request)

Creates a new hive catalog.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateHiveCatalogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.CreateHiveCatalogRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HiveCatalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveCatalog)` |   
  
### createHiveDatabase(CreateHiveDatabaseRequest request)
    
    
    public HiveDatabase createHiveDatabase(CreateHiveDatabaseRequest request)

Creates a new database.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateHiveDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.CreateHiveDatabaseRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HiveDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveDatabase)` |   
  
### createHiveTable(CreateHiveTableRequest request)
    
    
    public HiveTable createHiveTable(CreateHiveTableRequest request)

Creates a new hive table.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateHiveTableRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.CreateHiveTableRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HiveTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveTable)` |   
  
### deleteHiveCatalog(DeleteHiveCatalogRequest request)
    
    
    public Empty deleteHiveCatalog(DeleteHiveCatalogRequest request)

Deletes an existing catalog specified by the catalog ID. Delete will fail if the catalog is not empty.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteHiveCatalogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.DeleteHiveCatalogRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)` |   
  
### deleteHiveDatabase(DeleteHiveDatabaseRequest request)
    
    
    public Empty deleteHiveDatabase(DeleteHiveDatabaseRequest request)

Deletes an existing database specified by the database name.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteHiveDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.DeleteHiveDatabaseRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)` |   
  
### deleteHiveTable(DeleteHiveTableRequest request)
    
    
    public Empty deleteHiveTable(DeleteHiveTableRequest request)

Deletes an existing table specified by the table name.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteHiveTableRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.DeleteHiveTableRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)` |   
  
### failoverHiveCatalog(FailoverHiveCatalogRequest request)
    
    
    public FailoverHiveCatalogResponse failoverHiveCatalog(FailoverHiveCatalogRequest request)

Failover the catalog to a new primary replica region.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FailoverHiveCatalogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.FailoverHiveCatalogRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FailoverHiveCatalogResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.FailoverHiveCatalogResponse)` |   
  
### getHiveCatalog(GetHiveCatalogRequest request)
    
    
    public HiveCatalog getHiveCatalog(GetHiveCatalogRequest request)

Gets the catalog specified by the resource name.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetHiveCatalogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.GetHiveCatalogRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HiveCatalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveCatalog)` |   
  
### getHiveDatabase(GetHiveDatabaseRequest request)
    
    
    public HiveDatabase getHiveDatabase(GetHiveDatabaseRequest request)

Gets the database specified by the resource name.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetHiveDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.GetHiveDatabaseRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HiveDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveDatabase)` |   
  
### getHiveTable(GetHiveTableRequest request)
    
    
    public HiveTable getHiveTable(GetHiveTableRequest request)

Gets the table specified by the resource name.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetHiveTableRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.GetHiveTableRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HiveTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveTable)` |   
  
### listHiveCatalogs(ListHiveCatalogsRequest request)
    
    
    public ListHiveCatalogsResponse listHiveCatalogs(ListHiveCatalogsRequest request)

List all catalogs in a specified project.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListHiveCatalogsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListHiveCatalogsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListHiveCatalogsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListHiveCatalogsResponse)` |   
  
### listHiveDatabases(ListHiveDatabasesRequest request)
    
    
    public ListHiveDatabasesResponse listHiveDatabases(ListHiveDatabasesRequest request)

List all databases in a specified catalog.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListHiveDatabasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListHiveDatabasesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListHiveDatabasesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListHiveDatabasesResponse)` |   
  
### listHiveTables(ListHiveTablesRequest request)
    
    
    public ListHiveTablesResponse listHiveTables(ListHiveTablesRequest request)

List all hive tables in a specified project under the hive catalog and database.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListHiveTablesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListHiveTablesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListHiveTablesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListHiveTablesResponse)` |   
  
### listPartitions(ListPartitionsRequest request)
    
    
    public Iterator<ListPartitionsResponse> listPartitions(ListPartitionsRequest request)

Streams list of partitions from a table.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListPartitionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListPartitionsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Iterator](https://docs.oracle.com/javase/8/docs/api/java/util/Iterator.html)<[ListPartitionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListPartitionsResponse)>` |   
  
### updateHiveCatalog(UpdateHiveCatalogRequest request)
    
    
    public HiveCatalog updateHiveCatalog(UpdateHiveCatalogRequest request)

Updates an existing catalog.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateHiveCatalogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.UpdateHiveCatalogRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HiveCatalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveCatalog)` |   
  
### updateHiveDatabase(UpdateHiveDatabaseRequest request)
    
    
    public HiveDatabase updateHiveDatabase(UpdateHiveDatabaseRequest request)

Updates an existing database specified by the database name.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateHiveDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.UpdateHiveDatabaseRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HiveDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveDatabase)` |   
  
### updateHiveTable(UpdateHiveTableRequest request)
    
    
    public HiveTable updateHiveTable(UpdateHiveTableRequest request)

Updates an existing table specified by the table name.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateHiveTableRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.UpdateHiveTableRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HiveTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveTable)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
