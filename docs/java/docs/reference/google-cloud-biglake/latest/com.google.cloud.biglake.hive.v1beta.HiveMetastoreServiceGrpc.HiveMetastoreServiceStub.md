---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceGrpc.HiveMetastoreServiceStub
title: Class HiveMetastoreServiceGrpc.HiveMetastoreServiceStub (0.87.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:34:59.964556+00:00
---

# Class HiveMetastoreServiceGrpc.HiveMetastoreServiceStub (0.87.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceGrpc.HiveMetastoreServiceStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class HiveMetastoreServiceGrpc.HiveMetastoreServiceStub (0.87.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.87.0 (latest)  0.83.0  0.82.0  0.81.1  0.79.0  0.76.0  0.75.0  0.73.0  0.71.0  0.70.0  0.69.0  0.68.0  0.66.0  0.64.0  0.63.0  0.62.0  0.61.0  0.60.0  0.58.0  0.56.0  0.55.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static final class HiveMetastoreServiceGrpc.HiveMetastoreServiceStub extends AbstractAsyncStub<HiveMetastoreServiceGrpc.HiveMetastoreServiceStub>

A stub to allow clients to do asynchronous rpc calls to service HiveMetastoreService.

Hive Metastore Service is a biglake service that allows users to manage their external Hive catalogs. Full API compatibility with OSS Hive Metastore APIs is not supported. The methods match the Hive Metastore API spec mostly except for a few exceptions. These include listing resources with pattern, environment context which are combined in a single List API, return of ListResponse object instead of a list of resources, transactions, locks, etc. The BigLake Hive Metastore API defines the following resources:

  * A collection of Google Cloud projects: `/projects/*`
  * Each project has a collection of catalogs: `/catalogs/*`
  * Each catalog has a collection of databases: `/databases/*`
  * Each database has a collection of tables: `/tables/*`



## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractAsyncStub > HiveMetastoreServiceGrpc.HiveMetastoreServiceStub

## Inherited Members

io.grpc.stub.AbstractAsyncStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel)

io.grpc.stub.AbstractAsyncStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel,io.grpc.CallOptions)

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

### batchCreatePartitions(BatchCreatePartitionsRequest request, StreamObserver<BatchCreatePartitionsResponse> responseObserver)
    
    
    public void batchCreatePartitions(BatchCreatePartitionsRequest request, StreamObserver<BatchCreatePartitionsResponse> responseObserver)

