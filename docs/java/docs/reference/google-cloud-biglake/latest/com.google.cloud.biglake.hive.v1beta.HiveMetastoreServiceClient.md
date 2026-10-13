---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceClient
title: Class HiveMetastoreServiceClient (0.87.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:34:25.247793+00:00
---

# Class HiveMetastoreServiceClient (0.87.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class HiveMetastoreServiceClient (0.87.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.87.0 (latest)  0.83.0  0.82.0  0.81.1  0.79.0  0.76.0  0.75.0  0.73.0  0.71.0  0.70.0  0.69.0  0.68.0  0.66.0  0.64.0  0.63.0  0.62.0  0.61.0  0.60.0  0.58.0  0.56.0  0.55.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-biglake/google-cloud-biglake/src/main/java/com/google/cloud/biglake/hive/v1beta/HiveMetastoreServiceClient.java)| [Product Reference](https://cloud.google.com/biglake)  
---|---  
  
Service Description: Hive Metastore Service is a biglake service that allows users to manage their external Hive catalogs. Full API compatibility with OSS Hive Metastore APIs is not supported. The methods match the Hive Metastore API spec mostly except for a few exceptions. These include listing resources with pattern, environment context which are combined in a single List API, return of ListResponse object instead of a list of resources, transactions, locks, etc.

The BigLake Hive Metastore API defines the following resources:

  * A collection of Google Cloud projects: `/projects/*`
  * Each project has a collection of catalogs: `/catalogs/*`
  * Each catalog has a collection of databases: `/databases/*`
  * Each database has a collection of tables: `/tables/*`



This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       ProjectName parent = ProjectName.of("[PROJECT]");
       HiveCatalog hiveCatalog = HiveCatalog.newBuilder().build();
       String hiveCatalogId = "hiveCatalogId-575314556";
       HiveCatalog response =
           hiveMetastoreServiceClient.createHiveCatalog(parent, hiveCatalog, hiveCatalogId);
     }
     

