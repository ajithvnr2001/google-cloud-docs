---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.DataprocMetastoreClient
title: Class DataprocMetastoreClient (2.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:36:35.983974+00:00
---

# Class DataprocMetastoreClient (2.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.DataprocMetastoreClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DataprocMetastoreClient (2.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.100.0 (latest)  2.96.0  2.95.0  2.94.0  2.92.0  2.89.0  2.88.0  2.86.0  2.84.0  2.83.0  2.82.0  2.81.0  2.79.0  2.77.0  2.76.0  2.75.0  2.74.0  2.73.0  2.71.0  2.69.0  2.68.0  2.65.0  2.64.0  2.63.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.4  2.3.0  2.2.0  2.1.9 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-dataproc-metastore/google-cloud-dataproc-metastore/src/main/java/com/google/cloud/metastore/v1/DataprocMetastoreClient.java)| [Product Reference](https://cloud.google.com/dataproc-metastore/docs)| [REST Documentation](https://cloud.google.com/dataproc-metastore/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/dataproc-metastore/docs/reference/rpc)  
---|---|---|---  
  
Service Description: Configures and manages metastore services. Metastore services are fully managed, highly available, autoscaled, autohealing, OSS-native deployments of technical metadata management software. Each metastore service exposes a network endpoint through which metadata queries are served. Metadata queries can originate from a variety of sources, including Apache Hive, Apache Presto, and Apache Spark.

The Dataproc Metastore API defines the following resource model:

  * The service works with a collection of Google Cloud projects, named: `/projects/*`
  * Each project has a collection of available locations, named: `/locations/*` (a location must refer to a Google Cloud `region`) 
  * Each location has a collection of services, named: `/services/*`
  * Dataproc Metastore services are resources with names of the form: 



`/projects/{project_number}/locations/{location_id}/services/{service_id}`.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       ServiceName name = ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]");
       Service response = dataprocMetastoreClient.getService(name);
     }
     

