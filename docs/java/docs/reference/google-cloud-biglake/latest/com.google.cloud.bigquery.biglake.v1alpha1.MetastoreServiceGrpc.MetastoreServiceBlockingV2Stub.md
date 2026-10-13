---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.bigquery.biglake.v1alpha1.MetastoreServiceGrpc.MetastoreServiceBlockingV2Stub
title: Class MetastoreServiceGrpc.MetastoreServiceBlockingV2Stub (0.87.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:45:57.247291+00:00
---

# Class MetastoreServiceGrpc.MetastoreServiceBlockingV2Stub (0.87.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.bigquery.biglake.v1alpha1.MetastoreServiceGrpc.MetastoreServiceBlockingV2Stub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class MetastoreServiceGrpc.MetastoreServiceBlockingV2Stub (0.87.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.87.0 (latest)  0.83.0  0.82.0  0.81.1  0.79.0  0.76.0  0.75.0  0.73.0  0.71.0  0.70.0  0.69.0  0.68.0  0.66.0  0.64.0  0.63.0  0.62.0  0.61.0  0.60.0  0.58.0  0.56.0  0.55.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static final class MetastoreServiceGrpc.MetastoreServiceBlockingV2Stub extends AbstractBlockingStub<MetastoreServiceGrpc.MetastoreServiceBlockingV2Stub>

A stub to allow clients to do synchronous rpc calls to service MetastoreService.

BigLake Metastore is a serverless, highly available, multi-tenant runtime metastore for Google Cloud Data Analytics products. The BigLake Metastore API defines the following resource model:

  * A collection of Google Cloud projects: `/projects/*`
  * Each project has a collection of available locations: `/locations/*`
  * Each location has a collection of catalogs: `/catalogs/*`
  * Each catalog has a collection of databases: `/databases/*`
  * Each database has a collection of tables: `/tables/*`



## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractBlockingStub > MetastoreServiceGrpc.MetastoreServiceBlockingV2Stub

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

### build(Channel channel, CallOptions callOptions)
    
    
    protected MetastoreServiceGrpc.MetastoreServiceBlockingV2Stub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[MetastoreServiceGrpc.MetastoreServiceBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.bigquery.biglake.v1alpha1.MetastoreServiceGrpc.MetastoreServiceBlockingV2Stub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### checkLock(CheckLockRequest request)
    
    
    public Lock checkLock(CheckLockRequest request)

Checks the state of a lock specified by the lock ID.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CheckLockRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.bigquery.biglake.v1alpha1.CheckLockRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Lock](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.bigquery.biglake.v1alpha1.Lock)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createCatalog(CreateCatalogRequest request)
    
    
    public Catalog createCatalog(CreateCatalogRequest request)

Creates a new catalog.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateCatalogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.bigquery.biglake.v1alpha1.CreateCatalogRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Catalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.bigquery.biglake.v1alpha1.Catalog)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createDatabase(CreateDatabaseRequest request)
    
    
    public Database createDatabase(CreateDatabaseRequest request)

Creates a new database.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.bigquery.biglake.v1alpha1.CreateDatabaseRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.bigquery.biglake.v1alpha1.Database)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createLock(CreateLockRequest request)
    
    
    public Lock createLock(CreateLockRequest request)

Creates a new lock.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateLockRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.bigquery.biglake.v1alpha1.CreateLockRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Lock](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.bigquery.biglake.v1alpha1.Lock)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createTable(CreateTableRequest request)
    
    
    public Table createTable(CreateTableRequest request)

Creates a new table.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateTableRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.bigquery.biglake.v1alpha1.CreateTableRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.bigquery.biglake.v1alpha1.Table)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteCatalog(DeleteCatalogRequest request)
    
    
    public Catalog deleteCatalog(DeleteCatalogRequest request)

Deletes an existing catalog specified by the catalog ID.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteCatalogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.bigquery.biglake.v1alpha1.DeleteCatalogRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Catalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.bigquery.biglake.v1alpha1.Catalog)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteDatabase(DeleteDatabaseRequest request)
    
    
    public Database deleteDatabase(DeleteDatabaseRequest request)

Deletes an existing database specified by the database ID.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.bigquery.biglake.v1alpha1.DeleteDatabaseRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.bigquery.biglake.v1alpha1.Database)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteLock(DeleteLockRequest request)
    
    
    public Empty deleteLock(DeleteLockRequest request)

Deletes an existing lock specified by the lock ID.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteLockRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.bigquery.biglake.v1alpha1.DeleteLockRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteTable(DeleteTableRequest request)
    
    
    public Table deleteTable(DeleteTableRequest request)

Deletes an existing table specified by the table ID.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteTableRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.bigquery.biglake.v1alpha1.DeleteTableRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.bigquery.biglake.v1alpha1.Table)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getCatalog(GetCatalogRequest request)
    
    
    public Catalog getCatalog(GetCatalogRequest request)

Gets the catalog specified by the resource name.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetCatalogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.bigquery.biglake.v1alpha1.GetCatalogRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Catalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.bigquery.biglake.v1alpha1.Catalog)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getDatabase(GetDatabaseRequest request)
    
    
    public Database getDatabase(GetDatabaseRequest request)

Gets the database specified by the resource name.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.bigquery.biglake.v1alpha1.GetDatabaseRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.bigquery.biglake.v1alpha1.Database)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getTable(GetTableRequest request)
    
    
    public Table getTable(GetTableRequest request)

Gets the table specified by the resource name.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetTableRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.bigquery.biglake.v1alpha1.GetTableRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.bigquery.biglake.v1alpha1.Table)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listCatalogs(ListCatalogsRequest request)
    
    
    public ListCatalogsResponse listCatalogs(ListCatalogsRequest request)

List all catalogs in a specified project.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListCatalogsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.bigquery.biglake.v1alpha1.ListCatalogsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListCatalogsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.bigquery.biglake.v1alpha1.ListCatalogsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listDatabases(ListDatabasesRequest request)
    
    
    public ListDatabasesResponse listDatabases(ListDatabasesRequest request)

List all databases in a specified catalog.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDatabasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.bigquery.biglake.v1alpha1.ListDatabasesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListDatabasesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.bigquery.biglake.v1alpha1.ListDatabasesResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listLocks(ListLocksRequest request)
    
    
    public ListLocksResponse listLocks(ListLocksRequest request)

List all locks in a specified database.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListLocksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.bigquery.biglake.v1alpha1.ListLocksRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListLocksResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.bigquery.biglake.v1alpha1.ListLocksResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listTables(ListTablesRequest request)
    
    
    public ListTablesResponse listTables(ListTablesRequest request)

List all tables in a specified database.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListTablesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.bigquery.biglake.v1alpha1.ListTablesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListTablesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.bigquery.biglake.v1alpha1.ListTablesResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### renameTable(RenameTableRequest request)
    
    
    public Table renameTable(RenameTableRequest request)

Renames an existing table specified by the table ID.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RenameTableRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.bigquery.biglake.v1alpha1.RenameTableRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.bigquery.biglake.v1alpha1.Table)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateDatabase(UpdateDatabaseRequest request)
    
    
    public Database updateDatabase(UpdateDatabaseRequest request)

Updates an existing database specified by the database ID.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.bigquery.biglake.v1alpha1.UpdateDatabaseRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.bigquery.biglake.v1alpha1.Database)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateTable(UpdateTableRequest request)
    
    
    public Table updateTable(UpdateTableRequest request)

Updates an existing table specified by the table ID.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateTableRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.bigquery.biglake.v1alpha1.UpdateTableRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.bigquery.biglake.v1alpha1.Table)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