Note: close() needs to be called on the HiveMetastoreServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateHiveCatalog |  Creates a new hive catalog. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createHiveCatalog(CreateHiveCatalogRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createHiveCatalog(ProjectName parent, HiveCatalog hiveCatalog, String hiveCatalogId) 
  * createHiveCatalog(String parent, HiveCatalog hiveCatalog, String hiveCatalogId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createHiveCatalogCallable() 

  
GetHiveCatalog |  Gets the catalog specified by the resource name. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getHiveCatalog(GetHiveCatalogRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getHiveCatalog(CatalogName name) 
  * getHiveCatalog(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getHiveCatalogCallable() 

  
ListHiveCatalogs |  List all catalogs in a specified project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listHiveCatalogs(ListHiveCatalogsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listHiveCatalogs(ProjectName parent) 
  * listHiveCatalogs(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listHiveCatalogsPagedCallable() 
  * listHiveCatalogsCallable() 

  
UpdateHiveCatalog |  Updates an existing catalog. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateHiveCatalog(UpdateHiveCatalogRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateHiveCatalog(HiveCatalog hiveCatalog, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateHiveCatalogCallable() 

  
DeleteHiveCatalog |  Deletes an existing catalog specified by the catalog ID. Delete will fail if the catalog is not empty. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteHiveCatalog(DeleteHiveCatalogRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteHiveCatalog(CatalogName name) 
  * deleteHiveCatalog(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteHiveCatalogCallable() 

  
CreateHiveDatabase |  Creates a new database. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createHiveDatabase(CreateHiveDatabaseRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createHiveDatabase(CatalogName parent, HiveDatabase hiveDatabase, String hiveDatabaseId) 
  * createHiveDatabase(String parent, HiveDatabase hiveDatabase, String hiveDatabaseId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createHiveDatabaseCallable() 

  
GetHiveDatabase |  Gets the database specified by the resource name. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getHiveDatabase(GetHiveDatabaseRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getHiveDatabase(NamespaceName name) 
  * getHiveDatabase(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getHiveDatabaseCallable() 

  
ListHiveDatabases |  List all databases in a specified catalog. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listHiveDatabases(ListHiveDatabasesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listHiveDatabases(CatalogName parent) 
  * listHiveDatabases(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listHiveDatabasesPagedCallable() 
  * listHiveDatabasesCallable() 

  
UpdateHiveDatabase |  Updates an existing database specified by the database name. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateHiveDatabase(UpdateHiveDatabaseRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateHiveDatabase(HiveDatabase hiveDatabase, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateHiveDatabaseCallable() 

  
DeleteHiveDatabase |  Deletes an existing database specified by the database name. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteHiveDatabase(DeleteHiveDatabaseRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteHiveDatabase(NamespaceName name) 
  * deleteHiveDatabase(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteHiveDatabaseCallable() 

  
CreateHiveTable |  Creates a new hive table. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createHiveTable(CreateHiveTableRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createHiveTable(NamespaceName parent, HiveTable hiveTable, String hiveTableId) 
  * createHiveTable(String parent, HiveTable hiveTable, String hiveTableId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createHiveTableCallable() 

  
GetHiveTable |  Gets the table specified by the resource name. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getHiveTable(GetHiveTableRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getHiveTable(TableName name) 
  * getHiveTable(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getHiveTableCallable() 

  
ListHiveTables |  List all hive tables in a specified project under the hive catalog and database. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listHiveTables(ListHiveTablesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listHiveTables(NamespaceName parent) 
  * listHiveTables(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listHiveTablesPagedCallable() 
  * listHiveTablesCallable() 

  
UpdateHiveTable |  Updates an existing table specified by the table name. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateHiveTable(UpdateHiveTableRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateHiveTable(HiveTable hiveTable, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateHiveTableCallable() 

  
DeleteHiveTable |  Deletes an existing table specified by the table name. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteHiveTable(DeleteHiveTableRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteHiveTable(TableName name) 
  * deleteHiveTable(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteHiveTableCallable() 

  
BatchCreatePartitions |  Adds partitions to a table. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchCreatePartitions(BatchCreatePartitionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchCreatePartitions(TableName parent) 
  * batchCreatePartitions(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchCreatePartitionsCallable() 

  
BatchDeletePartitions |  Deletes partitions from a table. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchDeletePartitions(BatchDeletePartitionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchDeletePartitions(TableName parent) 
  * batchDeletePartitions(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchDeletePartitionsCallable() 

  
BatchUpdatePartitions |  Updates partitions in a table. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchUpdatePartitions(BatchUpdatePartitionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchUpdatePartitions(TableName parent) 
  * batchUpdatePartitions(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchUpdatePartitionsCallable() 

  
ListPartitions |  Streams list of partitions from a table. |  Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPartitionsCallable() 

  
FailoverHiveCatalog |  Failover the catalog to a new primary replica region. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * failoverHiveCatalog(FailoverHiveCatalogRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * failoverHiveCatalog(String name, String primaryReplica) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * failoverHiveCatalogCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of HiveMetastoreServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     HiveMetastoreServiceSettings hiveMetastoreServiceSettings =
         HiveMetastoreServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create(hiveMetastoreServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     HiveMetastoreServiceSettings hiveMetastoreServiceSettings =
         HiveMetastoreServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create(hiveMetastoreServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     HiveMetastoreServiceSettings hiveMetastoreServiceSettings =
         HiveMetastoreServiceSettings.newHttpJsonBuilder().build();
     HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create(hiveMetastoreServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > HiveMetastoreServiceClient

## Static Methods 

### create()
    
    
    public static final HiveMetastoreServiceClient create()

Constructs an instance of HiveMetastoreServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[HiveMetastoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(HiveMetastoreServiceSettings settings)
    
    
    public static final HiveMetastoreServiceClient create(HiveMetastoreServiceSettings settings)

Constructs an instance of HiveMetastoreServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[HiveMetastoreServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HiveMetastoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(HiveMetastoreServiceStub stub)
    
    
    public static final HiveMetastoreServiceClient create(HiveMetastoreServiceStub stub)

Constructs an instance of HiveMetastoreServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(HiveMetastoreServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[HiveMetastoreServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.stub.HiveMetastoreServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HiveMetastoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceClient)` |   
  
## Constructors 

### HiveMetastoreServiceClient(HiveMetastoreServiceSettings settings)
    
    
    protected HiveMetastoreServiceClient(HiveMetastoreServiceSettings settings)

Constructs an instance of HiveMetastoreServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[HiveMetastoreServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceSettings)`  
  
  
### HiveMetastoreServiceClient(HiveMetastoreServiceStub stub)
    
    
    protected HiveMetastoreServiceClient(HiveMetastoreServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[HiveMetastoreServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.stub.HiveMetastoreServiceStub)`  
  
  
## Methods 

### awaitTermination(long duration, TimeUnit unit)
    
    
    public boolean awaitTermination(long duration, TimeUnit unit)

**Parameters**  
---  
**Name** | **Description**  
`duration` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`unit` | `[TimeUnit](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/TimeUnit.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InterruptedException](https://docs.oracle.com/javase/8/docs/api/java/lang/InterruptedException.html)` |   
  
### batchCreatePartitions(@Nullable TableName parent)
    
    
    public final BatchCreatePartitionsResponse batchCreatePartitions(@Nullable TableName parent)

Adds partitions to a table.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       TableName parent = TableName.of("[PROJECT]", "[CATALOG]", "[DATABASE]", "[TABLE]");
       BatchCreatePartitionsResponse response =
           hiveMetastoreServiceClient.batchCreatePartitions(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.biglake.hive.v1beta.TableName`  
Required. Reference to the table to where the partitions to be added, in the format of projects/{project}/catalogs/{catalogs}/databases/{database}/tables/{table}.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreatePartitionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.BatchCreatePartitionsResponse)` |   
  
### batchCreatePartitions(BatchCreatePartitionsRequest request)
    
    
    public final BatchCreatePartitionsResponse batchCreatePartitions(BatchCreatePartitionsRequest request)

Adds partitions to a table.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       BatchCreatePartitionsRequest request =
           BatchCreatePartitionsRequest.newBuilder()
               .setParent(TableName.of("[PROJECT]", "[CATALOG]", "[DATABASE]", "[TABLE]").toString())
               .addAllRequests(new ArrayList<CreatePartitionRequest>())
               .setSkipExistingPartitions(true)
               .build();
       BatchCreatePartitionsResponse response =
           hiveMetastoreServiceClient.batchCreatePartitions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchCreatePartitionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.BatchCreatePartitionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreatePartitionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.BatchCreatePartitionsResponse)` |   
  
### batchCreatePartitions(String parent)
    
    
    public final BatchCreatePartitionsResponse batchCreatePartitions(String parent)

Adds partitions to a table.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       String parent = TableName.of("[PROJECT]", "[CATALOG]", "[DATABASE]", "[TABLE]").toString();
       BatchCreatePartitionsResponse response =
           hiveMetastoreServiceClient.batchCreatePartitions(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Reference to the table to where the partitions to be added, in the format of projects/{project}/catalogs/{catalogs}/databases/{database}/tables/{table}.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreatePartitionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.BatchCreatePartitionsResponse)` |   
  
### batchCreatePartitionsCallable()
    
    
    public final UnaryCallable<BatchCreatePartitionsRequest,BatchCreatePartitionsResponse> batchCreatePartitionsCallable()

Adds partitions to a table.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       BatchCreatePartitionsRequest request =
           BatchCreatePartitionsRequest.newBuilder()
               .setParent(TableName.of("[PROJECT]", "[CATALOG]", "[DATABASE]", "[TABLE]").toString())
               .addAllRequests(new ArrayList<CreatePartitionRequest>())
               .setSkipExistingPartitions(true)
               .build();
       ApiFuture<BatchCreatePartitionsResponse> future =
           hiveMetastoreServiceClient.batchCreatePartitionsCallable().futureCall(request);
       // Do something.
       BatchCreatePartitionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchCreatePartitionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.BatchCreatePartitionsRequest),[BatchCreatePartitionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.BatchCreatePartitionsResponse)>` |   
  
### batchDeletePartitions(@Nullable TableName parent)
    
    
    public final void batchDeletePartitions(@Nullable TableName parent)

Deletes partitions from a table.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       TableName parent = TableName.of("[PROJECT]", "[CATALOG]", "[DATABASE]", "[TABLE]");
       hiveMetastoreServiceClient.batchDeletePartitions(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.biglake.hive.v1beta.TableName`  
Required. Reference to the table to which these partitions belong, in the format of projects/{project}/catalogs/{catalogs}/databases/{database}/tables/{table}.  
  
### batchDeletePartitions(BatchDeletePartitionsRequest request)
    
    
    public final void batchDeletePartitions(BatchDeletePartitionsRequest request)

Deletes partitions from a table.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       BatchDeletePartitionsRequest request =
           BatchDeletePartitionsRequest.newBuilder()
               .setParent(TableName.of("[PROJECT]", "[CATALOG]", "[DATABASE]", "[TABLE]").toString())
               .addAllPartitionValues(new ArrayList<PartitionValues>())
               .build();
       hiveMetastoreServiceClient.batchDeletePartitions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchDeletePartitionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.BatchDeletePartitionsRequest)`  
The request object containing all of the parameters for the API call.  
  
### batchDeletePartitions(String parent)
    
    
    public final void batchDeletePartitions(String parent)

Deletes partitions from a table.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       String parent = TableName.of("[PROJECT]", "[CATALOG]", "[DATABASE]", "[TABLE]").toString();
       hiveMetastoreServiceClient.batchDeletePartitions(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Reference to the table to which these partitions belong, in the format of projects/{project}/catalogs/{catalogs}/databases/{database}/tables/{table}.  
  
### batchDeletePartitionsCallable()
    
    
    public final UnaryCallable<BatchDeletePartitionsRequest,Empty> batchDeletePartitionsCallable()

Deletes partitions from a table.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       BatchDeletePartitionsRequest request =
           BatchDeletePartitionsRequest.newBuilder()
               .setParent(TableName.of("[PROJECT]", "[CATALOG]", "[DATABASE]", "[TABLE]").toString())
               .addAllPartitionValues(new ArrayList<PartitionValues>())
               .build();
       ApiFuture<Empty> future =
           hiveMetastoreServiceClient.batchDeletePartitionsCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchDeletePartitionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.BatchDeletePartitionsRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### batchUpdatePartitions(@Nullable TableName parent)
    
    
    public final BatchUpdatePartitionsResponse batchUpdatePartitions(@Nullable TableName parent)

Updates partitions in a table.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       TableName parent = TableName.of("[PROJECT]", "[CATALOG]", "[DATABASE]", "[TABLE]");
       BatchUpdatePartitionsResponse response =
           hiveMetastoreServiceClient.batchUpdatePartitions(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.biglake.hive.v1beta.TableName`  
Required. Reference to the table to which these partitions belong, in the format of projects/{project}/catalogs/{catalogs}/databases/{database}/tables/{table}.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdatePartitionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.BatchUpdatePartitionsResponse)` |   
  
### batchUpdatePartitions(BatchUpdatePartitionsRequest request)
    
    
    public final BatchUpdatePartitionsResponse batchUpdatePartitions(BatchUpdatePartitionsRequest request)

Updates partitions in a table.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       BatchUpdatePartitionsRequest request =
           BatchUpdatePartitionsRequest.newBuilder()
               .setParent(TableName.of("[PROJECT]", "[CATALOG]", "[DATABASE]", "[TABLE]").toString())
               .addAllRequests(new ArrayList<UpdatePartitionRequest>())
               .build();
       BatchUpdatePartitionsResponse response =
           hiveMetastoreServiceClient.batchUpdatePartitions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchUpdatePartitionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.BatchUpdatePartitionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdatePartitionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.BatchUpdatePartitionsResponse)` |   
  
### batchUpdatePartitions(String parent)
    
    
    public final BatchUpdatePartitionsResponse batchUpdatePartitions(String parent)

Updates partitions in a table.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       String parent = TableName.of("[PROJECT]", "[CATALOG]", "[DATABASE]", "[TABLE]").toString();
       BatchUpdatePartitionsResponse response =
           hiveMetastoreServiceClient.batchUpdatePartitions(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Reference to the table to which these partitions belong, in the format of projects/{project}/catalogs/{catalogs}/databases/{database}/tables/{table}.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdatePartitionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.BatchUpdatePartitionsResponse)` |   
  
### batchUpdatePartitionsCallable()
    
    
    public final UnaryCallable<BatchUpdatePartitionsRequest,BatchUpdatePartitionsResponse> batchUpdatePartitionsCallable()

Updates partitions in a table.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       BatchUpdatePartitionsRequest request =
           BatchUpdatePartitionsRequest.newBuilder()
               .setParent(TableName.of("[PROJECT]", "[CATALOG]", "[DATABASE]", "[TABLE]").toString())
               .addAllRequests(new ArrayList<UpdatePartitionRequest>())
               .build();
       ApiFuture<BatchUpdatePartitionsResponse> future =
           hiveMetastoreServiceClient.batchUpdatePartitionsCallable().futureCall(request);
       // Do something.
       BatchUpdatePartitionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchUpdatePartitionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.BatchUpdatePartitionsRequest),[BatchUpdatePartitionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.BatchUpdatePartitionsResponse)>` |   
  
### close()
    
    
    public final void close()

### createHiveCatalog(@Nullable ProjectName parent, HiveCatalog hiveCatalog, String hiveCatalogId)
    
    
    public final HiveCatalog createHiveCatalog(@Nullable ProjectName parent, HiveCatalog hiveCatalog, String hiveCatalogId)

Creates a new hive catalog.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       ProjectName parent = ProjectName.of("[PROJECT]");
       HiveCatalog hiveCatalog = HiveCatalog.newBuilder().build();
       String hiveCatalogId = "hiveCatalogId-575314556";
       HiveCatalog response =
           hiveMetastoreServiceClient.createHiveCatalog(parent, hiveCatalog, hiveCatalogId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.biglake.hive.v1beta.ProjectName`  
Required. The parent resource where this catalog will be created. Format: projects/{project_id_or_number}  
`hiveCatalog` | `[HiveCatalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveCatalog)`  
Required. The catalog to create. The `name` field does not need to be provided. Gets copied over from catalog_id.  
`hiveCatalogId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The Hive Catalog ID to use for the catalog that will become the final component of the catalog's resource name. The maximum length is 256 characters.  
**Returns**  
---  
**Type** | **Description**  
`[HiveCatalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveCatalog)` |   
  
### createHiveCatalog(CreateHiveCatalogRequest request)
    
    
    public final HiveCatalog createHiveCatalog(CreateHiveCatalogRequest request)

Creates a new hive catalog.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       CreateHiveCatalogRequest request =
           CreateHiveCatalogRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setHiveCatalog(HiveCatalog.newBuilder().build())
               .setHiveCatalogId("hiveCatalogId-575314556")
               .setPrimaryLocation("primaryLocation-1140723753")
               .build();
       HiveCatalog response = hiveMetastoreServiceClient.createHiveCatalog(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateHiveCatalogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.CreateHiveCatalogRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[HiveCatalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveCatalog)` |   
  
### createHiveCatalog(String parent, HiveCatalog hiveCatalog, String hiveCatalogId)
    
    
    public final HiveCatalog createHiveCatalog(String parent, HiveCatalog hiveCatalog, String hiveCatalogId)

Creates a new hive catalog.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       String parent = ProjectName.of("[PROJECT]").toString();
       HiveCatalog hiveCatalog = HiveCatalog.newBuilder().build();
       String hiveCatalogId = "hiveCatalogId-575314556";
       HiveCatalog response =
           hiveMetastoreServiceClient.createHiveCatalog(parent, hiveCatalog, hiveCatalogId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where this catalog will be created. Format: projects/{project_id_or_number}  
`hiveCatalog` | `[HiveCatalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveCatalog)`  
Required. The catalog to create. The `name` field does not need to be provided. Gets copied over from catalog_id.  
`hiveCatalogId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The Hive Catalog ID to use for the catalog that will become the final component of the catalog's resource name. The maximum length is 256 characters.  
**Returns**  
---  
**Type** | **Description**  
`[HiveCatalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveCatalog)` |   
  
### createHiveCatalogCallable()
    
    
    public final UnaryCallable<CreateHiveCatalogRequest,HiveCatalog> createHiveCatalogCallable()

Creates a new hive catalog.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       CreateHiveCatalogRequest request =
           CreateHiveCatalogRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setHiveCatalog(HiveCatalog.newBuilder().build())
               .setHiveCatalogId("hiveCatalogId-575314556")
               .setPrimaryLocation("primaryLocation-1140723753")
               .build();
       ApiFuture<HiveCatalog> future =
           hiveMetastoreServiceClient.createHiveCatalogCallable().futureCall(request);
       // Do something.
       HiveCatalog response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateHiveCatalogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.CreateHiveCatalogRequest),[HiveCatalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveCatalog)>` |   
  
### createHiveDatabase(@Nullable CatalogName parent, HiveDatabase hiveDatabase, String hiveDatabaseId)
    
    
    public final HiveDatabase createHiveDatabase(@Nullable CatalogName parent, HiveDatabase hiveDatabase, String hiveDatabaseId)

Creates a new database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       CatalogName parent = CatalogName.of("[PROJECT]", "[CATALOG]");
       HiveDatabase hiveDatabase = HiveDatabase.newBuilder().build();
       String hiveDatabaseId = "hiveDatabaseId-1150232698";
       HiveDatabase response =
           hiveMetastoreServiceClient.createHiveDatabase(parent, hiveDatabase, hiveDatabaseId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.biglake.hive.v1beta.CatalogName`  
Required. The parent resource where this database will be created. Format: projects/{project_id_or_number}/catalogs/{catalog_id}  
`hiveDatabase` | `[HiveDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveDatabase)`  
Required. The database to create. The `name` field does not need to be provided.  
`hiveDatabaseId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the Hive Database. The maximum length is 128 characters.  
**Returns**  
---  
**Type** | **Description**  
`[HiveDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveDatabase)` |   
  
### createHiveDatabase(CreateHiveDatabaseRequest request)
    
    
    public final HiveDatabase createHiveDatabase(CreateHiveDatabaseRequest request)

Creates a new database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       CreateHiveDatabaseRequest request =
           CreateHiveDatabaseRequest.newBuilder()
               .setParent(CatalogName.of("[PROJECT]", "[CATALOG]").toString())
               .setHiveDatabase(HiveDatabase.newBuilder().build())
               .setHiveDatabaseId("hiveDatabaseId-1150232698")
               .build();
       HiveDatabase response = hiveMetastoreServiceClient.createHiveDatabase(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateHiveDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.CreateHiveDatabaseRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[HiveDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveDatabase)` |   
  
### createHiveDatabase(String parent, HiveDatabase hiveDatabase, String hiveDatabaseId)
    
    
    public final HiveDatabase createHiveDatabase(String parent, HiveDatabase hiveDatabase, String hiveDatabaseId)

Creates a new database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       String parent = CatalogName.of("[PROJECT]", "[CATALOG]").toString();
       HiveDatabase hiveDatabase = HiveDatabase.newBuilder().build();
       String hiveDatabaseId = "hiveDatabaseId-1150232698";
       HiveDatabase response =
           hiveMetastoreServiceClient.createHiveDatabase(parent, hiveDatabase, hiveDatabaseId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where this database will be created. Format: projects/{project_id_or_number}/catalogs/{catalog_id}  
`hiveDatabase` | `[HiveDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveDatabase)`  
Required. The database to create. The `name` field does not need to be provided.  
`hiveDatabaseId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the Hive Database. The maximum length is 128 characters.  
**Returns**  
---  
**Type** | **Description**  
`[HiveDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveDatabase)` |   
  
### createHiveDatabaseCallable()
    
    
    public final UnaryCallable<CreateHiveDatabaseRequest,HiveDatabase> createHiveDatabaseCallable()

Creates a new database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       CreateHiveDatabaseRequest request =
           CreateHiveDatabaseRequest.newBuilder()
               .setParent(CatalogName.of("[PROJECT]", "[CATALOG]").toString())
               .setHiveDatabase(HiveDatabase.newBuilder().build())
               .setHiveDatabaseId("hiveDatabaseId-1150232698")
               .build();
       ApiFuture<HiveDatabase> future =
           hiveMetastoreServiceClient.createHiveDatabaseCallable().futureCall(request);
       // Do something.
       HiveDatabase response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateHiveDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.CreateHiveDatabaseRequest),[HiveDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveDatabase)>` |   
  
### createHiveTable(@Nullable NamespaceName parent, HiveTable hiveTable, String hiveTableId)
    
    
    public final HiveTable createHiveTable(@Nullable NamespaceName parent, HiveTable hiveTable, String hiveTableId)

Creates a new hive table.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       NamespaceName parent = NamespaceName.of("[PROJECT]", "[CATALOG]", "[DATABASE]");
       HiveTable hiveTable = HiveTable.newBuilder().build();
       String hiveTableId = "hiveTableId152241145";
       HiveTable response =
           hiveMetastoreServiceClient.createHiveTable(parent, hiveTable, hiveTableId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.biglake.hive.v1beta.NamespaceName`  
Required. The parent resource for the table to be created. Format: projects/{project_id_or_number}/catalogs/{catalog_id}/databases/{database_id}  
`hiveTable` | `[HiveTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveTable)`  
Required. The Hive Table to create. The `name` field does not need to be provided.  
`hiveTableId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The Hive Table ID to use for the table that will become the final component of the table's resource name. The maximum length is 256 characters.  
**Returns**  
---  
**Type** | **Description**  
`[HiveTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveTable)` |   
  
### createHiveTable(CreateHiveTableRequest request)
    
    
    public final HiveTable createHiveTable(CreateHiveTableRequest request)

Creates a new hive table.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       CreateHiveTableRequest request =
           CreateHiveTableRequest.newBuilder()
               .setParent(NamespaceName.of("[PROJECT]", "[CATALOG]", "[DATABASE]").toString())
               .setHiveTable(HiveTable.newBuilder().build())
               .setHiveTableId("hiveTableId152241145")
               .build();
       HiveTable response = hiveMetastoreServiceClient.createHiveTable(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateHiveTableRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.CreateHiveTableRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[HiveTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveTable)` |   
  
### createHiveTable(String parent, HiveTable hiveTable, String hiveTableId)
    
    
    public final HiveTable createHiveTable(String parent, HiveTable hiveTable, String hiveTableId)

Creates a new hive table.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       String parent = NamespaceName.of("[PROJECT]", "[CATALOG]", "[DATABASE]").toString();
       HiveTable hiveTable = HiveTable.newBuilder().build();
       String hiveTableId = "hiveTableId152241145";
       HiveTable response =
           hiveMetastoreServiceClient.createHiveTable(parent, hiveTable, hiveTableId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource for the table to be created. Format: projects/{project_id_or_number}/catalogs/{catalog_id}/databases/{database_id}  
`hiveTable` | `[HiveTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveTable)`  
Required. The Hive Table to create. The `name` field does not need to be provided.  
`hiveTableId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The Hive Table ID to use for the table that will become the final component of the table's resource name. The maximum length is 256 characters.  
**Returns**  
---  
**Type** | **Description**  
`[HiveTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveTable)` |   
  
### createHiveTableCallable()
    
    
    public final UnaryCallable<CreateHiveTableRequest,HiveTable> createHiveTableCallable()

Creates a new hive table.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       CreateHiveTableRequest request =
           CreateHiveTableRequest.newBuilder()
               .setParent(NamespaceName.of("[PROJECT]", "[CATALOG]", "[DATABASE]").toString())
               .setHiveTable(HiveTable.newBuilder().build())
               .setHiveTableId("hiveTableId152241145")
               .build();
       ApiFuture<HiveTable> future =
           hiveMetastoreServiceClient.createHiveTableCallable().futureCall(request);
       // Do something.
       HiveTable response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateHiveTableRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.CreateHiveTableRequest),[HiveTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveTable)>` |   
  
### deleteHiveCatalog(@Nullable CatalogName name)
    
    
    public final void deleteHiveCatalog(@Nullable CatalogName name)

Deletes an existing catalog specified by the catalog ID. Delete will fail if the catalog is not empty.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       CatalogName name = CatalogName.of("[PROJECT]", "[CATALOG]");
       hiveMetastoreServiceClient.deleteHiveCatalog(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.biglake.hive.v1beta.CatalogName`  
Required. The name of the catalog to delete. Format: projects/{project_id_or_number}/catalogs/{catalog_id}  
  
### deleteHiveCatalog(DeleteHiveCatalogRequest request)
    
    
    public final void deleteHiveCatalog(DeleteHiveCatalogRequest request)

Deletes an existing catalog specified by the catalog ID. Delete will fail if the catalog is not empty.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       DeleteHiveCatalogRequest request =
           DeleteHiveCatalogRequest.newBuilder()
               .setName(CatalogName.of("[PROJECT]", "[CATALOG]").toString())
               .build();
       hiveMetastoreServiceClient.deleteHiveCatalog(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteHiveCatalogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.DeleteHiveCatalogRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteHiveCatalog(String name)
    
    
    public final void deleteHiveCatalog(String name)

Deletes an existing catalog specified by the catalog ID. Delete will fail if the catalog is not empty.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       String name = CatalogName.of("[PROJECT]", "[CATALOG]").toString();
       hiveMetastoreServiceClient.deleteHiveCatalog(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the catalog to delete. Format: projects/{project_id_or_number}/catalogs/{catalog_id}  
  
### deleteHiveCatalogCallable()
    
    
    public final UnaryCallable<DeleteHiveCatalogRequest,Empty> deleteHiveCatalogCallable()

Deletes an existing catalog specified by the catalog ID. Delete will fail if the catalog is not empty.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       DeleteHiveCatalogRequest request =
           DeleteHiveCatalogRequest.newBuilder()
               .setName(CatalogName.of("[PROJECT]", "[CATALOG]").toString())
               .build();
       ApiFuture<Empty> future =
           hiveMetastoreServiceClient.deleteHiveCatalogCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteHiveCatalogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.DeleteHiveCatalogRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteHiveDatabase(@Nullable NamespaceName name)
    
    
    public final void deleteHiveDatabase(@Nullable NamespaceName name)

Deletes an existing database specified by the database name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       NamespaceName name = NamespaceName.of("[PROJECT]", "[CATALOG]", "[DATABASE]");
       hiveMetastoreServiceClient.deleteHiveDatabase(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.biglake.hive.v1beta.NamespaceName`  
Required. The name of the database to delete. Format: projects/{project_id_or_number}/catalogs/{catalog_id}/databases/{database_id}  
  
### deleteHiveDatabase(DeleteHiveDatabaseRequest request)
    
    
    public final void deleteHiveDatabase(DeleteHiveDatabaseRequest request)

Deletes an existing database specified by the database name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       DeleteHiveDatabaseRequest request =
           DeleteHiveDatabaseRequest.newBuilder()
               .setName(NamespaceName.of("[PROJECT]", "[CATALOG]", "[DATABASE]").toString())
               .build();
       hiveMetastoreServiceClient.deleteHiveDatabase(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteHiveDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.DeleteHiveDatabaseRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteHiveDatabase(String name)
    
    
    public final void deleteHiveDatabase(String name)

Deletes an existing database specified by the database name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       String name = NamespaceName.of("[PROJECT]", "[CATALOG]", "[DATABASE]").toString();
       hiveMetastoreServiceClient.deleteHiveDatabase(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the database to delete. Format: projects/{project_id_or_number}/catalogs/{catalog_id}/databases/{database_id}  
  
### deleteHiveDatabaseCallable()
    
    
    public final UnaryCallable<DeleteHiveDatabaseRequest,Empty> deleteHiveDatabaseCallable()

Deletes an existing database specified by the database name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       DeleteHiveDatabaseRequest request =
           DeleteHiveDatabaseRequest.newBuilder()
               .setName(NamespaceName.of("[PROJECT]", "[CATALOG]", "[DATABASE]").toString())
               .build();
       ApiFuture<Empty> future =
           hiveMetastoreServiceClient.deleteHiveDatabaseCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteHiveDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.DeleteHiveDatabaseRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteHiveTable(@Nullable TableName name)
    
    
    public final void deleteHiveTable(@Nullable TableName name)

Deletes an existing table specified by the table name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       TableName name = TableName.of("[PROJECT]", "[CATALOG]", "[DATABASE]", "[TABLE]");
       hiveMetastoreServiceClient.deleteHiveTable(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.biglake.hive.v1beta.TableName`  
Required. The name of the database to delete. Format: projects/{project_id_or_number}/catalogs/{catalog_id}/databases/{database_id}/tables/{table_id}  
  
### deleteHiveTable(DeleteHiveTableRequest request)
    
    
    public final void deleteHiveTable(DeleteHiveTableRequest request)

Deletes an existing table specified by the table name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       DeleteHiveTableRequest request =
           DeleteHiveTableRequest.newBuilder()
               .setName(TableName.of("[PROJECT]", "[CATALOG]", "[DATABASE]", "[TABLE]").toString())
               .build();
       hiveMetastoreServiceClient.deleteHiveTable(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteHiveTableRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.DeleteHiveTableRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteHiveTable(String name)
    
    
    public final void deleteHiveTable(String name)

Deletes an existing table specified by the table name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       String name = TableName.of("[PROJECT]", "[CATALOG]", "[DATABASE]", "[TABLE]").toString();
       hiveMetastoreServiceClient.deleteHiveTable(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the database to delete. Format: projects/{project_id_or_number}/catalogs/{catalog_id}/databases/{database_id}/tables/{table_id}  
  
### deleteHiveTableCallable()
    
    
    public final UnaryCallable<DeleteHiveTableRequest,Empty> deleteHiveTableCallable()

Deletes an existing table specified by the table name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       DeleteHiveTableRequest request =
           DeleteHiveTableRequest.newBuilder()
               .setName(TableName.of("[PROJECT]", "[CATALOG]", "[DATABASE]", "[TABLE]").toString())
               .build();
       ApiFuture<Empty> future =
           hiveMetastoreServiceClient.deleteHiveTableCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteHiveTableRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.DeleteHiveTableRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### failoverHiveCatalog(FailoverHiveCatalogRequest request)
    
    
    public final FailoverHiveCatalogResponse failoverHiveCatalog(FailoverHiveCatalogRequest request)

Failover the catalog to a new primary replica region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       FailoverHiveCatalogRequest request =
           FailoverHiveCatalogRequest.newBuilder()
               .setName("name3373707")
               .setPrimaryReplica("primaryReplica-389090218")
               .setValidateOnly(true)
               .setConditionalFailoverReplicationTime(Timestamp.newBuilder().build())
               .build();
       FailoverHiveCatalogResponse response =
           hiveMetastoreServiceClient.failoverHiveCatalog(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FailoverHiveCatalogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.FailoverHiveCatalogRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FailoverHiveCatalogResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.FailoverHiveCatalogResponse)` |   
  
### failoverHiveCatalog(String name, String primaryReplica)
    
    
    public final FailoverHiveCatalogResponse failoverHiveCatalog(String name, String primaryReplica)

Failover the catalog to a new primary replica region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       String name = "name3373707";
       String primaryReplica = "primaryReplica-389090218";
       FailoverHiveCatalogResponse response =
           hiveMetastoreServiceClient.failoverHiveCatalog(name, primaryReplica);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the catalog in the form "projects/{project_id}/catalogs/{catalog_id}"  
`primaryReplica` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The region being assigned as the new primary replica region. For example "us-east1". This must be one of the replica regions in the catalog's list of replicas marked as a "secondary".  
**Returns**  
---  
**Type** | **Description**  
`[FailoverHiveCatalogResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.FailoverHiveCatalogResponse)` |   
  
### failoverHiveCatalogCallable()
    
    
    public final UnaryCallable<FailoverHiveCatalogRequest,FailoverHiveCatalogResponse> failoverHiveCatalogCallable()

Failover the catalog to a new primary replica region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       FailoverHiveCatalogRequest request =
           FailoverHiveCatalogRequest.newBuilder()
               .setName("name3373707")
               .setPrimaryReplica("primaryReplica-389090218")
               .setValidateOnly(true)
               .setConditionalFailoverReplicationTime(Timestamp.newBuilder().build())
               .build();
       ApiFuture<FailoverHiveCatalogResponse> future =
           hiveMetastoreServiceClient.failoverHiveCatalogCallable().futureCall(request);
       // Do something.
       FailoverHiveCatalogResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FailoverHiveCatalogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.FailoverHiveCatalogRequest),[FailoverHiveCatalogResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.FailoverHiveCatalogResponse)>` |   
  
### getHiveCatalog(@Nullable CatalogName name)
    
    
    public final HiveCatalog getHiveCatalog(@Nullable CatalogName name)

Gets the catalog specified by the resource name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       CatalogName name = CatalogName.of("[PROJECT]", "[CATALOG]");
       HiveCatalog response = hiveMetastoreServiceClient.getHiveCatalog(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.biglake.hive.v1beta.CatalogName`  
Required. The name of the catalog to retrieve. Format: projects/{project_id_or_number}/catalogs/{catalog_id}  
**Returns**  
---  
**Type** | **Description**  
`[HiveCatalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveCatalog)` |   
  
### getHiveCatalog(GetHiveCatalogRequest request)
    
    
    public final HiveCatalog getHiveCatalog(GetHiveCatalogRequest request)

Gets the catalog specified by the resource name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       GetHiveCatalogRequest request =
           GetHiveCatalogRequest.newBuilder()
               .setName(CatalogName.of("[PROJECT]", "[CATALOG]").toString())
               .build();
       HiveCatalog response = hiveMetastoreServiceClient.getHiveCatalog(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetHiveCatalogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.GetHiveCatalogRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[HiveCatalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveCatalog)` |   
  
### getHiveCatalog(String name)
    
    
    public final HiveCatalog getHiveCatalog(String name)

Gets the catalog specified by the resource name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       String name = CatalogName.of("[PROJECT]", "[CATALOG]").toString();
       HiveCatalog response = hiveMetastoreServiceClient.getHiveCatalog(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the catalog to retrieve. Format: projects/{project_id_or_number}/catalogs/{catalog_id}  
**Returns**  
---  
**Type** | **Description**  
`[HiveCatalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveCatalog)` |   
  
### getHiveCatalogCallable()
    
    
    public final UnaryCallable<GetHiveCatalogRequest,HiveCatalog> getHiveCatalogCallable()

Gets the catalog specified by the resource name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       GetHiveCatalogRequest request =
           GetHiveCatalogRequest.newBuilder()
               .setName(CatalogName.of("[PROJECT]", "[CATALOG]").toString())
               .build();
       ApiFuture<HiveCatalog> future =
           hiveMetastoreServiceClient.getHiveCatalogCallable().futureCall(request);
       // Do something.
       HiveCatalog response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetHiveCatalogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.GetHiveCatalogRequest),[HiveCatalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveCatalog)>` |   
  
### getHiveDatabase(@Nullable NamespaceName name)
    
    
    public final HiveDatabase getHiveDatabase(@Nullable NamespaceName name)

Gets the database specified by the resource name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       NamespaceName name = NamespaceName.of("[PROJECT]", "[CATALOG]", "[DATABASE]");
       HiveDatabase response = hiveMetastoreServiceClient.getHiveDatabase(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.biglake.hive.v1beta.NamespaceName`  
Required. The name of the database to retrieve. Format: projects/{project_id_or_number}/catalogs/{catalog_id}/databases/{database_id}  
**Returns**  
---  
**Type** | **Description**  
`[HiveDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveDatabase)` |   
  
### getHiveDatabase(GetHiveDatabaseRequest request)
    
    
    public final HiveDatabase getHiveDatabase(GetHiveDatabaseRequest request)

Gets the database specified by the resource name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       GetHiveDatabaseRequest request =
           GetHiveDatabaseRequest.newBuilder()
               .setName(NamespaceName.of("[PROJECT]", "[CATALOG]", "[DATABASE]").toString())
               .build();
       HiveDatabase response = hiveMetastoreServiceClient.getHiveDatabase(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetHiveDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.GetHiveDatabaseRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[HiveDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveDatabase)` |   
  
### getHiveDatabase(String name)
    
    
    public final HiveDatabase getHiveDatabase(String name)

Gets the database specified by the resource name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       String name = NamespaceName.of("[PROJECT]", "[CATALOG]", "[DATABASE]").toString();
       HiveDatabase response = hiveMetastoreServiceClient.getHiveDatabase(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the database to retrieve. Format: projects/{project_id_or_number}/catalogs/{catalog_id}/databases/{database_id}  
**Returns**  
---  
**Type** | **Description**  
`[HiveDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveDatabase)` |   
  
### getHiveDatabaseCallable()
    
    
    public final UnaryCallable<GetHiveDatabaseRequest,HiveDatabase> getHiveDatabaseCallable()

Gets the database specified by the resource name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       GetHiveDatabaseRequest request =
           GetHiveDatabaseRequest.newBuilder()
               .setName(NamespaceName.of("[PROJECT]", "[CATALOG]", "[DATABASE]").toString())
               .build();
       ApiFuture<HiveDatabase> future =
           hiveMetastoreServiceClient.getHiveDatabaseCallable().futureCall(request);
       // Do something.
       HiveDatabase response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetHiveDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.GetHiveDatabaseRequest),[HiveDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveDatabase)>` |   
  
### getHiveTable(@Nullable TableName name)
    
    
    public final HiveTable getHiveTable(@Nullable TableName name)

Gets the table specified by the resource name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       TableName name = TableName.of("[PROJECT]", "[CATALOG]", "[DATABASE]", "[TABLE]");
       HiveTable response = hiveMetastoreServiceClient.getHiveTable(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.biglake.hive.v1beta.TableName`  
Required. The name of the table to retrieve. Format: projects/{project_id_or_number}/catalogs/{catalog_id}/databases/{database_id}/tables/{table_id}  
**Returns**  
---  
**Type** | **Description**  
`[HiveTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveTable)` |   
  
### getHiveTable(GetHiveTableRequest request)
    
    
    public final HiveTable getHiveTable(GetHiveTableRequest request)

Gets the table specified by the resource name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       GetHiveTableRequest request =
           GetHiveTableRequest.newBuilder()
               .setName(TableName.of("[PROJECT]", "[CATALOG]", "[DATABASE]", "[TABLE]").toString())
               .build();
       HiveTable response = hiveMetastoreServiceClient.getHiveTable(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetHiveTableRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.GetHiveTableRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[HiveTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveTable)` |   
  
### getHiveTable(String name)
    
    
    public final HiveTable getHiveTable(String name)

Gets the table specified by the resource name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       String name = TableName.of("[PROJECT]", "[CATALOG]", "[DATABASE]", "[TABLE]").toString();
       HiveTable response = hiveMetastoreServiceClient.getHiveTable(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the table to retrieve. Format: projects/{project_id_or_number}/catalogs/{catalog_id}/databases/{database_id}/tables/{table_id}  
**Returns**  
---  
**Type** | **Description**  
`[HiveTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveTable)` |   
  
### getHiveTableCallable()
    
    
    public final UnaryCallable<GetHiveTableRequest,HiveTable> getHiveTableCallable()

Gets the table specified by the resource name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       GetHiveTableRequest request =
           GetHiveTableRequest.newBuilder()
               .setName(TableName.of("[PROJECT]", "[CATALOG]", "[DATABASE]", "[TABLE]").toString())
               .build();
       ApiFuture<HiveTable> future =
           hiveMetastoreServiceClient.getHiveTableCallable().futureCall(request);
       // Do something.
       HiveTable response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetHiveTableRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.GetHiveTableRequest),[HiveTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveTable)>` |   
  
### getSettings()
    
    
    public final @Nullable HiveMetastoreServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceSettings` |   
  
### getStub()
    
    
    public HiveMetastoreServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[HiveMetastoreServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.stub.HiveMetastoreServiceStub)` |   
  
### isShutdown()
    
    
    public boolean isShutdown()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### isTerminated()
    
    
    public boolean isTerminated()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### listHiveCatalogs(@Nullable ProjectName parent)
    
    
    public final HiveMetastoreServiceClient.ListHiveCatalogsPagedResponse listHiveCatalogs(@Nullable ProjectName parent)

List all catalogs in a specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       ProjectName parent = ProjectName.of("[PROJECT]");
       for (HiveCatalog element : hiveMetastoreServiceClient.listHiveCatalogs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.biglake.hive.v1beta.ProjectName`  
Required. The project to list catalogs from. Format: projects/{project_id_or_number}  
**Returns**  
---  
**Type** | **Description**  
`[HiveMetastoreServiceClient.ListHiveCatalogsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceClient.ListHiveCatalogsPagedResponse)` |   
  
### listHiveCatalogs(ListHiveCatalogsRequest request)
    
    
    public final HiveMetastoreServiceClient.ListHiveCatalogsPagedResponse listHiveCatalogs(ListHiveCatalogsRequest request)

List all catalogs in a specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       ListHiveCatalogsRequest request =
           ListHiveCatalogsRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (HiveCatalog element :
           hiveMetastoreServiceClient.listHiveCatalogs(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListHiveCatalogsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListHiveCatalogsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[HiveMetastoreServiceClient.ListHiveCatalogsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceClient.ListHiveCatalogsPagedResponse)` |   
  
### listHiveCatalogs(String parent)
    
    
    public final HiveMetastoreServiceClient.ListHiveCatalogsPagedResponse listHiveCatalogs(String parent)

List all catalogs in a specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       String parent = ProjectName.of("[PROJECT]").toString();
       for (HiveCatalog element : hiveMetastoreServiceClient.listHiveCatalogs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project to list catalogs from. Format: projects/{project_id_or_number}  
**Returns**  
---  
**Type** | **Description**  
`[HiveMetastoreServiceClient.ListHiveCatalogsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceClient.ListHiveCatalogsPagedResponse)` |   
  
### listHiveCatalogsCallable()
    
    
    public final UnaryCallable<ListHiveCatalogsRequest,ListHiveCatalogsResponse> listHiveCatalogsCallable()

List all catalogs in a specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       ListHiveCatalogsRequest request =
           ListHiveCatalogsRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListHiveCatalogsResponse response =
             hiveMetastoreServiceClient.listHiveCatalogsCallable().call(request);
         for (HiveCatalog element : response.getCatalogsList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListHiveCatalogsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListHiveCatalogsRequest),[ListHiveCatalogsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListHiveCatalogsResponse)>` |   
  
### listHiveCatalogsPagedCallable()
    
    
    public final UnaryCallable<ListHiveCatalogsRequest,HiveMetastoreServiceClient.ListHiveCatalogsPagedResponse> listHiveCatalogsPagedCallable()

List all catalogs in a specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       ListHiveCatalogsRequest request =
           ListHiveCatalogsRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<HiveCatalog> future =
           hiveMetastoreServiceClient.listHiveCatalogsPagedCallable().futureCall(request);
       // Do something.
       for (HiveCatalog element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListHiveCatalogsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListHiveCatalogsRequest),[ListHiveCatalogsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceClient.ListHiveCatalogsPagedResponse)>` |   
  
### listHiveDatabases(@Nullable CatalogName parent)
    
    
    public final HiveMetastoreServiceClient.ListHiveDatabasesPagedResponse listHiveDatabases(@Nullable CatalogName parent)

List all databases in a specified catalog.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       CatalogName parent = CatalogName.of("[PROJECT]", "[CATALOG]");
       for (HiveDatabase element :
           hiveMetastoreServiceClient.listHiveDatabases(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.biglake.hive.v1beta.CatalogName`  
Required. The hive catalog to list databases from. Format: projects/{project_id_or_number}/catalogs/{catalog_id}  
**Returns**  
---  
**Type** | **Description**  
`[HiveMetastoreServiceClient.ListHiveDatabasesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceClient.ListHiveDatabasesPagedResponse)` |   
  
### listHiveDatabases(ListHiveDatabasesRequest request)
    
    
    public final HiveMetastoreServiceClient.ListHiveDatabasesPagedResponse listHiveDatabases(ListHiveDatabasesRequest request)

List all databases in a specified catalog.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       ListHiveDatabasesRequest request =
           ListHiveDatabasesRequest.newBuilder()
               .setParent(CatalogName.of("[PROJECT]", "[CATALOG]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (HiveDatabase element :
           hiveMetastoreServiceClient.listHiveDatabases(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListHiveDatabasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListHiveDatabasesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[HiveMetastoreServiceClient.ListHiveDatabasesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceClient.ListHiveDatabasesPagedResponse)` |   
  
### listHiveDatabases(String parent)
    
    
    public final HiveMetastoreServiceClient.ListHiveDatabasesPagedResponse listHiveDatabases(String parent)

List all databases in a specified catalog.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       String parent = CatalogName.of("[PROJECT]", "[CATALOG]").toString();
       for (HiveDatabase element :
           hiveMetastoreServiceClient.listHiveDatabases(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The hive catalog to list databases from. Format: projects/{project_id_or_number}/catalogs/{catalog_id}  
**Returns**  
---  
**Type** | **Description**  
`[HiveMetastoreServiceClient.ListHiveDatabasesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceClient.ListHiveDatabasesPagedResponse)` |   
  
### listHiveDatabasesCallable()
    
    
    public final UnaryCallable<ListHiveDatabasesRequest,ListHiveDatabasesResponse> listHiveDatabasesCallable()

List all databases in a specified catalog.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       ListHiveDatabasesRequest request =
           ListHiveDatabasesRequest.newBuilder()
               .setParent(CatalogName.of("[PROJECT]", "[CATALOG]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListHiveDatabasesResponse response =
             hiveMetastoreServiceClient.listHiveDatabasesCallable().call(request);
         for (HiveDatabase element : response.getDatabasesList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListHiveDatabasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListHiveDatabasesRequest),[ListHiveDatabasesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListHiveDatabasesResponse)>` |   
  
### listHiveDatabasesPagedCallable()
    
    
    public final UnaryCallable<ListHiveDatabasesRequest,HiveMetastoreServiceClient.ListHiveDatabasesPagedResponse> listHiveDatabasesPagedCallable()

List all databases in a specified catalog.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       ListHiveDatabasesRequest request =
           ListHiveDatabasesRequest.newBuilder()
               .setParent(CatalogName.of("[PROJECT]", "[CATALOG]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<HiveDatabase> future =
           hiveMetastoreServiceClient.listHiveDatabasesPagedCallable().futureCall(request);
       // Do something.
       for (HiveDatabase element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListHiveDatabasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListHiveDatabasesRequest),[ListHiveDatabasesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceClient.ListHiveDatabasesPagedResponse)>` |   
  
### listHiveTables(@Nullable NamespaceName parent)
    
    
    public final HiveMetastoreServiceClient.ListHiveTablesPagedResponse listHiveTables(@Nullable NamespaceName parent)

List all hive tables in a specified project under the hive catalog and database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       NamespaceName parent = NamespaceName.of("[PROJECT]", "[CATALOG]", "[DATABASE]");
       for (HiveTable element : hiveMetastoreServiceClient.listHiveTables(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.biglake.hive.v1beta.NamespaceName`  
Required. The database to list tables from. Format: projects/{project_id_or_number}/catalogs/{catalog_id}/databases/{database_id}  
**Returns**  
---  
**Type** | **Description**  
`[HiveMetastoreServiceClient.ListHiveTablesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceClient.ListHiveTablesPagedResponse)` |   
  
### listHiveTables(ListHiveTablesRequest request)
    
    
    public final HiveMetastoreServiceClient.ListHiveTablesPagedResponse listHiveTables(ListHiveTablesRequest request)

List all hive tables in a specified project under the hive catalog and database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       ListHiveTablesRequest request =
           ListHiveTablesRequest.newBuilder()
               .setParent(NamespaceName.of("[PROJECT]", "[CATALOG]", "[DATABASE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (HiveTable element : hiveMetastoreServiceClient.listHiveTables(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListHiveTablesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListHiveTablesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[HiveMetastoreServiceClient.ListHiveTablesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceClient.ListHiveTablesPagedResponse)` |   
  
### listHiveTables(String parent)
    
    
    public final HiveMetastoreServiceClient.ListHiveTablesPagedResponse listHiveTables(String parent)

List all hive tables in a specified project under the hive catalog and database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       String parent = NamespaceName.of("[PROJECT]", "[CATALOG]", "[DATABASE]").toString();
       for (HiveTable element : hiveMetastoreServiceClient.listHiveTables(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The database to list tables from. Format: projects/{project_id_or_number}/catalogs/{catalog_id}/databases/{database_id}  
**Returns**  
---  
**Type** | **Description**  
`[HiveMetastoreServiceClient.ListHiveTablesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceClient.ListHiveTablesPagedResponse)` |   
  
### listHiveTablesCallable()
    
    
    public final UnaryCallable<ListHiveTablesRequest,ListHiveTablesResponse> listHiveTablesCallable()

List all hive tables in a specified project under the hive catalog and database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       ListHiveTablesRequest request =
           ListHiveTablesRequest.newBuilder()
               .setParent(NamespaceName.of("[PROJECT]", "[CATALOG]", "[DATABASE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListHiveTablesResponse response =
             hiveMetastoreServiceClient.listHiveTablesCallable().call(request);
         for (HiveTable element : response.getTablesList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListHiveTablesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListHiveTablesRequest),[ListHiveTablesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListHiveTablesResponse)>` |   
  
### listHiveTablesPagedCallable()
    
    
    public final UnaryCallable<ListHiveTablesRequest,HiveMetastoreServiceClient.ListHiveTablesPagedResponse> listHiveTablesPagedCallable()

List all hive tables in a specified project under the hive catalog and database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       ListHiveTablesRequest request =
           ListHiveTablesRequest.newBuilder()
               .setParent(NamespaceName.of("[PROJECT]", "[CATALOG]", "[DATABASE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<HiveTable> future =
           hiveMetastoreServiceClient.listHiveTablesPagedCallable().futureCall(request);
       // Do something.
       for (HiveTable element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListHiveTablesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListHiveTablesRequest),[ListHiveTablesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceClient.ListHiveTablesPagedResponse)>` |   
  
### listPartitionsCallable()
    
    
    public final ServerStreamingCallable<ListPartitionsRequest,ListPartitionsResponse> listPartitionsCallable()

Streams list of partitions from a table.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       ListPartitionsRequest request =
           ListPartitionsRequest.newBuilder()
               .setParent(TableName.of("[PROJECT]", "[CATALOG]", "[DATABASE]", "[TABLE]").toString())
               .setFilter("filter-1274492040")
               .build();
       ServerStream<ListPartitionsResponse> stream =
           hiveMetastoreServiceClient.listPartitionsCallable().call(request);
       for (ListPartitionsResponse response : stream) {
         // Do something when a response is received.
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[ServerStreamingCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ServerStreamingCallable.html)<[ListPartitionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListPartitionsRequest),[ListPartitionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListPartitionsResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateHiveCatalog(HiveCatalog hiveCatalog, FieldMask updateMask)
    
    
    public final HiveCatalog updateHiveCatalog(HiveCatalog hiveCatalog, FieldMask updateMask)

Updates an existing catalog.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       HiveCatalog hiveCatalog = HiveCatalog.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       HiveCatalog response = hiveMetastoreServiceClient.updateHiveCatalog(hiveCatalog, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`hiveCatalog` | `[HiveCatalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveCatalog)`  
Required. The hive catalog to update. The name under the catalog is used to identify the catalog. Format: projects/{project_id_or_number}/catalogs/{catalog_id}  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The list of fields to update. For the `FieldMask` definition, see <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask> If not set, defaults to all of the fields that are allowed to update.  
**Returns**  
---  
**Type** | **Description**  
`[HiveCatalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveCatalog)` |   
  
### updateHiveCatalog(UpdateHiveCatalogRequest request)
    
    
    public final HiveCatalog updateHiveCatalog(UpdateHiveCatalogRequest request)

Updates an existing catalog.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       UpdateHiveCatalogRequest request =
           UpdateHiveCatalogRequest.newBuilder()
               .setHiveCatalog(HiveCatalog.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       HiveCatalog response = hiveMetastoreServiceClient.updateHiveCatalog(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateHiveCatalogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.UpdateHiveCatalogRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[HiveCatalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveCatalog)` |   
  
### updateHiveCatalogCallable()
    
    
    public final UnaryCallable<UpdateHiveCatalogRequest,HiveCatalog> updateHiveCatalogCallable()

Updates an existing catalog.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       UpdateHiveCatalogRequest request =
           UpdateHiveCatalogRequest.newBuilder()
               .setHiveCatalog(HiveCatalog.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<HiveCatalog> future =
           hiveMetastoreServiceClient.updateHiveCatalogCallable().futureCall(request);
       // Do something.
       HiveCatalog response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateHiveCatalogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.UpdateHiveCatalogRequest),[HiveCatalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveCatalog)>` |   
  
### updateHiveDatabase(HiveDatabase hiveDatabase, FieldMask updateMask)
    
    
    public final HiveDatabase updateHiveDatabase(HiveDatabase hiveDatabase, FieldMask updateMask)

Updates an existing database specified by the database name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       HiveDatabase hiveDatabase = HiveDatabase.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       HiveDatabase response =
           hiveMetastoreServiceClient.updateHiveDatabase(hiveDatabase, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`hiveDatabase` | `[HiveDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveDatabase)`  
Required. The database to update. The database's `name` field is used to identify the database to update. Format: projects/{project_id_or_number}/catalogs/{catalog_id}/databases/{database_id}  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The list of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[HiveDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveDatabase)` |   
  
### updateHiveDatabase(UpdateHiveDatabaseRequest request)
    
    
    public final HiveDatabase updateHiveDatabase(UpdateHiveDatabaseRequest request)

Updates an existing database specified by the database name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       UpdateHiveDatabaseRequest request =
           UpdateHiveDatabaseRequest.newBuilder()
               .setHiveDatabase(HiveDatabase.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       HiveDatabase response = hiveMetastoreServiceClient.updateHiveDatabase(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateHiveDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.UpdateHiveDatabaseRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[HiveDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveDatabase)` |   
  
### updateHiveDatabaseCallable()
    
    
    public final UnaryCallable<UpdateHiveDatabaseRequest,HiveDatabase> updateHiveDatabaseCallable()

Updates an existing database specified by the database name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       UpdateHiveDatabaseRequest request =
           UpdateHiveDatabaseRequest.newBuilder()
               .setHiveDatabase(HiveDatabase.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<HiveDatabase> future =
           hiveMetastoreServiceClient.updateHiveDatabaseCallable().futureCall(request);
       // Do something.
       HiveDatabase response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateHiveDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.UpdateHiveDatabaseRequest),[HiveDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveDatabase)>` |   
  
### updateHiveTable(HiveTable hiveTable, FieldMask updateMask)
    
    
    public final HiveTable updateHiveTable(HiveTable hiveTable, FieldMask updateMask)

Updates an existing table specified by the table name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       HiveTable hiveTable = HiveTable.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       HiveTable response = hiveMetastoreServiceClient.updateHiveTable(hiveTable, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`hiveTable` | `[HiveTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveTable)`  
Required. The table to update. The table's `name` field is used to identify the table to update. Format: projects/{project_id_or_number}/catalogs/{catalog_id}/databases/{database_id}/tables/{table_id}  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The list of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[HiveTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveTable)` |   
  
### updateHiveTable(UpdateHiveTableRequest request)
    
    
    public final HiveTable updateHiveTable(UpdateHiveTableRequest request)

Updates an existing table specified by the table name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       UpdateHiveTableRequest request =
           UpdateHiveTableRequest.newBuilder()
               .setHiveTable(HiveTable.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       HiveTable response = hiveMetastoreServiceClient.updateHiveTable(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateHiveTableRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.UpdateHiveTableRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[HiveTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveTable)` |   
  
### updateHiveTableCallable()
    
    
    public final UnaryCallable<UpdateHiveTableRequest,HiveTable> updateHiveTableCallable()

Updates an existing table specified by the table name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (HiveMetastoreServiceClient hiveMetastoreServiceClient =
         HiveMetastoreServiceClient.create()) {
       UpdateHiveTableRequest request =
           UpdateHiveTableRequest.newBuilder()
               .setHiveTable(HiveTable.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<HiveTable> future =
           hiveMetastoreServiceClient.updateHiveTableCallable().futureCall(request);
       // Do something.
       HiveTable response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateHiveTableRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.UpdateHiveTableRequest),[HiveTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveTable)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
