---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceGrpc
title: Class HiveMetastoreServiceGrpc (0.87.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:34:59.419328+00:00
---

# Class HiveMetastoreServiceGrpc (0.87.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceGrpc

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class HiveMetastoreServiceGrpc (0.87.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.87.0 (latest)  0.83.0  0.82.0  0.81.1  0.79.0  0.76.0  0.75.0  0.73.0  0.71.0  0.70.0  0.69.0  0.68.0  0.66.0  0.64.0  0.63.0  0.62.0  0.61.0  0.60.0  0.58.0  0.56.0  0.55.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public final class HiveMetastoreServiceGrpc

Hive Metastore Service is a biglake service that allows users to manage their external Hive catalogs. Full API compatibility with OSS Hive Metastore APIs is not supported. The methods match the Hive Metastore API spec mostly except for a few exceptions. These include listing resources with pattern, environment context which are combined in a single List API, return of ListResponse object instead of a list of resources, transactions, locks, etc. The BigLake Hive Metastore API defines the following resources:

  * A collection of Google Cloud projects: `/projects/*`
  * Each project has a collection of catalogs: `/catalogs/*`
  * Each catalog has a collection of databases: `/databases/*`
  * Each database has a collection of tables: `/tables/*`



## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > HiveMetastoreServiceGrpc

## Inherited Members

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

## Static Fields 

### SERVICE_NAME
    
    
    public static final String SERVICE_NAME

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
## Static Methods 

### bindService(HiveMetastoreServiceGrpc.AsyncService service)
    
    
    public static final ServerServiceDefinition bindService(HiveMetastoreServiceGrpc.AsyncService service)

**Parameter**  
---  
**Name** | **Description**  
`service` | `[HiveMetastoreServiceGrpc.AsyncService](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceGrpc.AsyncService)`  
  
**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServerServiceDefinition` |   
  
### getBatchCreatePartitionsMethod()
    
    
    public static MethodDescriptor<BatchCreatePartitionsRequest,BatchCreatePartitionsResponse> getBatchCreatePartitionsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[BatchCreatePartitionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.BatchCreatePartitionsRequest),[BatchCreatePartitionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.BatchCreatePartitionsResponse)>` |   
  
### getBatchDeletePartitionsMethod()
    
    
    public static MethodDescriptor<BatchDeletePartitionsRequest,Empty> getBatchDeletePartitionsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[BatchDeletePartitionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.BatchDeletePartitionsRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getBatchUpdatePartitionsMethod()
    
    
    public static MethodDescriptor<BatchUpdatePartitionsRequest,BatchUpdatePartitionsResponse> getBatchUpdatePartitionsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[BatchUpdatePartitionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.BatchUpdatePartitionsRequest),[BatchUpdatePartitionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.BatchUpdatePartitionsResponse)>` |   
  
### getCreateHiveCatalogMethod()
    
    
    public static MethodDescriptor<CreateHiveCatalogRequest,HiveCatalog> getCreateHiveCatalogMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateHiveCatalogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.CreateHiveCatalogRequest),[HiveCatalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveCatalog)>` |   
  
### getCreateHiveDatabaseMethod()
    
    
    public static MethodDescriptor<CreateHiveDatabaseRequest,HiveDatabase> getCreateHiveDatabaseMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateHiveDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.CreateHiveDatabaseRequest),[HiveDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveDatabase)>` |   
  
### getCreateHiveTableMethod()
    
    
    public static MethodDescriptor<CreateHiveTableRequest,HiveTable> getCreateHiveTableMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateHiveTableRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.CreateHiveTableRequest),[HiveTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveTable)>` |   
  
### getDeleteHiveCatalogMethod()
    
    
    public static MethodDescriptor<DeleteHiveCatalogRequest,Empty> getDeleteHiveCatalogMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteHiveCatalogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.DeleteHiveCatalogRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getDeleteHiveDatabaseMethod()
    
    
    public static MethodDescriptor<DeleteHiveDatabaseRequest,Empty> getDeleteHiveDatabaseMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteHiveDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.DeleteHiveDatabaseRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getDeleteHiveTableMethod()
    
    
    public static MethodDescriptor<DeleteHiveTableRequest,Empty> getDeleteHiveTableMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteHiveTableRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.DeleteHiveTableRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getFailoverHiveCatalogMethod()
    
    
    public static MethodDescriptor<FailoverHiveCatalogRequest,FailoverHiveCatalogResponse> getFailoverHiveCatalogMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[FailoverHiveCatalogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.FailoverHiveCatalogRequest),[FailoverHiveCatalogResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.FailoverHiveCatalogResponse)>` |   
  
### getGetHiveCatalogMethod()
    
    
    public static MethodDescriptor<GetHiveCatalogRequest,HiveCatalog> getGetHiveCatalogMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetHiveCatalogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.GetHiveCatalogRequest),[HiveCatalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveCatalog)>` |   
  
### getGetHiveDatabaseMethod()
    
    
    public static MethodDescriptor<GetHiveDatabaseRequest,HiveDatabase> getGetHiveDatabaseMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetHiveDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.GetHiveDatabaseRequest),[HiveDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveDatabase)>` |   
  
### getGetHiveTableMethod()
    
    
    public static MethodDescriptor<GetHiveTableRequest,HiveTable> getGetHiveTableMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetHiveTableRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.GetHiveTableRequest),[HiveTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveTable)>` |   
  
### getListHiveCatalogsMethod()
    
    
    public static MethodDescriptor<ListHiveCatalogsRequest,ListHiveCatalogsResponse> getListHiveCatalogsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListHiveCatalogsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListHiveCatalogsRequest),[ListHiveCatalogsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListHiveCatalogsResponse)>` |   
  
### getListHiveDatabasesMethod()
    
    
    public static MethodDescriptor<ListHiveDatabasesRequest,ListHiveDatabasesResponse> getListHiveDatabasesMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListHiveDatabasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListHiveDatabasesRequest),[ListHiveDatabasesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListHiveDatabasesResponse)>` |   
  