Adds partitions to a table.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchCreatePartitionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.BatchCreatePartitionsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[BatchCreatePartitionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.BatchCreatePartitionsResponse)>`  
  
  
### batchDeletePartitions(BatchDeletePartitionsRequest request, StreamObserver<Empty> responseObserver)
    
    
    public void batchDeletePartitions(BatchDeletePartitionsRequest request, StreamObserver<Empty> responseObserver)

Deletes partitions from a table.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchDeletePartitionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.BatchDeletePartitionsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### batchUpdatePartitions(BatchUpdatePartitionsRequest request, StreamObserver<BatchUpdatePartitionsResponse> responseObserver)
    
    
    public void batchUpdatePartitions(BatchUpdatePartitionsRequest request, StreamObserver<BatchUpdatePartitionsResponse> responseObserver)

Updates partitions in a table.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchUpdatePartitionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.BatchUpdatePartitionsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[BatchUpdatePartitionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.BatchUpdatePartitionsResponse)>`  
  
  
### build(Channel channel, CallOptions callOptions)
    
    
    protected HiveMetastoreServiceGrpc.HiveMetastoreServiceStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[HiveMetastoreServiceGrpc.HiveMetastoreServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceGrpc.HiveMetastoreServiceStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createHiveCatalog(CreateHiveCatalogRequest request, StreamObserver<HiveCatalog> responseObserver)
    
    
    public void createHiveCatalog(CreateHiveCatalogRequest request, StreamObserver<HiveCatalog> responseObserver)

Creates a new hive catalog.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateHiveCatalogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.CreateHiveCatalogRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[HiveCatalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveCatalog)>`  
  
  
### createHiveDatabase(CreateHiveDatabaseRequest request, StreamObserver<HiveDatabase> responseObserver)
    
    
    public void createHiveDatabase(CreateHiveDatabaseRequest request, StreamObserver<HiveDatabase> responseObserver)

Creates a new database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateHiveDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.CreateHiveDatabaseRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[HiveDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveDatabase)>`  
  
  
### createHiveTable(CreateHiveTableRequest request, StreamObserver<HiveTable> responseObserver)
    
    
    public void createHiveTable(CreateHiveTableRequest request, StreamObserver<HiveTable> responseObserver)

Creates a new hive table.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateHiveTableRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.CreateHiveTableRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[HiveTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveTable)>`  
  
  
### deleteHiveCatalog(DeleteHiveCatalogRequest request, StreamObserver<Empty> responseObserver)
    
    
    public void deleteHiveCatalog(DeleteHiveCatalogRequest request, StreamObserver<Empty> responseObserver)

Deletes an existing catalog specified by the catalog ID. Delete will fail if the catalog is not empty.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteHiveCatalogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.DeleteHiveCatalogRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### deleteHiveDatabase(DeleteHiveDatabaseRequest request, StreamObserver<Empty> responseObserver)
    
    
    public void deleteHiveDatabase(DeleteHiveDatabaseRequest request, StreamObserver<Empty> responseObserver)

Deletes an existing database specified by the database name.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteHiveDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.DeleteHiveDatabaseRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### deleteHiveTable(DeleteHiveTableRequest request, StreamObserver<Empty> responseObserver)
    
    
    public void deleteHiveTable(DeleteHiveTableRequest request, StreamObserver<Empty> responseObserver)

Deletes an existing table specified by the table name.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteHiveTableRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.DeleteHiveTableRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### failoverHiveCatalog(FailoverHiveCatalogRequest request, StreamObserver<FailoverHiveCatalogResponse> responseObserver)
    
    
    public void failoverHiveCatalog(FailoverHiveCatalogRequest request, StreamObserver<FailoverHiveCatalogResponse> responseObserver)

Failover the catalog to a new primary replica region.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FailoverHiveCatalogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.FailoverHiveCatalogRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[FailoverHiveCatalogResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.FailoverHiveCatalogResponse)>`  
  
  
### getHiveCatalog(GetHiveCatalogRequest request, StreamObserver<HiveCatalog> responseObserver)
    
    
    public void getHiveCatalog(GetHiveCatalogRequest request, StreamObserver<HiveCatalog> responseObserver)

Gets the catalog specified by the resource name.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetHiveCatalogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.GetHiveCatalogRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[HiveCatalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveCatalog)>`  
  
  
### getHiveDatabase(GetHiveDatabaseRequest request, StreamObserver<HiveDatabase> responseObserver)
    
    
    public void getHiveDatabase(GetHiveDatabaseRequest request, StreamObserver<HiveDatabase> responseObserver)

Gets the database specified by the resource name.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetHiveDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.GetHiveDatabaseRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[HiveDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveDatabase)>`  
  
  
### getHiveTable(GetHiveTableRequest request, StreamObserver<HiveTable> responseObserver)
    
    
    public void getHiveTable(GetHiveTableRequest request, StreamObserver<HiveTable> responseObserver)

Gets the table specified by the resource name.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetHiveTableRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.GetHiveTableRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[HiveTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveTable)>`  
  
  
### listHiveCatalogs(ListHiveCatalogsRequest request, StreamObserver<ListHiveCatalogsResponse> responseObserver)
    
    
    public void listHiveCatalogs(ListHiveCatalogsRequest request, StreamObserver<ListHiveCatalogsResponse> responseObserver)

List all catalogs in a specified project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListHiveCatalogsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListHiveCatalogsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListHiveCatalogsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListHiveCatalogsResponse)>`  
  
  
### listHiveDatabases(ListHiveDatabasesRequest request, StreamObserver<ListHiveDatabasesResponse> responseObserver)
    
    
    public void listHiveDatabases(ListHiveDatabasesRequest request, StreamObserver<ListHiveDatabasesResponse> responseObserver)

List all databases in a specified catalog.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListHiveDatabasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListHiveDatabasesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListHiveDatabasesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListHiveDatabasesResponse)>`  
  
  
### listHiveTables(ListHiveTablesRequest request, StreamObserver<ListHiveTablesResponse> responseObserver)
    
    
    public void listHiveTables(ListHiveTablesRequest request, StreamObserver<ListHiveTablesResponse> responseObserver)

List all hive tables in a specified project under the hive catalog and database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListHiveTablesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListHiveTablesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListHiveTablesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListHiveTablesResponse)>`  
  
  
### listPartitions(ListPartitionsRequest request, StreamObserver<ListPartitionsResponse> responseObserver)
    
    
    public void listPartitions(ListPartitionsRequest request, StreamObserver<ListPartitionsResponse> responseObserver)

Streams list of partitions from a table.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListPartitionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListPartitionsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListPartitionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListPartitionsResponse)>`  
  
  
### updateHiveCatalog(UpdateHiveCatalogRequest request, StreamObserver<HiveCatalog> responseObserver)
    
    
    public void updateHiveCatalog(UpdateHiveCatalogRequest request, StreamObserver<HiveCatalog> responseObserver)

Updates an existing catalog.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateHiveCatalogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.UpdateHiveCatalogRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[HiveCatalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveCatalog)>`  
  
  
### updateHiveDatabase(UpdateHiveDatabaseRequest request, StreamObserver<HiveDatabase> responseObserver)
    
    
    public void updateHiveDatabase(UpdateHiveDatabaseRequest request, StreamObserver<HiveDatabase> responseObserver)

Updates an existing database specified by the database name.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateHiveDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.UpdateHiveDatabaseRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[HiveDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveDatabase)>`  
  
  
### updateHiveTable(UpdateHiveTableRequest request, StreamObserver<HiveTable> responseObserver)
    
    
    public void updateHiveTable(UpdateHiveTableRequest request, StreamObserver<HiveTable> responseObserver)

Updates an existing table specified by the table name.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateHiveTableRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.UpdateHiveTableRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[HiveTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveTable)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