Note: close() needs to be called on the DataprocMetastoreClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListServices |  Lists services in a project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listServices(ListServicesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listServices(LocationName parent) 
  * listServices(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listServicesPagedCallable() 
  * listServicesCallable() 

  
GetService |  Gets the details of a single service. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getService(GetServiceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getService(ServiceName name) 
  * getService(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getServiceCallable() 

  
CreateService |  Creates a metastore service in a project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createServiceAsync(CreateServiceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createServiceAsync(LocationName parent, Service service, String serviceId) 
  * createServiceAsync(String parent, Service service, String serviceId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createServiceOperationCallable() 
  * createServiceCallable() 

  
UpdateService |  Updates the parameters of a single service. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateServiceAsync(UpdateServiceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateServiceAsync(Service service, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateServiceOperationCallable() 
  * updateServiceCallable() 

  
DeleteService |  Deletes a single service. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteServiceAsync(DeleteServiceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteServiceAsync(ServiceName name) 
  * deleteServiceAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteServiceOperationCallable() 
  * deleteServiceCallable() 

  
ListMetadataImports |  Lists imports in a service. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listMetadataImports(ListMetadataImportsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listMetadataImports(ServiceName parent) 
  * listMetadataImports(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listMetadataImportsPagedCallable() 
  * listMetadataImportsCallable() 

  
GetMetadataImport |  Gets details of a single import. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getMetadataImport(GetMetadataImportRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getMetadataImport(MetadataImportName name) 
  * getMetadataImport(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getMetadataImportCallable() 

  
CreateMetadataImport |  Creates a new MetadataImport in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createMetadataImportAsync(CreateMetadataImportRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createMetadataImportAsync(ServiceName parent, MetadataImport metadataImport, String metadataImportId) 
  * createMetadataImportAsync(String parent, MetadataImport metadataImport, String metadataImportId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createMetadataImportOperationCallable() 
  * createMetadataImportCallable() 

  
UpdateMetadataImport |  Updates a single import. Only the description field of MetadataImport is supported to be updated. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateMetadataImportAsync(UpdateMetadataImportRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateMetadataImportAsync(MetadataImport metadataImport, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateMetadataImportOperationCallable() 
  * updateMetadataImportCallable() 

  
ExportMetadata |  Exports metadata from a service. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * exportMetadataAsync(ExportMetadataRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * exportMetadataOperationCallable() 
  * exportMetadataCallable() 

  
RestoreService |  Restores a service from a backup. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * restoreServiceAsync(RestoreServiceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * restoreServiceAsync(ServiceName service, BackupName backup) 
  * restoreServiceAsync(ServiceName service, String backup) 
  * restoreServiceAsync(String service, BackupName backup) 
  * restoreServiceAsync(String service, String backup) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * restoreServiceOperationCallable() 
  * restoreServiceCallable() 

  
ListBackups |  Lists backups in a service. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listBackups(ListBackupsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listBackups(ServiceName parent) 
  * listBackups(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listBackupsPagedCallable() 
  * listBackupsCallable() 

  
GetBackup |  Gets details of a single backup. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getBackup(GetBackupRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getBackup(BackupName name) 
  * getBackup(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getBackupCallable() 

  
CreateBackup |  Creates a new backup in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createBackupAsync(CreateBackupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createBackupAsync(ServiceName parent, Backup backup, String backupId) 
  * createBackupAsync(String parent, Backup backup, String backupId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createBackupOperationCallable() 
  * createBackupCallable() 

  
DeleteBackup |  Deletes a single backup. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteBackupAsync(DeleteBackupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteBackupAsync(BackupName name) 
  * deleteBackupAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteBackupOperationCallable() 
  * deleteBackupCallable() 

  
QueryMetadata |  Query DPMS metadata. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * queryMetadataAsync(QueryMetadataRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * queryMetadataOperationCallable() 
  * queryMetadataCallable() 

  
MoveTableToDatabase |  Move a table to another database. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * moveTableToDatabaseAsync(MoveTableToDatabaseRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * moveTableToDatabaseOperationCallable() 
  * moveTableToDatabaseCallable() 

  
AlterMetadataResourceLocation |  Alter metadata resource location. The metadata resource can be a database, table, or partition. This functionality only updates the parent directory for the respective metadata resource and does not transfer any existing data to the new location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * alterMetadataResourceLocationAsync(AlterMetadataResourceLocationRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * alterMetadataResourceLocationOperationCallable() 
  * alterMetadataResourceLocationCallable() 

  
ListLocations |  Lists information about the supported locations for this service. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listLocations(ListLocationsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listLocationsPagedCallable() 
  * listLocationsCallable() 

  
GetLocation |  Gets information about a location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getLocation(GetLocationRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getLocationCallable() 

  
SetIamPolicy |  Sets the access control policy on the specified resource. Replacesany existing policy.  Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED`errors. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setIamPolicy(SetIamPolicyRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setIamPolicyCallable() 

  
GetIamPolicy |  Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getIamPolicy(GetIamPolicyRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getIamPolicyCallable() 

  
TestIamPermissions |  Returns permissions that a caller has on the specified resource. If theresource does not exist, this will return an empty set ofpermissions, not a `NOT_FOUND` error.  Note: This operation is designed to be used for buildingpermission-aware UIs and command-line tools, not for authorizationchecking. This operation may "fail open" without warning. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * testIamPermissions(TestIamPermissionsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * testIamPermissionsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of DataprocMetastoreSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DataprocMetastoreSettings dataprocMetastoreSettings =
         DataprocMetastoreSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     DataprocMetastoreClient dataprocMetastoreClient =
         DataprocMetastoreClient.create(dataprocMetastoreSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DataprocMetastoreSettings dataprocMetastoreSettings =
         DataprocMetastoreSettings.newBuilder().setEndpoint(myEndpoint).build();
     DataprocMetastoreClient dataprocMetastoreClient =
         DataprocMetastoreClient.create(dataprocMetastoreSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DataprocMetastoreSettings dataprocMetastoreSettings =
         DataprocMetastoreSettings.newHttpJsonBuilder().build();
     DataprocMetastoreClient dataprocMetastoreClient =
         DataprocMetastoreClient.create(dataprocMetastoreSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > DataprocMetastoreClient

## Static Methods 

### create()
    
    
    public static final DataprocMetastoreClient create()

Constructs an instance of DataprocMetastoreClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[DataprocMetastoreClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.DataprocMetastoreClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DataprocMetastoreSettings settings)
    
    
    public static final DataprocMetastoreClient create(DataprocMetastoreSettings settings)

Constructs an instance of DataprocMetastoreClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DataprocMetastoreSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.DataprocMetastoreSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataprocMetastoreClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.DataprocMetastoreClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DataprocMetastoreStub stub)
    
    
    public static final DataprocMetastoreClient create(DataprocMetastoreStub stub)

Constructs an instance of DataprocMetastoreClient, using the given stub for making calls. This is for advanced usage - prefer using create(DataprocMetastoreSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DataprocMetastoreStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.stub.DataprocMetastoreStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataprocMetastoreClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.DataprocMetastoreClient)` |   
  
## Constructors 

### DataprocMetastoreClient(DataprocMetastoreSettings settings)
    
    
    protected DataprocMetastoreClient(DataprocMetastoreSettings settings)

Constructs an instance of DataprocMetastoreClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DataprocMetastoreSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.DataprocMetastoreSettings)`  
  
  
### DataprocMetastoreClient(DataprocMetastoreStub stub)
    
    
    protected DataprocMetastoreClient(DataprocMetastoreStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DataprocMetastoreStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.stub.DataprocMetastoreStub)`  
  
  
## Methods 

### alterMetadataResourceLocationAsync(AlterMetadataResourceLocationRequest request)
    
    
    public final OperationFuture<AlterMetadataResourceLocationResponse,OperationMetadata> alterMetadataResourceLocationAsync(AlterMetadataResourceLocationRequest request)

Alter metadata resource location. The metadata resource can be a database, table, or partition. This functionality only updates the parent directory for the respective metadata resource and does not transfer any existing data to the new location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       AlterMetadataResourceLocationRequest request =
           AlterMetadataResourceLocationRequest.newBuilder()
               .setService(ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString())
               .setResourceName("resourceName-384566343")
               .setLocationUri("locationUri552310135")
               .build();
       AlterMetadataResourceLocationResponse response =
           dataprocMetastoreClient.alterMetadataResourceLocationAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AlterMetadataResourceLocationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.AlterMetadataResourceLocationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AlterMetadataResourceLocationResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.AlterMetadataResourceLocationResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.OperationMetadata)>` |   
  
### alterMetadataResourceLocationCallable()
    
    
    public final UnaryCallable<AlterMetadataResourceLocationRequest,Operation> alterMetadataResourceLocationCallable()

Alter metadata resource location. The metadata resource can be a database, table, or partition. This functionality only updates the parent directory for the respective metadata resource and does not transfer any existing data to the new location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       AlterMetadataResourceLocationRequest request =
           AlterMetadataResourceLocationRequest.newBuilder()
               .setService(ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString())
               .setResourceName("resourceName-384566343")
               .setLocationUri("locationUri552310135")
               .build();
       ApiFuture<Operation> future =
           dataprocMetastoreClient.alterMetadataResourceLocationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AlterMetadataResourceLocationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.AlterMetadataResourceLocationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### alterMetadataResourceLocationOperationCallable()
    
    
    public final OperationCallable<AlterMetadataResourceLocationRequest,AlterMetadataResourceLocationResponse,OperationMetadata> alterMetadataResourceLocationOperationCallable()

Alter metadata resource location. The metadata resource can be a database, table, or partition. This functionality only updates the parent directory for the respective metadata resource and does not transfer any existing data to the new location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       AlterMetadataResourceLocationRequest request =
           AlterMetadataResourceLocationRequest.newBuilder()
               .setService(ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString())
               .setResourceName("resourceName-384566343")
               .setLocationUri("locationUri552310135")
               .build();
       OperationFuture<AlterMetadataResourceLocationResponse, OperationMetadata> future =
           dataprocMetastoreClient
               .alterMetadataResourceLocationOperationCallable()
               .futureCall(request);
       // Do something.
       AlterMetadataResourceLocationResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[AlterMetadataResourceLocationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.AlterMetadataResourceLocationRequest),[AlterMetadataResourceLocationResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.AlterMetadataResourceLocationResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.OperationMetadata)>` |   
  
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
  
### close()
    
    
    public final void close()

### createBackupAsync(@Nullable ServiceName parent, Backup backup, String backupId)
    
    
    public final OperationFuture<Backup,OperationMetadata> createBackupAsync(@Nullable ServiceName parent, Backup backup, String backupId)

Creates a new backup in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       ServiceName parent = ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]");
       Backup backup = Backup.newBuilder().build();
       String backupId = "backupId2121930365";
       Backup response = dataprocMetastoreClient.createBackupAsync(parent, backup, backupId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.metastore.v1.ServiceName`  
Required. The relative resource name of the service in which to create a backup of the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}`.  
`backup` | `[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.Backup)`  
Required. The backup to create. The `name` field is ignored. The ID of the created backup must be provided in the request's `backup_id` field.  
`backupId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID of the backup, which is used as the final component of the backup's name. This value must be between 1 and 64 characters long, begin with a letter, end with a letter or number, and consist of alpha-numeric ASCII characters or hyphens.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.Backup),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.OperationMetadata)>` |   
  
### createBackupAsync(CreateBackupRequest request)
    
    
    public final OperationFuture<Backup,OperationMetadata> createBackupAsync(CreateBackupRequest request)

Creates a new backup in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       CreateBackupRequest request =
           CreateBackupRequest.newBuilder()
               .setParent(ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString())
               .setBackupId("backupId2121930365")
               .setBackup(Backup.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Backup response = dataprocMetastoreClient.createBackupAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.CreateBackupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.Backup),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.OperationMetadata)>` |   
  
### createBackupAsync(String parent, Backup backup, String backupId)
    
    
    public final OperationFuture<Backup,OperationMetadata> createBackupAsync(String parent, Backup backup, String backupId)

Creates a new backup in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       String parent = ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString();
       Backup backup = Backup.newBuilder().build();
       String backupId = "backupId2121930365";
       Backup response = dataprocMetastoreClient.createBackupAsync(parent, backup, backupId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The relative resource name of the service in which to create a backup of the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}`.  
`backup` | `[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.Backup)`  
Required. The backup to create. The `name` field is ignored. The ID of the created backup must be provided in the request's `backup_id` field.  
`backupId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID of the backup, which is used as the final component of the backup's name. This value must be between 1 and 64 characters long, begin with a letter, end with a letter or number, and consist of alpha-numeric ASCII characters or hyphens.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.Backup),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.OperationMetadata)>` |   
  
### createBackupCallable()
    
    
    public final UnaryCallable<CreateBackupRequest,Operation> createBackupCallable()

Creates a new backup in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       CreateBackupRequest request =
           CreateBackupRequest.newBuilder()
               .setParent(ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString())
               .setBackupId("backupId2121930365")
               .setBackup(Backup.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           dataprocMetastoreClient.createBackupCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.CreateBackupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createBackupOperationCallable()
    
    
    public final OperationCallable<CreateBackupRequest,Backup,OperationMetadata> createBackupOperationCallable()

Creates a new backup in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       CreateBackupRequest request =
           CreateBackupRequest.newBuilder()
               .setParent(ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString())
               .setBackupId("backupId2121930365")
               .setBackup(Backup.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Backup, OperationMetadata> future =
           dataprocMetastoreClient.createBackupOperationCallable().futureCall(request);
       // Do something.
       Backup response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.CreateBackupRequest),[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.Backup),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.OperationMetadata)>` |   
  
### createMetadataImportAsync(@Nullable ServiceName parent, MetadataImport metadataImport, String metadataImportId)
    
    
    public final OperationFuture<MetadataImport,OperationMetadata> createMetadataImportAsync(@Nullable ServiceName parent, MetadataImport metadataImport, String metadataImportId)

Creates a new MetadataImport in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       ServiceName parent = ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]");
       MetadataImport metadataImport = MetadataImport.newBuilder().build();
       String metadataImportId = "metadataImportId1824548847";
       MetadataImport response =
           dataprocMetastoreClient
               .createMetadataImportAsync(parent, metadataImport, metadataImportId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.metastore.v1.ServiceName`  
Required. The relative resource name of the service in which to create a metastore import, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}`.  
`metadataImport` | `[MetadataImport](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.MetadataImport)`  
Required. The metadata import to create. The `name` field is ignored. The ID of the created metadata import must be provided in the request's `metadata_import_id` field.  
`metadataImportId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID of the metadata import, which is used as the final component of the metadata import's name. This value must be between 1 and 64 characters long, begin with a letter, end with a letter or number, and consist of alpha-numeric ASCII characters or hyphens.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[MetadataImport](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.MetadataImport),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.OperationMetadata)>` |   
  
### createMetadataImportAsync(CreateMetadataImportRequest request)
    
    
    public final OperationFuture<MetadataImport,OperationMetadata> createMetadataImportAsync(CreateMetadataImportRequest request)

Creates a new MetadataImport in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       CreateMetadataImportRequest request =
           CreateMetadataImportRequest.newBuilder()
               .setParent(ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString())
               .setMetadataImportId("metadataImportId1824548847")
               .setMetadataImport(MetadataImport.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       MetadataImport response = dataprocMetastoreClient.createMetadataImportAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateMetadataImportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.CreateMetadataImportRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[MetadataImport](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.MetadataImport),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.OperationMetadata)>` |   
  
### createMetadataImportAsync(String parent, MetadataImport metadataImport, String metadataImportId)
    
    
    public final OperationFuture<MetadataImport,OperationMetadata> createMetadataImportAsync(String parent, MetadataImport metadataImport, String metadataImportId)

Creates a new MetadataImport in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       String parent = ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString();
       MetadataImport metadataImport = MetadataImport.newBuilder().build();
       String metadataImportId = "metadataImportId1824548847";
       MetadataImport response =
           dataprocMetastoreClient
               .createMetadataImportAsync(parent, metadataImport, metadataImportId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The relative resource name of the service in which to create a metastore import, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}`.  
`metadataImport` | `[MetadataImport](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.MetadataImport)`  
Required. The metadata import to create. The `name` field is ignored. The ID of the created metadata import must be provided in the request's `metadata_import_id` field.  
`metadataImportId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID of the metadata import, which is used as the final component of the metadata import's name. This value must be between 1 and 64 characters long, begin with a letter, end with a letter or number, and consist of alpha-numeric ASCII characters or hyphens.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[MetadataImport](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.MetadataImport),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.OperationMetadata)>` |   
  
### createMetadataImportCallable()
    
    
    public final UnaryCallable<CreateMetadataImportRequest,Operation> createMetadataImportCallable()

Creates a new MetadataImport in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       CreateMetadataImportRequest request =
           CreateMetadataImportRequest.newBuilder()
               .setParent(ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString())
               .setMetadataImportId("metadataImportId1824548847")
               .setMetadataImport(MetadataImport.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           dataprocMetastoreClient.createMetadataImportCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateMetadataImportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.CreateMetadataImportRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createMetadataImportOperationCallable()
    
    
    public final OperationCallable<CreateMetadataImportRequest,MetadataImport,OperationMetadata> createMetadataImportOperationCallable()

Creates a new MetadataImport in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       CreateMetadataImportRequest request =
           CreateMetadataImportRequest.newBuilder()
               .setParent(ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString())
               .setMetadataImportId("metadataImportId1824548847")
               .setMetadataImport(MetadataImport.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<MetadataImport, OperationMetadata> future =
           dataprocMetastoreClient.createMetadataImportOperationCallable().futureCall(request);
       // Do something.
       MetadataImport response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateMetadataImportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.CreateMetadataImportRequest),[MetadataImport](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.MetadataImport),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.OperationMetadata)>` |   
  
### createServiceAsync(@Nullable LocationName parent, Service service, String serviceId)
    
    
    public final OperationFuture<Service,OperationMetadata> createServiceAsync(@Nullable LocationName parent, Service service, String serviceId)

Creates a metastore service in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Service service = Service.newBuilder().build();
       String serviceId = "serviceId-194185552";
       Service response =
           dataprocMetastoreClient.createServiceAsync(parent, service, serviceId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.metastore.v1.LocationName`  
Required. The relative resource name of the location in which to create a metastore service, in the following form: `projects/{project_number}/locations/{location_id}`.  
`service` | `[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.Service)`  
Required. The Metastore service to create. The `name` field is ignored. The ID of the created metastore service must be provided in the request's `service_id` field.  
`serviceId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID of the metastore service, which is used as the final component of the metastore service's name. This value must be between 2 and 63 characters long inclusive, begin with a letter, end with a letter or number, and consist of alpha-numeric ASCII characters or hyphens.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.Service),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.OperationMetadata)>` |   
  
### createServiceAsync(CreateServiceRequest request)
    
    
    public final OperationFuture<Service,OperationMetadata> createServiceAsync(CreateServiceRequest request)

Creates a metastore service in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       CreateServiceRequest request =
           CreateServiceRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setServiceId("serviceId-194185552")
               .setService(Service.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Service response = dataprocMetastoreClient.createServiceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.CreateServiceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.Service),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.OperationMetadata)>` |   
  
### createServiceAsync(String parent, Service service, String serviceId)
    
    
    public final OperationFuture<Service,OperationMetadata> createServiceAsync(String parent, Service service, String serviceId)

Creates a metastore service in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Service service = Service.newBuilder().build();
       String serviceId = "serviceId-194185552";
       Service response =
           dataprocMetastoreClient.createServiceAsync(parent, service, serviceId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The relative resource name of the location in which to create a metastore service, in the following form: `projects/{project_number}/locations/{location_id}`.  
`service` | `[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.Service)`  
Required. The Metastore service to create. The `name` field is ignored. The ID of the created metastore service must be provided in the request's `service_id` field.  
`serviceId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID of the metastore service, which is used as the final component of the metastore service's name. This value must be between 2 and 63 characters long inclusive, begin with a letter, end with a letter or number, and consist of alpha-numeric ASCII characters or hyphens.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.Service),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.OperationMetadata)>` |   
  
### createServiceCallable()
    
    
    public final UnaryCallable<CreateServiceRequest,Operation> createServiceCallable()

Creates a metastore service in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       CreateServiceRequest request =
           CreateServiceRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setServiceId("serviceId-194185552")
               .setService(Service.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           dataprocMetastoreClient.createServiceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.CreateServiceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createServiceOperationCallable()
    
    
    public final OperationCallable<CreateServiceRequest,Service,OperationMetadata> createServiceOperationCallable()

Creates a metastore service in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       CreateServiceRequest request =
           CreateServiceRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setServiceId("serviceId-194185552")
               .setService(Service.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Service, OperationMetadata> future =
           dataprocMetastoreClient.createServiceOperationCallable().futureCall(request);
       // Do something.
       Service response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.CreateServiceRequest),[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.Service),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.OperationMetadata)>` |   
  
### deleteBackupAsync(@Nullable BackupName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteBackupAsync(@Nullable BackupName name)

Deletes a single backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       BackupName name = BackupName.of("[PROJECT]", "[LOCATION]", "[SERVICE]", "[BACKUP]");
       dataprocMetastoreClient.deleteBackupAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.metastore.v1.BackupName`  
Required. The relative resource name of the backup to delete, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}/backups/{backup_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.OperationMetadata)>` |   
  
### deleteBackupAsync(DeleteBackupRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteBackupAsync(DeleteBackupRequest request)

Deletes a single backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       DeleteBackupRequest request =
           DeleteBackupRequest.newBuilder()
               .setName(BackupName.of("[PROJECT]", "[LOCATION]", "[SERVICE]", "[BACKUP]").toString())
               .setRequestId("requestId693933066")
               .build();
       dataprocMetastoreClient.deleteBackupAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.DeleteBackupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.OperationMetadata)>` |   
  
### deleteBackupAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteBackupAsync(String name)

Deletes a single backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       String name = BackupName.of("[PROJECT]", "[LOCATION]", "[SERVICE]", "[BACKUP]").toString();
       dataprocMetastoreClient.deleteBackupAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The relative resource name of the backup to delete, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}/backups/{backup_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.OperationMetadata)>` |   
  
### deleteBackupCallable()
    
    
    public final UnaryCallable<DeleteBackupRequest,Operation> deleteBackupCallable()

Deletes a single backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       DeleteBackupRequest request =
           DeleteBackupRequest.newBuilder()
               .setName(BackupName.of("[PROJECT]", "[LOCATION]", "[SERVICE]", "[BACKUP]").toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           dataprocMetastoreClient.deleteBackupCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.DeleteBackupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteBackupOperationCallable()
    
    
    public final OperationCallable<DeleteBackupRequest,Empty,OperationMetadata> deleteBackupOperationCallable()

Deletes a single backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       DeleteBackupRequest request =
           DeleteBackupRequest.newBuilder()
               .setName(BackupName.of("[PROJECT]", "[LOCATION]", "[SERVICE]", "[BACKUP]").toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           dataprocMetastoreClient.deleteBackupOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.DeleteBackupRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.OperationMetadata)>` |   
  
### deleteServiceAsync(@Nullable ServiceName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteServiceAsync(@Nullable ServiceName name)

Deletes a single service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       ServiceName name = ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]");
       dataprocMetastoreClient.deleteServiceAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.metastore.v1.ServiceName`  
Required. The relative resource name of the metastore service to delete, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.OperationMetadata)>` |   
  
### deleteServiceAsync(DeleteServiceRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteServiceAsync(DeleteServiceRequest request)

Deletes a single service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       DeleteServiceRequest request =
           DeleteServiceRequest.newBuilder()
               .setName(ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString())
               .setRequestId("requestId693933066")
               .build();
       dataprocMetastoreClient.deleteServiceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.DeleteServiceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.OperationMetadata)>` |   
  
### deleteServiceAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteServiceAsync(String name)

Deletes a single service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       String name = ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString();
       dataprocMetastoreClient.deleteServiceAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The relative resource name of the metastore service to delete, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.OperationMetadata)>` |   
  
### deleteServiceCallable()
    
    
    public final UnaryCallable<DeleteServiceRequest,Operation> deleteServiceCallable()

Deletes a single service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       DeleteServiceRequest request =
           DeleteServiceRequest.newBuilder()
               .setName(ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           dataprocMetastoreClient.deleteServiceCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.DeleteServiceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteServiceOperationCallable()
    
    
    public final OperationCallable<DeleteServiceRequest,Empty,OperationMetadata> deleteServiceOperationCallable()

Deletes a single service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       DeleteServiceRequest request =
           DeleteServiceRequest.newBuilder()
               .setName(ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           dataprocMetastoreClient.deleteServiceOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.DeleteServiceRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.OperationMetadata)>` |   
  
### exportMetadataAsync(ExportMetadataRequest request)
    
    
    public final OperationFuture<MetadataExport,OperationMetadata> exportMetadataAsync(ExportMetadataRequest request)

Exports metadata from a service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       ExportMetadataRequest request =
           ExportMetadataRequest.newBuilder()
               .setService(ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString())
               .setRequestId("requestId693933066")
               .build();
       MetadataExport response = dataprocMetastoreClient.exportMetadataAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ExportMetadataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.ExportMetadataRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[MetadataExport](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.MetadataExport),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.OperationMetadata)>` |   
  
### exportMetadataCallable()
    
    
    public final UnaryCallable<ExportMetadataRequest,Operation> exportMetadataCallable()

Exports metadata from a service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       ExportMetadataRequest request =
           ExportMetadataRequest.newBuilder()
               .setService(ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           dataprocMetastoreClient.exportMetadataCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ExportMetadataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.ExportMetadataRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### exportMetadataOperationCallable()
    
    
    public final OperationCallable<ExportMetadataRequest,MetadataExport,OperationMetadata> exportMetadataOperationCallable()

Exports metadata from a service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       ExportMetadataRequest request =
           ExportMetadataRequest.newBuilder()
               .setService(ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<MetadataExport, OperationMetadata> future =
           dataprocMetastoreClient.exportMetadataOperationCallable().futureCall(request);
       // Do something.
       MetadataExport response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ExportMetadataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.ExportMetadataRequest),[MetadataExport](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.MetadataExport),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.OperationMetadata)>` |   
  
### getBackup(@Nullable BackupName name)
    
    
    public final Backup getBackup(@Nullable BackupName name)

Gets details of a single backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       BackupName name = BackupName.of("[PROJECT]", "[LOCATION]", "[SERVICE]", "[BACKUP]");
       Backup response = dataprocMetastoreClient.getBackup(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.metastore.v1.BackupName`  
Required. The relative resource name of the backup to retrieve, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}/backups/{backup_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.Backup)` |   
  
### getBackup(GetBackupRequest request)
    
    
    public final Backup getBackup(GetBackupRequest request)

Gets details of a single backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       GetBackupRequest request =
           GetBackupRequest.newBuilder()
               .setName(BackupName.of("[PROJECT]", "[LOCATION]", "[SERVICE]", "[BACKUP]").toString())
               .build();
       Backup response = dataprocMetastoreClient.getBackup(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.GetBackupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.Backup)` |   
  
### getBackup(String name)
    
    
    public final Backup getBackup(String name)

Gets details of a single backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       String name = BackupName.of("[PROJECT]", "[LOCATION]", "[SERVICE]", "[BACKUP]").toString();
       Backup response = dataprocMetastoreClient.getBackup(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The relative resource name of the backup to retrieve, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}/backups/{backup_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.Backup)` |   
  
### getBackupCallable()
    
    
    public final UnaryCallable<GetBackupRequest,Backup> getBackupCallable()

Gets details of a single backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       GetBackupRequest request =
           GetBackupRequest.newBuilder()
               .setName(BackupName.of("[PROJECT]", "[LOCATION]", "[SERVICE]", "[BACKUP]").toString())
               .build();
       ApiFuture<Backup> future = dataprocMetastoreClient.getBackupCallable().futureCall(request);
       // Do something.
       Backup response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.GetBackupRequest),[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.Backup)>` |   
  
### getHttpJsonOperationsClient()
    
    
    public final OperationsClient getHttpJsonOperationsClient()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.OperationsClient.html)` |   
  
### getIamPolicy(GetIamPolicyRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyRequest request)

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   BackupName.of("[PROJECT]", "[LOCATION]", "[SERVICE]", "[BACKUP]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = dataprocMetastoreClient.getIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.GetIamPolicyRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.Policy` |   
  
### getIamPolicyCallable()
    
    
    public final UnaryCallable<GetIamPolicyRequest,Policy> getIamPolicyCallable()

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   BackupName.of("[PROJECT]", "[LOCATION]", "[SERVICE]", "[BACKUP]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future = dataprocMetastoreClient.getIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.GetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = dataprocMetastoreClient.getLocation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.cloud.location.GetLocationRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.cloud.location.Location` |   
  
### getLocationCallable()
    
    
    public final UnaryCallable<GetLocationRequest,Location> getLocationCallable()

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future =
           dataprocMetastoreClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getMetadataImport(@Nullable MetadataImportName name)
    
    
    public final MetadataImport getMetadataImport(@Nullable MetadataImportName name)

Gets details of a single import.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       MetadataImportName name =
           MetadataImportName.of("[PROJECT]", "[LOCATION]", "[SERVICE]", "[METADATA_IMPORT]");
       MetadataImport response = dataprocMetastoreClient.getMetadataImport(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.metastore.v1.MetadataImportName`  
Required. The relative resource name of the metadata import to retrieve, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}/metadataImports/{import_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[MetadataImport](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.MetadataImport)` |   
  
### getMetadataImport(GetMetadataImportRequest request)
    
    
    public final MetadataImport getMetadataImport(GetMetadataImportRequest request)

Gets details of a single import.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       GetMetadataImportRequest request =
           GetMetadataImportRequest.newBuilder()
               .setName(
                   MetadataImportName.of("[PROJECT]", "[LOCATION]", "[SERVICE]", "[METADATA_IMPORT]")
                       .toString())
               .build();
       MetadataImport response = dataprocMetastoreClient.getMetadataImport(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetMetadataImportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.GetMetadataImportRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[MetadataImport](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.MetadataImport)` |   
  
### getMetadataImport(String name)
    
    
    public final MetadataImport getMetadataImport(String name)

Gets details of a single import.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       String name =
           MetadataImportName.of("[PROJECT]", "[LOCATION]", "[SERVICE]", "[METADATA_IMPORT]")
               .toString();
       MetadataImport response = dataprocMetastoreClient.getMetadataImport(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The relative resource name of the metadata import to retrieve, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}/metadataImports/{import_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[MetadataImport](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.MetadataImport)` |   
  
### getMetadataImportCallable()
    
    
    public final UnaryCallable<GetMetadataImportRequest,MetadataImport> getMetadataImportCallable()

Gets details of a single import.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       GetMetadataImportRequest request =
           GetMetadataImportRequest.newBuilder()
               .setName(
                   MetadataImportName.of("[PROJECT]", "[LOCATION]", "[SERVICE]", "[METADATA_IMPORT]")
                       .toString())
               .build();
       ApiFuture<MetadataImport> future =
           dataprocMetastoreClient.getMetadataImportCallable().futureCall(request);
       // Do something.
       MetadataImport response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetMetadataImportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.GetMetadataImportRequest),[MetadataImport](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.MetadataImport)>` |   
  
### getOperationsClient()
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getService(@Nullable ServiceName name)
    
    
    public final Service getService(@Nullable ServiceName name)

Gets the details of a single service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       ServiceName name = ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]");
       Service response = dataprocMetastoreClient.getService(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.metastore.v1.ServiceName`  
Required. The relative resource name of the metastore service to retrieve, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.Service)` |   
  
### getService(GetServiceRequest request)
    
    
    public final Service getService(GetServiceRequest request)

Gets the details of a single service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       GetServiceRequest request =
           GetServiceRequest.newBuilder()
               .setName(ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString())
               .build();
       Service response = dataprocMetastoreClient.getService(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.GetServiceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.Service)` |   
  
### getService(String name)
    
    
    public final Service getService(String name)

Gets the details of a single service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       String name = ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString();
       Service response = dataprocMetastoreClient.getService(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The relative resource name of the metastore service to retrieve, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.Service)` |   
  
### getServiceCallable()
    
    
    public final UnaryCallable<GetServiceRequest,Service> getServiceCallable()

Gets the details of a single service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       GetServiceRequest request =
           GetServiceRequest.newBuilder()
               .setName(ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString())
               .build();
       ApiFuture<Service> future = dataprocMetastoreClient.getServiceCallable().futureCall(request);
       // Do something.
       Service response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.GetServiceRequest),[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.Service)>` |   
  
### getSettings()
    
    
    public final @Nullable DataprocMetastoreSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.metastore.v1.DataprocMetastoreSettings` |   
  
### getStub()
    
    
    public DataprocMetastoreStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[DataprocMetastoreStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.stub.DataprocMetastoreStub)` |   
  
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
  
### listBackups(@Nullable ServiceName parent)
    
    
    public final DataprocMetastoreClient.ListBackupsPagedResponse listBackups(@Nullable ServiceName parent)

Lists backups in a service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       ServiceName parent = ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]");
       for (Backup element : dataprocMetastoreClient.listBackups(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.metastore.v1.ServiceName`  
Required. The relative resource name of the service whose backups to list, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}/backups`.  
**Returns**  
---  
**Type** | **Description**  
`[DataprocMetastoreClient.ListBackupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.DataprocMetastoreClient.ListBackupsPagedResponse)` |   
  
### listBackups(ListBackupsRequest request)
    
    
    public final DataprocMetastoreClient.ListBackupsPagedResponse listBackups(ListBackupsRequest request)

Lists backups in a service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       ListBackupsRequest request =
           ListBackupsRequest.newBuilder()
               .setParent(ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Backup element : dataprocMetastoreClient.listBackups(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListBackupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.ListBackupsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataprocMetastoreClient.ListBackupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.DataprocMetastoreClient.ListBackupsPagedResponse)` |   
  
### listBackups(String parent)
    
    
    public final DataprocMetastoreClient.ListBackupsPagedResponse listBackups(String parent)

Lists backups in a service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       String parent = ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString();
       for (Backup element : dataprocMetastoreClient.listBackups(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The relative resource name of the service whose backups to list, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}/backups`.  
**Returns**  
---  
**Type** | **Description**  
`[DataprocMetastoreClient.ListBackupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.DataprocMetastoreClient.ListBackupsPagedResponse)` |   
  
### listBackupsCallable()
    
    
    public final UnaryCallable<ListBackupsRequest,ListBackupsResponse> listBackupsCallable()

Lists backups in a service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       ListBackupsRequest request =
           ListBackupsRequest.newBuilder()
               .setParent(ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListBackupsResponse response = dataprocMetastoreClient.listBackupsCallable().call(request);
         for (Backup element : response.getBackupsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListBackupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.ListBackupsRequest),[ListBackupsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.ListBackupsResponse)>` |   
  
### listBackupsPagedCallable()
    
    
    public final UnaryCallable<ListBackupsRequest,DataprocMetastoreClient.ListBackupsPagedResponse> listBackupsPagedCallable()

Lists backups in a service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       ListBackupsRequest request =
           ListBackupsRequest.newBuilder()
               .setParent(ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Backup> future =
           dataprocMetastoreClient.listBackupsPagedCallable().futureCall(request);
       // Do something.
       for (Backup element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListBackupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.ListBackupsRequest),[ListBackupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.DataprocMetastoreClient.ListBackupsPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final DataprocMetastoreClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : dataprocMetastoreClient.listLocations(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.cloud.location.ListLocationsRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataprocMetastoreClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.DataprocMetastoreClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             dataprocMetastoreClient.listLocationsCallable().call(request);
         for (Location element : response.getLocationsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,com.google.cloud.location.ListLocationsResponse>` |   
  
### listLocationsPagedCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,DataprocMetastoreClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           dataprocMetastoreClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.DataprocMetastoreClient.ListLocationsPagedResponse)>` |   
  
### listMetadataImports(@Nullable ServiceName parent)
    
    
    public final DataprocMetastoreClient.ListMetadataImportsPagedResponse listMetadataImports(@Nullable ServiceName parent)

Lists imports in a service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       ServiceName parent = ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]");
       for (MetadataImport element :
           dataprocMetastoreClient.listMetadataImports(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.metastore.v1.ServiceName`  
Required. The relative resource name of the service whose metadata imports to list, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}/metadataImports`.  
**Returns**  
---  
**Type** | **Description**  
`[DataprocMetastoreClient.ListMetadataImportsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.DataprocMetastoreClient.ListMetadataImportsPagedResponse)` |   
  
### listMetadataImports(ListMetadataImportsRequest request)
    
    
    public final DataprocMetastoreClient.ListMetadataImportsPagedResponse listMetadataImports(ListMetadataImportsRequest request)

Lists imports in a service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       ListMetadataImportsRequest request =
           ListMetadataImportsRequest.newBuilder()
               .setParent(ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (MetadataImport element :
           dataprocMetastoreClient.listMetadataImports(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListMetadataImportsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.ListMetadataImportsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataprocMetastoreClient.ListMetadataImportsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.DataprocMetastoreClient.ListMetadataImportsPagedResponse)` |   
  
### listMetadataImports(String parent)
    
    
    public final DataprocMetastoreClient.ListMetadataImportsPagedResponse listMetadataImports(String parent)

Lists imports in a service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       String parent = ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString();
       for (MetadataImport element :
           dataprocMetastoreClient.listMetadataImports(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The relative resource name of the service whose metadata imports to list, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}/metadataImports`.  
**Returns**  
---  
**Type** | **Description**  
`[DataprocMetastoreClient.ListMetadataImportsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.DataprocMetastoreClient.ListMetadataImportsPagedResponse)` |   
  
### listMetadataImportsCallable()
    
    
    public final UnaryCallable<ListMetadataImportsRequest,ListMetadataImportsResponse> listMetadataImportsCallable()

Lists imports in a service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       ListMetadataImportsRequest request =
           ListMetadataImportsRequest.newBuilder()
               .setParent(ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListMetadataImportsResponse response =
             dataprocMetastoreClient.listMetadataImportsCallable().call(request);
         for (MetadataImport element : response.getMetadataImportsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMetadataImportsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.ListMetadataImportsRequest),[ListMetadataImportsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.ListMetadataImportsResponse)>` |   
  
### listMetadataImportsPagedCallable()
    
    
    public final UnaryCallable<ListMetadataImportsRequest,DataprocMetastoreClient.ListMetadataImportsPagedResponse> listMetadataImportsPagedCallable()

Lists imports in a service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       ListMetadataImportsRequest request =
           ListMetadataImportsRequest.newBuilder()
               .setParent(ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<MetadataImport> future =
           dataprocMetastoreClient.listMetadataImportsPagedCallable().futureCall(request);
       // Do something.
       for (MetadataImport element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMetadataImportsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.ListMetadataImportsRequest),[ListMetadataImportsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.DataprocMetastoreClient.ListMetadataImportsPagedResponse)>` |   
  
### listServices(@Nullable LocationName parent)
    
    
    public final DataprocMetastoreClient.ListServicesPagedResponse listServices(@Nullable LocationName parent)

Lists services in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Service element : dataprocMetastoreClient.listServices(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.metastore.v1.LocationName`  
Required. The relative resource name of the location of metastore services to list, in the following form: `projects/{project_number}/locations/{location_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[DataprocMetastoreClient.ListServicesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.DataprocMetastoreClient.ListServicesPagedResponse)` |   
  
### listServices(ListServicesRequest request)
    
    
    public final DataprocMetastoreClient.ListServicesPagedResponse listServices(ListServicesRequest request)

Lists services in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       ListServicesRequest request =
           ListServicesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Service element : dataprocMetastoreClient.listServices(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListServicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.ListServicesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataprocMetastoreClient.ListServicesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.DataprocMetastoreClient.ListServicesPagedResponse)` |   
  
### listServices(String parent)
    
    
    public final DataprocMetastoreClient.ListServicesPagedResponse listServices(String parent)

Lists services in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Service element : dataprocMetastoreClient.listServices(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The relative resource name of the location of metastore services to list, in the following form: `projects/{project_number}/locations/{location_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[DataprocMetastoreClient.ListServicesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.DataprocMetastoreClient.ListServicesPagedResponse)` |   
  
### listServicesCallable()
    
    
    public final UnaryCallable<ListServicesRequest,ListServicesResponse> listServicesCallable()

Lists services in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       ListServicesRequest request =
           ListServicesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListServicesResponse response =
             dataprocMetastoreClient.listServicesCallable().call(request);
         for (Service element : response.getServicesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListServicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.ListServicesRequest),[ListServicesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.ListServicesResponse)>` |   
  
### listServicesPagedCallable()
    
    
    public final UnaryCallable<ListServicesRequest,DataprocMetastoreClient.ListServicesPagedResponse> listServicesPagedCallable()

Lists services in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       ListServicesRequest request =
           ListServicesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Service> future =
           dataprocMetastoreClient.listServicesPagedCallable().futureCall(request);
       // Do something.
       for (Service element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListServicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.ListServicesRequest),[ListServicesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.DataprocMetastoreClient.ListServicesPagedResponse)>` |   
  
### moveTableToDatabaseAsync(MoveTableToDatabaseRequest request)
    
    
    public final OperationFuture<MoveTableToDatabaseResponse,OperationMetadata> moveTableToDatabaseAsync(MoveTableToDatabaseRequest request)

Move a table to another database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       MoveTableToDatabaseRequest request =
           MoveTableToDatabaseRequest.newBuilder()
               .setService(ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString())
               .setTableName("tableName-1988717703")
               .setDbName("dbName-1339126743")
               .setDestinationDbName("destinationDbName-2077361705")
               .build();
       MoveTableToDatabaseResponse response =
           dataprocMetastoreClient.moveTableToDatabaseAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[MoveTableToDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.MoveTableToDatabaseRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[MoveTableToDatabaseResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.MoveTableToDatabaseResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.OperationMetadata)>` |   
  
### moveTableToDatabaseCallable()
    
    
    public final UnaryCallable<MoveTableToDatabaseRequest,Operation> moveTableToDatabaseCallable()

Move a table to another database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       MoveTableToDatabaseRequest request =
           MoveTableToDatabaseRequest.newBuilder()
               .setService(ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString())
               .setTableName("tableName-1988717703")
               .setDbName("dbName-1339126743")
               .setDestinationDbName("destinationDbName-2077361705")
               .build();
       ApiFuture<Operation> future =
           dataprocMetastoreClient.moveTableToDatabaseCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[MoveTableToDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.MoveTableToDatabaseRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### moveTableToDatabaseOperationCallable()
    
    
    public final OperationCallable<MoveTableToDatabaseRequest,MoveTableToDatabaseResponse,OperationMetadata> moveTableToDatabaseOperationCallable()

Move a table to another database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       MoveTableToDatabaseRequest request =
           MoveTableToDatabaseRequest.newBuilder()
               .setService(ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString())
               .setTableName("tableName-1988717703")
               .setDbName("dbName-1339126743")
               .setDestinationDbName("destinationDbName-2077361705")
               .build();
       OperationFuture<MoveTableToDatabaseResponse, OperationMetadata> future =
           dataprocMetastoreClient.moveTableToDatabaseOperationCallable().futureCall(request);
       // Do something.
       MoveTableToDatabaseResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[MoveTableToDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.MoveTableToDatabaseRequest),[MoveTableToDatabaseResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.MoveTableToDatabaseResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.OperationMetadata)>` |   
  
### queryMetadataAsync(QueryMetadataRequest request)
    
    
    public final OperationFuture<QueryMetadataResponse,OperationMetadata> queryMetadataAsync(QueryMetadataRequest request)

Query DPMS metadata.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       QueryMetadataRequest request =
           QueryMetadataRequest.newBuilder()
               .setService(ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString())
               .setQuery("query107944136")
               .build();
       QueryMetadataResponse response = dataprocMetastoreClient.queryMetadataAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[QueryMetadataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.QueryMetadataRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[QueryMetadataResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.QueryMetadataResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.OperationMetadata)>` |   
  
### queryMetadataCallable()
    
    
    public final UnaryCallable<QueryMetadataRequest,Operation> queryMetadataCallable()

Query DPMS metadata.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       QueryMetadataRequest request =
           QueryMetadataRequest.newBuilder()
               .setService(ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString())
               .setQuery("query107944136")
               .build();
       ApiFuture<Operation> future =
           dataprocMetastoreClient.queryMetadataCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[QueryMetadataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.QueryMetadataRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### queryMetadataOperationCallable()
    
    
    public final OperationCallable<QueryMetadataRequest,QueryMetadataResponse,OperationMetadata> queryMetadataOperationCallable()

Query DPMS metadata.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       QueryMetadataRequest request =
           QueryMetadataRequest.newBuilder()
               .setService(ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString())
               .setQuery("query107944136")
               .build();
       OperationFuture<QueryMetadataResponse, OperationMetadata> future =
           dataprocMetastoreClient.queryMetadataOperationCallable().futureCall(request);
       // Do something.
       QueryMetadataResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[QueryMetadataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.QueryMetadataRequest),[QueryMetadataResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.QueryMetadataResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.OperationMetadata)>` |   
  
### restoreServiceAsync(@Nullable ServiceName service, @Nullable BackupName backup)
    
    
    public final OperationFuture<Restore,OperationMetadata> restoreServiceAsync(@Nullable ServiceName service, @Nullable BackupName backup)

Restores a service from a backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       ServiceName service = ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]");
       BackupName backup = BackupName.of("[PROJECT]", "[LOCATION]", "[SERVICE]", "[BACKUP]");
       Restore response = dataprocMetastoreClient.restoreServiceAsync(service, backup).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`service` | `@org.jspecify.annotations.Nullable com.google.cloud.metastore.v1.ServiceName`  
Required. The relative resource name of the metastore service to run restore, in the following form: `projects/{project_id}/locations/{location_id}/services/{service_id}`.  
`backup` | `@org.jspecify.annotations.Nullable com.google.cloud.metastore.v1.BackupName`  
Required. The relative resource name of the metastore service backup to restore from, in the following form: `projects/{project_id}/locations/{location_id}/services/{service_id}/backups/{backup_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Restore](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.Restore),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.OperationMetadata)>` |   
  
### restoreServiceAsync(@Nullable ServiceName service, String backup)
    
    
    public final OperationFuture<Restore,OperationMetadata> restoreServiceAsync(@Nullable ServiceName service, String backup)

Restores a service from a backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       ServiceName service = ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]");
       String backup = BackupName.of("[PROJECT]", "[LOCATION]", "[SERVICE]", "[BACKUP]").toString();
       Restore response = dataprocMetastoreClient.restoreServiceAsync(service, backup).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`service` | `@org.jspecify.annotations.Nullable com.google.cloud.metastore.v1.ServiceName`  
Required. The relative resource name of the metastore service to run restore, in the following form: `projects/{project_id}/locations/{location_id}/services/{service_id}`.  
`backup` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The relative resource name of the metastore service backup to restore from, in the following form: `projects/{project_id}/locations/{location_id}/services/{service_id}/backups/{backup_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Restore](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.Restore),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.OperationMetadata)>` |   
  
### restoreServiceAsync(RestoreServiceRequest request)
    
    
    public final OperationFuture<Restore,OperationMetadata> restoreServiceAsync(RestoreServiceRequest request)

Restores a service from a backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       RestoreServiceRequest request =
           RestoreServiceRequest.newBuilder()
               .setService(ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString())
               .setBackup(
                   BackupName.of("[PROJECT]", "[LOCATION]", "[SERVICE]", "[BACKUP]").toString())
               .setRequestId("requestId693933066")
               .build();
       Restore response = dataprocMetastoreClient.restoreServiceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RestoreServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.RestoreServiceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Restore](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.Restore),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.OperationMetadata)>` |   
  
### restoreServiceAsync(String service, @Nullable BackupName backup)
    
    
    public final OperationFuture<Restore,OperationMetadata> restoreServiceAsync(String service, @Nullable BackupName backup)

Restores a service from a backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       String service = ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString();
       BackupName backup = BackupName.of("[PROJECT]", "[LOCATION]", "[SERVICE]", "[BACKUP]");
       Restore response = dataprocMetastoreClient.restoreServiceAsync(service, backup).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`service` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The relative resource name of the metastore service to run restore, in the following form: `projects/{project_id}/locations/{location_id}/services/{service_id}`.  
`backup` | `@org.jspecify.annotations.Nullable com.google.cloud.metastore.v1.BackupName`  
Required. The relative resource name of the metastore service backup to restore from, in the following form: `projects/{project_id}/locations/{location_id}/services/{service_id}/backups/{backup_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Restore](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.Restore),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.OperationMetadata)>` |   
  
### restoreServiceAsync(String service, String backup)
    
    
    public final OperationFuture<Restore,OperationMetadata> restoreServiceAsync(String service, String backup)

Restores a service from a backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       String service = ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString();
       String backup = BackupName.of("[PROJECT]", "[LOCATION]", "[SERVICE]", "[BACKUP]").toString();
       Restore response = dataprocMetastoreClient.restoreServiceAsync(service, backup).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`service` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The relative resource name of the metastore service to run restore, in the following form: `projects/{project_id}/locations/{location_id}/services/{service_id}`.  
`backup` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The relative resource name of the metastore service backup to restore from, in the following form: `projects/{project_id}/locations/{location_id}/services/{service_id}/backups/{backup_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Restore](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.Restore),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.OperationMetadata)>` |   
  
### restoreServiceCallable()
    
    
    public final UnaryCallable<RestoreServiceRequest,Operation> restoreServiceCallable()

Restores a service from a backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       RestoreServiceRequest request =
           RestoreServiceRequest.newBuilder()
               .setService(ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString())
               .setBackup(
                   BackupName.of("[PROJECT]", "[LOCATION]", "[SERVICE]", "[BACKUP]").toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           dataprocMetastoreClient.restoreServiceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RestoreServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.RestoreServiceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### restoreServiceOperationCallable()
    
    
    public final OperationCallable<RestoreServiceRequest,Restore,OperationMetadata> restoreServiceOperationCallable()

Restores a service from a backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       RestoreServiceRequest request =
           RestoreServiceRequest.newBuilder()
               .setService(ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString())
               .setBackup(
                   BackupName.of("[PROJECT]", "[LOCATION]", "[SERVICE]", "[BACKUP]").toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Restore, OperationMetadata> future =
           dataprocMetastoreClient.restoreServiceOperationCallable().futureCall(request);
       // Do something.
       Restore response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RestoreServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.RestoreServiceRequest),[Restore](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.Restore),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.OperationMetadata)>` |   
  
### setIamPolicy(SetIamPolicyRequest request)
    
    
    public final Policy setIamPolicy(SetIamPolicyRequest request)

Sets the access control policy on the specified resource. Replacesany existing policy.

Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED`errors.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   BackupName.of("[PROJECT]", "[LOCATION]", "[SERVICE]", "[BACKUP]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = dataprocMetastoreClient.setIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.SetIamPolicyRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.Policy` |   
  
### setIamPolicyCallable()
    
    
    public final UnaryCallable<SetIamPolicyRequest,Policy> setIamPolicyCallable()

Sets the access control policy on the specified resource. Replacesany existing policy.

Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED`errors.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   BackupName.of("[PROJECT]", "[LOCATION]", "[SERVICE]", "[BACKUP]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Policy> future = dataprocMetastoreClient.setIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.SetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### testIamPermissions(TestIamPermissionsRequest request)
    
    
    public final TestIamPermissionsResponse testIamPermissions(TestIamPermissionsRequest request)

Returns permissions that a caller has on the specified resource. If theresource does not exist, this will return an empty set ofpermissions, not a `NOT_FOUND` error.

Note: This operation is designed to be used for buildingpermission-aware UIs and command-line tools, not for authorizationchecking. This operation may "fail open" without warning.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(FederationName.of("[PROJECT]", "[LOCATION]", "[FEDERATION]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response = dataprocMetastoreClient.testIamPermissions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.TestIamPermissionsRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.TestIamPermissionsResponse` |   
  
### testIamPermissionsCallable()
    
    
    public final UnaryCallable<TestIamPermissionsRequest,TestIamPermissionsResponse> testIamPermissionsCallable()

Returns permissions that a caller has on the specified resource. If theresource does not exist, this will return an empty set ofpermissions, not a `NOT_FOUND` error.

Note: This operation is designed to be used for buildingpermission-aware UIs and command-line tools, not for authorizationchecking. This operation may "fail open" without warning.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(FederationName.of("[PROJECT]", "[LOCATION]", "[FEDERATION]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           dataprocMetastoreClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestIamPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### updateMetadataImportAsync(MetadataImport metadataImport, FieldMask updateMask)
    
    
    public final OperationFuture<MetadataImport,OperationMetadata> updateMetadataImportAsync(MetadataImport metadataImport, FieldMask updateMask)

Updates a single import. Only the description field of MetadataImport is supported to be updated.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       MetadataImport metadataImport = MetadataImport.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       MetadataImport response =
           dataprocMetastoreClient.updateMetadataImportAsync(metadataImport, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`metadataImport` | `[MetadataImport](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.MetadataImport)`  
Required. The metadata import to update. The server only merges fields in the import if they are specified in `update_mask`. The metadata import's `name` field is used to identify the metastore import to be updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. A field mask used to specify the fields to be overwritten in the metadata import resource by the update. Fields specified in the `update_mask` are relative to the resource (not to the full request). A field is overwritten if it is in the mask.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[MetadataImport](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.MetadataImport),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.OperationMetadata)>` |   
  
### updateMetadataImportAsync(UpdateMetadataImportRequest request)
    
    
    public final OperationFuture<MetadataImport,OperationMetadata> updateMetadataImportAsync(UpdateMetadataImportRequest request)

Updates a single import. Only the description field of MetadataImport is supported to be updated.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       UpdateMetadataImportRequest request =
           UpdateMetadataImportRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setMetadataImport(MetadataImport.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       MetadataImport response = dataprocMetastoreClient.updateMetadataImportAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateMetadataImportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.UpdateMetadataImportRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[MetadataImport](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.MetadataImport),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.OperationMetadata)>` |   
  
### updateMetadataImportCallable()
    
    
    public final UnaryCallable<UpdateMetadataImportRequest,Operation> updateMetadataImportCallable()

Updates a single import. Only the description field of MetadataImport is supported to be updated.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       UpdateMetadataImportRequest request =
           UpdateMetadataImportRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setMetadataImport(MetadataImport.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           dataprocMetastoreClient.updateMetadataImportCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateMetadataImportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.UpdateMetadataImportRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateMetadataImportOperationCallable()
    
    
    public final OperationCallable<UpdateMetadataImportRequest,MetadataImport,OperationMetadata> updateMetadataImportOperationCallable()

Updates a single import. Only the description field of MetadataImport is supported to be updated.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       UpdateMetadataImportRequest request =
           UpdateMetadataImportRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setMetadataImport(MetadataImport.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<MetadataImport, OperationMetadata> future =
           dataprocMetastoreClient.updateMetadataImportOperationCallable().futureCall(request);
       // Do something.
       MetadataImport response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateMetadataImportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.UpdateMetadataImportRequest),[MetadataImport](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.MetadataImport),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.OperationMetadata)>` |   
  
### updateServiceAsync(Service service, FieldMask updateMask)
    
    
    public final OperationFuture<Service,OperationMetadata> updateServiceAsync(Service service, FieldMask updateMask)

Updates the parameters of a single service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       Service service = Service.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Service response = dataprocMetastoreClient.updateServiceAsync(service, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`service` | `[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.Service)`  
Required. The metastore service to update. The server only merges fields in the service if they are specified in `update_mask`. The metastore service's `name` field is used to identify the metastore service to be updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. A field mask used to specify the fields to be overwritten in the metastore service resource by the update. Fields specified in the `update_mask` are relative to the resource (not to the full request). A field is overwritten if it is in the mask.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.Service),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.OperationMetadata)>` |   
  
### updateServiceAsync(UpdateServiceRequest request)
    
    
    public final OperationFuture<Service,OperationMetadata> updateServiceAsync(UpdateServiceRequest request)

Updates the parameters of a single service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       UpdateServiceRequest request =
           UpdateServiceRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setService(Service.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Service response = dataprocMetastoreClient.updateServiceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.UpdateServiceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.Service),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.OperationMetadata)>` |   
  
### updateServiceCallable()
    
    
    public final UnaryCallable<UpdateServiceRequest,Operation> updateServiceCallable()

Updates the parameters of a single service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       UpdateServiceRequest request =
           UpdateServiceRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setService(Service.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           dataprocMetastoreClient.updateServiceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.UpdateServiceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateServiceOperationCallable()
    
    
    public final OperationCallable<UpdateServiceRequest,Service,OperationMetadata> updateServiceOperationCallable()

Updates the parameters of a single service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataprocMetastoreClient dataprocMetastoreClient = DataprocMetastoreClient.create()) {
       UpdateServiceRequest request =
           UpdateServiceRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setService(Service.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Service, OperationMetadata> future =
           dataprocMetastoreClient.updateServiceOperationCallable().futureCall(request);
       // Do something.
       Service response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.UpdateServiceRequest),[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.Service),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1.OperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