### getListHiveTablesMethod()
    
    
    public static MethodDescriptor<ListHiveTablesRequest,ListHiveTablesResponse> getListHiveTablesMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListHiveTablesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListHiveTablesRequest),[ListHiveTablesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListHiveTablesResponse)>` |   
  
### getListPartitionsMethod()
    
    
    public static MethodDescriptor<ListPartitionsRequest,ListPartitionsResponse> getListPartitionsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListPartitionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListPartitionsRequest),[ListPartitionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListPartitionsResponse)>` |   
  
### getServiceDescriptor()
    
    
    public static ServiceDescriptor getServiceDescriptor()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServiceDescriptor` |   
  
### getUpdateHiveCatalogMethod()
    
    
    public static MethodDescriptor<UpdateHiveCatalogRequest,HiveCatalog> getUpdateHiveCatalogMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateHiveCatalogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.UpdateHiveCatalogRequest),[HiveCatalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveCatalog)>` |   
  
### getUpdateHiveDatabaseMethod()
    
    
    public static MethodDescriptor<UpdateHiveDatabaseRequest,HiveDatabase> getUpdateHiveDatabaseMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateHiveDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.UpdateHiveDatabaseRequest),[HiveDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveDatabase)>` |   
  
### getUpdateHiveTableMethod()
    
    
    public static MethodDescriptor<UpdateHiveTableRequest,HiveTable> getUpdateHiveTableMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateHiveTableRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.UpdateHiveTableRequest),[HiveTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveTable)>` |   
  
### newBlockingStub(Channel channel)
    
    
    public static HiveMetastoreServiceGrpc.HiveMetastoreServiceBlockingStub newBlockingStub(Channel channel)

Creates a new blocking-style stub that supports unary and streaming output calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[HiveMetastoreServiceGrpc.HiveMetastoreServiceBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceGrpc.HiveMetastoreServiceBlockingStub)` |   
  
### newBlockingV2Stub(Channel channel)
    
    
    public static HiveMetastoreServiceGrpc.HiveMetastoreServiceBlockingV2Stub newBlockingV2Stub(Channel channel)

Creates a new blocking-style stub that supports all types of calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[HiveMetastoreServiceGrpc.HiveMetastoreServiceBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceGrpc.HiveMetastoreServiceBlockingV2Stub)` |   
  
### newFutureStub(Channel channel)
    
    
    public static HiveMetastoreServiceGrpc.HiveMetastoreServiceFutureStub newFutureStub(Channel channel)

Creates a new ListenableFuture-style stub that supports unary calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[HiveMetastoreServiceGrpc.HiveMetastoreServiceFutureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceGrpc.HiveMetastoreServiceFutureStub)` |   
  
### newStub(Channel channel)
    
    
    public static HiveMetastoreServiceGrpc.HiveMetastoreServiceStub newStub(Channel channel)

Creates a new async stub that supports all call types for the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[HiveMetastoreServiceGrpc.HiveMetastoreServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceGrpc.HiveMetastoreServiceStub)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
